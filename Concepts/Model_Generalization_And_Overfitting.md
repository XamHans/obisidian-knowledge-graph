---
type: concept
title: Model Generalization and Overfitting
description: Whether a model performs on unseen data — bias–variance, regularization, the double-descent nuance, and distribution shift.
tags: [machine-learning, generalization, overfitting, regularization]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Training accuracy is vanity; **generalization is the only thing that ships**. Overfitting — fitting training noise instead of signal — makes a model that looks excellent offline collapse on real traffic. This is the central failure mode behind every [[Concepts/Supervised_Learning]] system.

## The Bias–Variance Decomposition
- For squared error, expected test error decomposes exactly: `Err = σ²_irreducible + Bias²[f̂] + Var[f̂]`.
- **Underfitting (high bias)** — too simple; train *and* validation error both high. **Overfitting (high variance)** — fits noise; train error low, validation high. Regularization trades a little bias for a large drop in variance.

## The U-Curve — and the Double-Descent Correction
- The classical story: test error is **U-shaped** in complexity, so aim for the bottom of the U. This holds **only in the under-parameterized regime**.
- For modern overparameterized nets it is incomplete: error rises to a peak at the **interpolation threshold** (capacity just enough to fit the training set, ≈ #params ≈ #samples), then **descends again** — often *below* the classical minimum. So "go bigger past interpolation" usually generalizes *better*, not worse.
- Corollary: **interpolation ≠ overfitting.** Nets can fit random labels yet still generalize, so zero train error is not itself a red flag — the **train–val gap** and val/test error are the real signals.

## Diagnosis
- Compare **training vs. validation curves every run**: low-train/high-val → variance (overfit); both-high-and-close → bias (underfit); both-low-and-close → healthy.
- **Learning curves vs. dataset size:** val error plateaus well above train → more data won't help (add capacity/features); curves still converging → more data will help.

## Remedies (cheap → expensive)
- **More / cleaner data** and **augmentation** (raises effective sample size) — usually highest leverage.
- **Regularization, mechanistically:** L2/weight decay shrinks weights toward (never exactly) 0; **L1/Lasso** drives weights to *exactly* 0 (sparsity); **dropout** randomly zeroes units (≈ ensemble over thinned subnets, typical p=0.5); **early stopping** ≈ implicit L2.
- **Cross-validation** (k=5/10) for honest estimates on small data; use grouped/temporal CV to avoid leakage, and ESL's **one-standard-error rule** (simplest model within 1 SE of the best) for principled selection — see [[Concepts/Training_Validation_Test_Splits]].
- *Caveat near the interpolation peak:* double descent is also **epoch-wise** and **sample-wise**, so "train longer" and "more data" can transiently *hurt* — most pronounced under label noise.

## Generalization ≠ Robustness
- Low validation error bounds only **in-distribution** (IID) performance. Real deployments face **distribution shift**; optimizing IID loss can even trade off against OOD robustness, so hold out hard edge-case slices and monitor drift — see _next-wave_ `Concept_Drift_And_Data_Drift`.

## Related
- [[Concepts/Supervised_Learning]], [[Concepts/Self_Supervised_Learning]]
- _Next-wave (forward refs):_ [[Concepts/Training_Validation_Test_Splits]], [[Concepts/Bias_Variance_Tradeoff]], [[Concepts/Model_Calibration]], [[Concepts/Concept_Drift_And_Data_Drift]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [Reconciling modern ML and the bias–variance trade-off (Belkin et al., PNAS 2019; arXiv:1812.11118)](https://arxiv.org/abs/1812.11118) — the canonical double-descent result.
- [Deep Double Descent: Where Bigger Models and More Data Hurt (Nakkiran et al., ICLR 2020; arXiv:1912.02292)](https://arxiv.org/abs/1912.02292) — model-/epoch-/sample-wise double descent in real nets.
- [Dropout: A Simple Way to Prevent Overfitting (Srivastava et al., JMLR 2014)](https://www.jmlr.org/papers/v15/srivastava14a.html) — dropout as implicit ensembling.
- [The Elements of Statistical Learning (Hastie, Tibshirani, Friedman)](https://hastie.su.domains/ElemStatLearn/download.html) — bias–variance decomposition (§7.3), model assessment & CV.
- [Google ML Crash Course — Overfitting & Regularization](https://developers.google.com/machine-learning/crash-course/overfitting/overfitting) — `minimize(loss + λ·complexity)`, train/val curve diagnosis.

> Core Node: [[START_HERE]]
