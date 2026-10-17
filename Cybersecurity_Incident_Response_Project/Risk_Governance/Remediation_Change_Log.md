# Remediation Change Log

| CHG | Change | Reason | Risk | Approval | Validation |
|---|---|---|---|---|---|
| 001 | Enforce MFA on scoped accounts | Reduce credential-only compromise | User access disruption | Security/IAM | 100% enrollment |
| 002 | Lower failed-login alert threshold | Earlier detection | False positives | SOC Lead | Test cases pass |
| 003 | Add multi-account source correlation | Detect spraying | SIEM load | SOC Lead | Synthetic scenario fires |
| 004 | Block high-confidence scenario IOCs | Stop repeated attempts | Accidental block | Network Lead | No approved business traffic affected |
| 005 | Privileged access recertification | Reduce blast radius | Admin delay | Security Lead | Exceptions documented |
