---
type: concept
title: Bias–Variance Tradeoff
description: The decomposition of error into bias, variance, and irreducible noise — the classic U-curve and the modern double-descent caveat.
tags: [machine-learning, generalization, bias-variance, double-descent]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- This is the theory that explains *why* models under- or over-fit, and what knob to turn. It is the conceptual backbone of regularization, early stopping, model selection, and ensembling — and the lens for reading a train/validation gap (see [[Concepts/Model_Generalization_And_Overfitting]]).

## The Decomposition
- For squared-error loss the expected test error splits **exactly** into three parts:
  `Err(x₀) = σ²_irreducible + Bias²[f̂(x₀)] + Var[f̂(x₀)]`.
- **Irreducible error** (`σ²`) is noise no model can remove — it sets the error floor. (For 0–1 classification loss the split is not additive; the intuition carries, the algebra doesn't.)

## Bias vs Variance
- **High bias = underfitting:** the model is too rigid, wrong on train *and* test.
- **High variance = overfitting:** the model fits noise, nails train, fails to generalize.
- Concrete forms (ESL): k-NN variance `= σ²/k` (grows as k shrinks → more complex), linear-model variance `≈ (p/N)·σ²` (scales with parameters p over samples N).

## The Classical U-Curve
- As complexity rises, bias² falls and variance rises; total test error is minimized at an intermediate sweet spot. This motivates validation-based model selection and regularization strength λ.

## The Double-Descent Correction (modern caveat)
- The U-curve holds in the *under-parameterized* regime only. Past the **interpolation threshold** (capacity just enough to fit the training set, train error ≈ 0), test error can **descend again** — overturning "more complex = worse" for heavily overparameterized models.
- In deep nets this appears model-wise, epoch-wise, *and* sample-wise; the peak sits near the interpolation threshold and is amplified by label noise — in a narrow regime even *more data can hurt*. Practical takeaway: large modern models often live to the right of the peak. See [[Concepts/Model_Generalization_And_Overfitting]].

## Related
- [[Concepts/Model_Generalization_And_Overfitting]], [[Concepts/Supervised_Learning]], [[Concepts/Hyperparameter_Optimization]], [[Concepts/Training_Validation_Test_Splits]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [The Elements of Statistical Learning — §7.3 Bias–Variance Decomposition (Hastie, Tibshirani, Friedman)](https://hastie.su.domains/ElemStatLearn/) — the exact decomposition and k-NN / linear closed forms.
- [Reconciling modern ML and the bias–variance trade-off (Belkin et al., PNAS 2019; arXiv:1812.11118)](https://arxiv.org/abs/1812.11118) — the double-descent result and interpolation threshold.
- [Deep Double Descent (Nakkiran et al., ICLR 2020; arXiv:1912.02292)](https://arxiv.org/abs/1912.02292) — model-/epoch-/sample-wise double descent in real nets.
- [Understanding the Bias-Variance Tradeoff (Fortmann-Roe, 2012)](https://scott.fortmann-roe.com/docs/BiasVariance.html) — clean graphical + mathematical treatment.
- [Google ML Crash Course — Overfitting](https://developers.google.com/machine-learning/crash-course/overfitting/overfitting) — practitioner framing and generalization preconditions.

> Core Node: [[START_HERE]]
