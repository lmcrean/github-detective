issue title: confirmPlatformPayPayment returns "Canceled" error even when payment is not canceled
labels: none
comment count: 4
hyperlink: https://github.com/stripe/stripe-react-native/issues/1970
status: open
date opened: 2025-06-13
repo 30d_merge_rate: 34

====

description:
Hi,

I'm occasionally seeing an issue with the `confirmPlatformPayPayment` function where it returns the following error, even though the user has **not** canceled the payment:

```json
{
  "code": "Canceled",
  "message": "The payment has been canceled",
  "localizedMessage": "The payment has been canceled",
  "declineCode": null,
  "type": null,
  "stripeErrorCode": null
}
```

Here's how I'm using the function:

```ts
await confirmPlatformPayPayment(clientSecret, {
  googlePay: {
    testEnv: ENVIRONMENT !== 'PRODUCTION',
    merchantName: 'XXXXX',
    merchantCountryCode: 'ES',
    currencyCode: 'EUR',
    billingAddressConfig: {
      format: PlatformPay.BillingAddressFormat.Full,
      isPhoneNumberRequired: true,
      isRequired: true,
    },
  },
  applePay: {
    cartItems: [
      {
        label: 'XXXXX',
        amount: `${pending.toFixed(2)}`,
        paymentType: PlatformPay.PaymentType.Immediate,
      },
    ],
    merchantCountryCode: 'ES',
    currencyCode: 'EUR',
  },
});
```

**Package versions:**

* `@stripe/stripe-react-native`: `0.43.0`
* `react-native`: `0.76.9`

**Affected device:**

* iOS 18.5 (latest known occurrence)

Any help or insight into what might be causing this would be greatly appreciated. Thanks!


===

comment #1 by minikdev, 2025-06-17, 06:32:09
CFBR

comment #2 by joyceqin-stripe, 2025-07-02, 22:04:38
Hi @minikdev, I'm sorry to hear that you're encountering issues. Could you provide more steps to reproduce the issue? I was unable to with the information given. I'd also love to point you to our support channel on [our Discord](https://stripe.com/go/developer-chat), where we have engineers ready to help you 24/5. Thank you!

comment #3 by enchorb, 2025-07-11, 16:09:06
I am getting this also on iOS both simulator and physical devices. 

@stripe/stripe-react-native: 0.49.0
react-native: 0.79.5 + New Arch Enabled


comment #4 by davidme-stripe, 2025-07-24, 00:35:53
Hi all! I'm able to reproduce this in our example app, but only when double-clicking the Apple Pay button: This causes `const { paymentIntent, error } = await confirmPlatformPayPayment()` to be called twice, which then causes the second attempt to fail as a cancellation. We may adjust the [example code](https://github.com/stripe/stripe-react-native/pull/2017/files) and error messages to make this a little clearer, but calling the API twice in quick succession will generally fail.

If anyone has noticed this happening without double-calling `confirmPlatformPayPayment` please let me know, and we'll investigate more!
