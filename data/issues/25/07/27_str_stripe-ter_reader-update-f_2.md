issue title: Reader update failed due to lack of internet connection
labels: none
comment count: 3
hyperlink: https://github.com/stripe/stripe-terminal-react-native/issues/1003
status: open
date opened: 2025-07-27
repo 30d_merge_rate: 19

====

description:
My Chipper reader requires an update.  The sample app will initiate the update and then fail around 52% with the following error:

connectBluetoothReader error: {"code": "READER_ERROR.READER_SOFTWARE_UPDATE_FAILED_SERVER_ERROR", "message": "Update failed due to lack of internet connection"}

I have tried with the Render backend and a local Docker backend with the same results. I am connected to the Internet with no interruptions.

I am running the app on Android 15 connected via bluetooth.




===

comment #1 by billfinn-stripe, 2025-07-28, 15:19:54
Hi there -- can you provide your reader's serial number and also an approximate timestamp in UTC when you are able to reproduce the problem?

comment #2 by erickaleida, 2025-07-28, 15:39:23
Yes, the serial number is CHB30D430012884.  I tried an update 7/27 around 5 PM EDT. 

comment #3 by billfinn-stripe, 2025-07-31, 15:07:53
Hi there -- it looks like reader `CHB30D430012884` was not purchased through Stripe. Only Terminal readers purchased through Stripe can be used with Stripe SDKs.
