issue title: Human-in-the-loop manual review steps
labels: brainstorm, epic/developer-experience
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/156
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Epic: Developer Experience Core

### Summary
Implement manual review steps that pause workflow execution for human input, supporting approval workflows via various communication channels.

### Acceptance Criteria
- [ ] Create step :review, kind: :manual primitive
- [ ] Support Slack/email callbacks for approval workflows
- [ ] Pause execution until human input received
- [ ] Provide clear status and context for reviewers

### Implementation Notes
- Should support multiple notification channels
- Consider webhook-based implementation for flexibility
- Need to persist workflow state during pause
- Support both approval/rejection and free-form input
- Consider timeout handling for unresponsive reviewers

===
