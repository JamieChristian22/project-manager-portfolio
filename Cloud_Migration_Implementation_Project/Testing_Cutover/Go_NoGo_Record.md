# Cloud cutover decision record

**Original simulation decision: GO. Evidence status: scenario assertion, not a verified production authorization.** The source narrative states that backup, rollback, target health, critical UAT, staffing, communications and monitoring were reviewed, with rollback retained for 24 hours. It does not supply a dated approver record or execution attachments.

## Required decision matrix

| Gate | Acceptance | Evidence owner | Required record |
|---|---|---|---|
| Data | All critical records reconcile; approved exclusions identified | Migration lead | Source/target counts, exception disposition, cutover watermark |
| Recovery | Restore and rollback complete within agreed windows | Operations lead | Timed rehearsal, recovery point and verification results |
| Application | Critical user journeys pass in target | QA/business owner | Versioned cases and observed results |
| Security | Approved access and monitoring in place | Security owner | Role review, alert test and residual-risk decision |
| Operations | Named on-call coverage and runbook accepted | Service owner | Roster, escalation path and handoff acceptance |
| Change authority | Authorized scope, timing and funding | Sponsor/change authority | Dated decision and change reference |

## Stop and rollback rules

Do not start the traffic switch if any mandatory evidence is missing. Stop if critical reconciliation fails, a critical journey fails, security validation fails, or the planned recovery window would be breached. The technical lead assesses recovery feasibility; the authorized decision owner chooses hold, rollback, or a revised plan. A PM records the decision and stakeholder communication rather than treating a green task list as authorization.

Retaining a backup for 24 hours does not itself prove an acceptable recovery point or recovery time. Specify data-write handling, DNS/traffic reversal, queue reconciliation, verification, and who confirms restoration before declaring rollback complete.

## Record completion

The original approver, date, environment version, rehearsal identifiers, exception list and approval reference are not supplied. Keep these fields explicit when presenting the scenario. The separate [restore control exercise](../Control_Exercise/README.md) demonstrates a HOLD condition until its linked records are complete.
