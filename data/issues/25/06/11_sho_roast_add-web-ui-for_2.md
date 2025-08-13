issue title: Add web UI for input steps
labels: enhancement, epic/ui-visualization
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/239
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Summary
Create a web-based interface for collecting user input during workflow execution, integrated with the future Roast UI.

## Requirements
- Web forms auto-generated from input step configuration
- Real-time updates via WebSocket
- Mobile-responsive design
- Integration with workflow visualization UI

## Example Usage
```yaml
steps:
  - input:
      name: bug_report
      prompt: "Submit bug report"
      type: multiline
      channel: web
      web:
        theme: light
        logo_url: "https://example.com/logo.png"
        return_url: "https://example.com/thank-you"
```

## Features
- Rich input components (file upload, date picker, etc.)
- Form validation with real-time feedback
- Progress indicators for multi-step inputs
- Accessibility compliance (WCAG 2.1)

## Technical Approach
- React/Vue component library
- REST API for form submission
- WebSocket for real-time updates
- JWT for session management

## Related Issues
- #102: User input step (CLI implementation)
- #167: Visual Workflow Builder
- #169: Workflow sharing features

## Milestone
Suggested: v0.9 (Advanced capabilities)

===
