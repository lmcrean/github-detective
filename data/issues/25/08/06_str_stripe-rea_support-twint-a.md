issue title: Support TWINT as a payment method
labels: none
comment count: 4
hyperlink: https://github.com/stripe/stripe-react-native/issues/2039
status: open
date opened: 2025-08-06
repo 30d_merge_rate: 34

====

description:
**Is your feature request related to a problem? Please describe.**
I was following the documentation here: https://docs.stripe.com/payments/twint/accept-a-payment?platform=web&ui=direct-api#post-payment-events. But I was not able to use the `confirmPayment` method with `Twint` as an option.

**Describe the solution you'd like**
Allow confirming TWINT payments, ideally opening the app.

**Describe alternatives you've considered**
Using the web version of stripe but it's difficult to make it work in the react native environment.

**Additional context**
Add any other context or screenshots about the feature request here.


===

comment #1 by nebiyuelias1, 2025-08-11, 10:16:07
@porter-stripe was hoping to get more insights about this.

comment #2 by porter-stripe, 2025-08-11, 16:24:02
Hi there, we currently do not support Twint through API bindings. However, we do support it with our Payment Element product.  https://docs.stripe.com/payments/accept-a-payment?platform=react-native

comment #3 by nebiyuelias1, 2025-08-12, 07:45:36
Hi @porter-stripe, thanks for the response. Upon checking with the Payment Element, it didn't support Twint. Maybe it could be the react native stripe version I installed. Due to my current project, I cannot jump to the latest version unfortunately. So I was hoping to figure which version of the sdk added support?

Also, do you think I can make an OS contribution to make stripe available on the react native SDK, was following PRs for other payment wallets. If so, I would appreciate it if you could guide me in the right direction.

comment #4 by nebiyuelias1, 2025-08-12, 07:48:56
@porter-stripe actually after upgrading to `"@stripe/stripe-react-native": "0.38.0"` I'm able to see TWINT in the payment element.
