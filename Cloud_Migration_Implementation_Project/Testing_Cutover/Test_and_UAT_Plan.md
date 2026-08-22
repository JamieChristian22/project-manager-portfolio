# Test & UAT Plan
| Test | Expected result | Owner | Result |
|---|---|---|---|
|Network connectivity|Approved paths succeed; blocked paths fail|Cloud Eng|Pass|
|ALB health|All target instances healthy|Cloud Eng|Pass|
|Login|Authorized user can authenticate|App Owner|Pass after remediation|
|Core transaction|Create/read/update workflow completes|App Owner|Pass|
|Static assets|Assets load from target storage|App Owner|Pass|
|DB validation|Counts/checksums within expected tolerance|Migration Lead|Pass|
|Scale test|Additional instance launches under load|Cloud Eng|Pass|
|CPU alarm|Alarm enters expected state and routes alert|Ops|Pass|
|Backup restore|Recovery point restores and app connects|Ops|Pass|
|Rollback rehearsal|Traffic can return to source within objective|Migration Lead|Pass|
Acceptance requires all critical tests pass and no open Sev-1 defects.
