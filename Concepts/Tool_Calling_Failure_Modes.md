---
type: concept
status: active
hub: Agent_Tool_Calling
persona: Professional Seeking AI Mastery
---

## Why It Matters
- Tool calling fails silently in production more often than model generation does; without a failure taxonomy you ship brittle agents that look smart but behave unpredictably.

## Playbook Moves
- **Separate selection vs execution errors** - Track wrong-tool choices separately from wrong-parameter/runtime errors so fixes target either prompting/policy or schema/runtime.
- **Build a top-10 failure taxonomy** - Start with: wrong tool, wrong params, missing required params, stale state assumptions, duplicate side effects, timeout/retry storms, hallucinated tool names, partial tool outputs, auth failures, and unsafe action escalation.
- **Log failed call context aggressively** - Capture user message, model reasoning summary, tool candidates, selected tool, payload, validation errors, and downstream side effects in one trace.
- **Turn repeat failures into guardrails** - Any failure seen 3+ times becomes either schema tightening, policy routing rule, or runtime validation gate.

## Source Transcripts
- [[Resources/Processed_Transcripts/MCP_Course_Architecture_Transport_Server_Deployment]]

## Connected Projects
- [[Projects/AI_Native_Engineer]]

## Linked Technologies
- [[Resources/Technologies/Model_Context_Protocol]]
- [[Technologies/FastMCP]]
- [[Technologies/OpenAI_Apps_SDK]]

## Related Concepts
- [[Resources/Concepts/Tool_Schema_Design_For_Agent_Tools]]
- [[Resources/Concepts/Tool_Calling_Guardrails_And_Recovery]]
- [[Resources/Concepts/Self_Reflective_RAG]]
- [[Resources/Concepts/Tool_Use_And_Action_Policies]]
- [[Resources/Concepts/Agent_Observability_And_Evaluation]]

> Related Hub: [[Hubs/Agent_Tool_Calling]]
> Core Node: [[Projects/AI_Native_Engineer]]
