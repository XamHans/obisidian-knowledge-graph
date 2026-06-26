---
type: concept
title: Hybrid Retrieval
description: Combines dense vector search with sparse BM25 via Reciprocal Rank Fusion — the single biggest quality jump over naive RAG.
tags: [rag, retrieval, bm25, fusion]
stability: stable
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Dense [[Concepts/Vector_Search|vector search]] handles paraphrase and concepts but misses **exact terms** — product codes, named entities, rare jargon. Sparse keyword search (BM25) nails exact matches but misses meaning. Combining them is the **single biggest quality jump** over naive RAG.

## How It Works
- **Sparse** retriever: BM25 (or SPLADE for learned sparse) — lexical, exact-term, no embedding needed.
- **Dense** retriever: [[Concepts/Text_Embeddings|embedding]]-based ANN — semantic.
- **Fusion via Reciprocal Rank Fusion (RRF):** each document gets `1 / (k + rank)` from each retriever (k ≈ 60), summed across retrievers. RRF is **rank-only**, so it sidesteps the score-incompatibility problem that breaks naively weighted combinations.

## Evidence
- On the WANDS e-commerce benchmark, tuned hybrid + RRF reaches ~0.75 NDCG — a ~7% lift over BM25 (0.70) or pure vector (0.70) alone.

## Related
- [[Concepts/Vector_Search]], [[Concepts/Reranking]], [[Concepts/Text_Embeddings]], [[Concepts/Retrieval_Augmented_Generation]]
- Tools: [[Tools/PGVector]]
- Hub: [[Hubs/RAG]]

## Sources
- [Hybrid Search for RAG: BM25 + Dense (2026) — Denser.ai](https://denser.ai/blog/hybrid-search-for-rag/)
- [Hybrid Search Done Right: BM25 + HNSW + RRF — Medium](https://ashutoshkumars1ngh.medium.com/hybrid-search-done-right-fixing-rag-retrieval-failures-using-bm25-hnsw-reciprocal-rank-fusion-a73596652d22)

> Core Node: [[START_HERE]]
