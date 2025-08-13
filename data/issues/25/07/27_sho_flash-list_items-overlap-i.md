issue title: Items overlap in FlashList v2
labels: bug
comment count: 7
hyperlink: https://github.com/shopify/flash-list/issues/1797
status: open
date opened: 2025-07-27
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

Trying to migrate to v2 (`2.0.0-rc.12`) and having issues with items being overlapped (for some items only). I am working on the Bible app and items (chapters) are sometimes very different in size.

For example, in the book of Psalms there are 150 psalms in total and there are psalms with just a few verses, but there are also psalms with 170+ verses. When trying to scroll to some items (i.e. user tries to navigate to a specific psalm) I see some items being rendered on top of each other. This happens quite consistently and is a major problem.

In v1 I was using size estimates and didn't have such problem.

<img width="300" alt="Image" src="https://github.com/user-attachments/assets/eef080e7-32d0-46cc-b8e4-c09b5d2804aa" />

## Expected behavior

Items are rendered one after another without overlap.

## To Reproduce

The code is not public at the moment and I don't have an example app to reproduce the issue. I can try creating one if that proves to be necessary, but I hope someone knows what might be the issue.

<!-- Please provide a way to reproduce the problem if it's possible. Use the fixture app to create an example that reproduces the bug and provide a link to a GitHub repository under your username. -->

## Platform:

- [x] iOS
- [ ] Android

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

@shopify/flash-list: `2.0.0-rc.12`
react-native: `0.80.1`


===

comment #1 by naqvitalha, 2025-07-28, 20:58:49
Are you using any library to rendering text or is it `Text` from RN? I'd appreciate if you can provide some kind of repro for this.

comment #2 by maxoschepkov, 2025-07-30, 19:03:36
Having the same issue. 
Also noticed that the content of the list leaves artifacts when switching between tabs/screens (background of the content stays under different screen, or even it overlaps with a content). My content contains text from rn components, video components, images inside lists.

<img width="1695" height="613" alt="Image" src="https://github.com/user-attachments/assets/6115733c-f9a1-4e14-8789-bc3be5d1d5b5" />

comment #3 by cletter7, 2025-07-30, 19:40:34
@naqvitalha I am using `react-native-styled-text` for rendering text. I will try with normal text and let you know, but can this be a root cause?

comment #4 by cletter7, 2025-07-31, 08:13:44
I replaced styled text with a `Text` from RN and the problem is still there. I will try to create a reproducible example in the following days.

comment #5 by YasserDbeis2, 2025-08-08, 02:24:41
Bump!

comment #6 by YasserDbeis2, 2025-08-08, 02:25:18
@naqvitalha can you please priortiize this? It basically makes this unusable :(

comment #7 by cletter7, 2025-08-10, 14:15:45
@naqvitalha 
I am trying to create a reproducible lightweight app, but so far I haven't succeeded. In my lightweight newly created app everything seems to be working fine, but in the original one it does not. It seems that the issue has something to do with `initialScrollIndex`, when I remove this parameter the overlapping disappears, but I can't reproduce in the the lean app. In the real app I have so many things like react navigation, custom fonts, more complex layout, etc., so the issue might be a combination of things.
Maybe what I describe will help to debug the issue on your side?
