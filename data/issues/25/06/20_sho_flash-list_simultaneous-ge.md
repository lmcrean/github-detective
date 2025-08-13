issue title: Simultaneous Gestures (RNGH) .Pan() + .Native() not working together w/ FlashList
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1744
status: open
date opened: 2025-06-20
repo 30d_merge_rate: 7

====

description:
### Description

## Current Behavior
I have a FlashList with items that can be panned to reveal timestamps and it seems I can either Pan or Scroll the FlashList even though I have a composed simultaneous gesture. Also seems that native gestures are not being detected from the FlashList

## Expected Behavior
https://github.com/user-attachments/assets/268d80cd-0e24-4e72-9982-05fd42348369

Something like iMessage timestamp revealing where I can almost free-pan so I can reveal timestamps and scroll. This works with FlatList so it likely means native gestures are not being detected from the FlashList. Some method to expose native elements?

## I have tried
- Single Gesture Detector with composed gesture
- renderScrollComponent from FlashList w/ GestureDetector wrapping a ScrollView passed in (https://github.com/software-mansion/react-native-gesture-handler/issues/2622#issuecomment-2276746709)
- 2 gesture detectors w/ outer one Gesture.Native() wrapping FlashList & other Gesture.Pan() wrapping messages
- .simultaneousWithExternalGesture(Gesture.Native()) on pan gesture
- overrideProps w/ some ref that is passed to FlashList & Gesture Detector
- ref to access native scrollable node of FlashList

FlatList instead of FlashList does work technically but it is awful looking with live data fetching and lots of messages. 

Minimal reproducible example: https://snack.expo.dev/@yaboibrando/flashlistgestures?platform=ios All things I have tried are on the snack to try

FlatList working and not FlashList indicates that Native gesture detection is not working on the FlashList which is why I've seen a lot of people suggesting the renderScrollComponent and passing a ScrollView in there, and also why I tried to use getScrollableNode from FlashList for the scrollableRef but these did not seem to work. The most commonly suggested solution online is using gesture handlers which are from older versions of RNGH like here: https://github.com/software-mansion/react-native-gesture-handler/issues/2175#issuecomment-1230207219

Are there any workarounds or is this not supported? The most recent active issue I have seen here: https://github.com/Shopify/flash-list/issues/551 was closed 3 weeks ago with an outdated solution almost 3 years old and on the older version of RNGH so I am wondering if anybody has found something for RNGH >2.0?

### Steps to reproduce

1.  Open Snack
2. Try simultaneous pan + scroll using FlashList
3. Comment out FlashList + try FlatList
4. Observe difference in behavior
5. Try uncommenting different things I've tried to see if they work

### A link to a [Gist](https://gist.github.com/), an [Expo Snack](https://snack.expo.io/) or a link to a repository based on [this template](https://github.com/react-native-community/reproducer-react-native) that reproduces the bug.

https://snack.expo.dev/@yaboibrando/flashlistgestures?platform=ios

### FlashList Version

1.6.4

### Gesture Handler version

2.16.1

### React Native version

0.74.3

### Platforms

iOS

### JavaScript runtime

None

### Workflow

Using Expo Go

### Architecture

None

### Build type

None

### Device

iOS simulator

### Device model

_No response_

### Acknowledgements

Yes

===
