issue title: CardForm - "Card details not complete" error when coming back to the screen
labels: none
comment count: 2
hyperlink: https://github.com/stripe/stripe-react-native/issues/1999
status: open
date opened: 2025-07-12
repo 30d_merge_rate: 34

====

description:
**Describe the bug**

Hi everyone, I'm using the `CardForm` component in a screen that is shown in a multiple-step flow to allow users to specify their card details. The integration with Stripe is done by using the SetupIntent.


`{stripeErrorCode: null, declineCode: null, localizedMessage: 'Card details not complete', message: 'Card details not complete', type: null, code: 'Failed'}`

The navigation can't be changed, nor can the choice of using the `CardForm` in the project.

**To Reproduce**

1. I have a screen named `CardDetails` that shows the `CardForm` and a "Continue" button at the bottom
```typescript
                       <CardForm
                            placeholders={{
                                number: t('card_number'),
                                cvc: t('cvc'),
                                expiration: t('card_expiry_date_placeholder'),
                            }}
                            defaultValues={{ countryCode: 'US' }}
                            style={styles.cardForm}
                            cardStyle={cardStyle(colors)}
                            onFormComplete={cardDetails => {
                                setCardFormComplete(cardDetails.complete);
                            }}
                        />
```

2. After filling in the `CardForm` data, using the `cardDetails.complete`, the "Continue" button is enabled. When the "Continue" button is clicked, I create the setupIntent, get a new `clientSecret`, call the `confirmSetupIntent`, and pass the client secret like this:
```typescript
const { confirmSetupIntent } = useConfirmSetupIntent();
...
const { setupIntent, error } = await confirmSetupIntent(
            clientSecret,
            {
                paymentMethodType: 'Card',
            },
            {
                setupFutureUsage: 'OffSession',
            },
        );
```
3. When the confirmation is completed, the app navigates automatically to the next screen, named `Confirmation`, that shows a summary of some other user data, plus it has a "Change card details" button to allow the user to change the card details before completing the flow. Clicking on that button opens a new instance of the `CardDetails` screen via `navigate`
4. If the user
    a.  Clicks on "Change card details" and shows a new instance of the `CardDetails` screen
    b.  Doesn't fill in any card data in the new `CardDetails` screen's `CardForm`
    c. **Goes back twice** by pressing the back button and reaching the first instance of the `CardDetails` screen
    d. The `CardForm` on that screen still shows the initial card data that was filled in the very first time
    e. Pressing the "Continue" button on that screen, without changing any value on the `CardForm` instance, shows the "Card details not complete" error, even if the `onFormComplete` contains correct data.

**Expected behavior**
The `CardForm` of the first instance of the `CardDetails` screen should clear itself once the setup is completed successfully, or should allow the user to confirm the `SetupIntent` again with a new `client_secret` and let the user proceed.

**Screenshots**
Unfortunately, I can't provide screenshots.

**Version info:**
 - RN version: 0.78.1
 - Stripe SDK version: 0.49.0

**Additional context**
I tried "resetting" the initial `CardForm` by adding a `key` to it and changing it via `useFocusEffect` when the user goes back to that screen, but it didn't solve the issue.

I checked on open issues and PRs, and discovered that `CardField` offers a `clear` method, while the `CardForm` doesn't.

Would it be possible to add it? Otherwise, would you be able to help with this issue?

Thank you.


===

comment #1 by seanzhang-stripe, 2025-07-15, 01:38:26
Hi @nlasagni Thanks for reaching out.

Can you share with us some screenshots to help understand your flow? Especially the part in Step 4 "The CardForm still shows the initial card data that was filled in the very first time". It's not clear to me why the CardForm showed card data if your customer didn't fill up any in Step 2.

comment #2 by nlasagni, 2025-07-17, 10:09:03
Hi @seanzhang-stripe, unfortunately, I can't provide official screenshots because the feature is under development and can't be shared. It will take some time to create a sample project that replicates the issue. I'll try to create one in the next days. 

In the meantime, to answer your question, I've edited steps 2, 3 and 4 above, since the "Continue" button is enabled only after the user has filled in the card data.

Here's also a summarized flow of the navigation when the error appears:

1. First instance of `CardDetails` screen with `CardForm`, fill in the card details
2. Click on "Continue", navigate to Confirmation
3. Click on "Change card details", navigate to a new instance of `CardDetails` screen with `CardForm`
4. Don't fill in anything and go back twice by pressing the back button, so doing `Card Details -> back to Confirmation -> back to first CardDetails`
5. The first instance of the `CardDetails` screen created at step 1 is shown, and the `CardForm` is still showing the data filled in at step 1
6. Don't change any card details, press "Continue"
7. The "Card details not complete" error is shown

Also, to give more context if useful

- The screens above are showing in a modal bottom sheet stack. 
- Essentially, the whole feature is a multi-step flow about filling in some user personal info and the card details, and confirming or editing the data before proceeding to the final step. 
- Every step is implemented by a separate screen, that can be shown while filling in the data, or when the user want to edit the data before the final confirmation. 
- In each step, the user has the possibility to go back to the previous screen.
- The whole flow is made of around 10 steps, but I focused on just the CardDetails and Confirmation steps to avoid confusion.

Here are some parts of the stack implementation if useful.

```typescript
// AppNavigator.tsx
export default function AppNavigator() {
    ...

    return (
        <>
            <NavigationContainer
                ...
            >
                <Stack.Navigator initialRouteName={initialRouteName} screenOptions={statusBarOptions}>
                    <Stack.Screen
                        name={StackRoutes.CustomFeatureStack}
                        component={CustomFeatureStack}
                        options={() => ({
                            headerShown: false,
                            presentation: 'fullScreenModal',
                            animation: 'slide_from_bottom',
                        })}
                    />
                </Stack.Navigator>
            </NavigationContainer>
            <CustomToast />
        </>
    );
} 

// CustomFeatureStack.tsx
export default function CustomFeatureStack() {
    ...

    return (
        <BottomSheetModalProvider>
            <Stack.Navigator initialRouteName={...}>
                <Stack.Screen
                    name={CustomFeatureStackRoutes.CardDetails}
                    component={CardDetailsScreen} // Has the "Continue" button that shows the ConfirmationScreen
                    ...
                />
                <Stack.Screen
                    name={CustomFeatureStackRoutes.Confirmation} // Has the "Change card details" button that shows a new CardDetailsScreen instance
                    component={ConfirmationScreen}
                    ...
                />
            </Stack.Navigator>
        </BottomSheetModalProvider>
    );
}
```
