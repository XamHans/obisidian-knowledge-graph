---
type: concept
title: Hyperparameter Optimization
description: Searching hyperparameters efficiently — random over grid, Bayesian optimization, successive halving, and the nested-validation discipline.
tags: [machine-learning, hyperparameter-optimization, automl, model-selection]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Hyperparameters (learning rate, depth, regularization λ, k) sit directly on the [[Concepts/Bias_Variance_Tradeoff]] curve, so tuning them is how you actually reach a model's potential. The catch: tune sloppily and you optimize against the test set, inflating every number you report.

## Grid vs Random — and why random wins
- Grid search scales **exponentially** with dimensions and re-tests redundant values on axes that don't matter. **Random search** covers each individual axis with far more distinct values for the same budget.
- The deeper reason is **low effective dimensionality**: on most datasets only a few hyperparameters drive performance, and *which* ones differ per dataset — so a grid wastes most trials. Random search of **60 trials** lands in the top-5% region with ~95% probability (`1 − 0.95⁶⁰ ≈ 0.954`), independent of budget.

## Smarter Search
- **Bayesian optimization** (TPE in Optuna; GP-based) builds a surrogate of the objective and an acquisition function to pick the next config — sample-efficient sequentially, harder to parallelize, often overkill for cheap-to-train models.
- **Successive halving / Hyperband / ASHA** attack the *budget* axis: train many configs cheaply (few epochs), keep the top `1/factor` (default 3), give survivors more resource, repeat. **ASHA** makes promotion asynchronous and scales linearly to hundreds of workers.

## The Disciplines That Make It Honest
- **Search-space design** matters as much as the algorithm: sample learning rate / weight decay / λ on a **log scale**, use categorical for discrete choices, bound ranges sensibly.
- **Validation protocol:** tune on a held-out validation set or **nested CV** (inner loop selects hyperparameters, outer loop gives the unbiased estimate); touch the test set only once — see [[Concepts/Training_Validation_Test_Splits]].

## Related
- [[Concepts/Training_Validation_Test_Splits]], [[Concepts/Model_Generalization_And_Overfitting]], [[Concepts/Bias_Variance_Tradeoff]], [[Concepts/ML_Experiment_Tracking]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [Random Search for Hyper-Parameter Optimization (Bergstra & Bengio, JMLR 2012)](https://jmlr.org/papers/v13/bergstra12a.html) — why random beats grid; low effective dimensionality.
- [Hyperband (Li et al., arXiv:1603.06560)](https://arxiv.org/abs/1603.06560) — bandit-based early-stopping; >10× speedup over Bayesian methods.
- [ASHA — Massively Parallel Hyperparameter Tuning (Li et al., arXiv:1810.05934)](https://arxiv.org/abs/1810.05934) — asynchronous successive halving, scales to 500 workers.
- [Optuna (Akiba et al., KDD 2019; arXiv:1907.10902)](https://arxiv.org/abs/1907.10902) — define-by-run API, TPE sampler, pruning.
- [scikit-learn — HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html) — production successive halving (`factor`, `resource`).

> Core Node: [[START_HERE]]
