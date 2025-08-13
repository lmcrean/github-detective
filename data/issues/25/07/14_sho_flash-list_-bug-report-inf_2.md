issue title: 🐛 Bug Report: Infinite Render Loop in FlashList v2 (setRenderId)
labels: bug
comment count: 20
hyperlink: https://github.com/shopify/flash-list/issues/1773
status: open
date opened: 2025-07-14
repo 30d_merge_rate: 7

====

description:
We encountered a crash in FlashList v2 (flashlist@2.x.x) that causes a maximum update depth exceeded error. This issue does not occur in FlashList v1, making it a regression.

error : "Render Error  
Maximum update depth exceeded. This can happen when a component repeatedly calls setState inside componentWillUpdate or componentDidUpdate."


✅ Expected Behavior

FlashList should avoid triggering an infinite re-render loop when modifying layout or handling orientation changes.

![Image](https://github.com/user-attachments/assets/eb7db091-e141-4832-8746-8ee7fd6011b1)

🔄 Actual Behavior
FlashList v2 causes setRenderId to continuously update, triggering an infinite loop and crashing the app.

🔙 Regression
✅ Yes — this issue does not happen in v1, so it is a regression in v2.

✍️ Additional Notes
We tried using extraData and forcing keys to re-render, but it did not prevent the crash.

This may be linked to how modifyChildrenLayout() internally triggers updates.



===

comment #1 by Prajwaltechversant, 2025-07-14, 08:33:11
@naqvitalha i got this crash both in debug and release. in v1 works fine without this crash

comment #2 by Prajwaltechversant, 2025-07-14, 09:46:21
@naqvitalha i also tried this in flatlist, works fine there 

comment #3 by Prajwaltechversant, 2025-07-14, 10:46:20
 @naqvitalha  data={listData.filter(f => !!f)} or data={listData.slice()} fixes the crash ,data={[...listData])} fixes the crash , does this make any sense

comment #4 by tsdevshop, 2025-07-14, 16:32:32
Issue appears to be coming from [this line, which is setting state inside a useLayoutEffect with no deps](https://github.com/Shopify/flash-list/blob/e70a8028d883c3b90fdddcd7738e9124fee227bb/src/recyclerview/RecyclerView.tsx#L215). As a result, the state is set, component re-renders, which fires the `useLayoutEffect`, which sets the state, which re-renders the component... etc.

Perhaps we need a way to short-circuit this if the layout measurements aren't stable?

comment #5 by naqvitalha, 2025-07-14, 18:35:21
Some more details or a repro will be helpful. This issue only happens when there's something wrong with list setup like duplicate keys in `keyExtractor` or having a list inside a ScrollView causing all items to render at one. If it's neither then I can look into it.

comment #6 by Prajwaltechversant, 2025-07-15, 03:41:18
Hi @naqvitalha ,
I've verified that the keyExtractor is not generating any duplicate keys. The crash still occurs even when renderItem={null} or when the render component is not being used.

comment #7 by AjayFrancisTechversant, 2025-07-15, 09:35:37
@naqvitalha , any updates on this?


comment #8 by naqvitalha, 2025-07-15, 09:38:06
I'd appreciate a repro for this or some more details. A video might help too. We do render in a loop but it's always supposed to end unless your items keep changing their size or you're rendering too many to begin with (hundreds).
There can be some bug but since I don't have a repro, I can't do much. We also changed how we mount in alpha.21 so if this is happening on mount, you can try the new version.

comment #9 by Prajwaltechversant, 2025-07-16, 03:32:02
HI @naqvitalha ,
I'll check that in the alpha version. Do you have an estimated timeline for the RC (release candidate) version?

comment #10 by Prajwaltechversant, 2025-07-16, 08:29:42
Hi @naqvitalha , works fine in alpha release

comment #11 by Gothamoo7, 2025-07-16, 10:56:40
@Prajwaltechversant @naqvitalha I'm getting the same issue in alpha.21 as well, if the list has more than 50 items.
Any workaround?

comment #12 by Prajwaltechversant, 2025-07-16, 12:19:23
HI @Gothamoo7 , for me , the rendering issues is fixed in alpha 21.


comment #13 by Prajwaltechversant, 2025-07-16, 12:19:50
@Gothamoo7 data={listData.filter(f => !!f)} or data={listData.slice()} fixes the crash ,data={[...listData])} fixes the crash , try this

comment #14 by naqvitalha, 2025-07-16, 14:57:26
@Gothamoo7 Can you provide a repro (on expo snack) ? 50 items shouldn't cause this.

comment #15 by leecuong666, 2025-07-17, 03:21:19
same error occurs when nesting a horizontal FlashList inside a vertical FlashList and setting the item container's width to 100%

comment #16 by switz, 2025-07-18, 04:17:38
This shouldn't be closed unless the underlying bug was fixed

https://github.com/Shopify/flash-list/blob/e70a8028d883c3b90fdddcd7738e9124fee227bb/src/recyclerview/RecyclerView.tsx#L215

If this is the source it makes sense that it's triggering an infinite re-render. Shouldn't there be a deps list to prevent setRenderId from triggering the useLayoutEffect?

comment #17 by naqvitalha, 2025-07-18, 14:45:50
@switz That's by design and not an issue. We break out of the loop once layouts have finished computing. Again, if there's a repro I can look into it.

comment #18 by alecgorge, 2025-07-18, 16:56:27
unfortunately i'm not able to repro this either, but i do see hundred of crashes in sentry for it on my latest app release (w/rc-10) with this stack. i'm going to try going back to 1.8.3 for now

```
Error: Maximum update depth exceeded. This can happen when a component repeatedly calls setState inside componentWillUpdate or componentDidUpdate. React limits the number of nested updates to prevent infinite loops.

This error is located at:
 at FlashList
...
```

comment #19 by naqvitalha, 2025-07-21, 14:12:48
@alecgorge Do you have ScrollView that might have lists inside them? I will include a workaround to avoid this case in one of the future releases. Will it be possible for you to share one of the complete stack traces?

comment #20 by varungandhi121, 2025-08-08, 12:14:54
When I comment out onEndReached and onEndReachedThreshold, the list behaves normally. But when I enable onEndReached, the availableLoadMore() function gets called multiple times in a loop — even when the end of the list hasn't actually been reached.My first data size is 20. after at the end i load more 20 data and then crash happen and also i changing tab crash happen.
-also i change tab and that tab have no data then it crash.
  <FlashList
                renderItem={({ item, index, target, extraData }) => this.renderItem({ item, index, target, extraData })}
                data={[{ uuid: '909909', val: 0 }, { uuid: '923w09909', val: 1 }, ...this.listData]}
                onEndReached={() => this.availableLoadMore()}
                onEndReachedThreshold={0.1}
                showsVerticalScrollIndicator={true}
                refreshControl={<RefreshControl refreshing={this.isPullToRefresh} onRefresh={() => this.onRefresh()} />}
                stickyHeaderIndices={[1]}
                scrollEnabled={this.isLoading ? false : true}
                keyExtractor={(item, index) => {
                  // console.log('item', item);
                  return item?.uuid || item?.val;
                }}
                removeClippedSubviews={true}
                drawDistance={2000}
                style={styles.recyclerBackground}
                // extendedState={{
                //   searchText: projectsStore?.searchText || '',
                // }}
              />


![Image](https://github.com/user-attachments/assets/406e1f83-3791-439e-9f78-eb2591dc4eac)
![Image](https://github.com/user-attachments/assets/cd137ef9-7b04-4bb1-8570-79968dad92ee)
![Image](https://github.com/user-attachments/assets/8ba5e4ff-725d-4a1a-990f-7df430faab8f)
