# 🔍 Incident Analysis  
## SIEM Investigation, Threat Detection & Attack Pattern Identification

---

## 📌 Overview
This section focuses on the detailed investigation and analysis of the cybersecurity incident using SIEM-based techniques. It demonstrates how log data, authentication events, and system activity were analyzed to detect threats, identify attack patterns, and assess potential security risks.

SIEM systems collect and analyze logs from multiple sources to detect anomalies, correlate events, and identify potential security threats.  

---

## 🎯 Objective
- Analyze security logs and authentication activity  
- Detect abnormal patterns and potential threats  
- Identify indicators of compromise (IOCs)  
- Understand attacker behavior and attack patterns  
- Support incident response and mitigation  

---

## 🛠️ Investigation Approach (SIEM-Based)

The analysis followed a structured SIEM investigation process:

### 1. Data Collection
- Aggregated logs from authentication systems and network activity  
- Centralized data for analysis and correlation  

SIEM systems collect and consolidate logs from servers, applications, and network devices to provide a unified view of security events. :contentReference[oaicite:0]{index=0}  

---

### 2. Threat Detection (Initial Alert)
- Identified abnormal login activity  
- Detected high volume of failed authentication attempts  
- Triggered alerts based on suspicious patterns  

SIEM tools continuously monitor systems and generate alerts when anomalies or suspicious behavior are detected. :contentReference[oaicite:1]{index=1}  

---

### 3. Event Analysis & Investigation
- Analyzed login attempts by:
  - Username  
  - Time  
  - Frequency  
- Identified unusual spikes and repeated failures  

SIEM enables deep analysis of logs to determine what happened, when it occurred, and how the incident developed. :contentReference[oaicite:2]{index=2}  

---

### 4. Data Correlation & Pattern Identification
- Correlated multiple events across users and timeframes  
- Connected failed logins, repeated attempts, and patterns  
- Identified coordinated attack behavior  

SIEM systems correlate events across multiple data sources to reveal hidden attack patterns and coordinated threats. :contentReference[oaicite:3]{index=3}  

---

## 📊 Key Analysis Areas

### 1. Failed Login Analysis
- High volume of failed login attempts detected  
- Indicates possible brute-force or credential stuffing attack  

---

### 2. User-Based Analysis
- Certain users targeted more frequently  
- Suggests attacker focus on specific accounts  

---

### 3. Time-Based Analysis
- Login attempts clustered within short time windows  
- Indicates automated attack scripts  

---

### 4. Network / Activity Analysis
- Monitored outbound traffic behavior  
- Investigated potential data exfiltration indicators  

---

## 📈 Visual Evidence

### SIEM Dashboard Analysis
![SIEM Analysis](2_Incident_Analysis/Failed_Logins_SIEM_Analysis.png)

### Supporting Analysis Visuals
- Failed Logins by Username  
- Failed Logins Over Time  
- Count of Failed Logins by IP  
- Brute Force Detection Checks  

---

## 🚨 Key Findings

- Evidence of brute-force / credential-based attack  
- Abnormal authentication patterns across multiple accounts  
- Repeated login attempts indicating automation  
- Potential indicators of unauthorized access attempts  

---

## ⚠️ Threat Assessment

- **Attack Type:** Brute-force / credential attack  
- **Severity Level:** Medium to High  
- **Risk Factors:**
  - Unauthorized access  
  - Account compromise  
  - Potential lateral movement  

---

## 🧠 Insights & Analysis

- Failed login spikes are strong indicators of attack attempts  
- Repeated patterns suggest automated attack tools  
- Correlating multiple data points reveals full attack behavior  
- SIEM analysis enables faster and more accurate threat detection  

---

## 📊 Role in Incident Response

Incident analysis is a critical phase of cybersecurity response because it:

- Identifies the root cause of the incident  
- Determines scope and impact  
- Guides containment and mitigation strategies  

SIEM plays a central role by providing real-time visibility and enabling faster detection and response to threats. :contentReference[oaicite:4]{index=4}  

---

## 📁 Files Included

- SIEM Analysis Dashboard (main investigation view)  
- Failed login analysis visuals  
- Brute force detection artifacts  
- Supporting investigation data  

---

## 🚀 Skills Demonstrated

- SIEM Investigation & Log Analysis  
- Threat Detection & Pattern Recognition  
- Incident Analysis & Root Cause Identification  
- Data Correlation & Event Analysis  
- Cybersecurity Risk Assessment  

---

## 🔁 Best Practices Applied

- Analyzed multiple data points (user, time, activity)  
- Correlated events across systems  
- Focused on high-risk indicators (failed logins, anomalies)  
- Used data-driven investigation approach  
- Identified attack patterns before escalation  

---

## 📌 Conclusion
This section demonstrates the ability to perform structured cybersecurity incident analysis using SIEM tools. By analyzing logs, identifying patterns, and correlating events, the project effectively detects threats and provides actionable insights for incident response and risk mitigation.
