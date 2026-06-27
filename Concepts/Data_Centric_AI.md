---
type: concept
title: Data-Centric AI
description: Improving the data, not the model, as the highest-ROI lever — label consistency, error-finding, and systematic dataset iteration.
tags: [machine-learning, data-centric-ai, data-quality, labeling]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- For many applications the architecture is "basically a solved problem" (Ng) — so data quality, not model tweaking, is the bottleneck and the highest-ROI lever. Data-centric AI is the discipline of **systematically improving the dataset with the model held fixed**, the counterpart to [[Concepts/Feature_Engineering]] at the dataset level.

## Data-Centric vs Model-Centric
- Model-centric iterates on architecture/loss with data fixed; data-centric **holds the model fixed and improves the data** — relabeling, augmenting, curating, and removing bad examples. The leverage is largest where the model is already good and the data is noisy.

## Label Consistency
- A primary failure mode is **annotator disagreement**: humans label the same example differently. The fix is tooling that surfaces inconsistent labels for targeted relabeling and consensus aggregation — not collecting more noisy data. Inter-annotator agreement is the practical ceiling on achievable accuracy.

## Finding Label Errors at Scale
- **Confident learning** estimates the joint distribution of noisy vs. true labels to algorithmically flag likely mislabeled examples (the cleanlab lineage); flagged candidates are then human-validated. This turns "clean the data" into a measurable, repeatable step.

## Label Errors Corrupt Benchmarks
- Noisy **test** sets destabilize model selection: on corrected labels, a smaller model can outrank a larger one — so "bigger is better" can be an artifact of mislabeled test data. Evaluate on corrected test sets.

## The Workflow
- Train → **error analysis** to find weak slices → improve the *data* (not the code) → retrain → iterate; supported by data documentation, slice-based evaluation, outlier/drift detection (see [[Concepts/Concept_Drift_And_Data_Drift]]), augmentation, and active learning.

## Related
- [[Concepts/Feature_Engineering]], [[Concepts/Supervised_Learning]], [[Concepts/Concept_Drift_And_Data_Drift]], [[Concepts/Training_Validation_Test_Splits]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [Andrew Ng: Unbiggen AI (IEEE Spectrum)](https://spectrum.ieee.org/andrew-ng-data-centric-ai) — the data-centric framing; "good data over big data," small-data leverage.
- [Introduction to Data-Centric AI — MIT (dcai.csail.mit.edu)](https://dcai.csail.mit.edu/) — the first university DCAI course (label quality, curation, evaluation).
- [Data-Centric vs. Model-Centric AI — MIT DCAI lecture](https://dcai.csail.mit.edu/2023/data-centric-model-centric/) — definitions and the technique catalog.
- [Pervasive Label Errors in Test Sets Destabilize ML Benchmarks (Northcutt et al., arXiv:2103.14749)](https://arxiv.org/abs/2103.14749) — ≥3.3% avg label errors across 10 benchmarks; ImageNet ≥6%.

> Core Node: [[START_HERE]]
