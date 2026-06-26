---
type: tool
stability: volatile
as_of: 2026-06
reviewed: 2026-06
linked_hubs:
  - [[Hubs/Model_Context_Protocol]]
---

## Definition
- Python framework for building MCP servers with decorators for tools, resources (including templates), and prompts, plus transport configuration helpers.

## Capabilities
- Simplifies server definitions via `@mcp.tool`, `@mcp.resource`, and `@mcp.prompt` decorators.
- Supports streamable HTTP transport configuration and host/port binding required for remote deployments.
- Provides logging and inspector compatibility for validating discovery endpoints.

## Integration Patterns
- Use resource templates to serve per-customer data without rewriting server code; validate IDs before file access. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Architecture_Transport_Server_Deployment]]
- Configure `transport="streamable_http"`, `host="0.0.0.0"`, and port alignment with Docker/Cloud Run to keep endpoints reachable. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Architecture_Transport_Server_Deployment]]
- Attach detailed tool/resource descriptions to improve model selection inside hosts like Claude Desktop. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Architecture_Transport_Server_Deployment]]

## Source Transcripts
- [[Resources/Processed_Transcripts/MCP_Course_Architecture_Transport_Server_Deployment]]

## Related Concepts
- [[Concepts/Tool_Schema_Design_For_Agent_Tools]]
- [[Concepts/Tool_Calling_Guardrails_And_Recovery]]

## Linked Hubs
- [[Hubs/Model_Context_Protocol]]

> Core Node: [[START_HERE]]
