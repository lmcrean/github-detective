issue title: WebView injectedJavaScript won't run in v2
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1794
status: open
date opened: 2025-07-22
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
I am on @shopify/flash-list 2.0.0-rc.11. When I use a WebView inside an item with injectedJavaScript, the javascript injected doesn't run

## Expected behavior

<!-- What do you expect to happen instead? -->
The injectedJavaScript runs as if it's not inside the item.

## To Reproduce

<!-- Please provide a way to reproduce the problem if it's possible. Use the fixture app to create an example that reproduces the bug and provide a link to a GitHub repository under your username. -->
It's could be very simple, you can try to change the background color with injectedJavaScript in WebView. You will see that outside of the item it works correctly, and inside the item the injectedJavaScript doesn't work.

## Platform:

- [x] iOS
- [x] Android

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

x.y.z


===
