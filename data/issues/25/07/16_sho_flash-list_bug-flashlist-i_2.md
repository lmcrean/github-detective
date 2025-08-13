issue title: [BUG] FlashList inside Stack of expo-router overlapping content
labels: bug
comment count: 1
hyperlink: https://github.com/shopify/flash-list/issues/1787
status: open
date opened: 2025-07-16
repo 30d_merge_rate: 7

====

description:
## Current behavior

Video attached below. 
https://youtube.com/shorts/YdR7z7DchoU

## Expected behavior

Images shouldn't be overalapping, I had to switch to FlatList from RN.

## To Reproduce

Create a Stack Navigator with expo-router, and presentation set as modal. The animation from modal on iOS makes the FlashList items overlap 50% of the times. If i change presentation to card then issue disappears. To keep it as modal I had to switch to FlatList and issue is gone.

## Platform:

- [X ] iOS
- [ ] Android

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

"@shopify/flash-list": "1.7.6",
"expo-router": "~5.1.3",
"react": "19.0.0",
"react-native": "0.79.5",



===

comment #1 by maxoschepkov, 2025-07-30, 19:05:52
Same issue. 
Flashlist breaks layout of components while switching between tabs/screens.
