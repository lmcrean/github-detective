issue title: Exponential backoff for failures
labels: brainstorm, epic/reliability
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/224
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Description
Implement exponential backoff retry strategies for handling transient failures.

## Acceptance Criteria
- [ ] Configurable backoff strategies
- [ ] Maximum retry limits
- [ ] Jitter implementation
- [ ] Per-step retry configuration

Epic: epic/reliability

## Context
Exponential backoff would improve reliability when dealing with rate-limited or temporarily unavailable services.

===
