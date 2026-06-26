---
type: concept
title: RAG Evaluation
description: Measures retrieval and generation quality separately — RAGAS faithfulness, answer relevancy, context precision and recall.
tags: [rag, evaluation, ragas, metrics]
stability: evolving
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- RAG fails *silently* — a fluent answer can be completely ungrounded. You cannot improve what you do not measure, and you must measure **retrieval quality separately from generation quality** to know which half to fix.

## RAGAS — the four core metrics
Retrieval side (did we fetch the right context?):
- **Context Recall** — of the information needed, how much did retrieval actually surface?
- **Context Precision** — of what was retrieved, how much is relevant (vs. noise)?

Generation side (did we use it faithfully?):
- **Faithfulness** — fraction of claims in the answer verifiable against the retrieved context (hallucination check).
- **Answer Relevancy** — does the answer actually address the question?

## Beyond RAGAS
- **Retrieval IR metrics** — recall@k, MRR, NDCG against a labelled gold set.
- **LLM-as-judge** — scalable scoring, but needs its own calibration against human labels.
- **Build a gold set first** — a small, curated query→answer set is the foundation of every honest RAG eval.

## Related
- [[Concepts/Retrieval_Augmented_Generation]], [[Concepts/Reranking]], [[Concepts/Hybrid_Retrieval]], [[Concepts/Query_Transformation]]
- Hub: [[Hubs/RAG]]

## Sources
- [List of available metrics — RAGAS docs](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)
- [RAG Evaluation Metrics — Confident AI](https://www.confident-ai.com/blog/rag-evaluation-metrics-answer-relevancy-faithfulness-and-more)

> Core Node: [[START_HERE]]
