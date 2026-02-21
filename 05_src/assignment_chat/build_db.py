import os
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "knowledge.txt")
DB_PATH = os.path.join(BASE_DIR, "chroma_db")

print("Reading data from:", DATA_PATH)
print("Saving database to:", DB_PATH)

with open(DATA_PATH, "r") as f:
    documents = [line.strip() for line in f.readlines() if line.strip()]

print("Loaded documents:", len(documents))

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection("knowledge")

embeddings = model.encode(documents)

for i, doc in enumerate(documents):
    collection.add(
        documents=[doc],
        embeddings=[embeddings[i]],
        ids=[str(i)]
    )

print("Database built successfully.")


