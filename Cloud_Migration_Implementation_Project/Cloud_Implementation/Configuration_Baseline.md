# Configuration Baseline
| Component | Scenario baseline |
|---|---|
|VPC|10.20.0.0/16 across 2 AZs|
|Web subnets|10.20.10.0/24, 10.20.20.0/24|
|DB subnets|10.20.110.0/24, 10.20.120.0/24|
|ASG|min 2, desired 2, max 4|
|Scale-out|Average CPU ≥70% for sustained period|
|CloudWatch CPU alarm|≥80% for 5 minutes|
|ALB health|HTTP application health endpoint|
|RDS|Managed relational DB, Multi-AZ scenario design|
|Backups|Daily recovery point + pre-cutover snapshot|
|Tagging|Project, Environment, Owner, CostCenter, ManagedBy|
