# 🔐 Cybersecurity Incident Response Project

## Security Incident Coordination, Threat Analysis & Remediation

![Project Management](https://img.shields.io/badge/Project-Management-blue)
![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Incident Response](https://img.shields.io/badge/Incident-Response-critical)
![NIST](https://img.shields.io/badge/Framework-NIST-purple)
![SIEM](https://img.shields.io/badge/Security-SIEM-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Portfolio](https://img.shields.io/badge/Portfolio-Project-green)

---

## 📌 Executive Summary

This portfolio project demonstrates the end-to-end management and coordination of a **simulated enterprise cybersecurity incident** involving abnormal authentication activity consistent with brute-force and password-spraying behavior, suspicious account activity, and outbound-traffic indicators requiring investigation.

As the simulated **Cybersecurity Incident Response Project Manager / Incident Response Coordinator**, I managed the response across detection, triage, classification, investigation, containment, eradication, recovery, security remediation, stakeholder communication, risk management, executive reporting, KPI tracking, root-cause analysis, lessons learned, and formal incident closure.

The project combines **cybersecurity incident response with technical project management**, demonstrating how security operations, identity administration, networking, systems, risk, compliance, business stakeholders, and executive leadership can be coordinated during a high-priority security event.

> **Portfolio Disclosure:** This is a simulated professional portfolio project. Organizations, users, budgets, incident metrics, timelines, stakeholders, costs, and response outcomes are scenario-based unless specifically identified as genuine technical lab evidence.

---

## 🎯 Project Snapshot

| Attribute                | Details                                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Project**              | Cybersecurity Incident Response & Security Remediation                                                           |
| **Role**                 | Project Manager / Incident Response Coordinator                                                                  |
| **Domain**               | Cybersecurity                                                                                                    |
| **Incident Type**        | Credential Attack / Potential Account Compromise                                                                 |
| **Primary Threats**      | Brute Force, Password Spraying, Unauthorized Access                                                              |
| **Additional Indicator** | Suspicious Outbound Traffic                                                                                      |
| **Framework**            | NIST-Aligned Incident Response                                                                                   |
| **Analysis Environment** | SIEM, Security Logs, Excel                                                                                       |
| **Scenario Budget**      | $85,000                                                                                                          |
| **Status**               | Completed                                                                                                        |
| **Primary Goal**         | Contain suspicious activity, protect accounts and systems, restore secure operations, and reduce recurrence risk |

---

## 🚨 Incident Scenario

The simulated organization experienced a significant increase in failed authentication attempts across multiple user accounts.

Security monitoring identified:

* High volumes of failed login attempts
* Repeated authentication attempts within short time intervals
* Multiple targeted user accounts
* Patterns consistent with brute-force activity
* Patterns consistent with password spraying
* Suspicious source-IP activity
* Abnormal login behavior
* Increased outbound network activity
* Potential indicators requiring investigation for unauthorized data transfer

The incident required coordinated investigation to determine whether credentials had been compromised, whether unauthorized access had occurred, and whether suspicious activity had progressed beyond authentication attempts.

---

## 🏢 Business Problem

A successful credential-based attack could expose the organization to:

* Unauthorized access
* Account compromise
* Sensitive-data exposure
* Lateral movement
* Data exfiltration
* Operational disruption
* Regulatory exposure
* Financial loss
* Reputational damage
* Increased recovery costs

Leadership required a rapid and structured incident response while preserving enough evidence to understand the scope, cause, business impact, and corrective actions required.

---

## 🎯 Incident Response Objectives

The response was designed to:

1. Detect suspicious authentication activity
2. Determine incident severity
3. Identify potentially compromised accounts
4. Analyze failed and successful login patterns
5. Identify suspicious source activity
6. Investigate abnormal outbound traffic
7. Contain potentially compromised accounts
8. Prevent additional unauthorized authentication
9. Preserve relevant incident evidence
10. Coordinate technical response teams
11. Maintain stakeholder communication
12. Restore secure authentication
13. Validate system integrity
14. Strengthen authentication controls
15. Implement MFA
16. Improve monitoring and alerting
17. Track corrective actions
18. Perform root-cause analysis
19. Capture lessons learned
20. Transition remediation into ongoing security operations

---

## 🧭 Incident Response Lifecycle

The project followed a structured NIST-aligned incident-response lifecycle.

```text
Preparation
    ↓
Detection & Analysis
    ↓
Triage & Classification
    ↓
Containment
    ↓
Eradication
    ↓
Recovery
    ↓
Post-Incident Review
    ↓
Security Remediation
    ↓
Incident Closure
```

---

## 🛡️ Phase 1 — Preparation

Preparation established the governance and technical foundations required to respond effectively.

Activities included:

* Defining incident-response roles
* Establishing escalation paths
* Identifying critical stakeholders
* Defining incident severity levels
* Establishing communication channels
* Identifying required log sources
* Establishing evidence-handling expectations
* Reviewing authentication policies
* Defining incident documentation standards
* Preparing response checklists

Preparation reduced uncertainty once suspicious activity was detected.

---

## 🔍 Phase 2 — Detection & Analysis

Security events were analyzed to identify patterns associated with unauthorized authentication attempts.

### Authentication Analysis

The investigation reviewed:

* Failed login volume
* Login frequency
* Targeted accounts
* Source IP activity
* Repeated authentication attempts
* Successful logins following repeated failures
* Authentication timestamps
* Account lockouts
* Abnormal login patterns

### User Account Analysis

Accounts with significantly elevated authentication failures were prioritized for:

* Account review
* Credential reset
* Session review
* Access validation
* MFA enforcement

### Time-Based Analysis

Authentication events were reviewed chronologically.

Sharp spikes in login activity during short time windows suggested automated behavior rather than normal user activity.

### Network Analysis

Outbound network traffic was reviewed for:

* Unusual transfer volume
* Unexpected destinations
* Traffic following suspicious authentication
* Activity outside expected baselines

---

## 🚨 Key Findings

### 🔐 Credential Attack Indicators

The simulated dataset demonstrated patterns consistent with:

* Brute-force attacks
* Password spraying
* Automated login attempts
* Targeted credential attacks

### 👤 Account Risk

Several accounts experienced unusually high failed-login activity.

These accounts were prioritized for containment and credential remediation.

### ⏱️ Automation Indicators

Authentication events were clustered within short time intervals, suggesting scripted or automated activity.

### 🌐 Outbound Traffic Indicator

Increased outbound traffic was identified and investigated as a **potential indicator of unauthorized data transfer**.

The evidence did **not** establish confirmed data exfiltration, so the project treats this as an investigative indicator rather than a confirmed breach.

---

## 🚦 Incident Classification

The incident was evaluated using:

**Likelihood × Business Impact × Technical Impact**

Factors included:

* Number of accounts targeted
* Successful authentication evidence
* Privilege level of targeted accounts
* Data sensitivity
* Network activity
* Potential lateral movement
* Business disruption
* Recovery complexity

### Scenario Classification

**High-Priority Security Incident**

The event required immediate coordinated response because compromised credentials could provide legitimate access to organizational systems.

---

## 👥 Incident Response Team

| Role                                   | Responsibility                                                 |
| -------------------------------------- | -------------------------------------------------------------- |
| **Executive Sponsor**                  | Executive oversight and business decisions                     |
| **Incident Response Coordinator / PM** | Coordination, timeline, risks, communications, action tracking |
| **SOC Analyst**                        | SIEM monitoring, detection, event correlation                  |
| **Security Engineer**                  | Technical containment and security controls                    |
| **IAM Administrator**                  | Credential security, MFA, account controls                     |
| **Network Engineer**                   | Source-IP blocking and network analysis                        |
| **Systems Administrator**              | Endpoint/server review and recovery                            |
| **Legal / Compliance**                 | Regulatory and reporting assessment                            |
| **Communications Lead**                | Controlled communications                                      |
| **Business Owner**                     | Business-impact assessment                                     |
| **Executive Leadership**               | Risk decisions and closure approval                            |

---

## 📋 RACI Matrix

| Activity                | IR Coordinator | SOC | Security | IAM | Network | Executive |
| ----------------------- | -------------- | --- | -------- | --- | ------- | --------- |
| Incident Detection      | I              | R   | C        | I   | I       | I         |
| Incident Classification | A              | R   | C        | C   | C       | I         |
| Account Containment     | A              | C   | C        | R   | I       | I         |
| IP Blocking             | A              | C   | C        | I   | R       | I         |
| Credential Reset        | A              | C   | C        | R   | I       | I         |
| MFA Enforcement         | A              | C   | C        | R   | I       | I         |
| Business Impact Review  | R              | C   | C        | I   | I       | A         |
| Executive Communication | R              | I   | C        | I   | I       | A         |
| Recovery Approval       | R              | C   | C        | C   | C       | A         |
| Post-Incident Review    | R              | C   | C        | C   | C       | A         |

---

## 🛑 Phase 3 — Containment

Containment focused on stopping additional unauthorized activity and reducing exposure.

Actions included:

1. Identifying high-risk accounts
2. Locking suspected compromised accounts
3. Invalidating applicable active sessions
4. Resetting affected credentials
5. Blocking suspicious source IP addresses
6. Implementing login-attempt thresholds
7. Enforcing MFA
8. Increasing security monitoring
9. Reviewing privileged accounts
10. Restricting unnecessary access

Containment activities were prioritized according to incident severity and business risk.

---

## 🧹 Phase 4 — Eradication

After containment, the team focused on removing remaining opportunities for unauthorized access.

Activities included:

* Resetting compromised credentials
* Removing unauthorized sessions
* Reviewing suspicious account activity
* Strengthening password controls
* Validating user permissions
* Reviewing privileged access
* Blocking malicious indicators
* Reviewing system configuration
* Verifying security policies
* Confirming no unauthorized persistence remained

---

## 🔄 Phase 5 — Recovery

Recovery focused on safely returning affected accounts and systems to normal operation.

Activities included:

* Restoring legitimate user access
* Validating credential changes
* Confirming MFA enrollment
* Reviewing system integrity
* Confirming account permissions
* Monitoring authentication activity
* Monitoring outbound network activity
* Verifying SIEM visibility
* Validating alert functionality
* Obtaining business approval

Affected accounts were restored only after defined validation criteria were satisfied.

---

## 📡 SIEM Monitoring Strategy

The SIEM environment supported detection, investigation, and post-remediation monitoring.

### Authentication Events

Monitoring included:

* Failed logins
* Successful logins
* Repeated failures
* Account lockouts
* Source IP activity
* Geographic anomalies
* Unusual login times

### User Behavior

Monitoring included:

* Login frequency
* Privileged activity
* Abnormal account behavior
* Access outside expected patterns

### Network Indicators

Monitoring included:

* Outbound traffic volume
* Unexpected destinations
* Abnormal transfer patterns
* Post-authentication network activity

### Security Events

Monitoring included:

* Account changes
* Privilege changes
* Authentication-policy changes
* Security-control events

---

## 🚨 Detection & Alerting Rules

### Failed Authentication Threshold

Alert when authentication failures exceed an approved threshold during a short period.

### Multi-Account Authentication Rule

Alert when a single source attempts authentication against multiple accounts.

### Targeted Account Rule

Alert when a single account receives abnormal authentication volume.

### Successful Login After Repeated Failures

Escalate when a successful authentication occurs after repeated failures.

### Outbound Traffic Anomaly

Alert when outbound data transfer significantly exceeds established behavioral baselines.

---

## 🔐 Security Controls Implemented

Corrective controls included:

* Multi-Factor Authentication
* Stronger password controls
* Account lockout thresholds
* Credential resets
* Suspicious-IP blocking
* Improved monitoring
* SIEM correlation rules
* Least-privilege access review
* Privileged-account review
* Improved logging
* Defined escalation procedures

These controls addressed both immediate containment and long-term risk reduction.

---

## ⚠️ RAID Management

The response maintained structured tracking of:

* Risks
* Assumptions
* Issues
* Dependencies

### Example Risk Register

| Risk                            | Probability | Impact   | Response                       |
| ------------------------------- | ----------- | -------- | ------------------------------ |
| Additional compromised accounts | Medium      | Critical | Expand authentication review   |
| Unauthorized data transfer      | Medium      | Critical | Analyze outbound traffic       |
| Privileged account compromise   | Low         | Critical | Prioritize privileged accounts |
| Incomplete log visibility       | Medium      | High     | Validate required log sources  |
| Incident recurrence             | Medium      | High     | MFA and enhanced alerting      |
| Business disruption from locks  | Medium      | Medium   | Controlled account recovery    |
| Evidence loss                   | Low         | High     | Preserve required logs         |

---

## 🔁 Change & Remediation Management

Security changes were managed as controlled remediation activities.

Changes included:

* MFA enforcement
* Login-threshold changes
* Password-policy updates
* Account restrictions
* IP blocking
* SIEM-rule changes
* Alert-threshold changes
* Privileged-access changes

Each significant change documented:

* Change description
* Reason
* Owner
* Security impact
* Business impact
* Implementation status
* Validation result

---

## 📢 Incident Communication Plan

| Audience               | Communication            | Cadence                     |
| ---------------------- | ------------------------ | --------------------------- |
| Incident Response Team | Technical status         | Continuous / as needed      |
| Security Leadership    | Incident update          | Scheduled                   |
| Executive Leadership   | Business-impact briefing | Major milestones            |
| IT Operations          | Recovery coordination    | During containment/recovery |
| Business Owners        | Service impact           | As needed                   |
| Legal / Compliance     | Exposure assessment      | Based on findings           |

Executive communications focused on:

* What happened
* Current impact
* Actions completed
* Remaining risk
* Business exposure
* Decisions required
* Recovery status
* Next steps

---

## 💰 Incident Financial Management

### Scenario Budget

| Cost Category                  | Scenario Budget |
| ------------------------------ | --------------: |
| Security Investigation         |         $18,000 |
| Incident Response Labor        |         $16,000 |
| Security Engineering           |         $12,000 |
| Identity & Access Remediation  |          $8,000 |
| SIEM / Monitoring Enhancements |         $10,000 |
| Recovery & Validation          |          $7,000 |
| Documentation / Compliance     |          $4,000 |
| Contingency                    |         $10,000 |
| **Total**                      |     **$85,000** |

Financial monitoring included:

* Planned cost
* Actual cost
* Forecast at completion
* Cost variance
* Contingency usage
* Remediation cost

> Financial figures are simulated portfolio values.

---

## 📊 Incident Response KPIs

| KPI                                | Scenario Target | Scenario Result |
| ---------------------------------- | --------------: | --------------: |
| Critical Accounts Contained        |            100% |        **100%** |
| High-Risk Credentials Reset        |            100% |        **100%** |
| MFA Coverage for Affected Accounts |            100% |        **100%** |
| Critical Indicators Addressed      |            100% |        **100%** |
| Required Log Sources Validated     |            100% |        **100%** |
| Critical Open Risks Without Owner  |               0 |           **0** |
| Recovery Validation Completion     |            100% |        **100%** |
| Required Stakeholder Approvals     |            100% |        **100%** |
| Corrective Actions Assigned        |            100% |        **100%** |

Additional metrics included:

* Mean Time to Detect
* Mean Time to Acknowledge
* Mean Time to Contain
* Mean Time to Recover
* Number of affected accounts
* Number of blocked indicators
* Number of unresolved findings
* Number of corrective actions

> KPI values are scenario-based portfolio outcomes.

---

## 📈 Executive Incident Dashboard

```text
INCIDENT STATUS
High Priority → Contained → Recovery → Closed

AFFECTED ACCOUNTS REVIEWED
████████████████████ 100%

CRITICAL ACCOUNT CONTAINMENT
████████████████████ 100%

MFA REMEDIATION
████████████████████ 100%

CRITICAL INDICATORS ADDRESSED
████████████████████ 100%

RECOVERY VALIDATION
████████████████████ 100%

OPEN CRITICAL RISKS
0

CORRECTIVE ACTION OWNERSHIP
████████████████████ 100%
```

The dashboard translated technical incident-response activity into executive-level status and decision support.

---

## 🔬 Root Cause Analysis

The simulated investigation identified several control weaknesses that increased exposure to credential-based attacks.

Contributing factors included:

* Insufficient MFA coverage
* Weak failed-login alert thresholds
* Limited behavioral monitoring
* Inadequate proactive detection
* Opportunities to strengthen privileged-account monitoring
* Opportunities to improve authentication controls

The project demonstrated that security incidents often result from combinations of **technology, process, monitoring, and governance weaknesses** rather than one isolated failure.

---

## 🧠 Five Whys Analysis

### Problem

Abnormal authentication activity created a risk of unauthorized access.

### Why 1

Why could attackers repeatedly attempt authentication?

Authentication endpoints allowed repeated attempts before sufficient intervention.

### Why 2

Why were repeated attempts not immediately stopped?

Login thresholds and automated response controls required strengthening.

### Why 3

Why could compromised credentials create significant risk?

MFA coverage was incomplete.

### Why 4

Why was abnormal activity not escalated sooner?

Alert thresholds and behavioral monitoring required improvement.

### Why 5

Why were these gaps present?

Preventive controls and proactive monitoring had not been sufficiently integrated into a mature continuous-detection process.

### Root Cause Theme

**Authentication-control maturity and proactive security monitoring required improvement.**

---

## 🛠️ Corrective & Preventive Actions

### Immediate

* Lock high-risk accounts
* Reset credentials
* Block suspicious IPs
* Review active sessions
* Increase monitoring

### Short-Term

* Enforce MFA
* Improve password controls
* Strengthen failed-login thresholds
* Create SIEM correlation rules
* Review privileged access

### Long-Term

* Implement behavioral analytics
* Conduct recurring access reviews
* Improve incident-response exercises
* Establish authentication baselines
* Expand SIEM detection coverage
* Conduct recurring security-control assessments
* Maintain corrective-action tracking

---

## 🔄 Post-Incident Review

The post-incident review evaluated:

* Detection effectiveness
* Incident escalation
* Investigation quality
* Containment speed
* Stakeholder communication
* Recovery effectiveness
* Control weaknesses
* Documentation
* Business impact
* Corrective actions

The goal was not merely to close the incident, but to reduce both the probability and impact of recurrence.

---

## 🧠 Lessons Learned

### What Worked Well

* Authentication-log analysis identified attack patterns
* Time-based analysis helped identify automation
* SIEM visibility supported investigation
* Rapid account containment reduced additional exposure
* Cross-functional coordination improved response execution
* Structured governance clarified ownership
* Executive reporting translated technical findings into business risk

### Opportunities for Improvement

* Enforce MFA proactively
* Improve failed-login alerting
* Establish behavioral baselines
* Increase privileged-account monitoring
* Improve outbound-traffic anomaly detection
* Conduct regular incident-response exercises
* Automate repetitive containment activities where appropriate
* Expand centralized logging

---

## 🏁 Incident Closure Criteria

The incident could be formally closed after:

* Affected accounts were reviewed
* High-risk credentials were reset
* Suspicious indicators were addressed
* Required MFA controls were implemented
* System integrity was validated
* Authentication behavior returned to expected patterns
* Critical corrective actions were completed or assigned
* Business stakeholders accepted recovery
* Post-incident actions had owners and due dates
* Lessons learned were documented
* Executive closure was completed

---

## 📈 Scenario Project Results

The completed scenario demonstrated:

* Suspicious authentication activity identified
* High-risk accounts investigated
* Potentially compromised accounts contained
* Credentials reset
* Suspicious source activity blocked
* MFA controls strengthened
* Authentication thresholds improved
* SIEM monitoring enhanced
* Outbound-traffic anomalies investigated
* Recovery validation completed
* RAID governance maintained
* Stakeholder communications coordinated
* Root-cause analysis completed
* Corrective actions assigned
* Lessons learned documented
* Formal incident closure completed

> These are simulated portfolio outcomes and are not represented as real employer or production incident results.

---

## 📂 Repository Structure

```text
Cybersecurity_Incident_Response_Project/
│
├── README.md
├── INTERVIEW_TALK_TRACK.md
├── RESUME_BULLETS.md
├── FILE_MANIFEST.md
│
├── 01_Incident_Initiation/
│
├── 02_Detection_Analysis/
│
├── 03_Project_Management/
│
├── 04_Risk_Governance/
│
├── 05_Containment_Recovery/
│
├── 06_Security_Remediation/
│
├── 07_Financials/
│
├── 08_KPI_Reporting/
│
├── 09_Post_Incident/
│
└── 10_Evidence/
```

---

## 🛠️ Tools, Frameworks & Methods

### Cybersecurity

* SIEM Analysis
* Security Log Analysis
* Authentication Monitoring
* Threat Detection
* Incident Triage
* Identity & Access Management
* MFA
* Network Traffic Analysis
* Security Monitoring
* Root Cause Analysis

### Frameworks

* NIST-Aligned Incident Response
* Incident Response Lifecycle
* Risk-Based Classification
* Defense-in-Depth
* Least Privilege

### Project Management

* Incident Governance
* RACI
* RAID
* Risk Register
* Issue Management
* Stakeholder Management
* Communications Planning
* Action Tracking
* Budget Management
* KPI Reporting
* Executive Reporting
* Change Management
* Lessons Learned
* Project Closure

### Analysis & Reporting

* Microsoft Excel
* SIEM Dashboards
* Trend Analysis
* KPI Scorecards
* Executive Status Reports
* Data Visualization

---

## 💡 Key Lessons Learned

1. Authentication spikes can provide early warning of credential attacks.
2. MFA significantly reduces credential-compromise risk.
3. Alert thresholds should be based on expected behavior and continuously tuned.
4. Time-based clustering can reveal automated attack behavior.
5. Outbound traffic should be investigated alongside authentication activity.
6. Executive communication should translate technical findings into business impact.
7. Incident response requires clear ownership and cross-functional coordination.
8. Corrective actions should remain tracked after technical recovery.
9. Root-cause analysis should address process and governance weaknesses as well as technical controls.
10. Incident closure should require both technical and business acceptance.

---

## 🎯 Skills Demonstrated

`Cybersecurity Project Management` • `Incident Response` • `Technical Project Coordination` • `SIEM Analysis` • `Threat Detection` • `Security Operations` • `Incident Triage` • `Identity & Access Management` • `MFA` • `Risk Management` • `RACI` • `RAID` • `Stakeholder Management` • `Executive Communication` • `Root Cause Analysis` • `Security Remediation` • `Incident Recovery` • `KPI Reporting` • `Change Management` • `Cross-Functional Coordination`

---

## 🎯 Target Roles

This project demonstrates skills relevant to:

* Cybersecurity Project Coordinator
* Security Project Coordinator
* IT Project Coordinator
* Technical Project Coordinator
* Security Operations Project Coordinator
* Incident Response Coordinator
* Cybersecurity Program Coordinator
* Associate Project Manager
* PMO Analyst
* Junior Technical Project Manager

---

## 📌 Portfolio Note

This project demonstrates practical cybersecurity project-management knowledge through a realistic simulated enterprise incident-response scenario.

All incident metrics, budgets, stakeholder roles, costs, business impacts, and project outcomes are presented as scenario assumptions rather than real employer or client incident results.

Potential data-exfiltration indicators are treated as **investigative findings**, not as confirmation that a breach or data exfiltration occurred.

---

## 👤 Author

**Jamie Christian**

GitHub: [JamieChristian22](https://github.com/JamieChristian22)

Portfolio: [project-manager-portfolio](https://github.com/JamieChristian22/project-manager-portfolio)
