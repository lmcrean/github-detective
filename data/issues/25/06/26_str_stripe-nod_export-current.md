issue title: Export current api version string
labels: future, feature-request
comment count: 0
hyperlink: https://github.com/stripe/stripe-node/issues/2357
status: open
date opened: 2025-06-26
repo 30d_merge_rate: 8

====

description:
### Is your feature request related to a problem? Please describe.

I'm trying to ensure that when I update the stripe package that it also updates my event destination API version to match the types (including "non-breaking" additions that will be in the types but not in older snapshots!)

Our event destination updates is sufficiently automated (an AWS CloudFormation custom resource) that this is actually the majority of the effort and risk in an SDK update (excluding API breaking changes, of course!)

### Describe the solution you'd like

For a strawman: `Stripe.DEFAULT_API_VERSION` but shouldn't matter except that ideally I shouldn't need to create an instance (since the types are not specific to any stripe account)

### Describe alternatives you've considered

At the moment it's either:
* a manual step looking at the npm package source,
* using the undocumented / untyped `new Stripe(apiKey)._api.version`, or
* using the undocumented `Stripe.prototype.getConstant("DEFAULT_API_VERSION")` (which says to open an issue, hello! 👋)

### Additional context

_No response_

===
