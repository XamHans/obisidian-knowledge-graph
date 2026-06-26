---
type: concept
title: Retrieval-Augmented Generation
description: Grounds LLM answers in an external knowledge base via the index→retrieve→generate pipeline, where retrieval is the bottleneck.
tags: [rag, retrieval, architecture, grounding]
stability: stable
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- RAG grounds LLM answers in an external, up-to-date knowledge base instead of relying on the model's frozen parametric memory. That cuts hallucination, lets you use private or fresh data without retraining, and gives **citeable provenance** for every answer.
- The hard part is not generation — it's getting the *right* context in front of the model. Treat the **knowledge source and retrieval quality as the primary investment**, not the model.

## The Pipeline
RAG has two phases:

- **Indexing (offline):** ingest documents → [[Concepts/Chunking_Strategies|chunk]] → [[Concepts/Text_Embeddings|embed]] → store vectors (+ keyword index) in a retrievable store.
- **Inference (online):** embed the query → [[Concepts/Vector_Search|retrieve]] candidates (ideally [[Concepts/Hybrid_Retrieval|hybrid]]) → [[Concepts/Reranking|rerank]] for precision → inject top-k chunks into the prompt → LLM generates a grounded, attributed answer.

## Key Truths
- **Retrieval is the bottleneck.** When a RAG system fails, the failure is in retrieval ~73% of the time, not generation. Fix retrieval first.
- **Hybrid search is the single biggest jump** in quality over a naive vector-only pipeline.
- **Garbage chunks cap the ceiling** — no reranker or prompt fixes context that was never retrieved.
- Improve [[Concepts/Query_Transformation|the query]] and the [[Concepts/Chunking_Strategies|chunks]] before reaching for a bigger model.

## Related
- [[Concepts/Chunking_Strategies]], [[Concepts/Text_Embeddings]], [[Concepts/Vector_Search]], [[Concepts/Hybrid_Retrieval]], [[Concepts/Reranking]], [[Concepts/Query_Transformation]], [[Concepts/Contextual_Retrieval]], [[Concepts/RAG_Evaluation]]
- Hub: [[Hubs/RAG]]

## Sources
- [What Is RAG? How Retrieval-Augmented Generation Works in 2026 — Atlan](https://atlan.com/know/what-is-rag/)
- [Engineering the RAG Stack (arXiv 2601.05264)](https://arxiv.org/html/2601.05264v1)
- [RAG in 2025: Proven Strategies at Scale — Morphik](https://www.morphik.ai/blog/retrieval-augmented-generation-strategies)

> Core Node: [[START_HERE]]
