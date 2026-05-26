# Architecture

## System Design
┌──────────────────┐
│  Frontend (React)│
└────────┬─────────┘
│ HTTP/REST
┌────────▼──────────────┐
│  FastAPI Backend      │
│  - Chat endpoint      │
│  - Search endpoint    │
│  - Documents endpoint │
└────────┬──────────────┘
│
┌────┴────────────┐
│                 │
┌───▼────────┐  ┌────▼──────────┐
│ Oracle 26ai│  │ Ollama        │
│ Vector DB  │  │ LLM Inference │
│ (HNSW)     │  │ (llama3.2)    │
└────────────┘  └───────────────┘

## Data Flow

1. **User Query** → Frontend sends question via API
2. **Semantic Search** → Backend queries Oracle 26ai for relevant documents
3. **Context Retrieval** → Fetch top-5 similar chunks
4. **LLM Generation** → Ollama generates answer with context
5. **Response** → Return answer + sources to frontend

## Vector Index

- **Type**: HNSW (Hierarchical Navigable Small World)
- **Dimensions**: 768 (nomic-embed-text output)
- **Distance**: Cosine similarity
- **Parameters**: neighbors=32, efConstruction=200

## Deployment

### Kubernetes
- **Cluster**: GKE (Google Kubernetes Engine)
- **Replicas**: 2-5 (auto-scaling based on CPU)
- **Resources**: e2-medium nodes
- **Network**: VPC with firewall rules

### Scaling
- **Horizontal**: HPA scales pods based on CPU usage
- **Vertical**: Node machine type can be increased
- **Database**: Oracle 26ai is separate, always available

## Security

- **Network**: VPC isolation, firewall rules
- **Secrets**: GCP Secret Manager
- **API**: CORS enabled for frontend only
- **Database**: Encrypted connections

See SECURITY.md for details.
