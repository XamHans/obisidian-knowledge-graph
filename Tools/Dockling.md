---
type: technology
status: active
linked_hubs:
  - [[Hubs/RAG]]
---

## Definition
- Python library for hybrid/context-aware chunking that preserves document structure by detecting natural boundaries.

## Capabilities
- Splits documents using embedding-based boundaries to keep semantics intact while producing bite-sized chunks. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^context-chunking]]
- Supports context-aware chunking strategies that improve embedding fidelity without heavy compute. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^context-chunking]]
- Helps maintain downstream recall so rerankers and LLMs receive coherent slices. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]

## Integration Patterns
- Use during ingest to avoid fixed-size splits; store resulting chunks with parent-child metadata for hierarchical retrieval. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^hierarchical]]
- Pair with LLM-written prefaces (contextual retrieval) when additional summaries are needed. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^contextual-chunk]]
- Benchmark chunk boundary quality vs naive fixed-length splits to justify the extra step. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^context-chunking]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^context-chunking]]
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^contextual-chunk]]
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^hierarchical]]

## Related Concepts
- [[Concepts/Context_Aware_Chunking]]
- [[Concepts/Contextual_Retrieval]]
- [[Concepts/Hierarchical_RAG]]

## Linked Hubs
- [[Hubs/RAG]]
