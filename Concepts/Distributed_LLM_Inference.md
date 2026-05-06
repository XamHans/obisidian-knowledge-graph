---
type: concept
status: active
hub: Generative_AI
persona: Professional Seeking AI Mastery
evidence_status: has_receipts
evidence_backlog:
  - BentoML LLM Inference Handbook — Distributed Inference
---

## Why It Matters
- Models that exceed single-device memory require distributed strategies. Choosing the wrong parallelism approach wastes hardware budget and adds latency instead of reducing it.

## Sub-Concept Map
- **Macro-level distribution**: running model replicas across multiple geographic regions, heterogeneous GPU clusters, or multiple cloud providers for reliability and latency optimization.
- **Micro-level distribution**: splitting a single inference request across devices to overcome memory or compute limits.
- **Tensor parallelism**: splits individual layers across multiple GPUs — required when a single layer's weights exceed one device's VRAM.
- **Pipeline parallelism**: assigns groups of consecutive layers to different devices — useful for very deep models with moderate per-layer size.
- **Data parallelism**: replicates the full model on multiple devices and splits incoming batches across them — scales throughput when the model fits on one device.
- **Prefill-decode disaggregation**: routes compute-heavy prefill to one hardware pool and memory-heavy decode to another, optimizing utilization of each.
- **KV cache offloading**: moves cache tensors to CPU memory or remote storage when GPU VRAM is exhausted, trading latency for capacity.
- **Prefix-aware routing**: directs requests to workers that already hold relevant cached prefixes, reducing redundant computation.
- **Implementation stack**: specialized runtimes (vLLM, SGLang, llm-d) on Kubernetes with orchestration layers for autoscaling, health checks, and observability.

## Playbook Moves
- Use tensor parallelism when a model exceeds single-GPU VRAM; prefer data parallelism for throughput scaling when the model fits on one device.
- Evaluate prefill-decode disaggregation for latency-critical applications with long prompts.
- Implement prefix-aware routing when workloads share common system prompts or few-shot examples.
- Monitor inter-device communication overhead — it caps the scaling efficiency of tensor and pipeline parallelism.

## Source Transcripts
- BentoML LLM Inference Handbook — Distributed Inference (2025).

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/BentoML]]

## Related Concepts
- [[Concepts/KV_Cache_And_Prefill_Decode_Phases]]
- [[Concepts/AI_Inference_Hardware]]
- [[Concepts/Inference_Optimization_Latency_Cost]]
- [[Concepts/Transformer_Architecture]]
- [[Concepts/LLM_Inference_Lifecycle]]

> Related Hub: [[Hubs/Generative_AI]]
> Core Node: [[START_HERE]]
