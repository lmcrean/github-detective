issue title: [Bug] [v2] "contentContainerStyle" prop shows error when passing a "ViewStyle" value
labels: bug, v2.0
comment count: 1
hyperlink: https://github.com/shopify/flash-list/issues/1683
status: open
date opened: 2025-05-31
repo 30d_merge_rate: 7

====

description:
From this comment: https://github.com/Shopify/flash-list/issues/848#issuecomment-2917298178 it became apparent to me that we can now add more values to the "contentContainerStyle" prop in Flashlist v2.

I'm using _"@shopify/flash-list": "^2.0.0-rc.2",_

It seems that we can now add ViewStyle values to the "contentContainerStyle" prop. The problem is that if we add a value that's not in this list:
```
 "backgroundColor"
  | "paddingTop"
  | "paddingLeft"
  | "paddingRight"
  | "paddingBottom"
  | "padding"
  | "paddingVertical"
  | "paddingHorizontal"

```
typescript will give you the following error:
> Object literal may only specify known properties, and 'flexGrow' does not exist in type 'ContentStyle'.ts(2353)
> FlashListProps.d.ts(103, 5): The expected type comes from property 'contentContainerStyle' which is declared here on type 'IntrinsicAttributes & IntrinsicClassAttributes<FlashList<BuddyHabit>> & Pick<Readonly<FlashListProps<BuddyHabit>>, "scrollEnabled" | ... 184 more ... | "onCommitLayoutEffect"> & InexactPartial<...> & InexactPartial<...>'


We can get around this by doing:
`import { ViewStyle } from "react-native"`
and then
`contentContainerStyle={{ flexGrow: 1 } as ViewStyle}`

but we shouldn't have to do this as I can see that ContentStyle is updated to include ViewStyle, yet it doesn't detect it. In _FlashListProps.ts_ we have:

```
export type ContentStyle = Pick<
  ViewStyle,
  | "backgroundColor"
  | "paddingTop"
  | "paddingLeft"
  | "paddingRight"
  | "paddingBottom"
  | "padding"
  | "paddingVertical"
  | "paddingHorizontal"
>;
```

===

comment #1 by naqvitalha, 2025-06-02, 18:26:25
It's a temporary thing because v2 is using v1 as a fallback on old arch. I'll change it soon.
