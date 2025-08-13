issue title: State persistence across restarts
labels: brainstorm, epic/reliability
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/230
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Description
Implement durable state persistence to survive process restarts.

## Acceptance Criteria
- [ ] Pluggable state storage backends
- [ ] Automatic state recovery
- [ ] State versioning
- [ ] Migration tools

Epic: epic/reliability

## Context
State persistence would ensure workflow progress isn't lost during system restarts or crashes.

===
