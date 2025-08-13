issue title: Add email integration for input steps
labels: enhancement, epic/integrations
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/238
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Summary
Extend the input step type to support collecting user input via secure email links.

## Requirements
- Send email notifications with secure input links
- Generate time-limited, single-use tokens for security
- Host lightweight web form for input collection
- Support all input types (text, boolean, choice, multiline)

## Example Usage
```yaml
steps:
  - input:
      name: approval
      prompt: "Please review and approve the deployment"
      type: boolean
      channel: email
      email:
        to: "approver@example.com"
        subject: "Deployment Approval Required"
        expires_in: 3600  # 1 hour
```

## Technical Approach
- Generate secure tokens with expiration
- Minimal web server for form hosting
- Email templates with branding support
- Webhook callback to resume workflow

## Security Considerations
- HTTPS only for input forms
- Token rotation and single-use enforcement
- Rate limiting on form submissions
- Optional authentication integration

## Related Issues
- #102: User input step (CLI implementation)
- #237: Slack integration for input steps

## Milestone
Suggested: v0.8 (Infrastructure & Scale)

===
