# 🧠 RecallApi

<div align="center">

**A Retrieval Augmented Generation (RAG) API**

*Combine vector search with Large Language Models to provide intelligent answers from your knowledge base*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128.2-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-326CE5.svg)](https://kubernetes.io/)

</div>

---

## � Project Overview

### What is RecallAPI?

**RecallAPI** is a complete **Retrieval Augmented Generation (RAG)** system that demonstrates how applications can interact with knowledge bases using AI. Instead of relying solely on Large Language Models (which can hallucinate or lack domain-specific knowledge), this project demonstrates how to ground AI responses in actual data through intelligent semantic search and context injection.

### What Was Built

This project implements a full-stack AI-powered API with:

- **RESTful API Backend**: Built with FastAPI, featuring health checks, dynamic content management, and intelligent query endpoints
- **Vector Database Integration**: ChromaDB for persistent storage and semantic similarity search using embeddings
- **Local LLM Integration**: Ollama server running TinyLlama for privacy-preserving AI inference
- **Multi-Environment Deployment**: Local development, Docker containerization, and complete Kubernetes orchestration
- **CI/CD Pipeline**: Automated testing, Docker image building, and security scanning via GitHub Actions
- **Mock Testing Layer**: GPU-free testing mode for rapid development and CI/CD workflows

### How It Works

The RAG pipeline follows this flow:

1. **Knowledge Storage**: Documents are embedded into vector representations and stored in ChromaDB
2. **User Query**: Natural language questions come in via REST API
3. **Semantic Retrieval**: ChromaDB finds the most relevant documents using vector similarity
4. **Context Injection**: Retrieved content is injected into the LLM prompt as context
5. **AI Generation**: Ollama's TinyLlama generates accurate, grounded answers based on actual data
6. **Response**: Structured JSON response delivered to the client

**Key Technical Implementation:**
- FastAPI handles REST API request processing
- ChromaDB manages vector embeddings and similarity search
- Ollama serves as the local LLM runtime (no external API calls)
- Kubernetes orchestrates separate pods for the API and LLM backend
- Service discovery enables pod-to-pod communication within the cluster

### Use Cases & Skills Demonstrated

**When This Architecture is Valuable:**

| Scenario | Application |
|----------|-------------|
| **Enterprise Knowledge Management** | Internal documentation search with AI-powered answers |
| **Customer Support** | Automated responses grounded in product manuals and FAQs |
| **Research & Education** | Query scientific papers or educational content with citations |
| **Privacy-Sensitive Applications** | Healthcare, legal, or financial systems requiring on-premise AI |
| **Edge AI Deployments** | Air-gapped environments where cloud APIs aren't available |

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Deployment](#-deployment)
- [API Reference](#-api-reference)
- [Testing](#-testing)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🚀 **High Performance** | Built with FastAPI for fast API processing |
| 🔍 **Semantic Search** | ChromaDB vector database for intelligent retrieval |
| 🤖 **Local LLM** | Privacy-first with Ollama - no data leaves your infrastructure |
| 🧪 **Mock Mode** | CI/CD friendly testing without GPU/LLM dependencies |
| 🐳 **Containerized** | Production-ready Docker images |
| ☸️ **Kubernetes Native** | Self-contained cluster deployment with Ollama |
| 🔒 **Secure by Default** | Environment-based config, no hardcoded secrets |

---

## 🛠 Tech Stack

### Core Dependencies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.11+ | Runtime |
| **FastAPI** | 0.128.2 | Web framework |
| **Uvicorn** | 0.40.0 | ASGI server |
| **ChromaDB** | 1.4.1 | Vector database |
| **Ollama** | 0.6.1 | Local LLM runtime |
| **Pydantic** | 2.12.5 | Data validation |

### Infrastructure

| Tool | Version | Purpose |
|------|---------|---------|
| **Docker** | 28.4.0 | Containerization |
| **Kubernetes** | 1.35.0 | Orchestration |
| **Minikube** | 1.38.0 | Local K8s cluster |
| **TinyLlama** | latest | LLM model (637MB) |

---

## 🏗 Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           KUBERNETES CLUSTER                            │
│                                                                         │
│  ┌─────────────────────────────────┐    ┌─────────────────────────────┐ │
│  │         recallApi Pod           │    │         Ollama Pod          │ │
│  │  ┌─────────────┐ ┌───────────┐  │    │  ┌───────────────────────┐  │ │
│  │  │   FastAPI   │ │ ChromaDB  │  │    │  │      TinyLlama        │  │ │
│  │  │   Server    │ │(Vector DB)│  │    │  │       Model           │  │ │
│  │  └──────┬──────┘ └───────────┘  │    │  └───────────────────────┘  │ │
│  │         │                       │    │             ▲               │ │
│  └─────────┼───────────────────────┘    └─────────────┼───────────────┘ │
│            │                                          │                 │
│            │         ollama-service:11434             │                 │
│            └──────────────────────────────────────────┘                 │
│                                                                         │
│  ┌─────────────────────┐                                                │
│  │ recallApi-service   │◀─── NodePort (auto-assigned)                   │
│  └──────────┬──────────┘                                                │
└─────────────┼───────────────────────────────────────────────────────────┘
              │
       ┌──────┴──────┐
       │   Client    │
       │  Requests   │
       └─────────────┘
```

### Data Flow

```
┌──────────┐     ┌─────────────────────────────────────────────────────────┐
│          │     │                      RAG Pipeline                       │
│  User    │     │  ┌─────────┐   ┌──────────┐   ┌─────────┐   ┌────────┐  │
│  Query   │────▶│  │ Embed   │──▶│ Retrieve │──▶│ Context │──▶│  LLM   │  │
│          │     │  │ Query   │   │ Top-K    │   │ Inject  │   │ Answer │  │
│          │     │  └─────────┘   └──────────┘   └─────────┘   └────────┘  │
└──────────┘     └─────────────────────────────────────────────────────────┘
                                                                      │
                              ┌───────────────────────────────────────┘
                              ▼
                       ┌─────────────┐
                       │  Response   │
                       │  {"answer": │
                       │   "..."}    │
                       └─────────────┘
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Required
python3 --version    # Python 3.11+
pip --version        # pip 25.3+

# For Kubernetes deployment
docker --version     # Docker 28.x+
kubectl version      # Kubernetes 1.35+
minikube version     # Minikube 1.38+
```

### Option 1: Local Development (Fastest)

```bash
# 1. Clone and setup
git clone https://github.com/Mohammad-Rifat-Khan/RecallAPI.git
cd RecallAPI

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Seed the knowledge base (optional)
python embed.py

# 5. Start the server
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

**Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345]
```

### Option 2: Mock Mode (No Ollama)

Perfect for testing and CI/CD pipelines:

```bash
USE_MOCK_LLM=1 uvicorn app:app --reload
```

**Output:**
```
INFO:     Mock LLM mode enabled - returning context directly
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## 🐳 Deployment

### Docker Deployment

```bash
# Build the image
docker build -t recallApi:latest .

# Run with host Ollama
docker run -p 8000:8000 \
  -e OLLAMA_HOST=http://host.docker.internal:11434 \
  recallApi:latest

# Run in mock mode (no Ollama needed)
docker run -p 8000:8000 -e USE_MOCK_LLM=1 recallApi:latest
```

### Kubernetes Deployment (Full Stack)

Deploy both the app and Ollama inside the cluster - no external dependencies:

```bash
# 1. Start minikube
minikube start

# 2. Build image inside minikube
eval $(minikube docker-env)
docker build -t recallApi:latest .

# 3. Deploy Ollama (LLM backend)
kubectl apply -f ollama-deployment.yaml
kubectl apply -f ollama-service.yaml

# 4. Wait for Ollama image (~5.6GB download, 10-15 min)
kubectl get pods -l app=ollama -w

# 5. Deploy the application
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# 6. Get the service URL
minikube service recallApi-service --url
```

**Expected Output:**
```
$ kubectl get pods
NAME                                    READY   STATUS    RESTARTS   AGE
recallApi-deployment-xxxxx-xxxxx     1/1     Running   0          2m
ollama-xxxxx-xxxxx                      1/1     Running   0          5m

$ minikube service recallApi-service --url
http://192.168.49.2:31641
```

### Verify Deployment

```bash
# Test root endpoint
curl http://192.168.49.2:31641/
# Output: {"name":"recallApi","version":"1.0.0","status":"running",...}

# Test query endpoint
curl -X POST "http://192.168.49.2:31641/query?q=What%20is%20Kubernetes?"
# Output: {"answer":"Kubernetes is a container orchestration platform..."}
```

---

## 📚 API Reference

### Interactive Documentation

| URL | Description |
|-----|-------------|
| `http://localhost:8000/docs` | Swagger UI |
| `http://localhost:8000/redoc` | ReDoc |

### Endpoints

#### `GET /` - Health Check
```bash
curl http://localhost:8000/
```
**Response:**
```json
{
  "name": "recallApi",
  "version": "1.0.0",
  "status": "running",
  "mock_mode": false,
  "endpoints": {
    "GET /": "API information",
    "POST /add": "Add content to knowledge base",
    "GET /list": "List all documents",
    "POST /query": "Query the knowledge base"
  }
}
```

---

#### `POST /add` - Add Document
```bash
curl -X POST "http://localhost:8000/add" \
  -H "Content-Type: application/json" \
  -d '{"content": "Docker is a containerization platform."}'
```
**Response:**
```json
{
  "status": "success",
  "message": "Content added to knowledge base",
  "id": "doc_20260207_143052_123456"
}
```

---

#### `GET /list` - List Documents
```bash
curl http://localhost:8000/list
```
**Response:**
```json
{
  "count": 2,
  "ids": ["k8s", "doc_20260207_143052_123456"],
  "documents": [
    "Kubernetes is a container orchestration...",
    "Docker is a containerization platform."
  ]
}
```

---

#### `POST /query` - Query Knowledge Base
```bash
curl -X POST "http://localhost:8000/query?q=What%20is%20Kubernetes?"
```
**Response:**
```json
{
  "answer": "Kubernetes is a container orchestration platform used to manage containers at scale. It automates deployment, scaling, and management of containerized applications."
}
```

---

## 🧪 Testing

### Run Semantic Tests

```bash
# Start server first
uvicorn app:app --host 127.0.0.1 --port 8000 &

# Run tests
python semantic_test.py
```

**Output:**
```
✅ Kubernetes query test passed
All semantic tests passed!
```

### CI/CD Testing (Mock Mode)

```bash
# No Ollama required
USE_MOCK_LLM=1 uvicorn app:app --host 127.0.0.1 --port 8000 &
sleep 3
python semantic_test.py
```

### GitHub Actions

Tests run automatically on push via `.github/workflows/ci.yml`:
- Uses mock LLM mode
- No GPU required
- Fast feedback loop

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OLLAMA_HOST` | Ollama server URL | `http://localhost:11434` | No |
| `USE_MOCK_LLM` | Enable mock mode (1/true) | `false` | No |

### Example `.env`

```bash
# Production
OLLAMA_HOST=http://ollama-service:11434
USE_MOCK_LLM=false

# Development/Testing
# USE_MOCK_LLM=1
```

---

## 📁 Project Structure

```
recallApi/
├── app.py                    # Main FastAPI application
├── embed.py                  # Knowledge base seeding script
├── semantic_test.py          # Semantic validation tests
├── requirements.txt          # Python dependencies
│
├── Dockerfile                # Container image definition
├── deployment.yaml           # K8s app deployment
├── service.yaml              # K8s app service (NodePort)
├── ollama-deployment.yaml    # K8s Ollama deployment
├── ollama-service.yaml       # K8s Ollama service (ClusterIP)
│
├── k8s.txt                   # Sample knowledge base content
├── db/                       # ChromaDB persistent storage
│
├── .env.example              # Environment template
├── .gitignore                # Git ignore rules
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI pipeline
│
├── LICENSE                   # MIT License
└── README.md                 # This file
```

---

## 🔧 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `Connection refused` to Ollama | Check `OLLAMA_HOST` env var, verify Ollama is running |
| Slow first query | Model loading into memory (~30s for TinyLlama) |
| K8s pod stuck `ContainerCreating` | Ollama image is ~5.6GB, wait 10-15 minutes |
| Mock mode not working | Use `USE_MOCK_LLM=1` (not `true`) |

### Useful Commands

```bash
# Check K8s logs
kubectl logs -l app=recallApi -f

# Check Ollama pod
kubectl exec -it $(kubectl get pod -l app=ollama -o jsonpath='{.items[0].metadata.name}') -- ollama list

# Restart deployment
kubectl rollout restart deployment/recallApi-deployment
```

---

## 📄 License

MIT License - Free to use and modify.

---

<div align="center">

**Built with ❤️ using FastAPI, ChromaDB, and Ollama**

</div>
