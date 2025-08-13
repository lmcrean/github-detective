issue title: Waterfall Layout with Severe Jumping Issues
labels: bug, v2.0
comment count: 1
hyperlink: https://github.com/shopify/flash-list/issues/1719
status: open
date opened: 2025-06-12
repo 30d_merge_rate: 7

====

description:
In waterfall layout, （masonry layout）severe jumping occurs when scrolling down after using scrollToIndex to navigate to a specific index. Similarly, after switching between narrow and wide screens on foldable devices with the same waterfall layout, scrolling down also triggers significant jumping.

version: "@shopify/flash-list": "^2.0.0-rc.4",

```
<FlashList
            ref={v=>{(this.listRef=v)}} 
            data={this.state.cardViewModelList}
            numColumns={2}
            masonry
            scrollEventThrottle={1}
            renderItem={this.renderItem}
            maintainVisibleContentPosition={{
              disabled: true,
            }}
            estimatedItemSize={200}
      />
```

===

comment #1 by housl, 2025-06-12, 07:24:34
瀑布流布局，严重跳动：
瀑布流布局，当通过scrollToIndex:滚动到某个index后，再下拉浏览时，会出现严重跳动。
同样的瀑布流布局时，在折叠屏宽窄屏切换后，再下拉浏览，同样严重跳动
