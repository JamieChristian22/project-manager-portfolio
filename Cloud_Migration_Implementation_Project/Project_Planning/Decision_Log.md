# Decision Log
| ID | Decision | Rationale | Date/Phase |
|---|---|---|---|
|DEC-01|Use replatform approach for database|Managed RDS reduces administration and improves resilience|Design|
|DEC-02|Use ALB + Auto Scaling for web tier|Supports health checks and elastic capacity|Design|
|DEC-03|Pre-stage bulk data before cutover|Protects two-hour outage objective|Pilot|
|DEC-04|No go-live with Sev-1 open defect|Protects service continuity|Planning|
|DEC-05|Retain rollback point for 24 hours|Allows controlled recovery if production validation fails|Cutover|
