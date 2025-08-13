issue title: Implement metrics collection and export system
labels: brainstorm, epic/cost-observability
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/162
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Summary
Build a comprehensive metrics collection system that tracks key performance indicators for AI workflows with export capabilities.

## Acceptance Criteria
- [ ] Prometheus-style metrics export endpoint
- [ ] Token usage tracking per step and workflow
- [ ] Execution duration measurements at step and workflow level
- [ ] Cost metrics correlated with usage
- [ ] Custom metric definitions for workflow-specific KPIs

## Technical Details
- Implement metrics registry compatible with Prometheus format
- Track counters (tokens, requests), gauges (cost), histograms (duration)
- HTTP endpoint for metrics scraping
- Configurable metric labels and dimensions

**Labels:** brainstorm, epic/cost-observability
**Epic:** Cost Management & Observability

===
