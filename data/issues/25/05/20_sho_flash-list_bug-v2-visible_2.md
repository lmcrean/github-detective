issue title: [Bug] [v2] Visible content position is not maintained when items are added and removed at the same time
labels: bug, P1, v2.0
comment count: 5
hyperlink: https://github.com/shopify/flash-list/issues/1667
status: open
date opened: 2025-05-20
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

I have a function that removes one item and adds new ones when the user reaches the start of the list (backward pagination). However, instead of maintaining a visible content position, it scrolls automatically to the top.

https://github.com/user-attachments/assets/7a898abd-23a7-4af2-b617-86d75a69d8b7

## Expected behavior

<!-- What do you expect to happen instead? -->

It should keep the current scroll position.

## To Reproduce

<!-- Please provide a way to reproduce the problem if it's possible. Use the fixture app to create an example that reproduces the bug and provide a link to a GitHub repository under your username. -->

https://github.com/jmysliv/rn-playground/tree/%40jmysliv/flash-list

## Platform:

- [x] iOS
- [ ] Android

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

2.0.0-alpha.11

===

comment #1 by naqvitalha, 2025-05-21, 17:18:43
That's a good edge case. I'll fix it in the next release.

comment #2 by naqvitalha, 2025-05-21, 17:47:26
I looked at your sample. It would be great to have a sample where data isn't tied to the component. With every render and index change, the size of the component can change. It might be a real use case however, it makes debugging a single issue very difficult. Let me know if you can provide a simpler one otherwise I'll come to this when I have some more time.

comment #3 by jmysliv, 2025-05-22, 09:48:44
@naqvitalha got it. Here I pushed a simpler example, with data extracted out of the component: https://github.com/jmysliv/rn-playground/tree/%40jmysliv/simpler-flash-list.

Note: I've noticed that it doesn't happen every time. Sometimes it works correctly, and sometimes it scrolls to the top and the position is not maintained.

comment #4 by jmysliv, 2025-07-24, 13:54:06
@naqvitalha Is there any progress on this one? Can I help fix it somehow? It's probably the biggest blocker for us currently.

comment #5 by naqvitalha, 2025-07-24, 17:01:50
We're occupied with other new arch optimization. It might be a while before we get to this. I think you should be able to workaround this in your app for now. You can just scroll down on data change.
