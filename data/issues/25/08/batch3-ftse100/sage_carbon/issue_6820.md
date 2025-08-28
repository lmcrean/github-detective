metadata {
link: https://github.com/Sage/carbon/issues/6820
labels: Bug, On Backlog, stale, Squad Nebula
data opened: 2024-07-08T09:57:46Z
author: szeyingyau
hyperlink: https://github.com/Sage/carbon/issues/6820
issue title: Menu stays expanded when menu options are selected while screen reader is enabled
}

issue description:
### Description

When I enable a screen reader software and select a menu item from a Menu, the expanded menu stays open even though a new page is loaded. I expect the menu to close when a menu item is selected.

### Reproduction

https://carbon.sage.com/?path=/story/menu--default-story

### Steps to reproduce

### VoiceOver for MacOS

1. Enable VoiceOver
2. Navigate to menu
3. Select and expand menu 
4. Navigate to any menu item 
5. Select menu item - Ctrl + Opt + Spacebar

### NVDA for Windows

1. Enable NVDA
2. Navigate to menu
3. Select and expand menu
4. Navigate to any menu item 
5. Select menu item - 'Enter' key

### JIRA ticket numbers (Sage only)

SBS-102689

### Suggested solution

_No response_

### Carbon version

135.1.0

### Design tokens version

4.34.0

### Relevant browsers

Chrome, Safari

### Relevant OSs

MacOS, Windows

### Additional context

Using 'Tab' and 'Enter' keys when screen reader isn't enabled closes the menu as expected when a menu item is selected

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **sianford** (2024-07-09T13:22:22Z):
  FE-6688 logged to investigate each screen reader behaviour in macOS (VoiceOver with Safari) and Windows (NVDA with Chrome, Firefox and Edge).

- **stale[bot]** (2025-07-19T05:06:48Z):
  This issue has been automatically marked as stale because it has not had recent activity. If you believe this issue is still valid and required please comment below. It will be reviewed by the core Carbon team and may be closed if no further activity occurs. Thank you for your contributions.



