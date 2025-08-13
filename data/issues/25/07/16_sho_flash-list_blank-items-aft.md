issue title: Blank items after setting scroll position with a `scrollTo...` method during a fling scroll (regression in v2)
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1784
status: open
date opened: 2025-07-16
repo 30d_merge_rate: 7

====

description:
## Current behavior

When the scroll position is reset to the start while a fling scroll is animating (i.e. after lifting your finger), some or all of the first items don't render and leave a blank space instead. The missing items will render when you start scrolling again. This is new in the v2 version and is not happening with v1.

https://github.com/user-attachments/assets/e2a6f56d-8c44-46d8-a542-2c43a7e9ec86

## Expected behavior

The scroll position should reset to 0 and the first items should be rendered.

## To Reproduce

Use this project: [FlashlistTestProject.zip](https://github.com/user-attachments/files/21264415/FlashlistTestProject.zip)
* Run on Android (`npm install && npm run android`)
* Select "Scroller test"
* Do a fling scroll
* While the scroll is still animating, press the "Jump to bottom" button

## Platform:

- [ ] iOS (not tested)
- [x] Android

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

FlashList 2.0 RC
React Native 0.80.1

===
