import os
from pathlib import Path
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load .env from project root
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / '.env')

# Load from your .env using your exact variable names
pinecone_api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX_NAME")          # 👈 updated
pinecone_env = os.getenv("PINECONE_ENVIRONMENT")       # 👈 updated

# Validate required variables
if not pinecone_api_key:
    raise ValueError("❌ Missing PINECONE_API_KEY in .env")
if not index_name:
    raise ValueError("❌ Missing PINECONE_INDEX_NAME in .env")
if not pinecone_env:
    raise ValueError("❌ Missing PINECONE_ENVIRONMENT in .env")

# Initialize Pinecone client
pc = Pinecone(api_key=pinecone_api_key)

# Create index if it doesn't exist
if index_name not in pc.list_indexes().names():
    print(f"🛠 Creating index '{index_name}'...")
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric='cosine',
        spec=ServerlessSpec(cloud='aws', region=pinecone_env)
    )

# Connect to index
index = pc.Index(index_name)

def upsert_chunks(chunks, embeddings):
    vectors = [(f"id-{i}", emb, {"text": chunk}) for i, (chunk, emb) in enumerate(zip(chunks, embeddings))]
    index.upsert(vectors=vectors)
    print(f"✅ Upserted {len(vectors)} vectors to '{index_name}'")

def search_top_k(query_embedding, k=3):
    results = index.query(vector=query_embedding, top_k=k, include_metadata=True)
    return [match['metadata']['text'] for match in results['matches']]
