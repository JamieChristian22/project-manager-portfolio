# Incident Charter

Incident ID: IR-2026-008
Incident name: Credential Attack & Suspicious Transfer Investigation
Severity: SEV-2 / High
Coordinator: Project Manager / Incident Response Coordinator

## Purpose
Coordinate rapid investigation and containment of abnormal authentication activity while protecting business operations, preserving evidence, validating recovery, and driving corrective action.

## Scope
Authentication logs, affected identities, suspicious source indicators, relevant outbound-transfer telemetry, IAM controls, SIEM alerting, recovery validation, communications, and remediation governance.

## Out of Scope
Attribution to a named threat actor, criminal prosecution, malware reverse engineering, public breach notification unless evidence establishes a reportable event, and unsupported claims of confirmed exfiltration.

## Objectives
Contain high-risk identities within four hours of SEV-2 declaration; review all prioritized accounts; reset suspected compromised credentials; enforce MFA; investigate outbound anomalies; validate critical logging; restore secure access; assign every corrective action.

## Constraints
Limited scenario telemetry, need to minimize user disruption, preservation of evidence, cross-functional availability, and requirement to distinguish indicators from confirmed compromise.

## Exit Criteria
Containment complete, recovery validated, critical risks owned, no open critical incident action without owner, executive closure approved, and remediation backlog transferred.
