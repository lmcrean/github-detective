# Issues for stripe/stripe-node

**Total Issues**: 179
**Repository**: https://github.com/stripe/stripe-node

**Open Issues**: 27
**Closed Issues**: 152

---

## Issues List (Most Recently Updated First)

- **#950: StripeAuthenticationError when loading stripe secret from environment variables**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-08-10
  > Hi all,  I'm currently working on a Stripe Checkout integration and I'm running into an issue when calling my api to create a Stripe session.  I'm using Next.js with API Routes and call my `create...

- **#2382: createPreview doesn't expand `lines.data.price.tiers`**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-08-05
  > ### Describe the bug  My goal is to get tiers along with the create preview API call.  However, below API call is success yet I do not receive any tiers informations    ### To Reproduce  ```typescript...

- **#1062: StripeConnectionError: An error occurred with our connection to Stripe.**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-08-01
  > **Node Version**:  v10.21.0 (necessary for running as a [Firebase Function](https://firebase.google.com/docs/functions)) **Node Platform**: MacOS 10.15.1 **Node Environment**: mocha w/ ts-node (thou...

- **#341: Webhook signature verification and bodyParser.json issue**
  - Labels: No labels
  - Comments: 85
  - Last updated: 2025-07-25
  > If you use in your express app `bodyParser.json()` for all routes, and then have a dedicated route for stripe's webhook, then the second call to `bodyParser.json({verify:  ...})` as done in the exampl...

- **#2368: Auto-pagination error iterating over subscriptions when updating last record of page to canceled state**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-07-23
  > ### Describe the bug  When using auto-pagination to iterate over active subscriptions, a `resource_missing` error is thrown if the last record in the current page is updated to a canceled state.  ###...

- **#2332: Requests not aborted within timeout**
  - Labels: bug
  - Comments: 8
  - Last updated: 2025-07-23
  > ### Describe the bug  I've noticed that the `elapsed` value in the `Stripe.ResponseEvent` sometimes exceeds the configured timeout by up to 15 seconds. I'm wondering if the request isn't being aborted...

- **#2378: Customer portal config - set min/max quantity range**
  - Labels: feature-request
  - Comments: 3
  - Last updated: 2025-07-21
  > ### Is your feature request related to a problem? Please describe.  Using 18.3.  Would like to configure a custom portal url that has a restriction on min/max quantity that can be update on a subscrip...

- **#2369: with Subscription object payment intent within latest invoice is not longer populated**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-07-10
  > ### Describe the bug  I'm trying to use the latest version of stripe 2025-06-30 With in stripe I have 2 products with two different prices In the code if I have a logged in user that doesn't have any...

- **#2366: stripe.invoices.retrieveUpcoming in SDK docs appears to be incorrect**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-07-07
  > ### Describe the bug  `stripe.invoices.retrieveUpcoming` is present in the [SDK Documentation](https://docs.stripe.com/api/invoices/upcoming?api-version=2024-12-18.acacia&lang=node) but when I try to...

- **#2364: Stripe V2 Account Link Preview - Results in 404**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-07-03
  > ### Describe the bug  We've enabled the V2 API in our Sandbox in the Stripe Dashboard to begin using V2 Accounts. We're using the latest preview for the Node SDK (18.4.0-beta.1).  Even using the examp...

- **#2327: TypeScript types are not accurate when expanding data and it's very annoying.**
  - Labels: bug, future
  - Comments: 5
  - Last updated: 2025-07-03
  > ### Describe the bug  I'm creating a new issue under the bug category because I don't think #1556 really captured how irritating this is. It makes using this otherwise fantastic package very tedious....

- **#2361: Add support for accounts v2**
  - Labels: feature-request
  - Comments: 0
  - Last updated: 2025-07-02
  > ### Is your feature request related to a problem? Please describe.  I had to dig through the source code to tell if `stripe.accounts` actually refers to v1 or v2 and apparently [it's v1](https://githu...

- **#2357: Export current api version string**
  - Labels: future, feature-request
  - Comments: 0
  - Last updated: 2025-07-01
  > ### Is your feature request related to a problem? Please describe.  I'm trying to ensure that when I update the stripe package that it also updates my event destination API version to match the types...

- **#2359: Missing 'nz_bank_account' in PaymentMethodType in SessionResources.d.ts**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-06-30
  > ### Describe the bug  SessionsResource.d.ts is missing the payment method 'nz_bank_account' on the type [PaymentMethodType](https://github.com/stripe/stripe-node/blob/ee9271384536644e2df20a9ca787a995f...

- **#2350: Zod schemas**
  - Labels: future, feature-request
  - Comments: 3
  - Last updated: 2025-06-23
  > ### Is your feature request related to a problem? Please describe.  I'd be nice to have zod schemas available.  ### Describe the solution you'd like  Here is a workaround I am using in case it helps:...

- **#2351: apiVersion set in new Stripe, but ephemeralKeys.create still ask for it**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-06-23
  > ### Describe the bug  ```js const stripe = new Stripe(conf.key, { apiVersion: '2025-05-28.basil' }); const customer = await stripe.customers.create(); const ephemeralKey = await stripe.ephemeralKeys.c...

- **#2353: `current_period_start` and `current_period_end` are not in the `Subscription` type**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-06-22
  > ### Describe the bug  Subscriptions have two properties, `current_period_start` and `current_period_end`, which appear in multiple examples in the docs, and work as I would expect, but are not listed...

- **#2349: Promotion code first_time_transaction isn't applied correctly**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-06-13
  > ### Describe the bug  I have a test mode customer with incomplete subscription and open invoice (no payments) and when I try to apply a promo code with first_time_transaction = true on create subscrip...

- **#1504: Possible error in README example, "Testing Webhook Signing"**
  - Labels: bug
  - Comments: 5
  - Last updated: 2025-06-12
  > ### Describe the bug  After implementing a webhook endpoint in a typescript express project, I first tested locally using the Stripe CLI. Everything worked as expected.  I then created automated t...

- **#2347: invoices.createPreview failing on customer param**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-06-11
  > ### Describe the bug  Docs for invoices.createPreview shows passing in customer id like so:  ``` const invoice = await stripe.invoices.createPreview({   customer: 'cus_NeZwdNtLEOXuvB', }); ```  Howeve...

- **#2340: Link used in "mcc" annotation goes to a missing page**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-05-30
  > ### Describe the bug  The link used here https://github.com/stripe/stripe-node/blob/8445f624fdcf278a5a61e0edb425fd46d9b23a4f/types/Accounts.d.ts#L140 points to a missing page.  https://stripe.com/conn...

- **#2241: Add AbortSignal support**
  - Labels: future, feature-request
  - Comments: 8
  - Last updated: 2025-05-22
  > ### Is your feature request related to a problem? Please describe.  Since v14, Node.js supports `AbortSignal` and `AbortController`. Both APIs allows to control async requests.  It allows the implem...

- **#2337: No signatures found matching the expected signature for payload**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-05-09
  > ### Describe the bug  I'm getting this error message when trying to use `stripe-webhook` edge function with Supabase  I already tried doing everything in the docs related to this issue: https://docs.s...

- **#2334: `retrieveUpcoming` missing?**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-05-07
  > ### Describe the bug  It seems as though the `stripe.invoices.retrieveUpcoming` function was removed as per v18 of this sdk? Was this intentional? If so, what should we now use?  ### To Reproduce  Sim...

- **#2328: Billing thresholds were removed from the API without adequate replacement**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-05-05
  > ### Describe the bug  Stripe completely removed `billing_thresholds` from subscriptions in their basil API update but doesn't detail how to actually migrate the same functionality:  https://docs.strip...

- **#2211: Default Node `httpClient` configuration does not get mocked by MSW nor upcoming Nock version**
  - Labels: bug, future
  - Comments: 5
  - Last updated: 2025-05-05
  > ### Describe the bug  Hi there. I'm using [`nock@beta`](https://github.com/nock/nock/tree/beta) and it is no longer able to intercept requests from this library when using the default Node.js `httpC...

- **#1556: TypeScript types are invalid when expanding responses**
  - Labels: No labels
  - Comments: 18
  - Last updated: 2025-05-03
  > ### Describe the bug  When expanding responses as per the documentation [here](https://stripe.com/docs/api/expanding_objects?lang=node), the return types for various Stripe methods are not updated to...

- **#2315: Accounts v2 API - Metadata not persisting**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-04-25
  > ### Describe the bug  Using version `^18.1.0-beta.2` of the Node.js SDK with the Accounts V2 API. Passing in the metadata Object does not persist to the Stripe customer/connect accounts.  ### To Repro...

- **#2305: `.retrieve()` calls should accept the object as first argument and allow reusing existing expansions**
  - Labels: future, feature-request
  - Comments: 1
  - Last updated: 2025-04-18
  > ### Is your feature request related to a problem? Please describe.  It is common that objects being passed around come expanded (e.g., webhook handler had to expand the object for routing purposes), b...

- **#2303: Usage records and retrieveUpcoming methods are removed in 18.0.0, but required for migrating customers to the new Meters API.**
  - Labels: bug
  - Comments: 5
  - Last updated: 2025-04-18
  > ### Describe the bug  We're trying to upgrade to the new Meters API, but the [official migration guide](https://docs.stripe.com/billing/subscriptions/usage-based-legacy/migration-guide#start-recording...

- **#2275: `stripe.invoices.upcoming` in SDK docs appears to be incorrect**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-04-14
  > ### Describe the bug  [Proration preview documentation here](https://docs.stripe.com/billing/subscriptions/prorations#preview-proration) uses `stripe.invoices.retrieveUpcoming` which appears to work a...

- **#1909: Property 'quantity' does not exist on type 'Response<Subscription>'**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-04-11
  > ### Describe the bug  When retrieving a subscription  `const subscription = await stripe.subscriptions.retrieve(sub)`  The resulting `Stripe.Subscription` has a `quantity` key.  However, typescri...

- **#2296: Detect breaking changes**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2025-04-08
  > ### Is your feature request related to a problem? Please describe.  When I read the list of breaking changes, I have a hard time figuring out if I’m affected or not.  https://github.com/stripe/stripe-...

- **#2299: Missing payment_intent in Invoice**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-04-08
  > ### Describe the bug  The Invoice object appears to be missing the payment_intent property when doing a  `stripe.invoices.retrieve(invoiceId)` or  `stripe.invoices.list({ limit: 3 })`  If an invoice i...

- **#2295: NPM module alias doesn't allow for module type resolution.**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-04-04
  > ### Describe the bug  If we use an alias for stripe via npm: ```npm i stripe-18@npm:stripe@18.0.0```  We are unable to resolve the index.d.ts as a module, although its present within our node modules...

- **#2176: Type issues**
  - Labels: feature-request
  - Comments: 3
  - Last updated: 2025-04-03
  > ### Is your feature request related to a problem? Please describe.  Some minor issues we identified from the latest API 2024-06-20  - product.attributes is not typed (https://docs.stripe.com/api/pro...

- **#2267: Stripe.SubscriptionSchedule.Phase type is missing trial property**
  - Labels: bug, future
  - Comments: 3
  - Last updated: 2025-04-03
  > ### Describe the bug  The `Stripe.SubscriptionSchedule.Phase` type in TypeScript is missing the `trial` property. I am currently using SubscriptionSchedules to sign up my users for a free 30-day trial...

- **#2273: Specify a major release for `apiVersion`**
  - Labels: future, feature-request
  - Comments: 3
  - Last updated: 2025-04-03
  > ### Is your feature request related to a problem? Please describe.  I'd like to pin my Stripe client to the latest major version (e.g., "acacia"). Right now, I can either declare a specific monthly ve...

- **#2290: Metadata not passed in customer.subscription.created when using live webhook**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-03-30
  > ### Describe the bug  ### Issue I’m encountering an issue where metadata is not being passed in the customer.subscription.created event when using a live webhook in production. However, the metadata i...

- **#2280: "Narrative" missing from evidence/dispute.**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-03-27
  > ### Describe the bug  We would like to be able to analyze our past disputes, part of doing that is seeing what the value of the "narrative" field was. I can see that it's returned via `https://dashboa...

- **#2276: ui_mode types out of sync with REST API**
  - Labels: feature-request
  - Comments: 2
  - Last updated: 2025-03-24
  > ### Is your feature request related to a problem? Please describe.  In the REST API, the Checkout Session ui_mode types are "embedded" | "hosted" | "custom"  wheras in stripe-node the Checkout Session...

- **#2268: Not working with Bun**
  - Labels: future
  - Comments: 2
  - Last updated: 2025-03-22
  > ### Describe the bug  When using Bun for starting my [Nitro app](https://github.com/nitrojs/nitro) using `bun .output/server/index.mjs` I get:  ``` error: Cannot find package 'stripe' from '/opt/rende...

- **#2274: Stripe.Subscription.data[0].plan type is missing plan property**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-03-22
  > ### Describe the bug  I am trying to `plan` property from subscription response however it showing an error. Even though logging the response does have plan property  ### To Reproduce  **Fetch subscri...

- **#2266: Not able to get charge's balance_transaction on payment_intent.succeeded first try**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-03-07
  > ### Describe the bug  Hello, after upgrading the SDK from 14.17.0 to 17.7.0 and api from 2023-10-16 to 2025-02-24.acacia I'm experiencing error when I try fetch charge's balance_transaction object on...

- **#2251: Scheduled Downgrade at Period End Not Triggering in Stripe Billing Portal?**
  - Labels: bug
  - Comments: 4
  - Last updated: 2025-02-27
  > ### Describe the bug  I'm using the Stripe API to configure the billing portal and allow subscription updates with scheduled downgrades. But, when I attempt to select a lower tiered plan with a shorte...

- **#2264: `clientSecret` is not valid and `options.defaultValues` is not an accepted parameter in Checkout beta**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-02-24
  > ### Describe the bug  I followed this https://docs.stripe.com/checkout/custom/quickstart  I use "stripe": "17.4.0-beta.2" and "@stripe/react-stripe-js": "^3.1.1" for embedded components. I am using Ty...

- **#645: Error: Invalid billing_cycle_anchor: must be one of now or unchanged**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-02-24
  > This is the code [supplied by the docs](https://stripe.com/docs/billing/subscriptions/billing-cycle#new-subscriptions): ``` const stripe = require('stripe')('sk_test_tYypR4PA1b5uu52A4iB84lXY');  (...

- **#1942: SubtleCryptoProvider cannot be used in a synchronous context**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-02-16
  > ### Describe the bug  After upgrading some modules in my project, the following error started popping up during tests: `SubtleCryptoProvider cannot be used in a synchronous context`.  ### To Reproduc...

- **#2262: Calls to stripe.customers.retrieveSubscription intermittently timing out in v2.9.0**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-02-10
  > ### Describe the bug  My integration using `v2.9.0` of this package stopped working properly yesterday.  The issue in my case seemed to be with calls to `stripe.customers.retrieveSubscription` which w...

- **#2263: Accessibility violations - iframe missing title**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-02-10
  > ### Describe the bug  We are experiencing issues on our site when assessing there are no a11y violations using `axe` accessibility tools after the recent change introducing the 'Autofill link' button:...

- **#2260: Subscription Not have "plan" children in interface**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-02-10
  > ### Describe the bug  I have used the main api for get Subscription, for get the plan and relative price: ![](https://i.imgur.com/19E6mkd.png)  The interface is Stripe.Subscription: ![](https://i.imgu...

- **#1542: Use async functions within request handling code**
  - Labels: future, feature-request
  - Comments: 8
  - Last updated: 2025-02-04
  > ### Is your feature request related to a problem? Please describe.  Currently, there is a lot of `setTimeout`s and other non-async-y code that means that we cannot take advantage of V8's [async stac...

- **#356: Problem parsing body: No signatures found matching the expected signature for payload**
  - Labels: No labels
  - Comments: 51
  - Last updated: 2025-02-01
  > I'm using AWS API Gateway/Lambda which passes the request body as an actual JSON object to my Lambda function, where I am calling `stripe.webhooks.constructEvent` on it.  It seems this function expect...

- **#2207: Neither apiKey nor config.authenticator provided**
  - Labels: bug
  - Comments: 18
  - Last updated: 2025-01-27
  > ### Describe the bug  When installing either the version 17.0.0 or 17.1.0 in a brand new next.js 14 from scratch after initializing stripe  ``` import Stripe from 'stripe';  export const stripe...

- **#2255: Best Tech Stack for Stripe Connect Express Integration: Laravel API vs. Vue 3 (Quasar Dashboard)**
  - Labels: feature-request
  - Comments: 2
  - Last updated: 2025-01-27
  > ### Is your feature request related to a problem? Please describe.  We're developing a project that requires onboarding vendors using **Stripe Connect for (Express Accounts)**. The primary challenge i...

- **#2100: Please add a Next.js App Router example for Webhook signing**
  - Labels: future, feature-request
  - Comments: 4
  - Last updated: 2025-01-14
  > ### Is your feature request related to a problem? Please describe.  _No response_  ### Describe the solution you'd like  _No response_  ### Describe alternatives you've considered  _No response_  ###...

- **#2248: You may only specify one of these parameters: allow_promotion_codes, discounts.**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-01-13
  > ### Describe the bug  I am trying to create a checkout session on Stripe. My requirement is to apply a default promo code by default while also displaying a promo code field, allowing users to chang...

- **#657: You can't delete invoices created by subscriptions.**
  - Labels: No labels
  - Comments: 8
  - Last updated: 2025-01-11
  > Hi, we are retrieving an invoice from an user that has been update to a new subscription.  We retrive the invoice:   `const invoice = await stripe.invoices.retrieve('in_1EudqzBn82mIxvX2CQAf****');...

- **#2246: Node.js 17.5.0 with restricted key missing permissions to retrieve accounts**
  - Labels: bug
  - Comments: 0
  - Last updated: 2025-01-09
  > ### Describe the bug  Hi, My app in NextJs (server component). I am trying fetch accounts using restricted key (I updated all possible permission on website to Read) by this code:   got this erro...

- **#2243: Stripe leaks NodeJS types if imported**
  - Labels: future, feature-request
  - Comments: 1
  - Last updated: 2025-01-06
  > ### Describe the bug  Due to weird behavior in TypeScript (Mainly https://github.com/microsoft/TypeScript/issues/37053) the use of `/// <reference types="node" />` will leak to any consumers of a ty...

- **#2231: Requests not Throwing Errors in NestJS App or AWS Lambda Node 20/18.x**
  - Labels: bug
  - Comments: 14
  - Last updated: 2025-01-06
  > ### Describe the bug  Within NestJS, when performing calls such as `StripeClient.invoices.create` or other operations with bad data, requests hang indefinitely and don't throw errors.  ### To Reproduc...

- **#331: Webhook signature validation not working**
  - Labels: No labels
  - Comments: 30
  - Last updated: 2025-01-04
  > Hi, I'm using the latest version of the stripe node.js library v4.19.0 and am trying to verify the signature in some test webhooks. It is failing with:  error: Error SyntaxError: Unexpected token o...

- **#2244: Incorrect Subscription Type**
  - Labels: bug
  - Comments: 4
  - Last updated: 2025-01-02
  > ### Describe the bug  The Subscription type is missing a few of the fields which are getting returned in the api response.   Another Issue is, I am only able to pass `apiVersion: "2023-08-16"`. If...

- **#2228: Types needed**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2024-12-19
  > ### Describe the solution you'd like  Noticed that the following new types were provided to the [UserProvidedConfig](https://github.com/stripe/stripe-node/blob/master/src/Types.d.ts#L250) but not [S...

- **#1636: Consider switching away from defining types with an ambient module**
  - Labels: future, feature-request
  - Comments: 3
  - Last updated: 2024-12-17
  > ### Is your feature request related to a problem? Please describe.  Right now, stripe defines its types with an amient module like so:  https://github.com/stripe/stripe-node/blob/a91857ad68c2ff1a3...

- **#2236: Plan is missing from Subscription namespace**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-12-11
  > ### Describe the bug  The Plan is missing from the Stripe.Subscription namespace: ``` "plan": {               "id": ["price_1PzNr6RoZW0oufzkXL0aCfRX"](https://dashboard.stripe.com/test/prices/pri...

- **#2234: The applies_to field is missing on the Coupon response object**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-12-06
  > ### Describe the bug  The `applies_to` field is missing on the Coupon response object in a scenario where it should be present.  ### To Reproduce  1. Create a coupon (through the web portal) and have...

- **#2233: Nestjs Webhook body check doesn't work in live mode**
  - Labels: bug
  - Comments: 0
  - Last updated: 2024-12-02
  > ### Describe the bug  Hello, when I configured the webhook in test mode, I was able to retrieve my body and process my requests, but when I switched to production mode I got this error, why?  ![imag...

- **#2197: Create customer portal session with flow subscription_update - property 'subscription_update' does not exist in type 'FlowData'**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-12-02
  > ### Describe the bug  TS complains about missing property 'subscription_update' on interface FlowData  ### To Reproduce  I want customers to be able to upgrade their subscriptions, so I followed...

- **#2223: Rate Limit returns HTTP 400 status code**
  - Labels: bug
  - Comments: 7
  - Last updated: 2024-11-11
  > ### Describe the bug  When i am creating connected accounts too quickly, i get an error with an HTTP status code of 400:  ```ts logger.error(error as Stripe.errors.StripeAPIError); logger.error(...

- **#2224: refund creation doesn't pass metadata to charge.refunded event**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-11-11
  > ### Describe the bug  we are creating a refund using stripe version "^17.0.0". we are calling stripe.refunds.create function and we pass some information in the metadata object. when the refund is b...

- **#2227: Add strict validation for webhook events**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2024-11-11
  > ### Is your feature request related to a problem? Please describe.  Currently the method that I'm using `stripe.webhooks.constructEventAsync` is not fully safe to use.  It just validates the signatu...

- **#2221: Missing endpoint `stripe.checkout.sessions.update`**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-11-02
  > ### Describe the bug  In [Stripe Docs](https://docs.stripe.com/api/checkout/sessions/update?lang=node&shell=true&api=true&resource=checkout%20sessions&action=update) I can see the example code provide...

- **#2112: PaymentIntent interafce does not have charges object in it even tho it is sent from stripe webhook on payment_intent.succeeded event**
  - Labels: bug
  - Comments: 5
  - Last updated: 2024-10-25
  > ### Describe the bug  PaymentIntent interafce does not have charges object in it even tho it is sent from stripe webhook on payment_intent.succeeded event.    ### To Reproduce  Check if type Stripe....

- **#2214: Total customers number doesn't match dashboard**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-10-23
  > ### Describe the bug  The number of customers displayed in the dashboard doesn't match the number of customers displayed in the dashboard  ### To Reproduce  Run a script to fetch all customers using s...

- **#2212: Stripe Connect: Platform pricing configuration ignored, resulting in a negative balance**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-10-21
  > ### Describe the bug  Our company is integrating Stripe Connect into our platform (based in Estonia), which has connected accounts based in Mexico. During our testing procedures, we noticed that the...

- **#2198: How to inspect Stripe's requests**
  - Labels: bug
  - Comments: 6
  - Last updated: 2024-10-03
  > ### Describe the bug  I'm seeking visibility on Stripe's requests.  In this piece of code: ```ts stripe.billingPortal.configurations.create({ 	business_profile: { 		headline: `${appName} - Custo...

- **#2191: Stripe docs are a mistake**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-09-27
  > ### Describe the bug  I didn't see a `docs` repo, so I'm guessing this is the right place for this. Please correct me if I'm wrong.  The `subscription_pause` key doesn't seem to be part of the `feat...

- **#2183: Prevent Instant Invoice Generation Upon Subscription Creation While Accruing Charges**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2024-09-23
  > ### Is your feature request related to a problem? Please describe.  I am currently using Stripe to manage subscriptions for my platform. My use case requires users to incur prorated charges from the d...

- **#2013: display_brand type missing in PaymentMethods.Card**
  - Labels: bug, future
  - Comments: 3
  - Last updated: 2024-09-10
  > ### Describe the bug  display_brand type is missing in the PaymentMethods.Card but it is sent by the api  ``` display_brand: {         label = "Visa"         logo_url = "https://b.stripecdn.com...

- **#650: StripeConnectionError: An error occurred with our connection to Stripe.**
  - Labels: No labels
  - Comments: 7
  - Last updated: 2024-09-02
  > Have been running into this issue during development. Sometimes everything works fine and other times I get this error  version: 7.20  I'm not sure if its a bug or a connectivity issue   ```sh...

- **#2166: `SELF_SIGNED_CERT_IN_CHAIN` when I am trying to mock it with MockServer**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-09-01
  > ### Describe the bug  I am getting this error message when I configure my stripe instance to send requests to the [MockServer](https://www.mock-server.com/):  ```cmd  StripeConnectionError: An erro...

- **#2165: Webhook Error 403**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-08-31
  > ### Describe the bug  Hi, I am experiencing a problem with the Stripe webhook listener while developing locally.  When I run my project on localhost:3000 and I am listening for Stripe webhooks, eve...

- **#1294: NextJS - Error: construction of webhook event returned an error: No signatures found matching the expected signature for payload. Are you passing the raw request body you received from Stripe? https://github.com/stripe/stripe-node#webhook-signing**
  - Labels: No labels
  - Comments: 21
  - Last updated: 2024-08-30
  > Hi   I am pulling my hair out trying to pass raw JSON to NextJS 12 endpoint.  I have tried sooo many solutions and I just cant get it to work.  Please help as I have wasted half a day on this an...

- **#407: Timestamp outside the tolerance zone**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2024-08-24
  > When using the express example I get the error: Timestamp outside the tolerance zone  Can anyone suggest what could be the reason?

- **#2153: Property 'retrieve' does not exist on type 'CalculationsResource'**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-08-20
  > ### Describe the bug  Typescript type information is missing for the `stripe.tax.calculations.retrieve` api method described here: https://docs.stripe.com/api/tax/calculations/retrieve  ### To Reprodu...

- **#1846: Listen for errors globally**
  - Labels: future, feature-request
  - Comments: 3
  - Last updated: 2024-08-13
  > ### Is your feature request related to a problem? Please describe.  I would like to listen for errors in my Stripe calls so that I can log to my error tracking service.  I see there is `stripe.on(...

- **#2156: feat: Modular API for edge runtimes**
  - Labels: future, feature-request
  - Comments: 1
  - Last updated: 2024-08-12
  > ### Is your feature request related to a problem? Please describe.  In "edge runtimes" such as Cloudflare Workers, Vercel Edge Functions, the size of the application code comes at a premium (as little...

- **#2154: Cannot create a product with custom unit amount**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-08-07
  > ### Describe the bug  [Per the Stripe API docs](https://docs.stripe.com/api/products/create), I am attempting to create a Product using the Stripe API with `default_price_data.currency_options.usd.cus...

- **#2141: TWINT Payment Method missing from `PaymentMethodConfigurationCreateParams`**
  - Labels: bug
  - Comments: 4
  - Last updated: 2024-07-25
  > [TWINT](https://docs.stripe.com/payments/twint) is a new payment method in Switzerland. It hasn't been added to `PaymentMethodConfigurationCreateParams`.

- **#2024: invoice.will_be_due event is missing in webhook events types**
  - Labels: bug, future
  - Comments: 7
  - Last updated: 2024-07-25
  > ### Describe the bug  ![image](https://github.com/stripe/stripe-node/assets/5787117/4ab6f4b3-7a8d-46f9-9524-cc51cf638bc4)  ![image](https://github.com/stripe/stripe-node/assets/5787117/4a96319e-ecd6...

- **#2142: Product Data metadata is not returned when calling listLineItems**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2024-07-25
  > ### Is your feature request related to a problem? Please describe.  I'm writing my function to fulfill orders, and trying to identify products in my db based on the metadata sent on price_data.product...

- **#2139: `plan` is missing on `Stripe.Subscription` type**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-07-15
  > ### Describe the bug  The `Stripe.Subscription` type does not match the data returned from `stripe.subscriptions.retrieve()`.  ### To Reproduce  ```ts import Stripe from 'stripe';  const stri...

- **#2060: stripe.resources.Checkout.prototype seems to be broken?**
  - Labels: bug
  - Comments: 5
  - Last updated: 2024-07-12
  > ### Describe the bug  Seems to be empty compared to other prototypes. <img width="332" alt="Screenshot 2024-04-07 at 9 52 25 PM" src="https://github.com/stripe/stripe-node/assets/61447509/5272a651-6f...

- **#2135: Connect Account Payout object does not contain stripe account payment intent or charge obj id.**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-07-10
  > ### Describe the bug  When working with Stripe Connect, the Payout object for a connected account does not contain direct references to the original PaymentIntent or Charge object IDs from the platfor...

- **#2131: List Prices not reporting active status properly**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-07-09
  > ### Describe the bug  When I make a request to get a list of prices using `stripe.prices.list({active: true})`, I get a bunch of prices on products that I just archived.  When I make a subsequent at...

- **#2114: `_prepResources()` and `ResourceNamespace` iterate all properties, but don't check `hasOwnProperty`**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-07-09
  > ### Describe the bug  Hi there, when including the [scope-extensions-js](https://github.com/TheDavidDelta/scope-extensions-js) package in my project, Stripe errors out with the following on startup:...

- **#2076: stripe-node bumps into TypeScript issue 45096 for triple slash directives when forceConsistentCasingInFileNames**
  - Labels: feature-request
  - Comments: 8
  - Last updated: 2024-07-08
  > ### Is your feature request related to a problem? Please describe.  Logging this as a FR because the issue is caused by an [long-open TS issue](https://github.com/microsoft/TypeScript/issues/45096),...

- **#2117: consider replacing `qs` dependency**
  - Labels: future, feature-request
  - Comments: 1
  - Last updated: 2024-07-01
  > ### Is your feature request related to a problem? Please describe.  The `qs` library includes a lot of polyfills via subdependencies. Polyfills that are required for very old versions of Node.js below...

- **#2127: Type Stripe.Subscription don't show attribute plan**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-06-29
  > ### Describe the bug  There is a problem with the typing of Stripe.Subscription. The plan object within the subscription is not being properly recognized.  ### To Reproduce  Try to access the pl...

- **#2124: Stripe.paymentIntents missing `payment_method_details` type but is included in the returned data object.**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-06-28
  > ### Describe the bug  Using NextJS 14. I'm trying to get the last 4 digits of the card on payment success event. I set up my code to create a payment intent from the server with `confirm: true` and...

- **#2123: Stripe elements are showing errors after mounting**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-06-28
  > ### Describe the bug  I'm not sure how to describe it, but suddenly my Stripe form is loading the fields with an error state, as shown in the picture. What could be going wrong? The fields have never...

- **#644: How add metadata in payment intent when creating subscription**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2024-06-19
  > I need to set metadata in every payment intent because i want to receive hook from `payment_intent.created` event always with some fields in meta data. In which way i can do it?

- **#2105: NodeJs - InvoiceItemsUpdateParams - Missing "invoice" param as an option**
  - Labels: bug
  - Comments: 4
  - Last updated: 2024-06-11
  > ### Describe the bug  Documentation here (https://docs.stripe.com/api/invoiceitems) states that "You can add an invoice item to to an invoice by creating or updating it with an invoice parameter". Th...

- **#2096: Missing type in Checkout.SessionCreateParams**
  - Labels: bug
  - Comments: 8
  - Last updated: 2024-06-05
  > ### Describe the bug  types/Checkout is missing the property payment_method_data.  https://docs.stripe.com/api/checkout/sessions/create  ### To Reproduce  Add a params const and set the type to Stri...

- **#2099: Stripe.checkout.session Type error**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-05-31
  > ### Describe the bug  Stripe.checkout.session type have `shipping_details` property but webhook request doesn't contain `shipping_details`, it has `shipping` property  ### To Reproduce  1) Add e...

- **#2097: Add dashboard-visible Radar results to SetupIntent or SetupAttempt**
  - Labels: feature-request
  - Comments: 2
  - Last updated: 2024-05-28
  > ### Is your feature request related to a problem? Please describe.  My company applies Charges to saved Cards/PaymentMethods well after accepting payment information. Currently, we set those PaymentMe...

- **#1896: stripe__WEBPACK_IMPORTED_MODULE_0__.default is not a constructor**
  - Labels: bug
  - Comments: 12
  - Last updated: 2024-05-18
  > ### Describe the bug  I receive an error when importing stripe:  ![image](https://github.com/stripe/stripe-node/assets/45767683/d114373f-0ab1-462e-9579-e3714802b261) ![image](https://github.com/str...

- **#2091: Support for `footer` in `invoice_settings`**
  - Labels: feature-request
  - Comments: 2
  - Last updated: 2024-05-17
  > ### Is your feature request related to a problem? Please describe.  I'm not sure if this is a bug in this library or lack of support in the underlying API, but there doesn't seem to be a way to prog...

- **#1502: Export object interfaces from Typescript definitions**
  - Labels: future, feature-request
  - Comments: 10
  - Last updated: 2024-05-10
  > ### Is your feature request related to a problem? Please describe.  I need to be able to reference object interfaces defined inside the Stripe namespace, but I'm unable to because these interfaces are...

- **#2089: Prices.list throws error when ids array length rather than default limit (10) even when limit provided**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-05-09
  > ### Describe the bug  Whenever I call the stripe prices api ``` stripe.prices.list({ limit: pricesToFetch.length, lookup_keys: pricesToFetch }); ``` i get an error  ``` error: {      "type": "E...

- **#2082: Argument "subscriptionExposedId" must be a string, but got: undefined**
  - Labels: bug
  - Comments: 0
  - Last updated: 2024-05-05
  > ### Describe the bug  After Success on `checkout.sessions.create` it saves on my database and also goes through on the dashboard (stripe) and I can see it is successful . But afterwards my server cras...

- **#2081: update typescript interface to include v15.0.0 changes (features => marketing_features)**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-05-04
  > ### Describe the bug  I use inbuilt types from the Stripe library, the interface for Product still has the old 'features' instead of the new 'marketing_features' which been introduced in v15.  ### To...

- **#2078: No signatures found matching the expected signature for payload.**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-05-02
  > ### Describe the bug  I'm using Astro to construct a webhook for Stripe, following the Deno example here because it uses the same `request` object.   But I'm getting an error that says "No signature...

- **#2075: id type does not exist on SourceTransaction.PaperCheck**
  - Labels: bug, future
  - Comments: 1
  - Last updated: 2024-04-30
  > ### Describe the bug  Although the event for `source.transaction.update` provides an ID for the paper check if the transaction is a paper check transaction, the type does not include `id` under `Paper...

- **#2068: Get Stripe Customer List**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-04-16
  > ### Describe the bug  I am trying to fetch list of stripe customers and filtering it using an email:  `        const customers = await stripe.customers.list({email: 'musadiq.khan@gmail.com'});...

- **#2066: Unnecessary dependency @types/node in non dev dependency**
  - Labels: bug, future
  - Comments: 1
  - Last updated: 2024-04-15
  > ### Describe the bug  viewing the latest version of stripe, there is a **types** on a **dependency** level instead of **devDependency** - so on production install, the types are still installed and...

- **#1953: [1]  ⨯ Error: Stripe: Argument "subscription_exposed_id" must be a string, but got: undefined (on API request to `GET /v1/subscriptions/{subscription_exposed_id}`)**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-04-11
  > ### Describe the bug  Dear all,  I am just trying to understand how to stripe in my project. This is my `webhook` code  ```js import { headers } from "next/headers" import Stripe from "stripe"...

- **#2063: stripe.checkout.sessions.create(params) stopped working between Next.js 14.1.0 and 14.1.4**
  - Labels: bug
  - Comments: 8
  - Last updated: 2024-04-10
  > ### Describe the bug  I get this error:  ``` Internal error: Error: Missing required param: success_url.     at StripeError.generate (./node_modules/stripe/esm/Error.js:23:20)     at res.toJSON.t...

- **#2056: [Feature request] built-in retry when `lock_timeout` error for `stripe.customers.retrieve()`**
  - Labels: feature-request
  - Comments: 2
  - Last updated: 2024-03-29
  > ### Is your feature request related to a problem? Please describe.  sometimes i get the below error and it would be nice if the library could take care of it (with exponential backoff) instead of devs...

- **#2041: Cannot access LatestApiVersion type in Typescript**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-03-22
  > ### Describe the bug  `LatestApiVersion` is exported as a type, but I cannot seem to be able to access it  ### To Reproduce  1. create new Stripe instance 2. try to use `LatestApiVersion` for `apiVer...

- **#2042: error.type does not survive minification**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-03-21
  > ### Describe the bug  When bundling and minifying using a tool like esbuild, the `type` included in errors thrown by Stripe is also minified into a shorter string. Strings are usually safe from minifi...

- **#2044: Export StripeError class**
  - Labels: feature-request
  - Comments: 2
  - Last updated: 2024-03-21
  > ### Is your feature request related to a problem? Please describe.  I'm not sure then this was changes. I'm trying to update my code to the latest stripe version and update API. Currently I'm on `11.6...

- **#2038: Remix/Cloudflare | Uncaught ReferenceError: process is not defined**
  - Labels: bug
  - Comments: 7
  - Last updated: 2024-03-18
  > ### Describe the bug  When using `'stripe'` package in Remix on CloudFlare workers, it throws an error  `Uncaught ReferenceError: process is not defined`  ### To Reproduce  - Goto https://codesandbo...

- **#2037: Resolution for worker and other modules fails**
  - Labels: bug
  - Comments: 5
  - Last updated: 2024-03-18
  > ### Describe the bug  If you try to use `import Stripe from 'stripe/worker';`, it throws an error, `Cannot resolve dependency 'stripe/worker'`  There are also some other TS types problems - https://...

- **#1535: Add a "locale" variable to the options configuration**
  - Labels: future, feature-request
  - Comments: 2
  - Last updated: 2024-03-17
  > ### Is your feature request related to a problem? Please describe.  I'm actually facing a problem when the errors returning by Stripe Node are all in English. I would like to have to possibility to...

- **#2034: Please pull through 'active' value on subscriptions, rather than putting it in a string as 'status' where that status can be overwritten by other values**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2024-03-07
  > ### Is your feature request related to a problem? Please describe.  I'm annoyed that the Subscription object does not have a simple, clear way to see that a subscription is currently active. If you ha...

- **#2031: Api feature: Credit notes - filter by date**
  - Labels: feature-request
  - Comments: 3
  - Last updated: 2024-03-04
  > ### Is your feature request related to a problem? Please describe.  Working on an accounting solution, we need to get invoices and credit notes for a given date range. While it is possible to list inv...

- **#2028: Add the "node:" prefix in Node.js core module imports**
  - Labels: bug
  - Comments: 4
  - Last updated: 2024-02-29
  > ### Describe the bug  When developing an application using Stripe on Cloudflare Pages, a crypto is not found error occurred.  ### To Reproduce  1. Copy the Cloudflare Pages template using `create hono...

- **#1999: Incomplete Typescript Types**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-02-28
  > ### Describe the bug  The types for retrieving are incomplete.  (checkout.sessions.retrieve, some.function.retrieve, ...etc)  the return type gives customers as optionals when it needs to depend...

- **#2020: default_currency is optional on the Account object type**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-02-13
  > ### Describe the bug  Hello, On the Account object, the type of default_currency is optional  https://github.com/stripe/stripe-node/blob/master/types/Accounts.d.ts#L59  However, the documentatio...

- **#2019: Invoice is always empty**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-02-11
  > ### Describe the bug  When using the below code I get this empty data array:  ```js {   object: 'list',   data: [],   has_more: false,   url: '/v1/invoiceitems' } ```  ### To Reproduce  ```ts...

- **#2016: Subscription Back date**
  - Labels: feature-request
  - Comments: 3
  - Last updated: 2024-02-09
  > ### Is your feature request related to a problem? Please describe.  So I have a use case, wherein I want to start a subscription in the backdate to avoid proration. The example is as follows,  A cust...

- **#2015: stripe events resend support in stripe-node**
  - Labels: feature-request
  - Comments: 3
  - Last updated: 2024-02-07
  > ### Is your feature request related to a problem? Please describe.  I am building automated dead letter replay for stripe events. We have several processes that rely on stripe event delivery to func...

- **#2006: Allow HTTP requests to *.stripe.com**
  - Labels: feature-request
  - Comments: 2
  - Last updated: 2024-02-05
  > ### Is your feature request related to a problem? Please describe.  Currently the library does not allow HTTP connections to Stripe API, rightfully. However, changing the protocol back to HTTP might b...

- **#2011: Please add Stripe payment for Egypt**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2024-02-01

- **#2008: Change a price**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-01-28
  > ### Describe the bug  Dear all,  I cannot find any way to contact the support so I am inquiring here. How do I change a price in the dashboard? I cannot really understand it from the UI  <img widt...

- **#2007: Missing types for shipping based on Session object and checkout.session.completed event**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-01-28
  > ### Describe the bug  I am utilizing some data that are not typed by the Stripe.Checkout.Session object that I received from checkout.session.completed event  Had to extend the typings usign the fol...

- **#2005: Duplicate customer creating at Stripe Dashboard**
  - Labels: bug
  - Comments: 0
  - Last updated: 2024-01-27

- **#2004: Permission denied when passing unified_accounts_beta=v1 header**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-01-26
  > ### Describe the bug  I have been in contact with stripe support back and forth a lot since _December 7th_ and I haven't been able to get a straight answer as to why I can't integrate what is outlined...

- **#2003: Expandable object types used in webhooks instead of strings**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-01-26
  > ### Describe the bug  Example handling of setup intent complete: ```           case 'setup_intent.succeeded': {             const setup_intent = event.data.object;             const customer_id...

- **#1586: Subscription Custom Invoice Field missing on the API**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-01-23
  > ### Describe the bug  I can add/edit custom invoice fields of a subscription on the dashboard (on create and on update).  But this is not exist on the Stripe.js library. <img width="666" alt="image"...

- **#2000: Pre authorize an invoice payment**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2024-01-22
  > ### Is your feature request related to a problem? Please describe.  I had my payment integration set up and working. Basically I have gifting app where the user creates a gifting campaign, and the t...

- **#1978: previous_attributes on StripeEvent should be typed as Partial**
  - Labels: feature-request
  - Comments: 2
  - Last updated: 2024-01-22
  > ### Is your feature request related to a problem? Please describe.  Created from https://github.com/stripe/stripe-node/issues/758#issuecomment-1866063063  @hayksaryan  > For me, event.data.previ...

- **#1424: Missing Types on Invoice PaymentMethodType**
  - Labels: bug, type definition
  - Comments: 5
  - Last updated: 2024-01-12
  > ### Describe the bug  `Invoice.d.ts` is missing payment methods on the type [`PaymentMethodType`](https://github.com/stripe/stripe-node/blob/master/types/2020-08-27/Invoices.d.ts#L733). From the docs...

- **#1984: `invoiceitem.updated` poorly documented**
  - Labels: bug, next-major
  - Comments: 2
  - Last updated: 2024-01-12
  > ### Describe the bug  There seems to be an event type for `invoiceitem.updated` found [here](https://github.com/stripe/stripe-node/blob/master/types/EventTypes.d.ts#L3395-L3402) but when I view the [E...

- **#1981: Verifying signatures: add hint about line endings**
  - Labels: feature-request
  - Comments: 3
  - Last updated: 2024-01-12
  > ### Is your feature request related to a problem? Please describe.  Stripe's uses `\n` in it's payload. If you were to console.log() the raw payload, and paste into say, Postman (on windows at least...

- **#1991: metadata empty when retrieving a Checkout Session's line items**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-01-08
  > ### Describe the bug  Hello everyone, I've created a stripe checkout session and in the **line_items property** I'm passing the products I receive from the request's body. In the **product_data**...

- **#1983: Attempt to read property "last4" on null**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-12-31
  > ### Describe the bug  Upgraded to Spark 5.0 from Spark 4.0     ### To Reproduce  Create a Subscription, visit billing portal -> code breaks.  ### Expected behavior  nullcheck on $paymentMethod->card...

- **#1982: CSP on checkout server is causing problems in Google Chrome**
  - Labels: bug
  - Comments: 3
  - Last updated: 2023-12-27
  > ### Describe the bug  In my Next.js app, I create the stripe checkout session inside a server action, as follows:  ```ts export async function createCheckoutSession(ordersForPriceCalculation: Ord...

- **#1980: Whitespace in header signature**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-12-23
  > ### Describe the bug  I have problem with the header signature  Note: The provided signing secret contains whitespace. This often indicates an extra newline or space is in the value t=1703329668,v1...

- **#758: Specify event.data.object as an alternative**
  - Labels: future, type definition
  - Comments: 17
  - Last updated: 2023-12-22
  > `event.data.object` is currently specified as an empty interface, which seems invalid. My understanding of the API is that it should be an alternative of all possibilities. Relevant code:  https://g...

- **#1254: Webhook validate signing error: No signature found matching the expected signature for payload. | express**
  - Labels: No labels
  - Comments: 20
  - Last updated: 2023-12-20
  > # Another 'Webhook validate signing' issue! Whoooohooo 🥳   Hi there! I am trying to built a Backend Server for a Web project with Google Cloud App Engine.   ## What do I want to achieve: I want...

- **#1463: Zero currency converter**
  - Labels: future, feature-request
  - Comments: 2
  - Last updated: 2023-12-17
  > ### Is your feature request related to a problem? Please describe.  Working with multiple currencies is difficult since there are zero decimal currencies. We have to create and calculate the conversi...

- **#590: Received unknown parameter: transfer_data[destination]**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2023-12-15
  > I'm hoping someone can help me.  I am using stripe in Canada. I am doing a stripe charge without doing a capture. Afterward, when I process the charge I add in the transfer_data[destination] while doi...

- **#1693: Support for tree-shaking**
  - Labels: future, feature-request
  - Comments: 6
  - Last updated: 2023-12-05
  > ### Is your feature request related to a problem? Please describe.  Stripe apps developers are looking for a tree-shakeable Stripe SDK to help reduce the size of their apps  https://github.com/strip...

- **#1970: Extend all resources w/ API mode DELETE: stripeMethod del()**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2023-12-02
  > ### Is your feature request related to a problem? Please describe.  Reviewed https://stripe.com/docs/api, several resources support mode **DELETE** are not extended with **stripeMethod del()** by th...

- **#1963: Add Parameter: Status filter to /payouts**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2023-11-20
  > ### Is your feature request related to a problem? Please describe.  I use this API and it would be cleaner and less data if /payouts had a parameter to filter out status: paid, in_transit  ### Describ...

- **#1428: The library doesn't work on Deno. **
  - Labels: bug
  - Comments: 16
  - Last updated: 2023-11-17
  > ### Describe the bug  It was fixed in https://github.com/stripe/stripe-node/issues/997, but as I've pointed out in https://github.com/stripe/stripe-node/issues/997#issuecomment-1115941961, it doesn'...

- **#1956: Make webhooks utilities available as a static property**
  - Labels: feature-request
  - Comments: 5
  - Last updated: 2023-11-17
  > ### Is your feature request related to a problem? Please describe.  In some scenarios for me (normally when using Stripe Connect), we don't have enough information to create a Stripe instance until we...

- **#1950: Use AbortSignal for timeout in FetchHttpClient implementation**
  - Labels: future, feature-request
  - Comments: 1
  - Last updated: 2023-11-13
  > ### Is your feature request related to a problem? Please describe.  The current implementation of `FetchHttpClient` uses `Promise.race()` to reject the promise while not actually cancelling the fetch...

- **#977: StripeAuthenticationError error on stripeAPI.paymentMethods.list**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2023-11-11
  > Hi there,  when I try to list specific customer as stated here:  ```js stripe.paymentMethods.list({customer: 'customerid', type: 'card'}); ``` I got 400 with following result  ```json type:...

- **#1951: Null value for `idempotency_key` on webhook**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-11-07
  > ### Describe the bug  I'm using webhooks to listen to the `customer.subscription.trial_will_end` event, when I receive the event I get **null** values for  `idempotency_key` and `id` under the _requ...

- **#1949: Unable to filter calls using startTime and endTime in the list method (please see closing comments in `Additional context` section)**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-11-06
  > ### Describe the bug  My code works perfectly when I run:  ```ts const calls = await twilioClient.calls.list({   from: "+12223334444", // fake number }) ```  but when I try to add the `startTi...

- **#1946: Cannot specify API version other than latest ("2023-10-16")**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-10-31
  > ### Describe the bug  I'm unable to supply stripe with my API version "2020-08-27". This is causing issues as it's breaking types since it thinks for example, certain enum values exist that don't in t...

- **#1944: Checkout session create success_url should be optional?**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-10-30
  > ### Describe the bug  May be interpreting the docs incorrectly, but it looks like checkout session success_url was relatively recently changed to optional; however, when creating a checkout sessions w...

- **#902: [Feature] Strongly Typed Event Type for Stripe.Event**
  - Labels: future, type definition
  - Comments: 11
  - Last updated: 2023-10-26
  > Not too important, but it would be nice if this type:  https://github.com/stripe/stripe-node/blob/02da7dc2c5edae280aaf5e3566f3b7b383024371/types/2020-03-02/Events.d.ts#L52  is strongly typed with...

- **#1941: Add Type for <stripe-pricing-table> element**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2023-10-19
  > ### Is your feature request related to a problem? Please describe.  Adding a stripe pricing table no-code embed causes errors in TypeScript:  ``` Property 'stripe-pricing-table' does not exist on t...

- **#1937: error TypeError: stripe__WEBPACK_IMPORTED_MODULE_1__.default is not a constructor **
  - Labels: bug
  - Comments: 3
  - Last updated: 2023-10-18
  > ### Describe the bug  I'm adding stripe integration into a NextJS 13.4+ app. I have an endpoint that looks like this:  ```javascript import Stripe from 'stripe';  export async function POST(requ...

- **#1923: Move types to separate @types npm package**
  - Labels: feature-request
  - Comments: 5
  - Last updated: 2023-10-18
  > Hi there,  In my case, I use only typing from the `stripe` package.  Is it possible to move the `types` folder to a separate types definition package like @types/stripe?  I didn't find any similar...

- **#1936: list payment intents of specific account return an empty array**
  - Labels: bug
  - Comments: 0
  - Last updated: 2023-10-17
  > ### Describe the bug   i am using stripe shell from the website for getting list of payment intent to spefic payment account ex: stripe payment_intents list --stripe-account acct_xxxxxxxxxxxx i get...

- **#317: Received unknown parameter: name**
  - Labels: No labels
  - Comments: 10
  - Last updated: 2023-10-17
  > npm version 4.16.0 node version 6.10 This worked until three days ago.  When I create a customer, I recieve this error from Stripe :   ```  stripe.customers.create({       card: data.card_tok...

- **#1934: Api version 2023-10-16 appears to not exist**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-10-17
  > ### Describe the bug  The release notes for version 14.0.0 appear to link to a non-existent api version: https://stripe.com/docs/upgrades#2023-10-16. The stripe dash also lists 2023-08-16 as the lates...

- **#1922: need a v13+ beta released that includes `CustomerSession` **
  - Labels: feature-request
  - Comments: 2
  - Last updated: 2023-10-12
  > ### Is your feature request related to a problem? Please describe.  We rely on the pricing tables UI where our customers choose a plan from. We need to be able to pass existing customers, so rely on t...

- **#1918: Creating Invoice Items before Invoice - No longer getting automatically added to invoice**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-10-05
  > ### Describe the bug  We just upgrade our stripe-node package to latest `13.0.8` from `8.177.0` and started having some issues with the invoice and invoice item creation logic.   According to the...

- **#541: Expose constants**
  - Labels: future
  - Comments: 3
  - Last updated: 2023-09-28
  > Would it possible to expose constants on the relevant API endpoints (or in its own namespace)? For example:  ```js stripe.constants.subscriptionStatuses = {   TRIALING: 'trialing',    ACTIVE: 'ac...

- **#1116: Add Typescript Definition for Creating a File**
  - Labels: future, type definition
  - Comments: 2
  - Last updated: 2023-09-28
  > Node Version: 13.9.0 Stripe Version: 8.76.0  The Typescript definition for `FileCreateParams` in `Files.d.ts` appears to be incomplete.  Source: ``` interface FileCreateParams {} ```

- **#1765: Support for clear_usage param when deleting subscription item**
  - Labels: feature-request
  - Comments: 4
  - Last updated: 2023-09-28
  > ### Is your feature request related to a problem? Please describe.  According to [these Stripe API docs](https://stripe.com/docs/api/subscription_items/delete#delete_subscription_item-clear_usage),...

- **#1772: the PaymentMethod.CardPresent interface is empty**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-09-28
  > ### Describe the bug  In types/PaymentMethods.d.ts, the CardPresent interface is empty Issue persists as of v12.2.0  ### Expected behavior  The expected type should be similar to the Card inter...

