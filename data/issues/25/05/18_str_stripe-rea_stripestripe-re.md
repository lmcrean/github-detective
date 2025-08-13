issue title: @stripe/stripe-react-native build fails with Kotlin 1.8.0 – Incompatible with Compose Compiler 1.3.2
labels: none
comment count: 12
hyperlink: https://github.com/stripe/stripe-react-native/issues/1937
status: open
date opened: 2025-05-18
repo 30d_merge_rate: 34

====

description:
I'm encountering a build error when running react-native run-android after installing @stripe/stripe-react-native. The build fails due to Kotlin version incompatibility:


This version (1.3.2) of the Compose Compiler requires Kotlin version 1.7.20
but you appear to be using Kotlin version 1.8.0 which is not known to be compatible.
Please fix your configuration (or `suppressKotlinVersionCompatibilityCheck` but don't say I didn't warn you!).
The error originates from the task:


:stripe_stripe-react-native:compileDebugKotlin FAILED
Environment:

React Native version: 0.73.x

Kotlin version: 1.8.0

Android Gradle Plugin: 8.1.1

@stripe/stripe-react-native: latest version (at time of posting)

compileSdkVersion: 35

Expected Behavior:
I expect the package to compile without needing to downgrade Kotlin or suppress compatibility checks manually.

Steps to Reproduce:

Install @stripe/stripe-react-native in a new RN 0.73+ project

Run npx react-native run-android

Build fails due to incompatible Compose Compiler and Kotlin versions

Temporary Workarounds Tried:

Downgrading Kotlin to 1.7.20 (not ideal since other packages may require 1.8.0)

Adding suppressKotlinVersionCompatibilityCheck (not a clean solution)

===

comment #1 by jacksangl, 2025-05-19, 01:37:32
I thought I was going crazy. This has been happening to me for the past hour. Thanks for the temporary solution.

comment #2 by kelvin-pelago, 2025-05-22, 14:29:12
same issue, same env, but cannot bypass by workaround solution

comment #3 by tjclawson-stripe, 2025-05-22, 23:35:09
Hey @PandorasBoxTool2024, can you try to solution listed [here](https://github.com/stripe/stripe-react-native/issues/1924#issuecomment-2867227374) and see if that resolves your issue?

comment #4 by justynpollard1, 2025-05-23, 18:18:09
> Hey [@PandorasBoxTool2024](https://github.com/PandorasBoxTool2024), can you try to solution listed [here](https://github.com/stripe/stripe-react-native/issues/1924#issuecomment-2867227374) and see if that resolves your issue?

I had same issue and that solution worked for me, thanks!

comment #5 by PandorasBoxTool2024, 2025-05-24, 20:43:33
@justynpollard1 Is not working :-(

comment #6 by justynpollard1, 2025-05-24, 20:47:35
> @justynpollard1 Is not working :-(

Have you tried deleting your gradle cache folders, and gradlew clean?

comment #7 by Alishaikh31, 2025-05-29, 17:44:55
I encountered the same issue. After spending many hours debugging, I resolved it by downgrading the Stripe SDK version to 0.39.0. That fixed the problem for me.

comment #8 by MuhammadTalhaTahir1, 2025-06-02, 11:57:12
I encountered the same issue. After several hours of debugging, I resolved it by upgrading to the latest Stripe SDK (0.47.1) and updating my Kotlin version to 2.0.21 (previously it was 1.9.25).
My React Native version is 0.76.7.

comment #9 by PandorasBoxTool2024, 2025-06-02, 17:31:17
> > [@justynpollard1](https://github.com/justynpollard1) Is not working :-(
> 
> Have you tried deleting your gradle cache folders, and gradlew clean?

Yes i try Downgrade and Upgrade all and try /android gradlew clean


comment #10 by hezhengjian, 2025-06-04, 02:09:39
Hi, I’m running into a build error related to Jetpack Compose Compiler and Kotlin compatibility:
```
e: This version (1.2.0) of the Compose Compiler requires Kotlin version 1.7.0 but you appear to be using Kotlin version 1.8.10 which is not known to be compatible. Please fix your configuration (or `suppressKotlinVersionCompatibilityCheck` but don't say I didn't warn you!).
```
It seems like the Stripe SDK might be using an older version of the Compose Compiler (1.2.0), which isn’t compatible with my current Kotlin version (1.8.10). Has anyone else run into this, or is there a recommended way to resolve this without downgrading Kotlin?
"@stripe/stripe-react-native": "0.47.1",

comment #11 by muchirasamwel, 2025-07-05, 19:16:17
Its still an issue even with the latest version of stripe. downgrading worked for me.

> I encountered the same issue. After spending many hours debugging, I resolved it by downgrading the Stripe SDK version to 0.39.0. That fixed the problem for me.



comment #12 by canberkvarli, 2025-07-20, 14:44:28
Any update on this? I also am having the same issue.
