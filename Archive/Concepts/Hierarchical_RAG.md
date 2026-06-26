---
type: concept
stability: stable
reviewed: 2026-06
hub: RAG
---

## Why It Matters
- Layered chunk relationships let agents search precisely while still pulling larger context when needed, improving grounding without ballooning tokens.

## Playbook Moves
- **Store parent-child metadata** — Track which fine-grained chunks belong to each document so retrieval can pivot to broader context. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^hierarchical]]
- **Search small, return big** — Run semantic search on small chunks, then fetch the full document or larger sections for grounding. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^hierarchical]]
- **Combine with agentic routing** — Let agents decide when to escalate from chunk to document reads based on question intent. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^agentic-routing]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^hierarchical]]
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^agentic-routing]]

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/Neon_Postgres]]
- [[Tools/PGVector]]
- [[Tools/Dockling]]

## Related Concepts
- [[Concepts/Agentic_RAG]]
- [[Concepts/Context_Aware_Chunking]]
- [[Concepts/RAG_Re_Ranking]]

> Related Hub: [[Hubs/RAG]]

> Core Node: [[START_HERE]]
