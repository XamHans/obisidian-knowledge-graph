---
type: concept
status: active
hub: Machine_Learning
persona: Professional Seeking AI Mastery
evidence_status: needs_receipts
evidence_backlog:
  - Add transcript with concrete split strategy and leakage prevention example.
---

## Why It Matters
- Reliable model evaluation depends on strict separation between training, validation, and test data to prevent leakage and over-optimistic results.

## Sub-Concept Map
- Training set drives parameter updates.
- Validation set drives hyperparameter/model selection.
- Test set estimates final out-of-sample performance.
- Data leakage silently inflates apparent quality.
- Temporal/domain shifts require split strategy adaptation.

## Playbook Moves
- Freeze test set access until final model selection stage.
- Build leakage checks into preprocessing pipelines.
- Recalculate metrics by segment to expose brittle performance.

## Source Transcripts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[Projects/AI_Native_Engineer]]

## Linked Technologies
- [[Resources/Software/Phoenix]]
- [[Technologies/Neon_Postgres]]

## Related Concepts
- [[Resources/Concepts/Model_Generalization_And_Overfitting]]
- [[Resources/Concepts/Evaluation_Metrics_Classification_Regression]]
- [[Resources/Concepts/Supervised_Learning]]

> Related Hub: [[Hubs/Machine_Learning]]
> Core Node: [[Projects/AI_Native_Engineer]]
