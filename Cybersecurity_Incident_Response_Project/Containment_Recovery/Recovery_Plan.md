# Recovery Plan

## Sequence
Restore affected users in business-priority order after credential reset, MFA enrollment, session cleanup, permission validation, and endpoint/account review.

## Heightened Monitoring
For five business days, review failed-login rates, success-after-failure alerts, privileged changes, outbound anomalies, and account lockouts twice daily.

## Rollback
If suspicious activity recurs, re-lock the identity, invalidate sessions, isolate related assets as appropriate, and return to containment.

## Recovery Approval
Requires IAM validation, security validation, business-owner confirmation, and incident coordinator documentation.
