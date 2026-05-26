# Deployment

Local: python3 app/main.py
Docker: docker build -t oracle-rag-api .
GKE: kubectl apply -f k8s-deployment.yaml
