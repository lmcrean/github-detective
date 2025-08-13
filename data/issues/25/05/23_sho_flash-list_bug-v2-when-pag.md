issue title: [Bug] [v2] When pagination is triggered in both directions, autoscroll to bottom doesn't work
labels: bug, P1, v2.0
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1671
status: open
date opened: 2025-05-23
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

<!-- What code are you running and what is happening? Include a screenshot or video if it's a UI related issue. -->

I have a list with `maintainContentVisiblePosition` prop and `autoScrollToBottomThreshold` set to `0.2`. When backward and forward pagination is enabled, it might happen that they are both triggered at the same time, for example, when we render a short list. In such a case, autoscroll to the bottom doesn't work.

https://github.com/user-attachments/assets/5c95a84c-dd4e-40de-b2e2-b4837369632b

## Expected behavior

<!-- What do you expect to happen instead? -->

Autoscroll to bottom should work when both paginations are triggered.

## To Reproduce

<!-- Please provide a way to reproduce the problem if it's possible. Use the fixture app to create an example that reproduces the bug and provide a link to a GitHub repository under your username. -->

https://github.com/jmysliv/rn-playground/tree/%40jmysliv/simpler-flash-list

## Platform:

- [x] iOS
- [ ] Android

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

2.0.0-alpha.11


===
