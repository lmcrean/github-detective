issue title: Add Slack integration for input steps
labels: enhancement, epic/integrations
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/237
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Summary
Extend the input step type to support collecting user input via Slack messages with interactive buttons and forms.

## Requirements
- Send Slack messages with interactive components (buttons, select menus, text inputs)
- Wait for user response via Slack webhooks
- Support timeout handling with reminders
- Map Slack user responses back to workflow state

## Example Usage
```yaml
steps:
  - input:
      name: approval
      prompt: "Approve deployment to production?"
      type: boolean
      channel: slack
      slack:
        channel: "#deployments"
        mention: "@oncall"
        reminder_after: 300  # 5 minutes
```

## Technical Approach
- Use Slack Block Kit for rich message formatting
- Implement webhook receiver for Slack interactions
- Store pending requests with correlation IDs
- Handle multiple concurrent workflows

## Related Issues
- #102: User input step (CLI implementation)
- #172: Event-driven workflow triggers

## Milestone
Suggested: v0.8 (Infrastructure & Scale)

===
