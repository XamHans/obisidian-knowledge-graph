---
type: concept
status: active
hub: Generative_AI
persona: Professional Seeking AI Mastery
evidence_status: has_receipts
evidence_backlog:
  - BentoML LLM Inference Handbook — CPU vs GPU vs TPU
---

## Why It Matters
- Hardware choice determines the cost floor, latency ceiling, and scaling model for every inference workload. Picking the wrong accelerator wastes budget; picking the wrong deployment topology creates compliance or latency problems.

## Sub-Concept Map
- **CPU inference**: general-purpose, low-cost, widely available. Suitable for small quantized models or infrequent requests. Lacks parallelism for production-grade LLM throughput.
- **GPU inference**: dominant choice for LLMs. Architecture optimized for matrix multiplication and tensor operations. VRAM capacity is the primary constraint (model weights + KV cache). Ecosystem: CUDA, ROCm, PyTorch, vLLM, SGLang, TensorRT-LLM.
- **TPU inference**: Google-designed ASICs for tensor operations. Very high parallelism and memory bandwidth. Best for large-scale training and high-batch inference within the Google/JAX/XLA ecosystem.
- **Memory bandwidth** is the primary bottleneck for autoregressive LLM inference (decode phase reads KV cache repeatedly).
- **Deployment topologies**:
  - Cloud single-provider — on-demand GPU/TPU access with managed services.
  - Multi-cloud / cross-region — distributes workloads for latency reduction and cost optimization.
  - BYOC (Bring Your Own Cloud) — vendor software in your cloud account with managed orchestration.
  - On-premises — full control over data and compliance; significant operational overhead.
  - Edge — runs on user devices or local nodes for reduced latency and enhanced privacy.

## Playbook Moves
- Match hardware to workload: CPU for small models / low traffic, GPU for production LLMs, TPU for Google-native high-batch scenarios.
- Size VRAM against model parameters plus KV cache at target concurrency before selecting GPU tier.
- Evaluate deployment topology against data residency requirements, latency SLAs, and team ops capacity.
- Monitor memory bandwidth utilization — it reveals whether you are compute-bound (prefill) or memory-bound (decode).

## Source Transcripts
- BentoML LLM Inference Handbook — CPU vs GPU vs TPU (2025).

## Connected Projects
- [[Projects/AI_Native_Engineer]]

## Related Concepts
- [[Resources/Concepts/Inference_Optimization_Latency_Cost]]
- [[Resources/Concepts/LLM_Training_Vs_Inference]]
- [[Resources/Concepts/Distributed_LLM_Inference]]
- [[Resources/Concepts/Serverless_Vs_Self_Hosted_Inference]]
- [[Resources/Concepts/KV_Cache_And_Prefill_Decode_Phases]]
- [[Resources/Concepts/LLM_Inference_Lifecycle]]

> Related Hub: [[Resources/Hubs/Generative_AI]]
> Core Node: [[Projects/AI_Native_Engineer]]
