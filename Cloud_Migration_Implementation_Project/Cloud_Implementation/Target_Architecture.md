# Target Architecture Design
Users reach the application through HTTPS and an Application Load Balancer. The ALB distributes requests to EC2 instances managed by an Auto Scaling Group across two availability zones. Application data resides in Amazon RDS; static assets and backup exports use S3. IAM roles provide workload permissions. CloudWatch captures operational metrics and alarms. Backups protect the database and critical data.
## Design Principles
High availability; least privilege; managed services where practical; automated scaling; observable operations; recoverability; cost tagging; repeatable configuration.
