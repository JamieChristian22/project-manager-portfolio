# Scope & Requirements Baseline
## In Scope
Discovery, dependency mapping, AWS account controls, VPC/networking, IAM roles, EC2 web tier, ALB, Auto Scaling, RDS, S3, CloudWatch, backup/restore, migration execution, UAT, cutover, hypercare, documentation and handoff.
## Out of Scope
New application features; mobile redesign; enterprise SSO replacement; unrelated file servers; multi-region active-active.
## Functional Requirements
FR-01 portal serves authenticated user traffic; FR-02 application reads/writes database; FR-03 static assets stored/retrieved; FR-04 backups restorable; FR-05 alerts delivered to operations.
## Nonfunctional Requirements
NFR-01 availability ≥99.9%; NFR-02 encrypted traffic; NFR-03 least-privilege access; NFR-04 CPU alarm at ≥80% for 5 minutes; NFR-05 RPO ≤24h and RTO ≤4h for scenario workload; NFR-06 cutover outage ≤2h; NFR-07 tagged resources for cost ownership.
## Acceptance
All critical requirements pass testing; no Sev-1 defects; sponsor and operations owner sign acceptance.
