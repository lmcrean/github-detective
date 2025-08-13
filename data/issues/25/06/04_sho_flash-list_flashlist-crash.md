issue title: Flashlist crashes expo web
labels: bug, v2.0
comment count: 4
hyperlink: https://github.com/shopify/flash-list/issues/1697
status: open
date opened: 2025-06-04
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

Flashlist v2 crashes on expo web. 

I see the following error:
```tsx
Uncaught ReferenceError: exports is not defined
    node_modules bundle.js:94397
    Webpack 51
[useDataMultiplier.ts:8]
(.../node_modules/@shopify/flash-list/src/benchmark/useDataMultiplier.ts)
```

## Expected behavior

Flashlist should not crash.

## To Reproduce

Create a flashlist and start expo web.

## Platform:

- [ ] iOS
- [ ] Android
- [x] Web

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

^2.0.0-rc.2


===

comment #1 by naqvitalha, 2025-06-04, 22:32:24
Are you using the benchmark by any chance? Our fixture uses expo web and I don't see any issues. Which version of expo are you using?

comment #2 by SamuraiF0x, 2025-06-06, 16:44:04
Not using the benchmark. I'm using `"expo": ^53.0.7` and `"@shopify/flash-list": "^2.0.0-rc.2"`

comment #3 by SamuraiF0x, 2025-06-06, 16:53:00
Updated to `"@shopify/flash-list": "^2.0.0-rc.4"`, still the same issue

comment #4 by SamuraiF0x, 2025-06-17, 17:22:52
I get those errors. when I import like this:
```tsx
import { FlashList, useMappingHelper } from '@shopify/flash-list';
```

It works when importing this way:

```tsx
import FlashList from '@shopify/flash-list/dist/FlashList';
import { useMappingHelper } from '@shopify/flash-list/dist/recyclerview/hooks/useMappingHelper';
```
