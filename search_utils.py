import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd

# Load the FAISS index and sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("semantic_index.faiss")

# Load the saved disputes data
with open("dispute_data.pkl", "rb") as f:
    df = pickle.load(f)

def search_similar_disputes(query, top_k=5):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), top_k)
    return df.iloc[indices[0]]
