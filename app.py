import os
from fastapi import FastAPI
from typing import Optional
from datetime import datetime
from pydantic import BaseModel
import chromadb

# Mock LLM mode for CI testing
USE_MOCK_LLM = os.getenv("USE_MOCK_LLM", "0") == "1"
# OLLAMA_HOST must be set via environment variable in Kubernetes
# Default works for local development only
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

if not USE_MOCK_LLM:
    import ollama
    ollama_client = ollama.Client(host=OLLAMA_HOST)

app = FastAPI(
    title="recallApi API",
    description="Retrieval Augmented Generation API for Knowledge Management",
    version="1.0.0"
)

chroma = chromadb.PersistentClient(path="./db")
collection = chroma.get_or_create_collection("docs")


class AddContent(BaseModel):
    """Request model for adding content to knowledge base."""
    content: str
    id: Optional[str] = None


@app.get("/")
def root():
    """Root endpoint with API information."""
    return {
        "name": "recallApi",
        "version": "1.0.0",
        "status": "running",
        "mock_mode": USE_MOCK_LLM,
        "endpoints": {
            "GET /": "API information",
            "POST /add": "Add content to knowledge base",
            "GET /list": "List all documents",
            "POST /query": "Query the knowledge base"
        }
    }


@app.post("/add")
def add_content(data: AddContent):
    """Add new content to the knowledge base dynamically."""
    doc_id = data.id or f"doc_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
    
    collection.add(documents=[data.content], ids=[doc_id])
    
    return {
        "status": "success",
        "message": "Content added to knowledge base",
        "id": doc_id
    }


@app.get("/list")
def list_all():
    """List all documents in the knowledge base."""
    results = collection.get()
    return {
        "count": len(results["ids"]),
        "ids": results["ids"],
        "documents": results["documents"]
    }


@app.post("/query")
def query(q: str):
    """Query the knowledge base using RAG."""
    results = collection.query(query_texts=[q], n_results=1)
    context = results["documents"][0][0] if results["documents"] else ""

    if USE_MOCK_LLM:
        # In mock mode, return the retrieved context directly
        return {"answer": context}

    # In production mode, use Ollama
    answer = ollama_client.generate(
        model="tinyllama",
        prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
    )

    return {"answer": answer["response"]}