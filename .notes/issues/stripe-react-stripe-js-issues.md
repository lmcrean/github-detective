# Issues for stripe/react-stripe-js

**Total Issues**: 325
**Repository**: https://github.com/stripe/react-stripe-js

**Open Issues**: 4
**Closed Issues**: 321

---

## Issues List (Most Recently Updated First)

- **#603: [BUG]: The `on` method of the `useCheckout()` function is omitted, yet it is utilised in the provided quickstart example**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2025-08-11
  > ### What happened?  While following and copying the code from the [quickstarter](https://docs.stripe.com/checkout/custom/quickstart?lang=node) using Node as the server and React as front-end component...

- **#601: [BUG]: ExpressCheckoutElement onClick doesn't work with latest stripe-js version**
  - Labels: bug, stale
  - Comments: 10
  - Last updated: 2025-08-05
  > ### What happened?  When trying to specify the onClick prop to the `ExpressCheckoutElement` I get the following error,  I've tried downgrading both packages several versions but still have the same is...

- **#596: [BUG]: Auto-focus in "Country" field dropdown after entering CVC on iOS Safari**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-07-29
  > ### What happened?  When entering the 3-digit security code (CVC) in the Stripe Card Element during the payment process on iOS Safari, the Country dropdown field unexpectedly opens right after typing...

- **#569: [BUG]: React 19 global JSX namespace deprecation**
  - Labels: bug
  - Comments: 19
  - Last updated: 2025-07-25
  > ### What happened?  As part of the React 19 release they've deprecated the JSX global namespace, in favour of React.JSX.Element. While y'all aren't explicitly using JSX.Element anywhere, it does it ap...

- **#598: [BUG]: Unable to set background color of additional padding in iframe**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2025-07-21
  > ### What happened?  Hi,  Can we make `EmbeddedCheckout` allow for different background colors to fill the iframe's side padding?  `EmbeddedCheckout` appears to color its extra padding with whatever th...

- **#441: [BUG]:  input.__PrivateStripeElement-input ARIA hidden element must not be focusable or contain focusable elements**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-07-15
  > ### What happened?  When running an accessibility scan on a page that uses the following @stripe/react-stripe-js components `<CardNumberElement>`, `<CardExpiryElement> and `<CardCvcElement>` 3 Serious...

- **#592: [BUG]: 3DS confirmation flow broken with ExpressCheckoutElement**
  - Labels: bug, stale
  - Comments: 3
  - Last updated: 2025-06-26
  > ### What happened?  When using the ExpressCheckoutElement with a card that requires 3D Secure authentication, the Google Pay (or Apple Pay) dialog does not close after completing the authentication. A...

- **#597: [BUG]: Stripe Payment Element Not Loading on iOS WebView (CMZ Mobile App)**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-06-20
  > ### What happened?  We are experiencing an issue with the Stripe Payment Element not loading within our iOS mobile application. Here's a detailed breakdown of the problem:  * We have a webpage where w...

- **#595: [BUG]: My client_secret starts with cs_... instead of sess_... when I'm using Stripe’s Embedded/Custom Checkout (ui_mode: 'custom')**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-06-20
  > ### What happened?  Hi,  I am building an integration using Stripe’s Embedded/Custom Checkout (`ui_mode: 'custom'`). However, my Checkout Session’s `client_secret` still starts with `cs_` instead of `...

- **#594: [BUG]: Hydration Error with Stripe PaymentElement in Next.js**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-06-18
  > ### What happened?  Hi team,  I'm encountering a hydration error when migrating from `CardElement` to `PaymentElement` within my Next.js 15 application (using the App Router). My current setup uses `C...

- **#110: Request: A new Tax ID component**
  - Labels: No labels
  - Comments: 8
  - Last updated: 2025-06-15
  > #### Summary  A Tax ID component identical to the one used in the stripe dashboard.  Including the country selection and validation on the value.   <!-- TODO -->  #### Motivation  Implementin...

- **#591: [BUG]: Stripe Customer Session payment_method_save 'disabled' hides Saved Payment Methods**
  - Labels: bug, stale
  - Comments: 3
  - Last updated: 2025-06-06
  > ### What happened?  We are using the Stripe Payment Element in a React App. We want to save all cards for redisplay, so we are setting `params.payment_method_data.allow_redisplay` to `always` on Creat...

- **#581: [BUG]: Express Checkout Element errors with token_already_used if the user users a card with a failure followed by a card that should be successful**
  - Labels: bug
  - Comments: 9
  - Last updated: 2025-05-27
  > ### What happened?  When using the Express Checkout Element, Stripe is erroring with token_already_used if the user users a card that is declined first and then uses one that should succeed.  **Steps...

- **#587: What's making requests to r.stripe.com?**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-05-14
  > ### What happened?  I am trying to find it in the codebase, but I am unable to.  I keep seeing these requests fail with error:  ``` {error: {message: "Invalid request."}} ```  I am pretty sure it's sa...

- **#572: [NOTICE]: Versioning coming soon to Stripe.js. Pay attention to breaking changes in the next release.**
  - Labels: pinned
  - Comments: 1
  - Last updated: 2025-05-14
  > # The most important thing to know: A new major version of `@stripe/stripe-js` will be released soon that has potentially breaking changes. Please read the release notes and linked documentation caref...

- **#584: [BUG]: The setup_future_usage option does not hide the checkbox**
  - Labels: bug, stale
  - Comments: 5
  - Last updated: 2025-05-13
  > ### What happened?  We have just enabled the setup_future_usage to save automatically the credit card but the checkbox always appears on the element for our webapp.  ![Image](https://github.com/user-a...

- **#580: [BUG]: Accessibility issues with Paypal button from Express Checkout element**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2025-04-25
  > ### What happened?  When focusing the PayPal button, its not properly outlined and the button has a blue border. Also, it is not properly announced, instead of "PayPal" it announces "Entering Paypal f...

- **#586: [BUG]: Invalid createShippingAddressElement() parameter: options.defaultValues is not an accepted parameter.**
  - Labels: bug
  - Comments: 0
  - Last updated: 2025-04-15
  > ### What happened?  Getting this error:   IntegrationError: Invalid createShippingAddressElement() parameter: options.defaultValues is not an accepted parameter.  I'm following the docs: https://docs....

- **#574: [BUG]: Card Element onChange does not work consistently**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2025-04-11
  > ### What happened?  ``` <CardElement     key={clientSecret}     onChange={() => {         //! This only fires on the card number NOT the expiry date or cvc         console.log("onChange")      }}...

- **#570: [BUG]: IntegrationError: Element confirming payment is "expressCheckout", but stripe.confirmPayment() was not called within the "confirm" event. Please call stripe.confirmPayment() in the "confirm" event**
  - Labels: bug, stale
  - Comments: 5
  - Last updated: 2025-04-04
  > ### What happened?  I follow strictly to the guide at https://docs.stripe.com/elements/express-checkout-element/accept-a-payment, included the optional `Create a ConfirmationToken` step, but receive t...

- **#567: [BUG]: Tabbing navigation issue Chrome + VoiceOver ON**
  - Labels: bug, stale
  - Comments: 5
  - Last updated: 2025-03-26
  > ### What happened?  Both `<PaymentElement>` and `<AddressElement>` have a broken behaviour while using Google Chrome + VoiceOver ON when they're both rendered. - This is issue is not happening in neit...

- **#568: [BUG]: 1p focus flickers when using AddressElement and PaymentElement.**
  - Labels: bug, stale
  - Comments: 6
  - Last updated: 2025-03-05
  > ### What happened?  Hello! We spotted an issue w/ the Stripe Element's form controls + FF + 1password. It seems that including both the PaymentElement and AddressElement on the same screen causes 1pas...

- **#566: [feature request]: add metadata property to useCheckout() react hook**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2025-02-25
  > ### What happened?  Retrieving a session object from Stripe it's not supported in any react hook. Can we add it to the useCheckout or create a useSession hook?  ref: https://docs.stripe.com/api/checko...

- **#562: [BUG]: Missing `customerSessionClientSecret` type in the `<Elements />` `options` prop**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2025-02-21
  > ### What happened?  The `customerSessionClientSecret` option in the `options` prop of `<Elements />` has no type definition but the option works if we ignore the missing type error.  ### Environment...

- **#546: [Feature Request]: Provide fallback prop to `CheckoutProvider`**
  - Labels: bug, stale
  - Comments: 5
  - Last updated: 2025-02-14
  > ### What happened?  The `CheckoutProvider` is returning `null` during the prepare phase:  https://github.com/stripe/react-stripe-js/blob/885a0d7d9632e3931caa1762ac775e368850409b/src/components/Check...

- **#547: [BUG]: Incorrect result types**
  - Labels: bug, stale
  - Comments: 5
  - Last updated: 2025-02-14
  > ### What happened?  ```ts const result = await checkout.applyPromotionCode(code); ```  here result is:  ```ts export type StripeCheckoutApplyPromotionCodeResult =   | {type: 'success'; success...

- **#557: [BUG]: `readOnly` option in PaymentElement component when using Tabs layout**
  - Labels: bug, stale
  - Comments: 4
  - Last updated: 2025-02-07
  > ### What happened?  Hello,  When I add the option [readOnly](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-readOnly) in the PaymentElement componen...

- **#558: [BUG]: Accessibility issues with buttons from the Express Checkout Element**
  - Labels: bug, stale
  - Comments: 2
  - Last updated: 2025-02-03
  > ### What happened?  # What happened? On mobile web, right swiping from Express checkout heading, ‘Book with Gpay’ is focused but not announced. On right swiping again it focuses and announces.  Exp...

- **#554: [Question]: Autofill Styling Issue: Card Number Input Becomes Invisible with Autofill Enabled**
  - Labels: bug, stale
  - Comments: 3
  - Last updated: 2025-01-18
  > ### What happened?  I’m experiencing an issue with the Card Number input field when autofill is used. Specifically, the input’s background color changes to white during autofill, causing the text (w...

- **#550: [Question]: How to update the amount with Stripe Elements?**
  - Labels: bug, stale
  - Comments: 4
  - Last updated: 2025-01-18
  > ### What happened?  When using Stripe Elements (and passing the amount server side to get the client secret), is the right way to pass a `key` prop with something like `JSON.stringify(options)` to m...

- **#549: [BUG]: The focus state of the production key CardNumberElement is unstable**
  - Labels: bug, stale
  - Comments: 6
  - Last updated: 2025-01-11
  > ### What happened?  Steps to reproduce: 1、Ensure the latest version of Chrome is installed, then switch to mobile mode. 2、 Here is my reproduction code, and the publishableKey I’m using works fin...

- **#540: [Feature Request] React 19 support**
  - Labels: stale, feature request
  - Comments: 10
  - Last updated: 2025-01-11
  > ### What happened?  After updating NextJS to latest 15.x this package stopped working, because of its peer-dependencies. (see log below) Please add React 19 as a possible peer-dependency.  ``` npm...

- **#561: [FEATURE?]: Update @stripe/stripe-js to 5.4.0 or latest**
  - Labels: bug
  - Comments: 9
  - Last updated: 2025-01-09
  > ### What happened?  Hope this is the right place to put this request but currently cannot use some props such as AddressElement autocomplete / defaultValues options as @stripe/stripe-js in this librar...

- **#548: [BUG]: Intermittent issue with CardElement**
  - Labels: bug, stale
  - Comments: 16
  - Last updated: 2025-01-06
  > ### What happened?  The issue is intermittent. Clients have been reporting this icon in the Credit Card form. <img width="1440" alt="117db7c2-5200-4614-a7a8-be838cddee48" src="https://github.com/u...

- **#543: [BUG]: @stripe/stripe-js version 4.9**
  - Labels: bug, stale
  - Comments: 3
  - Last updated: 2025-01-06
  > ### What happened?  Cannot use newest @stripe/stripe-js version with @stripe/react-stripe-js v2.9.0.   ### Environment  _No response_  ### Reproduction  _No response_

- **#541: [BUG]: PaymentElement onChange triggers only once and doesn't provide country data**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2024-12-28
  > ### What happened?  I want to extract the country field value from the `PaymentElement` on every change.  `<PaymentElement onChange={(e) => console.log(e)} />`  When I select a country from the...

- **#222: PaymentRequestButtonElement triggers missing string field warning**
  - Labels: stale
  - Comments: 5
  - Last updated: 2024-12-22
  > To reproduce add a `PaymentRequestButtonElement` to your component.  Displayed warning in Google Chrome:  ``` Each dictionary in the list "icons" should contain a non-empty UTF8 string field "typ...

- **#535: [BUG]: is the cvv masking issue fixed or not? **
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2024-12-08
  > ### What happened?  keeping the cvv visible while payment can be a major issue as the other person can see it and use it illegally.  ### Environment  _No response_  ### Reproduction  _No response_

- **#534: [BUG]: ExpressCheckoutElement Inconsistent Row Rendering**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2024-12-08
  > ### What happened?  I have the following  ``` <ExpressCheckoutElement       options={{           layout: {               overflow: "never",               maxColumns: 0,           },...

- **#520: [BUG]: Accessibility issues with buttons from the Express Checkout Element**
  - Labels: bug, stale
  - Comments: 3
  - Last updated: 2024-12-08
  > ### What happened?  When focusing the Google Pay button, the outline is not displayed correctly, it only appears at the top & bottom of the component.  Expected behavior: 1. The button should hav...

- **#532: [BUG]: Can not set API version for  ```/v1/payment_methods```**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2024-12-08
  > ### What happened?  I am using  Embedded Form for payment follow: ``` const stripePromise = loadStripe(process.env.STRIPE_KEY, {   apiVersion: process.env.STRIPE_API_VERSION, });  const Check...

- **#545: [help wanted]: I want to remove country selection option from payment element, is there any way to do that in react..?**
  - Labels: bug
  - Comments: 0
  - Last updated: 2024-11-22
  > ### What happened?  Want to remove country selection field form payment element  ### Environment  Chrome  ### Reproduction  _No response_

- **#542: [BUG]: Multibanco Payment is not in type**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-11-22
  > ### What happened?  I was just having Multibanco Payment on my custom payment screen. But typescript says `Property 'confirmMultibancoPayment' does not exist on type 'Stripe'.ts(2339)`  I see docs f...

- **#236: [Accessibility Bug] CardElement aria-hidden component contains focusable elements**
  - Labels: stale
  - Comments: 9
  - Last updated: 2024-11-13
  > Feature request or idea? Consider opening an [API review](https://github.com/stripe/react-stripe-js/tree/master/.github/API_REVIEW.md)!  <!-- React Stripe.js is a thin wrapper around Stripe.js and...

- **#537: Requesting Payment Element support for "hideIcon" option**
  - Labels: enhancement
  - Comments: 1
  - Last updated: 2024-10-18
  > ### What happened?  We would like to be able to hide the card brand logos when using Payment element, as some merchants find the rotating logos to be inconsistent with the store theme, and possibly di...

- **#509: [BUG]: 3d secure 2 error from confirmSetup**
  - Labels: bug, stale
  - Comments: 6
  - Last updated: 2024-09-30
  > ### What happened?  I'm trying to confirm setupIntent using PaymentElement. But especially for certain card information, It produces an error and authentication is failed. What i found out is that,...

- **#530: [BUG]: Can't customise dark mode on EmbeddedCheckoutProvider, EmbeddedCheckout as show in the Checkouts (embedded) docs in NextJs**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2024-09-25
  > ### What happened?  It doesn't mention in the docs on EmbeddedCheckoutProvider, EmbeddedCheckout on how to change their appearance.  my code: ``` const PaymentForm = ({ clientSecret }: { clientSec...

- **#527: [BUG]: EmbeddedChechout doesn't work for connect account**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-09-24
  > ### What happened?  On the backend I'm able to create a checkout session for a connect account and get the `client_secret` . This is my code:   ```js const info = {     ui_mode: 'embedded',...

- **#59: Exposing mockStripe and mockElements for testing purposes**
  - Labels: enhancement, stale
  - Comments: 26
  - Last updated: 2024-09-23
  > Would it be possible to expose your testing mocks as part of your library? It would make it a lot easier to write jest tests for components that implement the useStripe and useElements hooks, since th...

- **#516: [BUG]: 3DS Challenge popup appearing below google pay popup **
  - Labels: bug, stale
  - Comments: 3
  - Last updated: 2024-09-22
  > ### What happened?  When paying with google pay, any 3DS challenge popup appears below the google pay native UI so it cannot be interacted with.  ### Environment  Windows - chrome  ### Reprodu...

- **#524: [BUG]: Crash with "Error: Unknown country code: SD"**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-08-30
  > ### What happened?  When selecting the country "SD" ( Sudan), the following error occurs: "Error: Unknown country code: SD".  ### Environment  Browser: Chromium Engine Version 127.0.6533.73  OS...

- **#526: [BUG]: retrievePaymentIntent doesn't have metadata property**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2024-08-30
  > ### What happened?  Hi,  I'm using latest version of stripe/react-stripe-js  When I call ```retrievePaymentIntent``` method with payment intent client secret, the response doesn't include metadata...

- **#522: Stripe+AliPayment  Next Action url  doesn't work on mobile browser with live mode **
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-08-30
  > ### What happened?  I am integrating with stripe+Alipayment+wechat payment. But it worked on test mode but when I switched it with live mode, the wechat payment didn't work. For Alipayment, it  does...

- **#519: [BUG]: "City" input does not show up when selecting Japan as a country**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-08-20
  > ### What happened?  For some reason, the "City" input does not show up when selecting Japan as the country.  This can be demonstrated in the Address Element docs: https://docs.stripe.com/elements/...

- **#523: [BUG]: **
  - Labels: bug
  - Comments: 0
  - Last updated: 2024-08-14
  > ### What happened?  When selecting the country "SD" ( Sudan), the following error occurs: "Error: Unknown country code: SD".  ### Environment  Browser: Chromium Engine Version 127.0.6533.73 OS: MacOS...

- **#521: [BUG]: Cannot change colorText for Block text**
  - Labels: bug
  - Comments: 4
  - Last updated: 2024-08-12
  > ### What happened?  Currently there is no rule or property available to edit the Block text color, which results in unreadable text for things like the Stripe Link block <img width="499" alt="image"...

- **#514: [BUG]: Autofill with select password managers breaks PaymentElement component**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-08-09
  > ### What happened?  I've noticed that some users are experiencing difficulty when autofilling their card details in the `PaymentElement` component. Once autofilled, the whole component goes blank and...

- **#515: [BUG]: Need to not be able submit a form with Return Key **
  - Labels: bug, stale
  - Comments: 2
  - Last updated: 2024-08-09
  > ### What happened?  I am using stripe CardElement, and when pressing Return key inside it my submit handler is called. But I have a use case here that it must not be possible submit my form with Retur...

- **#377: [BUG]: unhandled wallet account email with trailing whitespaces on PaymentRequest for Apple/Google Pay integration**
  - Labels: bug, pinned
  - Comments: 5
  - Last updated: 2024-08-09
  > ### What happened?  When using `PaymentRequest` to handle [apple/google pay integration](https://stripe.com/docs/stripe-js/elements/payment-request-button), create `payment_method` (`POST` `v1/payment...

- **#517: [BUG]: The "Google Pay" button in ExpressCheckout isn't read correctly by screen readers**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-08-08
  > ### What happened?  As a user using a screen reader, when you navigate through the ExpressCheckout payment options, the Google Pay button is just read as "Frame 0". Apple Pay is read correctly as "A...

- **#518: [BUG]: customerOptions prop on Elements says you need beta permissions but there is no other option. **
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-07-30
  > ### What happened?  The [documentation](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements#save-payment-methods) says that in order to use customer saved payment methods you...

- **#510: [BUG]: Invalid attribute on card number input in terms of accessibility**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-06-28
  > ### What happened?  **Issue** Rendering `<PaymentElement />` from the library renders the card number input inside the payment form. The `input` field for card number created has the attribute `autoc...

- **#511: Declared peer dependency forbids latest version of @stripe/stripe-js@4.0.0**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-06-27
  > ### What happened?  Trying to install latest versions of this and @stripe/stripe-js doesn't work due to the way peer dependency is declared in https://github.com/stripe/react-stripe-js/blob/master/pac...

- **#506: Express checkout apple pay element won't update to a higher price in onShippingAddressChange**
  - Labels: bug
  - Comments: 5
  - Last updated: 2024-06-14
  > ### What happened?  ## Issue I need the shipping address to calculate tax. I listen to onShippingAddressChange, use the address to calculate tax and update the total amount to reflect the increase in...

- **#505: [BUG]: Unable to import useEmbeddedCheckoutContext **
  - Labels: bug
  - Comments: 8
  - Last updated: 2024-06-14
  > ### What happened?  I am trying to unmount the EmbeddedCheckout using the `unmount` function. Checking the code I see there is a hook called `useEmbeddedCheckoutContext` to access to the context . Thi...

- **#65: update "amount" for <PaymentRequestButtonElement /> **
  - Labels: No labels
  - Comments: 9
  - Last updated: 2024-06-13
  > I'm trying to make the "amount" update based on state change.   However, despite the state's value changing correctly, the Payment Request's "amount" remains at the initial value.  Please check ou...

- **#507: [BUG]: Why are secrets exposed in the front end?**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-06-07
  > ### What happened?  I'm not really understanding why "secrets" are handled in this way.  Any user can call/playback/sniff/whatever the /create-intent endpoint and get the "secret".     const res =...

- **#504: Unable to disable express checkout setting address with publishable key**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-06-06
  > ### What happened?  When I use ExpressCheckout, I update the address on the payment intent on the server with the secret key. When I call `stripe.confirmPayment`, it tries to update the address with...

- **#502: [BUG]: googlepay integration in stripe **
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-06-03
  > ### What happened?  stripe version^1.16.5  and it is not showing googlepay , i have activated googlepay in payment methods in stripe so give me solution how can i integrate googlepay in my website thr...

- **#503: Support for stripe-mock to test donations locally**
  - Labels: bug
  - Comments: 0
  - Last updated: 2024-06-03
  > ### What happened?  It would be nice if I could use stripe-mock to test my donations locally, it would require me to be able to change the base url.  ### Environment  _No response_  ### Reproduction...

- **#501: [BUG]: StripeCardElement does not support cards with US issue country but CA post code**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-05-30
  > ### What happened?  Stripe seems to use card issue country to enable/disable entry of letters, spaces or other characters in the zip code field.  If the card issue country uses numeric post codes bu...

- **#492: StripeCardElementOptions - add disabled property to classes**
  - Labels: No labels
  - Comments: 7
  - Last updated: 2024-05-16
  > ### What happened?  Please add a new property `disabled` to `StripeElementClasses` to let me change styles when I change `StripeCardElementOptions` to disabled = true.  Or propagate this disabled...

- **#498: Can i used my own input elements instead stripe elements**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-05-16
  > ### What happened?  how can i validate my card and create token by using my own input elements instead stripe elements  ### Environment  Version 121.0.6167.184  ### Reproduction  _No response_

- **#497: [BUG]: Uncaught SyntaxError: "[object Object]" is not valid JSON**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-05-15
  > ### What happened?  The error is constantly spamming the console when using Elements when they are import from @stripe/react-stripe-js  Steps to reproduce: 1. npx create-next-app --example with-str...

- **#485: [BUG]: Customer retrieved address state value does not match client side <option> value.**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-05-06
  > ### What happened?  ## What Happened  When retrieving a Customer data from the V1 endpoint and using the ReactJS Stripe npm package (`@stripe/react-stripe-js @stripe/stripe-js`), the string `state`...

- **#470: [BUG]: Elements controls with floating labels are rendered incorrectly**
  - Labels: bug, stale
  - Comments: 5
  - Last updated: 2024-05-04
  > ### What happened?  I'm using `<Elements>` in my React app and interested in using floating labels . The problem is that the controls are rendered incorrectly, as can be seen below.  I'm passing the...

- **#496: [BUG]: Test mode API is fetching archived products  -  Live mode is working perfectly**
  - Labels: bug
  - Comments: 6
  - Last updated: 2024-04-30
  > ### What happened?  The issue still persists with NextJS14. It was rendering fine and now it just disappeared so wired...  Stripe API version: ``` apiVersion: '2023-08-16', ```  Stripe test dash...

- **#466: [BUG]: Stripe CardElement is not rendering in Next.js 14 with TypeScript**
  - Labels: bug, stale
  - Comments: 6
  - Last updated: 2024-04-29
  > ### What happened?  Setup Next.js 14 with TypeScript Within Stripe Elements Provider put form In PaymentForm Component elements.getElement("card") or elements.getElement(CardElement) is Null You ca...

- **#495: [BUG]: IntegrationError: Invalid value for stripe.confirmSetup(): elements should have a mounted Payment Element or Express Checkout Element. **
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-04-26
  > ### What happened?  I have developed a form to save payment details for the user.  I'm rendering this form inside a Mui Popup component on my page.  When I try to fill details submit for the first...

- **#491: [BUG]: MerchantDisplayName doesn't work in Stripe Elements**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2024-04-25
  > ### What happened?  I have a marketplace application where customers place orders with merchants. Merchants have connected accounts in Stripe in which they receive their payouts. When a customer place...

- **#296: [BUG]: Elements component can create multiple instances of stripeJs.StripeElements**
  - Labels: bug
  - Comments: 23
  - Last updated: 2024-04-25
  > ### What happened?  [Recent changes](https://github.com/stripe/react-stripe-js/commit/85cccb7ab9aabd023e7b3a6493aabab4f06268ee) to this library have changed [when and how often the `useEffect` which c...

- **#494: It's not possible to get the billing address in shipping mode**
  - Labels: bug
  - Comments: 4
  - Last updated: 2024-04-17
  > ### What happened?  I use AddressElement with shipping mode and PaymentElement. In such case there is Billing is same as shipping information checkbox. When I uncheck it, two fields appear, country...

- **#482: [BUG]: PaymentElement onLoaderStart sometimes fails to fire**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-04-14
  > ### What happened?  Apologies, as it's difficult to create a reproduction since the failure is intermittent; however, we were able to reproduce the issue on our end with repetitive retries. We depend...

- **#477: [BUG]: CardNumberElement onChange did not trigger when copy and paste**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-04-09
  > ### What happened?  When using `<CardNumberElement />`, `onChange` did not trigger on the second copy and paste if the two cards brand are the same.  ### Steps to reproduce 1. Copy and paste test c...

- **#86: Clear CardComponent**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2024-03-28
  > Feature request or idea? Consider opening an [API review](https://github.com/stripe/react-stripe-js/tree/master/.github/API_REVIEW.md)!  <!-- React Stripe.js is a thin wrapper around Stripe.js and...

- **#303: [BUG]: SCA Handle Card Action - Input Field is Disabled **
  - Labels: bug
  - Comments: 4
  - Last updated: 2024-03-13
  > ### What happened?  When an SCA payment is required, I am calling stripe.handleCardAction('clientSecret')  The authentication dialog is appearing as expected. However, the user is unable to type the...

- **#318: [BUG]: Can't focus on 3d secure popup iframe input with mouse cursor**
  - Labels: bug
  - Comments: 5
  - Last updated: 2024-03-13
  > ### What happened?  Can't focus on 3d secure popup iframe input with the mouse cursor. To see the issue, please go to this live app: https://fetchcambs.beezer.com/  After clicking the subscribe butt...

- **#478: Update dependency @stripe/stripe-js to v3**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-03-04
  > ### What happened?  It's still on `^2.2.0` when there is `3.0.6` already out. Our dependency management fails on it. Please do the upgrade.  https://github.com/stripe/stripe-js/releases  ![Screen...

- **#469: [BUG]: Stripe.confirmSetup promise when set with `billingDetails: "never"` does not resolve**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2024-03-03
  > ### What happened?  I am using Payment Elements to allow users to set up new payment methods without paying.  My react component is the following: ``` // ...imports...  export type PropsType =...

- **#447: [BUG]: Canno suppress the `name` field of `Address` element, particularly when using `afterpay_clearpay`**
  - Labels: bug, stale
  - Comments: 17
  - Last updated: 2024-02-27
  > ### What happened?  ![image](https://github.com/stripe/react-stripe-js/assets/115199/b9f92f54-db72-44ff-a919-b715ff81b935)  This is the default form that Stripe presents for Afterpay.  Unfortunately...

- **#472: [BUG]: Cookie without Consent**
  - Labels: bug
  - Comments: 1
  - Last updated: 2024-02-20
  > ### What happened?  Hello! Still about this issue https://github.com/stripe/react-stripe-js/issues/367 I do see a 3rd party cookie being set like in the image (in red):   ![image](https://github....

- **#107: A way of changing `stripeAccount`**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2024-02-10
  > ### Summary  It would be awesome to have a way of changing `stripeAccount` without the need of refreshing the page. Currently setting `stripeAccount` is possible by passing an object with options as...

- **#468: [BUG]: Collect full billing address on a single page checkout**
  - Labels: bug
  - Comments: 2
  - Last updated: 2024-01-26
  > ### What happened?  When using the PaymentElement (specifically a credit card), The billing information only includes country and postal_code. We need to collect full billing address. We've also tried...

- **#465: [BUG]: Element create "payment" does not have applePay object type**
  - Labels: bug, stale
  - Comments: 2
  - Last updated: 2024-01-25
  > ### What happened?  When I enter this code:  const paymentElement = elements.create('payment', { 	applePay: { 		recurringPaymentRequest: { 			paymentDescription: 'My subscription', 			management...

- **#467: [BUG]: in `shipping` mode `PaymentElement` does not collect full billing address, only country and in some countries postal code**
  - Labels: bug
  - Comments: 3
  - Last updated: 2024-01-11
  > ### What happened?  I use the `PaymentElement` and `AddressElement` in `shipping` mode, in which the `AddressElement` collects shipping address, and the `PaymentElement` shows a checkbox if the billin...

- **#167: Is there a way to make CardCvcElement to be displayed with dots (type='password')**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2024-01-03
  > I want to change CVC code from plain number to dots (as password).  I found [an issue ](https://github.com/stripe/react-stripe-elements/issues/328) in old react-stripe-elements repo. > Most online...

- **#457: [BUG]: IntegrationError: You must pass in a clientSecret when calling stripe.confirmPayment()**
  - Labels: bug, stale
  - Comments: 2
  - Last updated: 2023-12-20
  > ### What happened?  Getting bellow error even im passing clientSecret properly.  Uncaught (in promise) IntegrationError: You must pass in a clientSecret when calling stripe.confirmPayment().     at...

- **#114: Typescript error for createPaymentMethod**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2023-12-13
  > ### Summary  ``` const cardElement = elements.getElement(CardElement);  const { error, paymentMethod } = await stripe.createPaymentMethod({     type: "card",     card: cardElement, // type erro...

- **#464: [BUG]: Disable an Input fire stopPropgation() is not a function**
  - Labels: bug
  - Comments: 4
  - Last updated: 2023-11-30
  > ### What happened?  When I disable an input, and I click in the TextField, this trigg an error :  ![image](https://github.com/stripe/react-stripe-js/assets/7886368/784ff7fa-bb47-478b-9bed-b45f216585...

- **#463: [BUG]: AddressElement does not allow to show address line2 without specifying ahead of time the details**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-11-21
  > ### What happened?  The next code ``` <AddressElement         options={{           mode: "billing",           display: {             name: "split",           },                  }}       />...

- **#425: [BUG]: PaymentElement with ExpressCheckoutElement and setup_future_usage parameter**
  - Labels: bug, stale
  - Comments: 8
  - Last updated: 2023-11-17
  > ### What happened?  I have integrated PaymentElement & ExpressCheckoutElement to my ReactJS App but I have an issue. My component structure is below:   ``` <div> <ExpressCheckoutElement  onConf...

- **#456:  Getting an integration error:  elements should have a mounted Payment Element or Express Checkout Element **
  - Labels: bug
  - Comments: 4
  - Last updated: 2023-11-15
  > ### What happened?  I have build an E-commerce web application and I'm trying to integrate a payment gateway using Stripe. when ever I try to submit PaymentElement form, stripe.confirmPayment() is...

- **#455: paymentRequestButton onclick event not working**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-11-14
  > ### What happened?  Hi, I want to check if product option selected or not before payment request send when button onClick. But onClick function not working.  ``` useEffect(() => {   if (stripe) {...

- **#288: [BUG]:  Can't Type OTP When payment with 3DS secure, in modal**
  - Labels: bug
  - Comments: 3
  - Last updated: 2023-10-25
  > ### What happened?  Can't Type in OTP Payment in 3DS Secure, in the payment modal  ### Environment  _No response_  ### Reproduction  _No response_

- **#448: [BUG]: CORS error when using CardElement**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-10-12
  > ### What happened?  <img width="1353" alt="image" src="https://github.com/stripe/react-stripe-js/assets/3676208/210d5650-97cc-420f-af30-a180abcea7d9">   ```shell Access to fetch at 'https://mercha...

- **#307: [BUG]: How to collect user email not documented**
  - Labels: bug
  - Comments: 4
  - Last updated: 2023-10-01
  > ### What happened?  Neither https://stripe.com/docs/stripe-js/react nor https://github.com/stripe/react-stripe-js mention how to collect email or any additional fields.  ### Environment  Chrome  ### R...

- **#445: [BUG]: Unable to programatically dismiss Apple Pay modal**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-09-21
  > ### What happened?  Hi team! Apologies if this is the wrong place to report this one.  We are currently using the ECE to present Apple and Google Pay to our customers. During a checkout flow when...

- **#421: [BUG]: Google Pay wait payment stub appear in wrong moment**
  - Labels: bug, stale
  - Comments: 8
  - Last updated: 2023-09-14
  > ### What happened?  On IOS Google Pay wait payment stub appear in wrong moment when I use `ExpressCheckoutElement` component.  I need to validate my custom fields to click pay button. Now I make it...

- **#423: [BUG]: Conflicting documentation about <Elements>**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-08-22
  > ### What happened?  The docs say  > Render an Elements provider at the root of your React app so that it is available everywhere you need it. > > https://stripe.com/docs/stripe-js/react#elements...

- **#435: [BUG]: Visual bug on dark mode with tailwind**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-08-22
  > ### What happened?  Card details not visible on dark mode with tailwind.  Light mode: ![image](https://github.com/stripe/react-stripe-js/assets/22732118/4d98e4f5-fc7b-40da-859c-a52e263d8fbc)  D...

- **#431: [BUG]: Not Possible to hide Paypal in Express Checkout Element**
  - Labels: bug
  - Comments: 3
  - Last updated: 2023-08-14
  > ### What happened?  I am using the ExpressCheckoutElement and am trying to hide only Paypal, but display GooglePay and ApplePay..   Unfortunately there is no option for that currently.  Or have i...

- **#432: [BUG]: Multiple Element providers interfere with each other**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-08-11
  > ### What happened?  * I have two versions of my checkout screen. * I conditionally show one or the other. While one version is being shown, the other version is removed from the DOM ``` if(condit...

- **#427: [BUG]: React-Native iOS issue but android works fine - **
  - Labels: bug
  - Comments: 0
  - Last updated: 2023-08-09
  > DELETED

- **#428: [BUG]: cant prefill email value for LinkAuthenticationElement**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-08-09
  > ### What happened?  checked everywhere, tried setting value, defaultValue, etc, dont know how i can prefill the email of the user in this LinkAuthenticationElement for react  ### Environment  _No resp...

- **#429: [BUG]: not compatible with @stripe/stripe-js@2.0.0 ?**
  - Labels: bug
  - Comments: 3
  - Last updated: 2023-08-09
  > ### What happened?  The peer dependency indicates those not being compatible (points to `"@stripe/stripe-js": "^1.44.1",`. Is that true or just a matter of updating the peerDependency?  ### Environmen...

- **#426: [BUG]: Not Able to Show Retrived Card in CardElement and CardExpiryElement    **
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-08-03
  > ### What happened?  i am retrieving card details from stripe and i want to show that details in particular elements example expiry date in cardExpiryElement, i have gone through each properties of tha...

- **#414: [BUG]: IntegrationError Apple Pay, Chrome iOS**
  - Labels: bug, stale
  - Comments: 6
  - Last updated: 2023-08-02
  > ### What happened?  After trying to pay by Apple Pay error "Something went wrong. Unable to show Apple Pay. Please choose a different payment method and try again.  I have a checkout page where user...

- **#422: [BUG]: i have an issue with msi implementation**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-07-31
  > ### What happened?  I did setup MSI and enabled installments that are available in my React app <img width="693" alt="Captura de pantalla 2023-07-29 a la(s) 16 37 26" src="https://github.com/stripe/r...

- **#424: [BUG]: Security Vulnerability**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-07-31
  > ### What happened?  When I use stripe elements, it creates Iframe, as part of our security scan from netsparker its been advised that we put a sandbox attribute on the iframe however there is no docum...

- **#420: [BUG]: Stripe form in a dialog => We could not retrieve data from the specified element**
  - Labels: bug
  - Comments: 7
  - Last updated: 2023-07-31
  > ### What happened?  Hi,  I wrapp a card form in a dialog component to change user payment card. This work fine, if the user fill form once, complet this and submit.  To reproduce the problem, o...

- **#405: [BUG]: blocked frame with origin "https://example.com" from accessing frame with origin "https://js.stripe.com"**
  - Labels: bug, stale
  - Comments: 2
  - Last updated: 2023-07-26
  > ### What happened?  We use a basic react stripe integration with react-stripe-js.  Everything works well with chrome & firefox. But with Safari (15.6 & +) stripe iframe creates the following error a...

- **#416: [BUG]: LinkAuthenticationElement placeholder text**
  - Labels: bug, pinned
  - Comments: 2
  - Last updated: 2023-07-25
  > ### What happened?  The `LinkAuthenticationElement ` doesn't have any placeholder value, and cannot set through props  ![image](https://github.com/stripe/react-stripe-js/assets/93682696/467e3729-2...

- **#411: [BUG]: hsl support in appearance rules**
  - Labels: bug
  - Comments: 7
  - Last updated: 2023-07-23
  > ### What happened?  I'm trying to use some brand colors in the Stripe Elements Appearance values. We store all of those colors as `hsl()` in a totally normal CSS color value format ( `hsl(227.37deg 12...

- **#418: [BUG]: Using "locale" prints a warning**
  - Labels: bug
  - Comments: 4
  - Last updated: 2023-07-14
  > ### What happened?  When the elements options has "locale" a warning is printed.  ```jsx <Elements stripe={stripe} options={{ locale: "en", ... }}> ... </Elements> ```  The above used to wor...

- **#417: [BUG]: ExpressCheckout - onShippingRateChange, inconsistent event structure.**
  - Labels: bug
  - Comments: 7
  - Last updated: 2023-07-13
  > ### What happened?  _Fully appreciate that the Express Checkout is still in beta, but thought this was worth mentioning._  I'm running a function via the onShippingRateChange prop on the ExpressChec...

- **#364: [Enhancement]: Please add official support for Vue JS**
  - Labels: bug, stale, feature request
  - Comments: 4
  - Last updated: 2023-07-05
  > ### What happened?  The Verified Partner of Stripe for Vue JS is no more maintaining the project, the [@vue-stripe](https://github.com/vue-stripe) is not compatible with newer versions of VueJS. Pleas...

- **#415: [BUG]: Autocompleted Addresses Not Populating Accurately **
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-07-03
  > ### What happened?  When filling out AddressElement some auto completions do not get populated accurately when selected.  For example the address api successfully finds and completes this address:...

- **#407: [BUG]: TypeError: Network request failed**
  - Labels: bug
  - Comments: 3
  - Last updated: 2023-06-26
  > ### What happened?  import React, { useState } from 'react'; import { View, Text, Button } from 'react-native'; import { CardField, useStripe } from '@stripe/stripe-react-native'; import axios fr...

- **#413: [BUG]: Network request pending causes `stripe.confirmCardPayment` to hang indefinitely**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-06-23
  > ### What happened?  I am running an automated Puppeteer test that utilises `@stripe/stripe-js`. Occasionally, the following resource fails to load `https://js.stripe.com/v3/controller-40ef05cf99ae2bbb...

- **#408: [BUG]: Price Creation / Integer Problem**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-06-16
  > ### What happened?  I'm using this library in combination with Firebase Cloud Functions. I'm passing the following integer to the `stripe.prices.create` API: `7840`  This integer is tabulated by mul...

- **#398: [FEATURE]: Pricing Table Element**
  - Labels: bug
  - Comments: 3
  - Last updated: 2023-06-16
  > ### What happened?  I am trying to customize my pricing table and this using React, but @stripe/react-stripe-js doesn't include a PricingTable element in its API  ### Environment  _No response_  ### R...

- **#404: [BUG]: cannot pre-fill IBAN value in SEPA payments**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-06-16
  > ### What happened?  I'm using IbanElement from '@stripe/react-stripe-js' for initialising SEPA payments. In our case we already have the user's IBAN in our database and we want them to see the IBAN al...

- **#396: [BUG]: POST https://r.stripe.com/0 always returns 400 status code in Cypress**
  - Labels: bug, stale
  - Comments: 5
  - Last updated: 2023-06-16
  > ### What happened?  I'm trying to test payment in my application with Cypress end-to-end testing, but when I redirect to the https://checkout.stripe.com/c/pay/ page, the AJAX calls to POST https://r.s...

- **#402: [BUG]: STYLING**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2023-06-16
  > ### What happened?  Hi, I am trying to style my fontWeight light in my options. It is not working. .Dropdown selector is not also working:    ```     variables: {         colorBackground: '#ED...

- **#394: [BUG]: firefox with uBlock generates a lot of request (always retrying) even after successful payment**
  - Labels: bug, needs more info, stale
  - Comments: 4
  - Last updated: 2023-06-16
  > ### What happened?  When visiting https://stripe.dev/elements-examples/ the page is slowed down because of many requests even after the payment was successful.  ### Environment  Firefox 111.0.1 (64-bi...

- **#403: [BUG]: CardElement complete attribute not properly updated**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2023-06-16
  > ### What happened?  I am still seeing this issue on 1.16.4: https://github.com/stripe/react-stripe-js/issues/185 it was closed as stale, but @bui-stripe said: > Hi! We are aware of this issue and a...

- **#395: [BUG]:  SETUP INTENT DOUBLE CLICK**
  - Labels: bug, stale
  - Comments: 3
  - Last updated: 2023-06-16
  > ### What happened?  I have to call setup intent twice the first time I try to add a payment method for a user that does not have a customer id. We are using the full code implementation, and customer...

- **#406: [BUG]: Express Checkout Element - PayPal**
  - Labels: bug
  - Comments: 5
  - Last updated: 2023-06-05
  > ### What happened?  When attempting to set PayPal payments as authorized and then capture later instead of automatically capturing them we get [this](https://www.paypal-community.com/t5/SDKs/error-wit...

- **#95: Where do add the locale props**
  - Labels: No labels
  - Comments: 7
  - Last updated: 2023-05-12
  > This new version of the React wrapper is excellent although I cannot figure out where to pass the `locale` props.  Tried with `<Elements locale="de" stripe={stripePromise}>` as well as `<CardElement...

- **#399: [BUG]: Unable to load elements on initial load of page (using v2 & v3)**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-05-05
  > ### What happened?  Hello! We are using the `<Elements />` from the react-stripe-js package and we are getting the following error on the first load:   ``` Uncaught (in promise) Error: Invalid pro...

- **#392: [BUG]: Elements options dont match stripe docs**
  - Labels: bug
  - Comments: 3
  - Last updated: 2023-05-04
  > ### What happened?  The [stripe docs detail this use case](https://stripe.com/docs/payments/payment-element/migration?integration-path=one-time&client=react#one-time-update-elements), where the `mod...

- **#397: [Feature]: Expose BIN for CardElement**
  - Labels: question
  - Comments: 1
  - Last updated: 2023-05-03
  > ### What happened?  Hi,  We have a use case where we need to access the user's BIN number for the credit card.  As it's not considered sensible information for PCI Compliance, we would love to kno...

- **#393: [BUG]: createPaymentMethod doesnt return any errors**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-04-05
  > ### What happened?  ``` return await stripe           .createPaymentMethod({             type: 'card',             card: cardElement,             billing_details: {               name: fullNam...

- **#390: [BUG]: `.Input:hover` styles overriding `.Input:focus`**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-03-30
  > ### What happened?  I'm trying to change the appearance of Stripe Elements using the following rules of the [Appearance API](https://stripe.com/docs/elements/appearance-api):  ```ts import { Elemen...

- **#391: [BUG]: Elements options dont match stripe docs**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-03-28
  > https://github.com/stripe/react-stripe-js/issues/392

- **#159: Failed to load stripe.js**
  - Labels: No labels
  - Comments: 12
  - Last updated: 2023-03-21
  > Similar to this: https://github.com/stripe/react-stripe-js/issues/139  This happens frequently in our app. Is this a known issue?

- **#379: [BUG]:  RTL locale is using wrong "direction"**
  - Labels: bug
  - Comments: 3
  - Last updated: 2023-03-11
  > ### What happened?  Hi,  A few issues I noticed when trying to use an RTL locale "he" (Hebrew)  - Alignment is off, even though "he" was specified as the locale, the rendered "direction" is "ltr"....

- **#385: [BUG]: Elements is not reactive**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-03-09
  > ### What happened?  I would like to update the `clientSecret` if a user adds a Coupon Code after the checkout form has been rendered.  I wrote a `StripeWrapper` component that wraps the checkout for...

- **#56: loadStripe is not working with latest version**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2023-03-05
  > I'm following pretty closely to the documentation, and am receiving the following error:  Error: Invalid prop `stripe` supplied to `Elements`. We recommend using the `loadStripe` utility from `@stri...

- **#382: [BUG]: `CardElement` `ZIP` field shows `Postcode` instead of `ZIP`**
  - Labels: bug
  - Comments: 2
  - Last updated: 2023-03-01
  > ### What happened?  We want to use [CardElement](https://stripe.com/docs/payments/card-element) on our payment page, but we see `Postcode` field, which we couldn't change. Is there a way to change it...

- **#367: Stripe cookies set before consent**
  - Labels: bug
  - Comments: 5
  - Last updated: 2023-02-28
  > ### What happened?  I've integrated Stripe into my app and seeing that cookies are always set immediately without, for example, giving my customers the choice of whether they want to pay with Stripe a...

- **#171: Use refs for stripe elements**
  - Labels: No labels
  - Comments: 11
  - Last updated: 2023-02-22
  > Hello,  I have a _hybrid_ form, which has _stripe elements_ and _"vanilla" html inputs_.  I'm trying to validate that my button will **only** submit if all `stripe elements` are filled and validat...

- **#365: [BUG]: LinkAuthenticationElement no longer fires `onChange` event when it is mounted.**
  - Labels: bug
  - Comments: 10
  - Last updated: 2023-02-18
  > ### What happened?  Hi There, I am upgrading from version `1.7.0` to the latest `1.16.1`. We are noticing a difference in behavior with the `LinkAuthenticationElement`. Previously, when this compone...

- **#381: [BUG]: Requires 'unsafe-eval' in Content Security Policy directive**
  - Labels: bug
  - Comments: 4
  - Last updated: 2023-02-02
  > ### What happened?  #380  **As I wrote in the Bug Report** I followed the instructions on how to setup CSP and I correctly set up them. I'm sure about that because in the errors **that I posted** th...

- **#380: [BUG]: Requires 'unsafe-eval' in Content Security Policy directive**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-01-31
  > ### What happened?  I followed the guide on [stripe.com](https://stripe.com/docs/security/guide) to correctly setup CSP but when I'm in production and trying to load the Stripe Elements form I get the...

- **#375: [BUG] [1.16.3]: IntegrationError: Can only create one Element of type card**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-01-18
  > ### What happened?  When including `<CardElement />` using 1.16.3 I get the error `Uncaught IntegrationError: Can only create one Element of type card`.  Rolling back to 1.16.2 fixes this without an...

- **#366: [BUG]: **
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-01-13
  > ### What happened?  When trying to load the PaymentElement i am seeing:  <img width="1141" alt="image" src="https://user-images.githubusercontent.com/2570105/209833787-ca3eb855-1bfa-4b57-8a42-c88a...

- **#371: [BUG]: IntegrationError loaderUi Element didn't mount normally.**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-01-13
  > ### What happened?  While using stripe checkout, we found a unexpected error on:  ```     "@stripe/react-stripe-js": "^1.6.0",     "@stripe/stripe-js": "^1.19.1", ```  Here is the public detail...

- **#374: [BUG]: Test bug**
  - Labels: bug
  - Comments: 0
  - Last updated: 2023-01-12
  > ### What happened?  Validating internal slack integration.  ### Environment  _No response_  ### Reproduction  _No response_

- **#373: [BUG]:IdealBankElement no longer fires onChange event when it is mounted at version 1.16.1**
  - Labels: bug
  - Comments: 1
  - Last updated: 2023-01-11
  > ### What happened?  IdealBankElement no longer fires onChange event when it is mounted at version 1.16.1  ### Environment  _No response_  ### Reproduction  _No response_

- **#188: "Failed to execute 'postMessage' on 'DOMWindow'" with Turbo**
  - Labels: stale
  - Comments: 13
  - Last updated: 2023-01-04
  > NB: this issue is not directly related to React Stripe, but I'm opening it here [as suggested by @sashko-stripe](https://github.com/stripe/react-stripe-elements/issues/98#issuecomment-808459130).  #...

- **#131: Is there a way to change placeholder color on CardElement input focus?**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2023-01-04
  > Hi Guys, Great library!  Thanks for your help!  For our purposes we have a stripe CardElement in which we toggle the background color of the input from transparent to white on focus.  I have things...

- **#362: When load paymentElement component, Uncaught (in promise) TypeError: Failed to retrieve dependencies of service**
  - Labels: bug
  - Comments: 4
  - Last updated: 2022-12-19
  > ### What happened?  When load the PaymentElement component, there is uncaught type error in the production only. This below console error does not happen in the local development environment, but whe...

- **#363: Loading Elements without blocking on a server call**
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-12-15
  > ### What happened?  This is half bug / half question.  The `<Elements>` provider will not render correctly without a clientSecret correctly set (it throws this error: `Uncaught IntegrationError: I...

- **#358: [BUG]: Issue with creating custom prices**
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-12-04
  > ### What happened?  When using a custom price I get an error 500 while attempting to make a subscription.  ``` const price = await stripe.prices.create({       unit_amount: planPrice,       cur...

- **#353: [BUG]: PAY button doesnt works on codesandbox**
  - Labels: bug
  - Comments: 3
  - Last updated: 2022-12-02
  > ### What happened?  Hello, when i open the codesandbox demo and i add my test stripe key. When I type CB test card 4242 4242 4242 4242 01/25 123 and validate by clicking on "Pay" CTA. Nothings appea...

- **#352: [BUG]: React.createContext is not a function**
  - Labels: bug
  - Comments: 3
  - Last updated: 2022-12-02
  > ### What happened?  When using Stripe elements trying to make a subscription form, I get the error `React.createContext is not a function`. I can't find any solution to this anywhere.  The same code...

- **#105: Type definitions for `onBlur` and `onFocus` are incorrect**
  - Labels: No labels
  - Comments: 8
  - Last updated: 2022-12-02
  > https://github.com/stripe/react-stripe-js/blob/master/src/types/index.ts#L18 https://github.com/stripe/react-stripe-js/blob/master/src/types/index.ts#L23  The type definitions do not properly defin...

- **#351: [BUG]: onBlur incorrectly typed**
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-12-02
  > ### What happened?  As mentioned [here](https://github.com/stripe/react-stripe-js/issues/105#issuecomment-1331870851) the onBlur callback is incorrectly typed. An event containing `elementType` of t...

- **#349: [BUG]: Card element displays Link payment method by default.**
  - Labels: bug
  - Comments: 2
  - Last updated: 2022-11-29
  > ### What happened?  We are using Card element to take payments via card. Suddenly it started displaying Link payment methods. We don't want it to get display on our checkout page. I have read stripe d...

- **#311: [BUG]: Typescript error with confirmPayment**
  - Labels: bug, stale
  - Comments: 3
  - Last updated: 2022-11-28
  > ### What happened?  I am running into a typing issue when I am trying to confirm the payment intent when using the payment element. I am mostly following the docs here: https://stripe.com/docs/strip...

- **#343: [BUG]: Apple Pay was use to request a payment, the payment interface was showing however it was immediately closing**
  - Labels: bug
  - Comments: 6
  - Last updated: 2022-11-17
  > ### What happened?  When the Apple Pay was use to request a payment, the payment interface was showing however it was immediately closing without finishing the process... and not event triggering th...

- **#126: How to update a paymentmethod listener for paymentRequest button**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2022-11-14
  > ### Summary We're using a Stripe PaymentRequestButton, and would like to update the purchased product based on a selection on the page.  The docs provide a way of updating the [payment request obje...

- **#340: [BUG]: Apple Pay button doesn't load properly**
  - Labels: bug
  - Comments: 5
  - Last updated: 2022-11-14
  > ### What happened?  Sometimes (4 / 10 tries) apple pay button doesn't load properly for the React component, see image from your example ![image](https://user-images.githubusercontent.com/22882779/199...

- **#130: Error: The paymentRequestButton Element is not available in the current environment.**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2022-11-13
  > <!-- React Stripe.js is a thin wrapper around Stripe.js and Stripe Elements for React. Please only file issues here that you believe represent bugs with React Stripe.js, not Stripe.js itself....

- **#333: Guidance on how to test CardElement interaction**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2022-11-12
  > ### What happened?  We are trying to do the same thing as https://github.com/stripe/react-stripe-js/issues/214: >I am trying to add tests where a user enters credit card numbers. Do you have any exam...

- **#341: [BUG]: Memory leak when calling window.postMessage**
  - Labels: bug
  - Comments: 3
  - Last updated: 2022-11-09
  > ### What happened?  I'm not exactly sure if this originates from react-stripe-js or stripe-js.  **Reproduction steps:**  1. Open this [Codesandbox with a minimal reproduction](https://codesandbox....

- **#325: [BUG]: paymentRequest.abort() doesn't do anything**
  - Labels: bug, stale
  - Comments: 7
  - Last updated: 2022-11-04
  > ### What happened?  I'm working on implementing `PaymentRequestButtonElement` with `stripe.paymentRequest()`. I'm collecting shipping with `requestShipping: true` and have handlers for the `shippingad...

- **#326: [BUG]:  Black Inputs**
  - Labels: bug, stale
  - Comments: 2
  - Last updated: 2022-11-01
  > ### What happened?  For some reason, CardElement inputs have a Black background when resizing the screen...or sometimes even randomly these become black if this element is in a modal or resizable elem...

- **#322: [BUG]: Google Pay button not appearing, 404 error from pay.google.com domain**
  - Labels: bug, stale
  - Comments: 5
  - Last updated: 2022-11-01
  > ### What happened?  I'm having a problem with using the `PaymentRequestButtonElement`, specifically with Google Pay. Apple Pay does appear and works as expected on both macOS and iOS Safari browser....

- **#332: [BUG]: Input field for smaller screens**
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-11-01
  > ### What happened?  Yo. Any way we can fit the entire input box contents for smaller devices? ![image](https://user-images.githubusercontent.com/30643024/195722469-5ac403eb-4f54-4774-90de-91182256735...

- **#315: [BUG]: Issue at ticket Checkout form:: IntegrationError: We could not retrieve data from the specified Element.**
  - Labels: bug, stale
  - Comments: 3
  - Last updated: 2022-10-29
  > ### What happened?  I tried to add validation on the stripe form for empty of invalid form fields but getting an unknow error. Form works fine if I enter the correct data but If I tried to submit for...

- **#334: We could not retrieve data from the specified Element.**
  - Labels: bug
  - Comments: 5
  - Last updated: 2022-10-25
  > ### What happened?  So I am having a complicated issue running a CardElement with a loader. As there is no indication of the Element form being submitted by default, I am trying to use a simple loa...

- **#336: [BUG]: The type Stripe.confirmSetup and Stripe.confirmPayment is not compatible with the documents**
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-10-24
  > ### What happened?  The type `options.redirect?` is not compatible with the documents. Currently the library only allow the type `"always" | undefined`, but it should be `"if_required" | "always" |...

- **#313: [BUG]: Elements not rendering at all after client-side navigation in Next.js**
  - Labels: bug, stale
  - Comments: 5
  - Last updated: 2022-10-19
  > ### What happened?  **TLDR: Stripe Elements is not rendering anything when using client side routing to checkout and gives no errors or clues what is wrong.**  I'm trying to do something that I wo...

- **#328: Typescript error while using createPaymentMethod**
  - Labels: bug
  - Comments: 0
  - Last updated: 2022-10-14
  > ### What happened?  `const { error, paymentMethod } = await stripe!.createPaymentMethod({       type: 'card',       card: elements.getElement(CardElement),  });`   I checked this issue but didn...

- **#329: [BUG]: Google / Apple Pay button doesn't appearing with slow internet**
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-10-13
  > ### What happened?  Problem with using the `PaymentRequestButtonElement` and` createPaymentRequest.canMakePayment()`, for slow internet, from time to time returns `null` and buttons doesn't appears. A...

- **#324: Server side rendering (SSR) support**
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-10-03
  > ### What happened?  Trying to use this library with SSR using [Hypernova](https://github.com/airbnb/hypernova) and getting errors. What would it take to support SSR if it's not a fault of my own?...

- **#123: Need to change the placeholder of the CardElement base on the website language**
  - Labels: No labels
  - Comments: 7
  - Last updated: 2022-09-12
  > ### Summary  I want to change the placeholder of the CardElement based on the language of my website  1h I've been searching on the doc... No info, no example. Then, here on this issue #120 I've...

- **#319: [BUG]: need to show card holder and billing text field in element **
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-09-09
  > ### What happened?  i thought need to add props in stripe Element that can show some text field like cardholder name , billling address......!  ### Environment  _No response_  ### Reproduction  _No re...

- **#316: [BUG]: Uncaught IntegrationError: card Element didn't mount normally. **
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-09-09
  > ### What happened?  I'm getting this Stripe error from our app: "Uncaught IntegrationError: card Element didn't mount normally."   My app is a Web Component, is that not supported? Are there worka...

- **#314: [BUG]: elements.getElement(CardElement) return null**
  - Labels: bug
  - Comments: 2
  - Last updated: 2022-09-09
  > ### What happened?  Hi,  Since few days, the function getElement return null all the time, but before all worked well.  Stripe is well loaded with the Elements wrapper, and the elements object (vi...

- **#317: [BUG]: No tutorials work **
  - Labels: bug
  - Comments: 2
  - Last updated: 2022-08-31
  > ### What happened?  Hi,  On the official website there are examples of how to use [react-stripe-js](https://github.com/stripe/react-stripe-js).  confirmPayment no longer exists on useStripe.....

- **#304: [Not really a bug]: Checkout form takes long to load leading to poor UX**
  - Labels: bug, stale
  - Comments: 10
  - Last updated: 2022-08-11
  > ### What happened?  The standard flow is as follows: 1. Create PaymentIntent on server 2. Get back client secret 3. Use client secret to collect payment details, (as given here https://stripe.com/d...

- **#310: [BUG]: Wechat payment QR code disappears after 3 seconds**
  - Labels: bug
  - Comments: 2
  - Last updated: 2022-08-02
  > ### What happened?  Hi there,  Not sure if this is a bug - whenever I try to do a payment in test mode, using wechat payment, the QR code frame shows up for 3 seconds and then disappears, making i...

- **#306: [BUG]: CardElement submits form its inside of when return key is pressed, even if form submit button is disabled**
  - Labels: bug, wontfix
  - Comments: 1
  - Last updated: 2022-07-07
  > ### What happened?  I have a `CardElement` inside a `form` element. This `form` has an `onSubmit` function and includes a `button` element with `type="submit"` that is sometimes disabled. In a normal...

- **#305: [BUG]: the stripe checkout session isn't appearing **
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-07-05
  > ### What happened?  this is what appears when i redirect to the stripe checkout session ![photo_2022-07-04_12-30-22](https://user-images.githubusercontent.com/64759461/177146091-0542f622-6c14-4802-...

- **#258: Unrecognized create() parameter: appearance is not a recognized parameter.**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2022-07-05
  > I am trying to change the appearance parameter but I see no changes and the following message display on the console 👍   > Unrecognized create() parameter: appearance is not a recognized parameter....

- **#295: [BUG]: Test cards that require 3D Secure authentication doesn't trigger 3d secure modal.**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2022-06-19
  > ### What happened?  Hi I'm trying to integrate stripe payment for an E-commerce website, I'm working with react and node js.  Test cards works fine in test environment, but when i try to use a tes...

- **#302: [BUG]: Can't find variable: PaymentAutofillConfig**
  - Labels: bug
  - Comments: 2
  - Last updated: 2022-06-14
  > ### What happened?  Hi,  We are using the react-stripe-js library to take payments on our web application using the Stripe PaymentIntent API.  We've recently started seeing the following error in...

- **#272: Stripe doesn't works after build to test/staging/prod**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2022-06-13
  > Hi, guys  I have encountered the same issue that was described here https://github.com/stripe/react-stripe-js/issues/173 The guy from issue somehow solved it, but didn't provide the solution can an...

- **#267: className prop changes remove the StripeElement classes from the wrapping DOM node**
  - Labels: stale
  - Comments: 10
  - Last updated: 2022-06-09
  > ### Summary  The `StripeElement` class (and any corresponding `--<state>` sibling class) is removed from the parent dom node when the `className` prop of the component changes after the first render...

- **#300: [BUG]: Card Element doesn't bind to existing Elements provider when using promisified Stripe**
  - Labels: bug
  - Comments: 8
  - Last updated: 2022-06-08
  > ### What happened?  After [upgrading to React Stripe.js](https://github.com/stripe/react-stripe-js/blob/master/docs/migrating.md), we roughly set up our app like this:  ```tsx function StripeWrap...

- **#299: [BUG]: Apple Pay icon disappears on `<PaymentElement>`**
  - Labels: bug
  - Comments: 3
  - Last updated: 2022-06-03
  > ## What happened? While working with the `<PaymentElement>`, my team noticed that the Apple Pay icon disappeared after selecting "Apple Pay " then selecting "Cards". A video demonstrating the issue s...

- **#291: [BUG]: Stripe.js error being thrown in React lifecycle**
  - Labels: bug, stale
  - Comments: 1
  - Last updated: 2022-06-01
  > ### What happened?  ### Summary Recently there was a bug in the Stripe.js API which resulted in the Stripe components, specifically `PaymentElement`, failing to initialize on our site. Anytime the co...

- **#87: Cannot read property 'getElement' of null**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2022-05-19
  > <!-- React Stripe.js is a thin wrapper around Stripe.js and Stripe Elements for React. Please only file issues here that you believe represent bugs with React Stripe.js, not Stripe.js itself.  If...

- **#273: React 18 compatibility**
  - Labels: No labels
  - Comments: 21
  - Last updated: 2022-05-16
  > <!-- React Stripe.js is a thin wrapper around Stripe.js and Stripe Elements for React. Please only file issues here that you believe represent bugs with React Stripe.js, not Stripe.js itself....

- **#246: Stripe Elements confirms the first paymentIntent it receives**
  - Labels: stale
  - Comments: 6
  - Last updated: 2022-05-16
  > ### Summary After a `paymentIntent` `clientSecret` is created and passed to Stripe Elements via `options.clientSecret`, react-stripe.js appears to hold on to that original `paymentIntent` (and along...

- **#278: `canMakePayment` results to `null` for no reason**
  - Labels: stale
  - Comments: 1
  - Last updated: 2022-05-05
  > ### Summary Hi there! Our web application is supposed to handle payments vie Google/Apple Pay. When I use `canMakePayment`, it always results to `null`. I have read all cases when it can lead to `nu...

- **#290: [Stripe Files]: load failure can't catch error**
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-05-05
  > ### What happened?  ![image](https://user-images.githubusercontent.com/4416839/166866032-f67d8ecd-3a75-469b-a5c0-1a0185b7a385.png) How catch this error?  Visitors visit the CVV page, the network is...

- **#281: Example for using Appearance with React Stripe JS?**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2022-05-03
  > ### Summary Hello! I've been having a tough time getting the appearance prop of the options to be accepted by `Elements` and have the style propagate to other react elements. Is there an example of h...

- **#289: [Support]:  PaymentElement feature and PaymentIntent**
  - Labels: bug
  - Comments: 1
  - Last updated: 2022-04-29
  > ### What happened?  I am using PaymentElement component using React 17. When I recharge a customer, I dont want ask card detail to customer. i.e. I want to display all card list that customer used b...

- **#285: [BUG]: Elements component doesn't have children in typescript props definition**
  - Labels: bug
  - Comments: 2
  - Last updated: 2022-04-19
  > ### What happened?  When I try to wrap my App with the Elements provider component. Typescript throw the error :  TS2322: Type '{ children: Element; stripe: Promise<Stripe | null>; }' is not assigna...

- **#286: ChainAlert: new npm maintainer has published version 1.7.2 of package @stripe/react-stripe-js**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2022-04-18
  > Dear [@stripe/react-stripe-js](https://npmjs.com/package/@stripe/react-stripe-js) maintainers, Thank you for your contribution to the open-source community.  We've noticed that [bmathews-stripe](https...

- **#277: Example doesn't seem to work**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2022-04-07
  > <!-- React Stripe.js is a thin wrapper around Stripe.js and Stripe Elements for React. Please only file issues here that you believe represent bugs with React Stripe.js, not Stripe.js itself.  If...

- **#275: PaymentElement has padding issues when using US bank account **
  - Labels: No labels
  - Comments: 2
  - Last updated: 2022-04-06
  > ### Summary  The PaymentElement has padding issues when using `US Bank account` and terms is set to `never`.  When `terms`  is set to `never`:  `<PaymentElement  options={{ terms: { usBankAcco...

- **#136: Card Element input field appears invisible when typing in iOS**
  - Labels: No labels
  - Comments: 11
  - Last updated: 2022-04-01
  > ### Summary  https://stackoverflow.com/questions/57473114/ios-input-field-when-typing-text-is-invisible  My problem is the same as what appears in this stackoverflow issue. The text field appears...

- **#201: Feature Request: Add Typescript Examples**
  - Labels: stale
  - Comments: 2
  - Last updated: 2022-04-01
  > Add alternative typescript files for the examples. Either alongside the `js` files or in a separate folder `/examples-typescript/...`

- **#270: colorTextTerms variable not supported**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2022-03-31
  > When reviewing logs reported by our app using stripe.elements, I noticed the following error:   ``` Using stripe.elements(): invalid variable "colorTextTerms"; "colorTextTerms" is not a supported v...

- **#173: Minified React error #321**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2022-03-31
  > Hi all,  I am currently working on an application and after creating the production build, I get this error stemming from the react-stripe-js module:  ![image](https://user-images.githubuserconten...

- **#254: Refused to frame 'http://localhost:3000/' because it violates the following Content Security Policy directive: "frame-src https:".**
  - Labels: stale
  - Comments: 6
  - Last updated: 2022-03-23
  > Getting this error after I entered all the credit card information. Been stuck with this for a while now

- **#266: Error: Could not find Elements context**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2022-03-23
  > ### Summary I am using       "@stripe/react-stripe-js": "^1.7.0",     "@stripe/stripe-js": "^1.24.0",       with nextjs-12.0.10  it is working fine in development mode but giving this error in p...

- **#265: CSS Variables on ::placeholder**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2022-03-21
  > ### Summary  Cannot pass css color variables to the ::placeholder pseudo element.  There is no way that i know of for dynamically changing the `style` object in the `options` prop so that it re-re...

- **#14: Please add a usage example for Connect**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2022-03-20
  > ### Summary  I'd like to put Connect on a react app but there's no example. The only example is for a swift app  Would it please be possible to add a usage example of react-stripe-js to make a s...

- **#43: Feature request: Render elements while stripe.js is loading, gives a way to handle loading and error states**
  - Labels: enhancement, stale
  - Comments: 9
  - Last updated: 2022-03-19
  > #### Summary  > A brief of the new API, including a code sample. Consider where this feature > would fit into our documentation, and what the updated documentation would > look like.  ```js imp...

- **#256: Not compatible with `React.StrictMode`**
  - Labels: stale
  - Comments: 2
  - Last updated: 2022-03-17
  > ### Summary My application is running on a `React@18-rc`version and was facing some issues with the `Elements` api. The hooks `useStripe` and `useElements` return values were `null` when using `React...

- **#262: Error in console when open stripe session **
  - Labels: No labels
  - Comments: 2
  - Last updated: 2022-03-15
  > ### Summary  macOS 12.0.1, Firefox 97.0.1  <img width="753" alt="image" src="https://user-images.githubusercontent.com/24506752/156720508-6baceaa8-078e-4f39-8a85-cad743614c26.png">  Error 1:  C...

- **#263: Card Element - only takes 3 digits of the CVC number with American Express cards**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2022-03-10
  > ### Summary  Hi Stripe team!  We were trying to implement a payment process with the CardElement component from `react-stripe-js` and we found the next issues:  <img width="866" alt="image" src=...

- **#260: Finalize payments on the server using PaymentElement**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2022-03-07
  > Is it possible to finalize payments on the server using `PaymentElement`? I have researched in the Stripe doc and it seems `PaymentElement` requires to create a `setupIntent` or `paymentIntent` befor...

- **#214: How to enter credit card numbers during test**
  - Labels: stale
  - Comments: 9
  - Last updated: 2022-03-07
  > ### Summary  I am trying to add tests where a user enters credit card numbers. Do you have any examples of this? We are using Jest + React Testing Library.

- **#261: User agent parsing and upcoming Chrome & Firefox versions 100**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2022-03-03
  > ### Summary Chrome and Firefox will both be releasing a 3 digit version of 100 shortly and I wanted to bring up the issue of UA parsing within `react-stripe-js`and the dependency `stripe-js`.  Is the...

- **#249: 3D secure iFrame not opening up because an ancestor violates the following Content Security Policy directive: "frame-ancestors 'none'".**
  - Labels: stale
  - Comments: 7
  - Last updated: 2022-02-27
  > While integrating stripe into our website, ran into the issue of the 3D secure modal showing up for a fraction of a second then disappearing with this message in the console  ``` [Report Only] Refu...

- **#255: Should changing `options.classes` or `options.disabled` initiate XHR `elements.update` calls?**
  - Labels: stale
  - Comments: 1
  - Last updated: 2022-02-27
  > Feature request or idea? Consider opening an [API review](https://github.com/stripe/react-stripe-js/tree/master/.github/API_REVIEW.md)!  ### Summary  This is more of a question of what's expected...

- **#187: CardElement expiry details overlaps on smaller screen **
  - Labels: No labels
  - Comments: 4
  - Last updated: 2022-02-22
  > Feature request or idea? Consider opening an [API review](https://github.com/stripe/react-stripe-js/tree/master/.github/API_REVIEW.md)!  <!-- React Stripe.js is a thin wrapper around Stripe.js and...

- **#253: Add methods to validate bank value for Eps/p24/iDeal**
  - Labels: stale
  - Comments: 4
  - Last updated: 2022-02-21
  > ### Summary  So consider I use iDeal/p24/Eps - all these payment methods require customer to select a bank they are customers of.  for (iDeal) the simple example would be:  ```typescript import...

- **#248: Card Payment renders without style**
  - Labels: stale
  - Comments: 3
  - Last updated: 2022-02-18
  > ### Summary  I try to render   ```   <Elements stripe={stripePromiseEl} options={{}}>     <CheckoutForm />   </Elements> ```  And it only renders the Card Number, Date, and CVV inputs, with...

- **#259: CORS Policy issue with PaymentElement**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2022-02-17
  > I'm facing an issue using the `PaymentElement` from `@stripe/react-stripe-js`.  in my console i can see the issue :  “Access to XMLHttpRequest at ‘https://r.stripe.com/0’ from origin ‘https://js.str...

- **#251: Extracting the IBAN number from a StripeIbanElement**
  - Labels: stale
  - Comments: 1
  - Last updated: 2022-02-15
  > IBANs and BICs are not impacted by PCI DSS compliance. Is there a way to retrieve the IBAN number from a `StripeIbanElement` element?  The on change event handler does not include the IBAN input val...

- **#257: `PaymentElement` background color collides with `color-scheme: dark;`**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2022-02-08
  > ### Summary The `PaymentElement` component should have a `background-color` of `transparent`, but whenever a custom `color-scheme` is defined with `dark`, in my case its on the root level of the DOM,...

- **#247: Unsupported payment methods included in React App(NextJS) when using Payment Elements in India.**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2022-01-21
  > ### Summary This issue is specific to platforms in India and it is occurring in Production/Live code and it can be reproduced as follows: In a React App, follow the steps given here https://stripe.c...

- **#252: onBlur Not triggering for react-stripe elements (NextJS)**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2022-01-20
  > <!-- React Stripe.js is a thin wrapper around Stripe.js and Stripe Elements for React. Please only file issues here that you believe represent bugs with React Stripe.js, not Stripe.js itself.  If...

- **#250: Stripe infinite loop api call (Promise Error)**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2022-01-20
  > Summary:  When i open application, Stripe Api continuously get's called and  app is getting crashed, ![stripe_issue1](https://user-images.githubusercontent.com/70878198/149689008-61fb52b1-068e-4866...

- **#242: [Bug] CardElement postcode requirement true/false display problems**
  - Labels: stale
  - Comments: 7
  - Last updated: 2022-01-18
  > ### Summary  I'm having an issue with the card element and switching the postcode requirement true/false. The postcode field isn't available unless one of the other fields is edited when switching f...

- **#243: [Bug] Not working with react testing library and enzyme**
  - Labels: stale
  - Comments: 1
  - Last updated: 2021-12-28
  > Hi,   we're working with a checkout flow and are seeing that Stripe Elements never gets initialised properly and times out when using these testing libraries. We are mocking certain stripe methods t...

- **#241: Elements not rendering and unexpected postMessage events arriving from js.stripe.com**
  - Labels: stale
  - Comments: 7
  - Last updated: 2021-12-19
  > Feature request or idea? Consider opening an [API review](https://github.com/stripe/react-stripe-js/tree/master/.github/API_REVIEW.md)!  <!-- React Stripe.js is a thin wrapper around Stripe.js and...

- **#231: [Bug] CardElement content extends out of bounds of input element + overlays other elements**
  - Labels: stale
  - Comments: 4
  - Last updated: 2021-12-12
  > ### Summary  The `CardElement` input does not correctly scroll as the user types their card number, and overlays other elements  ### Other information  @stripe/react-stripe-js library version: ^...

- **#244: How can I customize CardElement Form?**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-12-07
  > I search in documentation. But not getting any docs. I need to customize Card Element Form. How Can I customize it. The default `CardElement` show this like image-  ![Screenshot 2021-12-07 221045](h...

- **#240: How to use PaymentElement without PaymentIntent/SetupIntent? Amount is unknown?**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2021-11-16
  > Similar to this here - https://github.com/stripe/react-stripe-js/issues/234 - but I don't know the amount ahead of time, the users enter a custom donation amount, so I cannot create a PaymentIntent, w...

- **#239: No way to pass requiredShippingContactFields to Apple Pay**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-11-11
  > ![image](https://user-images.githubusercontent.com/83773047/141290162-bfd5d3ca-3708-4db3-a005-60257662ae0b.png)  Over the years we've become experts in handling, co-ercing and extra-polating address...

- **#85: Confirm Card Payment with Idempotent key**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2021-11-10
  > Looks like I am unable to confirm the card payment using `confirmCardPayment` method from `useStripe` by passing in an options object with `idempotency_key`. ``` const stripe = useStripe(); stripe....

- **#238: How to open 3Ds modal on createPaymentMethod response**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-11-10
  > I have a scenario where I need to add 3D secure on `stripe.createPaymentMethod` . I'm thinking about implementing 3D secure on `card.three_d_secure_usage.supported` on the response of `stripe.createPa...

- **#237: No demos available **
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-11-08
  > Hello,  please consider adding some live demos, that would help a lot

- **#230: isEqual flawed **
  - Labels: No labels
  - Comments: 5
  - Last updated: 2021-11-04
  > isEqual is flawed. returns false for when object is identical. this causes a console warning related to mutable properties  ![image](https://user-images.githubusercontent.com/83773047/137620889-e74d...

- **#226: PaymentRequestButton IntegrationError: Invalid value for paymentRequest(): total.amount should be a positive amount in the currency's subunit. You specified: 220.00000000000003.**
  - Labels: stale
  - Comments: 5
  - Last updated: 2021-11-04
  > <!-- React Stripe.js is a thin wrapper around Stripe.js and Stripe Elements for React. Please only file issues here that you believe represent bugs with React Stripe.js, not Stripe.js itself.  If...

- **#234: Uncaught IntegrationError[..] with PaymentElement, does not raise for CardElement **
  - Labels: No labels
  - Comments: 3
  - Last updated: 2021-10-29
  > <!-- React Stripe.js is a thin wrapper around Stripe.js and Stripe Elements for React. Please only file issues here that you believe represent bugs with React Stripe.js, not Stripe.js itself.  If...

- **#233: No modify?**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-10-28
  > Just want to confirm there's no modification support of an existing payment method. Kind of crazy considering how popular Stripe is.  https://stripe.com/docs/api/payment_methods/update

- **#227: Not possible to set payment method with Payment Request Button**
  - Labels: stale
  - Comments: 2
  - Last updated: 2021-10-27
  > ### Summary  Hi, I need to display a list of payment methods for a checkout page. The googlePay/applePay button should be displayed at the top of the list, but it should not trigger a payment reques...

- **#232: Question regarding currying the useStripe function**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-10-26
  > So if you go here: https://stripe.com/docs/payments/quickstart and choose the react frontend then go to the CheckoutForm.jsx file you will see on line #9 the follwoing code snipped `const stripe = use...

- **#17: Set hidePostalCode on CardElement not working**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-10-25
  > Example: `<CardElement hidePostalCode />`  It works for me with the legacy react-stripe-elements.

- **#223: Local fonts for card details**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-10-15
  > Local fonts not working. If I use https://fonts.gstatic.com/s/cantarell/v10/B50NF7ZDq37KMUvlO015jKJrPqySLQ.woff2 in url, it's working, but when I download it pass the local path, it is not working So...

- **#229: 3D secure problem**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-10-15
  > I'm using this test card number `4000000000003220`. The card number require 3D secure process.  The detail document is on https://stripe.com/docs/payments/3d-secure.  How can I implement 3D secure p...

- **#172: Stripe CardElement iframe does not load in Playwright test**
  - Labels: stale
  - Comments: 3
  - Last updated: 2021-10-03
  > <!-- React Stripe.js is a thin wrapper around Stripe.js and Stripe Elements for React. Please only file issues here that you believe represent bugs with React Stripe.js, not Stripe.js itself.  If...

- **#224: CardField force focus when it's show up and it's blocking other user interactions.**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-09-30
  > ### Summary I have a form with several actions. It includes making a payment through stripe but when the user scrolls the view and the card field shows up, the user can not do other interactions like...

- **#215: Card type error**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-09-27
  > ### Summary Running https://github.com/stripe/react-stripe-js/blob/master/examples/hooks/2-Split-Card.js in typescript gives  ```/Users/vivekadepu/Desktop/Searce/noQ/noq-webapp/src/Components/Payme...

- **#210: Have an issue with google chrome.**
  - Labels: stale
  - Comments: 2
  - Last updated: 2021-09-15
  > Hi, thank you for your amazing package for stripe.  I develop websites with react native web and I'd like to integrate stripe using this module. But I have an issue with google chrome. ![Screensho...

- **#212: Dropdown rendering depends on the device**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-09-01
  > Hello team. I think it is not a bug but rather a feature. But I want to clarify the behavior is intended.   For bank selection components - which are basically dropdowns, we see they render options...

- **#211: AmEx CVC is not checked correctly.**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-08-31
  > Hi! American Express payment has 4-digit CVC code, but stripe accepts both 3 and 4 digits.  I'm wondering if there are any ways to check CVC length? Thanks.  Link to reproduce: https://codesandbo...

- **#209: Change border color when input is focused?**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-08-20
  > Hey, just wondering if there's a way to:  * Add a border around the input * Change the border color when the input is focused?

- **#207: StripeCardElementChangeEvent's complete is true with an amex card and 3 digit CVC**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-08-15
  > ### Summary  **STEPS**  1. Set up a `<CardElement>` and listen to its `onChange` 2. Enter an AMEX card (for example the test card 378282246310005) 3. Enter a 3 digit CVC  **RESULT**  - The `...

- **#206: Supporting BAC's (UK direct debits)**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-08-05
  > ### Summary  Any plans to support a BAC's (UK direct debit) type element for react?  ### Other information   Currently use Card elements with no issues however getting more and more requests for...

- **#205: [Help] How to determine if payment sheet is showing?**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2021-08-05
  > Feature request or idea? Consider opening an [API review](https://github.com/stripe/react-stripe-js/tree/master/.github/API_REVIEW.md)!  <!-- React Stripe.js is a thin wrapper around Stripe.js and...

- **#199: How to populate saved card values in the stripe element?**
  - Labels: stale
  - Comments: 1
  - Last updated: 2021-07-21
  > Hello,  I have multiple cards store in my browser. Is there a way I can populate my stripe card element with the save card information from the browser or 1Password?  Thanks

- **#198: Save Credit Card info in browser or 1Password**
  - Labels: stale
  - Comments: 1
  - Last updated: 2021-07-18
  > I am using @stripe/react-stripe-js. However, when user enters card details on our website to save it in the profile. No options comes up to save the card details in browser or 1password. Secondly, if...

- **#185: CardElement complete attribute not properly updated**
  - Labels: stale
  - Comments: 3
  - Last updated: 2021-07-13
  > I'm experiencing an issue with the **complete** attribute from the CardElement onChange event (that I'm using to enable/disabled a button).   For reference, this is the event object: ` {   brand:...

- **#202: How to use 3d secure if requiresAction come from server side(PHP)?**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-07-12
  > I am using React and PHP. I don't know how to use 3d secure if  **requires_action** from server side. Here is my code  ``` const CheckoutForm = (props) => {   const elements = useElements();   co...

- **#192: [bug] HMR causes warning to be spammed in console**
  - Labels: stale
  - Comments: 2
  - Last updated: 2021-07-01
  > ### Summary  When using HMR such as react-refresh then every change causes the warning  > Unsupported prop change on Elements: You cannot change the `stripe` prop after setting it.   to be displ...

- **#200: Feature Request: "LastFour" only Card Element**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-06-29
  > I am writing a custom integration (very similar to functionality of the Stripe Customer Portal), where the user can update certain billing settings, upgrade or downgrade their subscription, etc.  I...

- **#194: Migrate from 'react-stripe-elements'**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2021-06-17
  > I'm migrating from `react-stripe-elements` to `stripe/react-stripe-js` following next instructions: https://github.com/stripe/react-stripe-js/blob/master/docs/migrating.md However, I'm a little bit...

- **#186: Chrome inconsistent visual bug: CardElement partial background sometimes dark.**
  - Labels: No labels
  - Comments: 9
  - Last updated: 2021-06-05
  > Hi,  I followed this guide, except that I'm not creating a paymentIntent on load as anonymous users need to input their email: https://stripe.com/docs/payments/integration-builder  1/2 times on...

- **#190: POST Method Not Allowed 405**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-06-04
  > Everything going well on the local host but when I'm trying to build production it returns Method Not Allowed 405

- **#189: How can I get the value of cardNumber in CardNumberElement**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-05-27
  > How can I get the value of cardNumber in CardNumberElement? I needed to be able to use it together with react-credit-cards.

- **#48: Support for react native?**
  - Labels: No labels
  - Comments: 14
  - Last updated: 2021-05-12
  > Hi there, Stripe is an amazing payment gateway. I would like to know if this library support react-native also? if not, are there any library that support react native at the moment.  Thank you.

- **#179: EpsBankElement not working**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2021-05-10
  > I have issue with `EpsBankElement`. Select element display correctly but not react to clicks. There is some changes in DOM classes to `focused` but bank list not show up. In DOM list always have `-hid...

- **#100: Not compatible with StrictMode**
  - Labels: stale
  - Comments: 4
  - Last updated: 2021-05-09
  > ### Summary  We have discovered that this package is not compatible with StrictMode if `sync` mode is used. Async mode is working without any issues.  ### Other information  I've opened an issu...

- **#174: Afterpay not allow in typescript**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2021-04-28
  > Payment_method_type doesn't accept 'afterpay_clearpay' in typescript - unsure which package its defined

- **#176: `canMakePayment` always returns `null`**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-04-28
  > <!-- React Stripe.js is a thin wrapper around Stripe.js and Stripe Elements for React. Please only file issues here that you believe represent bugs with React Stripe.js, not Stripe.js itself.  If...

- **#74: Focus/Keyboard Navigation broken in Safari + VoiceOver**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2021-04-20
  > Both the Stripe `<CardElement>` and the individual card elements (`<CardNumberElement>`, `<CardExpiryElement>` and `<CardCvcElement>`) exhibit unpredictable and broken behavior in Safari while using V...

- **#170: Propagate current state to event listeners on Stripe elements**
  - Labels: stale
  - Comments: 1
  - Last updated: 2021-04-12
  > I can't get my event listeners to work with the current state. I have a fairly simple event listener on my stripe elements:   ``` const cardElementOnReady = name => el => {         el.addEventList...

- **#165: Can't start storybook script**
  - Labels: stale
  - Comments: 2
  - Last updated: 2021-04-08
  > Hey!  I want to look at examples. But can't start storybook script and getting the following error. As far as I can see there are no lodash in `package.json`.  ``` $ start-storybook -p 6006 inte...

- **#122: Example code contradicts TypeScript types**
  - Labels: stale
  - Comments: 6
  - Last updated: 2021-03-29
  > The README contains this example code:  ```javascript const CheckoutForm = () => {   const stripe = useStripe();   const elements = useElements();    const handleSubmit = async (event) => {...

- **#157: typeError i.postMessage is not a function**
  - Labels: help wanted, stale
  - Comments: 8
  - Last updated: 2021-03-26
  > i got this error  {"error":"TypeError: i.postMessage is not a function. (In 'i.postMessage(JSON.stringify(se({},e,{__stripeJsV3:!0})),a)', 'i.postMessage' is undefined)","info":{"componentStack":"\n...

- **#102: Accept a Payment - Documentation on github and on Stripe website**
  - Labels: documentation, stale
  - Comments: 2
  - Last updated: 2021-03-26
  > The first link under Getting Started - "Learn how to accept a payment" on Stripe's GitHub page goes through creating a client secret PaymentIntent on the backend, sending that to the frontend, and exe...

- **#158: Safari Mobile keeps virtual keyboard open on submit.**
  - Labels: needs more info, stale
  - Comments: 3
  - Last updated: 2021-03-25
  > clicking on pay button does not hide the keypad and it keeps opening up when clicked on other buttons. please try you example on iphone (ios)  if you don't believe me.  clicking 'Done' keypad butt...

- **#45: add example how to collect card country for postal code collection**
  - Labels: documentation, stale
  - Comments: 3
  - Last updated: 2021-03-20
  > ### Summary  I'm following the [example here](https://github.com/stripe/react-stripe-js/blob/master/examples/hooks/2-Split-Card.js) -- it collects postal code without element assuming the card is US...

- **#166: Content Security Policy Issue**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-03-09
  > Greetings folks,  I have an issue, when building my app I get this error. My Stripe elements are not showing, anyone knows how can I fix this?  _Refused to load the script 'https://js.stripe.com/v...

- **#164: How to force the card logo preview on Stripe's CardNumberElement to be grey?**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-03-09
  > ### Summary  I have a Stripe input field to collect the user's card number. It works well, except that the preview of the creditcard logo has a pale blue color. it doesn't match my ui. I need to app...

- **#91: What's the point of CardExpiryElement and CardCvcElement**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2021-03-04
  > The examples highlight two main ways to integrate React Stripe with Stripe.js. The most common is to use the `CardElement` component, which allows the user to enter the card number, expiry, and cvc al...

- **#111: AuBankAccountElement shows invalid BSB error for test bank accounts**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2021-02-26
  > Using the Australia bank account numbers found on the Testing documentation, I'm trying to test the AuBankAccountElement react integration.  The test BSB (routing) number is being marked invalid both...

- **#119: Allow modification of the `title` of the rendered iframe**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2021-02-26
  > <!-- React Stripe.js is a thin wrapper around Stripe.js and Stripe Elements for React. Please only file issues here that you believe represent bugs with React Stripe.js, not Stripe.js itself.  If...

- **#129: Styling the input box**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-02-26
  > ### Summary  The style documentation list styling for the input text (https://stripe.com/docs/js/appendix/style?type=card). Is it possible to style the input box itself? I'd like to add css styling...

- **#135: maybeStripe.apply is not a function**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2021-02-26
  > ### Summary  I installed Stripe packages as per the tutorial [here](https://stripe.com/docs/stripe-js/react) and I'm getting the following error:  ```stripe.esm.js:101 Uncaught (in promise) TypeEr...

- **#137: How can I make a read-only card component?**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-02-26
  > As simple as I want to display the card for the user, I can built it myself with CSS but is there any way to take advantage of this library to display the card details?

- **#140: React 17 Support**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2021-02-26
  > ### Summary  <!-- For bug reports, include detailed steps to reproduce or a minimal reproduction of the issue -->  ### Other information React 17 is functionally very similar to 16, but I get the...

- **#142: PaymentRequestButton doesn't set cardholder_name when `requestPayerName: true`**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-02-26
  > Hello. Not sure if it's a bug or intended behavior, I'm initializing the PaymentRequest with: `{ requestPayerName: true, requestPayerEmail: true }`  Then upon `paymentmethod` event I can trigger th...

- **#146: Feature Request: Expose Elements Context**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2021-02-26
  > It is impossible to access Stripe Elements' context from within a modal -- take a look here for an explanation: https://github.com/mpontus/react-modal-hook/issues/30  Quoting from above:  > In the...

- **#151: How to set iDeal Banks List height**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-02-26
  > Hello,  I have an issue with the IdealBankElement, the banks list is too big for my parent iframe. I can't reach the bottom of the list.  <img width="313" alt="Screenshot 2021-01-19 at 23 46 45" s...

- **#161: Payment request button doesn't work**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-02-19
  > hii, this library really helpful and i enjoy to use. everything works well on Card Payment.  but when i try Payment request button, i don't get any deduction to my account after completing Google Pa...

- **#154: [React@17][React-Stripe-JS@1.2.1] Error - Can only create one Element of type card**
  - Labels: No labels
  - Comments: 9
  - Last updated: 2021-02-01
  > ### Summary When removing and adding a card element elsewhere in the dom it will throw the error "Uncaught IntegrationError: Can only create one Element of type card." This happens on React 17 but...

- **#155: Private key exposed with stripePromise**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2021-01-29
  > I am confused that in examples you are using this line below which will make private key visible to any user, point would be to keep PK secure `const stripePromise = loadStripe('pk_test_6pRNASCoBOKtI...

- **#152: IntegrationError on latest 1.2.0 update**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2021-01-29
  > With latest update of react-stripe-js (1.1.2 => 1.2.0), I'm getting error: `IntegrationError: Can only create one Element of type card`.  My code looks as follow: ```       <section>         <div...

- **#150: Intermittent appearance of placeholder even when setting it to empty string**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2021-01-15
  > Hello,  A recent problem we've noticed, just like to clarify whether anything has changed with `placeholder` usage.  Here is a fork of the Stripe Elements 'Split card' demo - https://codesandbox.i...

- **#149: Flex Functionality for CardElement**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2021-01-14
  > <!-- React Stripe.js is a thin wrapper around Stripe.js and Stripe Elements for React. Please only file issues here that you believe represent bugs with React Stripe.js, not Stripe.js itself....

- **#145: CardElement does not render on Safari (Mobile/Desktop) **
  - Labels: No labels
  - Comments: 2
  - Last updated: 2020-12-14
  > ### Summary  CardElement Compoent does not render on safari (Mobile/Desktop) .  ### Other information  ``` function CardSection() {     return (             <CardElement options={CARD_OPTIONS...

- **#141: idealBankelement can not click arrows**
  - Labels: Stripe.js
  - Comments: 2
  - Last updated: 2020-12-10
  > ### Summary  In the idealBankElement you can not click the arrows on the right side.  Its also in the CodeSandbox example. If i add with element inspection **pointer-events: none** it's works  <!...

- **#139: Failed to load stripe.js**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2020-11-28
  > I have a Failed to load.js issue randomly happening on my website as of today.  Any idea why ?

- **#132: Iframe with allowpaymentrequest property does not allow express payment methods**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2020-10-02
  > ### Summary  `stripe.paymentRequest` does not have the same result as the native `PaymentRequest` when calling `canMakePayment` within an Iframe. The Iframe has the `allowpaymentrequest` attribute a...

- **#108: TypeError when creating payment method**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2020-08-30
  > As I submit the card details to Stripe I get the following error:  ``` TypeError: Converting circular structure to JSON     --> starting at object with constructor 'HTMLDivElement'     |     prop...

- **#125: CORS exception for CardNumberElement on Google Chrome**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2020-08-18
  > Am I the only one to get those kind of errors in the Development console logs on Google Chrome?  > Uncaught DOMException: Blocked a frame with origin "https://m.stripe.network" from accessing a cros...

- **#89: Value prop doesn't change placeholder**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2020-08-14
  > I want to change the placeholder "Card number" to another language but with no success. Am I using the wrong prop or are you not able to change the placeholder?  ` const CARD_ELEMENT_OPTIONS = {...

- **#124: React Stripe Chrome 80(SameSite issue blocking CORS with stripe.com)**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2020-08-12
  > Feature request or idea? Consider opening an [API review](https://github.com/stripe/react-stripe-js/tree/master/.github/API_REVIEW.md)!  <!-- React Stripe.js is a thin wrapper around Stripe.js and...

- **#121: NPM 404**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2020-08-06
  > ### Summary  404 error when installing through NPM.  npm ERR! code E404 npm ERR! 404 Not Found - GET https://registry.npmjs.org/@stripe%2freact-stripe-js - Not found npm ERR! 404 npm ERR! 404...

- **#120: CardNumberElement Can't Set Placeholder**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2020-08-05
  > Hello, I have the following simple example.  ``` import React from 'react'; import { CardNumberElement, CardExpiryElement, CardCvcElement } from '@stripe/react-stripe-js';  function CardSection(...

- **#117: Broken UI for CA/GB cards due to postcode element in mobile view**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2020-08-02
  > In Chromium Web Browser, in mobile view, when using a CA/GB card that requires Postcode, card field UI is "broken" as you can see in the screenshot below. The last card digit overlaps the first month...

- **#115: Incorrect field validation on CardNumberComponent**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2020-07-28
  > ### Summary  We realized that by using this specific card number: **1234 5909 8765 4320** the _onChange_ listener for the _CardNumberComponent_ receives `error: undefined, complete: true` so it's no...

- **#106: Unable to update publishable key from component.**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2020-07-15
  > Feature request or idea? Consider opening an [API review](https://github.com/stripe/react-stripe-js/tree/master/.github/API_REVIEW.md)!  <!-- React Stripe.js is a thin wrapper around Stripe.js and...

