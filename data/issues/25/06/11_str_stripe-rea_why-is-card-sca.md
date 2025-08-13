issue title: Why is "card scanning" iOS only?
labels: enhancement
comment count: 2
hyperlink: https://github.com/stripe/stripe-react-native/issues/1968
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 34

====

description:
When looking at the docs I can see that when using the Android SDK directly card scanning can be enabled pretty easily. So I was just wondering what's preventing the scan card functionality from working on Android when using the stripe-react-native SDK?

Stripe React Native SDK Docs:
<img width="871" alt="Image" src="https://github.com/user-attachments/assets/10ded6c4-7e04-409b-95e4-ab226a031875" />

Stripe Android SDK Docs:
<img width="884" alt="Image" src="https://github.com/user-attachments/assets/43d6e15b-f965-449c-8c00-d184b3047745" />

Is this something planned for a future release?
Are we waiting for some upstream changes to make this easier to implement for the react-native SDK?

===

comment #1 by wooj-stripe, 2025-06-11, 22:46:49
HI @ammar-madni Appreciate the suggestion, as it seems like a reasonable request given there is support for it in the native Android SDK. We revisit our roadmap periodically and will keep this idea in mind.

comment #2 by Rayhko, 2025-06-12, 13:31:41
It would be really interesting to have it on Android too, especially since it's supported by the Android SDK.
Thanks @wooj-stripe !
