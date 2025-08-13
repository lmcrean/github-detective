issue title: Exclude Apple pay or PassKit framework from the generated binary
labels: none
comment count: 1
hyperlink: https://github.com/stripe/stripe-react-native/issues/1936
status: open
date opened: 2025-05-17
repo 30d_merge_rate: 34

====

description:
Is it possible to exclude apple pay in an expo workflow.
We only intend to use this library in our android build, we already use apple in app purchase services for our ios builds. The problem is that apple pay dependencies still gets bundled and our ios app binary gets rejected when we submit it to app store connect.

This is the rejection message

"The app binary includes the [PassKit framework](https://developer.apple.com/documentation/passkit) for implementing Apple Pay, but we were unable to verify any integration of Apple Pay within the app."

Is there a way to specify that apple pay should be excluded.

===

comment #1 by imraann0, 2025-06-19, 14:40:39
> Is it possible to exclude apple pay in an expo workflow. We only intend to use this library in our android build, we already use apple in app purchase services for our ios builds. The problem is that apple pay dependencies still gets bundled and our ios app binary gets rejected when we submit it to app store connect.
> 
> This is the rejection message
> 
> "The app binary includes the [PassKit framework](https://developer.apple.com/documentation/passkit) for implementing Apple Pay, but we were unable to verify any integration of Apple Pay within the app."
> 
> Is there a way to specify that apple pay should be excluded.

did you find solution for this
