---
type: technology
status: active
linked_hubs:
  - [[Hubs/Model_Context_Protocol]]
---

## Definition
- Open protocol that standardizes how applications expose tools, resources, and prompts to LLM hosts using JSON-RPC plus defined transports (stdio, SSE, streamable HTTP).

## Capabilities
- Describes discoverable primitives with metadata so hosts can list and call them without bespoke integrations.
- Supports multiple transports with consistent message shapes, enabling both local and remote connectivity.
- Enables sampling flows where servers request LM completions through clients with optional human approval.

## Integration Patterns
- Use streamable HTTP as the default transport for new deployments; keep stdio for local dev and legacy SSE only when required. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Architecture_Transport_Server_Deployment]]
- Expose resource templates for dynamic URIs (e.g., customer logs) so clients stay lightweight while servers validate IDs. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Architecture_Transport_Server_Deployment]]
- Package prompts on the server with parameter interpolation to standardize downstream agent behavior. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Architecture_Transport_Server_Deployment]]

## Source Transcripts
- [[Resources/Processed_Transcripts/MCP_Course_Architecture_Transport_Server_Deployment]]

## Related Concepts
- [[Resources/Concepts/Tool_Calling_Failure_Modes]]
- [[Resources/Concepts/Tool_Schema_Design_For_Agent_Tools]]

## Linked Hubs
- [[Hubs/Model_Context_Protocol]]

> Core Node: [[Projects/AI_Native_Engineer]]
