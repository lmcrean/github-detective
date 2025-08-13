issue title: .shopify/metafields.json is showing up everywhere
labels: none
comment count: 1
hyperlink: https://github.com/shopify/theme-tools/issues/1005
status: open
date opened: 2025-07-16
repo 30d_merge_rate: 11

====

description:
Same issue as the below:

[FabianGenell](https://community.shopify.dev/u/FabianGenell)
[Feb 24](https://community.shopify.dev/t/shopify-metafields-json-is-showing-up-everywhere/9275)
I have an issue where .shopify/metafields.json keeps appearing in completely unrelated projects and repos. If I run shopify theme dev or shopify theme pull while working on a theme, I get a metafields.json file, which is fine.

The problem is that later, when I switch to a React app or another unrelated project, .shopify/metafields.json randomly shows up. It’s extremely annoying, especially when I don’t notice and accidentally commit it to unrelated repos.


===

comment #1 by aswamy, 2025-07-24, 16:24:11
Hey @ben-lattimore, what version of CLI are you running.

This bug was patched - i assume you have an up-to-date VSCode extension + CLI version > 3.77.0?

