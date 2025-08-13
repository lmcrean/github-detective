issue title: Step execution middleware system
labels: brainstorm, epic/developer-experience
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/157
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Epic: Developer Experience Core

### Summary
Implement a middleware system using Ruby blocks that wrap step execution, enabling cross-cutting concerns like metrics, tracing, and policy injection.

### Acceptance Criteria
- [ ] Ruby blocks that wrap any step execution
- [ ] Enable metrics, tracing, and policy injection
- [ ] Similar to Rails controller filters (before/after/around)
- [ ] Support both global and per-step middleware

### Implementation Notes
- Should allow composition of multiple middleware
- Consider performance impact of wrapper chains
- Enable easy integration with observability tools
- Support both synchronous and asynchronous middleware
- Provide hooks for common use cases (timing, logging, auth)

===
