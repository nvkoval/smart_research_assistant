# Smart Research Assistant

The **Smart Research Assistant** is a domain-adaptable RAG (Retrieval-Augmented Generation) system designed to answer questions from user-uploaded documents (PDFs) by leveraging modern LLMs, vector embeddings, and a conversational interface.

This assistant is ideal for use cases such as:
- Academic research
- Legal contract analysis
- Health documentation support

---

## Features

- **PDF Uploads**: Users can upload one or multiple documents.
- **RAG Pipeline**: Integrates document chunking, vector search, and LLM-based answer generation.
- **Source Citations**: Links answers to the original text locations.
- **Conversational Interface**: Supports follow-up questions with chat history.
- **FastAPI Backend**: REST API for interaction and integration.

## Tech Stack

| Component       | Tool                     |
|----------------|--------------------------|
| LLM            | OpenAI (`gpt-4o`)  |
| Vector Store   | ChromaDB (local)         |
| Embeddings     | HuggingFace (MiniLM)     |
| Parsing        | PyMuPDF                  |
| Backend        | FastAPI                  |
| Observability  | LangSmith    |


## 📂 Project Structure

```
smart-research-assistant/
├── app/
│   ├── api.py                   # FastAPI routes
│   ├── assistant.py             # RAG pipeline orchestrator
│   ├── config.py                # Environment & key loader
│   ├── document_processor.py    # PDF loader and splitter
│   ├── formatter.py             # Response formatting with sources
│   ├── rag_chain.py             # QA chain with ConversationalRetrievalChain
│   └── vector_store.py          # ChromaDB handler
├── data/
│   ├── docs/                    # User-uploaded documents
│   └── temp_docs/               # Temporary upload storage
├── notebooks/
│   └── document_ingestion.ipynb # Notebook demonstrating RAG pipeline usage
├── .env                         # API keys and settings
├── main.py                      # CLI interface (optional)
├── requirements.txt
└── README.md
```

## Installation

```bash
# Clone the repo
git clone https://github.com/your-username/smart-research-assistant.git
cd smart-research-assistant

# Install dependencies
pip install -r requirements.txt

# Create a .env file (see below)
cp .env.example .env
```

### Example `.env` file
```
OPENAI_API_KEY=your-openai-key
LANGSMITH_API_KEY=your-langsmith-key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_PROJECT=smart_research_assistant
HF_HUB_DISABLE_SYMLINKS_WARNING=1
TOKENIZERS_PARALLELISM=false
```

## Running the API

```bash
uvicorn app.api:app --reload
```

### Available Endpoints
| Method | Route     | Description                      |
|--------|-----------|----------------------------------|
| `POST` | `/setup`  | Upload and embed PDFs            |
| `POST` | `/ask`    | Ask a question                   |
| `POST` | `/clear`  | Clear chat history               |
| `GET`  | `/status` | Check if assistant is initialized|


## CLI Example
```bash
python main.py
```
Ask questions from the terminal after documents are indexed.

## Notebook Example
A Jupyter notebook is available for quick testing and experimentation:

**`notebooks/document_ingestion.ipynb`** demonstrates how to:
- Load and split documents
- Create and persist vector index
- Query using the RAG pipeline

This is helpful for debugging, prototyping, and understanding each component before running the full backend.

---

### Acknowledgements
Built using [LangChain](https://github.com/langchain-ai/langchain)
