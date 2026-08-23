# SIEM Enhancement Plan

## New/Improved Rules
1. Multi-account failures from common source.
2. High failures against a single identity.
3. Successful login following abnormal failure burst.
4. Privileged login from new source/device.
5. Authentication anomaly followed by unusual outbound transfer.

## Operations
Each rule has severity, owner, response playbook, suppression logic, test case, and review cadence. False positives are tracked monthly. Critical log-source health is monitored so detection failures become visible.
