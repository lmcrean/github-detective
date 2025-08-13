issue title: [Feature]: The ability to develop a theme locally and preview it for a specific market
labels: Severity: 3, Type: Enhancement, Area: @shopify/theme
comment count: 0
hyperlink: https://github.com/shopify/cli/issues/6074
status: open
date opened: 2025-07-07
repo 30d_merge_rate: 77

====

description:
### What area(s) will this request affect?

Theme

### What type of change do you want to see?

Substantial change to existing feature

### Overview

I am essentially attempting to run a command like:

$ shopify theme dev --store uk.mystore.com --theme 177002348907

but ofcourse this doesn't work. The intention is to preview a specific geo-targeted Market like our UK store or EU store, as opposed to our US store/default.

the -h flag does not provide any useful information on how to do this, and copying the ?preview_market= url param from the browser doesn't work. My current understanding is that it isn't possible. If the only way to develop a theme for new markets is to create a fake store or push your changes to your live site, that's not really good. 

### Motivation

A note for anyone looking for this: the current way to achieve this is to push your changes to the remote/Shopify theme (ideally not a live one), and then go to Preview theme, and then change the URL in the address bar or use the dropdown in the sticky footer bar to select the Market you wish to preview. This is slower than developing locally though.

===
