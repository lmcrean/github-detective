issue title: 'StripeSdk' could not be found
labels: none
comment count: 16
hyperlink: https://github.com/stripe/stripe-react-native/issues/1962
status: open
date opened: 2025-06-02
repo 30d_merge_rate: 34

====

description:
**Describe the bug**
I have installed the Stripe SDK using npm install @stripe/stripe-react-native but i am getting 

Invariant Violation: TurboModuleRegistry.getEnforcing(...): 'StripeSdk' could not be found. Verify that a module by this name is registered in the native binary., js engine: hermes Error Component Stack:

**Code**
import { STRIPE_PUBLISHABLE_KEY } from '@env';
import { StripeProvider } from '@stripe/stripe-react-native';
<StripeProvider
    publishableKey={STRIPE_PUBLISHABLE_KEY}
    merchantIdentifier="merchant.identifier" // required for Apple Pay
    urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
>
    <PaymentScreen />
</StripeProvider>

// PaymentScreen.ts
import { useStripe } from '@stripe/stripe-react-native';
import { useEffect } from 'react';
import { View, Button } from 'react-native';

export default function PaymentScreen() {
    const { initPaymentSheet, presentPaymentSheet } = useStripe();

    const setup = async () => {
        const { error } = await initPaymentSheet({
            merchantDisplayName: 'Example, Inc.',
            paymentIntentClientSecret: '', // retrieve this from your server
        });
        if (error) {
            // handle error
        }
    };

    useEffect(() => {
        setup();
    }, []);

    const checkout = async () => {
        const { error } = await presentPaymentSheet();

        if (error) {
            // handle error
        } else {
            // success
        }
    };

    return (
        <View>
            <Button title="Checkout" onPress={checkout} />
        </View>
    );
}


**To Reproduce**
Steps to reproduce the behavior:
1. Go to install Stripe SDK
2. Add the Stripe provider
3. Run the project
4. See error

**Expected behavior**
Run the app and open the Stripe payment gateway

**Specifications**
System:
  OS: Windows 11 10.0.26100
  CPU: (16) x64 Intel(R) Core(TM) i7-10700 CPU @ 2.90GHz
  Memory: 1.86 GB / 15.83 GB
Binaries:
  Node:
    version: 20.18.0
    path: C:\Program Files\nodejs\node.EXE
  Yarn:
    version: 1.22.22
    path: ~\AppData\Roaming\npm\yarn.CMD
  npm:
    version: 11.2.0
    path: C:\Program Files\nodejs\npm.CMD
  Watchman: Not Found
SDKs:
  Android SDK:
    API Levels:
      - "31"
      - "33"
      - "34"
      - "35"
    Build Tools:
      - 34.0.0
      - 35.0.0
    System Images:
      - android-34 | Intel x86_64 Atom
      - android-34 | Google APIs ARM 64 v8a
      - android-34 | Google APIs Intel x86_64 Atom
      - android-34 | Google Play Intel x86_64 Atom
      - android-35 | Google Play Intel x86_64 Atom
      - android-35 | Pre-Release 16 KB Page Size Google APIs Intel x86_64 Atom
      - android-36 | Google Play Intel x86_64 Atom
      - android-36 | Pre-Release 16 KB Page Size Google Play Intel x86_64 Atom
      - android-UpsideDownCakePrivacySandbox | Google Play Intel x86_64 Atom
    Android NDK: Not Found
  Windows SDK:
    AllowDevelopmentWithoutDevLicense: Enabled
IDEs:
  Android Studio: AI-243.26053.27.2432.13536105
  Visual Studio: Not Found
Languages:
  Java: 17.0.12
  Ruby: Not Found
npmPackages:
  "@react-native-community/cli":
    installed: 18.0.0
    wanted: 18.0.0
  react:
    installed: 19.0.0
    wanted: 19.0.0
  react-native:
    installed: 0.79.2
    wanted: 0.79.2
  react-native-windows: Not Found
npmGlobalPackages:
  "*react-native*": Not Found
Android:
  hermesEnabled: true
  newArchEnabled: true
iOS:
  hermesEnabled: Not found
  newArchEnabled: Not found

**Full error message**
Invariant Violation: TurboModuleRegistry.getEnforcing(...): 'StripeSdk' could not be found. Verify that a module by this name is registered in the native binary., js engine: hermes Error Component Stack:
    at Subscription (Subscription.tsx:87:73)
    at StaticContainer (StaticContainer.js:9:15)
    at EnsureSingleNavigator (EnsureSingleNavigator.js:12:11)
    at SceneView (SceneView.js:15:9)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at CardSheet (CardSheet.js:11:10)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at Animated(View) (createAnimatedComponent.js:67:57)
    at PanGestureHandler (createHandler.tsx:197:51)
    at PanGestureHandler (GestureHandlerNative.js:8:34)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at Animated(View) (createAnimatedComponent.js:67:57)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at Card (Card.js:31:18)
    at CardContainerInner (CardContainer.js:13:21)
    at RNSScreen (<anonymous>)
    at Animated(Anonymous) (createAnimatedComponent.js:67:57)
    at Suspender (index.tsx:6:9)
    at Suspense (<anonymous>)
    at Freeze (index.tsx:24:32)
    at DelayedFreeze (DelayedFreeze.tsx:11:32)
    at InnerScreen (Screen.tsx:62:34)
    at Screen (Screen.tsx:290:41)
    at MaybeScreen (Screens.js:27:10)
    at RNSScreenContainer (<anonymous>)
    at ScreenContainer (ScreenContainer.tsx:13:70)
    at MaybeScreenContainer (Screens.js:13:10)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at CardStack (CardStack.js:204:22)
    at RNCSafeAreaProvider (<anonymous>)
    at SafeAreaProvider (SafeAreaContext.tsx:35:11)
    at SafeAreaProviderCompat (SafeAreaProviderCompat.js:30:11)
    at RNGestureHandlerRootView (<anonymous>)
    at GestureHandlerRootView (GestureHandlerRootView.android.tsx:12:8)
    at StackView (StackView.js:20:23)
    at PreventRemoveProvider (PreventRemoveProvider.js:31:11)
    at NavigationContent (useComponent.js:6:9)
    at anonymous (useComponent.js:22:13)
    at StackNavigator (createStackNavigator.js:8:5)
    at ThemeProvider (ThemeProvider.js:7:8)
    at EnsureSingleNavigator (EnsureSingleNavigator.js:12:11)
    at BaseNavigationContainer (BaseNavigationContainer.js:72:15)
    at NavigationContainerInner (NavigationContainer.js:42:9)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at Index (Index.tsx:23:61)
    at ToastProvider (ToastContext.tsx:35:41)
    at ThemeProvider (ThemeContext.tsx:18:71)
    at Provider (react-redux.legacy-esm.js:910:66)
    at App (<anonymous>)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at AppContainer (AppContainer-dev.js:88:11)
    at MetricDash(RootComponent) (getCachedComponentWithDebugName.js:26:42)
anonymous @ console.js:654
overrideMethod @ backend.js:17042
reactConsoleErrorHandler @ ExceptionsManager.js:182
anonymous @ setUpDeveloperTools.js:40
registerError @ LogBox.js:231
anonymous @ LogBox.js:80
reportException @ ExceptionsManager.js:111
handleException @ ExceptionsManager.js:171
handleError @ setUpErrorHandling.js:25
reportFatalError @ error-guard.js:49
guardedLoadModule @ require.js:179
metroRequire @ require.js:92
Subscription @ Subscription.tsx:215
reactStackBottomFrame @ ReactFabric-dev.js:14768
renderWithHooks @ ReactFabric-dev.js:4581
updateFunctionComponent @ ReactFabric-dev.js:6959
beginWork @ ReactFabric-dev.js:8215
runWithFiberInDEV @ ReactFabric-dev.js:571
performUnitOfWork @ ReactFabric-dev.js:12184
workLoopSync @ ReactFabric-dev.js:12010
renderRootSync @ ReactFabric-dev.js:11990
performWorkOnRoot @ ReactFabric-dev.js:11478
performSyncWorkOnRoot @ ReactFabric-dev.js:2822
flushSyncWorkAcrossRoots_impl @ ReactFabric-dev.js:2689
processRootScheduleInMicrotask @ ReactFabric-dev.js:2717
anonymous @ ReactFabric-dev.js:2839
Show 25 more frames
Show less
Subscription.tsx:215 Invariant Violation: TurboModuleRegistry.getEnforcing(...): 'StripeSdk' could not be found. Verify that a module by this name is registered in the native binary., js engine: hermes Error Component Stack:
    at Subscription (Subscription.tsx:87:73)
    at StaticContainer (StaticContainer.js:9:15)
    at EnsureSingleNavigator (EnsureSingleNavigator.js:12:11)
    at SceneView (SceneView.js:15:9)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at CardSheet (CardSheet.js:11:10)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at Animated(View) (createAnimatedComponent.js:67:57)
    at PanGestureHandler (createHandler.tsx:197:51)
    at PanGestureHandler (GestureHandlerNative.js:8:34)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at Animated(View) (createAnimatedComponent.js:67:57)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at Card (Card.js:31:18)
    at CardContainerInner (CardContainer.js:13:21)
    at RNSScreen (<anonymous>)
    at Animated(Anonymous) (createAnimatedComponent.js:67:57)
    at Suspender (index.tsx:6:9)
    at Suspense (<anonymous>)
    at Freeze (index.tsx:24:32)
    at DelayedFreeze (DelayedFreeze.tsx:11:32)
    at InnerScreen (Screen.tsx:62:34)
    at Screen (Screen.tsx:290:41)
    at MaybeScreen (Screens.js:27:10)
    at RNSScreenContainer (<anonymous>)
    at ScreenContainer (ScreenContainer.tsx:13:70)
    at MaybeScreenContainer (Screens.js:13:10)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at CardStack (CardStack.js:204:22)
    at RNCSafeAreaProvider (<anonymous>)
    at SafeAreaProvider (SafeAreaContext.tsx:35:11)
    at SafeAreaProviderCompat (SafeAreaProviderCompat.js:30:11)
    at RNGestureHandlerRootView (<anonymous>)
    at GestureHandlerRootView (GestureHandlerRootView.android.tsx:12:8)
    at StackView (StackView.js:20:23)
    at PreventRemoveProvider (PreventRemoveProvider.js:31:11)
    at NavigationContent (useComponent.js:6:9)
    at anonymous (useComponent.js:22:13)
    at StackNavigator (createStackNavigator.js:8:5)
    at ThemeProvider (ThemeProvider.js:7:8)
    at EnsureSingleNavigator (EnsureSingleNavigator.js:12:11)
    at BaseNavigationContainer (BaseNavigationContainer.js:72:15)
    at NavigationContainerInner (NavigationContainer.js:42:9)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at Index (Index.tsx:23:61)
    at ToastProvider (ToastContext.tsx:35:41)
    at ThemeProvider (ThemeContext.tsx:18:71)
    at Provider (react-redux.legacy-esm.js:910:66)
    at App (<anonymous>)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at RCTView (<anonymous>)
    at View (View.js:32:34)
    at AppContainer (AppContainer-dev.js:88:11)
    at MetricDash(RootComponent) (getCachedComponentWithDebugName.js:26:42)
anonymous @ console.js:654
overrideMethod @ backend.js:17042
reactConsoleErrorHandler @ ExceptionsManager.js:182
anonymous @ setUpDeveloperTools.js:40
registerError @ LogBox.js:231
anonymous @ LogBox.js:80
reportException @ ExceptionsManager.js:111
handleException @ ExceptionsManager.js:171
handleError @ setUpErrorHandling.js:25
reportFatalError @ error-guard.js:49
guardedLoadModule @ require.js:179
metroRequire @ require.js:92
Subscription @ Subscription.tsx:215
reactStackBottomFrame @ ReactFabric-dev.js:14768
renderWithHooks @ ReactFabric-dev.js:4581
updateFunctionComponent @ ReactFabric-dev.js:6959
beginWork @ ReactFabric-dev.js:8215
runWithFiberInDEV @ ReactFabric-dev.js:571
performUnitOfWork @ ReactFabric-dev.js:12184
workLoopSync @ ReactFabric-dev.js:12010
renderRootSync @ ReactFabric-dev.js:11990
performWorkOnRoot @ ReactFabric-dev.js:11521
performSyncWorkOnRoot @ ReactFabric-dev.js:2822
flushSyncWorkAcrossRoots_impl @ ReactFabric-dev.js:2689
processRootScheduleInMicrotask @ ReactFabric-dev.js:2717
anonymous @ ReactFabric-dev.js:2839
Show 25 more frames
Show less
console.js:654 Warning: TypeError: Cannot read property 'StripeProvider' of undefined

This error is located at:
    at Subscription (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:171228:41)
    at StaticContainer (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:155077:17)
    at EnsureSingleNavigator (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:150695:24)
    at SceneView (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:154917:22)
    at RCTView (<anonymous>)
    at View (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:52158:43)
    at RCTView (<anonymous>)
    at View (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:52158:43)
    at RCTView (<anonymous>)
    at View (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:52158:43)
    at CardSheet (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:194829:23)
    at RCTView (<anonymous>)
    at View (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:52158:43)
    at Animated(View) (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:61639:47)
    at PanGestureHandler (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:173989:38)
    at PanGestureHandler (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:190502:34)
    at RCTView (<anonymous>)
    at View (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:52158:43)
    at Animated(View) (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:61639:47)
    at RCTView (<anonymous>)
    at View (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:52158:43)
    at Card (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:194346:36)
    at CardContainerInner (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:193960:34)
    at RNSScreen (<anonymous>)
    at Animated(Anonymous) (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:61639:47)
    at Suspender (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:192952:22)
    at Suspense (<anonymous>)
    at Freeze (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:192962:23)
    at DelayedFreeze (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:192917:22)
    at InnerScreen (http://localhost:8081/index.bundle//&platform=android&dev=true&lazy=true&minify=false&app=com.metricdash&modulesOnly=false&runModule=true&excludeSource=true&sourcePaths=url-server:192711:41)
    at Screen (http://localhost:8081/index.b


===

comment #1 by anacicconi, 2025-06-04, 14:42:31
Are you using EAS build? If that's the case, you have to rebuild the app. You probably changed the app.json or app.config.ts so the app needs to be rebuilt for this config to work.

comment #2 by thedev132, 2025-06-09, 00:48:13
I'm encountering the same issue now too, I tried rebuilding and removing node modules but nothing helps. 

comment #3 by seanzhang-stripe, 2025-06-10, 19:17:00
Hi @Aniket239 did you run run `pod install` in your `ios` directory to install the native dependencies? 

comment #4 by thedev132, 2025-06-10, 19:53:27
Even after using pod install I receive this error in the console:

` ERROR  Invariant Violation: TurboModuleRegistry.getEnforcing(...): 'StripeSdk' could not be found. Verify that a module by this name is registered in the native binary., js engine: hermes`

Hope that helps :)

comment #5 by jasonaibrahim, 2025-06-22, 15:46:02
I'm seeing the same issue too with `"expo": "~53.0.11"` and `"@stripe/stripe-react-native": "0.45.0"`. I'm using `expo run:ios` with a development build, ios project is building successfully, but seeing the above runtime error when the app launches.

Update: I deleted Podfile.lock and re-ran `expo run:ios` and everything works as expected.

comment #6 by seanzhang-stripe, 2025-06-24, 07:15:03
Thanks @jasonaibrahim for the solution. 

@thedev132 can you try the same (i.e., delete `Podfile.lock` and re-run `expo run:ios`) and see if it solves your problem?

comment #7 by Ritorna, 2025-06-26, 09:30:39
I also run into the same problem. I'm using the react native cli and the issues started occurring to me after i've upgraded to the latest stripe version and react native 0.79.4
Weirdly enough, this error will only show after closing and re-opening the app which is using the sdk - but it's consistent in dev and release mode. 

comment #8 by Ritorna, 2025-06-30, 09:48:18
In my case i figured that in my MainActivity i've passed ```null``` to the inherited onCreate function, as it did cause issues in previous react native version. 

As for now, it seems to work flawless. I would need to dig deeper to fully understand, whether this is now required in order to make turbo modules work or not. 

```kotlin
 override fun onCreate(savedInstanceState: Bundle?) {
    SplashScreen.show(this);
    super.onCreate(savedInstanceState); // <=  pass the savedInstanceState as it now is correctly persisted
  }
```

comment #9 by hugoth, 2025-07-06, 13:55:57
hey guys, also seeing this error running `npx expo run:ios`
 with   "@stripe/stripe-react-native": "^0.49.0",

Any idea how to resolve this? 

comment #10 by jasonaibrahim, 2025-07-06, 13:57:35
@hugoth did you try deleting Podfile.lock and re-run expo run:ios?

comment #11 by hugoth, 2025-07-06, 14:02:21
@jasonaibrahim yes just did same result :(
here my app.config plugin's file

```
    plugins: [
      "@react-native-google-signin/google-signin",
      [
        "expo-build-properties",
        {
          ios: {
            useFrameworks: "static",
          },
        },
      ],
      "expo-router",
      "@react-native-firebase/app",
      "@react-native-firebase/auth",
      [
        "@stripe/stripe-react-native",
        {
          merchantIdentifier: "merchant.com.xxxxxx",
          enableGooglePay: true, // Enable Google Pay
        },
      ],
    ],
```

also cleared different expo's cache and node modules


comment #12 by jasonaibrahim, 2025-07-06, 14:10:10
Are you using eas build? Is it possible to delete the ios/ and android/ directories and try again?

comment #13 by hugoth, 2025-07-06, 14:53:26
@jasonaibrahim yes still have the same issue with eas build and after deleting ios/ and android/ directories

comment #14 by Aniket239, 2025-07-06, 15:38:45
Try deleting the installed app from the emulator or mobile device and then reinstalling it. 

comment #15 by hugoth, 2025-07-06, 22:27:21
Update: running eas build fixed it, the error is still triggered on simulator when app launches, but once I close and reopen it, it works fine 

comment #16 by sjuery, 2025-08-07, 16:08:27
I'm also running into this issue, what's worked for me is to run expo prebuild, followed by opening the app in xcode and launching it from there in production mode.

Any attempt to launch in development mode gives me the above error.

It's not an ideal fix because it's quite a bit slower and dosen't auto refresh on updates, but at least it's something
