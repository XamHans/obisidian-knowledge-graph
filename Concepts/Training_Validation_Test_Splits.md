---
type: concept
title: Training, Validation and Test Splits
description: How data is partitioned so tuning and final evaluation stay honest — three-way splits, cross-validation, and leakage-safe splitting.
tags: [machine-learning, evaluation, cross-validation, data-leakage]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Every reported number is only as honest as the split behind it. The split is what separates *fitting* the model from *estimating* how it will behave on data it has never seen — get it wrong and you ship a model that looked great offline and fails in production. It is the operational defense against [[Concepts/Model_Generalization_And_Overfitting]].

## Three Sets, Three Jobs
- **Train** fits the parameters. **Validation** selects models/hyperparameters. **Test** gives one final, unbiased generalization estimate. As ESL puts it: use train + validation to *choose* the model, test to *assess* the chosen one.
- Training error always *underestimates* test error and keeps falling with complexity — which is exactly why a held-out estimate is non-negotiable.

## Test-Set Hygiene
- The moment you tune against a set, information leaks in and its estimate turns optimistic ("teaching to the test"). The test set is touched **once**, after the model is frozen.
- Validation error is itself optimistically biased after selection (you picked the best of many), so the independent test set is what you actually trust.
- Sets **wear out** with repeated use — deduplicate test/val against train, and don't let a fixed test set silently drive months of decisions.

## Cross-Validation
- When data is limited, **k-fold CV** replaces a fragile single split: each fold is held out once while the other k−1 train; average the scores for a lower-variance estimate.
- **StratifiedKFold** preserves per-class proportions in every fold — essential for imbalanced classification. If CV is used to *select* a model, you still need an outer test set or **nested CV**.

## Leakage-Aware Splitting
- **Grouped** (`GroupKFold`): the same entity (patient, user, document) must never appear in both train and validation.
- **Temporal** (`TimeSeriesSplit`, forward-chaining): train always precedes test — never train on the future to predict the past. Plain shuffled k-fold on time series creates spurious correlation.
- **Preprocessing belongs inside the fold:** fit scalers/imputers/encoders on train only (wrap in a `Pipeline`), or you leak test statistics — see [[Concepts/Feature_Engineering]].

## Practical Defaults
- Common proportions: 50/25/25 (ESL) or ~70/15/15 (Google) — there is no canonical ratio; it depends on dataset size and signal-to-noise. Make every split **representative of the serving distribution**.

## Related
- [[Concepts/Model_Generalization_And_Overfitting]], [[Concepts/Hyperparameter_Optimization]], [[Concepts/Supervised_Learning]], [[Concepts/Bias_Variance_Tradeoff]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [scikit-learn — Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html) — train/test rationale, k-fold, group & time-series splits, leakage.
- [Google ML Crash Course — Dividing the original dataset](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets) — three-way split roles and set "wear-out."
- [scikit-learn — StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html) — folds preserve per-class proportions.
- [scikit-learn — TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) — forward-chaining temporal splits.
- [Model Assessment and Selection — ESL Ch. 7 (course notes, PDF)](http://rafalab.dfci.harvard.edu/pages/649/section-07.pdf) — model selection vs. assessment; why training error underestimates test error.

> Core Node: [[START_HERE]]
