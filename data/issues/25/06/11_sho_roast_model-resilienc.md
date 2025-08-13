issue title: Model resilience and fallback configuration
labels: brainstorm, epic/developer-experience
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/155
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Epic: Developer Experience Core

### Summary
Enhance Roast's resilience by supporting timeouts, fallback models, and automatic retries to handle quota limits and model failures gracefully.

### Acceptance Criteria
- [ ] Add timeout field to step configuration
- [ ] Support fallback_model configuration for graceful degradation
- [ ] Auto-retry with cheaper models when quotas exceeded
- [ ] Maintain execution continuity despite model failures

### Implementation Notes
- Timeout should be configurable per-step and globally
- Fallback chain should be configurable (e.g., gpt-4 → gpt-3.5-turbo → claude-instant)
- Should track and report which model was ultimately used
- Consider exponential backoff for retries

===
