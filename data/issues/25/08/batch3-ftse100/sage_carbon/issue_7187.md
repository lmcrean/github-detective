metadata {
link: https://github.com/Sage/carbon/issues/7187
labels: Bug, On Backlog, Squad Delta
data opened: 2025-01-30T10:14:43Z
author: LPTSage
hyperlink: https://github.com/Sage/carbon/issues/7187
issue title: Draggable FlatTable error in DevTools > Console: 'Failed prop type: Invalid prop `rowRef` supplied...'
}

issue description:
### Description

There is an error logged in DevTools Console when rendering Draggable FlatTable; namely
'Failed prop type: Invalid prop `rowRef` supplied to `FlatTableRowDraggable`, expected one of type [function].'


### Reproduction

https://stackblitz.com/edit/parsium-carbon-starter-iekazx6v?file=src%2FApp.tsx,package.json,src%2FApp.spec.tsx

### Steps to reproduce

GIVEN I render a Draggable FlatTable
WHEN I open DevTools > Console
THEN I see an error 'Failed prop type: Invalid prop `rowRef` supplied to `FlatTableRowDraggable`, expected one of type [function].'

### JIRA ticket numbers (Sage only)

_No response_

### Suggested solution

_No response_

### Carbon version

142.13.5

### Design tokens version

_No response_

### Relevant browsers

Chrome, Microsoft Edge

### Relevant OSs

Windows, Linux

### Additional context

I can reproduce in stackblitz using the latest _carbon v147.0.0

### Confidentiality

- [x] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **Parsium** (2025-02-04T14:21:06Z):
  FE-7069


