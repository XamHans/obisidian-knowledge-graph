---
type: concept
stability: stable
reviewed: 2026-06
hub: AI_Agents
evidence_status: has_receipts
---

## Why It Matters
- Without observability and evaluation, agent systems degrade silently and cannot be improved systematically.

## Sub-Concept Map
- Trace-level visibility across steps/tools.
- Task success metrics and failure taxonomies.
- Offline eval sets for regression detection.
- Online monitoring for drift and incident response.
- Experiment tracking for prompt/policy changes.

## Playbook Moves
- Define agent KPIs before shipping new workflows.
- Maintain fixed benchmark tasks for every release.
- Instrument traces and alerts for top failure classes.
- **Build failure taxonomies by category (planning, tool use, recovery) from trace-level inspection** — categorizing failures by type enables targeted improvements instead of shotgun prompt changes. *Receipt:* [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^failure-taxonomy-agentic]]
- **Use trace debugging to surface failure patterns invisible in aggregate metrics** — a single pass/fail on the final output hides whether the failure was retrieval or reasoning; traces reveal the exact step where the chain broke. *Receipt:* [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^trace-debug-failure-analysis]]
- **Monitor for criteria drift with periodic SME re-validation** — user behavior changes over time; rubrics that worked at launch stop catching new failure modes. *Receipt:* [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^criteria-drift]]

## Source Transcripts
- [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^trace-debug-failure-analysis]]
- [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^failure-taxonomy-agentic]]
- [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^criteria-drift]]

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/Phoenix]]
- [[Tools/FastMCP]]

## Related Concepts
- [[Concepts/Evaluation_Metrics_Classification_Regression]]
- [[Concepts/Planning_And_Reasoning_Strategies]]
- [[Concepts/Tool_Calling_Failure_Modes]]
- [[Concepts/LLM_Judge_Meta_Evaluation]]
- [[Concepts/Eval_Engineering_Lifecycle]]

> Related Hub: [[Hubs/AI_Agents]]
> Core Node: [[START_HERE]]
