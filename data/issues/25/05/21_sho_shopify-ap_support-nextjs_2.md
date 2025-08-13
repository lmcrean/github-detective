issue title: Support Next.js caching options in the GraphQL client
labels: Stale
comment count: 1
hyperlink: https://github.com/shopify/shopify-app-js/issues/2489
status: open
date opened: 2025-05-21
repo 30d_merge_rate: 10

====

description:
## Overview

Dear Shopify dev team,

I would like to propose an enhancement to the Shopify GraphQL client that enables it to support the caching and revalidation options provided by the `fetch` function in Next.js.

### Background

Currently, the Shopify GraphQL client allows injecting a custom `fetch` function, which is great. However, when using this in a Next.js environment, we cannot leverage Next.js-specific options such as `cache`, `next.revalidate`, or `next.tags`, because the client does not forward these options to the underlying `fetch` call.

### Proposal

I suggest extending the `request` method of the client to support passing fetch options directly, so that Next.js can properly handle caching and ISR (Incremental Static Regeneration). For example:

```TypeScript
const { data, errors } = await storefrontApiClient.request(getProductByHandleQuery, {
  variables: { language, country, handle },
  cache: 'force-cache',
  next: { revalidate: false, tags: ['product'] },
});
```

These additional options would be passed through to the custom fetch implementation provided to the client.

### Status

I have already implemented the necessary changes, including tests, and validated the functionality in a real Next.js application. If the team sees value in this feature, I would be happy to follow up with a pull request.

Thanks for your consideration!

Best regards,
Void

===

comment #1 by github-actions[bot], 2025-07-22, 02:16:46
We're labeling this issue as stale because there hasn't been any activity on it for 60 days. While the issue will stay open and we hope to resolve it, this helps us prioritize community requests.

You can add a comment to remove the label if it's still relevant, and we can re-evaluate it.
