issue title: Timeout leaves zombie processes
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/324
status: open
date opened: 2025-07-14
repo 30d_merge_rate: 13

====

description:
The way we're currently timing out is by asking for a TERM and then [falling back to a KILL on the executed process](https://github.com/Shopify/roast/blob/50eaa6407f8bd44b4231f0cb55581869050d7f31/lib/roast/helpers/timeout_handler.rb#L77C34-L77C37).

This doesn't work, as we're relying on the process we're killing to clean up all of its children. Instead we could spawn new process in a pgroup, and kill the whole group.

I've done something similar in the past: https://github.com/shop/world/pull/22857 

===
