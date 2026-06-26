---
type: concept
stability: stable
reviewed: 2026-06
hub: Generative_AI
evidence_status: has_receipts
evidence_backlog:
  - BentoML LLM Inference Handbook — How LLM Inference Works
---

## Why It Matters
- The KV cache is the mechanism that makes autoregressive generation practical — it avoids recomputing attention for every previously seen token. Understanding prefill vs decode phases is the prerequisite for every inference optimization decision, from hardware sizing to batching strategy.

## Sub-Concept Map
- **Prefill phase**: processes the full prompt in parallel, computes query/key/value vectors at every transformer layer, and populates the KV cache. This phase is compute-bound; the key metric is Time to First Token (TTFT).
- **Decode phase**: generates tokens one at a time autoregressively, reading from the growing KV cache to avoid redundant computation. This phase is memory-bound due to repeated cache reads.
- KV cache stores key and value tensors at every layer for all processed tokens — memory footprint scales linearly with sequence length and model depth.
- **Paged attention** manages cache memory in fixed-size blocks to reduce fragmentation and waste.
- **KV cache offloading** moves cache data to CPU memory or remote storage when GPU VRAM is exhausted.
- Cache eviction strategies determine which sequences to drop under memory pressure.
- Prefill-decode disaggregation assigns each phase to specialized hardware pools for optimal resource utilization.

## Playbook Moves
- Size GPU VRAM against model parameters plus KV cache at maximum concurrent sequence count.
- Monitor TTFT separately from token generation throughput — they respond to different bottlenecks.
- Use prefill-decode disaggregation for latency-sensitive workloads with long prompts.
- Implement paged attention (vLLM, SGLang) to serve more concurrent sequences within fixed memory.

## Source Transcripts
- BentoML LLM Inference Handbook — How LLM Inference Works (2025).

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/BentoML]]

## Related Concepts
- [[Concepts/Context_Window_And_Attention_Budget]]
- [[Concepts/Transformer_Architecture]]
- [[Concepts/Inference_Optimization_Latency_Cost]]
- [[Concepts/Distributed_LLM_Inference]]
- [[Concepts/Decoding_Strategies_And_Sampling]]
- [[Concepts/LLM_Inference_Lifecycle]]

> Related Hub: [[Hubs/Generative_AI]]
> Core Node: [[START_HERE]]
