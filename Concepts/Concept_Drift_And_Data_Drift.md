---
type: concept
title: Concept Drift and Data Drift
description: Why production models decay — covariate, label, and concept drift, how to detect them, and when to retrain.
tags: [machine-learning, mlops, drift, monitoring]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- A model is trained on a snapshot of a world that keeps moving — user behavior, adversaries, seasonality, schema changes. Drift is the silent failure mode: accuracy decays with no error thrown. Monitoring for it is what turns a one-time [[Concepts/Supervised_Learning]] model into a maintained production system.

## Decompose P(X, Y) = P(Y|X)·P(X)
- **Covariate / data drift** — input distribution `P(X)` changes, `P(Y|X)` stable.
- **Label / prior shift** — the target base rate `P(Y)` changes.
- **Concept drift** — the decision boundary `P(Y|X)` changes (Gama: *real* drift; a `P(X)`-only change is *virtual* drift).
- Key consequence: **only real concept drift necessarily degrades accuracy.** Covariate shift hurts only where the model was already weak — so "input drift detected" is a warning, not proof of decay.

## Temporal Patterns
- **Sudden/abrupt** (instant switch), **incremental** (slow monotonic transition), **gradual** (old/new alternate, new rising), **recurring/seasonal** (known concepts reappear) — distinct from one-off outliers.

## Detection
- **Without labels (data drift):** per-feature tests — KS (numerical), Chi-square (categorical), distance/divergence (Wasserstein, Jensen–Shannon, **PSI**); multivariate methods (PCA-reconstruction error, domain classifier) catch correlated shifts univariate tests miss.
- **With labels (concept/performance drift):** monitor live accuracy/AUC/error. Because labels are often **delayed**, use data-drift signals or estimated-performance methods as a leading proxy in the interim.

## Retraining Triggers
- Trigger on sustained performance drop, drift alerts crossing thresholds, or a scheduled cadence; mitigate with windowed/incremental retraining, ensembles, and reference-window refresh. Drift detection is the trigger layer feeding the retraining pipeline — closely tied to [[Concepts/Data_Centric_AI]].

## Related
- [[Concepts/Data_Centric_AI]], [[Concepts/Model_Generalization_And_Overfitting]], [[Concepts/Evaluation_Metrics_Classification_Regression]], [[Concepts/Training_Validation_Test_Splits]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [A Survey on Concept Drift Adaptation (Gama et al., ACM Computing Surveys 2014, PDF)](https://mpechen.win.tue.nl/publications/pubs/Gama_ACMCS_AdaptationCD_accepted.pdf) — canonical taxonomy; real vs. virtual drift; the P(X,Y) formalism.
- [What is data drift, and how to detect and handle it (Evidently AI)](https://www.evidentlyai.com/ml-in-production/data-drift) — data vs. concept drift; drift as a proxy under delayed labels.
- [Data Drift algorithm explainer (Evidently docs)](https://docs.evidentlyai.com/metrics/explainer_drift) — default tests/thresholds (KS, Chi-square, Wasserstein, JS).
- [Detecting Data Drift (NannyML docs)](https://nannyml.readthedocs.io/en/stable/tutorials/detecting_data_drift.html) — P(X) vs P(Y|X) framing; univariate vs multivariate.
- [Measuring Data Drift with PSI (Fiddler AI)](https://www.fiddler.ai/blog/measuring-data-drift-population-stability-index) — PSI formula and threshold bands (<0.1 / 0.1–0.2 / >0.2).

> Core Node: [[START_HERE]]
