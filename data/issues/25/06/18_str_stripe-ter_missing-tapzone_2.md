issue title: Missing tapZoneIndicator option for NFC readers located to the right of the screen
labels: enhancement, Tap to Pay
comment count: 5
hyperlink: https://github.com/stripe/stripe-terminal-react-native/issues/970
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 19

====

description:
**Describe the bug**
We're using Tap To Pay on the Stripe Terminal in a React Native Android app. We are running the app on a standard off-the-shelf kiosk device, which includes an NFC reader physically located to the **right** of the screen. 

When configuring setTapToPayUxConfiguration, the tapZoneIndicator property does not include an option to indicate that the NFC reader is to the right. The only available options are default, above, below, behind, and front. This makes it impossible to properly reflect the actual tap zone location in our UI, which makes for a terrible user experience. 

**Expected behavior**
We expect to be able to specify that the tap zone is to the right of the screen, as this is a common hardware layout on kiosks. The SDK should include a "right" or similar enum value for tapZoneIndicator.

**Stripe Terminal React Native SDK version**
^0.0.1-beta.25

OS: Android 13

**Additional context**
Adding support for right-side tap zones would improve flexibility for a wide range of commercial kiosk devices and provide a more intuitive user experience. Let us know if this can be added or if a workaround is available.

===

comment #1 by sethia-stripe, 2025-06-19, 19:59:38
We are looking into it! @johncthings - Can you please share the device model ?

comment #2 by johncthings, 2025-06-20, 08:48:34
Hi @sethia-stripe, thanks for looking into this! We're using the Newland Mantra III running Android 13 - but just to clarify, this issue isn’t device-specific. It affects all setups using external NFC readers mounted to the right of the screen.

At the moment, leaving the tapZoneIndicator as default results in a "Tap behind the device" message, which is very misleading.

comment #3 by maggiewhite-stripe, 2025-06-24, 02:45:37
@johncthings Thanks for sharing that context - we will update this ticket when we have any updates about when this would be available

comment #4 by johncthings, 2025-07-09, 15:21:51
Any idea of a timeline on when this will be available?

comment #5 by johncthings, 2025-08-04, 09:44:47
Hello, just wondering if there is any update on this?
