---
type: concept
title: Unsupervised Learning
description: Finding structure in unlabeled data — clustering, dimensionality reduction, anomaly detection — when labels are scarce or unknown.
tags: [machine-learning, unsupervised-learning, clustering, dimensionality-reduction]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Labels are expensive and most raw data arrives **without them**. Unsupervised methods surface latent structure — segments, topics, outliers — *before* you spend labeling budget, and feed a sharper taxonomy back into [[Concepts/Supervised_Learning]]. The hard part is that with no ground truth, **validation is a judgment call**.

## The Families
- **Clustering** — group similar samples. **k-means** minimizes within-cluster sum-of-squares (inertia) but assumes **convex *and isotropic*** (roughly spherical, equal-variance) clusters; it fails on elongated, unequal-size, or varying-density groups. **HDBSCAN** drops the single-density assumption of DBSCAN, finds clusters across density scales, needs no preset `k`, and labels outliers as noise (`-1`).
- **Dimensionality reduction** — **PCA** (linear, fast, interpretable variance) vs. **UMAP/t-SNE** (nonlinear). UMAP is positioned as a general-purpose DR method (better global-structure retention, no embedding-dim cap); **t-SNE is for 2–3D visualization only**.
- **Anomaly detection** — density-based (LOF, GMM likelihood) *and* isolation-based (**Isolation Forest** — a partition method, *not* a density estimator).
- **Association / topic discovery** — co-occurrence and latent themes.

## Two Footguns That Bite Everyone
- **k-means is non-deterministic.** Its objective is non-convex, so it only finds a *local* optimum that depends on initialization. Always use **k-means++ seeding + multiple restarts** (keep lowest inertia), and **run PCA first in high dimensions** (Euclidean distance degrades under the curse of dimensionality).
- **t-SNE plots are routinely over-read.** Cluster *sizes* carry no meaning, *distances between* clusters often carry none, **perplexity** changes the picture dramatically, and pure noise can form convincing "clusters" — always view several perplexities/runs. (UMAP/t-SNE *coordinates* are for viewing, not as downstream feature vectors.)

## The Evaluation Problem
- No labels means no accuracy. Use **internal metrics** — **silhouette ∈ [−1, 1]** (higher better; ≈0 = overlapping, negative = likely mis-assigned), **Davies–Bouldin ≥ 0** (lower better) — *plus* **downstream utility**: does the segmentation improve a real decision? Internal metrics structurally favor convex clusters, so they can unfairly penalize valid density-based results.

## Where It Fits
- **Discovery before labeling:** cluster first to shape the label taxonomy, then label representative samples.
- **On embeddings:** clustering vectors from [[Concepts/Text_Embeddings]] (retrieved via [[Concepts/Vector_Search]]) is a common way to mine themes from a corpus.

## Related
- [[Concepts/Supervised_Learning]], [[Concepts/Self_Supervised_Learning]], [[Concepts/Text_Embeddings]], [[Concepts/Vector_Search]]
- _Next-wave (forward refs):_ [[Concepts/Feature_Engineering]], [[Concepts/Representation_Learning_For_Vision]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [UMAP: Uniform Manifold Approximation and Projection (McInnes et al., arXiv:1802.03426)](https://arxiv.org/abs/1802.03426) — UMAP as general-purpose DR; global structure & runtime vs. t-SNE.
- [Visualizing Data using t-SNE (van der Maaten & Hinton, JMLR 2008)](https://www.jmlr.org/papers/v9/vandermaaten08a.html) — the original t-SNE, designed for 2–3D visualization.
- [How to Use t-SNE Effectively (Distill, 2016)](https://distill.pub/2016/misread-tsne/) — the canonical guide to t-SNE viewing pitfalls.
- [scikit-learn — Clustering (User Guide)](https://scikit-learn.org/stable/modules/clustering.html) — k-means assumptions, HDBSCAN, silhouette/Davies–Bouldin.
- [How HDBSCAN Works (hdbscan docs)](https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html) — mutual reachability, condensed tree, stability-based extraction.
- [CS229 — The k-means clustering algorithm (Ng, Stanford)](https://cs229.stanford.edu/notes2020spring/cs229-notes7a.pdf) — k-means as coordinate descent on a non-convex distortion.

> Core Node: [[START_HERE]]
