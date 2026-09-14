# Project Controls Data Dictionary

## Cost controls
- **Original Budget**: approved baseline allocation by cost code.
- **Approved Changes**: net approved budget adjustment/transfers applied to that cost code.
- **Revised Budget**: `Original Budget + Approved Changes`.
- **Committed**: executed subcontract/purchase-order value.
- **Actual Cost to Date**: recognized/project cost incurred to the status date.
- **ETC**: estimate to complete from status date through final completion.
- **FAC**: `Actual Cost to Date + ETC`.
- **Variance to Budget**: `Revised Budget - FAC`; positive is favorable.
- **% Committed**: `Committed / Revised Budget`.
- **% Spent**: `Actual Cost to Date / Revised Budget`.

## Schedule controls
- **Planned %**: baseline completion expected by the status date.
- **Actual %**: verified physical progress.
- **Variance (pp)**: `Actual % - Planned %`.
- **Critical?**: activity flagged as directly/near-directly affecting contractual finish or key milestones.

## RFI / submittal controls
- **Ball in Court**: party currently responsible for response.
- **Due Date / Review Due**: required date to protect the work plan.
- **Schedule Impact**: days of known or forecast impact if the issue affects sequence.
- **Related CO**: approved or potential cost/change record linked to the technical issue.

## Risk controls
- **Score**: `Probability x Impact`, each rated 1-5.
- **Low**: score <6. **Medium**: 6-11. **High**: 12-19. **Critical**: 20-25.
- **Trigger**: observable condition that causes the response plan to activate.
- **Residual Score**: expected risk after mitigation.

## Closeout controls
- **Retention Link**: payment leverage tied to completion of trade obligations.
- **Forecast**: current expected date when different from the baseline due date.
- **% Complete**: verified completeness of the closeout item, not merely “submitted.”
