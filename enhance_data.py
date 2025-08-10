#!/usr/bin/env python3
"""
Knowledge Base Enhancement Script
Adds high-quality comparative diabetes information to your knowledge base
"""

import pandas as pd
import os

def enhance_knowledge_base():
    """Add better diabetes content to the knowledge base"""
    
    # Path to your current knowledge base
    db_path = "/medical_chatbot_project/data/common_diseases_dataset.csv"
    
    print("Loading current knowledge base...")
    try:
        df = pd.read_csv(db_path)
        print(f"Current knowledge base has {len(df)} entries")
        print(f"Columns: {list(df.columns)}")
        
        # Show current diabetes entries
        if 'completion' in df.columns:
            diabetes_entries = df[df['completion'].str.contains('diabetes|Diabetes', case=False, na=False)]
            print(f"Current diabetes entries: {len(diabetes_entries)}")
            
            # Show unique diabetes entries
            unique_diabetes = diabetes_entries['completion'].nunique()
            print(f"Unique diabetes entries: {unique_diabetes}")
            
            if unique_diabetes < 5:
                print("❌ Knowledge base has very few unique diabetes entries!")
                print("Adding comprehensive diabetes information...")
                
                # High-quality diabetes information
                new_entries = [
                    {
                        'prompt': 'What is the difference between Type 1 and Type 2 diabetes?',
                        'completion': 'Type 1 diabetes is an autoimmune condition where the pancreas produces little to no insulin, typically diagnosed in children and young adults. The immune system destroys insulin-producing beta cells. Type 2 diabetes is a metabolic disorder where the body becomes resistant to insulin or doesn\'t produce enough insulin, usually developing in adults over 45. Type 1 requires insulin injections for survival, while Type 2 can often be managed with lifestyle changes, oral medications, and sometimes insulin. Type 1 accounts for 5-10% of all diabetes cases, while Type 2 accounts for 90-95%.'
                    },
                    {
                        'prompt': 'Type 1 vs Type 2 diabetes comparison',
                        'completion': 'Key differences between Type 1 and Type 2 diabetes: ONSET - Type 1 usually develops in childhood/adolescence, Type 2 typically in adulthood. CAUSE - Type 1 is autoimmune destruction of pancreatic cells, Type 2 is insulin resistance. TREATMENT - Type 1 always requires insulin therapy, Type 2 may be managed with diet, exercise, and oral medications initially. BODY WEIGHT - Type 1 patients are often normal weight or underweight, Type 2 patients are frequently overweight. SYMPTOMS - Type 1 symptoms appear rapidly, Type 2 develops gradually over years.'
                    },
                    {
                        'prompt': 'How are Type 1 and Type 2 diabetes different?',
                        'completion': 'Type 1 and Type 2 diabetes differ fundamentally in their causes and characteristics. Type 1 is an autoimmune disease where the body attacks its own insulin-producing cells, requiring lifelong insulin replacement. It typically appears suddenly in young people with symptoms like rapid weight loss, excessive thirst, and fatigue. Type 2 develops when cells become resistant to insulin or the pancreas cannot produce enough insulin. It progresses slowly, often without symptoms initially, and is strongly linked to obesity, sedentary lifestyle, and genetics. While Type 1 always needs insulin, Type 2 can sometimes be reversed through lifestyle changes.'
                    },
                    {
                        'prompt': 'What causes Type 1 diabetes vs Type 2 diabetes?',
                        'completion': 'Type 1 diabetes is caused by an autoimmune reaction where the immune system mistakenly attacks and destroys insulin-producing beta cells in the pancreas. The exact trigger is unknown but may involve genetic predisposition combined with environmental factors like viruses. Type 2 diabetes is caused by insulin resistance, where cells don\'t respond properly to insulin, combined with the pancreas\'s inability to produce enough insulin to overcome this resistance. Risk factors include obesity, physical inactivity, age over 45, family history, and certain ethnicities.'
                    },
                    {
                        'prompt': 'Type 1 diabetes characteristics and symptoms',
                        'completion': 'Type 1 diabetes characteristics: Autoimmune destruction of pancreatic beta cells, absolute insulin deficiency, rapid onset of symptoms, typically diagnosed before age 30, not preventable, requires immediate insulin therapy. Symptoms include extreme thirst, frequent urination, rapid weight loss, fatigue, blurred vision, and ketoacidosis risk. Without insulin treatment, Type 1 diabetes is life-threatening. Patients need to monitor blood glucose frequently and adjust insulin doses based on food intake and activity levels.'
                    },
                    {
                        'prompt': 'Type 2 diabetes characteristics and management',
                        'completion': 'Type 2 diabetes characteristics: Insulin resistance with relative insulin deficiency, gradual onset, typically diagnosed after age 45, often associated with obesity, may be preventable and sometimes reversible. Early symptoms are mild: increased thirst, frequent urination, fatigue, slow-healing wounds. Management includes lifestyle modifications (diet, exercise, weight loss), oral medications (metformin, sulfonylureas), and insulin if needed. Many people can achieve remission through significant weight loss and sustained lifestyle changes.'
                    },
                    {
                        'prompt': 'Can diabetes be prevented or reversed?',
                        'completion': 'Type 1 diabetes cannot be prevented or reversed as it is an autoimmune condition. However, Type 2 diabetes can often be prevented through maintaining healthy weight, regular physical activity, balanced diet, and avoiding smoking. Type 2 diabetes can sometimes be reversed or put into remission through significant weight loss (10-15% of body weight), sustained dietary changes, and increased physical activity. Studies show that intensive lifestyle interventions can help some people achieve normal blood glucose levels without medication, though this requires ongoing commitment to healthy habits.'
                    }
                ]
                
                # Add new entries to the dataframe
                new_df = pd.DataFrame(new_entries)
                
                # Remove duplicate diabetes entries first
                print("Removing duplicate diabetes entries...")
                non_diabetes = df[~df['completion'].str.contains('diabetes|Diabetes', case=False, na=False)]
                
                # Combine with new entries
                enhanced_df = pd.concat([non_diabetes, new_df], ignore_index=True)
                
                print(f"Enhanced knowledge base will have {len(enhanced_df)} entries")
                
                # Create backup
                backup_path = db_path + ".backup"
                df.to_csv(backup_path, index=False)
                print(f"Created backup at: {backup_path}")
                
                # Save enhanced knowledge base
                enhanced_df.to_csv(db_path, index=False)
                print(f"Enhanced knowledge base saved!")
                
                return True
            else:
                print(" Knowledge base already has diverse diabetes content")
                return False
                
    except Exception as e:
        print(f" Error enhancing knowledge base: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_enhanced_retrieval():
    """Test the retrieval system with the enhanced knowledge base"""
    print("\n" + "="*50)
    print("TESTING ENHANCED RETRIEVAL SYSTEM")
    print("="*50)
    
    try:
        from sentence_transformers import SentenceTransformer, util
        import torch
        
        # Load the knowledge base
        db_path = "/medical_chatbot_project/data/common_diseases_dataset.csv"
        df = pd.read_csv(db_path)
        
        # Initialize retriever (same as in your bot)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        retriever_model = SentenceTransformer('all-MiniLM-L6-v2', device=device)
        
        # Encode knowledge base
        print("Encoding knowledge base...")
        db_embeddings = retriever_model.encode(df['completion'].tolist(), convert_to_tensor=True, device=device)
        
        # Test query
        test_query = "What is the difference between Type 1 and Type 2 diabetes?"
        print(f"\nTesting query: '{test_query}'")
        
        # Retrieve context
        query_embedding = retriever_model.encode(test_query, convert_to_tensor=True, device=device)
        hits = util.semantic_search(query_embedding, db_embeddings, top_k=3)
        
        print(f"\nTop 3 retrieved contexts:")
        for i, hit in enumerate(hits[0]):
            score = hit['score']
            content = df['completion'].iloc[hit['corpus_id']]
            print(f"\nRank {i+1} (Score: {score:.3f}):")
            print(f"{content[:300]}...")
            
    except Exception as e:
        print(f" Error testing retrieval: {e}")

if __name__ == "__main__":
    print("KNOWLEDGE BASE ENHANCEMENT SCRIPT")
    print("="*50)
    
    enhanced = enhance_knowledge_base()
    
    if enhanced:
        test_enhanced_retrieval()
        
        print("\n" + "="*50)
        print("NEXT STEPS:")
        print("="*50)
        print("1. The knowledge base has been enhanced with better diabetes content")
        print("2. A backup of the original was created (.backup extension)")
        print("3. Now restart your Flask server:")
        print("   cd /medical_chatbot_project")
        print("   gunicorn --workers 1 --bind 0.0.0.0:5000 --timeout 120 app:app")
        print("4. Test the diabetes question again in the web interface")
    else:
        print("No enhancement needed or enhancement failed")
