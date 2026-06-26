---
type: concept
title: Text Embeddings
description: Dense vector representations of text where semantic similarity becomes geometric proximity — the substrate of dense retrieval.
tags: [rag, embeddings, retrieval, vectors]
stability: stable
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Embeddings map text to dense vectors where **semantic similarity becomes geometric proximity**. They are the substrate of dense retrieval: "find related meaning" turns into "find nearby vectors."

## Core Ideas
- **Bi-encoder models** embed query and document *independently*, so document vectors can be precomputed and indexed once — fast at query time. (Contrast: cross-encoders in [[Concepts/Reranking]] score a pair jointly, far more accurate but uncacheable.)
- **Similarity** is usually cosine (or dot product on normalized vectors). Normalize consistently.
- **Dimensionality** trades quality for storage/latency; many models support shortening (e.g. Matryoshka) to cut index size.
- **Domain fit matters** — a general model underperforms on legal/medical/code jargon. [[Concepts/Fine_Tuned_Embeddings|Fine-tuning]] or a domain model lifts recall.

## Pitfalls
- An embedding only captures what was *in the chunk* — context lost during [[Concepts/Chunking_Strategies|chunking]] cannot be recovered by the embedder. This motivates [[Concepts/Contextual_Retrieval]].

## Related
- [[Concepts/Vector_Search]], [[Concepts/Chunking_Strategies]], [[Concepts/Reranking]], [[Concepts/Hybrid_Retrieval]]
- Hub: [[Hubs/RAG]]

## Sources
- [Sparse vs Dense Retrieval for RAG — ML Journey](https://mljourney.com/sparse-vs-dense-retrieval-for-rag-bm25-embeddings-and-hybrid-search/)
- [Contextual Retrieval — Anthropic](https://www.anthropic.com/news/contextual-retrieval)

> Core Node: [[START_HERE]]
