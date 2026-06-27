---
type: concept
title: Feature Engineering
description: Transforming raw data into model-ready features — encoding, scaling, interactions, and the leakage traps that sink them.
tags: [machine-learning, feature-engineering, preprocessing, data-leakage]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- On tabular problems, feature quality usually beats model choice — and the most common production bug, **data leakage**, hides in the preprocessing. Done right, feature engineering raises the ceiling for [[Concepts/Supervised_Learning]]; done carelessly, it quietly leaks the label and inflates offline scores.

## Categorical Encoding (and its leakage trap)
- **One-hot** is safe but explodes dimensionality on high cardinality. **Target/mean encoding** compresses to one column but *leaks the label* unless done with **cross-fitting** — encode each fold using statistics from the *other* folds (scikit-learn's `TargetEncoder.fit_transform` does this; `fit().transform()` does not).
- Encoders must be fit **inside** the CV loop / `Pipeline`, never on the full dataset before the split — see [[Concepts/Training_Validation_Test_Splits]].

## Scaling, Transforms, Interactions
- **Scaling:** standardization, min-max, robust (median/IQR for outliers), power transforms (Box-Cox/Yeo-Johnson). Fit on train only; apply the *same* transform to val/test/serving.
- **Interactions:** feature crosses (categorical Cartesian products) let linear models capture nonlinearity; `PolynomialFeatures`/`SplineTransformer` are the numeric analog. Both inflate feature count fast.
- **Datetime / missing / selection:** encode periodic features with sin/cos (so Dec→Jan is adjacent); impute missing values (+ optional missingness indicator) fit on train; prune with feature selection / PCA.

## Train/Serve Consistency
- A **feature store** (e.g. Feast) keeps an offline store (point-in-time-correct joins for training) and an online store (low-latency serving) from one feature definition — eliminating **training-serving skew**, the bug where train-time and serve-time feature computation silently diverge.

## GBDTs vs Deep Nets
- Gradient-boosted trees on tabular data lean heavily on manual FE (encoding, interactions, binning) and remain a strong baseline; deep nets learn representations end-to-end, **reducing — not eliminating** — manual FE.

## Related
- [[Concepts/Supervised_Learning]], [[Concepts/Training_Validation_Test_Splits]], [[Concepts/Data_Centric_AI]], [[Concepts/Unsupervised_Learning]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [scikit-learn — Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html) — scaling, encoding, polynomial/spline features, fit-on-train discipline.
- [scikit-learn — Target Encoder's internal cross-fitting](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder_cross_val.html) — why target encoding leaks without cross-fitting (~0.86 train/0.63 test vs ~0.80/0.79).
- [Google ML Crash Course — Feature crosses](https://developers.google.com/machine-learning/crash-course/categorical-data/feature-crosses) — encoding interactions; sparsity blowup.
- [Feature Engineering for Machine Learning (Zheng & Casari, O'Reilly)](https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/) — the standard FE reference.
- [Feast — Open Source Feature Store](https://docs.feast.dev/) — offline/online stores and point-in-time joins to prevent train/serve skew.

> Core Node: [[START_HERE]]
