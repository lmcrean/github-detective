issue title: com.stripeterminalreactnative.TokenProvider.setConnectionToken Android Crash
labels: none
comment count: 3
hyperlink: https://github.com/stripe/stripe-terminal-react-native/issues/979
status: open
date opened: 2025-06-26
repo 30d_merge_rate: 19

====

description:
**Describe the bug**
A few of our users are crashing right when connectLocalMobileReader is called. There is no error being returned from connectLocalMobileReader so it could potentially be a native error (not sure). I am seeing this crash being logged in our Google Play console, presumably coming from the StripeTerminalProvider. It is only affecting a very small subset of users, but we would still like to fix it.

Exception java.lang.RuntimeException:
  at com.facebook.react.bridge.JavaMethodWrapper.invoke (JavaMethodWrapper.java:381)
  at com.facebook.react.bridge.JavaModuleWrapper.invoke (JavaModuleWrapper.java:146)
  at com.facebook.jni.NativeRunnable.run
  at android.os.Handler.handleCallback (Handler.java:959)
  at android.os.Handler.dispatchMessage (Handler.java:100)
  at com.facebook.react.bridge.queue.MessageQueueThreadHandler.dispatchMessage (MessageQueueThreadHandler.java:27)
  at android.os.Looper.loopOnce (Looper.java:257)
  at android.os.Looper.loop (Looper.java:342)
  at com.facebook.react.bridge.queue.MessageQueueThreadImpl$4.run (MessageQueueThreadImpl.java:233)
  at java.lang.Thread.run (Thread.java:1012)
Caused by java.lang.reflect.InvocationTargetException:
  at java.lang.reflect.Method.invoke
  at com.facebook.react.bridge.JavaMethodWrapper.invoke (JavaMethodWrapper.java:372)
Caused by com.stripe.stripeterminal.external.models.ConnectionTokenException:
  at com.stripeterminalreactnative.TokenProvider.setConnectionToken (TokenProvider.kt:17)
  at com.stripeterminalreactnative.StripeTerminalReactNativeModule.setConnectionToken (StripeTerminalReactNativeModule.kt:187)

**To Reproduce**
Not reproducible in dev env.

**Expected behavior**
Connection token is set successfully and payments flow continues, as with other devices.

**Stripe Terminal React Native SDK version**
^0.0.1-beta.23

**Smartphone:**
- Device: Samsung Galaxy A15
- OS: Android 14


===

comment #1 by mindy-stripe, 2025-06-27, 17:20:52
Hi @inzqne thanks for writing in. A couple of questions:

1. Could you please provide a snippet of sample code on how you are setting the connection token provider?
2. Do you have device serial numbers or timestamps of this issue occurring in your application so that we can look into logging from our side? 

Thanks in advance.

comment #2 by inzqne, 2025-07-04, 10:12:55
> Hi [@inzqne](https://github.com/inzqne) thanks for writing in. A couple of questions:
> 
> 1. Could you please provide a snippet of sample code on how you are setting the connection token provider?
> 2. Do you have device serial numbers or timestamps of this issue occurring in your application so that we can look into logging from our side?
> 
> Thanks in advance.

Hello @mindy-stripe, I would like to also add that we started seeing these crashes after we upgraded from ^0.0.1-beta.16 to ^0.0.1-beta.23 for Expo 51 upgrade. Is the ^0.0.1-beta.16 version compatible with Expo 51? If so, we can just downgrade for the time being. My theory is that this issue is coming from the Stripe Android native SDK that version 23 is using.

Here is the info you requested
1. 
```javascript
const fetchTokenProvider = async () => {
      var response = await api.getStripeConnectionToken();

      if (response.status == 'success')
        return response.secretToken;
      else
        throw new Error('Token request failed');
};
``` 
2. I don't have specific serial numbers but here are the following timestamps from recently:
- July 2, 2025 at 1:00 PM PST
- June 26, 2025 at 3:00 PM PST

I went ahead and checked our logs through Stripe Workbench but couldn't find anything related.


comment #3 by inzqne, 2025-07-09, 21:37:34
Hello @mindy-stripe, do you any updates? This is blocking some of our users so we want to fix this ASAP.
