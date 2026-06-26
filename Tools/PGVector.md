---
type: tool
title: pgvector
description: Postgres extension adding vector search; stores embeddings alongside relational data for dense and hybrid retrieval.
tags: [rag, vector-db, postgres]
resource: https://github.com/pgvector/pgvector
stability: evolving
as_of: 2026-06
reviewed: 2026-06
lifecycle: ga
---

## Definition
- Open-source Postgres extension that adds a `vector` column type plus similarity operators, turning a standard Postgres database into a vector store for [[Concepts/Vector_Search|vector search]].

## Capabilities
- Stores [[Concepts/Text_Embeddings|embeddings]] alongside relational data — no separate vector database to operate.
- ANN indexes: **HNSW** (high recall) and **IVFFlat** (lower memory); distance ops for cosine, L2, and inner product.
- Combines vector similarity with SQL `WHERE` filters and full-text search — a practical base for [[Concepts/Hybrid_Retrieval|hybrid retrieval]] (dense + BM25-style keyword) in one engine.

## Integration Patterns
- Co-locate embeddings with chunk metadata (parent/child IDs, source, tenant) to enable metadata filtering and access control in the same query.
- Pair first-stage pgvector retrieval with a [[Concepts/Reranking|cross-encoder reranker]] to control how many chunks reach the LLM.

## Related Concepts
- [[Concepts/Vector_Search]], [[Concepts/Hybrid_Retrieval]], [[Concepts/Text_Embeddings]]

## Linked Hubs
- [[Hubs/RAG]]

> Core Node: [[START_HERE]]
