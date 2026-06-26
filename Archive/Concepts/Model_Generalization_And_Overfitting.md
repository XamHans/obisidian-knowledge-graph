---
type: concept
stability: stable
reviewed: 2026-06
hub: Machine_Learning
evidence_status: needs_receipts
evidence_backlog:
  - Add transcript receipts on regularization and generalization diagnostics.
---

## Why It Matters
- Generalization determines whether models stay useful outside the training set; overfitting makes performance collapse in real usage.

## Sub-Concept Map
- Overfitting memorizes training artifacts.
- Underfitting fails to capture useful signal.
- Regularization controls model complexity.
- Data augmentation improves robustness.
- Distribution shift testing reveals fragility.

## Playbook Moves
- Compare training vs validation curves every run.
- Add regularization and simplify architecture before adding data size.
- Maintain holdout slices for hard edge-case evaluation.

## Source Transcripts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/Phoenix]]
- [[Tools/Docker]]

## Related Concepts
- [[Concepts/Training_Validation_Test_Splits]]
- [[Concepts/Evaluation_Metrics_Classification_Regression]]
- [[Concepts/Inference_Optimization_Latency_Cost]]

> Related Hub: [[Hubs/Machine_Learning]]
> Core Node: [[START_HERE]]
