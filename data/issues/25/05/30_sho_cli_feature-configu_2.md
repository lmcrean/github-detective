issue title: [Feature]: Configurable hot-reload delay for full page reload
labels: Type: Enhancement, Area: @shopify/theme
comment count: 3
hyperlink: https://github.com/shopify/cli/issues/5913
status: open
date opened: 2025-05-30
repo 30d_merge_rate: 77

====

description:
### What area(s) will this request affect?

Theme

### What type of change do you want to see?

New feature

### Overview

Add in a flag that allows for a delay before a full-page reload occurs like `--live-reload-delay 1s`.

### Motivation

I much prefer to run the CLI using full-page live reload (`--live-reload full-page`) due to working with more JS heavy development but often I find a second or even third refresh is needed to finally show the changes.

Having a 'delay' before the hot reload kicks in may help to solve this.

===

comment #1 by nbskubix, 2025-07-04, 11:53:49
@gonzaloriestra is there any response on this?

comment #2 by omri-luz, 2025-08-03, 10:35:36
im interested as well, my files do not get updated properly and there is inconsistencies in both hmr and full reload

comment #3 by nbskubix, 2025-08-12, 10:52:38
@gonzaloriestra / @karreiro 

Is there any chance we can have some eyes on this please? It's also affecting the hot reload within the customizer too as I need a further refresh to then see new customizer options.
