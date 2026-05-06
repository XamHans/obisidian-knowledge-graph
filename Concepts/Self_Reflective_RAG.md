---
type: concept
status: active
hub: RAG
persona: Professional Seeking AI Mastery
---

## Why It Matters
- Introducing a grading loop on retrieved chunks catches low-quality results and retries automatically, improving answer reliability.

## Playbook Moves
- **Grade retrieval outputs** — Ask an LLM to score chunk relevance (e.g., 1–5) before responding. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^self-reflect]]
- **Retry on low scores** — Trigger refined searches when the grade falls below a threshold to self-correct. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^self-reflect]]
- **Control cost with thresholds** — Set conservative retry rules to avoid runaway LLM calls while improving precision. *Receipt:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^self-reflect]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^self-reflect]]

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/PGVector]]
- [[Tools/Neon_Postgres]]

## Related Concepts
- [[Concepts/Query_Expansion_RAG]]
- [[Concepts/Multi_Query_RAG]]
- [[Concepts/RAG_Re_Ranking]]
- [[Concepts/Planning_And_Reasoning_Strategies]]
- [[Concepts/Agent_Observability_And_Evaluation]]

> Related Hub: [[Hubs/RAG]]
> Core Node: [[START_HERE]]
