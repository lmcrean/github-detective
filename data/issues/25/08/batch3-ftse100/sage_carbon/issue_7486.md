metadata {
link: https://github.com/Sage/carbon/issues/7486
labels: Bug, On Backlog, Squad Megabat
data opened: 2025-08-14T14:06:00Z
author: kohli-pratik-sage
hyperlink: https://github.com/Sage/carbon/issues/7486
issue title: Form height not applied due to child <div>
}

issue description:
### Description

The Form component provides a `height` prop allowing the consumer to set the height for the form. However, the direct child `<div>` element with the data-role "form-content" has no styles applied to it and so its height is set based on the content within itself which makes the height set to the Form component redundant.

The height set to Form should be respected and the content should take up the available space.

### Reproduction

https://stackblitz.com/edit/parsium-carbon-starter-moagdatx?file=src%2FApp.tsx

### Steps to reproduce

_No response_

### JIRA ticket numbers (Sage only)

_No response_

### Suggested solution

_No response_

### Carbon version

153.0.0

### React version

v18, v17

### Design tokens version

4.35.0

### Relevant browsers

Microsoft Edge

### Relevant OSs

MacOS

### Additional context

_No response_

### Confidentiality

- [x] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **tomdavies73** (2025-08-19T13:05:48Z):
  FE-7450


