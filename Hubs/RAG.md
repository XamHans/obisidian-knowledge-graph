---
type: hub
title: RAG
description: Map of content for Retrieval-Augmented Generation — the foundational concept path from chunking to evaluation, plus tools.
tags: [rag, retrieval]
stability: stable
reviewed: 2026-06
---

## Overview
- Map of content for **Retrieval-Augmented Generation**: grounding LLM answers in an external knowledge base. Retrieval — not generation — is the bottleneck, so most of the leverage lives in chunking, embeddings, search, and reranking.

## Foundational Path
Read in order — each builds on the last:

1. [[Concepts/Retrieval_Augmented_Generation]] — the pipeline and why it exists
2. [[Concepts/Chunking_Strategies]] — how documents are split
3. [[Concepts/Text_Embeddings]] — turning text into searchable vectors
4. [[Concepts/Vector_Search]] — fast nearest-neighbour retrieval
5. [[Concepts/Hybrid_Retrieval]] — dense + BM25 with RRF (biggest quality jump)
6. [[Concepts/Reranking]] — precision via cross-encoders
7. [[Concepts/Query_Transformation]] — multi-query, HyDE, decomposition
8. [[Concepts/Contextual_Retrieval]] — Anthropic's chunk-context technique
9. [[Concepts/RAG_Evaluation]] — RAGAS: faithfulness, relevancy, context precision/recall

## Tools
- [[Tools/PGVector]] — Postgres vector store for dense + hybrid retrieval
- [[Tools/Cohere_Rerank]] — managed cross-encoder reranking endpoint

## Related Hubs
- [[Hubs/LLM_Evals]] — evaluation discipline that RAG eval builds on
- [[Hubs/AI_Agents]] — agentic RAG and tool-driven retrieval

> Core Node: [[START_HERE]]
