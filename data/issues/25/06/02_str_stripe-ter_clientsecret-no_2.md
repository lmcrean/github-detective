issue title: client_secret not exposed following createPaymentIntent
labels: feature-request
comment count: 2
hyperlink: https://github.com/stripe/stripe-terminal-react-native/issues/957
status: open
date opened: 2025-06-02
repo 30d_merge_rate: 19

====

description:
**Is your feature request related to a problem? Please describe.**
Upon creating a payment intent using the `createPaymentIntent` from the hook `useStripeTerminal` on version `beta.25`, the `client_secret` is not returned as seen on the [`<PaymentIntent.type>`](https://github.com/stripe/stripe-terminal-react-native/blob/1775870dd2a24e5a994be90b4f03a72b0a4bbc4c/src/types/PaymentIntent.ts).

**Describe the solution you'd like**
Could you expose the `client_secret` attribute in the response of the payment intent creation?



===

comment #1 by MattYang-Stripe, 2025-06-18, 07:48:04
Hi @ls-frederic-bouchard, we have merged this PR, and it should be included in the next release beta.26.

comment #2 by ls-frederic-bouchard, 2025-06-18, 15:18:56
@MattYang-Stripe thank you!
