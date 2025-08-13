issue title: v2: maintainVisibleContentPosition doesn't work in horizontal
labels: bug
comment count: 2
hyperlink: https://github.com/shopify/flash-list/issues/1817
status: open
date opened: 2025-08-02
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

Flashlist fails to maintain the current scroll position when new items are added to the beginning in the case of `horizontal` being enabled. See two videos below:

https://github.com/user-attachments/assets/9afc00ae-a901-444e-8d6e-bcc190e369b4

https://github.com/user-attachments/assets/ffb85f38-2808-4232-bfb1-3765f5138f20

## Expected behavior

Regardless of the scroll orientation, the current element should be maintained upon adding data to either the beginning or the end.

## To Reproduce

<!-- Please provide a way to reproduce the problem if it's possible. Use the fixture app to create an example that reproduces the bug and provide a link to a GitHub repository under your username. -->

https://pastebin.com/K5nHe0bv

## Platform:

- [x] iOS
- [x] Android

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

2.0.1

===

comment #1 by d-rumal, 2025-08-02, 12:02:28
Same issue in horizontal, flashlist cannot maintain scroll position when onStartReached is called

comment #2 by PatiannaOlehZankiv, 2025-08-12, 08:18:16
The same issue. I have a horizontal list, and new items are coming from the websocket to the start of the list. My list jumping because of it. Please fix that.
