---
type: concept
stability: stable
reviewed: 2026-06
hub: Agent_Tool_Calling
---

## Why It Matters
- Most wrong-parameter tool failures are schema and description design problems, not model IQ problems.

## Playbook Moves
- **Design for constrained decisions** - Prefer narrow enums and explicit object shapes over free-form strings for action selection fields.
- **Use operation-specific tools** - Split overloaded tools into single-purpose endpoints so the model has fewer ambiguous choices.
- **Embed decision boundaries in descriptions** - State when to call and when not to call a tool, including disallowed intents and required prerequisites.
- **Validate before execute** - Run schema + semantic checks (ID existence, range checks, state preconditions) before side-effecting operations.

## Source Transcripts
- [[Resources/Processed_Transcripts/MCP_Course_Architecture_Transport_Server_Deployment]]

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/Model_Context_Protocol]]
- [[Tools/FastMCP]]
- [[Tools/OpenAI_Apps_SDK]]

## Related Concepts
- [[Concepts/Tool_Calling_Failure_Modes]]
- [[Concepts/Tool_Calling_Guardrails_And_Recovery]]
- [[Concepts/Agentic_RAG]]
- [[Concepts/Tool_Use_And_Action_Policies]]
- [[Concepts/Prompt_Engineering_Patterns]]

> Related Hub: [[Hubs/Agent_Tool_Calling]]
> Core Node: [[START_HERE]]
