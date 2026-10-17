# Incident Classification

## Severity Model
SEV-1 Critical: confirmed widespread compromise, material data loss, or major service outage.
SEV-2 High: credible compromise indicators with significant account/data risk requiring coordinated response.
SEV-3 Medium: contained suspicious activity with limited impact.
SEV-4 Low: informational or low-risk event.

## Classification Decision
IR-2026-008 is SEV-2 because multiple identities were targeted, automated credential-attack patterns were present, one post-failure successful authentication required validation, and outbound-transfer anomalies could not initially be dismissed. No evidence in the scenario justifies declaring confirmed exfiltration or widespread compromise.

## Escalation Triggers
Escalate to SEV-1 if privileged compromise is confirmed, sensitive-data exfiltration is validated, lateral movement is established, or critical services are materially disrupted.
