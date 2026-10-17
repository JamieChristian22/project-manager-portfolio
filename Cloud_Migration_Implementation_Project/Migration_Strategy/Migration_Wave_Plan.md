# Migration Wave Plan
| Wave | Scope | Strategy | Window | Success criterion |
|---|---|---|---|---|
|0|Foundation|Build|Weeks 4-6|Network/security/monitoring validated|
|1|Static assets + nonprod web|Rehost|Week 7|Functional + performance tests pass|
|2|Database rehearsal|Replatform|Week 7-8|Restore/sync within RTO/RPO|
|3|Production web + DB|Rehost/replatform|Week 9-10|100% validation; traffic switched|
|4|Legacy retirement|Retire|After 24h rollback hold|Sponsor/ops approval|
Entry criteria: approved design, backup, rollback, owners present. Exit criteria: validation complete, defects accepted, monitoring green, documentation updated.
