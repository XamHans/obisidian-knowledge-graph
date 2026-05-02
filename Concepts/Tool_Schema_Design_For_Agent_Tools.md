---
type: concept
status: active
hub: Agent_Tool_Calling
persona: Professional Seeking AI Mastery
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
- [[Projects/AI_Native_Engineer]]

## Linked Technologies
- [[Resources/Technologies/Model_Context_Protocol]]
- [[Technologies/FastMCP]]
- [[Technologies/OpenAI_Apps_SDK]]

## Related Concepts
- [[Resources/Concepts/Tool_Calling_Failure_Modes]]
- [[Resources/Concepts/Tool_Calling_Guardrails_And_Recovery]]
- [[Resources/Concepts/Agentic_RAG]]
- [[Resources/Concepts/Tool_Use_And_Action_Policies]]
- [[Resources/Concepts/Prompt_Engineering_Patterns]]

> Related Hub: [[Hubs/Agent_Tool_Calling]]
> Core Node: [[Projects/AI_Native_Engineer]]
