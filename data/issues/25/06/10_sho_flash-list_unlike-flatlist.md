issue title: Unlike FlatList, which resizes properly when the screen dimensions change, the FlashList container does not adjust its size correctly.
labels: bug, v2.0
comment count: 6
hyperlink: https://github.com/shopify/flash-list/issues/1717
status: open
date opened: 2025-06-10
repo 30d_merge_rate: 7

====

description:
Unlike FlatList, which resizes properly when the screen dimensions change, the FlashList container does not adjust its size correctly.
videoUrl:  https://file.douqianba.com/file/doumaoappqianduan-mp4/2025-6-10/1749531823728_49956.mp4

===

comment #1 by xtayaitak, 2025-06-11, 14:42:41
@418442040 I'm also has this problem. I'm also in China. My email zds1275161667@163.com or wechat me .

comment #2 by 418442040, 2025-06-18, 08:31:45
> [@418442040](https://github.com/418442040) I'm also has this problem. I'm also in China. My email [zds1275161667@163.com](mailto:zds1275161667@163.com) or wechat me .

你有什么好的解决方案吗?

comment #3 by naqvitalha, 2025-06-19, 11:03:34
We've made some improvements to chat experience in v2.0.0-alpha.20. Can you please try and let use know if it's better?

comment #4 by 418442040, 2025-06-19, 11:20:22
> We've made some improvements to chat experience in v2.0.0-alpha.20. Can you please try and let use know if it's better?

In fact, it still does not work properly. The code is as follows. You can freely switch between FlatList and FlashList.

The current environment is React Native 0.80.0.

import { FlashList } from '@shopify/flash-list';
import { View, Text, TextInput, FlatList, Platform } from 'react-native';
import {
  KeyboardProvider,
  KeyboardAvoidingView,
} from 'react-native-keyboard-controller';
import Markdown from 'react-native-marked';

const list = [1, 2, 3, 4, 5, 6];

export default () => {
  return (
    <KeyboardProvider>
      <KeyboardAvoidingView behavior="padding" style={{ flex: 1 }}>
        <FlashList
          // maintainVisibleContentPosition={{
          //   autoscrollToTopThreshold: 999999,
          //   startRenderingFromBottom: true,
          // }}
          // estimatedItemSize={Platform.OS === 'ios' ? 554 : 801}
          data={list}
          keyExtractor={(item) => item.toString()}
          inverted
          renderItem={() => {
            return (
              <View style={{ backgroundColor: 'pink', marginBottom: 20 }}>
                <Markdown
                  value={`# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world# Hello world`}
                  flatListProps={{
                    initialNumToRender: 8,
                    scrollEnabled: false,
                  }}
                />
              </View>
            );
          }}
        />
        <TextInput
          style={{ backgroundColor: 'red', width: 300, height: 50 }}
        />
      </KeyboardAvoidingView>
    </KeyboardProvider>
  );
};


comment #5 by naqvitalha, 2025-06-24, 07:35:04
If you can provide a reproducible expo snack then I'll be able to look into this quickly.

comment #6 by creix, 2025-07-30, 10:00:40
I also have the same problem using v2.0.0-rc.12

https://github.com/user-attachments/assets/267dd308-e18b-4236-aa3a-36d8e83e17a1

Currently i'm using the KeyboardAvoidingView from react-native-keyboard-controller

This is my setup:

```jsx
<SafeAreaView className="flex-1" edges={['bottom']}>
  <KeyboardAvoidingView 
    style={{ flex: 1 }}
    behavior="translate-with-padding"
    keyboardVerticalOffset={90}
  >
    <View className="flex-1 bg-white">
      <FlashList
        ref={listRef}
        data={items}
        renderItem={renderItem}
        estimatedItemSize={50}
        keyExtractor={(item) => {
          return item._id; 
        }}
        getItemType={getItemType}
        ListEmptyComponent={renderEmptyComponent}
        showsVerticalScrollIndicator={false}
        contentContainerStyle={{ paddingTop: 16, paddingBottom: 8}}
        extraData={items.length}
        maintainVisibleContentPosition={{
          autoscrollToBottomThreshold: 0.2,
          startRenderingFromBottom: true,
          animateAutoScrollToBottom: true
        }}
      />
    </View>
  </KeyboardAvoidingView>
</SafeAreaView>
```

