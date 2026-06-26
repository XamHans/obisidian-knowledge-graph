---
type: concept
stability: evolving
reviewed: 2026-06
hub: RAG
---

## Why It Matters
- Letting agents choose retrieval modes (chunk-level semantic search vs whole-document reads) unlocks flexibility for varied questions while keeping storage unified.

## Playbook Moves
- **Expose multiple search tools** — Provide semantic chunk search and full-document read paths so the agent can route per query. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^agentic-routing]]
- **Store chunk + document tables** — Keep separate tables with shared IDs to let agents jump between fine-grained and coarse-grained context. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^agentic-routing]]
- **Add guardrails for predictability** — Define clear policies for when agents should switch retrieval modes to offset routing unpredictability. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^agentic-routing]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^agentic-routing]]

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/Neon_Postgres]]
- [[Tools/PGVector]]

## Related Concepts
- [[Concepts/Hierarchical_RAG]]
- [[Concepts/RAG_Re_Ranking]]
- [[Concepts/Multi_Query_RAG]]
- [[Concepts/Agent_Architecture_Patterns]]
- [[Concepts/Tool_Use_And_Action_Policies]]

> Related Hub: [[Hubs/RAG]]
> Core Node: [[START_HERE]]
