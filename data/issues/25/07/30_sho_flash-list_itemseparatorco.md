issue title: ItemSeparatorComponent is rendered on second to last item when numColumns={2}
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1809
status: open
date opened: 2025-07-30
repo 30d_merge_rate: 7

====

description:
## Current behavior

I noticed that when numColumns is set to 2, so two items are in each row, separator is rendered on the second to last item, and so it creates unnecessary spacing at the bottom of the list

## Expected behavior

Expected behavior should be that separator is rendered on items whose index is smaller than items length minus number of columns (index < data.length - numColumns)

## Environment

1.7.6v


===
