metadata {
link: https://github.com/Sage/carbon/issues/6761
labels: Bug, On Backlog, stale
data opened: 2024-05-31T13:21:27Z
author: Sage-AlanYoung
hyperlink: https://github.com/Sage/carbon/issues/6761
issue title: Badge Component Styling Issues
}

issue description:
### Description

The Badge component looks to have fallen out of sync with the Design System, original message: 

I've been playing around with the Badge component used with an icon and have some questions around styling. It doesn't seem like we have much control over the size/positioning of the component, is there anything we can do to adjust it? I've included a StackBlitz example below that shows a couple of cases but neither look particularly good and would need some adjustment. The example also shows what appears to be an issue when rendering the badge within a menu item/popover container, with the same components rendering differently than those outside the menu. Finally, is there any way to change the background colour of the badge or will this always be white? Thanks!

https://stackblitz.com/edit/parsium-carbon-starter-g3wx3z?file=src%2FApp.tsx

### Reproduction

https://stackblitz.com/edit/parsium-carbon-starter-g3wx3z?file=src%2FApp.tsx

### Steps to reproduce

_No response_

### JIRA ticket numbers (Sage only)

_No response_

### Suggested solution

_No response_

### Carbon version

134.1.1

### Design tokens version

4.29.0

### Relevant browsers

Chrome

### Relevant OSs

Windows

### Additional context

_No response_

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **Parsium** (2024-06-04T13:12:19Z):
  FE-6651

- **Parsium** (2024-06-04T13:42:32Z):
  Hi @Sage-AlanYoung 👋🏼 Currently, we don't provide the ability to amend the sizing or position of `Badge`. Looking at the latest version of Design System, it seems Carbon's `Badge` has a few discrepancies with the DS, so we will need to review these and make the necessary changes.

- **stale[bot]** (2025-07-19T05:06:49Z):
  This issue has been automatically marked as stale because it has not had recent activity. If you believe this issue is still valid and required please comment below. It will be reviewed by the core Carbon team and may be closed if no further activity occurs. Thank you for your contributions.



