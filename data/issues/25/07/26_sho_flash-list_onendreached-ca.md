issue title: onEndReached calls infinitilly in v2
labels: bug
comment count: 2
hyperlink: https://github.com/shopify/flash-list/issues/1795
status: open
date opened: 2025-07-26
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

I use base Flashlist component with onEndReached prop for pagination. It works as expected in v1, but in version v2(2.0.0-rc.12, 2.0.0-alpha.22) onEndReached calls infinitly at the end of list when there are no items left. 

## Expected behavior

onEndReached should calls only once at the end of list

## To Reproduce

<!-- Please provide a way to reproduce the problem if it's possible. Use the fixture app to create an example that reproduces the bug and provide a link to a GitHub repository under your username. -->

## Platform:

- [x] iOS
- [x] Android

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

x.y.z


===

comment #1 by Yurii-Lutsyk, 2025-07-26, 14:13:27
Sorry for the poor description, i can attach some code later, but what has been changed in the v2 version?

comment #2 by dengcqw, 2025-08-11, 09:51:48
check onEndReachedThreshold, it is less then 1
