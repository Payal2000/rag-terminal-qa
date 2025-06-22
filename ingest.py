from utils.pdf_parser import read_pdf, chunk_text
from utils.embedder import get_embeddings
from utils.vector_store import upsert_chunks
import sys

if __name__ == "__main__":
    file_path = sys.argv[1]
    print(f"Ingesting: {file_path}")
    text = read_pdf(file_path)
    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)
    upsert_chunks(chunks, embeddings)
    print("✅ Ingestion complete.")
