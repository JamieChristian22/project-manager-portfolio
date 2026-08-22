# Discovery & Assessment
## Source Inventory
| Asset | Current state | Dependency | Criticality | Disposition |
|---|---|---|---|---|
|WEB01|On-prem web server|DB01, file assets|High|Rehost to EC2/ASG image|
|WEB02|On-prem web server|DB01, file assets|High|Rehost to EC2/ASG image|
|DB01|On-prem relational DB|Web tier|High|Replatform to RDS|
|FILE01|Static assets/backups|Web tier|Medium|Move to S3|
|Monitoring|Local/manual|All|High|Replace with CloudWatch|
## Assessment Findings
Single-site dependency, limited redundancy, manual scaling, inconsistent alerting, and backup verification risk. No blocker found for the selected rehost/replatform approach after pilot validation.
