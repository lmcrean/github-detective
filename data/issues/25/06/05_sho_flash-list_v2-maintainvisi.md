issue title: [v2] maintainVisibleContentPosition - there is no way to disable scroll animation
labels: bug, v2.0
comment count: 2
hyperlink: https://github.com/shopify/flash-list/issues/1698
status: open
date opened: 2025-06-05
repo 30d_merge_rate: 7

====

description:
When `maintainVisibleContentPosition` is configured on a FlashList, any time the list prepending or appending items, it always performs the scroll using the default animation. There is no way to opt out of or disable that animation.

In our use case (a chat interface), we need the list to “jump” immediately to the new position rather than animate, but `maintainVisibleContentPosition` does not expose any property to turn off animations. By contrast, calling methods like `scrollToIndex` or `scrollToOffset` allow passing `animated: false` to disable animation.

To reproduce render a FlashList with:

```
<FlashList
  //...
  maintainVisibleContentPosition={{
    startRenderingFromBottom: true,
    autoscrollToBottomThreshold: 0.1,
    // no “animated” flag is available here
  }}
/>
```

and append new items to `messages` array.

===

comment #1 by naqvitalha, 2025-06-08, 00:59:29
We reuse `autoScrollToTopThreshold` from `ScrollView` so there's no way to stop that. We can have an option to disable the animation when scrolling to the end automatically. I'll look into it.

comment #2 by naqvitalha, 2025-06-19, 11:04:12
This option is now available in alpha.20. Can you try it?
