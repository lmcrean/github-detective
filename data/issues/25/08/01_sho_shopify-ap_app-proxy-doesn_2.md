issue title: App proxy doesn't work with multiple query parameters
labels: none
comment count: 0
hyperlink: https://github.com/shopify/shopify-app-js/issues/2692
status: open
date opened: 2025-08-01
repo 30d_merge_rate: 10

====

description:
# Issue summary

Before opening this issue, I have:

- [x] Upgraded to the latest version of the relevant packages
  - `@shopify/*` package and version:
  - Node version:
  - Operating system:
- [x] Set `{ logger: { level: LogSeverity.Debug } }` in my configuration, when applicable
- [x] Found a reliable way to reproduce the problem that indicates it's a problem with the package
- [x] Looked for similar issues in this repository
- [x] Checked that this isn't an issue with a Shopify API
  - If it is, please create a post in the [Shopify community forums](https://community.shopify.com/c/partners-and-developers/ct-p/appdev) or report it to [Shopify Partner Support](https://help.shopify.com/en/support/partners/org-select)

When authenticating an app proxy request, hmac validation fails if a query parameter is repeated.

## Expected behavior

HMAC signature validation should still pass

## Actual behavior

It fails

## Steps to reproduce the problem

1. Create an app proxy route
1. Call it with a repeated query param ie `a=1&a=2`
1. It will fail with an auth error


===
