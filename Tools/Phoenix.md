---
type: software
status: active
category: llm_eval
linked_hubs:
  - [[Hubs/LLM_Evals]]
---

## Definition
- Arize Phoenix: evaluation/observability platform for LLM apps that manages labeled datasets, runs judge prompts with explanations, visualizes confusion matrices, and compares prompt/model versions.

## Capabilities
- Upload CSVs, stratify dev/test splits, and track ground truth vs judge outputs with explanations.
- Compute accuracy/precision/recall/F1 and confusion matrices to diagnose harsh vs lenient judges.
- Run experiments across prompt versions (manual or LLM-optimized) and compare on held-out tests.
- Support stochastic judge reruns to surface ambiguous examples with high response variance.

## Integration Patterns
- Start `phoenix serve`, load a labeled eval dataset (>=100 examples), and set dev/test splits before tuning judges. *Source:* [[Resources/Processed_Transcripts/LLM_Judge_Meta_Evaluation_Phoenix#^dataset-representative]]
- Use confusion matrices to rebalance harsh/lenient judge behavior, guided by explanations. *Source:* [[Resources/Processed_Transcripts/LLM_Judge_Meta_Evaluation_Phoenix#^overly-harsh-lenient]]
- Iterate prompts on the dev split, then validate best versions on held-out tests; try the built-in prompt optimizer loop for additional lift. *Source:* [[Resources/Processed_Transcripts/LLM_Judge_Meta_Evaluation_Phoenix#^prompt-iterate-results]]

## Source Transcripts
- [[Resources/Processed_Transcripts/LLM_Judge_Meta_Evaluation_Phoenix#^dataset-representative]]
- [[Resources/Processed_Transcripts/LLM_Judge_Meta_Evaluation_Phoenix#^overly-harsh-lenient]]
- [[Resources/Processed_Transcripts/LLM_Judge_Meta_Evaluation_Phoenix#^prompt-iterate-results]]

## Related Concepts
- [[Resources/Concepts/LLM_Judge_Meta_Evaluation]]
- [[Resources/Concepts/LLM_As_Judge_Evaluation]]
- [[Resources/Concepts/Eval_Engineering_Lifecycle]]

## Linked Hubs
- [[Hubs/LLM_Evals]]

> Core Node: [[Projects/AI_Native_Engineer]]
