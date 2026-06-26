---
type: concept
title: Vector Search
description: Fast approximate nearest-neighbour retrieval over embeddings (HNSW/IVF), trading a little recall for large speed gains.
tags: [rag, retrieval, ann, vector-db]
stability: stable
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Once documents are [[Concepts/Text_Embeddings|embedded]], retrieval = "find the nearest vectors to the query vector." At scale you cannot brute-force compare against millions of vectors, so **Approximate Nearest Neighbour (ANN)** search trades a little recall for orders-of-magnitude speed.

## Core Ideas
- **Similarity metric** — cosine or dot product on normalized embeddings.
- **ANN indexes** — HNSW (graph-based, high recall, memory-heavy) and IVF/PQ (cluster + compress, cheaper memory). The knob is the **recall ↔ latency** tradeoff.
- **top-k** — retrieve a wide candidate set first (recall), then narrow with [[Concepts/Reranking|reranking]] (precision).
- **Metadata filtering** — combine vector similarity with structured filters (date, source, tenant) for access control and relevance.

## Limits
- Pure dense search underweights **exact tokens** (codes, names, rare terms). That gap is why production systems use [[Concepts/Hybrid_Retrieval]].

## Related
- [[Concepts/Text_Embeddings]], [[Concepts/Hybrid_Retrieval]], [[Concepts/Reranking]], [[Concepts/Chunking_Strategies]]
- Tools: [[Tools/PGVector]]
- Hub: [[Hubs/RAG]]

## Sources
- [Hybrid Search: BM25, Vector & Reranking 2026 — Digital Applied](https://www.digitalapplied.com/blog/hybrid-search-bm25-vector-reranking-reference-2026)

> Core Node: [[START_HERE]]
