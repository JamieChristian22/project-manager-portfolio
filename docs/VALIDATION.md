# Validation scope

The validator reads CSVs, Markdown links, and XLSX XML using only the Python standard library. It calculates supplemental exercise schedules, budgets, test coverage, and readiness. It verifies record identifiers, cross-file references, ownership, dates represented as exercise days, and evidence requirements. It checks local Markdown destinations outside the retained historical overview.

Workbook inspection inventories sheets and formula cells, detects stored error values and explicit broken-reference formulas, and reports missing formula caches. It does **not** execute Excel formulas, validate macros, test native filters, or certify charts. Original workbooks are retained without binary edits. A clean structural scan is not a claim that native workbook recalculation has passed.

Coordinator source queries are executed in SQLite against the supplied CSV data. Reports distinguish source-data arithmetic from the separate tabletop exercises. No real system deployment, stakeholder approval, clinical validation, or Salesforce/AWS execution is implied.

Run `python scripts/validate_portfolio.py` to regenerate reports. Run `python -m unittest discover -s tests -v` for negative cases covering cycles, orphan references, missing evidence, resource ownership, cost gates, and incomplete approvals. Reports should be regenerated whenever inputs change.

Run `python scripts/source_metrics.py` for the independent original-source reconciliation. Known historical discrepancies are documented as findings, not hidden behind a passing structural scan.
