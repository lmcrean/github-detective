metadata {
link: https://github.com/Sage/carbon/issues/7469
labels: Bug, On Backlog
data opened: 2025-07-30T14:28:41Z
author: Chris3y
hyperlink: https://github.com/Sage/carbon/issues/7469
issue title: Message doesn't appear to be focusable as docs (storybook) suggest
}

issue description:
### Description

I noticed that focusing doesn't appear to work on Message.

Looking at the source, it looks like the component accepts a ref and then passes it to the Message.style styled component but that does nothing with the ref?

Would expect the ref was passed to icon button so user can dismiss the message easily, if we decide to focus it on open.

### Reproduction

https://carbon.sage.com/iframe.html?viewMode=docs&id=message--docs&globals=#with-focus

### Steps to reproduce

Storybook

### JIRA ticket numbers (Sage only)

_No response_

### Suggested solution

_No response_

### Carbon version

153.1

### React version

v18

### Design tokens version

_No response_

### Relevant browsers

Chrome

### Relevant OSs

Windows

### Additional context

_No response_

### Confidentiality

- [x] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **nineteen88** (2025-08-06T09:06:55Z):
  FE-7435


