---
type: concept
stability: stable
reviewed: 2026-06
hub: Generative_AI
evidence_status: has_receipts
evidence_backlog:
  - Add transcript or paper receipts for this concept.
  - BentoML LLM Inference Handbook — How LLM Inference Works (2025).
---

## Why It Matters
- Decoding Strategies And Sampling is a core concept for reliable Generative AI systems and should be formalized before deep implementation work.

## Sub-Concept Map
- **Greedy decoding**: always selects the highest-probability token — deterministic but repetitive.
- **Temperature**: reshapes the probability distribution before sampling; lower values sharpen (more deterministic), higher values flatten (more creative).
- **Top-k sampling**: restricts selection to the k most probable tokens, then samples from that subset.
- **Top-p (nucleus) sampling**: restricts selection to the smallest set of tokens whose cumulative probability exceeds threshold p.
- **Combined top-k + top-p**: applies both filters for finer control over output diversity.
- **Beam search**: maintains multiple candidate sequences in parallel, selecting the highest-scoring complete sequence.
- **Speculative decoding**: uses a smaller draft model to propose multiple tokens, which the main model verifies in parallel — reduces latency without changing output quality.
- **Autoregressive decode phase** is the latency bottleneck: each token depends on all previous tokens, making generation inherently sequential.
- **Stopping conditions**: maximum token length, stop words, or end-of-sequence token.

## Playbook Moves
- Design explicit behavior contracts for Decoding Strategies And Sampling before prompt tuning.
- Add validation and guardrails around outputs and tool actions.
- Measure quality, latency, and cost together on fixed eval sets.

## Source Receipts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[START_HERE]]

## Related Concepts
- [[Concepts/Prompt_Engineering_Patterns]]
- [[Concepts/Transformer_Architecture]]
- [[Concepts/Inference_Optimization_Latency_Cost]]
- [[Concepts/KV_Cache_And_Prefill_Decode_Phases]]
- [[Concepts/LLM_Inference_Lifecycle]]

> Related Hub: [[Hubs/Generative_AI]]
> Core Node: [[START_HERE]]
