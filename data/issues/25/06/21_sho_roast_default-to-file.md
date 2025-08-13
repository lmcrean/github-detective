issue title: Default to filestorage instead of sqlite ?
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/296
status: open
date opened: 2025-06-21
repo 30d_merge_rate: 13

====

description:
I think we need to default to filestorage not sqlite and relax roast dependency to `sqlite3`. IMO, since it's a CLI, logging to files seems more natural than a DB. What do you think ?

===
