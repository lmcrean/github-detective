issue title: Billie support
labels: none
comment count: 2
hyperlink: https://github.com/stripe/stripe-react-native/issues/1953
status: open
date opened: 2025-05-28
repo 30d_merge_rate: 34

====

description:
**Is your feature request related to a problem? Please describe.**
We're trying to integrate Billie using the "Direct API" integration in our iOS/Android React Native app.

**Describe the solution you'd like**
I would love for this to work the same way as Klarna does, e.g:

```ts
const result = await confirmPayment(clientSecret, {
  paymentMethodType: 'Billie',
  paymentMethodData: {
    billingDetails: {
      address: { country },
      email
    }
  }
})
```

**Describe alternatives you've considered**
Our alternative at the moment is integrating directly with Billie outside of Stripe, or using Svea which provides a similar service in our region.

**Additional context**
I'm open to creating a pull request to get this moving. We have been stuck in a long process trying to get B2B invoicing delivered to our customer, and this is a high priority for us.


===

comment #1 by porter-stripe, 2025-05-29, 16:17:04
Hi @LinusU feel free to create a pull request, we do accept them! Please see [CONTRIBUTING.md](https://github.com/stripe/stripe-react-native/blob/master/CONTRIBUTING.md).

comment #2 by LinusU, 2025-05-29, 17:51:47
@porter-stripe that's awesome! 🙌 

Here we go https://github.com/stripe/stripe-react-native/pull/1956 🚀 
