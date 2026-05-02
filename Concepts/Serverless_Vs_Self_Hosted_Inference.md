---
type: concept
status: active
hub: Generative_AI
persona: Professional Seeking AI Mastery
evidence_status: has_receipts
evidence_backlog:
  - BentoML LLM Inference Handbook — Serverless vs Self-Hosted LLM Inference
---

## Why It Matters
- The deployment model choice locks in cost structure, data governance posture, and optimization ceiling for the life of the system. Switching later is expensive.

## Sub-Concept Map
- **Serverless inference**: managed API services (OpenAI, Anthropic, Together AI, Fireworks). Zero infrastructure, pay-per-token, minimal setup (API key + a few lines of code). Tradeoffs: limited customization, cold start risk, linear cost scaling, data leaves your network.
- **Self-hosted inference**: deploy on your own cloud GPUs, private networks, or on-premises servers. Full operational control over hardware, runtime, and data. Tradeoffs: requires ops expertise, higher upfront investment, but potentially lower per-token cost at scale.
- **Hybrid patterns**: use serverless for burst traffic and prototyping; self-host for baseline load where unit economics favor fixed infrastructure.
- **Data security and compliance**: self-hosting keeps sensitive data within secure perimeters — critical for regulated industries (legal, healthcare, finance).
- **Performance customization**: techniques like prefill-decode disaggregation, prefix caching, speculative decoding, and quantization are only available when you control the inference stack.
- **Cost crossover**: serverless is cheaper at low volume; self-hosted becomes cheaper when token volume makes per-call pricing uneconomical.
- **Competitive differentiation**: self-hosting enables fine-tuning with proprietary data and compound AI system architectures that API providers cannot replicate.

## Playbook Moves
- Start serverless for prototyping and low-traffic MVPs — validate the use case before investing in infrastructure.
- Track cost-per-token and project the crossover point where self-hosting becomes cheaper.
- Evaluate data residency and compliance requirements before choosing any serverless provider.
- When migrating to self-hosted, begin with a managed platform (BentoCloud, Replicate) before going fully custom on Kubernetes.

## Source Transcripts
- BentoML LLM Inference Handbook — Serverless vs Self-Hosted LLM Inference (2025).

## Connected Projects
- [[Projects/AI_Native_Engineer]]

## Linked Technologies
- [[Resources/Technologies/BentoML]]
- [[Technologies/Google_Cloud_Run]]

## Related Concepts
- [[Resources/Concepts/Inference_Optimization_Latency_Cost]]
- [[Resources/Concepts/AI_Inference_Hardware]]
- [[Resources/Concepts/Model_Routing_Strategies]]
- [[Resources/Concepts/LLM_Training_Vs_Inference]]
- [[Resources/Concepts/LLM_Inference_Lifecycle]]

> Related Hub: [[Resources/Hubs/Generative_AI]]
> Core Node: [[Projects/AI_Native_Engineer]]
