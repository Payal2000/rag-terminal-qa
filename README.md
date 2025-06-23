# 📄 RAG-Based PDF Question Answering System

This project is a Retrieval-Augmented Generation (RAG) system that allows users to upload any PDF document and ask natural language questions about it. It combines OpenAI's GPT model with Pinecone vector search to provide accurate, context-aware answers from your own documents.

---

## 🚀 Features

- 🧠 **Retrieval-Augmented Generation (RAG)** with OpenAI GPT
- 📚 Upload any custom PDF document
- 🔎 Ask natural language questions and get smart answers
- ⚡ CLI and Web App (Streamlit) interface
- 🔒 Environment-based API key management

---

## 🛠 Tech Stack

- **Backend**: Python 3, OpenAI GPT-4, Pinecone Vector DB
- **Text Parsing**: `pdfminer.six`
- **Embeddings**: `text-embedding-3-small`
- **Frontend (optional)**: Streamlit
- **Vector Search**: Pinecone
- **Utilities**: `dotenv`, `tiktoken`, `fastapi` (optional)

---

## 🧩 Folder Structure

rag_terminal_qa/
├── ingest.py              # CLI script to process and embed PDFs
├── query.py               # CLI script to ask questions
├── streamlit_app.py       # Streamlit web app interface
├── utils/
│   ├── pdf_parser.py      # PDF extraction + chunking
│   ├── embedder.py        # Embedding with OpenAI
│   └── vector_store.py    # Pinecone vector indexing + querying
├── .gitignore
├── .env.example           # Safe template for environment variables
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repository

\`\`\`bash
git clone https://github.com/Payal2000/rag-terminal-qa.git
cd rag-terminal-qa
\`\`\`

### 2. Create and activate a virtual environment

\`\`\`bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate     # Windows
\`\`\`

### 3. Install dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Set up your \`.env\` file

Create a \`.env\` file in the root directory based on \`.env.example\`:

\`\`\`env
OPENAI_API_KEY=your-openai-api-key
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_INDEX_NAME=doc-qa-index
PINECONE_ENVIRONMENT=us-east-1
\`\`\`

---

## 🧪 How to Use

### 📥 Ingest a PDF (CLI)

\`\`\`bash
python3 ingest.py sample.pdf
\`\`\`

### ❓ Ask a question (CLI)

\`\`\`bash
python3 query.py
\`\`\`

Example:
\`\`\`
❓ Ask your question: What is the payment clause?
🤖 Answer: Clause 4 outlines the payment terms agreed upon by both parties.
\`\`\`

---

### 🌐 Run the Streamlit Web App

\`\`\`bash
streamlit run streamlit_app.py
\`\`\`

You can upload a PDF and ask questions via a friendly UI.

---

## 💡 Sample Questions to Try

- What is this document about?
- What are the payment terms?
- Who are the parties involved?
- Summarize section 3.1.
- What methodology was used in this paper?
- What benefits are offered to employees?

---

## 📄 .env.example (included)

Please use `.env.example` to share your config template without exposing actual API keys.

---

## 📦 Coming Soon

- Citation source highlighting
- Multi-document support
- Chat history + document summaries
- FastAPI backend for production

---

## 🙌 Author

**Payal Sanjay Nagaonkar**  
[LinkedIn](https://www.linkedin.com/in/payal-sanjay-nagaonkar-76b733188/) | [GitHub](https://github.com/Payal2000)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
