# CRM decision register

These are fictional scenario decisions. The original register supplied phases but no calendar dates or approval attachments. The expanded register assigns accountable roles and specifies the evidence needed without inventing signed approvals.

| ID | Decision and alternative | Rationale / tradeoff | Accountable approver | Trigger / phase | Required evidence |
|---|---|---|---|---|---|
| D1 | Standard Opportunity object; alternative custom object | Reduces customization and maintenance; confirm business-field fit | Sales operations owner + solution owner | Design review | Requirements mapping, access model and report compatibility |
| D2 | Single cutover for 75 users; alternative staged rollout | Simpler synchronization but larger one-time exposure | Sponsor + service owner | Planning gate | Rehearsal timing, reconciliation, rollback and staffing plan |
| D3 | Exclude obsolete records; alternative archive separately and load all active records | Improves quality but can lose history if exclusions are uncontrolled | Business data owner | Trial-load review | Exclusion register, retention rationale and source-count bridge |
| D4 | Move advanced automation to Phase 2; alternative delay launch | Protects committed scope at the cost of deferred benefit | Product/business owner | Sprint 3 scope review | Change request, revised backlog, impact on acceptance and training |
| D5 | Require manager UAT signoff; alternative QA-only acceptance | Adds business ownership but needs representative participants | Sales operations owner | UAT exit | Required/executed/pass counts, defects, exceptions and dated approval |

## Recording and control rules

Each decision needs a decision date, effective baseline/version, approving role, approval reference, affected requirements, cost/schedule impact, conditions and review trigger. Original approval references are **not supplied**. The decisions are scenario descriptions rather than auditable authorizations.

For D3, reconcile source rows = migrated rows + approved exclusions + unresolved rejects. Zero unexplained critical differences is a separate gate from a high migration success percentage. For D4, preserve the rejected/deferred scope so it cannot silently return during cutover. For D2, a failed rehearsal or unproven restore capability reopens the decision.

## Example review agenda

1. Confirm the change or issue requiring a decision and its owner.
2. Compare at least two options with quantified impact and assumptions.
3. Confirm the approver's authority and budget availability.
4. Record the selected option, conditions, due date and evidence.
5. Update linked tasks, risks, tests, communications and baseline only after approval.

The separate [control exercise](../Control_Exercise/README.md) provides machine-checkable examples of missing approval and blocked release. Its records do not authenticate D1–D5.
