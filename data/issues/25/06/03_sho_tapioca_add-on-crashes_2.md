issue title: Add-on crashes if `sorbet/rbi/gems` doesn't exist
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/tapioca/issues/2308
status: open
date opened: 2025-06-03
repo 30d_merge_rate: 12

====

description:
The [gem RBI check](https://github.com/Shopify/tapioca/blob/main/lib/ruby_lsp/tapioca/run_gem_rbi_check.rb) always assumes that the directory will be present, but that's not guaranteed - especially if someone is just setting up their repo with Tapioca.

If the directory is not there, loading the Tapioca add-on crashes.

===
