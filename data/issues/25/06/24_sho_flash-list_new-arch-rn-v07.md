issue title: New arch RN v0.79.4 performance issues
labels: bug, v2.0
comment count: 11
hyperlink: https://github.com/shopify/flash-list/issues/1751
status: open
date opened: 2025-06-24
repo 30d_merge_rate: 7

====

description:
## Current Behavior

My app contains a highly complex list with intensive calculations and was working perfectly on React Native v0.76.9 (old architecture). However, after upgrading to RN v0.79.4 with the new architecture and FlashList `v2.0.0-rc.9`, I'm encountering two major issues:

1. **White screen while navigating** to the screen containing FlashList — this is temporarily resolved by switching from `@react-navigation/stack` to `@react-navigation/native-stack`, but that workaround is not ideal or reliable. Please provide a proper fix. This issue doesn't get reproduced when I use flatlist instead of flashlist *(Please see the attached video demonstrating the issue.)*

https://github.com/user-attachments/assets/35baccd2-71ba-4e66-b404-5c95f6f05a02

2. **Blank spaces while scrolling** — some items intermittently render with gaps while scrolling. *(Refer to the attached video for context.)*

https://drive.google.com/file/d/15tWcuMaiL_x6XGP5e5TsnvUXUqQ1gJxS/view?usp=sharing

I've tried all the new v2 props and confirmed that there are no duplicate keys in the list, but the issues still persist.

Any insights or suggestions would be greatly appreciated.

---

## Expected Behavior

FlashList should render consistently and reliably during navigation and scrolling without visual glitches such as white screens or blank spaces, regardless of the navigator stack used.

---

## To Reproduce

Unfortunately, I’m unable to create a minimal repro since the issue doesn't occur in simple list setups. Due to the complexity and confidentiality of the project, I’m unable to share the actual source code.

---

## Platform

- [✔️] iOS  
- [✔️] Android  

---

## Environment

- **FlashList Version:** `2.0.0-rc.9`  
- **React Native Version:** `0.79.4` (New Architecture)


===

comment #1 by victormarques-ia, 2025-06-26, 01:14:00
I'm facing the same issue. I have a fairly complex list since I need to render horizontal lists inside a vertical FlashList, and each horizontal list contains product cards that interact with the cart. I've never been able to make it fully performant, but with FlashList v2 it's become unusable—no matter what I try, I can't find a solution.

comment #2 by AjayFrancisTechversant, 2025-06-26, 04:34:04
@victormarques-ia , same situation i guess

comment #3 by vanntrong, 2025-06-30, 15:34:18
Hello @AjayFrancisTechversant I'm facing the same issue. Have you fix this?

comment #4 by AjayFrancisTechversant, 2025-07-01, 04:35:59
@vanntrong 
No, I'm still stuck here.

comment #5 by anhbuidev, 2025-07-08, 09:01:20
I got pretty similar issue too. My Flastlist is rendered inside the `react-native-modalfy` for modal behaviour. The modal will call api to get data to display to the list. After getting the new data, the list was not render any item to screen until I`touch` the modal. 

Note that the `ListFooterComponent` that I used to render the loading skeleton is working as expected. And the issue just appears randomly so I cannot reproduce to consider what's going wrong

Does any one facing the same issue?

Here is my render code inside the modal.

```jsx
<View flex={1} width={'100%'}>
	<FlashList
		data={itemList}
		renderItem={(props) => (
			<RenderItem
				{...props}
				onAddItemClick={onAddRecommendItemClick}
				onIncreaseItemClick={onIncreaseItemClick}
				onRemoveItemClick={onRemoveRecommendItemClick}
				onSubtractItemClick={onSubtractRecommendItemClick}
				onUpdatePizzaClick={onUpdateRecommendItemClick}
			/>
		)}
		estimatedItemSize={itemHeight}
		ListFooterComponent={
			isLoading ? (
				<YStack gap={16}>
					<Skeleton />
					<Skeleton />
					<Skeleton />
					<Skeleton />
				</YStack>
			) : null
		}
	/>
</View>
```

comment #6 by lovegaoshi, 2025-07-10, 18:42:41
I also saw performance degradation albeit not exactly on your issue. Specifically my case is a custom/complex  cellRendererComponent causing performance loss - I had to use [a state to selectively load it](https://github.com/lovegaoshi/react-native-flashdrag-list/commit/3850e1ee2929c0e24c82dc625deee6625389dc7f) to ensure no performance loss when state is OFF. This was NOT an issue in the old arch. 

curious for the white screen - could u remove components and isolate what exactly lead to this lag in rendering? eg if you do data=[] does it happen? if u remove certain elements in flashlist itself does it happen?

comment #7 by Prajwaltechversant, 2025-07-18, 09:03:31
Hi @lovegaoshi ,
Just an update regarding Issue number 1 (white screen) reported by @AjayFrancisTechversant — this has been resolved by replacing Stack Navigation with Native Stack.

However, I'm still facing Issue number 2:

Blank spaces while scrolling — some items intermittently render with gaps while scrolling. (Refer to the attached video for context.)

Is there any known workaround or recommended fix for this issue?

comment #8 by saif-techversant, 2025-07-18, 09:07:27
+1 
I’m also experiencing this issue and actively looking for a workaround or solution.

comment #9 by AjayFrancisTechversant, 2025-07-18, 09:26:32
@lovegaoshi , about the white screen issue, i tried data=[], still white screen exists


comment #10 by colaquecez, 2025-07-27, 01:27:50
Im having the same issue on android, when using the old arch it works perfectly, but when I enable the new arch the list just break for android(empty spaces, triggering the scroll events wrongly etc)

comment #11 by colaquecez, 2025-07-27, 15:31:22
I've updated to alpha-22 and removed a Tamagui component that was using enterStyle. It seems the new FlashList version is conflicting with Tamagui when using their out-of-the-box animations.

code removed:
```js
    enterStyle={{
    opacity: 0,
     scale: 0.5,
     }}
     animation={'bouncy'}
     exitStyle={{
      opacity: 0,
      }}
```
