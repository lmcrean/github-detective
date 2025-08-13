issue title: Add observability platform integrations (Datadog, CloudWatch, OpenTelemetry)
labels: brainstorm, epic/cost-observability
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/161
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Summary
Integrate Roast with popular observability platforms to enable monitoring and alerting for AI workflows in production environments.

## Acceptance Criteria
- [ ] Integration with Datadog for metrics and logs
- [ ] Integration with AWS CloudWatch for cloud-native deployments
- [ ] OpenTelemetry hooks for all workflow steps
- [ ] Configurable exporters for different platforms
- [ ] Documentation for setting up integrations

## Technical Details
- Implement OpenTelemetry SDK integration as the foundation
- Create platform-specific exporters (Datadog, CloudWatch)
- Add tracing spans for workflow and step execution
- Include custom attributes for AI-specific metrics (tokens, cost, model)

**Labels:** brainstorm, epic/cost-observability
**Epic:** Cost Management & Observability

===
