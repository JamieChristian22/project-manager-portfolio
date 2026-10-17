# Monitoring & Alerting Plan
| Signal | Threshold/condition | Severity | Action |
|---|---|---|---|
|EC2 CPU|≥80% for 5 min|P2|Investigate load; confirm ASG action|
|ALB unhealthy targets|>0 sustained|P1/P2|Check app/instance health|
|HTTP 5xx|Above baseline|P1/P2|Inspect app/ALB logs|
|Latency|Above agreed threshold|P2|Check capacity/database|
|RDS connections|Near capacity|P2|Investigate pooling/load|
|Backup failure|Any scheduled failure|P1|Re-run and verify recovery point|
|Disk/storage trend|Capacity risk|P3|Plan expansion/cleanup|
Dashboard views: availability, request/error rate, latency, CPU, healthy hosts, DB connections, backup status.
