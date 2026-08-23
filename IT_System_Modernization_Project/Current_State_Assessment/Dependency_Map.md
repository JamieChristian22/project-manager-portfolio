# Dependency Map

Core Application → SQL Database → File Share → Reporting Extract → Finance Export.

Core Application → Identity Sync.  
Core Application → Notification Service.  
Nightly Scheduler → Database + Vendor Import + Reporting Extract.

Critical cutover dependencies: identity, database, finance export, and reporting.
