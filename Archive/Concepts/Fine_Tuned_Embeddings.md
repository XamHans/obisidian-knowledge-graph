---
type: concept
stability: stable
reviewed: 2026-06
hub: RAG
---

## Why It Matters
- Domain-tuned embedding models improve retrieval precision (often 5–10%) and can let smaller models outperform generic larger ones on specialized corpora.

## Playbook Moves
- **Train on domain pairs** — Fine-tune embeddings with in-domain examples (e.g., legal, medical) to lift similarity accuracy. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^ft-embed]]
- **Beat bigger base models** — Use tuned small models to outperform larger generic ones when data is available. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^ft-embed]]
- **Optimize for target similarity** — Shift objectives (e.g., sentiment-focused vs semantic) to align retrieval with business needs. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^ft-embed]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^ft-embed]]

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/PGVector]]
- [[Tools/Neon_Postgres]]

## Related Concepts
- [[Concepts/Contextual_Retrieval]]
- [[Concepts/Late_Chunking]]
- [[Concepts/RAG_Re_Ranking]]

> Related Hub: [[Hubs/RAG]]

> Core Node: [[START_HERE]]
