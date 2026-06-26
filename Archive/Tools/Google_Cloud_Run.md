---
type: tool
stability: evolving
as_of: 2026-06
reviewed: 2026-06
linked_hubs:
  - [[Hubs/Model_Context_Protocol]]
---

## Definition
- Google’s managed container runtime that serves HTTP endpoints from OCI images with autoscaling and built-in TLS; suitable for exposing MCP servers publicly.

## Capabilities
- Deploys tagged Docker images from Artifact Registry with configurable memory, port, and auth settings.
- Provides logs, metrics, and health checks for MCP server endpoints.
- Supports unauthenticated access when MCP servers must serve multiple clients without credentials.

## Integration Patterns
- Build Linux/amd64 images locally, tag with Artifact Registry path, push, then `gcloud run deploy` with matching port (e.g., 8080) and `--allow-unauthenticated`. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Technova_Server_Deployment#^deploy-host]]
- Ensure server binds `0.0.0.0` and expose the same port in Dockerfile/Cloud Run to avoid connection failures. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Technova_Server_Deployment#^deploy-host]]
- Append `/mcp/` (or configured transport endpoint) in client configs when using streamable HTTP to the Cloud Run URL. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Technova_Server_Deployment#^deploy-host]]

## Source Transcripts
- [[Resources/Processed_Transcripts/MCP_Course_Technova_Server_Deployment#^deploy-host]]

## Related Concepts
- [[Concepts/MCP_Production_Workflows]]

## Linked Hubs
- [[Hubs/Model_Context_Protocol]]
