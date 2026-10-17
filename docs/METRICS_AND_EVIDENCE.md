# Metric and evidence rules

## Source hierarchy

The original artifacts describe their own scenario snapshot. Supplemental Control_Exercise records describe a separate tabletop exercise and must never be combined with original budgets or reported as original test evidence. Calculated_Status.md is generated from that exercise's CSVs. Source file inventory is not a claim of live execution.

## Measures that must remain distinct

| Measure | Correct interpretation | Common error to avoid |
|---|---|---|
| Task completion | Completed tasks / tasks in the named population | Final-week delivery is not all-project completion |
| Test pass rate | Passed / required, with executed coverage shown | Excluding not-run tests can conceal missing coverage |
| Adoption | Active eligible users / eligible users during the named window | Training completion does not establish actual usage |
| Training completion | Completed / attended, or completed / target; label denominator | These two percentages answer different questions |
| Budget variance | Authorized baseline minus forecast, positive favorable | Treating unapproved change as available funding |
| Forecast | Actual plus remaining cost estimate | Adding actual to the full commitment double-counts spend |
| Remaining reserve | Opening reserve less approved draws | Under-budget performance does not automatically replenish reserve |
| Schedule progress | Explicit task-count, duration-weighted, or earned-value basis | Comparing differently weighted percentages as equivalent |
| EVM forecast | Model output under stated productivity assumptions | Equating CPI-based EAC with bottom-up management forecast |
| Weekly issue count | Point-in-time open stock | Summing weekly open issues counts the same issue repeatedly |

## Workbook interpretation

Several legacy manager workbooks are static snapshots. Do not describe them as formula-driven models. The construction workbook uses both average task progress and cost-based earned value; these are different measures. Its approved-change total and budget revisions require a reconciled change bridge before they can be treated as the same funding measure. Preserve the original snapshot and disclose that limitation.

Coordinator workbook reserve lines add favorable variance to a starting reserve. That is an illustrative capacity calculation, not evidence of an authorized contingency transfer. Treat the base-budget reconciliation separately. Training regional totals and weekly activity have different populations; do not add them together. Satisfaction averages are not respondent-weighted without response counts. CRM Week 1 migration/UAT rates with zero activity mean not measured, not a demonstrated zero-percent quality result.

## Evidence needed for stronger claims

A native-tool claim needs a saved project/workbook, its version, instructions, and a demonstrated calculation or export. An approval needs an authorized role, date, decision scope, conditions, and evidence reference. A production outcome needs a defined baseline, comparable observation period, denominator, and source. If these are unavailable, label the claim as a scenario assumption or an unverified capability.
