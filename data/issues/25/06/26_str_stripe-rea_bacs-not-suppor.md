issue title: BACS not supported in Android Payment Sheet
labels: none
comment count: 0
hyperlink: https://github.com/stripe/stripe-react-native/issues/1982
status: open
date opened: 2025-06-26
repo 30d_merge_rate: 34

====

description:
**Describe the bug**
BACS payment method does not show up in payment sheet on Android.

**To Reproduce**
https://snack.expo.dev/@vistar/stripe-sandbox

**Expected behavior**
BACS should be visible as an accepted payment method.

**Screenshots**

![Image](https://github.com/user-attachments/assets/d8073070-3c4f-41e9-8466-51dc3408469d)

![Image](https://github.com/user-attachments/assets/eb279460-f913-4ebf-af23-5694a7b31272)

**Desktop (please complete the following information):**
 - OS: MacOS 15.3.1

**Smartphone (please complete the following information):**
 - Device: Android Emulator
 - OS: Android 16

**Additional context**
A recent PR was raised for the stripe android-sdk fixing this issue, can we replicate it for the react-native library as well? https://github.com/stripe/stripe-android/pull/11007


===
