# Troubleshooting

## Common Issues

### Pod Can't Connect to Ollama
**Error**: "Failed to connect to Ollama"

**Solution**:
- Check Ollama VM is running: `gcloud compute instances list`
- Verify Ollama service: SSH into VM, run `ollama list`
- Check network: `kubectl exec -it <pod> -- curl http://10.162.0.24:11434/api/tags`
- Update OLLAMA_BASE_URL if IP changed

### High Latency on Chat Response
**Cause**: LLM is generating large responses

**Solution**:
- Reduce context window (top_k parameter)
- Use faster LLM model
- Scale replicas: `kubectl scale deployment oracle-rag-api --replicas=5`

### Vector Search Returns No Results
**Cause**: Documents not embedded yet, or wrong query

**Solution**:
- Add documents: `curl -X POST http://api/documents ...`
- Check embedding: Verify embeddings table has data
- Try broader query terms

### High Memory Usage
**Cause**: Large vector index, batch processing

**Solution**:
- Increase pod memory: Edit k8s-deployment.yaml
- Chunk documents smaller (< 500 chars)
- Scale horizontally instead of vertically

### Database Connection Failed
**Error**: "ORACLE_HOST not found"

**Solution**:
- Verify .env file exists
- Check Oracle VM is running
- Confirm network connectivity
- Check tnsnames.ora entry

## Debugging

### View Pod Logs
```bash
kubectl logs -f deployment/oracle-rag-api
```

### SSH into Pod
```bash
kubectl exec -it <pod-name> -- /bin/bash
```

### Check GKE Events
```bash
kubectl describe nodes
kubectl describe pod <pod-name>
```

### Test API Manually
```bash
curl -X POST http://34.19.151.78/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "test"}'
```

## Performance Tuning

### Embedding Generation
- Cache embeddings to avoid regeneration
- Batch embed documents
- Use GPU-accelerated Ollama (if available)

### Vector Search
- Increase HNSW neighbors for accuracy
- Decrease for speed
- Monitor index size

### LLM Inference
- Increase context window for better answers
- Decrease for faster generation
- Use quantized models for speed

## Cost Optimization

- Use GCP Committed Use Discounts
- Enable autoscaling to right-size resources
- Monitor Cloud Billing alerts
- Archive old documents in Oracle

See MONITORING.md for metrics dashboard setup.
