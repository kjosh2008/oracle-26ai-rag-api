# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-05-26

### Added
- RAG chat endpoint with source attribution (`POST /chat`)
- Semantic search via Oracle 26ai HNSW indexing (`POST /search`)
- Document management (`POST /documents`)
- LLM inference with Ollama (llama3.2)
- Embedding generation with nomic-embed-text (768-dim)
- Auto-scaling Kubernetes deployment (HPA 2-5 replicas)
- Health check endpoint (`GET /health`)
- Comprehensive logging and error handling
- Docker containerization
- GKE Kubernetes manifests
- GitHub Actions CI/CD pipeline
- Extensive documentation and wiki

### Infrastructure
- FastAPI REST API
- Oracle 26ai vector database
- Ollama LLM inference
- LangChain orchestration
- GCP Cloud Logging & Monitoring
- Kubernetes auto-scaling

### Documentation
- Comprehensive README
- Architecture diagrams
- API reference
- Deployment guide
- Troubleshooting wiki
- Configuration examples

## [1.1.0] - Planned

### Planned Features
- [ ] Firebase Authentication
- [ ] Rate limiting & quotas
- [ ] Response caching layer
- [ ] Batch document upload
- [ ] Performance benchmarks
- [ ] Advanced monitoring dashboard
- [ ] Multi-document RAG improvement

## [1.2.0] - Planned

### Future Improvements
- [ ] Database query optimization
- [ ] Custom embedding models
- [ ] Webhook support
- [ ] Advanced RAG techniques (reranking, etc.)
- [ ] GraphQL API option
