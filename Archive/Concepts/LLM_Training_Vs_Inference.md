---
type: concept
stability: stable
reviewed: 2026-06
hub: Generative_AI
evidence_status: has_receipts
evidence_backlog:
  - BentoML LLM Inference Handbook — Training vs Inference Differences
---

## Why It Matters
- Training is a one-time capital investment that teaches a model to recognize patterns; inference is the ongoing operational cost that runs every time a user sends a request. Confusing the two leads to misallocated budgets and wrong hardware choices.

## Sub-Concept Map
- **Purpose**: training adjusts model weights to learn patterns; inference applies frozen weights to generate predictions on new inputs.
- **Data flow**: training consumes massive curated datasets in batches; inference processes individual user requests in real time.
- **Cost model**: training is CapEx (GPU-hours once); inference is OpEx (per-token, scales with traffic). Inference often exceeds training cost long-term.
- **Duration**: training runs hours to weeks; inference responds in milliseconds to seconds.
- **Hardware profile**: training favors multi-node GPU/TPU clusters with high interconnect bandwidth; inference favors optimized runtimes with caching and batching.
- **Optimization levers differ**: training optimizes data quality, architecture, and learning rate schedules; inference optimizes quantization, KV caching, batching, and model routing.
- **Key training techniques**: supervised learning, reinforcement learning, self-supervised learning (next-token prediction).

## Playbook Moves
- Budget training as CapEx and inference as OpEx — track cost-per-token as the primary inference efficiency metric.
- Choose hardware based on workload profile: training clusters need high interconnect; inference nodes need large VRAM and fast memory bandwidth.
- Evaluate fine-tuning vs prompt engineering tradeoffs as a training-inference cost boundary decision.

## Source Transcripts
- BentoML LLM Inference Handbook — Training vs Inference Differences (2025).

## Connected Projects
- [[START_HERE]]

## Related Concepts
- [[Concepts/Inference_Optimization_Latency_Cost]]
- [[Concepts/AI_Inference_Hardware]]
- [[Concepts/Fine_Tuning_Adaptation_Strategies]]
- [[Concepts/Transformer_Architecture]]
- [[Concepts/LLM_Inference_Lifecycle]]

> Related Hub: [[Hubs/Generative_AI]]
> Core Node: [[START_HERE]]
