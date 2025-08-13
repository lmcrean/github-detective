issue title: [Feature]: Feedback for shopify app build & shopify app deploy --no-build
labels: Type: Enhancement, Area: @shopify/app
comment count: 1
hyperlink: https://github.com/shopify/cli/issues/6195
status: open
date opened: 2025-07-31
repo 30d_merge_rate: 77

====

description:
### What area(s) will this request affect?

App

### What type of change do you want to see?

Substantial change to existing feature

### Overview

Hey there,

After the --no-build flag was introduced (#5943), I started experimenting with my CI setup, building extensions with `shopify app build` and deploying them using `shopify app deploy --no-build`.

Overall, I’m loving it! I have a couple of suggestions though:

1. The `shopify app build` command relies on the config file, but it only uses `extension_directories` from it. Could we pass directories as an argument instead of needing a config file? The goal is to build once and switch between environments without relying on the config. For now, we’ve got a workaround using a `shopify.app.build.toml` file, like this:

```toml
# This file is required by Shopify CLI to run the `shopify app build` command
# ---
# The actual configuration is deployed during `shopify app deploy --no-build` command from either:
# - shopify.app.staging.toml 
# - shopify.app.production.toml

client_id = ""
extension_directories = ["packages/extensions/*"]
application_url = "https://.com"
embedded = true

[webhooks]
api_version = ""

[auth]
redirect_urls = []
```

2. The `shopify app build` command doesn’t seem to validate extension TOML files. It’s fine for now, but it’d be nicer if issues like that were caught early.

Thanks!

### Motivation

Improving app CI/CD

===

comment #1 by amcaplan, 2025-08-05, 08:09:22
RE 1, I think this is the right solution. We need the app TOML file as a marker of the app root. Otherwise, there really isn't anything obvious in your filesystem that indicates where your app root is. We don't assume you're currently in the root directory; you can be anywhere inside your app. That only works because we search recursively upwards until we find an app TOML. So I don't think this is likely to change, but having a TOML for the build case sounds like a great solution for your case!

RE 2, there's a bit of tension, because the schema for extension TOML files is stored on Shopify's systems, but we want the `build` command not to connect to the backend, and the CLI itself isn't really supposed to know too much about individual extensions (this keeps it maximally flexible/future-proof). So we are thinking about ways to improve this, but there are questions about what way of doing things will be best for UX.
