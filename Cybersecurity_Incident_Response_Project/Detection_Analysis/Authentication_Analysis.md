# Authentication Analysis

## Prioritization
Tier 1: five accounts with >150 failures or a successful login following a failure burst.
Tier 2: accounts with 50-149 failures from shared suspicious sources.
Tier 3: remaining targeted accounts for validation and monitoring.

## Findings
The highest-risk account recorded 312 failures followed by a successful login from a source not observed in its normal baseline. That event triggered session invalidation, credential reset, MFA verification, and access review. Four additional accounts had 180-265 failures but no confirmed successful authentication.

## Validation Questions
Was the successful login expected? Was MFA satisfied? Was the device known? Did privilege or resource access change? Did the account generate unusual outbound activity? Answers determine whether the event remains suspicious or becomes confirmed compromise.
