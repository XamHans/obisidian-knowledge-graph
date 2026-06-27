---
type: concept
title: Supervised Learning
description: Learning a function from labeled input→output pairs — the default paradigm for classification and regression in production ML.
tags: [machine-learning, supervised-learning, classification, regression]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Most production ML that "predicts a known thing" is supervised: spam vs. not-spam, price, churn, document class. The ceiling is set by **label quality and an honest train/eval split**, not by model size — a bigger model on leaky or mislabeled data just memorizes the leak faster.

## How It Works
- Given pairs `(x, y)`, fit `f(x) ≈ y` by minimizing **regularized empirical risk** — `loss + λ·complexity`, not loss alone. That regularization term is the lever that controls [[Concepts/Model_Generalization_And_Overfitting]]; dropping it is the most common way to overfit.
- The loss encodes what you want, and it is a modeling decision: **cross-entropy** for classification; for regression, **MSE** penalizes outliers quadratically (optimizes the conditional *mean*), **MAE** is robust but optimizes the *median*, and **Huber/quantile** loss are the practical compromises.

## The Surrogate–Metric Gap (a common production miss)
- You optimize a smooth **surrogate** (log loss / MSE) but are judged on non-differentiable **metrics** (F1, recall@precision, AUC). Pick the surrogate that aligns with the metric, then **tune the decision threshold on validation data** — the default 0.5 is rarely optimal under imbalance or asymmetric FP/FN cost.
- **Accuracy lies on imbalanced data:** on a 99%-negative set, "always predict negative" scores 99% and is useless. Track per-class **precision/recall** (`F1 = 2·TP / (2·TP + FP + FN)`).
- Metric folklore to avoid: "PR-AUC always beats ROC-AUC for imbalance" is not unconditional — **AUROC's random baseline is 0.5 regardless of prevalence, while PR-AUC's baseline equals the positive rate**, so PR-AUC isn't comparable across base rates. Choose by what you care about (high-score region vs. overall ranking) and by FP/FN cost.

## Calibration (scores you can trust as probabilities)
- Maximizing accuracy/AUC does **not** make scores usable as probabilities. Logistic regression is well-calibrated by default (canonical logit link); tree ensembles and SVMs are systematically miscalibrated. Fix with reliability diagrams + **Platt (sigmoid) or isotonic** calibration **fit on held-out data** (isotonic overfits below ~1000 samples).

## What Drives Performance — and What Breaks It
- **Label quality & class balance** set the achievable ceiling. Handle imbalance with class weights, resampling, threshold moving, or focal loss — but resampling distorts the base rate (re-check calibration) and must happen *inside* CV folds.
- **Data leakage** is the #1 cause of "great offline, broken in prod." The most common form is **preprocessing leakage** — fitting scalers/imputers/encoders on the full data before the split. Mechanical fix: wrap all preprocessing in a `Pipeline` so it refits inside each fold; for time series, use time-ordered splits, never random K-fold.

## Practical Defaults
- Ship a **trivial baseline** (majority class / `DummyClassifier`) *and* a strong-simple one. On **tabular data, gradient-boosted trees (XGBoost/LightGBM) often match or beat deep nets** — the "simple" model is frequently the destination, not a stepping stone.
- Review false positives and false negatives to refine data and objective; lock split discipline first — see [[Concepts/Training_Validation_Test_Splits]].

## Related
- [[Concepts/Unsupervised_Learning]], [[Concepts/Self_Supervised_Learning]], [[Concepts/Model_Generalization_And_Overfitting]]
- _Next-wave (forward refs):_ [[Concepts/Training_Validation_Test_Splits]], [[Concepts/Evaluation_Metrics_Classification_Regression]], [[Concepts/Feature_Engineering]], [[Concepts/Model_Calibration]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [CS229 Lecture Notes 1: Supervised Learning & Linear Models (Ng/Ma, Stanford)](https://cs229.stanford.edu/notes2021fall/cs229-notes1.pdf) — supervised learning as empirical risk minimization.
- [scikit-learn — Supervised learning (User Guide)](https://scikit-learn.org/stable/supervised_learning.html) — canonical catalog of model families and defaults.
- [scikit-learn — Probability calibration](https://scikit-learn.org/stable/modules/calibration.html) — reliability diagrams, Platt vs. isotonic, fitting on held-out data.
- [Google ML Crash Course — Accuracy, precision, recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) — metric definitions and the imbalance trap.
- [Kapoor & Narayanan — Leakage and the Reproducibility Crisis in ML-based Science (arXiv:2207.07048)](https://arxiv.org/abs/2207.07048) — 8-type leakage taxonomy; failures across 329 papers / 17 fields.
- [A Closer Look at AUROC and AUPRC under Class Imbalance (arXiv:2401.06091)](https://arxiv.org/abs/2401.06091) — corrects the PR-AUC-superiority folklore.

> Core Node: [[START_HERE]]
