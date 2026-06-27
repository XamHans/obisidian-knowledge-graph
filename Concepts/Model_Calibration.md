---
type: concept
title: Model Calibration
description: Making predicted probabilities match real frequencies — reliability diagrams, ECE, temperature scaling, and why modern nets are overconfident.
tags: [machine-learning, calibration, probability, uncertainty]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- A model can rank perfectly yet output probabilities you can't trust. Whenever the *probability itself* drives a decision — a threshold, a cost-sensitive choice, abstention/human routing, or a downstream system — calibration matters as much as accuracy, and the two are **orthogonal**.

## What Calibration Is
- A classifier is calibrated when predicted probability matches empirical frequency: among samples scored ~0.8, about 80% should be positive. This is independent of accuracy/AUC (a model can be accurate but badly calibrated, and vice versa).

## Measuring It
- **Reliability diagram:** bin predictions by confidence, plot mean predicted probability (x) vs. observed fraction-positive (y); perfect calibration is the y=x diagonal — below = overconfident, above = underconfident.
- **Expected Calibration Error (ECE):** `ECE = Σ_m (|B_m|/n)·|acc(B_m) − conf(B_m)|` — the sample-weighted average bin gap. Caveat: sensitive to bin count/scheme and only scores the top class.

## Fixing It (post-hoc, on held-out data)
- **Platt / sigmoid scaling** — parametric, low-variance; good for small data and the sigmoid-shaped distortion of max-margin methods (SVMs, boosted trees).
- **Isotonic regression** — non-parametric, more flexible, but **overfits below ~1000 samples**.
- **Temperature scaling** — a single scalar `T` on the logits (`softmax(z/T)`); accuracy-preserving (monotonic) and the multiclass go-to.
- Always fit the calibrator and measure ECE on **held-out/CV** data, never on training data — see [[Concepts/Training_Validation_Test_Splits]].

## Modern Nets Are Overconfident
- Guo et al. (2017): modern deep nets are systematically overconfident, and **depth, width, reduced weight decay, and BatchNorm** all worsen it — yet single-parameter temperature scaling fixes it "surprisingly" well. (Classic NNs and bagged trees were natively well-calibrated; the regression came with scale.)

## Related
- [[Concepts/Supervised_Learning]], [[Concepts/Evaluation_Metrics_Classification_Regression]], [[Concepts/Model_Generalization_And_Overfitting]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [On Calibration of Modern Neural Networks (Guo et al., ICML 2017; arXiv:1706.04599)](https://arxiv.org/abs/1706.04599) — modern-net overconfidence; temperature scaling.
- [scikit-learn — Probability calibration](https://scikit-learn.org/stable/modules/calibration.html) — sigmoid vs isotonic, CalibratedClassifierCV, the <1000-sample caveat.
- [scikit-learn — Probability calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html) — reliability diagrams + Brier/log-loss.
- [Predicting Good Probabilities With Supervised Learning (Niculescu-Mizil & Caruana, ICML 2005)](https://www.cs.cornell.edu/~alexn/papers/calibration.icml05.crc.rev3.pdf) — sigmoid distortion of max-margin methods; Platt vs isotonic.
- [Understanding Model Calibration — a gentle intro to ECE (arXiv:2501.19047)](https://arxiv.org/html/2501.19047v2) — reliability diagrams, ECE formula, binning limitations.

> Core Node: [[START_HERE]]
