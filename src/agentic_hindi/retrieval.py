from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np

MODEL = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'

class Retriever:
    def __init__(self, docs_path='data/docs.json'):
        self.model = SentenceTransformer(MODEL)
        with open(docs_path, 'r', encoding='utf-8') as f:
            self.docs = json.load(f)
        self.corpus = [d['text'] for d in self.docs]
        self.embeddings = self.model.encode(self.corpus, convert_to_numpy=True)
        d = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(d)
        faiss.normalize_L2(self.embeddings)
        self.index.add(self.embeddings)

    def retrieve(self, query, k=3):
        q_emb = self.model.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(q_emb)
        D, I = self.index.search(q_emb, k)
        results = []
        for idx in I[0]:
            results.append(self.docs[idx])
        return results
