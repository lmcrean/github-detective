# Issues for stripe/stripe-go

**Total Issues**: 65
**Repository**: https://github.com/stripe/stripe-go

**Open Issues**: 7
**Closed Issues**: 58

---

## Issues List (Most Recently Updated First)

- **#2093: Unable to create BankAccount**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-08-11
  > ### Describe the bug  Error on create BankAccount: `parse \"https://api.stripe.com/v1/accounts/btok_456/external_accounts%!(EXTRA string=, string=acct_123)\": invalid URL escape \"%!(\"\n`  The OpenAP...

- **#2092: Missing .Metadata field for BankAccountCreateParams**
  - Labels: bug
  - Comments: 4
  - Last updated: 2025-08-11
  > ### Describe the bug  Error on create BankAccount with specified Metadata: `You cannot specify both the (deprecated) .Params.Metadata and .Metadata in BankAccountCreateParams`  BankAccountCreateParams...

- **#2104: Add Opentelemetry support**
  - Labels: feature-request
  - Comments: 0
  - Last updated: 2025-08-08
  > ### Is your feature request related to a problem? Please describe.  We are trying to figure out what is the most optimal way to add OTEL to the Stripe API calls.  ### Describe the solution you'd like...

- **#2095: TerminalReaderCollectInputsInputSelectionParams server-side validation issue**
  - Labels: bug
  - Comments: 9
  - Last updated: 2025-07-30
  > ### Describe the bug  In order to use specific beta features for the client we have to switch our SDK from `v79.13.0-beta.1` to `v82.3.0-beta.1`.  Whilst conducting the smoke testing we have identifie...

- **#2094: charge.Invoice does not exists in Charges Retrieve API**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-07-29
  > ### Describe the bug  When i call the Rest API directly, i can see the charges have `invoice` property, but in Golang it does not  ```sh curl --location 'https://api.stripe.com/v1/charges/py_3Rnw8qAq0...

- **#2087: Seq2 and LastResponse**
  - Labels: bug
  - Comments: 6
  - Last updated: 2025-07-29
  > ### Describe the bug  Hi there, I've noticed what I believe to be an oversight in the new Stripe Client that's referenced [here](https://github.com/stripe/stripe-go/wiki/Migration-guide-for-Stripe-Cli...

- **#1937: Add `omitempty` to JSON field tags on optional fields**
  - Labels: future, feature-request
  - Comments: 11
  - Last updated: 2025-07-24
  > ### Describe the bug  When my API receives a webhook request from Stripe via the CLI, I got the error `expected required property account to be present` and the location attribute is: `body`. After...

- **#2085: V2 Accounts**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-07-14
  > ### Describe the bug  Where can I fine V2 accounts functionality?  The changelog entry for 82.1.0 specifies:  ``` Services are all version-namespaced for symmetry. E.g. stripeClient.V1Accounts and str...

- **#1205: Parse unix timestamps into times (time.Time)**
  - Labels: future
  - Comments: 4
  - Last updated: 2025-06-18
  > It'd be nice to parse timestamps into their time.Time during unmarshaling. I'd expect most people will be operating with the values as times (could be wrong) so most people are having to do `time.Unix...

- **#2075: Missing `PaymentIntent` property in `Invoice` struct.**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-06-06
  > ### Describe the bug  I am trying to load some information from the Invoice and issue refunds for a few of them but i have noticed the latest version of SDK is missing the `PaymentIntent` property in...

- **#2072: noncompliant not represented as a DisputeReason**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-06-04
  > ### Describe the bug  Hey folks, I've spotted that the dispute reason of `noncompliant` is not represented in your Go SDK but it is a valid API response https://docs.stripe.com/disputes/categories?dis...

- **#1647: Proposal to return `nil` pointers instead of structs on request error**
  - Labels: future, proposal, feature-request
  - Comments: 2
  - Last updated: 2025-04-15
  > ### Is your feature request related to a problem? Please describe.  This feature request is to track community interest in stripe-go API calls returning a `nil` pointer when the error is not `nil`....

- **#2021: CheckoutSession billing dates on api 2025-03-31.basil**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-04-09
  > ### Describe the bug  I'm in the process of integrating with stripe and I had everything working how I want until I upgraded to the latest api `2025-03-31.basil` with go package v82.  The issue I'm se...

- **#2016: Support to display tax breakdown for Payment Intents**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-04-08
  > ### Describe the bug  We are creating a payment intent in Stripe and sending the total amount (including GST). While the payment intent is successfully created, we need to display the tax breakdown in...

- **#1993: Subscription schedule update received unknown parameter: start_date**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-03-08
  > ### Describe the bug  Regardless where the `StartDate` is set (ref: https://github.com/stripe/stripe-go/issues/1883), the subscription schedules cannot be updated when the parameter is present. When t...

- **#1804: Billing quickstart contains invalid code**
  - Labels: support
  - Comments: 2
  - Last updated: 2025-03-01
  > ### Describe the bug  The billing quickstart Go example code calls `.Front` which does not exist in this library:   https://stripe.com/docs/billing/quickstart   ```     i := price.List(params)...

- **#1990: InvoiceParams missing SubscriptionItems and SubscriptionProrationDate fields**
  - Labels: feature-request
  - Comments: 0
  - Last updated: 2025-02-28
  > ### Is your feature request related to a problem? Please describe.  According to [documentation](https://docs.stripe.com/billing/subscriptions/prorations#preview-proration) the `InvoiceParams` struct...

- **#1978: Newly added `Jpy` variable name is not ALL CAPS**
  - Labels: feature-request
  - Comments: 2
  - Last updated: 2025-02-03
  > ### Is your feature request related to a problem? Please describe.  I don't see OpenAPI or source, but this is part of generated file.  Newly added `Jpy` and existing `Pln` variable names are not ALL...

- **#1556: Provide a strongly-typed way of clearing fields on update**
  - Labels: future, feature-request
  - Comments: 3
  - Last updated: 2025-01-29
  > ### Is your feature request related to a problem? Please describe.  I asked to support developers on Discord about how to disable the billing threshold from the SubscriptionSchedulePhaseItemParams str...

- **#1966: `Quantity` field missing from `Subscription` object**
  - Labels: bug
  - Comments: 0
  - Last updated: 2025-01-14
  > --- My bad, please delete ----

- **#1959: Add support for aws partner eventbus "Event Destinations"**
  - Labels: feature-request
  - Comments: 4
  - Last updated: 2024-12-20
  > ### Is your feature request related to a problem? Please describe.  The go api currently does not support setting up and configuring aws partner eventbus "Event Destinations".   ### Describe the solut...

- **#1961: Outdated Link in Docs: Account_object-controller-requirement_collection**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-12-17
  > ### Describe the bug  The SDK contains a couple of references to `[controller.requirement_collection](https://stripe.com/api/accounts/object#account_object-controller-requirement_collection)`. However...

- **#1960: Product Metadata is empty when retrieving from the subscription object**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-12-17
  > ### Describe the bug  Hello,  I tried to retrieve a Metadata that I set on a product from the subscription object.  ![image](https://github.com/user-attachments/assets/b3019c5f-44b2-46c0-af08-719ebe...

- **#1954: Compile Error when attempting to tokenize payment method**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-12-05
  > ### Describe the bug  [This documentation](https://docs.stripe.com/connect/payouts-bank-accounts?bank-account-collection-integration=direct-api&shell=true&api=true&resource=tokens&action=create) is th...

- **#1944: You cannot specify both the (deprecated) .Params.Metadata and .Metadata, for SubscriptionCancelParams**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-10-30
  > ### Describe the bug  I have an error when trying to attach metadata to SubscriptionCancelParams:  > You cannot specify both the (deprecated) .Params.Metadata and .Metadata in SubscriptionCancelPara...

- **#1927: Limit parameter not applied when fetching payment methods**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-10-14
  > ### Describe the bug  I am attempting to list customer payment methods with a limit parameter, but the results continue to return the full list of payment methods. It appears that the limit parameter...

- **#1679: Represent enums on method params**
  - Labels: future, breaking-api-change, feature-request
  - Comments: 3
  - Last updated: 2024-09-14
  > ### Is your feature request related to a problem? Please describe.  _No response_  ### Describe the solution you'd like  In a previous stripe-go version, we had the following enum:  ```go  // Subs...

- **#1894: GetBackendWithConfig overrides the config argument**
  - Labels: bug
  - Comments: 0
  - Last updated: 2024-07-30
  > ### Describe the bug  Currently, [`NewBackendsWithConfig`](https://github.com/stripe/stripe-go/blob/124246af3a3ba52c22b267248c79a115709ee482/stripe.go#L1186-L1192) does not allow a single config wit...

- **#1674: SetupIntentNextActionUseStripeSDK is always empty**
  - Labels: support
  - Comments: 5
  - Last updated: 2024-07-17
  > ### Describe the bug  When a card number required action of SetupIntentNextAction use_stripe_sdk, always is empty field SetupIntentNextActionUseStripeSDK, why?   ### To Reproduce  create setup intent...

- **#1671: Upcoming invoice API bug**
  - Labels: support
  - Comments: 1
  - Last updated: 2024-07-17
  > ### Describe the bug  When changing from an existing subscription to another subscription, the duration of the coupon(e.g. one month)  less than the subscription end period of the upcoming plan(e.g....

- **#1667: Checkout Session Type is Inconsistent with the Typescript Type**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2024-07-17
  > ### Describe the bug  I want to parse a Typescript Checkout Session as part of a migration from Typescript to Go for client work. What I have found is I need to create my own structs that match the...

- **#1681: Plan object missing on Subscription object despite being present in Webhook Event**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2024-07-17
  > ### Describe the bug  In the `customer.subscription.succeeded` event JSON, I see the `plan` object as a top-level attribute.  I want to access this using the Go SDK.  It appears undocumented her...

- **#1686: Make it easier to add subscription schedule phases**
  - Labels: support
  - Comments: 1
  - Last updated: 2024-07-17
  > ### Is your feature request related to a problem? Please describe.  I want to add a phase to an existing subscription schedule, keeping any existing phases as is.  I can easily get the subscription...

- **#1695: Empty refund list in the charge object**
  - Labels: support
  - Comments: 2
  - Last updated: 2024-07-17
  > ### Describe the bug  I'm trying to retrieve the reason for refunded charge in by listening to the `charge.refunded` event, in the event data in the dashboard, I'm able to see the refunds, but in the...

- **#1710: Unable to update shipping rates using `shippingrate.Update()` method.**
  - Labels: support
  - Comments: 2
  - Last updated: 2024-07-17
  > ### Describe the bug  When trying to use the `shippingrate.Update()` method to update a Stripe connect account's shipping rate, it gives the error: ``` [ERROR] Request error from Stripe (status 400)...

- **#1723: Payout object: include `trace_number`**
  - Labels: support
  - Comments: 2
  - Last updated: 2024-07-17
  > ### Is your feature request related to a problem? Please describe.  As a consumer of the stripe-go library, I would like `Payout.trace_number` to be included when querying Stripe for payout data. Th...

- **#1726: Incompatible field type `LatestInvoice` in struct `stripe.Subscription` for webhook events**
  - Labels: support
  - Comments: 2
  - Last updated: 2024-07-17
  > ### Describe the bug  Field `LatestInvoice` from struct `stripe.Subscription` has type `*stripe.Invoice` however the json body in the webhook event comes as a `string`.  Docs says is a `string` as we...

- **#1727: Missing features field in Product struct**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2024-07-17
  > ### Describe the bug  `Product` is missing `features` field.  https://stripe.com/docs/api/products/object#product_object-features  ### To Reproduce  See Describe  ### Expected behavior  ``` type Pr...

- **#1733: Ability to pass multiple status' when fetching subscriptions **
  - Labels: support
  - Comments: 2
  - Last updated: 2024-07-17
  > ### Is your feature request related to a problem? Please describe.  When fetching the subscriptions in my code, I frequently have to fetch subscriptions of different status'. This means making multipl...

- **#1766: Checkout Session is missing the `invoice_creation` field**
  - Labels: support
  - Comments: 1
  - Last updated: 2024-07-17
  > ### Is your feature request related to a problem? Please describe.  When creating the checkout session for one time payment, based on the docs, Stripe doesn't auto generate the invoice. At the moment...

- **#1771: Creating checkout session with metadata not propagating metadata to all events**
  - Labels: support
  - Comments: 2
  - Last updated: 2024-07-17
  > ### Describe the bug  (not sure if it is a bug)  When I create a checkout session with metadata. The "checkout complete" contains the metadata. But the "payment_intent.created" does not  ### To Repr...

- **#1826: Minor typo on wiki for v73 migration**
  - Labels: docs
  - Comments: 1
  - Last updated: 2024-07-17
  > ### Describe the bug  Please excuse me if this is not the correct template 🙇 , but couldn't find an appropriate one I would do a PR but GH and Wiki's PRs 🤷   There's a small typo on https://github....

- **#1842: Custom terms of service don't override auto generated terms of service disclaimer as expected.**
  - Labels: support
  - Comments: 1
  - Last updated: 2024-07-17
  > ### Describe the bug  I'm not able to override the auto-generated terms of service disclaimer below the checkout button, even though [the docs suggest it is possible to override completely](https://do...

- **#1863: Support passing key when create client**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2024-07-17
  > ### Is your feature request related to a problem? Please describe.  I need to use multiple stripe client in one project.  But currently, the `stripe.Key` is a global variable shared in the same proj...

- **#1884: Subscription is incorrectly typed in CheckoutSession**
  - Labels: No labels
  - Comments: 7
  - Last updated: 2024-07-17
  > ### Describe the bug  From `checkout_session.go`:  ``` // The ID of the subscription for Checkout Sessions in `subscription` mode. Subscription *Subscription`json:"subscription"` ``` As the comm...

- **#1887: cancel subscription response no such subscription**
  - Labels: support
  - Comments: 2
  - Last updated: 2024-07-17
  > ### Describe the bug  When I cancel a subscription, has a error: no such subscription version: v79.2.0  ### To Reproduce  ![Snipaste_2024-07-11_14-22-54](https://github.com/stripe/stripe-go/assets/44...

- **#1891: Customer Metadata Search doesn't return results in first attempt**
  - Labels: support
  - Comments: 1
  - Last updated: 2024-07-17
  > ### Describe the bug  I am creating a new Customer object which has a couple of metadata keys as part of an API. When another API tries to search that metadata key right after creation by querying i...

- **#29: Iterator conventions**
  - Labels: No labels
  - Comments: 8
  - Last updated: 2024-07-08
  > Congrats on releasing this package! It looks comprehensive and clean. I have one initial suggestion, if you're interested:  I find the naming convention and behavior for iterators in this package a li...

- **#1883: Misleading field in `SubscriptionSchedulePhaseParams` for POST /v1/subscription_schedules in v78**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-07-02
  > ### Describe the bug  The `StartDate` field should not be present [here](https://github.com/stripe/stripe-go/blob/26539500cc8267f40f25c0c4ff7235fbdeec6ebf/subscriptionschedule.go#L307), it's actuall...

- **#1866: Missing GeneratedFrom property of PaymentMethodCard type**
  - Labels: bug
  - Comments: 4
  - Last updated: 2024-06-03
  > ### Describe the bug  [Official API docs](https://docs.stripe.com/api/payment_methods/object) has it described and cURL response does return card.generated_from property as part of PaymentMethod obj...

- **#1855: Invalid header value Authorization when using Environment variable**
  - Labels: bug
  - Comments: 7
  - Last updated: 2024-04-29
  > ### Describe the bug  I have this scenario, where the log is outputting the correct key, replacing the parameter in `client.New` with the key hardcoded produces a satisfactory response.  ```go 	ssk...

- **#1845: Update payment intent parameters are not correct**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-04-08
  > ### Describe the bug  The parameters struct has `mandate_data` and `confirm` fields, but they are not supported on the update endpoint. There are probably more such fields.  ### To Reproduce  ``...

- **#1193: Create A Mock Test Client**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2024-03-15
  > ## Proposed Feature  After implementing the Golang SDK there could possibly be a better test suite that can be created. For instance the current issue I am having is mocking a response from:  ```g...

- **#1263: Add Level 3 to PaymentIntents**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2024-02-29
  > Providing Level 3 charge data is available via the "Charges" API using the ChargeParams.Level3 field.  However, providing Level 3 data is not available for the "Payment Intents" API.  Can this functio...

- **#1774: PlanProductParams for a new plan of an existing product does not behave like the spec**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-02-15
  > ### Describe the bug  I create a product and then i try to add a new plan for it. I get the error message `Product already exists`. I was expecting no errors and a new plan to be created. Instead i ge...

- **#1807: `recipient_details` for `PaymentIntentPaymentMethodOptionsCardParams`**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2024-01-31
  > ### Is your feature request related to a problem? Please describe.  Hi,  We've been asked by Stripe to populate `recipient_details` for Visa cards payments. [Stripe Go library](https://github.com/...

- **#1794: Custom backend implementation issues with deprecation of `Params.Metadata`**
  - Labels: feature-request
  - Comments: 3
  - Last updated: 2024-01-11
  > ### Is your feature request related to a problem? Please describe.  We use a custom backend for unit tests to add metadata to the objects automatically. Until now, we used this code:  ```go func...

- **#1747: Better api for creating Backends with config**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2023-10-13
  > ### Is your feature request related to a problem? Please describe.  It is very difficult to setup a custom client with your own config for logging. You can set the global default logger but a per clie...

- **#1750: I want to integrate stripe accounts of multiple services into one stripe service, but stripe does not support multiple instances. Why use a global key**
  - Labels: feature-request
  - Comments: 1
  - Last updated: 2023-10-12
  > ### Is your feature request related to a problem? Please describe.  _No response_  ### Describe the solution you'd like  _No response_  ### Describe alternatives you've considered  _No response_  ###...

- **#1734: Files.New is broken**
  - Labels: bug
  - Comments: 3
  - Last updated: 2023-09-13
  > ### Describe the bug  When posting file via stripe-go Files.New we get an error:  Unrecognized request URL (POST: /v1/files). Please see https://stripe.com/docs or we can help at https://support.str...

- **#1728: initUserAgent is slow**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-09-07
  > ### Describe the bug  initUserAgent is relatively slow (100ms) and is run always, even when stripe client is not being used.  https://github.com/stripe/stripe-go/blob/d038ebbf7b3100fb94bfb4ac21874a5...

- **#1698: Upgrading API versions cannot be done cleanly**
  - Labels: feature-request
  - Comments: 4
  - Last updated: 2023-08-02
  > ### Is your feature request related to a problem? Please describe.  The README suggests upgrading to a new major version: > If you are on an older major version, we recommend that you upgrade to the...

- **#1655: Struct 'ChargePaymentMethodDetailsCard' doesn't include 'NetworkToken' event though it is given in webhook events**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-05-11
  > ### Describe the bug  Struct 'ChargePaymentMethodDetailsCard' doesn't include 'NetworkToken' event though it is given in webhook events of checkout sessions, payment intents...  ### To Reproduce  1. a...

- **#1649: PresentPaymentMethod is not exposed **
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-04-27
  > ### Describe the bug  Contrary to the official documentation, the PresentPaymentMethod does not appear to be exposed in terminal/reader/client.go  ### To Reproduce  The API example does not compile...

- **#1650: CheckoutSession.customer unmarshals to *Customer instead of a string (customer id)**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-04-27
  > ### Describe the bug  Hi,  I think there's a problem with the `CheckoutSession.customer` field: ```go type CheckoutSession struct {         ... 	// The ID of the customer for this Session. 	//...

