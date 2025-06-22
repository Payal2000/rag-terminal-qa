from utils.embedder import get_embeddings
from utils.vector_store import search_top_k
import openai
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv(dotenv_path=Path(__file__).resolve().parents[0] / '.env')
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(question, context):
    prompt = f"""Answer the question based only on the context below:
    
Context:
{context}

Question: {question}
Answer:"""
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    question = input("❓ Ask your question: ")
    embedding = get_embeddings([question])[0]
    top_chunks = search_top_k(embedding)
    final_answer = ask_llm(question, "\n\n".join(top_chunks))
    print("\n🤖 Answer:\n", final_answer)
