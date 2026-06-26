---
type: concept
stability: stable
reviewed: 2026-06
hub: AI_Agents
evidence_status: has_receipts
---

## Why It Matters
- Agent systems need task-level and step-level benchmarks to prevent silent regressions across planning, tool use, and recovery.

## Sub-Concept Map
- Task success and completion quality
- Step accuracy and tool-call correctness
- Latency and cost envelopes
- Regression gating in CI/CD

## Playbook Moves
- Maintain a fixed benchmark suite for every release.
- Score both end-task success and intermediate decision quality.
- Block rollout when reliability, latency, or cost budgets regress.
- **Construct golden datasets from SME-consensus labels; use disagreement cases to refine rubrics** — disagreements are not noise to discard but signals that reveal edge cases the scoring contract doesn't yet cover. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^golden-dataset-construction]]
- **Gate deployments on eval score thresholds derived from golden dataset baselines** — select metrics that match the failure mode you're detecting; misaligned metrics hide real problems. *Receipt:* [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^eval-metric-selection]]

## Source Receipts
- [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^golden-dataset-construction]]
- [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^eval-metric-selection]]

## Connected Projects
- [[START_HERE]]

## Related Concepts
- [[Concepts/Agent_Observability_And_Evaluation]]
- [[Concepts/Tool_Calling_Failure_Modes]]
- [[Concepts/Agent_Benchmark_Suites]]
- [[Concepts/Eval_Engineering_Lifecycle]]

> Related Hub: [[Hubs/AI_Agents]]
> Core Node: [[START_HERE]]
