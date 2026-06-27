---
type: concept
title: Evaluation Metrics (Classification & Regression)
description: Choosing the right metric — precision/recall/F1, ROC vs PR-AUC, micro/macro averaging, and regression errors MAE/RMSE/R².
tags: [machine-learning, evaluation, metrics, classification, regression]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- The metric *is* the objective you optimize toward — pick the wrong one and you ship the wrong model. The single most common mistake is reading **accuracy** on imbalanced data; the rest is matching the metric to the cost of being wrong.

## Classification — The Confusion Matrix and Up
- Everything derives from TP/FP/FN/TN. **Accuracy** = (TP+TN)/total is a trap: at 1% positives, "always predict negative" scores 99% and is useless.
- **Precision** = TP/(TP+FP) (cost of false alarms) vs **Recall** = TP/(TP+FN) (cost of misses); they trade off. **F1** = harmonic mean = `2·P·R/(P+R)`. The choice is cost-driven (recall-first for fraud/disease, precision-first when false positives are expensive).

## Threshold-Free: ROC-AUC vs PR-AUC
- **ROC-AUC** = P(a random positive ranks above a random negative); 0.5 = random, 1.0 = perfect; threshold-independent. But it looks **optimistic under heavy imbalance** (FPR draws on the huge negative pool).
- **PR-AUC** ignores TN and focuses on the minority class. **Prevalence caveat:** ROC's no-skill baseline is a fixed 0.5; **PR's baseline equals the positive prevalence**, so PR-AUC is only meaningful relative to the base rate. (Demo at 99:1 — ROC-AUC 0.869 looks skillful while PR-AUC 0.228 reveals the weakness.)

## Multi-Class Averaging
- **Micro** aggregates over all samples (dominated by frequent classes; equals accuracy with all labels). **Macro** is the unweighted per-class mean (gives small classes equal voice — surfaces minority failures). **Weighted** scales by support.

## Regression
- **MAE** robust and interpretable; **MSE/RMSE** penalize large errors quadratically (RMSE ≥ MAE, same units as target). **MAPE** is scale-free but breaks near zero targets and is biased toward under-forecasts. **R²** is bounded (≤1), reads as variance explained — Chicco et al. argue it's the most informative single number.

## Related
- [[Concepts/Supervised_Learning]], [[Concepts/Model_Calibration]], [[Concepts/Training_Validation_Test_Splits]], [[Concepts/LLM_As_Judge_Evaluation]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [scikit-learn — Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html) — precision/recall/F-beta, averaging, ROC vs average_precision, log_loss, regression metrics.
- [Google ML Crash Course — Accuracy, precision, recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) — confusion matrix and the imbalance trap.
- [Google ML Crash Course — ROC and AUC](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc) — ROC/AUC ranking interpretation and balance guidance.
- [ROC and Precision-Recall Curves for Imbalanced Classification (ML Mastery)](https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-imbalanced-classification/) — ROC optimism under imbalance; no-skill baselines.
- [R² is more informative than SMAPE/MAE/MAPE/MSE/RMSE (Chicco et al., PeerJ CS 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8279135/) — the case for bounded R² over unbounded error metrics.

> Core Node: [[START_HERE]]
