# 🧠 KnowledgeRAG

**KnowledgeRAG** is a production-ready Retrieval Augmented Generation (RAG) API that combines vector search with Large Language Models to provide intelligent answers based on your knowledge base.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## ✨ Features

- 🚀 **Fast API** - Built with FastAPI for high performance
- 🔍 **Vector Search** - Powered by ChromaDB for semantic search
- 🤖 **LLM Integration** - Seamless integration with Ollama
- 🧪 **Mock LLM** - Built-in mock LLM for testing without external dependencies
- 🐳 **Containerized** - Docker support for easy deployment
- ☸️ **Kubernetes Ready** - Production-ready Kubernetes manifests
- 🔒 **Secure** - Environment-based configuration, no hardcoded secrets
- 📊 **Observable** - Structured logging and health checks

## 🏗️ Architecture

```
User Request → FastAPI → ChromaDB (Vector Search) → LLM (Ollama/Mock) → Response
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker (optional)
- Ollama (for production use)

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/knowledgerag.git
cd knowledgerag
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Run the application**
```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

### Using Mock LLM (No Ollama Required)

For testing without Ollama:

```bash
export USE_MOCK_LLM=true
uvicorn app:app --reload
```

### Docker Deployment

```bash
docker build -t knowledgerag .
docker run -p 8000:8000 knowledgerag
```

### Kubernetes Deployment

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## 📚 API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Endpoints

#### `POST /add` - Add content to knowledge base
```bash
curl -X POST "http://localhost:8000/add" \
  -H "Content-Type: application/json" \
  -d '{"content": "Kubernetes is a container orchestration platform"}'
```

#### `GET /list` - List all documents
```bash
curl "http://localhost:8000/list"
```

#### `POST /query` - Query the knowledge base
```bash
curl -X POST "http://localhost:8000/query?q=What is Kubernetes?"
```

#### `GET /health` - Health check
```bash
curl "http://localhost:8000/health"
```

## 🧪 Testing

Run tests:
```bash
python semantic_test.py
```

Run with mock LLM for CI/CD:
```bash
USE_MOCK_LLM=true python semantic_test.py
```

## ⚙️ Configuration

Configuration is managed through environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `OLLAMA_HOST` | Ollama server URL | `http://localhost:11434` |
| `OLLAMA_MODEL` | LLM model name | `tinyllama` |
| `CHROMA_DB_PATH` | ChromaDB storage path | `./db` |
| `COLLECTION_NAME` | ChromaDB collection name | `docs` |
| `API_HOST` | API host binding | `0.0.0.0` |
| `API_PORT` | API port | `8000` |
| `USE_MOCK_LLM` | Use mock LLM for testing | `false` |
| `ENVIRONMENT` | Environment (development/production) | `development` |

## 🐳 Docker Support

### Build
```bash
docker build -t knowledgerag:latest .
```

### Run with environment variables
```bash
docker run -p 8000:8000 \
  -e OLLAMA_HOST=http://host.docker.internal:11434 \
  -e USE_MOCK_LLM=false \
  knowledgerag:latest
```

## ☸️ Kubernetes Deployment

The project includes production-ready Kubernetes manifests:

- `deployment.yaml` - Application deployment
- `service.yaml` - Service configuration

**Note:** For production, update the Ollama host configuration in your environment or ConfigMap.

## 🏭 Production Deployment

### Recommended Setup

1. **Run Ollama as a separate service** in Kubernetes
2. **Use ConfigMaps** for non-sensitive configuration
3. **Use Secrets** for sensitive data
4. **Enable health checks** and readiness probes
5. **Set resource limits** appropriately
6. **Use persistent volumes** for ChromaDB data

### Security Checklist

- ✅ No hardcoded credentials
- ✅ Environment-based configuration
- ✅ CORS configured properly
- ✅ Health check endpoints
- ✅ Structured logging
- ✅ Error handling

## 🔄 CI/CD

GitHub Actions workflow is included for:
- Automated testing
- Docker image building
- Linting and code quality checks

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please use the GitHub Issues page.

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Vector search powered by [ChromaDB](https://www.trychroma.com/)
- LLM integration via [Ollama](https://ollama.ai/)

---

Made with ❤️ for the AI community
