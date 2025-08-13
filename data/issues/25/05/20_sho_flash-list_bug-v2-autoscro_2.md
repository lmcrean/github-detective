issue title: [Bug] [v2] Autoscroll to bottom doesn't work when items are changing its size
labels: bug, P1, v2.0
comment count: 6
hyperlink: https://github.com/shopify/flash-list/issues/1666
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

I have a chat interface and I want it to open on the latest message. To achieve that I'm using `maintainVisibleContentPosition` with the following config:

```
maintainVisibleContentPosition={{
  startRenderingFromBottom: true,
  autoscrollToBottomThreshold: 0.2,
}}
```

However, when items are changing their size, autoscroll to the bottom doesn't work.

https://github.com/user-attachments/assets/a7a0dad7-f840-42cc-89b6-6afb6a0301b1

## Expected behavior

<!-- What do you expect to happen instead? -->

The list should keep the scroll position at the bottom, even when the size of item changes.

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

comment #1 by naqvitalha, 2025-05-21, 17:51:01
The feature is designed to scroll on data change and not on item size change. Can you explain the use case to me? You can always call `scrollToEnd` yourself if you need to.

comment #2 by jmysliv, 2025-05-22, 09:32:59
@naqvitalha Use Case: 
Chat Interface. We want the list to start at the bottom with the latest message. Some messages might have a URL in their text, and for them, we display a URL preview. It takes some time for the URL preview to render, and when it does, the message size changes, and the list loses its scroll position at the bottom. Instead, it should stick to the bottom.

comment #3 by naqvitalha, 2025-06-25, 04:25:31
@jmysliv I tried this use case in my samples and it's working. Did you test this one in alpha.20? Not sure if this test case is present in the simpler sample you provided.

comment #4 by jmysliv, 2025-06-25, 08:59:05
@naqvitalha it's in my other sample, and I can still reproduce it in `alpha.20`. 
https://github.com/jmysliv/rn-playground/tree/%40jmysliv/flash-list

comment #5 by naqvitalha, 2025-06-26, 12:17:58
@jmysliv When a few items change size then it works fine. The sample is an extreme case where everything changes size and in practice it might not be good user experience. As of now, we probably won't be solving for this edge case but I'd urge you to simplify it and see if it works. If it does then I'd like to close the issue.

comment #6 by jmysliv, 2025-06-27, 11:41:03
@naqvitalha, yes, this sample is an extreme case. In our app, it works in most cases, but such an extreme case sometimes happens, and it's currently a blocker for us. I would expect that when using the `startRenderingFromBottom` with `autoscrollToBottomThreshold`, the scroll position will be maintained at the bottom, no matter what is rendered above. 
