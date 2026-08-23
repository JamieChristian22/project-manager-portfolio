# Data Mapping Matrix

| Source | Target | Rule |
|---|---|---|
| Legacy_ID | External_ID | Preserve |
| Customer_Name | Customer.Name | Trim |
| Status_Code | Status | Controlled map |
| Created_Date | CreatedDate | Date conversion |
| Owner_Login | OwnerId | Directory lookup |
| Amount_Text | Amount | Numeric conversion |
