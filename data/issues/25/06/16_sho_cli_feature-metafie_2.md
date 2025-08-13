issue title: [Feature]: metafieldNamespaces (or metafields) doesn't seem to be supported in toml webhook subscriptions
labels: Type: Enhancement
comment count: 3
hyperlink: https://github.com/shopify/cli/issues/5987
status: open
date opened: 2025-06-16
repo 30d_merge_rate: 77

====

description:
### What area(s) will this request affect?

App

### What type of change do you want to see?

New feature

### Overview

Not sure why, but `metafieldNamespaces` and `metafields` props of webhook susbcriptions aren't available when setting up webhooks via the app toml.

Per this page, these options are missing: https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration#webhooks

They're available via graphql admin API:
https://shopify.dev/docs/api/admin-graphql/latest/input-objects/WebhookSubscriptionInput

Weirdly, the Remix template does support `metafieldNamespaces` for it's `registerWebhooks` function, but it doesn't support `filters` - so neither toml or `registerWebhooks` can be used to create a webhook subscription with a filter on metafields.

Any plans to support these options in toml webhook subscription definitions?

### Motivation

Need to create a webhook subscription that filters on a product metafield value in a public app. TOML is the easiest way to do this and I'd like to avoid manually creating these on install via graphql mutation (and then having to keep them up to date with manual jobs to update existing stores if things change).

===

comment #1 by gonzaloriestra, 2025-06-19, 11:26:59
Thanks for the suggestion! cc: @rebeccajfriedman 

comment #2 by github-actions[bot], 2025-08-01, 04:04:03
This issue seems inactive. If it's still relevant, please add a comment saying so. Otherwise, take no action.
→ If there's no activity within a week, then a bot will automatically close this.
Thanks for helping to improve Shopify's dev tooling and experience.

P.S. You can learn more about why we stale issues [here](https://github.com/Shopify/cli/blob/main/docs/decision-record/2023_02-Stale-action.md).

comment #3 by fabregas4, 2025-08-02, 04:37:49
Commenting to prevent closure
