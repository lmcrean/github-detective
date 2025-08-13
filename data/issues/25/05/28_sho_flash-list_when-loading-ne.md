issue title: When loading new, Can not show RefreshControl
labels: bug
comment count: 1
hyperlink: https://github.com/shopify/flash-list/issues/1678
status: open
date opened: 2025-05-28
repo 30d_merge_rate: 7

====

description:
iOS 2.0.0-rc.1

When I click "click loading" button,RefreshControl can not show
```
import { useRef, useState } from "react";
import { RefreshControl, View, Text, Button } from "react-native";
import { MasonryFlashList } from "@shopify/flash-list";

export default function MyMasonryList() {
  const [refreshing, setRefreshing] = useState(false);
  const [data, setData] = useState([]);
  const listRef = useRef(null);

  const onRefresh = () => {
    setRefreshing(true);

    setTimeout(() => {
      setData([
        { id: "1", height: 100, color: "red" },
        { id: "2", height: 150, color: "blue" },
        { id: "3", height: 200, color: "green" },
        { id: "4", height: 100, color: "red" },
        { id: "5", height: 150, color: "blue" },
        { id: "6", height: 200, color: "green" },
        { id: "7", height: 100, color: "red" },
        { id: "8", height: 150, color: "blue" },
        { id: "9", height: 200, color: "green" },
        { id: "10", height: 100, color: "red" },
        { id: "11", height: 150, color: "blue" },
        { id: "12", height: 200, color: "green" },
        { id: "13", height: 100, color: "red" },
        { id: "14", height: 150, color: "blue" },
        { id: "15", height: 200, color: "green" },
      ]);
      setRefreshing(false);
    }, 2000);
  };

  const triggerRefresh = () => {
    listRef.current?.scrollToOffset({ offset: 0, animated: true });
    setTimeout(() => {
      onRefresh();
    }, 300);
  };

  return (
    <View style={{ flex: 1 }}>
      <Button title="click loading" onPress={triggerRefresh} />
      <MasonryFlashList
        ref={listRef}
        refreshing={refreshing}
        data={data}
        keyExtractor={(item) => item.id}
        numColumns={2}
        renderItem={({ item }) => (
          <View style={{ height: item.height, backgroundColor: item.color, margin: 4 }} />
        )}
        refreshControl={<RefreshControl refreshing={refreshing} onRefresh={onRefresh} />}
        ListEmptyComponent={
          <View style={{ height: 400, justifyContent: "center", alignItems: "center" }}>
            <Text>loading...</Text>
          </View>
        }
      />
    </View>
  );
}
```


===

comment #1 by KolissnikBogdan, 2025-07-01, 12:08:15
@xiaolu8866 try to change offset value (maybe -60)
