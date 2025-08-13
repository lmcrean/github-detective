issue title: Scrolling jumps when removing data for invisible items
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1786
status: open
date opened: 2025-07-16
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

This test case limits the number of data pages in memory by removing a page from the other end of the list when a new page of data is loaded. But this causes a sudden jump in the scrolling when data items are removed even though none of those items are visible.

https://github.com/user-attachments/assets/bfd2a300-2d53-4e61-825c-1a4d5820382a

## Expected behavior

There should be no visible jump in the scrolling when data for invisible items is removed.

## To Reproduce

Use this project: [FlashlistTestProject.zip](https://github.com/user-attachments/files/21264415/FlashlistTestProject.zip)
* Run on Android (`npm install && npm run android`)
* Select "Limited pages in memory"
* Keep scrolling up until you observe a jump

## Platform:

- [ ] iOS (not tested)
- [X] Android

## Environment

FlashList 2.0 RC
React Native 0.80.1

===
