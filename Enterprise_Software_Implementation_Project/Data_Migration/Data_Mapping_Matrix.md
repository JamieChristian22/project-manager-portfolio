# Data Mapping Matrix

| Source Field | Salesforce Target | Rule |
|---|---|---|
| Company Name | Account.Name | Trim whitespace |
| Contact Email | Contact.Email | Validate format |
| Lead Source | Lead.LeadSource | Standardize values |
| Deal Value | Opportunity.Amount | Numeric conversion |
| Sales Stage | Opportunity.StageName | Map legacy stage |
| Expected Close | Opportunity.CloseDate | ISO date conversion |
| Owner Email | OwnerId | Lookup by approved user |
| Legacy ID | External_ID__c | Preserve for reconciliation |
