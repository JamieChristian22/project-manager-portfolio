# Rollback Plan

## Trigger
Critical data corruption, widespread access failure, core opportunity process failure, Sev 1 defect, or material reconciliation failure.

## Actions
Pause user release, disable affected production activity, preserve logs, remove/revert affected import batches where feasible, restore approved data state, communicate status, and reconvene go/no-go.

## Authority
Sponsor owns business rollback decision; PM coordinates execution; Salesforce Admin and Data Lead perform technical recovery.
