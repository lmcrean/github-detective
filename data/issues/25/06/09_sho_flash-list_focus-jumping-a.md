issue title: focus jumping and list disappears when scrolling in AndroidTV/FireTV/AppleTV
labels: bug
comment count: 2
hyperlink: https://github.com/shopify/flash-list/issues/1716
status: open
date opened: 2025-06-09
repo 30d_merge_rate: 7

====

description:
## Current behavior

I have a nested flast-list, so as to display the channels within the categories.
There are multiple categories and each category has multiple channels, so to display this data, I have implemented a vertical flash-list and a horizontal flash-list within the vertical flash-list.

While scrolling down the vertical list, the focus keeps jumping from 0th index to random index.
And some times, while scrolling, the list completely disappears showing empty space.

## Expected behavior
Expected behaviour is to have have the focus on the 0th index while scrolling in the vertical index. And also there should be no disappearance of the lsit.

Also please find attached a video of the issue.

## Platform:
AppleTV, AndroidTV, FireTV

## Environment
I initially discovered the issue in version number 1.8.2
I have also been able to reproduce this issue with the latest versions as well.

https://github.com/user-attachments/assets/b13558e5-c804-4c1c-9dad-f75162ccd887

The implementation of flash-list

<FlashList
						data={categories}
						renderItem={({ item, index }) => getComponentForCategory(item, index)}
						estimatedItemSize={ESTIMATED_SIZE}
						snapToAlignment="center"
						centerContent
						bounces={false}
						overScrollMode="never"
						ref={listRef}
						extraData={extraData || categories?.length}
						contentContainerStyle={{ paddingBottom: screenVPadding }}
						ItemSeparatorComponent={() => <View style={{ height: railVPadding, width: 1 }} />}
						showsVerticalScrollIndicator={false}
						overrideItemLayout={overrideItemLayout}
						getItemType={getItemType}
					/>


===

comment #1 by mohsinDPRO, 2025-06-10, 10:01:28
I've got the jumping focus to stop by implementing the following changes
<FlashList
	ref={listRef}
	data={categories}
	renderItem={({ index, item }) => getComponentForCategory(item, index)}
	estimatedItemSize={ESTIMATED_SIZE}
	extraData={extraData}
	showsVerticalScrollIndicator={false}
	contentContainerStyle={{ paddingBottom: screenVPadding }}
	scrollEnabled={!isAndroid}
	ItemSeparatorComponent={() => <View style={{ width: 1, height: screenVMargin }} />}
	estimatedListSize={{ height: SCREEN_HEIGHT, width: SCREEN_WIDTH }}
	getItemType={getItemType}
	scrollEventThrottle={32}
	keyExtractor={(category) => category.strId}
	overrideItemLayout={overrideItemLayout}
/>

few properties which are removed from the previous implementation are 
 - snapToAlignment="center"
 - centerContent
 - bounces={false}
 - overScrollMode="never"

This has stopped the jumping of focus to stop when scrolling vertically.
This is all I've figured so far with the above issue.

comment #2 by DalBrar, 2025-06-15, 04:24:12
I've a similar issue, nested horizontal list inside vertical lists on my Android TCL Smart TV.
- When scrolling the horizontal nested list slowly to the right the focus of the horizontal list goes off screen, then jumps back 5 items to the left to create an effect that looks like the focus is wrapping around on the screen while the item's themselves are loading into view.
- when scrolling the horizontal nested list really fast the items disappear and the list focus moves down to the next vertical list as if the list thought it reached the end of its content but then the items load and appear but now we're in a different horizontal list already
- also the onScroll(), onMomentumScrollEnd(), onScrollEndDrag() events only seem to fire when on screen content of the list changes, is there an event to detect when item focus changes?
