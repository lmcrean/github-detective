metadata {
link: https://github.com/Sage/carbon/issues/7066
labels: Bug, On Backlog
data opened: 2024-11-08T08:56:13Z
author: amieedwards-sage
hyperlink: https://github.com/Sage/carbon/issues/7066
issue title: Responsive Tile with FlexTileDivider - content shifts with NVDA and browse mode
}

issue description:
### Description

I am using the Responsive Tile component with `<FlexTileDivider />` between each cell.
When using Browse mode and navigating through the Tile using the arrow keys to read out each element within the component the content shifts left.
The layout is affected when the separators are read out.

https://carbon.sage.com/?path=/docs/tile--docs#responsive-tile

Chrome: 130.0
NVDA: Version 2024.4.0.34423

### Reproduction

https://stackblitz.com/edit/parsium-carbon-starter-4hbtpv?file=src%2FApp.tsx

### Steps to reproduce

Enable NVDA > change to browse mode.
Use arrow keys to navigate within the elements of the Tile.

### JIRA ticket numbers (Sage only)

SBS-114292

### Suggested solution

_No response_

### Carbon version

142.13.0

### Design tokens version

4.34.0

### Relevant browsers

Firefox, Chrome

### Relevant OSs

Windows

### Additional context

_No response_

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **nuria1110** (2024-11-12T14:14:09Z):
  FE-6899


