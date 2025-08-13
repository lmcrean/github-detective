issue title: Rework `DocumentLinks` to use `@shopify/theme-graph`
labels: enhancement, good first issue, tech debt, area:language-server
comment count: 0
hyperlink: https://github.com/shopify/theme-tools/issues/968
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 11

====

description:
**Is your feature request related to a problem? Please describe.**

[Shopify/theme-graph](https://github.com/Shopify/theme-tools/pull/956) allowed each file to be able to tell if it has a reference or dependency to another file.

Instead of explicitly looking through Liquid Tags and checking to see if it's a variable or liquid string, we can just underline all references in liquid files using theme-graph's reference.

File in question: https://github.com/Shopify/theme-tools/blob/main/packages/theme-language-server-common/src/documentLinks/DocumentLinksProvider.ts#L37-L50

- [ ] Refactor provider to include theme-graph
- [ ] Introduce document linking from Liquid schemas to blocks/sections it's referencing
- [ ] Introduce document linking from web components to the javascript file it's referencing

**Describe the solution you'd like**
- Ideally we can keep this file extremely minimal and only check the theme-graph for references and where it's located in the file
- Introduces schema level document linking (which currently doesn't exist)


===
