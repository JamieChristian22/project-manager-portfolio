# Work Breakdown Structure & 12-Week Schedule
| Wk | Work package | Deliverable | Owner | Exit criterion |
|---:|---|---|---|---|
|1|Initiation|Charter/business case|PM|Sponsor approval|
|2|Discovery|Inventory/dependencies|Cloud Lead|100% scoped assets assessed|
|3|Design|Architecture/security design|Architect|Design approval|
|4|Foundation|VPC/IAM/logging|Cloud Eng|Foundation checks pass|
|5|Platform build|ALB/EC2/ASG/RDS/S3|Cloud Eng|Build validated|
|6|Observability|Dashboards/alarms/backups|Ops|Alert + restore tests pass|
|7|Pilot|Pilot migration|Migration Lead|Pilot exit approved|
|8|Remediation|Defects/performance tuning|Team|No critical pilot blockers|
|9|Production migration|Data/app sync|Migration Lead|Validation passed|
|10|Cutover|DNS/traffic switch|PM + Tech Lead|Go-live approved|
|11|Hypercare|Stabilization/handoff|Ops|SLA stable, docs accepted|
|12|Closeout|Lessons/closure|PM|Sponsor closure approval|
Critical path: design → foundation → platform build → pilot → remediation → production migration → cutover.
