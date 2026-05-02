---
type: concept
status: active
hub: RAG
persona: Professional Seeking AI Mastery
---

## Why It Matters
- Expanding a single user query with LLM hints increases precision by steering search toward more specific chunks without changing the UI.

## Playbook Moves
- **LLM-enrich the query** — Insert domain-specific details before search to pull better-matched chunks. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^query-expand]]
- **Template the expansions** — Define instructions for how the LLM should add entities, timeframes, or constraints to avoid drift. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^query-expand]]
- **Measure latency hit** — Track added cost from the extra LLM call and gate expansion for fast-path queries. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^query-expand]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^query-expand]]

## Connected Projects
- [[Projects/AI_Native_Engineer]]

## Linked Technologies
- [[Technologies/PGVector]]
- [[Technologies/Neon_Postgres]]

## Related Concepts
- [[Resources/Concepts/Multi_Query_RAG]]
- [[Resources/Concepts/RAG_Re_Ranking]]
- [[Resources/Concepts/Self_Reflective_RAG]]

> Related Hub: [[Hubs/RAG]]

> Core Node: [[Projects/AI_Native_Engineer]]
