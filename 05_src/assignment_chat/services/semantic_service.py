import os
import chromadb
from sentence_transformers import SentenceTransformer

# Get absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "chroma_db")

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_collection("knowledge")

def semantic_search(query: str) -> str:
    embedding = model.encode([query])[0]

    results = collection.query(
        query_embeddings=[embedding],
        n_results=2
    )

    docs = results["documents"][0]

    return "Here is what I found:\n" + "\n".join(docs)
