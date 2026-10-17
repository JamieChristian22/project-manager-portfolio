# Business Case
## Current State
Two aging on-premises application servers and a single database host support a customer portal. Capacity is manually provisioned, alerting is fragmented, backup validation is inconsistent, and hardware replacement is approaching.
## Drivers
1. Improve resilience and scalability. 2. Establish centralized monitoring. 3. Reduce hardware refresh exposure. 4. Define recovery objectives. 5. Improve access control and auditability.
## Options Considered
| Option | Benefit | Limitation | Decision |
|---|---|---|---|
| Refresh on-prem hardware | Familiar operations | Upfront capital, limited elasticity | Reject |
| Lift-and-shift only | Fast | Carries operational weaknesses forward | Partial |
| Replatform web tier + managed database | Resilience, monitoring, scalability | Moderate change effort | **Selected** |
## Expected Benefits
Target 99.9% availability; autoscaling for peak demand; centralized metrics/alarms; validated backups; lower infrastructure administration burden; monthly cost visibility.
## Financial Summary
Approved one-time project budget: **$125,000**. Scenario final spend: **$122,000**, a **$3,000 / 2.4% favorable variance**.
