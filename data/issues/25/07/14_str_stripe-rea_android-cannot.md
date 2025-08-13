issue title: Android - Cannot read property 'StripeProvider' of undefined
labels: none
comment count: 1
hyperlink: https://github.com/stripe/stripe-react-native/issues/2000
status: open
date opened: 2025-07-14
repo 30d_merge_rate: 34

====

description:
**Describe the bug**
When trying to import and use the StripeProvider from the @stripe/stripe-react-native package, the app crashes with the error:
Cannot read property 'StripeProvider' of undefined.
This suggests that the package is either not linked correctly or not properly initialized.

**To Reproduce**
Steps to reproduce the behavior:
1. Create a new React Native project (e.g., using npx react-native init).
2. Install @stripe/stripe-react-native.
3. Import StripeProvider from @stripe/stripe-react-native.
4. Use <StripeProvider> component in your app.
5. Run the app.
6. See the error in the console or app crash.


**Expected behavior**
The <StripeProvider> component should be properly imported and usable without causing runtime errors.

**Desktop (please complete the following information):**

- OS: [macos sequoia 15.5]
- Node version: [20.15.0]
- React Native version: [0.80.1]
- Stripe React Native version: [^0.49.0]
- 

**Smartphone (please complete the following information):**
 - Device: [Emulators and real devices]
 - OS: [Android]

**Additional context**

- The package is installed via npm.
- Tried cleaning build cache, reinstalling node_modules, and rebuilding the app.
- The error occurs immediately upon rendering the <StripeProvider> component.



===

comment #1 by davidme-stripe, 2025-07-24, 01:59:08
Hello, sorry for the trouble! Can you share how you installed `stripe-react-native`, and maybe attach some additional logs? It sounds like React Native is unable to import the library, but it's hard to tell why without more logging detail.
