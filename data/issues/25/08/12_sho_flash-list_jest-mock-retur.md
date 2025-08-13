issue title: Jest mock returns `undefined`
labels: bug, v2.0
comment count: 1
hyperlink: https://github.com/shopify/flash-list/issues/1834
status: open
date opened: 2025-08-12
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
I'm trying to test my component which is based on `FlashList` (right now 2.0.0 as I'm migrating) and the mock returns `undefined` instead of mocked component.


## Expected behavior
The mock is successfully returned.
<!-- What do you expect to happen instead? -->

## To Reproduce
Just import flashlist mock in your `jestSetup`
<!-- Please provide a way to reproduce the problem if it's possible. Use the fixture app to create an example that reproduces the bug and provide a link to a GitHub repository under your username. -->

## Platform:

- [ ] iOS
- [ ] Android

## Environment
2.0.0, on the 1st version it works fine


===

comment #1 by zfurtak, 2025-08-12, 11:28:10
I assume that the problem is caused by using `RecyclerView` in the mock which is not exported in the `@shopify/flash-list/src/index.ts`. After deleting it, everything works fine.

```ts
jest.mock("@shopify/flash-list", () => {
  const RecyclerView = jest.requireActual("@shopify/flash-list").RecyclerView;

  return {
    ...jest.requireActual("@shopify/flash-list"),
    FlashList: RecyclerView,
  };
});
```
