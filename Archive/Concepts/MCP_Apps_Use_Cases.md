---
type: concept
stability: stable
reviewed: 2026-06
evidence_status: needs_receipts
linked_hubs:
  - [[Hubs/ChatGPT_Apps]]
  - [[Hubs/Model_Context_Protocol]]
---

## Definition
MCP apps use cases are product patterns where an LLM host needs both model-directed tools and an interactive interface. They are most useful when text alone is too weak for inspection, editing, comparison, or repeated workflow execution.

## Common Use Cases
- Data explorers that let users filter, inspect, and act on records.
- Workflow consoles where the model plans but the user confirms critical actions.
- Learning tools that combine generated guidance with persistent visual state.
- Internal operational tools that wrap existing APIs in an LLM-native interface.

## Engineering Notes
- Use apps when the UI state matters across turns.
- Keep sensitive writes behind explicit confirmation.
- Prefer small, composable tools over one broad tool with ambiguous behavior.

## Related
- [[Tools/MCP_Apps]]
- [[Tools/OpenAI_Apps_SDK]]
- [[Concepts/Human_In_The_Loop_Agent_Controls]]
- [[Concepts/Agent_Permissioning_And_Trust_Boundaries]]
- [[Concepts/Tool_Calling_Guardrails_And_Recovery]]

> Related Hub: [[Hubs/ChatGPT_Apps]]
> Core Node: [[START_HERE]]
