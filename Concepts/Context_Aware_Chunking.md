---
type: concept
status: active
hub: RAG
persona: Professional Seeking AI Mastery
---

## Why It Matters
- Chunk boundaries that respect document structure produce higher-quality embeddings and reduce hallucinations from split sentences or tables.

## Playbook Moves
- **Detect natural boundaries with embeddings** — Use tools like Dockling to find coherent split points instead of fixed-length cuts. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^context-chunking]]
- **Preserve structure for downstream recall** — Maintain section integrity so rerankers and LLMs receive self-contained slices. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^context-chunking]]
- **Chain with reranking and hierarchies** — Combine quality chunks with reranking and parent-child metadata to keep context precise yet explorable. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^context-chunking]]
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]

## Connected Projects
- [[Projects/AI_Native_Engineer]]

## Linked Technologies
- [[Technologies/Dockling]]
- [[Technologies/PGVector]]

## Related Concepts
- [[Resources/Concepts/Hierarchical_RAG]]
- [[Resources/Concepts/Contextual_Retrieval]]
- [[Resources/Concepts/RAG_Re_Ranking]]

> Related Hub: [[Hubs/RAG]]

> Core Node: [[Projects/AI_Native_Engineer]]
