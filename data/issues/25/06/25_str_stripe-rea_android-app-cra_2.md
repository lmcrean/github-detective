issue title: Android app crashes on - ActivityTaskManager timeout and StripeKeepJsAwakeTask error `presentPaymentSheet()`
labels: none
comment count: 3
hyperlink: https://github.com/stripe/stripe-react-native/issues/1981
status: open
date opened: 2025-06-25
repo 30d_merge_rate: 34

====

description:
Our React Native Android application crashes when calling the method from the Stripe React Native SDK. The crash occurs consistently on Android devices with ActivityTaskManager timeout and StripeKeepJsAwakeTask warning. `presentPaymentSheet`

**To Reproduce** Steps to reproduce the behavior:
1. Go to payment screen in the app
2. Fill in payment form and tap 'Pay' button
3. App calls `initPaymentSheet()` (works correctly)
4. App calls `presentPaymentSheet()`
5. See error - app crashes immediately

**Expected behavior** The Stripe payment sheet should open, allowing users to complete their payment without the app crashing.
**Error Logs**
``` 
06-25 14:56:01.764   498   516 W ActivityTaskManager: Activity top resumed state loss timeout for ActivityRecord{4781c8 u0 com.railmonsters/com.stripe.android.paymentsheet.PaymentSheetActivity} t-1 f}}

WARN  No task registered for key StripeKeepJsAwakeTask
```
**Screenshots** N/A - App crashes before any UI is displayed
**Desktop (please complete the following information):**
- OS: macOS Sonoma (aarch64)
- IDE: WebStorm 2025.1.2
- Development environment: React Native CLI

**Smartphone (please complete the following information):**
- Device: Multiple Android devices tested
- OS: Android 10-14
- Testing: Both physical devices and emulators
- Version: Consistent across all tested versions

**Environment Information:**
- **@stripe/stripe-react-native:** 0.48.0
- **React Native:** 0.76.5
- **React:** 18.3.1
- **TypeScript:** 5.7.2
- **Android Target SDK:** 34
- **Android Compile SDK:** 35
- **Android Min SDK:** 24
- **Build Tools:** 35.0.0
- **Kotlin:** 2.0.21
- **Hermes:** Enabled

**Additional context**
- iOS works perfectly with identical code
- `initPaymentSheet()` completes successfully, only crashes `presentPaymentSheet()`
- Issue occurs in both debug and release builds
- Using test publishable key:
- Tried clean builds, Metro cache reset, and dependency updates
- The "StripeKeepJsAwakeTask" warning suggests a background task registration issue
- ActivityTaskManager timeout indicates PaymentSheetActivity lifecycle problems
- App uses splash screen and custom MainActivity configuration
- Could be related to React Native 0.76.5 compatibility issues


===

comment #1 by wassiq, 2025-06-27, 13:43:17
i am facing the same issue.

comment #2 by DimaNovik, 2025-06-30, 16:17:49
@wassiq 

try add 

resolutionStrategy {
        force 'androidx.activity:activity:1.8.0'
}

and

dependencies {
    implementation "com.google.android.material:material:1.12.0"
}

in app/build.gradle

comment #3 by Eti-Fromentin, 2025-07-24, 16:22:22
I just had the exact same problem.  RN 0.78, newArch enabled, stripe-react-native 0.50

After the crash I did `adb logcat -v time | grep -A 50 "FATAL EXCEPTION"`. 
And there was `java.lang.NoSuchMethodError: No static method getApplicationLocales()Landroidx/core/os/LocaleListCompat` 
I just had to upgrade `androidx.appcompat:appcompat` in build.gradle

