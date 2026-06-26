---
type: concept
stability: stable
reviewed: 2026-06
hub: RAG
---

## Why It Matters
- Enriching chunks with LLM-written context blurbs improves retrieval precision by clarifying how each slice fits within the broader document.

## Playbook Moves
- **Prepend summaries to chunks** — Add a short LLM-generated description before each chunk to anchor meaning during embedding. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^contextual-chunk]]
- **Budget for slower ingest** — Account for extra LLM calls when enriching every chunk during indexing. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^contextual-chunk]]
- **Pair with structure-aware chunking** — Use boundary-respecting chunkers so the prepended summaries map cleanly to coherent sections. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^context-chunking]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^contextual-chunk]]
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^context-chunking]]

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/Dockling]]
- [[Tools/PGVector]]

## Related Concepts
- [[Concepts/Context_Aware_Chunking]]
- [[Concepts/RAG_Re_Ranking]]
- [[Concepts/Fine_Tuned_Embeddings]]

> Related Hub: [[Hubs/RAG]]

> Core Node: [[START_HERE]]
