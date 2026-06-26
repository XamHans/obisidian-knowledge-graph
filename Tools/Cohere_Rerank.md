---
type: tool
title: Cohere Rerank
description: Managed cross-encoder reranking API that reorders retrieved candidates by query relevance and returns relevance scores.
tags: [rag, reranking, cross-encoder]
resource: https://docs.cohere.com/docs/rerank-overview
stability: volatile
as_of: 2026-06
reviewed: 2026-06
lifecycle: ga
---

## Definition
- Hosted [[Concepts/Reranking|reranking]] endpoint: send a query plus a list of retrieved documents, get back the documents reordered by relevance with a score each. A managed cross-encoder, so no model to host.

## Capabilities
- Second-stage precision on top of a first-stage [[Concepts/Vector_Search|vector]] or [[Concepts/Hybrid_Retrieval|hybrid]] retriever — the standard retrieve-then-rerank shape.
- Multilingual reranking and long-document support; returns `top_n` with relevance scores for thresholding.

## Integration Patterns
- Retrieve a wide candidate set (e.g. 50–100), pass query + candidates to the rerank endpoint, keep `top_n` (e.g. 5) for the prompt — controls token load on the LLM.
- Score-threshold to drop weak matches before they reach generation.

## Related Concepts
- [[Concepts/Reranking]], [[Concepts/Hybrid_Retrieval]], [[Concepts/Vector_Search]]

## Linked Hubs
- [[Hubs/RAG]]

> Core Node: [[START_HERE]]
