# Security Event Analysis

## Scenario Dataset Summary
A 60-minute review window contained 2,460 failed authentications across 31 accounts from 14 source addresses. Five accounts exceeded 150 failures. One account showed a successful authentication 90 seconds after a concentrated failure burst and was treated as high priority. A separate outbound-transfer signal exceeded the established hourly baseline by 2.8x and required correlation.

## Analysis
The distribution across many accounts from overlapping sources is consistent with password spraying, while rapid repeated attempts against selected identities also resemble brute-force behavior. Time clustering increases confidence that automation was involved. The outbound anomaly alone does not prove exfiltration; correlation with identity, endpoint, destination, and data-access telemetry is required.

## Decision
Declare SEV-2, contain high-risk identities, block confirmed suspicious sources, preserve logs, and perform targeted correlation before any breach conclusion.
