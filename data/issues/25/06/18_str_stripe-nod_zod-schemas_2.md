issue title: Zod schemas
labels: future, feature-request
comment count: 3
hyperlink: https://github.com/stripe/stripe-node/issues/2350
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 8

====

description:
### Is your feature request related to a problem? Please describe.

I'd be nice to have zod schemas available.

### Describe the solution you'd like

Here is a workaround I am using in case it helps: https://gist.github.com/sergiojoker11/7e2da7fa97a67cba799f1e75a2e530c4

### Describe alternatives you've considered

_No response_

### Additional context

_No response_

===

comment #1 by jar-stripe, 2025-06-18, 19:20:55
Hi @sergiojoker11 thank you for the feature request!  We will add this to our backlog for consideration for future versions.  Can you share a bit about how you use Zod and how this would help you with your Stripe integration?

comment #2 by sergiojoker11, 2025-06-18, 23:03:36
Sure, definitely.

We are building the webhook part at the minute via EventBridge. Using some event bridge rules and targets events get queue in SQS and then consumed by a lambda function. So that those objects are properly typed and we don't have to do any casting we use that zod schema to parse the event as it steps into our platform. That way everything stays strongly typed and, in case something does not adhere to the schema we'd rather fail fast. If proper testing has been done nothing should go wrong in prod.

comment #3 by jar-stripe, 2025-06-23, 17:20:43
Thank you!  This is in our backlog.  We'll let you know here if we pick it up for a future version.
