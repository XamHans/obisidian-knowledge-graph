---
type: concept
title: ML Experiment Tracking
description: Logging params, metrics, artifacts, and code/data/env versions so ML runs are comparable, reproducible, and promotable.
tags: [machine-learning, mlops, experiment-tracking, reproducibility]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Without tracking, a hyperparameter search produces results you can't compare, a failure can't be traced to its inputs, and a teammate can't reproduce your run. Tracking is the system-of-record that makes [[Concepts/Hyperparameter_Optimization]] and team collaboration possible at all.

## Runs vs Experiments
- A **run** is one execution of training code, recording params, metrics, artifacts, and timing. An **experiment** is the logical container grouping related runs so they can be searched, sorted, and compared. This data model is shared across MLflow, Weights & Biases, and others — they are implementations of one discipline.

## What to Log — the full quartet
- Reproducibility needs **code + data + environment + hyperparameters**, not just metrics:
  - **Parameters** (config inputs) and **metrics** (time-series, e.g. per-step loss, so convergence is visible).
  - **Artifacts** (model weights, plots, data files).
  - **Code version** (git commit) and **dataset references** (split pointers, schema, feature defs).
  - **Environment** (container image, runtime deps). The standard: identical inputs → identical results.

## Model Registry & Lineage
- A registry turns ad-hoc runs into a governed lifecycle: each registered **version** links back to the exact run that produced it (**lineage**), and mutable **aliases/stages** (e.g. "champion") let you promote or roll back production traffic without retraining.

## Comparing Runs Is the Payoff
- The core value-add is listing/sorting runs by metric (e.g. order by `val_loss`) and overlaying metric curves — the substrate every HPO sweep logs into and the shared record a team builds on.

## Related
- [[Concepts/Hyperparameter_Optimization]], [[Concepts/Training_Validation_Test_Splits]], [[Concepts/Data_Centric_AI]], [[Concepts/Evaluation_Metrics_Classification_Regression]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/) — logging params/metrics/artifacts/code/datasets; runs vs experiments.
- [Weights & Biases — Experiments](https://docs.wandb.ai/models/track) — runs, config, system metrics, artifacts, multi-run dashboards.
- [MLflow Model Registry](https://mlflow.org/docs/latest/ml/model-registry/) — versioning, lineage, aliases, lifecycle.
- [ml-ops.org — MLOps Principles](https://ml-ops.org/content/mlops-principles) — reproducibility and versioning of data/code/model/environment.
- [Google Cloud — MLOps: Continuous delivery and automation pipelines](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — the ML metadata store and what to version.

> Core Node: [[START_HERE]]
