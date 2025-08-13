issue title: Circuit breaker pattern for external services
labels: brainstorm, epic/reliability
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/225
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Description
Implement circuit breaker pattern to prevent cascading failures from external services.

## Acceptance Criteria
- [ ] Circuit state management (closed/open/half-open)
- [ ] Failure threshold configuration
- [ ] Recovery timeout settings
- [ ] Fallback mechanism support

Epic: epic/reliability

## Context
Circuit breakers would protect workflows from repeated failures when external services are down.

===
