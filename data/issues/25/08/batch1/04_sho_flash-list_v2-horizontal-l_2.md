issue title: v2: Horizontal list overflow clipped
labels: bug
comment count: 2
hyperlink: https://github.com/shopify/flash-list/issues/1822
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

Overflow on horizontal lists is clipped.

<img width="520" height="66" alt="Image" src="https://github.com/user-attachments/assets/5a76dc2a-194c-4395-af5c-9b0d104b728d" />

## Expected behavior

Overflow visibility should be controllable via normal react-native overflow styles.

## To Reproduce

Setting `overflow: 'visible'` works for FlatList and LegendList but not FlashList.

https://github.com/ammar-madni/repro-flashlist-overflow-issue

## Platform:

- [x] iOS
- [x] Android

## Environment

v2.0.1


===

comment #1 by naqvitalha, 2025-08-05, 19:04:20
Can you try passing the style to inner ScrollView? You can do so by passing `overrideProps={{ style: { overflow: 'visible'} }}`.


comment #2 by ammar-madni, 2025-08-05, 19:37:44
> Can you try passing the style to inner ScrollView? You can do so by passing `overrideProps={{ style: { overflow: 'visible'} }}`.

<img width="1108" height="834" alt="Image" src="https://github.com/user-attachments/assets/4cb670f2-9851-4542-a597-71692a92cf0b" />

Overflow is still clipped I'm afraid.
