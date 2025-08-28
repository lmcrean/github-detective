metadata {
link: https://github.com/Sage/carbon/issues/6266
labels: Bug, On Backlog, stale
data opened: 2023-08-21T15:34:18Z
author: phil9690
hyperlink: https://github.com/Sage/carbon/issues/6266
issue title: FlatTable has both rounded and square corners
}

issue description:
### Current behaviour

In some cases the FlatTable component has both rounded corners and square corners overlapping each other. This also appears on some tables when zooming in 200%, then zooming out again.

### Expected behaviour

The FlatTable component should only have rounded corners, or square corners, but not both. Zooming in and out of the page should not affect the border radius.

### CodeSandbox or Storybook URL

n/a

### JIRA Ticket (Sage Only)

SBS-65909
SBS-65907

### Suggested Solution

_No response_

### Carbon Version

119.3.1

### Design Tokens Version

_No response_

### What browsers are you seeing the problem on?

Chrome, Safari

### What Operating System are you seeing the problem on?

MacOS, Windows

### Anything else we should know?

This issue may be present in browsers other than Chrome and Safari, but hasn't been checked.

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **edleeks87** (2023-08-21T15:47:37Z):
  I'll discuss this with @harpalsingh and @ljemmo next week as we may need to have a re-think on how tables with rounded corners work given the complexity/ configurability of the component

- **edleeks87** (2023-08-22T13:04:45Z):
  FE-6185

- **stale[bot]** (2025-04-26T14:40:19Z):
  This issue has been automatically marked as stale because it has not had recent activity. If you believe this issue is still valid and required please comment below. It will be reviewed by the core Carbon team and may be closed if no further activity occurs. Thank you for your contributions.



