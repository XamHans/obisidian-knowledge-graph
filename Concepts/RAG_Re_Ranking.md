---
type: concept
status: active
hub: RAG
persona: Professional Seeking AI Mastery
---

## Why It Matters
- Two-stage retrieval widens recall then trims to the most relevant chunks so agents avoid blowing the context window while still seeing enough evidence.

## Playbook Moves
- **Pull wide then filter tight** — Retrieve many candidates from PGVector and compress to top-N with a cross-encoder so the LLM only sees the best few chunks. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]
- **Tune candidate width vs budget** — Adjust how many chunks you fetch before reranking to balance recall and token spend per query. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]
- **Make reranking the default layer** — Start every RAG build with reranking as part of the recommended trio to stabilize answer quality. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^starter-stack]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^starter-stack]]

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/PGVector]]
- [[Tools/Neon_Postgres]]

## Related Concepts
- [[Concepts/Multi_Query_RAG]]
- [[Concepts/Agentic_RAG]]
- [[Concepts/Context_Aware_Chunking]]

> Related Hub: [[Hubs/RAG]]

> Core Node: [[START_HERE]]
