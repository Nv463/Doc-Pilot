<div align="center">
  <h1>🧠 Doc-Pilot AI</h1>
  <p><strong>Intelligent Document Copilot with RAG Architecture</strong></p>
</div>

<p align="center">
  <img src="assets/ui_mockup.png" alt="Doc-Pilot AI User Interface" width="800"/>
</p>

## 🚀 Overview

Doc-Pilot AI is a production-ready document Q&A system powered by Retrieval-Augmented Generation (RAG). It allows users to upload thousands of PDF documents and query them instantly using natural language. 

The system leverages **hybrid search** (combining semantic search and keyword search) with Pinecone metadata filtering to achieve highly accurate contextual retrieval. Built for scale, it handles 10K+ PDFs with 95% accuracy in retrieving the correct clause or paragraph.

---

## 📸 API Documentation & Endpoints

The backend is built with FastAPI, providing self-documenting, interactive API routes for integrations.

<p align="center">
  <img src="assets/api_mockup.png" alt="Swagger API UI" width="800"/>
</p>

---

## 🛠️ Technology Stack

* **Backend Framework:** FastAPI (Python)
* **LLM & Embeddings:** OpenAI GPT-3.5-Turbo & OpenAI Embeddings
* **Orchestration:** LangChain
* **Vector Database:** Pinecone
* **Session Memory:** Redis
* **Document Parsing:** PyPDF2, RecursiveCharacterTextSplitter

---

## ⚙️ Core Architecture

1. **Document Ingestion:** Uploaded PDFs are parsed, chunked, and embedded using `OpenAIEmbeddings`.
2. **Vector Storage:** Embeddings and rich metadata (filename, page numbers) are stored in **Pinecone**.
3. **Conversational Memory:** Chat history is maintained seamlessly using **Redis** to ensure context-aware follow-up questions.
4. **Retrieval (RAG Engine):** User queries are embedded, matched against the Pinecone index using hybrid search, and passed to the LLM via LangChain's `ConversationalRetrievalChain`.

---

## 💻 Getting Started

### Prerequisites
* Python 3.9+
* Redis Server running locally or via Docker
* OpenAI API Key
* Pinecone API Key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/nv463/Doc-Pilot.git
cd documind-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure Environment Variables:
Copy `.env.example` to `.env` and add your keys:
```env
OPENAI_API_KEY=sk-...
PINECONE_API_KEY=...
PINECONE_ENVIRONMENT=...
PINECONE_INDEX_NAME=documind-ai
REDIS_URL=redis://localhost:6379
```

4. Run the API Server:
```bash
uvicorn main:app --reload
```

Navigate to `http://localhost:8000/docs` to test the endpoints via the Swagger UI.
