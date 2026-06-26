---
type: tool
stability: stable
as_of: 2026-06
reviewed: 2026-06
linked_hubs:
  - [[Hubs/Model_Context_Protocol]]
---

## Definition
- Containerization platform for packaging MCP servers and dependencies into portable images that run consistently across local machines and Cloud Run.

## Capabilities
- Builds platform-specific images (e.g., `--platform linux/amd64`) for deployment targets.
- Tags and pushes images to Artifact Registry or other registries for distribution.
- Exposes ports to match server bindings, enabling MCP transports over HTTP.

## Integration Patterns
- Build and tag MCP server images before pushing to Artifact Registry; keep tags aligned with Cloud Run deploy commands. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Technova_Server_Deployment#^deploy-host]]
- Use consistent port exposure (8080) between Dockerfile, server config, and Cloud Run to avoid connection errors. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Technova_Server_Deployment#^deploy-host]]
- Pair Docker builds with Makefile targets to streamline rebuild/push/deploy cycles for MCP updates. *Source:* [[Resources/Processed_Transcripts/MCP_Course_Technova_Server_Deployment#^deploy-host]]

## Source Transcripts
- [[Resources/Processed_Transcripts/MCP_Course_Technova_Server_Deployment#^deploy-host]]

## Related Concepts
- [[Concepts/MCP_Production_Workflows]]

## Linked Hubs
- [[Hubs/Model_Context_Protocol]]
