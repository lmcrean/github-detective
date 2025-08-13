issue title: Theme check to notify when files are orphaned
labels: enhancement, good first issue, area:theme-check
comment count: 0
hyperlink: https://github.com/shopify/theme-tools/issues/969
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 11

====

description:
**Is your feature request related to a problem? Please describe.**
[Shopify/theme-graph](https://github.com/Shopify/theme-tools/pull/956) allowed each file to be able to tell if it has a reference or dependency to another file.

It would be nice to tell if a file was unused or not by looking at the file structure in VSCode

**Describe the solution you'd like**
- An error appears on the file level saying the file isn't used
- `shopify theme check` would return a info/warning/error message if the file is orphaned


===
