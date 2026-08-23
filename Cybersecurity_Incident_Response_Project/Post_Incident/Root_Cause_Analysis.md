# Root Cause Analysis

## Problem Statement
The environment allowed abnormal credential-attack activity to reach a volume requiring coordinated incident response before preventive and detective controls fully interrupted it.

## Root Cause Theme
Authentication-control and proactive-monitoring maturity was insufficient for the observed attack pattern.

## Contributing Factors
Incomplete MFA coverage on scoped accounts; alert logic did not correlate multi-account spraying early enough; success-after-failure behavior lacked a dedicated high-priority rule; outbound anomaly analysis required manual cross-source correlation.

## Not Claimed
The scenario does not establish a named attacker, malware infection, confirmed data theft, or definitive credential compromise beyond the modeled suspicious event requiring containment.
