# Security, Backup & Recovery Plan
- IAM roles follow least privilege; no shared administrator credentials.
- Security groups allow only required inbound paths; database is not publicly exposed.
- Encryption required in transit; storage encryption enabled for scenario design.
- CloudWatch logs/metrics centralized for operational visibility.
- Daily database backups and retained recovery points; S3 versioning/lifecycle considered for protected assets.
- Scenario RPO: 24 hours maximum; RTO: 4 hours maximum.
- Restore test performed before production cutover and documented as pass.
- Access review and operational owner signoff required before closure.
