issue title: Add real-time cost tracking and budget management
labels: brainstorm, epic/cost-observability
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/159
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Summary
Implement real-time cost tracking capabilities to monitor and control AI workflow costs during execution.

## Acceptance Criteria
- [ ] Real-time cost estimation during YAML parsing based on configured models and expected token usage
- [ ] Live cost increment tracking during workflow execution
- [ ] Configurable budget ceiling with automatic abort when reached
- [ ] Cost breakdowns per step showing token usage and associated costs
- [ ] Cost summary report at workflow completion

## Technical Details
- Parse workflow YAML to estimate costs based on model pricing
- Track actual token usage during each step execution
- Implement budget checks before each step execution
- Store cost data in workflow context for reporting

**Labels:** brainstorm, epic/cost-observability
**Epic:** Cost Management & Observability

===
