issue title: PaymentIntent `sdkUuid` is blank after `confirmPaymentIntent` failed
labels: bug
comment count: 0
hyperlink: https://github.com/stripe/stripe-terminal-react-native/issues/978
status: open
date opened: 2025-06-26
repo 30d_merge_rate: 19

====

description:
**Describe the bug**

If the result of `confirmPaymentIntent` has an `error` and a `paymentIntent`, it's not possible to use the `paymentIntent` to retry collecting the payment method because the `sdkUuid` is blank. 

**To Reproduce**

Here is a small React Native component to reproduce the error, assuming the SDK is already initialized.

```tsx
import { PaymentIntentResultType, useStripeTerminal } from "@stripe/stripe-terminal-react-native";
import { useState } from "react";
import { Button, ScrollView, Text, View } from "react-native";

export default function Test() {
  // Assuming the SDK is already initialized
  const { createPaymentIntent, collectPaymentMethod, confirmPaymentIntent } = useStripeTerminal();
  const [createPaymentIntentResult, setCreatePaymentIntentResult] = useState<PaymentIntentResultType>();
  const [collectPaymentMethodResult, setCollectPaymentMethodResult] = useState<PaymentIntentResultType>();
  const [confirmPaymentIntentResult, setConfirmPaymentIntentResult] = useState<PaymentIntentResultType>();
  const [retryCollectPaymentMethodResult, setRetryCollectPaymentMethodResult] = useState<PaymentIntentResultType>();

  async function test() {
    setCreatePaymentIntentResult(undefined);
    setCollectPaymentMethodResult(undefined);
    setConfirmPaymentIntentResult(undefined);
    setRetryCollectPaymentMethodResult(undefined);

    // Create Payment Intent
    const createPaymentIntentResult = await createPaymentIntent({
      amount: 105, // Using special decimal to trigger a failure
      currency: "cad",
    });
    setCreatePaymentIntentResult(createPaymentIntentResult);
    console.log("[DEBUG] createPaymentIntent result", JSON.stringify(createPaymentIntentResult, null, 2));
    if (!createPaymentIntentResult.paymentIntent) return;

    // Collect Payment Method
    const collectPaymentMethodResult = await collectPaymentMethod({
      paymentIntent: createPaymentIntentResult.paymentIntent,
      updatePaymentIntent: true,
    });
    setCollectPaymentMethodResult(collectPaymentMethodResult);
    console.log("[DEBUG] collectPaymentMethod result", JSON.stringify(collectPaymentMethodResult, null, 2));
    if (!collectPaymentMethodResult.paymentIntent) return;

    // Confirm Payment Intent
    const confirmPaymentIntentResult = await confirmPaymentIntent({
      paymentIntent: collectPaymentMethodResult.paymentIntent,
    });
    setConfirmPaymentIntentResult(confirmPaymentIntentResult);
    console.log("[DEBUG] confirmPaymentIntent result", JSON.stringify(confirmPaymentIntentResult, null, 2));
    if (!confirmPaymentIntentResult.paymentIntent) return;

    // Retry Collect Payment Method
    const retryCollectPaymentMethodResult = await collectPaymentMethod({
      paymentIntent: confirmPaymentIntentResult.paymentIntent,
    });
    setRetryCollectPaymentMethodResult(retryCollectPaymentMethodResult);
    console.log("[DEBUG] retryCollectPaymentMethod result", JSON.stringify(retryCollectPaymentMethodResult, null, 2));
  }

  return (
    <ScrollView contentContainerStyle={{ justifyContent: "center", alignItems: "center", padding: 16 }}>
      <Button title="Test" onPress={test} />
      <View style={{ gap: 16 }}>
        <Text>Create Payment Intent Result</Text>
        <Text>{JSON.stringify(createPaymentIntentResult, null, 2)}</Text>
        <Text>Collect Payment Method Result</Text>
        <Text>{JSON.stringify(collectPaymentMethodResult, null, 2)}</Text>
        <Text>Confirm Payment Intent Result</Text>
        <Text>{JSON.stringify(confirmPaymentIntentResult, null, 2)}</Text>
        <Text>Retry Collect Payment Method Result</Text>
        <Text>{JSON.stringify(retryCollectPaymentMethodResult, null, 2)}</Text>
      </View>
    </ScrollView>
  );
}
```

<details><summary>Logs</summary>

```
 (NOBRIDGE) LOG  [DEBUG] createPaymentIntent result {
  "paymentIntent": {
    "paymentMethodOptions": {
      "cardPresent": {
        "surcharge": {
          "maximumAmount": 0,
          "status": "unavailable"
        },
        "requestIncrementalAuthorizationSupport": false,
        "requestPartialAuthorization": "",
        "requestExtendedAuthorization": false
      }
    },
    "paymentMethod": null,
    "sdkUuid": "ac5e4016-d7c2-4a45-998f-88dfa9a9c8a8",
    "statementDescriptorSuffix": null,
    "amountTip": 0,
    "paymentMethodId": null,
    "captureMethod": "manual",
    "statementDescriptor": null,
    "currency": "cad",
    "id": "pi_2ReL2zaWD3IeJDOB1G3eXygn",
    "metadata": {},
    "charges": [],
    "created": "1750964481000",
    "amount": 105,
    "offlineDetails": null,
    "amountDetails": {
      "tip": {
        "amount": null
      }
    },
    "status": "requiresPaymentMethod"
  }
}
 (NOBRIDGE) LOG  [Stripe terminal]: didChangePaymentStatus waitingForInput
 (NOBRIDGE) LOG  [Stripe terminal]: didChangeOfflineStatus {"reader": {"networkStatus": "unknown", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}, "sdk": {"networkStatus": "online", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}}
 (NOBRIDGE) LOG  [Stripe terminal]: didChangeOfflineStatus {"reader": {"networkStatus": "online", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}, "sdk": {"networkStatus": "online", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}}
 (NOBRIDGE) LOG  [Stripe terminal]: didChangeOfflineStatus {"reader": {"networkStatus": "online", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}, "sdk": {"networkStatus": "unknown", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}}
 (NOBRIDGE) LOG  [DEBUG] collectPaymentMethod result {
  "paymentIntent": {
    "paymentMethodOptions": {
      "cardPresent": {
        "surcharge": {
          "maximumAmount": 2,
          "status": "available"
        },
        "requestIncrementalAuthorizationSupport": false,
        "requestPartialAuthorization": "",
        "requestExtendedAuthorization": false
      }
    },
    "paymentMethod": {
      "type": "cardPresent",
      "customer": null,
      "affirmDetails": null,
      "metadata": {},
      "wechatPayDetails": null,
      "interacPresentDetails": null,
      "id": "pm_0ReL31aWD3IeJDOBVxAytPwG",
      "cardPresentDetails": {
        "location": null,
        "preferredLocales": [
          "en"
        ],
        "wallet": {
          "type": null
        },
        "reader": null,
        "description": "Visa Classic",
        "network": null,
        "iin": null,
        "issuer": "Stripe Payments UK Limited",
        "expMonth": 12,
        "generatedCard": null,
        "receiptDetails": {
          "terminalVerificationResult": null,
          "transactionStatusInformation": null,
          "dedicatedFileName": null,
          "cvm": null,
          "applicationCryptogram": null,
          "authorizationResponseCode": null,
          "authorizationCode": null,
          "applicationPreferredName": null,
          "accountType": null
        },
        "funding": "credit",
        "expYear": 2021,
        "last4": "9999",
        "cardholderName": "TEST/STRIPE",
        "emvAuthData": null,
        "country": "US",
        "readMethod": "contactless_emv",
        "brand": "visa"
      }
    },
    "sdkUuid": "ac5e4016-d7c2-4a45-998f-88dfa9a9c8a8",
    "statementDescriptorSuffix": null,
    "amountTip": 0,
    "paymentMethodId": "pm_0ReL31aWD3IeJDOBVxAytPwG",
    "captureMethod": "manual",
    "statementDescriptor": null,
    "currency": "cad",
    "id": "pi_2ReL2zaWD3IeJDOB1G3eXygn",
    "metadata": {},
    "charges": [],
    "created": "1750964481000",
    "amount": 105,
    "offlineDetails": null,
    "amountDetails": null,
    "status": "requiresConfirmation"
  }
}
 (NOBRIDGE) LOG  [Stripe terminal]: didChangePaymentStatus processing
 (NOBRIDGE) LOG  [DEBUG] confirmPaymentIntent result {
  "error": {
    "code": "PAYMENT_ERROR.DECLINED_BY_STRIPE_API",
    "message": "Your card was declined. In testmode, using a physical test card with designated amount ending values produce specific decline responses. See https://stripe.com/docs/terminal/references/testing#physical-test-cards for details."
  },
  "paymentIntent": {
    "paymentMethodOptions": {
      "cardPresent": {
        "surcharge": {
          "maximumAmount": 2,
          "status": "available"
        },
        "requestIncrementalAuthorizationSupport": false,
        "requestPartialAuthorization": "",
        "requestExtendedAuthorization": false
      }
    },
    "paymentMethod": null,
    "sdkUuid": "",
    "statementDescriptorSuffix": null,
    "amountTip": 0,
    "paymentMethodId": null,
    "captureMethod": "manual",
    "statementDescriptor": null,
    "currency": "cad",
    "id": "pi_2ReL2zaWD3IeJDOB1G3eXygn",
    "metadata": {},
    "charges": [
      {
        "paymentMethodDetails": {
          "affirmDetails": null,
          "wechatPayDetails": null,
          "interacPresentDetails": null,
          "type": "cardPresent",
          "cardPresentDetails": {
            "location": null,
            "preferredLocales": [
              "en"
            ],
            "wallet": {
              "type": null
            },
            "reader": null,
            "description": "Visa Classic",
            "network": "visa",
            "iin": null,
            "issuer": "Stripe Payments UK Limited",
            "expMonth": 12,
            "generatedCard": null,
            "receiptDetails": {
              "terminalVerificationResult": "0000000000",
              "transactionStatusInformation": "0000",
              "dedicatedFileName": "A000000003101001",
              "cvm": "approval",
              "applicationCryptogram": "571BB1AE8B51E7F0",
              "authorizationResponseCode": "3035",
              "authorizationCode": "123456",
              "applicationPreferredName": "Stripe Credit",
              "accountType": "credit"
            },
            "funding": "credit",
            "expYear": 2021,
            "last4": "9999",
            "cardholderName": "TEST/STRIPE",
            "emvAuthData": "8A023035",
            "country": "US",
            "readMethod": "contactless_emv",
            "brand": "visa"
          }
        },
        "authorizationCode": "123456",
        "currency": "cad",
        "id": "ch_2ReL2zaWD3IeJDOB1qI6XPLv",
        "status": "failed",
        "description": null,
        "amount": 105
      }
    ],
    "created": "1750964481000",
    "amount": 105,
    "offlineDetails": null,
    "amountDetails": {
      "tip": {
        "amount": null
      }
    },
    "status": "requiresPaymentMethod"
  }
}
 (NOBRIDGE) LOG  [Stripe terminal]: didChangePaymentStatus ready
 (NOBRIDGE) LOG  [DEBUG] retryCollectPaymentMethod result {
  "error": {
    "code": "INTEGRATION_ERROR.INVALID_REQUIRED_PARAMETER",
    "message": "No PaymentIntent was found with the sdkUuid . The PaymentIntent provided must be re-retrieved with retrievePaymentIntent or a new PaymentIntent must be created with createPaymentIntent."
  }
}
 (NOBRIDGE) LOG  [Stripe terminal]: didChangeOfflineStatus {"reader": {"networkStatus": "online", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}, "sdk": {"networkStatus": "online", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}}
 (NOBRIDGE) LOG  [Stripe terminal]: didChangeOfflineStatus {"reader": {"networkStatus": "unknown", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}, "sdk": {"networkStatus": "online", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}}
 (NOBRIDGE) LOG  [Stripe terminal]: didChangeOfflineStatus {"reader": {"networkStatus": "online", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}, "sdk": {"networkStatus": "online", "offlinePaymentAmountsByCurrency": {}, "offlinePaymentsCount": 0}}
```

</details>

**Expected behavior**

I'm expecting to be able to reuse the `paymentIntent` from the return result of `confirmPaymentIntent` when there is an error to try to collect the payment method. 

**Stripe Terminal React Native SDK version**

- `^0.0.1-beta.25`

**Additional context**

I'm using Stripe S700 reader (devkit).




===
