---
type: concept
title: Query Transformation
description: Rewriting the user query before search — multi-query, HyDE, decomposition, step-back — to lift retrieval recall.
tags: [rag, retrieval, query-rewriting, recall]
stability: evolving
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- The user's raw query is often a poor retrieval key — vague, underspecified, or using different vocabulary than the corpus. Since [[Concepts/Retrieval_Augmented_Generation|retrieval is the bottleneck]], rewriting the query before search is one of the cheapest recall wins.

## Techniques (combine them — each fixes a different failure)
- **Multi-query** — generate N reformulations from different angles, retrieve for each, union the results. Covers intent ambiguity.
- **HyDE (Hypothetical Document Embeddings)** — have the LLM draft a hypothetical *answer*, embed *that* for retrieval. Works when the corpus is dense, descriptive prose where a pseudo-answer aligns better than a short question.
- **Decomposition** — split a complex/multi-hop question into sub-questions, retrieve per sub-question. Surfaces different evidence clusters.
- **Step-back** — generalize to a broader question first to pull in foundational context.
- **Query expansion** — add synonyms/related terms to close vocabulary gaps (helps [[Concepts/Hybrid_Retrieval|sparse]] retrieval).

## Tradeoff
- Each transformation adds LLM latency and more retrieval calls. Use [[Concepts/RAG_Evaluation|evaluation]] to confirm the recall lift is worth the cost.

## Related
- [[Concepts/Retrieval_Augmented_Generation]], [[Concepts/Vector_Search]], [[Concepts/Hybrid_Retrieval]], [[Concepts/RAG_Evaluation]]
- Hub: [[Hubs/RAG]]

## Sources
- [RAG Query Transformation: Multi-Query, Decomposition, Step-Back — DEV](https://dev.to/jamesli/in-depth-understanding-of-rag-query-transformation-optimization-multi-query-problem-decomposition-and-step-back-27jg)
- [HyDE, Query Expansion, and Multi-Query RAG — Medium](https://medium.com/@mudassar.hakim/retrieval-is-the-bottleneck-hyde-query-expansion-and-multi-query-rag-explained-for-production-c1842bed7f8a)

> Core Node: [[START_HERE]]
