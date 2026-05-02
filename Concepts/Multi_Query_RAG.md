---
type: concept
status: active
hub: RAG
persona: Professional Seeking AI Mastery
---

## Why It Matters
- Generating multiple query variants broadens coverage for ambiguous questions, reducing the chance of missing relevant chunks.

## Playbook Moves
- **Spawn parallel query variants** — Use an LLM to propose alternative phrasings and intents, then issue them concurrently. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^multi-query]]
- **Merge then rerank** — Collect results across all queries and rerank to surface the most relevant final set. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]
- **Budget DB and LLM costs** — Account for extra pre-search LLM calls and higher database fan-out when turning this on. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^multi-query]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^multi-query]]
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]

## Connected Projects
- [[Projects/AI_Native_Engineer]]

## Linked Technologies
- [[Technologies/PGVector]]
- [[Technologies/Neon_Postgres]]

## Related Concepts
- [[Resources/Concepts/RAG_Re_Ranking]]
- [[Resources/Concepts/Query_Expansion_RAG]]
- [[Resources/Concepts/Self_Reflective_RAG]]

> Related Hub: [[Hubs/RAG]]

> Core Node: [[Projects/AI_Native_Engineer]]
