---
type: technology
status: active
linked_hubs:
  - "[[Resources/Hubs/Generative_AI]]"
---

## Definition
- Open-source platform for building, shipping, and scaling AI inference services; provides model packaging, adaptive batching, and multi-framework support for production LLM deployments.

## Capabilities
- Model packaging as Bentos with versioned dependency isolation for reproducible deployments.
- Adaptive batching that dynamically groups incoming requests to maximize GPU utilization.
- Multi-framework support: PyTorch, TensorFlow, ONNX, JAX, and Hugging Face models.
- Distributed inference orchestration across multiple GPUs and nodes.
- BentoCloud managed platform for serverless-style deployment with autoscaling.
- OpenAI-compatible API endpoints for drop-in integration with existing toolchains.

## Integration Patterns
- Package models with `bentoml.models` and define serving logic in a `Service` class for consistent deployment artifacts.
- Configure adaptive batching parameters (max batch size, wait timeout) per endpoint to balance latency and throughput.
- Deploy to BentoCloud for managed scaling or export containers for self-hosted Kubernetes clusters.
- Combine with vLLM or SGLang runtimes for high-performance LLM inference behind BentoML's serving layer.

## Source Transcripts
- BentoML LLM Inference Handbook (2025) — comprehensive guide covering inference basics, optimization, and deployment patterns.

## Related Concepts
- [[Resources/Concepts/Inference_Optimization_Latency_Cost]]
- [[Resources/Concepts/Serverless_Vs_Self_Hosted_Inference]]
- [[Resources/Concepts/Distributed_LLM_Inference]]
- [[Resources/Concepts/LLM_Inference_Lifecycle]]

## Linked Hubs
- [[Resources/Hubs/Generative_AI]]

> Core Node: [[Projects/AI_Native_Engineer]]
