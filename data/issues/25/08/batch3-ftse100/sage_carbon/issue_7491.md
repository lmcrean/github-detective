metadata {
link: https://github.com/Sage/carbon/issues/7491
labels: Bug, On Backlog
data opened: 2025-08-18T15:29:02Z
author: amieedwards-sage
hyperlink: https://github.com/Sage/carbon/issues/7491
issue title: Responsive Vertical Menu - Scroll bar indicator cut off bottom of page
}

issue description:
### Description

Vertical scroll indicator is cut off the bottom of the page.
It does have the potential to give the user the impression that there are more menu items hidden off the page.

### Reproduction

https://stackblitz.com/edit/parsium-carbon-starter-e7cskdsu?file=README.md

### Steps to reproduce

1. Reduce screen size to view the menu in one single column (via the Responsive view)
2. When viewing a list of items which expand past the viewport height
3. The bottom of the scroll indicator appears to be cut off - at the top of the menu it is rounded, which is missing from the bottom of the menu.


### JIRA ticket numbers (Sage only)

SBS-142006

### Suggested solution

_No response_

### Carbon version

155.7.0

### React version

v17

### Design tokens version

4.34.0

### Relevant browsers

Chrome

### Relevant OSs

MacOS

### Additional context

_No response_

### Confidentiality

- [x] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **tomdavies73** (2025-08-19T13:25:07Z):
  FE-7452


