issue title: Dead letter queue for failed steps
labels: brainstorm, epic/reliability
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/226
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Description
Implement dead letter queue functionality for handling permanently failed steps.

## Acceptance Criteria
- [ ] Failed step capture and storage
- [ ] Retry mechanisms from DLQ
- [ ] Inspection and analysis tools
- [ ] Alerting integration

Epic: epic/reliability

## Context
Dead letter queues would allow failed steps to be analyzed and retried without blocking workflows.

===
