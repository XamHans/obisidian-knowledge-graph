---
type: concept
title: Reranking
description: Second-stage cross-encoder that reorders retrieved candidates for precision before they hit the limited prompt budget.
tags: [rag, reranking, cross-encoder, precision]
stability: stable
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- First-stage retrieval ([[Concepts/Vector_Search|vector]] / [[Concepts/Hybrid_Retrieval|hybrid]]) is tuned for **recall** — cast a wide net cheaply. A reranker is tuned for **precision** — reorder that net so the most relevant chunks land in the limited prompt budget. This two-stage "retrieve-then-rerank" is the standard production shape.

## How It Works
- A **cross-encoder** feeds query + document *together* through a transformer, so attention models their interaction directly. Far more accurate than the independent [[Concepts/Text_Embeddings|bi-encoder]] embeddings used for first-stage search.
- The cost: it can't be precomputed, so it's too slow for the whole corpus. Apply it only to the **top-N candidates** (e.g. rerank 50 → keep 5).
- Common rerankers: Cohere Rerank, BGE / Jina cross-encoders.

## Payoff
- Adding reranking on top of [[Concepts/Contextual_Retrieval|contextual retrieval]] pushes the top-20 retrieval-failure reduction to ~67%.

## Related
- [[Concepts/Hybrid_Retrieval]], [[Concepts/Vector_Search]], [[Concepts/Text_Embeddings]], [[Concepts/RAG_Evaluation]]
- Tools: [[Tools/Cohere_Rerank]]
- Hub: [[Hubs/RAG]]

## Sources
- [Hybrid Search and Re-ranking in Production RAG 2026 — AppScale](https://appscale.blog/en/blog/hybrid-search-and-reranking-production-rag-bm25-dense-cross-encoder-2026)
- [Contextual Retrieval — Anthropic](https://www.anthropic.com/news/contextual-retrieval)

> Core Node: [[START_HERE]]
