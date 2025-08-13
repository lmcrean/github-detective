issue title: React Native 0.80.1 in new Arch - lost items when scrolling
labels: bug
comment count: 8
hyperlink: https://github.com/shopify/flash-list/issues/1771
status: open
date opened: 2025-07-11
repo 30d_merge_rate: 7

====

description:
In the new React Native 0.80.+ when scrolling using FlashList - the items will disappear when scrolling back up. This is new and had to revert to React Native FlatList to fix it.


===

comment #1 by cjhlette, 2025-07-14, 14:23:08
+1

comment #2 by naqvitalha, 2025-07-14, 18:36:01
Is this issue with v1 or v2? If you're on new arch please use v2.

comment #3 by cjhlette, 2025-07-15, 12:06:11
Occurs in v1 and is normal in v2 I'm waiting for v2 release

comment #4 by naqvitalha, 2025-07-15, 17:22:09
You can ship one of the v2 RCs. They're production ready.

comment #5 by billnbell3, 2025-07-15, 19:13:09
OK we will try v2 RC

comment #6 by Prajwaltechversant, 2025-07-18, 08:56:23
HI @naqvitalha , i have the white space or gap issue in flashlist v2 and new acrhcitecture . i have tried the new props form v2 and verified the keyextractor duplication. everything is fine , but i am getting the white space issue while scrolling. is there any workarounds to fix this.
The list was properly working without any gap in old architecture and flashlist v1



comment #7 by Yurii-Lutsyk, 2025-07-24, 11:10:07
> HI [@naqvitalha](https://github.com/naqvitalha) , i have the white space or gap issue in flashlist v2 and new acrhcitecture . i have tried the new props form v2 and verified the keyextractor duplication. everything is fine , but i am getting the white space issue while scrolling. is there any workarounds to fix this. The list was properly working without any gap in old architecture and flashlist v1

I had the same problem after upgrade to the latest rn (0.80.1). But i've updated flashlist to 2.0.0-alpha.22 and it works fine (at least at first glance)

comment #8 by brianaderer, 2025-07-27, 17:27:11
Better with 2.0.0-alpha.22 but items still rendering in a very 'jumpy' way. Scroll down is fine, only on scroll up. reverting to FlatList solves it
