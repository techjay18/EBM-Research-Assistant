import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

import torch

# Embedding model
embed_model = SentenceTransformer(
    "pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb"
)




# Load FAISS index
import os
import faiss

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

index_path = os.path.join(BASE_DIR, "..", "faiss_index", "oncology.faiss")

index = faiss.read_index(index_path)

# Load papers
papers_path = os.path.join(BASE_DIR, "..", "faiss_index", "papers.pkl")
papers = pd.read_pickle(papers_path)


def search(query, top_k=3):

    # 1. Convert query into embedding
    query_embedding = embed_model.encode([query])
    query_embedding = np.array(query_embedding, dtype="float32")

    # 2. FAISS search
    D, I = index.search(query_embedding, top_k)

    # 3. Collect results
    results = []

    for idx in I[0]:
        doc = {
            "Title": papers.iloc[idx]["Title"],
            "Source": papers.iloc[idx]["Source"],
            "Link": papers.iloc[idx]["Link"],
            "Summary": papers.iloc[idx]["Summary"]
        }
        results.append(doc)

    return results