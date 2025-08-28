issue title: V2: MVCP not adjusting position when item above changes layout
labels: bug
comment count: 1
hyperlink: https://github.com/shopify/flash-list/issues/1823
status: open
date opened: 2025-08-04
repo 30d_merge_rate: 7

====

description:
<!-- Thanks for taking the time to fill out this bug report!

If this is not a bug report, please use other relevant channels:
- [Create a feature proposal on Discussions](https://github.com/Shopify/flash-list/discussions/new)
- [Chat with others in the #flash-list channel on Shopify React Native Open Source Discord](https://discord.com/channels/928252803867107358/986654488326701116)

Before you proceed:

- Make sure you are on latest versions of the FlashList package.
- If you are having an issue with your machine or build tools, the issue belongs on another repository as that is outside of the scope of FlashList. -->

## Current behavior

- List with items 
- `maintainVisibleContentPosition` active
- An item is aligned to the top edge of the list (ie. `initialScrollIndex` or user scrolled there)
- A react update changes one of the items above the current top item to change its height
- The item we were previously scrolled to doesn't stay in position, or it does but there is a flickering

| Repro in fixture | In a production app |
|--------|--------|
| <video src="https://github.com/user-attachments/assets/0c694b25-1fb5-4e67-9fd5-9aeab09538b4" /> | <video src="https://github.com/user-attachments/assets/fbbf0638-bfd1-4b44-ace1-b5d55a9e96c7" /> | 

In the video from the _production app_ we can see how:
1. We click on the image with the glass, however on the first frame we aren't scrolled to the right position
2. On the second frame the image with the glass is correctly positioned
3. On the third frame the item above the glass has changed its height and we can see how the glass image got pushed down
4. On the forth frame the glass image is back its correct position



## Expected behavior

<!-- What do you expect to happen instead? -->

When using `maintainVisibleContentPosition` and `initialScrollIndex` there should be no erratic flickering. 

## To Reproduce

<!-- Please provide a way to reproduce the problem if it's possible. Use the fixture app to create an example that reproduces the bug and provide a link to a GitHub repository under your username. -->

https://github.com/margelo/flash-list/tree/reproduction-scroll-mvcp-issue
- Specifically: https://github.com/margelo/flash-list/blob/reproduction-scroll-mvcp-issue/fixture/react-native/src/MVCPExample.tsx

Note: this is **not** reproducible with a plain React Native `ScrollView`.

## Platform:

- [x] iOS
- [ ] Android (Potentially android as well, haven' tested yet)

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

2.0.1


===

comment #1 by naqvitalha, 2025-08-05, 17:03:18
Thanks for reporting this issue. I might not be able to get to it this week but it'll be on my list for next week.
