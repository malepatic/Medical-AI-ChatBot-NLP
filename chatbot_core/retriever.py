import torch
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import os

class Retriever:
    def __init__(self, knowledge_base_path: str, model_name: str = 'dmis-lab/biobert-base-cased-v1.1'):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(model_name, device=self.device)
        
        # Load and process the knowledge base
        print("Loading knowledge base...")
        df = pd.read_csv(knowledge_base_path).dropna(subset=['prompt', 'completion'])
        self.knowledge_base = df['completion'].tolist() # We search the answers/completions
        
        # Pre-compute embeddings for the knowledge base for fast search
        embeddings_path = 'kb_embeddings.pt'
        if os.path.exists(embeddings_path):
            print("Loading existing knowledge base embeddings...")
            self.kb_embeddings = torch.load(embeddings_path, map_location=self.device)
        else:
            print("Computing knowledge base embeddings (this may take a while)...")
            self.kb_embeddings = self.model.encode(self.knowledge_base, convert_to_tensor=True, device=self.device)
            torch.save(self.kb_embeddings, embeddings_path)
        print("Retriever initialized.")

    def search(self, query: str, top_k: int = 3) -> str:
        """Finds the top_k most relevant documents for a query."""
        query_embedding = self.model.encode(query, convert_to_tensor=True, device=self.device)
        hits = util.semantic_search(query_embedding, self.kb_embeddings, top_k=top_k)
        
        # Combine the retrieved snippets into a single context string
        context = "\n".join([self.knowledge_base[hit['corpus_id']] for hit in hits[0]])
        return context
