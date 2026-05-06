---
type: concept
status: active
hub: RAG
persona: Professional Seeking AI Mastery
---

## Why It Matters
- Knowledge graphs add relationship-aware retrieval so agents can answer questions that depend on entity connections instead of pure similarity.

## Playbook Moves
- **Extract entities and edges with LLMs** — Use an LLM to build graph nodes/relationships from documents, accepting higher ingest cost. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^kg-balance]]
- **Blend graph and vector search** — Run graph traversals alongside PGVector queries to cover relational and semantic matches. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^kg-balance]]
- **Reserve for relationship-heavy domains** — Apply graph builds when relationships drive answers to justify slower, pricier ingest. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^kg-balance]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^kg-balance]]

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/Graffiti_LLM_Graphs]]
- [[Tools/PGVector]]

## Related Concepts
- [[Concepts/RAG_Re_Ranking]]
- [[Concepts/Hierarchical_RAG]]
- [[Concepts/Contextual_Retrieval]]

> Related Hub: [[Hubs/RAG]]

> Core Node: [[START_HERE]]
