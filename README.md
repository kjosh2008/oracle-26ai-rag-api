# Oracle 26ai RAG API

Production-grade Retrieval-Augmented Generation (RAG) API powered by Oracle 26ai vector search, Ollama LLM inference, and FastAPI.

## Features

- **Semantic Search** — Oracle 26ai HNSW vector indexing (768-dim embeddings)
- **RAG Pipeline** — Retrieve relevant documents and generate answers with context
- **LLM Inference** — Ollama llama3.2 for fast local processing
- **Auto-scaling** — Kubernetes HPA (2-5 replicas based on CPU)
- **Production Ready** — Logging, monitoring, error handling
- **Zero Cost** — Deployed on GCP free tier

## Quick Start

### Local Development

```bash
# Clone repo
git clone https://github.com/kjosh2008/oracle-26ai-rag-api.git
cd oracle-26ai-rag-api

# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure .env
cp .env.example .env
# Edit .env with your Oracle & Ollama credentials

# Run locally
python3 app/main.py
# API available at http://localhost:8080
```
## System Architecture

```
Frontend (Cloud Run)
    ↓ HTTP/REST
Backend API (GKE)
    ↓
┌─────────────────┐
│  Ollama Server  │  (llama3.2, embeddings)
├─────────────────┤
│  Oracle 26ai    │  (vector database, RAG)
└─────────────────┘
```

**POST /chat** — Ask a question
```bash
curl -X POST http://localhost:8080/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What technologies are used?"}'
```

Response:
```json
{
  "answer": "...",
  "sources": ["Document1", "Document2"],
  "context_used": true
}
```

**POST /search** — Semantic search
```bash
curl -X POST http://localhost:8080/search \
  -H "Content-Type: application/json" \
  -d '{"query": "vector database", "top_k": 5}'
```

**POST /documents** — Add documents to RAG
```bash
curl -X POST http://localhost:8080/documents \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Document",
    "content": "Document content here...",
    "doc_type": "general"
  }'
```

**GET /health** — Health check
```bash
curl http://localhost:8080/health
```

## Architecture
FastAPI Server
↓
LangChain RAG Pipeline
↓
┌─────────────────────────┐
│ Oracle 26ai             │
│ Vector Database         │
│ HNSW Index (768-dim)    │
└─────────────────────────┘
↓
Document Chunks + Embeddings
↓
Ollama llama3.2 (LLM Inference)

## Deployment

### GKE Kubernetes
```bash
kubectl apply -f k8s-deployment.yaml
kubectl scale deployment oracle-rag-api --replicas=3
```

### Docker
```bash
docker build -t oracle-rag-api.
docker run -p 8080:8080 oracle-rag-api
```

## Configuration

Environment variables (see `.env.example`):
- `ORACLE_HOST` — Oracle 26ai database host
- `ORACLE_PORT` — Database port (1521)
- `ORACLE_SERVICE` — PDB service name
- `ORACLE_USER` — Database user
- `ORACLE_PASSWORD` — Database password
- `OLLAMA_BASE_URL` — Ollama server URL
- `OLLAMA_EMBED_MODEL` — Embedding model (nomic-embed-text)
- `OLLAMA_CHAT_MODEL` — Chat model (llama3.2)

## Monitoring

- **GCP Cloud Logging** — Real-time logs
- **GCP Cloud Monitoring** — Metrics & dashboards
- **Kubernetes Metrics** — Pod CPU/memory usage

## Tech Stack

- **Framework** — FastAPI, Python 3.12
- **Database** — Oracle 26ai (vector search)
- **LLM** — Ollama (llama3.2, nomic-embed-text)
- **Orchestration** — LangChain
- **Deployment** — GKE Kubernetes
- **CI/CD** — GitHub Actions

## Status

- ✅ Production ready
- ✅ Auto-scaling enabled
- ✅ Monitoring configured
- ✅ CI/CD pipeline active

## Related Projects

- **[oracle-26ai-rag-api](https://github.com/kjosh2008/oracle-26ai-rag-api)** — RAG backend API
- **[oracle-26ai-chat](https://github.com/kjosh2008/oracle-26ai-chat)** — Frontend web interface
- **[oracle-26ai-ollama](https://github.com/kjosh2008/oracle-26ai-ollama)** — LLM inference server


## License

MIT

## Support

Issues? Open a GitHub issue or check the Wiki for troubleshooting.
