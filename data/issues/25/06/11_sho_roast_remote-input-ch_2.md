issue title: Remote input channel orchestration
labels: enhancement, epic/infrastructure
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/241
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Summary
Create the orchestration layer that manages remote input channels (Slack, email, web) for the input step type.

## Requirements
This issue focuses on the shared infrastructure needed by all remote input channels:

### Core Orchestration
- Webhook receiver service for callbacks
- Request/response correlation system
- Channel routing based on configuration
- Unified timeout and retry handling

### State Management
- Persistent storage for pending inputs
- Session recovery after restarts
- Multi-channel fallback support
- Audit logging for compliance

### Channel Abstraction
```yaml
steps:
  - input:
      name: approval
      prompt: "Approve this action?"
      type: boolean
      channels:
        - slack:
            channel: "#approvals"
            timeout: 600
        - email:
            to: "backup-approver@example.com"
            timeout: 3600
        - cli:
            timeout: 300
      fallback_order: [slack, email, cli]
```

### Security & Reliability
- Channel-specific authentication
- Rate limiting per channel
- Circuit breakers for external services
- Encrypted state storage

## Technical Design
- Channel adapter pattern
- Message queue for reliability
- Webhook signature verification
- Distributed lock management

## Related Issues
- #237: Slack integration for input steps
- #238: Email integration for input steps
- #239: Web UI for input steps
- Depends on #102 (basic CLI input)

## Milestone
Suggested: v0.8 (Infrastructure & Scale)

===
