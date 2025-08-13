issue title: onEndReached fires on mount in FlashList and never fires again if INITIAL_ITEM_COUNT is low...
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1789
status: open
date opened: 2025-07-20
repo 30d_merge_rate: 7

====

description:
Hey, I'm building a little Instagram‑style profile screen is driving me up the wall. I have a big 500 px profile header and then a 3‑column grid of photos. With FlatList everything’s fine: I start with 6 items, onEndReached fires only when I actually scroll, and I page in 9 more. But with FlashList the callback fires the moment the list mounts (so I waste a network request), and after that it never fires again no matter how far I scroll. I’ve tried Animated/ non‑Animated lists, moving the header inside the list, flex/no‑flex—nothing changes this behaviour, and I really need to avoid fetching more posts than necessary.

Could you please take a look? Below are two drop‑in components that reproduce the issue in a fresh RN project. The only difference is the list component—FlatList works, FlashList doesn’t.

Thanks in advance!

FlatList Video:
https://github.com/user-attachments/assets/27f7b875-5c3e-497d-86b7-f53743daed11

FlashList Video:
https://github.com/user-attachments/assets/b42a8946-16f0-4e01-a3ad-82601757725e

FlashList Code:
```
import React, { useState, useCallback, useEffect, useRef } from "react";
import { View, Text, StyleSheet, ActivityIndicator, useWindowDimensions, Animated } from "react-native";
import { FlashList } from "@shopify/flash-list";

const INITIAL_ITEM_COUNT = 6;
const HEADER_HEIGHT = 500;
const SUBSEQUENT_ITEM_COUNT = 9;
const NUM_COLUMNS = 3;
const TOTAL_ITEMS_LIMIT = 50;
const ITEM_MARGIN = 2;

type FakePost = { id: string; color: string };

const generateFakePosts = (count: number, startIndex = 0): FakePost[] =>
  Array.from({ length: count }, (_, i) => ({
    id: `post-${startIndex + i}`,
    color: `#${Math.floor(Math.random() * 0xffffff).toString(16).padStart(6, "0")}`,
  }));

const AnimatedFlashList = Animated.createAnimatedComponent(FlashList);

export default function FlashListDemo() {
  const [posts, setPosts] = useState<FakePost[]>([]);
  const [loadingMore, setLoadingMore] = useState(false);
  const [hasMore, setHasMore] = useState(true);

  const scrollY = useRef(new Animated.Value(0)).current;
  const { width } = useWindowDimensions();
  const cellWidth = (width - ITEM_MARGIN * (NUM_COLUMNS * 2)) / NUM_COLUMNS;
  const estimatedItemSize = cellWidth * 0.74 + ITEM_MARGIN * 2;

  useEffect(() => setPosts(generateFakePosts(INITIAL_ITEM_COUNT)), []);

  const loadMorePosts = useCallback(() => {
    if (loadingMore || !hasMore) return;
    setLoadingMore(true);
    setTimeout(() => {
      const newPosts = generateFakePosts(SUBSEQUENT_ITEM_COUNT, posts.length);
      setPosts(prev => [...prev, ...newPosts]);
      if (posts.length + newPosts.length >= TOTAL_ITEMS_LIMIT) setHasMore(false);
      setLoadingMore(false);
    }, 1500);
  }, [loadingMore, hasMore, posts.length]);

  const headerTranslateY = scrollY.interpolate({
    inputRange: [0, HEADER_HEIGHT],
    outputRange: [0, -HEADER_HEIGHT],
    extrapolate: "clamp",
  });

  const renderItem = ({ item }: { item: FakePost }) => (
    <View style={[styles.postItem, { backgroundColor: item.color }]} />
  );

  return (
    <View style={styles.container}>
      <Animated.View style={[styles.header, { transform: [{ translateY: headerTranslateY }] }]}>
        <Text style={styles.headerText}>Scrolling Header</Text>
        <Text style={styles.headerSubText}>{`(${HEADER_HEIGHT}px height)`}</Text>
      </Animated.View>

      <AnimatedFlashList
        data={posts}
        renderItem={renderItem}
        keyExtractor={item => item.id}
        numColumns={NUM_COLUMNS}
        estimatedItemSize={estimatedItemSize}
        onEndReached={loadMorePosts}
        onEndReachedThreshold={0.5}
        onScroll={Animated.event([{ nativeEvent: { contentOffset: { y: scrollY } } }], { useNativeDriver: true })}
        scrollEventThrottle={16}
        contentContainerStyle={{ paddingTop: HEADER_HEIGHT }}
        ListFooterComponent={
          loadingMore ? (
            <View style={styles.footer}>
              <ActivityIndicator size="large" color="#007AFF" />
            </View>
          ) : null
        }
      />

      <View style={styles.infoBox}>
        <Text style={styles.infoText}>
          Total Items: <Text style={{ fontWeight: "bold" }}>{posts.length}</Text>
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: "#f0f0f0" },
  header: {
    position: "absolute", top: 0, left: 0, right: 0, zIndex: 1,
    height: HEADER_HEIGHT, backgroundColor: "#4a148c", justifyContent: "center", alignItems: "center",
  },
  headerText: { fontSize: 32, fontWeight: "bold", color: "#fff" },
  headerSubText: { fontSize: 16, color: "#e0e0e0", marginTop: 8 },
  postItem: { flex: 1, aspectRatio: 0.74, margin: ITEM_MARGIN, borderRadius: 8 },
  footer: { paddingVertical: 20, justifyContent: "center", alignItems: "center" },
  infoBox: {
    position: "absolute", bottom: 20, left: 20, right: 20,
    backgroundColor: "rgba(0,0,0,0.7)", padding: 10, borderRadius: 10,
  },
  infoText: { textAlign: "center", color: "white", fontSize: 14 },
});
```

FlatList Code:
```
import React, { useState, useCallback, useEffect, useRef } from "react";
import { View, Text, StyleSheet, ActivityIndicator, Animated, FlatList } from "react-native";

const INITIAL_ITEM_COUNT = 6;
const HEADER_HEIGHT = 500;
const SUBSEQUENT_ITEM_COUNT = 9;
const NUM_COLUMNS = 3;
const TOTAL_ITEMS_LIMIT = 50;
const ITEM_MARGIN = 2;

type FakePost = { id: string; color: string };

const generateFakePosts = (count: number, startIndex = 0): FakePost[] =>
  Array.from({ length: count }, (_, i) => ({
    id: `post-${startIndex + i}`,
    color: `#${Math.floor(Math.random() * 16777215).toString(16).padStart(6, "0")}`,
  }));

export default function FlatListDemo() {
  const [posts, setPosts] = useState<FakePost[]>([]);
  const [loadingMore, setLoadingMore] = useState(false);
  const [hasMore, setHasMore] = useState(true);

  const scrollY = useRef(new Animated.Value(0)).current;

  useEffect(() => setPosts(generateFakePosts(INITIAL_ITEM_COUNT)), []);

  const loadMorePosts = useCallback(() => {
    if (loadingMore || !hasMore) return;
    setLoadingMore(true);
    setTimeout(() => {
      const newPosts = generateFakePosts(SUBSEQUENT_ITEM_COUNT, posts.length);
      setPosts(prev => [...prev, ...newPosts]);
      if (posts.length + newPosts.length >= TOTAL_ITEMS_LIMIT) setHasMore(false);
      setLoadingMore(false);
    }, 1500);
  }, [loadingMore, hasMore, posts.length]);

  const headerTranslateY = scrollY.interpolate({
    inputRange: [0, HEADER_HEIGHT],
    outputRange: [0, -HEADER_HEIGHT],
    extrapolate: "clamp",
  });

  const renderItem = ({ item }: { item: FakePost }) => (
    <View style={[styles.postItem, { backgroundColor: item.color }]} />
  );

  return (
    <View style={styles.container}>
      <Animated.View style={[styles.header, { transform: [{ translateY: headerTranslateY }] }]}>
        <Text style={styles.headerText}>Scrolling Header</Text>
        <Text style={styles.headerSubText}>{`(${HEADER_HEIGHT}px height)`}</Text>
      </Animated.View>

      <Animated.FlatList
        data={posts}
        renderItem={renderItem}
        keyExtractor={item => item.id}
        numColumns={NUM_COLUMNS}
        onEndReached={loadMorePosts}
        onEndReachedThreshold={0.5}
        onScroll={Animated.event([{ nativeEvent: { contentOffset: { y: scrollY } } }], { useNativeDriver: true })}
        scrollEventThrottle={16}
        contentContainerStyle={{ paddingTop: HEADER_HEIGHT }}
        ListFooterComponent={
          loadingMore ? (
            <View style={styles.footer}>
              <ActivityIndicator size="large" color="#007AFF" />
            </View>
          ) : null
        }
      />

      <View style={styles.infoBox}>
        <Text style={styles.infoText}>
          Total Items: <Text style={{ fontWeight: "bold" }}>{posts.length}</Text>
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: "#f0f0f0" },
  header: {
    position: "absolute", top: 0, left: 0, right: 0, zIndex: 1,
    height: HEADER_HEIGHT, backgroundColor: "#4a148c", justifyContent: "center", alignItems: "center",
  },
  headerText: { fontSize: 32, fontWeight: "bold", color: "#fff" },
  headerSubText: { fontSize: 16, color: "#e0e0e0", marginTop: 8 },
  postItem: { flex: 1, aspectRatio: 0.74, margin: ITEM_MARGIN, borderRadius: 8 },
  footer: { paddingVertical: 20, justifyContent: "center", alignItems: "center" },
  infoBox: {
    position: "absolute", bottom: 20, left: 20, right: 20,
    backgroundColor: "rgba(0,0,0,0.7)", padding: 10, borderRadius: 10,
  },
  infoText: { textAlign: "center", color: "white", fontSize: 14 },
});
```


===
