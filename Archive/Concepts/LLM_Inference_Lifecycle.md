---
type: concept
stability: stable
reviewed: 2026-06
hub: Generative_AI
evidence_status: has_receipts
evidence_backlog:
  - BentoML LLM Inference Handbook — What is LLM Inference, How LLM Inference Works
---

## Why It Matters
- Understanding the end-to-end inference lifecycle — from raw text input to generated response — is the prerequisite for making any optimization, hardware, or deployment decision. Every downstream choice maps back to a specific phase in this pipeline.

## Sub-Concept Map
- **Tokenization**: converts input text into token IDs that the model processes. A token can be a word, subword, or character depending on the tokenizer vocabulary.
- **Prefill phase**: processes the full prompt in parallel through transformer layers, building the KV cache. Compute-bound; metric is Time to First Token (TTFT).
- **Decode phase**: generates output tokens one at a time autoregressively, sampling from probability distributions shaped by temperature, top-k, and top-p. Memory-bound due to KV cache reads.
- **Detokenization**: converts generated token IDs back into human-readable text.
- **Inference servers**: the operational hub managing the lifecycle — loads models, coordinates GPU access, handles request batching, streaming, dynamic scaling, and performance monitoring. Examples: vLLM, SGLang, TensorRT-LLM, Hugging Face TGI, BentoML.
- **Key metrics**: Time to First Token (TTFT), tokens per second (TPS), end-to-end latency, throughput (requests/second).
- **Stopping conditions**: maximum token length, stop words, or end-of-sequence token.
- **Diffusion LLMs (dLLMs)**: emerging non-autoregressive alternative that outputs the entire response in parallel through a denoising process. Examples: Mercury (Inception AI), Gemini Diffusion (Google DeepMind). Not yet supported by mainstream frameworks.

## Playbook Moves
- Map each lifecycle phase to its latency and cost contribution before optimizing — profile where time is actually spent.
- Instrument per-phase metrics (TTFT, TPS, queue time) as separate observability signals.
- Evaluate inference server features (batching mode, streaming support, quantization compatibility) against your workload requirements before selecting a runtime.
- Watch diffusion LLMs as an emerging paradigm shift — they may fundamentally change the latency profile of generation.

## Source Transcripts
- BentoML LLM Inference Handbook — What is LLM Inference (2025).
- BentoML LLM Inference Handbook — How LLM Inference Works (2025).

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/BentoML]]

## Related Concepts
- [[Concepts/KV_Cache_And_Prefill_Decode_Phases]]
- [[Concepts/Decoding_Strategies_And_Sampling]]
- [[Concepts/Inference_Optimization_Latency_Cost]]
- [[Concepts/Transformer_Architecture]]
- [[Concepts/LLM_Training_Vs_Inference]]
- [[Concepts/AI_Inference_Hardware]]
- [[Concepts/Distributed_LLM_Inference]]
- [[Concepts/Serverless_Vs_Self_Hosted_Inference]]

> Related Hub: [[Hubs/Generative_AI]]
> Core Node: [[START_HERE]]
