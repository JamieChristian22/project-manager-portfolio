# Threat Indicator Log

| ID | Indicator | Type | Confidence | Action | Status |
|---|---|---|---|---|---|
| IOC-01 | 198.51.100.24 | Scenario IP | High | Block and search logs | Closed |
| IOC-02 | 203.0.113.77 | Scenario IP | High | Block and correlate | Closed |
| IOC-03 | 192.0.2.45 | Scenario IP | Medium | Monitor and investigate | Closed |
| BEH-01 | Multi-account failed login burst | Behavior | High | SIEM rule | Implemented |
| BEH-02 | Success after repeated failures | Behavior | High | High-priority alert | Implemented |
| NET-01 | 2.8x outbound baseline | Behavior | Medium | Correlate destination/user/host | Investigated |

All addresses use documentation-only IP ranges and are not asserted to be real malicious infrastructure.
