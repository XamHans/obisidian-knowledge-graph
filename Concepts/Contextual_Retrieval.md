---
type: concept
title: Contextual Retrieval
description: Anthropic's technique of prepending LLM-generated document context to each chunk before indexing; cuts retrieval failures up to 49–67%.
tags: [rag, chunking, retrieval, anthropic]
stability: evolving
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- A [[Concepts/Chunking_Strategies|chunk]] ripped from its document loses context — "the company reported 3% growth" no longer says *which* company or *when*. That ambiguity is a top cause of retrieval failure. **Contextual Retrieval** (Anthropic) fixes it by prepending a short, LLM-generated, chunk-specific summary of the surrounding document *before* embedding and indexing.

## How It Works
- **Contextual Embeddings** — for each chunk, an LLM writes 1–2 sentences situating it in the whole document; that context is prepended, then the chunk is [[Concepts/Text_Embeddings|embedded]].
- **Contextual BM25** — the same enriched chunk is also indexed for keyword/[[Concepts/Hybrid_Retrieval|sparse]] search.

## Evidence (top-20 retrieval-failure reduction)
- Contextual embeddings alone: **−35%**.
- Contextual embeddings + contextual BM25: **−49%**.
- Plus [[Concepts/Reranking|reranking]]: **−67%**.

## Cost & When to Use
- Adds one LLM pass *per chunk at index time* — mitigate with prompt caching. Use it when retrieval quality is the priority and the corpus is worth the indexing cost. Cheaper alternative: late chunking (see [[Concepts/Chunking_Strategies]]).

## Related
- [[Concepts/Chunking_Strategies]], [[Concepts/Text_Embeddings]], [[Concepts/Hybrid_Retrieval]], [[Concepts/Reranking]]
- Hub: [[Hubs/RAG]]

## Sources
- _Ingested receipt:_ [[Sources/Contextual_Retrieval_Anthropic]] — method + benchmark numbers (private)
- [Introducing Contextual Retrieval — Anthropic](https://www.anthropic.com/news/contextual-retrieval)
- [Contextual Retrieval: A Guide with Implementation — DataCamp](https://www.datacamp.com/tutorial/contextual-retrieval-anthropic)

> Core Node: [[START_HERE]]
