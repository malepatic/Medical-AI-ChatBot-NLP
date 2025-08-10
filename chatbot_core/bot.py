import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer, util
import os
import re
from collections import defaultdict, deque

class MedicalChatbot:
    def __init__(self, generative_model_path: str, classifier_model_path: str, db_path: str):
        print("Initializing Enhanced RAG chatbot system for Web App...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # --- Enhanced Emergency Detection ---
        self.emergency_keywords = [
            "severe chest pain", "chest pain", "heart attack", "crushing chest pain",
            "can't breathe", "trouble breathing", "difficulty breathing", "choking",
            "suicidal", "kill myself", "end my life", "suicide",
            "unconscious", "passed out", "unresponsive",
            "stroke", "slurred speech", "facial drooping", "sudden weakness",
            "seizure", "convulsions", "shaking uncontrollably",
            "uncontrollable bleeding", "bleeding heavily", "blood everywhere",
            "numbness on one side", "can't move one side", "paralyzed",
            "severe abdominal pain", "excruciating pain", "worst pain ever",
            "high fever", "fever over 103", "temperature over 103"
        ]

        # --- Load all models ---
        print("Loading intent classifier...")
        self.intent_tokenizer = AutoTokenizer.from_pretrained(classifier_model_path, local_files_only=True)
        self.intent_model = AutoModelForSequenceClassification.from_pretrained(classifier_model_path, local_files_only=True).to(self.device)
        
        print("Loading generative model...")
        self.gen_tokenizer = AutoTokenizer.from_pretrained(generative_model_path, local_files_only=True)
        self.gen_model = AutoModelForSeq2SeqLM.from_pretrained(generative_model_path, local_files_only=True).to(self.device)
        
        print("Loading medical text retriever...")
        self.retriever_model = SentenceTransformer('microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext', device=self.device)
        
        # --- Load and index knowledge base ---
        print("Loading and indexing medical knowledge base...")
        self.db = pd.read_csv(db_path).dropna()
        
        print("Computing medical text embeddings...")
        self.db_embeddings = self.retriever_model.encode(
            self.db['completion'].tolist(), 
            convert_to_tensor=True, 
            device=self.device,
            show_progress_bar=True,
            batch_size=32
        )
        
        self.histories = defaultdict(lambda: deque(maxlen=6))  # Store last 3 exchanges
        print("Enhanced Chatbot initialized successfully.")
        
    def _keyword_emergency_check(self, prompt: str) -> bool:
        """Enhanced emergency detection with more comprehensive keywords"""
        prompt_lower = prompt.lower()
        return any(keyword in prompt_lower for keyword in self.emergency_keywords)

    def _enhanced_intent_classification(self, prompt: str) -> str:
        """Enhanced intent classification with better handling of short prompts"""
        
        # Handle very short medical symptoms
        short_medical_terms = [
            'fever', 'cold', 'cough', 'pain', 'headache', 'nausea', 'dizzy', 'tired',
            'sick', 'hurt', 'ache', 'sore', 'swelling', 'rash', 'infection', 'symptoms',
            'diabetes', 'asthma', 'flu', 'migraine', 'arthritis', 'allergy'
        ]
        
        prompt_lower = prompt.lower().strip()
        words = prompt.split()
        
        # If it's a short prompt with medical terms, classify as medical
        if len(words) <= 3 and any(term in prompt_lower for term in short_medical_terms):
            return 'medical_question'
        
        # Use the trained classifier for longer prompts
        try:
            inputs = self.intent_tokenizer(prompt, return_tensors="pt", truncation=True, max_length=128).to(self.device)
            with torch.no_grad():
                logits = self.intent_model(**inputs).logits
            predicted_class_id = torch.argmax(logits, dim=1).item()
            return self.intent_model.config.id2label[predicted_class_id]
        except Exception as e:
            print(f"Intent classification error: {e}")
            return 'medical_question'  # Default to medical if error
    
    def _retrieve_context(self, query: str, top_k: int = 3) -> str:
        """Enhanced context retrieval with deduplication and relevance filtering"""
        try:
            query_embedding = self.retriever_model.encode(query, convert_to_tensor=True, device=self.device)
            hits = util.semantic_search(query_embedding, self.db_embeddings, top_k=top_k*2)  # Get more for filtering
            
            # Filter and deduplicate contexts
            contexts = []
            seen_contexts = set()
            
            for hit in hits[0]:
                if hit['score'] < 0.3:  # Skip low-relevance results
                    continue
                    
                context = self.db['completion'].iloc[hit['corpus_id']]
                context_snippet = context[:100].lower()  # First 100 chars for dedup
                
                if context_snippet not in seen_contexts and len(context) > 50:
                    contexts.append(context)
                    seen_contexts.add(context_snippet)
                    
                if len(contexts) >= top_k:
                    break
            
            return "\n\n---\n\n".join(contexts) if contexts else "No relevant medical information found."
            
        except Exception as e:
            print(f"Retrieval error: {e}")
            return "Unable to retrieve medical information."
    
    def _clean_response(self, response: str) -> str:
        """Enhanced response cleaning to remove repetition and improve formatting"""
        
        # Remove common problematic phrases
        problematic_phrases = [
            "Thanks for your question on Chat Doctor",
            "Chat Doctor",
            "Hope I have solved your query",
            "I will be happy to help you further",
            "Wish you good health",
            "For an accurate diagnosis, please consult a healthcare professional"
        ]
        
        cleaned = response
        for phrase in problematic_phrases:
            cleaned = re.sub(re.escape(phrase) + r'\.?\s*', '', cleaned, flags=re.IGNORECASE)
        
        # Split into sentences and remove duplicates
        sentences = re.split(r'[.!?]+', cleaned)
        unique_sentences = []
        seen_sentences = set()
        
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence and len(sentence) > 10:
                sentence_lower = sentence.lower()
                sentence_key = sentence_lower[:80]  # Use first 80 chars for similarity
                
                if sentence_key not in seen_sentences:
                    unique_sentences.append(sentence)
                    seen_sentences.add(sentence_key)
        
        # Reconstruct response
        if unique_sentences:
            cleaned_response = '. '.join(unique_sentences)
            if not cleaned_response.endswith('.'):
                cleaned_response += '.'
        else:
            cleaned_response = "I apologize, but I couldn't generate a clear response to your question."
        
        # Remove excessive repetition patterns
        repetition_patterns = [
            r'(\b(?:You should|Avoid|Take|Don\'t)\s+[^.]{5,50}\.)\s*\1+',  # Repeated advice
            r'(\b[A-Z][^.]{10,}\.)(\s*\1){2,}',  # Any sentence repeated 3+ times
        ]
        
        for pattern in repetition_patterns:
            cleaned_response = re.sub(pattern, r'\1', cleaned_response, flags=re.IGNORECASE)
        
        return cleaned_response
            
    def get_response(self, prompt: str, session_id: str) -> dict:
        """Enhanced response generation with proper context handling and Flask compatibility"""
        
        try:
            # --- Enhanced Emergency Detection ---
            if self._keyword_emergency_check(prompt):
                intent = "emergency_keyword"
                final_response = "Based on your description, this may be a medical emergency. Please seek immediate medical attention or call your local emergency services."
                confidence = 1.0
            else:
                # --- Enhanced Intent Classification ---
                intent = self._enhanced_intent_classification(prompt)
                confidence = 1.0

                if intent == 'emergency':
                    final_response = "This may be a medical emergency. Please seek immediate medical attention or call your local emergency services."
                elif intent == 'greeting':
                    final_response = "Hello! I am a medical AI assistant. How can I help you with your health questions today?"
                elif intent == 'medical_question':
                    print("Processing medical question with enhanced RAG...")
                    
                    # --- ENHANCED CONTEXT HANDLING ---
                    # 1. Retrieve context using ONLY the current prompt (clean query)
                    retrieved_context = self._retrieve_context(prompt)
                    
                    # 2. Get conversation history separately
                    conversation_history = "\n".join(list(self.histories[session_id])[-4:])  # Last 4 entries
                    
                    # 3. Create structured prompt for the generator
                    augmented_prompt = (
                        "You are a knowledgeable medical assistant. Based on the conversation context and medical information provided, "
                        "give a clear, helpful, and concise answer to the user's question. Avoid repetition.\n\n"
                        f"Previous Conversation:\n{conversation_history}\n\n"
                        f"Medical Information:\n{retrieved_context}\n\n"
                        f"Current Question: {prompt}\n\n"
                        f"Response:"
                    )
                    
                    print("Generating enhanced medical response...")
                    inputs = self.gen_tokenizer(augmented_prompt, return_tensors="pt", max_length=1024, truncation=True).to(self.device)
                    
                    with torch.no_grad():
                        output = self.gen_model.generate(
                            **inputs,
                            max_length=200,           # Shorter to reduce repetition
                            num_beams=4,              # Fewer beams for efficiency
                            early_stopping=True,
                            repetition_penalty=1.3,   # Higher penalty
                            no_repeat_ngram_size=3,   # Prevent 3-word repetitions
                            temperature=0.8,          # Slight randomness
                            do_sample=True            # Enable sampling
                        )
                    
                    raw_response = self.gen_tokenizer.decode(output[0], skip_special_tokens=True)
                    final_response = self._clean_response(raw_response)
                    
                    print(f"Generated response length: {len(final_response)} characters")
                    
                else:
                    final_response = "I'm not sure how to respond to that. Could you please rephrase your question?"
            
            # --- Update History with Clean Entries ---
            self.histories[session_id].append(f"User: {prompt}")
            self.histories[session_id].append(f"Bot: {final_response[:100]}...")  # Store truncated response
            
            disclaimer = "\n\nDisclaimer: This is an AI-generated response and does not constitute medical advice."
            
            return {
                "responseText": final_response + disclaimer,
                "intent": intent, 
                "confidence": confidence
            }
            
        except Exception as e:
            print(f"Error in get_response: {e}")
            return {
                "responseText": "I apologize, but I encountered an error processing your request. Please try rephrasing your question.",
                "intent": "error",
                "confidence": 0.0
            }
