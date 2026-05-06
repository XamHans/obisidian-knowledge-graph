---
type: concept
status: active
hub: Generative_AI
persona: Professional Seeking AI Mastery
evidence_status: needs_receipts
evidence_backlog:
  - Add transcript or paper receipts for this concept.
---

## Why It Matters
- Model routing aligns workload complexity, latency, and cost by sending each task to the right model path.

## Sub-Concept Map
- Task classification for routing
- Fallback trees and degrade modes
- Cost-aware quality targets
- Provider and model heterogeneity
- Serverless vs self-hosted as a routing dimension — route to managed APIs for burst traffic, self-hosted for baseline load.
- Hardware-aware routing — direct requests to appropriate GPU tiers or cloud regions based on model requirements and latency SLAs.

## Playbook Moves
- Route simple requests to low-cost models and escalate only when needed.
- Define deterministic fallback behavior for outages and limits.
- Track quality and spend by route to tune policy over time.

## Source Receipts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[START_HERE]]

## Related Concepts
- [[Concepts/Inference_Optimization_Latency_Cost]]
- [[Concepts/Tool_Calling_Strategy_Design]]
- [[Concepts/Agent_Evaluation_And_Benchmarking]]
- [[Concepts/Serverless_Vs_Self_Hosted_Inference]]
- [[Concepts/AI_Inference_Hardware]]

> Related Hub: [[Hubs/Generative_AI]]
> Core Node: [[START_HERE]]
