issue title: Scroll position changes when navigating back to a list in react navigation stack
labels: bug
comment count: 1
hyperlink: https://github.com/shopify/flash-list/issues/1816
status: open
date opened: 2025-08-02
repo 30d_merge_rate: 7

====

description:
## Current behavior

Upon navigating backwards, the list's scroll position is different from where it was originally.

## Expected behavior

The scroll position should not change.

## Platform:

- [x] Web
- [ ] iOS
- [ ] Android

## Environment

2.0.1


===

comment #1 by ericpoulinnz, 2025-08-08, 21:41:18
@naqvitalha sorry for the tag but this is a longstanding issue (#635 ) which V2 has not fixed. It makes for a terrible UX for a very common use case involving lists.
