issue title: [Feature Request/Bug] Enable Dynamic Cart Updates in Apple Pay via onShippingAddressChange
labels: enhancement
comment count: 2
hyperlink: https://github.com/stripe/stripe-react-native/issues/2001
status: open
date opened: 2025-07-14
repo 30d_merge_rate: 34

====

description:
### **Is your feature request related to a problem? Please describe.**

Yes. The current implementation of the `usePlatformPay` hook in `@stripe/stripe-react-native` prevents a critical e-commerce feature: dynamically calculating taxes and shipping based on the user's address *within* the Apple Pay sheet.

While the `onShippingAddressChange` callback is triggered, any attempt to update the cart's line items via the provided `update()` function fails to produce a visual change in the Apple Pay UI. The user is always asked to confirm the initial, pre-tax amount.

This forces a suboptimal user experience and makes it impossible to present a final, accurate total before payment authorization, which can lead to customer confusion and abandoned carts.

### **Describe the solution you'd like**

We would like the library to fully support the native Apple Pay functionality for real-time cart updates. The ideal flow, which aligns with the current API design, would be:

1.  The `onShippingAddressChange` callback is reliably triggered when the user selects a shipping address.
2.  Inside the callback, after updating the `PaymentIntent` on the backend with the new total, the `update({ cartItems: newItems })` function should successfully and visually update the line items in the Apple Pay sheet.
3.  This would allow the final, accurate total to be displayed to the user for their authorization, creating a seamless and transparent checkout experience.

### **Describe alternatives you've considered**

We have considered several workarounds, but all of them degrade the user experience that Apple Pay is designed to provide:

1.  **Pre-calculating Estimated Taxes:** Showing an estimate based on common locations, which can be inaccurate and lead to confusion.
2.  **Custom Checkout Form:** Building our own address form to be filled out *before* showing the Apple Pay button. This adds friction and defeats the purpose of a quick checkout.
3.  **Displaying a Disclaimer:** Informing the user that the final total will be different after payment. This is not transparent and can feel untrustworthy.

We also noted that the user's address seems to only be available on the `PaymentIntent`'s `paymentMethod.billingDetails.address` property *after* the initial user authorization, which is too late to update the sheet before final confirmation.

### **Additional context**

This limitation appears to be specific to the abstraction level of the React Native SDK, as other platforms have robust support for this feature.

**Platform Comparisons:**

  * **Native iOS:** Apple's native PassKit API fully supports this via the `PKPaymentAuthorizationControllerDelegate`. Its `paymentAuthorizationController(_:didSelectShippingContact:handler:)` method is designed specifically for this real-time update flow.
  * **Stripe on the Web:** Stripe's web-based Elements and Checkout also offer greater flexibility for dynamic updates during the payment process.

This suggests the functionality is supported by both Apple and Stripe, but not fully exposed through the React Native SDK.

**Minimal Reproducible Code:**
```typescript
const PaymentComponent = () => {
  const [calculatedTax, setCalculatedTax] = useState<number>(0);
  const [collectedAddress, setCollectedAddress] = useState<any>(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [paymentResult, setPaymentResult] = useState<string>('');
  
  const PRODUCT_PRICE = 150.00;
  const PRODUCT_SIZE = "M";
  const PRODUCT_NAME = "Example Product";

  const { isPlatformPaySupported } = usePlatformPay();
  const { getPaymentSheetData } = usePayments();
  const getTaxes = useStore((state: any) => state.payments.getTax);

  const startPayment = async () => {
    if (isProcessing) return;
    
    try {
      setIsProcessing(true);
      setPaymentResult('');
      
      const isSupported = await isPlatformPaySupported();
      if (!isSupported) {
        setPaymentResult('Apple Pay is not supported on this device');
        return;
      }

      console.log('Starting Apple Pay flow with 0 tax initially...');

      // Create payment intent with base amount only (no tax initially)
      const { payment_intent } = await getPaymentSheetData(PRODUCT_PRICE);

      console.log('Presenting Apple Pay sheet...');
      
      // Present Apple Pay with 0 tax initially - address will be collected
      const { error, paymentIntent } = await confirmPlatformPayPayment(
        payment_intent,
        {
          applePay: {
            cartItems: [
              {
                label: PRODUCT_NAME + "\nSize: " + PRODUCT_SIZE,
                amount: PRODUCT_PRICE.toFixed(2),
                paymentType: PlatformPay.PaymentType.Immediate,
              },
              {
                label: "Tax",
                amount: "0.00", // Start with 0 tax
                paymentType: PlatformPay.PaymentType.Immediate,
              },
              {
                label: "Shipping",
                amount: "0.00",
                paymentType: PlatformPay.PaymentType.Immediate,
              },
              {
                label: "Total",
                amount: PRODUCT_PRICE.toFixed(2), // Just product price initially
                paymentType: PlatformPay.PaymentType.Immediate,
              },
            ],
            merchantCountryCode: "US",
            currencyCode: "USD",
            shippingType: PlatformPay.ApplePayShippingType.Shipping,
            requiredShippingAddressFields: [
              PlatformPay.ContactField.PostalAddress,
            ],
            requiredBillingContactFields: [
              PlatformPay.ContactField.EmailAddress,
              PlatformPay.ContactField.Name,
            ],
          },
        }
      );

      if (error) {
        console.error('Payment error:', error);
        setPaymentResult(`Payment failed: ${error.message}`);
        return;
      }

      if (paymentIntent) {
        console.log('Payment successful! Now calculating tax based on collected address...');
        
        // Get the address that was collected from Apple Pay
        const billingDetails = paymentIntent.paymentMethod?.billingDetails;
        console.log('Billing details:', billingDetails);
        
        // Try to get address from billing details
        const addressFromApplePay = billingDetails?.address;
        
        let finalTax = 0;
        let finalTotal = PRODUCT_PRICE;
        
        if (addressFromApplePay?.state && addressFromApplePay?.postalCode) {
          console.log('Address collected from Apple Pay:', addressFromApplePay);
          setCollectedAddress(addressFromApplePay);
          
          try {
            // Calculate tax based on the collected address
            const taxAmount = await getTaxes(
              "US",
              addressFromApplePay.state,
              addressFromApplePay.postalCode,
              PRODUCT_PRICE,
            );
            
            finalTax = taxAmount || 0;
            finalTotal = PRODUCT_PRICE + finalTax;
            
            setCalculatedTax(finalTax);
            
            console.log(`Tax calculated: $${finalTax.toFixed(2)}`);
            console.log(`Final total: $${finalTotal.toFixed(2)}`);
          } catch (e: any) {
            console.error("Error calculating tax:", e.message);
            finalTax = 0;
            finalTotal = PRODUCT_PRICE;
          }
        } else {
          console.log('No address collected from Apple Pay, using 0 tax');
          setCalculatedTax(0);
        }
        
        const resultMessage = `Payment Successful!\n\n` +
          `Product: ${PRODUCT_NAME}\n` +
          `Size: ${PRODUCT_SIZE}\n` +
          `Price: $${PRODUCT_PRICE.toFixed(2)}\n` +
          `Tax: $${finalTax.toFixed(2)}\n` +
          `Total: $${finalTotal.toFixed(2)}\n\n` +
          `Email: ${billingDetails?.email || 'N/A'}\n` +
          `Name: ${billingDetails?.name || 'N/A'}\n` +
          `Address: ${addressFromApplePay ? `${addressFromApplePay.city}, ${addressFromApplePay.state} ${addressFromApplePay.postalCode}` : 'Not collected'}\n\n` +
          `Note: Tax calculated after address collection`;
        
        setPaymentResult(resultMessage);
      }
    } catch (e: any) {
      console.error('Payment error:', e);
      setPaymentResult(`Payment failed: ${e.message}`);
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Apple Pay Dynamic Tax Calculation</Text>
      <Text style={styles.subtitle}>Address collected from Apple Pay, then tax calculated</Text>
      
      <View style={styles.productInfo}>
        <Text style={styles.product}>{PRODUCT_NAME}</Text>
        <Text style={styles.size}>Size: {PRODUCT_SIZE}</Text>
        <Text style={styles.price}>Price: ${PRODUCT_PRICE.toFixed(2)}</Text>
        <Text style={styles.tax}>Tax: ${calculatedTax.toFixed(2)}</Text>
        <Text style={styles.total}>
          Total: ${(PRODUCT_PRICE + calculatedTax).toFixed(2)}
        </Text>
      </View>

      {collectedAddress && (
        <View style={styles.addressContainer}>
          <Text style={styles.addressTitle}>Address from Apple Pay:</Text>
          <Text style={styles.address}>
            {collectedAddress.line1 && `${collectedAddress.line1}\n`}
            {collectedAddress.line2 && `${collectedAddress.line2}\n`}
            {collectedAddress.city}, {collectedAddress.state} {collectedAddress.postalCode}
          </Text>
        </View>
      )}

      <View style={styles.flowExplanation}>
        <Text style={styles.flowTitle}>How it works:</Text>
        <Text style={styles.flowText}>
          1. Apple Pay starts with $0 tax{'\n'}
          2. User selects address in Apple Pay{'\n'}
          3. Payment processes with base amount{'\n'}
          4. Tax calculated from collected address{'\n'}
          5. Final amounts displayed to user
        </Text>
      </View>

      <View style={styles.limitation}>
        <Text style={styles.limitationTitle}>Limitation:</Text>
        <Text style={styles.limitationText}>
          Stripe React Native doesn't support real-time tax updates during Apple Pay flow.
          Tax is calculated after address collection.
        </Text>
      </View>

      {paymentResult ? (
        <View style={styles.resultContainer}>
          <Text style={styles.resultTitle}>Payment Result:</Text>
          <Text style={styles.resultText}>{paymentResult}</Text>
        </View>
      ) : null}

      <PlatformPayButton
        type={PlatformPay.ButtonType.Pay}
        onPress={startPayment}
        style={[styles.payButton, isProcessing && styles.payButtonDisabled]}
        disabled={isProcessing}
      />
      
      {isProcessing && (
        <Text style={styles.processingText}>Processing payment...</Text>
      )}
    </View>
  );
};
```

**Environment:**

  * `@stripe/stripe-react-native` version: **"0.46.0"**
  * React Native version: **"0.79.3**
  * iOS version: **18.0**

===

comment #1 by davidme-stripe, 2025-07-21, 20:58:48
Hi, thanks for filing this! We don't currently expose these hooks via React Native — you'd need to wrap a native iOS PaymentSheet integration instead to implement the proper PKPaymentRequest handlers. We'll track adding support for this in a future RN SDK update.

comment #2 by instabuyapp, 2025-07-24, 22:34:49
Thank you for creating such a detailed issue on the topic. Although I am using flutter_stripe (which is based on this library), I am facing the exact same among other problems.

Some of them: the required shipping fields (except the .postalAddress) do not update the contact information in the payment intent. Not to speak about Google Pay, where even enabling required shipping info was a hurdle, and the fact that it does not even have this dynamic update by design…

Even though I did not want that, I accepted that my android app would require a custom address form to calculate shipping beforehand (which as you said introduces friction). Then when started implementing Apple Pay the way I want it, I faced the exact same problem as yourself.

I couldn’t find any other discussions on these topics, so I’d be open and happy to have a chat with anyone who has found a proper workaround or has properly implemented it the way it is supposed to be.
