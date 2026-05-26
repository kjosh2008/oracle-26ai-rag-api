# Security

## Credentials Management

### Environment Variables
- Store in GCP Secret Manager
- Never commit .env to git
- Use .env.example as template
- Rotate credentials regularly

### Database Credentials
- Change Oracle password quarterly
- Use service accounts (not admin)
- Enable audit logging
- Restrict network access

## Network Security

### Firewall Rules
- Restrict API access to frontend only
- Limit Ollama access to GKE pods
- Use VPC Service Controls

### API Security
- Enable CORS only for trusted domains
- Implement rate limiting
- Use HTTPS in production
- Validate all inputs

## Data Protection

### Encryption
- Enable encryption at rest in Oracle
- Use TLS for in-transit data
- Encrypt backups
- Key rotation: quarterly

### Backups
- Daily snapshots of Oracle
- Store in separate region
- Test restore regularly
- Encrypt backup storage

## Compliance

### Logging
- Enable Cloud Audit Logs
- Retain logs 90 days minimum
- Monitor for security events
- Alert on suspicious activity

### Access Control
- Use service accounts with minimal permissions
- Implement RBAC in GKE
- Audit user access monthly
- Disable unused service accounts

## Best Practices

1. Never log sensitive data
2. Validate all user inputs
3. Use dependency scanning
4. Keep libraries updated
5. Regular security audits

## Incident Response

If compromised:
1. Rotate all credentials immediately
2. Check audit logs for unauthorized access
3. Update firewall rules
4. Notify users if data exposed
5. Post-incident review

Contact: security@example.com
