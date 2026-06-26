---
type: concept
stability: stable
reviewed: 2026-06
hub: RAG
---

## Why It Matters
- Embedding documents before chunking retains global context inside each slice, improving relevance at the cost of complexity.

## Playbook Moves
- **Embed first, chunk later** — Apply the embedding model to the full document, then segment token embeddings instead of raw text. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^late-chunking]]
- **Preserve full-document context** — Use embedding-first chunks when you need each slice to carry knowledge of the whole file. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^late-chunking]]
- **Plan for complexity** — Reserve late chunking for specialized cases since implementation overhead is high. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^late-chunking]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^late-chunking]]

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/PGVector]]
- [[Tools/Dockling]]

## Related Concepts
- [[Concepts/Context_Aware_Chunking]]
- [[Concepts/Hierarchical_RAG]]
- [[Concepts/Fine_Tuned_Embeddings]]

> Related Hub: [[Hubs/RAG]]

> Core Node: [[START_HERE]]
