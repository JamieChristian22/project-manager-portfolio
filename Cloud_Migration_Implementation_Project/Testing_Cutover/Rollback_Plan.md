# Rollback Plan
## Trigger Conditions
Sev-1 defect; data integrity failure; >30 minutes of unexplained critical errors; inability to complete a critical business transaction; target infrastructure instability that cannot be corrected within the decision window.
## Procedure
Stop new writes where possible; announce rollback; revert traffic/DNS to source; validate source health; reconcile transactions created during the cutover window; confirm user access; open incident/problem record; preserve target logs; reschedule migration after root-cause review.
## Decision Authority
PM coordinates; Technical Lead recommends; App Owner validates business impact; Sponsor is accountable for final business decision when time permits.
