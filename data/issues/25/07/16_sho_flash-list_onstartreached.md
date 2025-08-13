issue title: onStartReached isn't always called on reaching the start of the list
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1785
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

The `onStartReached` callback isn't always called when the start of the list is reached. I have attached a project that reproduces a case where it's not called. Here onStartReached should trigger the loading of more data.

https://github.com/user-attachments/assets/901f763a-603f-45e8-b158-c385ad285953

## Expected behavior

`onStartReached` should be called when the start of the list is reached.

## To Reproduce

Use this project: [FlashlistTestProject.zip](https://github.com/user-attachments/files/21264415/FlashlistTestProject.zip)
* Run on Android (`npm install && npm run android`)
* Select "Start at top"
* Scroll downwards until you reach the bottom
* Observe that the last item starts with "6 72 ..." and no more items load after that.

## Platform:

- [ ] iOS (not tested)
- [X] Android

## Environment

FlashList 2.0 RC
React Native 0.80.1


===
