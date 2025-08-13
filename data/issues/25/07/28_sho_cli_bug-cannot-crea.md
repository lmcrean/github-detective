issue title: [Bug]: Cannot create unscoped, app-specific webhooks with legacy install flow
labels: Area: @shopify/app
comment count: 0
hyperlink: https://github.com/shopify/cli/issues/6171
status: open
date opened: 2025-07-28
repo 30d_merge_rate: 77

====

description:
Prior to [validation for app-specific webhooks](https://github.com/Shopify/cli/pull/6003), it was possible to create webhook subscriptions for app-specific webhooks that did not require scopes, even when `use_legacy_install_flow = true`. 

As a (non-exhaustive) example, the following `shopify.app.toml` used to work without error:

```toml
[access_scopes]
scopes = "read_content,write_content,read_customers,write_customers"
use_legacy_install_flow = true

[build]
include_config_on_deploy = true

[auth]
redirect_urls = [
  "https://app.example.com/auth/shopify/offline/callback",
  "https://app.example.com/auth/shopify/online/callback",
]

[webhooks]
api_version = "2025-01"

[[webhooks.subscriptions]]
topics = ["app/uninstalled"]
uri = "https://example.com/shopify/uninstall"

[[webhooks.subscriptions]]
uri = "https://example.com/shopify/webhooks/customer_account_settings/update"
topics = ["customer_account_settings/update"]
```

But as of the latest CLI, it will fail with "App-specific webhook subscriptions are not supported when use_legacy_install_flow is enabled"

I believe this is a regression because webhooks such as `app/uninstalled` and `customer_account_settings/update` do not require additional scopes, and therefore should still be configurable via the CLI even when `use_legacy_install_flow = true`.

This _also_ impacted compliance webhooks, but those have been fixed separately as of the PR [Fix: Allow compliance webhooks with legacy install flow](https://github.com/Shopify/cli/pull/6108)

We have patched out the "app-specific validation" check in our local version of CLI and deploys of those webhooks have been working without issue.


===
