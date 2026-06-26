---
type: concept
stability: stable
reviewed: 2026-06
hub: Machine_Learning
evidence_status: needs_receipts
evidence_backlog:
  - Add transcript receipts for metric selection tied to business risk.
---

## Why It Matters
- Metric choice defines what success means; the wrong metric can optimize the wrong behavior and hide critical failures.

## Sub-Concept Map
- Classification metrics: precision, recall, F1, ROC-AUC.
- Regression metrics: MAE, MSE/RMSE, R2.
- Threshold tuning changes operating behavior.
- Calibration quality matters for decision systems.
- Segment-level metrics reveal uneven model quality.

## Playbook Moves
- Tie each metric to a concrete business failure cost.
- Track both aggregate and slice-level metrics in dashboards.
- Revisit thresholds after every major data or model change.

## Source Transcripts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/Phoenix]]
- [[Tools/Neon_Postgres]]

## Related Concepts
- [[Concepts/Training_Validation_Test_Splits]]
- [[Concepts/Model_Generalization_And_Overfitting]]
- [[Concepts/Agent_Observability_And_Evaluation]]

> Related Hub: [[Hubs/Machine_Learning]]
> Core Node: [[START_HERE]]
