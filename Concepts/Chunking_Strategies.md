---
type: concept
title: Chunking Strategies
description: How documents are split for retrieval — fixed, recursive, semantic, late, and contextual chunking, and when each pays off.
tags: [rag, chunking, retrieval, indexing]
stability: evolving
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Chunk size and boundaries decide what the retriever *can* find. A chunk too large dilutes the embedding with noise; too small loses the context the LLM needs to answer. Chunking sets the ceiling for the whole pipeline.

## The Spectrum (cheap → expensive)
- **Fixed / character split** — split every N characters. Fast, dumb, breaks mid-thought. Baseline only.
- **Recursive / structural** — split on document structure (headings, paragraphs, sentences) with overlap. Strong default.
- **Semantic** — embed sentences, cut where meaning shifts. ~+9% recall but ~14× slower; sentence-level chunking matches it up to ~5k tokens for far less cost.
- **Late chunking** — embed the *whole document* first, then pool token embeddings into chunks. Preserves cross-chunk context, uses the embedding model only (cheap). Like a "smarter embedding" with no architecture change.
- **Contextual** — prepend an LLM-generated, document-wide blurb to each chunk before embedding (see [[Concepts/Contextual_Retrieval]]). Best quality, highest index-time cost.

## Practical Defaults
- **~512 tokens** is a strong starting chunk size — small enough for precise matches, large enough to answer from. Add overlap (~10–20%). Tune to content type (code, tables, and prose chunk differently).

## Related
- [[Concepts/Text_Embeddings]], [[Concepts/Contextual_Retrieval]], [[Concepts/Vector_Search]], [[Concepts/Retrieval_Augmented_Generation]]
- Hub: [[Hubs/RAG]]

## Sources
- [RAG Chunking Strategies: A 2026 Retrieval Playbook — Digital Applied](https://www.digitalapplied.com/blog/rag-chunking-strategies-2026-retrieval-quality-playbook)
- [Reconstructing Context: Evaluating Advanced Chunking Strategies (arXiv 2504.19754)](https://arxiv.org/abs/2504.19754)
- [Late Chunking vs Contextual Retrieval — KX Systems](https://medium.com/kx-systems/late-chunking-vs-contextual-retrieval-the-math-behind-rags-context-problem-d5a26b9bbd38)

> Core Node: [[START_HERE]]
