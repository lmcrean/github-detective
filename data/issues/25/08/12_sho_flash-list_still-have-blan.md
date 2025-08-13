issue title: still have blank cells in V2，RN 0.79.2
labels: bug, v2.0
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1833
status: open
date opened: 2025-08-12
repo 30d_merge_rate: 7

====

description:
## Current behavior

![Image](https://github.com/user-attachments/assets/450aa845-4cdf-4382-93d9-734b5c305590)

## Expected behavior

<img width="350" height="588" alt="Image" src="https://github.com/user-attachments/assets/24847eb7-9a26-44e1-b27c-409fa6e3a6b9" />

## To Reproduce

FlashList has a big header,and then has 2 numColumns.sometimes it still has blank cells.
And another QA, at this situation how to get item columnIndex,

```
<FlashList
  masonry
  contentInset={{ bottom: bottomSafePadding ?? 0 }}
  numColumns={2}
  nestedScrollEnabled={true}
  data={data}
  renderItem={renderItem}
  keyExtractor={keyExtractor}
  onEndReachedThreshold={2}
  onEndReached={onLoadMoreData}
  ListEmptyComponent={<ListLoadingOrEmptyView isLoading={firstLoading} />}
  ListFooterComponent={<ListLoadMoreFooter hasData={hasData} hasMoreData={hasMoreData} />}
  ListHeaderComponent={header}
  // ListHeaderComponentStyle={{ backgroundColor: 'green' }}
  onScroll={onScroll}
  scrollEventThrottle={Platform.OS === 'android' ? 32 : 16}
  contentContainerStyle={{
    // backgroundColor: 'red',
    paddingHorizontal: 0,
    // paddingHorizontal: RecommendCardViewLayout.listContentPadding, // 保证左右边距对称
  }}
/>
```

## Platform:

- [x] iOS
- [x] Android

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

2.0.2


===
