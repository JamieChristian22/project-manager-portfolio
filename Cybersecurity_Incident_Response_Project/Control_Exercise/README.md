# Incident response coordination: linked control exercise

**Separate fictional tabletop scenario.** These records were created to demonstrate controls, not to reconstruct the original project. The exercise budget is $7,000 and is not additive to the original $85,000 scenario budget. Day numbers are business days relative to this exercise's start, not calendar dates. The issue is intentionally unresolved; a correct readiness calculation must return **HOLD**.

## Follow the evidence

1. [Requirements](requirements.csv) define ownership and acceptance.
2. [Tasks](tasks.csv) reference requirements and finish-to-start predecessors.
3. [Tests](tests.csv) reference both requirements and tasks. [Evidence](evidence.csv) explicitly identifies fictional demonstration records.
4. [Issue ISS-01](issues.csv) links to [decision DEC-01](decisions.csv) and [follow-up actions](actions.csv).
5. [Budget](budget.csv) separates baseline, approved change, actual, and estimate to complete. Pending decisions do not change the authorized baseline.
6. [Release gate](gates.csv) requires mandatory tests, completed tasks, no open high/critical issues, no open actions, and authorized approval.

## Reproduce

From the repository root, run `python scripts/validate_portfolio.py`. Read [the calculated report](Calculated_Status.md). The script performs a forward and backward schedule pass, calculates float, recomputes forecast costs, checks record references, and prevents unapproved release. It uses Python's standard library.

## Working definitions

- Forecast cost = actual cost + estimate to complete. Actual is incurred cost, not the full commitment value.
- Authorized budget = baseline + approved changes. Do not include a proposed change before authorization.
- Favorable variance = authorized budget − forecast cost. Negative values indicate an overrun.
- Schedule starts at day 0. Finish = start + duration. Parallel tasks share a predecessor and are not summed as serial work.
- Test rate = passed tests / all required tests, including tests not yet run. Execution coverage is reported separately.
- A missing owner, broken reference, absent pass evidence, or missing approval cannot be interpreted as success.

## Practice a recovery decision

Make a disposable copy. Increase T-03 duration from 4 to 7 days, rerun, and inspect the final finish and float. Add an open critical issue and confirm the gate remains HOLD. To model release, supply actual simulated results and evidence for every remaining requirement, complete the task and action records, resolve the issue with evidence, record an approved decision with a day, and obtain gate approval with a day. Never change status labels alone to manufacture readiness.

## Meeting agenda and action discipline

Review overdue actions first, then session revocation evidence, the options in DEC-01, forecast movement, resource commitments, and release gates. Read each action back with its owner and due day. If a commitment is missed, retain the original due day and explain the revised forecast in the decision record. Distribute an updated status only after owners confirm it.

## Handoff checklist

- Support owner and escalation path accepted.
- Operational instructions and fallback steps available.
- Open exceptions retained with owner and review date.
- Acceptance measures use a stated population and reporting period.
- Authorized decision links to test evidence and financial exposure.
