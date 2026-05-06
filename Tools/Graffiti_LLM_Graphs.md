---
type: technology
status: active
linked_hubs:
  - [[Hubs/RAG]]
---

## Definition
- Library for building knowledge graphs from unstructured text by extracting entities and relationships with LLMs.

## Capabilities
- Constructs graph databases that complement vector search for relational queries. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^kg-balance]]
- Enables hybrid retrieval paths that traverse entity edges alongside similarity search. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^kg-balance]]
- Provides pseudo-code patterns for graph ingest within RAG pipelines. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^kg-balance]]

## Integration Patterns
- Run LLM extraction over documents to produce node/edge inserts, accepting higher ingest cost for richer relationship recall. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^kg-balance]]
- Blend graph traversal results with vector search candidates before reranking. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]
- Reserve for domains where entity relationships drive answers (people, systems, timelines). *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^kg-balance]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^kg-balance]]

## Related Concepts
- [[Concepts/Knowledge_Graph_RAG]]
- [[Concepts/RAG_Re_Ranking]]

## Linked Hubs
- [[Hubs/RAG]]
