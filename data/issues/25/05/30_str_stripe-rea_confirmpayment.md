issue title: confirmPayment not sending full billingDetails and shippingDetails (missing carrier and phone)
labels: none
comment count: 2
hyperlink: https://github.com/stripe/stripe-react-native/issues/1959
status: open
date opened: 2025-05-30
repo 30d_merge_rate: 34

====

description:
Hi Stripe team,

I’m using @stripe/stripe-react-native version ^0.37.2 with React Native 0.72.7, and I’m encountering an issue when calling confirmPayment.

Here is the code snippet where I call confirmPayment:
```
import { confirmPayment } from '@stripe/stripe-react-native';

const params = {
    paymentMethodType: 'Card',
    paymentMethodData: {
      paymentMethodId: 'pm_*********',
      billingDetails: {
        name: 'aaaahajjsjxhzhhdbsbggdgvv bbbahsbsggdgfddf',
        email: 'hezj@163.com',
        phone: '2345623456',
      },
      shippingDetails: {
        name: 'aaaahajjsjxhzhhdbsbggdgvv bbbahsbsggdgfddf',
        phone: '2345623456',
        carrier: 'DoorDash Delivery',
        address: {
          line1: 'xxxxxxx',
          city: 'Rockville',
          state: 'MD',
          postalCode: '20852',
        },
      },
    },
  };

const result = await confirmPayment(clientSecret, params);
```

The strange behavior is:
	•	billingDetails is completely missing from the Stripe Workbench request logs.
	•	shippingDetails appears in the request, but only partially:
	•	The carrier and phone fields are not included in the payload.
	•	The address and name fields are sent correctly.

Questions:
	1.	Is this the expected behavior?
	2.	Should I be using paymentMethodData instead of paymentMethodId if I want billingDetails to be included?
	3.	Why are parts of shippingDetails (like carrier and phone) not being sent?

Let me know if I’m missing something, or if this could be a bug. Any help would be appreciated.

Thanks!

===

comment #1 by porter-stripe, 2025-05-30, 15:49:58
Hi there, can you please try the latest version of the SDK 0.47.1 and see if the issue persists?

comment #2 by hezhengjian, 2025-06-03, 01:53:51
> Hi there, can you please try the latest version of the SDK 0.47.1 and see if the issue persists?

Thanks for the suggestion to upgrade to the latest version of stripe-react-native. I’ve tried upgrading, but unfortunately the issue still persists.

Here are the details after upgrading:
	•	stripe-react-native version: 0.47.1 (previously 0.37.2)
	•	Pod install output:
```
Installing Stripe 24.14.0 (was 23.26.0)
Installing StripeApplePay 24.14.0 (was 23.26.0)
Installing StripeCore 24.14.0 (was 23.26.0)
Installing StripeFinancialConnections 24.14.0 (was 23.26.0)
Installing StripePaymentSheet 24.14.0 (was 23.26.0)
Installing StripePayments 24.14.0 (was 23.26.0)
Installing StripePaymentsUI 24.14.0 (was 23.26.0)
Installing StripeUICore 24.14.0 (was 23.26.0)
Installing stripe-react-native 0.47.1 (was 0.37.2)
```
Here is the request payload I’m passing into confirmPayment:
```
{
  "paymentMethodType": "Card",
  "paymentMethodData": {
    "paymentMethodId": "pm_xxxxxxxxxxxxx",
    "billingDetails": {
      "name": "aaaahajjsjxhzhhdbsbggdgvv bbbahsbsggdgfddf",
      "email": "hezj@163.com",
      "phone": "2345623456"
    }
  }
}
```
However, in Stripe Workbench logs, I still don’t see the billingDetails values reflected. Here is the log from Stripe’s Workbench:
```
{
  "client_secret": "************************************************************",
  "expand": {
    "0": "payment_method"
  },
  "payment_method": "pm_xxxxx",
  "use_stripe_sdk": "true"
}
```
As for shippingDetails, I’ve now included them in the createPaymentIntent backend call instead, so I’m not passing them in the confirmPayment call anymore.

I also noticed that the Stripe API version in use is 2020-08-27. I’m wondering if this could be contributing to the issue (e.g., the billing_details not appearing in logs).

Please let me know if there’s anything I’m missing, or if this might be a known issue with a workaround.

Thanks!
