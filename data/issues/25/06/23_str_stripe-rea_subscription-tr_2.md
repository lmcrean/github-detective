issue title: Subscription trial manages the same way Checkout does
labels: none
comment count: 4
hyperlink: https://github.com/stripe/stripe-react-native/issues/1975
status: open
date opened: 2025-06-23
repo 30d_merge_rate: 34

====

description:
**Is your feature request related to a problem? Please describe.**

We use Stripe to offer a subscription to our customers with a 14 days free trial.   

On our Web App, we use Stripe Checkout to perform subscription and everything is fine, the UX is good and customers understand that there are subscribing to a monthly (or yearly subscription) and they are not charged until the 14 days are passed.

On the React Native App, with stripe-react-native lib, this is more complicated. We couldn't find a way to provide the same UX as Stripe Checkout and customer is getting lost on process, or solution is not viable for us. 

Here is the simple case, a **subscription without free trial**, everything is fine, customer sees the price and pays for it: 
<img src="https://github.com/user-attachments/assets/676c3cb3-4443-4a95-86db-99bfccab278d" width="300">

We are able to perform this render with following code on our NodeJS Backend App: 
```
const subscription = await stripe.subscriptions.create({
      customer: customer.id,
      items: [
        {
          price: 'price_XXX',
        },
      ],
      payment_behavior: 'default_incomplete',
      payment_settings: {save_default_payment_method: 'on_subscription'},
      expand: ['latest_invoice.confirmation_secret'],
    });
```


Now if we want to add a **14 days free trial, we add trial_period_days prop**: 
```
const subscription = await stripe.subscriptions.create({
      customer: customer.id,
      items: [
        {
          price: 'price_XXX',
        },
      ],
      payment_behavior: 'default_incomplete',
      payment_settings: {save_default_payment_method: 'on_subscription'},
      expand: ['latest_invoice.confirmation_secret'],
      trial_period_days: 14, <===========================
    });
```

**Problem:** Since this is a free trial, Stripe considers that payment informations are not required and **automatically validates the subscription**, no paymentIntent is generated. For us this a "churn" issue because I can't imagine customer setting their payment informations after been already subscribed.

This issue has already been mentioned here #1509  and here #1523 .

The solution gave in the previous issues is to ask customer payment informations before subscription and this is where we have a UX problem.

We generate a setupIntent: 
```
const setupIntent = await stripe.setupIntents.create({
      customer: customer.id,
});
```
And this is what we get in React Native App: 

<img src="https://github.com/user-attachments/assets/07d5f877-4c27-446c-8797-44a595d0078f" width="300">
<img src="https://github.com/user-attachments/assets/ba4b87d1-bbd4-484c-9155-ddda45ba5407" width="300">

After customer has set his payment informations we can generate and activate the subscription.    
The problem here is this "Setup" modal where customer has no information about the further price and the free trial. And of course, in Apple Pay, there is this "Pending amount" which can be very scary. I don't see myself subscribe to a "Pending amount" subscription.

Maybe we have not find the right process but we couldn't find a way to perform the same process as Stripe Checkout.

**Describe the solution you'd like**

We would like the same experience as Stripe Checkout in terms of UX: 

These screens are from Stripe Checkout which we are using right now in Web App and React Native App (until we find a better approach).

<img src="https://github.com/user-attachments/assets/8e1a6778-d3d5-4c44-8ebb-c543ea0b0c81" width="300">
<img src="https://github.com/user-attachments/assets/c3a88771-8efc-488a-b982-039eb4973904" width="300">

As you can see, all informations are here, "Start Trial" then "$X.XX per month", same on Apple Pay render. 
We would like to offer the same UX with stripe-react-native, so customer understand what he is subscribing for and everything without leaving the application.

**Describe alternatives you've considered**
Same UX as Stripe Checkout for Subscription with free trial

**Additional context**
/


===

comment #1 by tianzhao-stripe, 2025-06-30, 17:39:31
Hi @Aximem 

Have you tried using a PaymentIntent with setupFutureUsage? You'll be able to charge the user 0$ now and save their paymentMethod for the subscription 

comment #2 by Aximem, 2025-07-01, 07:48:56
Hi @tianzhao-stripe 

I have tried it today but I'm not able to perform what I want, or maybe I'm not doing things correctly.

I tried to generate a paymentIntent (not a subscription), with setup_future_usage as following: 

```
const customer = await stripe.customers.create({email: 'test2@test.test'});
const paymentIntent = await stripe.paymentIntents.create({
    amount: 1299,
    currency: 'usd',
    customer: customer.id,
    setup_future_usage: 'off_session',
    automatic_payment_methods: {
        enabled: true,
    }
});
```

But the result in app is the same as a paymentIntent without setup_future_usage. I mean the Stripe modal is showing the price and user is charged of amount. (even if you see: "This payment successfully set up pm_1RfycDDmJ5jF85u6bvgNBIBy for future off-session payments" in screen 3)

<img src="https://github.com/user-attachments/assets/6d900a2f-174a-4939-a86d-b1133af017e5" width="300">
<img src="https://github.com/user-attachments/assets/8f31423b-158d-4eb3-bac1-c9ebe1a46a4c" width="300">
<img src="https://github.com/user-attachments/assets/f4bc64ac-4190-4f6b-b6a5-1d6f0c479bfb" width="300">

No matter if I use off_session or on_session btw.

I also tried to generate a subscription this time, without trial_period_days else I don't have a paymentIntent generated.  
Then I update the subscription payment intent with setup_future_usage:

```
const subscription = await stripe.subscriptions.create({
    customer: customer.id,
    items: [
      {
        price: 'price_XXX',
      },
    ],
    payment_behavior: 'default_incomplete',
    expand: ['latest_invoice.payment_intent'],
});

const paymentIntentId = (
      (subscription.latest_invoice as Stripe.Invoice)
        ?.payment_intent as Stripe.PaymentIntent
    )?.id;

await stripe.paymentIntents.update(paymentIntentId, {
      setup_future_usage: 'off_session',
});
```
But again, the result is the same, Stripe modal shows the price, no 0$ and of course no "trial mention" since I remove trial_period_days, and user is immediately charged.


comment #3 by davidme-stripe, 2025-07-23, 03:29:34
Hi @Aximem, can you try using the ["Recurring" PaymentRequestType](https://github.com/stripe/stripe-react-native/blob/6efbacf8e423970f83d42cca353245bc61f65ec2/src/types/PlatformPay.ts#L79)? You can then fill out the `RecurringPaymentRequest` fields to get the UI you're looking for in Apple Pay.

We don't have very robust subscriptions support on the mobile Payment Element just yet, but it's something we plan to improve in a future update.

comment #4 by Aximem, 2025-07-23, 07:49:16
Hi @davidme-stripe, Thanks for the tips, I tried Recurring payment type and the render, for Apple Pay, is exactly what I except!

<img src="https://github.com/user-attachments/assets/2e8abcc9-2f80-4064-95f3-ab391e0d3531" width="300">
<img src="https://github.com/user-attachments/assets/65404518-72b2-45c0-a265-c534be25e040" width="300">

Note that I had to use `confirmPlatformPayPayment` instead of `initPaymentSheet` since I ended up on the same bug as #1659 

```
await confirmPlatformPayPayment(clientSecret, {
      applePay: {
        currencyCode: 'USD',
        merchantCountryCode: 'US',
        cartItems: [
          {
            amount: '0',
            paymentType: PaymentType.Recurring,
            label: 'Free trial',
            intervalCount: 14,
            intervalUnit: IntervalUnit.Day,
          },
        ],
        request: {
          billing: {
            paymentType: PaymentType.Recurring,
            intervalCount: 1,
            intervalUnit: IntervalUnit.Month,
            label: 'Subscription Label',
            amount: '12.99$',
            startDate: dayjs().add(14, 'days').unix(),
          },
          description: 'Recurring',
          managementUrl: 'https://www.domain.com',
          type: PaymentRequestType.Recurring,
          trialBilling: {
            amount: '0',
            paymentType: PaymentType.Recurring,
            label: 'Free trial',
            intervalCount: 14,
            intervalUnit: IntervalUnit.Day,
          },
        },
      },
 });
```

But the UI is clear for the customer and corresponds to what we except.   
Should be awesome to get this UI for all kind of payments: Google Pay, Credit Card, PayPal. 
Waiting for the future improvements thanks.
