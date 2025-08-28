issue title: FlashList Small Gap Sometimes Between Items with Fractional Heights
labels: bug, v2.0
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1827
status: open
date opened: 2025-08-07
repo 30d_merge_rate: 7

====

description:
## Current behavior

When item heights are fractions then sometimes we see small gaps between items. It looks like some rounding error?

(Hard to see)
<img width="459" height="296" alt="Image" src="https://github.com/user-attachments/assets/f857875a-a7f2-47d5-9b03-bc46fad14ad5" />

## Expected behavior

Items should be positioned flush against one another.

## To Reproduce

Make items have a dynamic height which paints to a fractional height.

## Platform:

- [X] iOS
- [ ] Android

## Environment

`2.0.2`

===
