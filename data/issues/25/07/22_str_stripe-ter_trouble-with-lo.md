issue title: Trouble with locally testing reader updates
labels: none
comment count: 2
hyperlink: https://github.com/stripe/stripe-terminal-react-native/issues/997
status: open
date opened: 2025-07-22
repo 30d_merge_rate: 19

====

description:
We are using the stripeM2 card reader, but having issues with being able to simulate updates in specific scenarios.

Problem:
Currently when calling `connectReader` if a reader has an update it will immediately begin installing the update before it connects (stripeM2), this does not call `onDidReportUpdate` because the reader hasn't been officially connected to the SDK. `onDidReportUpdate` only appears to being called when a reader has an update after already being connected with `connectReader`.  It does however call `onDidStartInstallingUpdate` which we can store the update and progress in state to display in UI. However, there is no way to actually simulate this scenario unless we use brand new unopened M2s (we've seen this for every new M2 we use) because 1. We can't force an update to be needed on real m2 readers 2. Can only simulate updates with emulator and simulated readers with `simulateUpdate('arg')` after the reader has been connected.

Would love some input on how we should be defensively coding against this edge case because there currently doesn't seem to be a way to test it until it's in production with live devices.

Version: beta@25
OS: Android

===

comment #1 by tlin-c-stripe, 2025-07-23, 14:28:47
There's a simulateReaderUpdate API in useStripeTerminal, you can try to see if it help your case. Thanks
Please reference https://github.com/stripe/stripe-terminal-react-native/issues/645. 

comment #2 by imjakechapman, 2025-08-01, 15:21:35
@tlin-c-stripe, the above reference doesn't do much for us since we already have the ability to simulateReaderUpdate with simulated: true - The issue comes from using the real hardware (M2) fresh out of the box. We haven't had a single M2 fresh out of the box that didn't immediately start downloading an update before it was connected to SDK.

Exact repro steps:
1. Open fresh M2
2. discoverReaders('bluetoothScan')
3. connectReader
4. SDK moves reader status to 'connecting'
5. Starts logging update progress
6. Update completes
7. SDK continues with connecting and moves device to status 'connected'

But since it's never connected, we don't get any update callbacks except "onDidStartInstallingUpdate". So I'm hoping you can add some sort of simulateReaderUpdate and have it force simulate that update prior to the SDK connecting to device so we can  handle this scenario.
