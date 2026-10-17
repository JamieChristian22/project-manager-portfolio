# Migration Runbook
## T-7 Days
Freeze scope; confirm maintenance window; verify owners; complete backup/restore rehearsal; issue user communication.
## T-24 Hours
Confirm latest backup; validate target health; export configuration; pre-stage data; review RAID; conduct go/no-go precheck.
## Cutover
1. Open bridge and attendance check. 2. Announce change start. 3. Place source in maintenance/read-only mode. 4. Run final database delta sync. 5. Validate row counts/checksums. 6. Start/validate target application. 7. Verify ALB health. 8. Execute smoke tests. 9. Change DNS/traffic routing. 10. Monitor errors, latency, CPU, DB connections. 11. Business owner executes critical-path validation. 12. PM records go-live decision and timestamp.
## Exit
No Sev-1/2 defect; critical transactions pass; monitoring green for 60 minutes; sponsor/app owner informed; rollback point retained for 24 hours.
