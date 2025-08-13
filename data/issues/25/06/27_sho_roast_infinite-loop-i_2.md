issue title: Infinite loop if project root is not under home
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/300
status: open
date opened: 2025-06-27
repo 30d_merge_rate: 13

====

description:
Hey all, I'm currently working in a devcontainer, where my project is under `/workspaces/` and my user's home is under `/home/` 

This means this while loop iterates forever on lookup of initializers:

https://github.com/Shopify/roast/blob/272a5eddd4d717106e6d2b977098c3f8370854ea/lib/roast/initializers.rb#L9C11-L12C11

===
