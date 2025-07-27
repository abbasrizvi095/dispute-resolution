# semantic_search.py
import pandas as pd
import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load sample disputes
df = pd.read_csv("sample_disputes.csv")

# Load Sentence-BERT model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(df["DisputeText"], convert_to_numpy=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Save the index to disk
faiss.write_index(index, "semantic_index.faiss")

# Save the dispute data
with open("dispute_data.pkl", "wb") as f:
    pickle.dump(df, f)

print("✅ FAISS index and data saved.")
