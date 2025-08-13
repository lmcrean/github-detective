issue title: Changing Terminal Tokens
labels: none
comment count: 5
hyperlink: https://github.com/stripe/stripe-terminal-react-native/issues/982
status: open
date opened: 2025-06-29
repo 30d_merge_rate: 19

====

description:
**Describe the bug**

When the StripeTerminalProvider token is changed from a connected account of type "destination charges" to "direct charges", and vice-versa, the createPaymentIntent fails with:

PAYMENT_ERROR.DECLINED_BY_STRIPE_API You did not provide an API key.

If you hard-restart the application, and re-provide the token, the payment intent creates correctly.
I suspect an issue with the terminal holding the old token.

**To Reproduce**
Steps to reproduce the behavior:

1. Within the same application (you have a `dev-app` with similar logic), select a stripe-connect account to connect to of type "destination charges"
2. Call `initStripe()`
3. Make sure you produce server-side a terminal token scoped to the platform (you)
4. Connect to a taptopay reader
5. Create a payment intent clientside. Make sure you provide a transferDataDestination and applicationFeeAmount (see below for example)
6. Confirm payment completes as expected.
7. Go back to account selection, and select an account of type "direct charges"
8. Call `initStripe()`
9. Make sure you produce server-side a terminal token scoped for the target account (as required for direct charges).
10. Reconnect to reader if required (I tried both reconnecting and not, same outcome)
11. Create a payment intent clientside. Make sure you don't provide a transferDataDestination but applicationFeeAmount (see below for example)
12. Payment intent throw an error.

**Expected behavior**

I can see from the expo logs, few interesting things

1. The terminal token endpoint is called twice during the first connection, only once after the account is changed
2. A new terminal token is indeed requested when changing the account and calling initStripe() again.
3. Also tried doing same as dev-app, calling `clearCachedCredentials` without changes in behavior.

I am expecting the stripe sdk to use the newly produced token.

**Screenshots**

```
const paymentDetails: CreatePaymentIntentParams = {
      amount: currentPaymentAmount,
      currency: "aud",
      ...(stripeChargeType === "destination" && connectAccountId
        ? { transferDataDestination: connectAccountId }
        : {}),
      applicationFeeAmount: [number],
    };
```

**Stripe Terminal React Native SDK version**

- (^0.0.1-beta.23`)
- (^0.0.1-beta.25`)

**Smartphone (please complete the following information):**

- Device: [Pixel 7]
- OS: [Android 15]

**Additional context**
Add any other context about the problem here.


===

comment #1 by billfinn-stripe, 2025-07-11, 20:53:56
Hi there -- if you are changing accounts and/or changing the token provider implementation, can you try calling `clearCachedCredentials` before attempting to collect payments with the new account?

comment #2 by federicobarera2, 2025-07-12, 01:47:32
Hi @billfinn-stripe , thanks for coming back to me. I am afraid we have tried that (see bullet point 3 under expected behavior) . I have followed the same initialisation code you guys have in this repo in the `dev-app`. I can see that when the account changes you are calling `clearCachedCredentials` and then `initStripe`.

In our app we are seeing the error reported above. I can see a new token is requested and generated (with additional logging to make sure we are indeed contacting our server to request a token with the right connected account context), but new payment intents are failing. 

Do you obsereve the same behavior in your dev-app (when switching between a destination and direct charge account)?



comment #3 by billfinn-stripe, 2025-07-15, 20:05:46
Hey @federicobarera2 -- ah, sorry I missed that the first time. The other piece of cached data could be the `onBehalfOf` parameter that you pass to `ConnectTapToPayParams`. Can you try reconnecting and connecting to the tap-to-pay reader without setting an `onBehalfOf` account ID for the second connection (and you also clear cached credentials)?

If that still doesn't work, can you provide a mostly complete example of the code you are using? I know you referenced our `dev-app`, but it would be helpful to have a specific example for us to look at (and also make immutable for the sake of archiving this issue).

comment #4 by federicobarera2, 2025-07-20, 03:26:27
Hi @billfinn-stripe . We are not setting the `onBehalfOf`. I will provide a stripped-down replica asap

comment #5 by federicobarera2, 2025-08-10, 12:41:29
Hi @billfinn-stripe , @xiaoshen-stripe 

EDIT: Sorry for the confusion, editing

**Scenario 1**
If we are changing the reader token from a destination to a direct charges (even clearing the cache). We are getting

> ERROR  Error in StripeTerminalManager::createPaymentIntent {"code": "PAYMENT_ERROR.DECLINED_BY_STRIPE_API", "message": "You did not provide an API key. You need to provide your API key in the Authorization header, using Bearer auth (e.g. 'Authorization: Bearer YOUR_SECRET_KEY'). See https://stripe.com/docs/api#authentication for details, or we can help at https://support.stripe.com/."}

Logs and replica can be found here: https://github.com/federicobarera2/stripe-terminal-repro/blob/no-disconnect/logs_no_disconnect_reader.txt  (no-discconect branch)


**Scenario 2**
If, after changing the token, we disconnect and reconnect the terminal, we see no errors.
However, if an expo update (OTA) is triggered, the `connectReader` hangs indefinetely. During an expo update, the javascript layer reloads, but the reader remains connected. Launching a discover and disconnect operations work, however as mentioned the connect hangs.

> "error": {"code": "NETWORK_ERROR.CONNECTION_TOKEN_PROVIDER_ERROR", "message": "Timed out waiting for connection token"}}

Logs and repro can be found here https://github.com/federicobarera2/stripe-terminal-repro/blob/master/logs.txt (master branch)
