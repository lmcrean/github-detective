issue title: [Feature]: GraphiQL Explorer to shopify cli app scaffold
labels: Type: Enhancement, Area: @shopify/app
comment count: 4
hyperlink: https://github.com/shopify/cli/issues/5928
status: open
date opened: 2025-06-02
repo 30d_merge_rate: 77

====

description:
### What area(s) will this request affect?

Running your code locally

### What type of change do you want to see?

New feature

### Overview

It would be great to have [GraphiQL Explorer plugin](https://github.com/OneGraph/graphiql-explorer) in GraphiQL provided by shopify cli app creation.

For now, I am just using GraphiQL for the Admin API installed from [here](https://shopify-graphiql-app.shopifycloud.com/login) as described [here](https://shopify.dev/docs/api/usage/api-exploration/admin-graphiql-explorer)

### Motivation

Building queries would be much easier with local development.

===

comment #1 by amcaplan, 2025-06-03, 15:21:16
Hi @madfcat, are you aware that you run a local copy of GraphiQL Explorer when you run `app dev` on your app? It's mentioned in [the doc you linked](https://shopify.dev/docs/api/usage/api-exploration/admin-graphiql-explorer#use-a-local-graphiql-instance) and you should see the option to launch it with the `g` key.

comment #2 by madfcat, 2025-06-05, 11:59:22
> Hi [@madfcat](https://github.com/madfcat), are you aware that you run a local copy of GraphiQL Explorer when you run `app dev` on your app? It's mentioned in [the doc you linked](https://shopify.dev/docs/api/usage/api-exploration/admin-graphiql-explorer#use-a-local-graphiql-instance) and you should see the option to launch it with the `g` key.

I am aware. `app dev` runs GraphiQL without GraphiQL Explorer plugin (interface in which you can click checkboxes in schema to build queries and mutations). It is present in the docs link that you have provided. Where can I find it in the local copy?

<img width="1721" alt="Image" src="https://github.com/user-attachments/assets/839049ae-81b4-4af8-af37-8cf912b48322" />

<img width="945" alt="Image" src="https://github.com/user-attachments/assets/9c309d82-71a5-4b6c-8ce8-0c8048c42cf0" />

comment #3 by github-actions[bot], 2025-07-25, 03:52:37
This issue seems inactive. If it's still relevant, please add a comment saying so. Otherwise, take no action.
→ If there's no activity within a week, then a bot will automatically close this.
Thanks for helping to improve Shopify's dev tooling and experience.

P.S. You can learn more about why we stale issues [here](https://github.com/Shopify/cli/blob/main/docs/decision-record/2023_02-Stale-action.md).

comment #4 by madfcat, 2025-07-31, 17:38:40
> This issue seems inactive. If it's still relevant, please add a comment saying so. Otherwise, take no action. → If there's no activity within a week, then a bot will automatically close this. Thanks for helping to improve Shopify's dev tooling and experience.
> 
> P.S. You can learn more about why we stale issues [here](https://github.com/Shopify/cli/blob/main/docs/decision-record/2023_02-Stale-action.md).

still relevant
