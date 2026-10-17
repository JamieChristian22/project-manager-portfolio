# IT modernization: delivery and recovery case

**Role:** Modernization PM. **Original scenario budget:** $425,000. This is a portfolio simulation. The original project snapshot and the supplemental control exercise have different reporting periods. Do not merge their totals or describe the exercise as historical employer work.

## Business problem and scope

The service can appear healthy while losing business events. The delivery decision depends on transaction reconciliation, not merely an available endpoint.

The delivery objective is to resolve **legacy integration silently drops retry messages** while protecting approved scope, service continuity, and acceptance criteria. The exercise covers dependency inventory, interface contract, retry test, parallel run, cutover, retirement approval. Procurement of additional tools, expansion to new business units, and unapproved production changes are outside this exercise.

### Definition of completion

Retrying the same message produces one business transaction and all source IDs reconcile. Completion also requires an accepted operational owner, closure evidence for blocking defects, approved residual risks, and a dated decision record. A completed task without its acceptance evidence is not a passed release gate.

## Accountability and decision rights

| Responsibility | Accountable role | Working evidence |
|---|---|---|
| Track actions, dependencies, and due dates | Modernization PM | tasks.csv and weekly action review |
| Produce technical or operational evidence | Integration lead | tests.csv and evidence descriptions |
| Approve scope, residual risk, and release | Application service owner | gates.csv and decision record |
| Confirm financial capacity | Finance representative | budget.csv and approved change reference |
| Accept ongoing support | Service or operations owner | handoff checklist and open-item disposition |

Decommission only after a complete business cycle reconciles and rollback retention is accepted. A coordinator can recommend and escalate but cannot self-approve a scope change. A PM can organize a decision but cannot replace the technical owner’s validation.

## Delivery plan and dependencies

| Stage | Exit evidence | Stop condition |
|---|---|---|
| Establish baseline | Scope, owner, budget basis, acceptance measures | Unapproved scope or missing owner |
| Prepare solution | Documented option, dependency and resource review | Unresolved critical dependency |
| Rehearse or pilot | Expected and observed results captured | Critical scenario fails or evidence missing |
| Evaluate readiness | Tests, actions, budget and residual risk reviewed together | Any mandatory gate remains open |
| Authorize and hand over | Authorized decision and support owner | Missing approval or rollback capability |
| Review benefits | Comparable measurement period and denominator | Missing baseline or incompatible population |

The exercise schedule uses finish-to-start links and business-day durations. Its computed critical path is a planning model, not proof that the original project used the same network. When a predecessor changes, recalculate the forecast before promising a date. Do not add recovery days from overlapping activities together.

## Decision analysis

**Decision required:** How should the team address legacy integration silently drops retry messages?

| Option | Benefit | Cost/risk | Decision condition |
|---|---|---|---|
| Use an idempotent retry queue with exception monitoring | Addresses the constraint before release | Additional owner time and revalidation | Preferred if evidence can be produced before the gate |
| Keep the legacy interface active for one additional cycle | Preserves a fallback | Additional coordination, scope or date impact | Use only after approver accepts the tradeoff |
| Proceed without resolving the gap | Protects the nominal milestone | Unverified acceptance and avoidable service exposure | Reject while mandatory evidence is missing |

The exercise decision remains **proposed** until application service owner records authorization. Financial and schedule impacts must be quantified from the relevant task and cost rows. The recommendation is not an approval.

## Risk response and escalation

| Risk | Trigger | Owner | Response | Escalation |
|---|---|---|---|---|
| Evidence not ready | Retry and reconciliation review incomplete at review | Integration lead | Timebox remediation and arrange backup | Notify Application service owner before release decision |
| Scope growth | Additional feature or cohort requested | Modernization PM | Record change and quantify impact | Approval before baseline amendment |
| Resource conflict | Named owner cannot meet commitment | Workstream lead | Reassign only with capacity confirmation | Same-day escalation if on critical path |
| Hidden quality failure | Summary metric passes but exception test fails | Quality lead | Reopen gate and repeat the failed path | Immediate release hold |
| Operational ownership gap | No accepted support contact | Operations owner | Complete handoff and escalation path | No transition until accepted |

A probability-impact score supports prioritization but does not override a release-blocking condition. Record risk closure evidence separately from a status label.

## Status communication example

**Reporting basis:** Supplemental exercise day 8, not the original closeout date. **Health: Amber.** The current blocker is legacy integration silently drops retry messages. Integration lead owns the evidence follow-up. The decision requested from Application service owner is whether to accept the preferred recovery option after its estimate and validation are reviewed. The next checkpoint is retry and reconciliation review. Until approval and validation exist, the team should not communicate an unconditional release commitment.

## Acceptance, rollback, and handoff

Before release, verify the acceptance condition above, mandatory tests, owner assignments, approved changes, support contacts, and recovery steps. If a critical check fails, hold the gate, record the observed result, identify the affected task, and route a decision to the accountable owner. Use the existing operational state or approved fallback until a revised plan passes validation.

Handoff must include the runbook location, monitoring or review cadence, support hours, escalation contact, known exceptions, owner acceptance, and the next review date. A residual issue needs an owner, due date, workaround, and explicit acceptance; it must not disappear from the tracker simply because the project closes.

## Benefits and interview discussion

Measure operational improvement using the original source period and denominator. Separate task completion, test pass rate, adoption, and business benefit. Avoid claiming causation from a short simulated trend.

In an interview, explain: the constraint; the two viable options; who had authority; the evidence required; the cost and schedule tradeoff; and what would cause you to reverse the recommendation. Describe this as a designed simulation and demonstrate the reproducible checks. Do not imply that fictional approvals or results came from a client.

## Working files

[Linked exercise and calculation instructions](Control_Exercise/README.md) · [Original artifact index](Evidence_Index.md)
