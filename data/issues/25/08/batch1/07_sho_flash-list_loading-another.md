issue title: Loading another Flashlist causes a horizontal scroll bar to appear - IOS
labels: bug, v2.0
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1828
status: open
date opened: 2025-08-07
repo 30d_merge_rate: 7

====

description:

## Expected behavior
Hey,

On iPhone 16 Pro (iOS 18.6), for unknown reasons, horizontal scrolling appears, even though all elements fit within the view.
For example:
1. I load data from the API into FlashList associated with `view` = `devices` - no horizontal scrolling, everything fits**(!)**.
2. I change `view` to `notifications` - a horizontal scroll bar appears (even when `renderItem={() => {return <></>}`)
3. I go back to `view` = `devices` and suddenly there is horizontal scrolling there too.

I tested this issue on Android and it does not occur. I also used an iPhone 8 with iOS 15 and the issue does not occur there either.
<!-- What do you expect to happen instead? -->


## To Reproduce
```typescript 
  const [view, setView] = useState<'devices' | 'notifications'>('devices');
  return(
      <View style={{ flex: 1 }}>
        {/* Content */}
        {view === 'devices' ? (
          <FlashList
            ListEmptyComponent={loadingOrEmptyFlatListComponent({ isLoading: loading })}
            key={view}
            data={filteredDevices}
            renderItem={renderDeviceItem}
            keyExtractor={(item) => item.id.toString()}
            numColumns={2}
            onLayout={(event) => {
              const { width } = event.nativeEvent.layout;
              console.log('towers-list FlashList width:', width);
            }}
            contentContainerStyle={{
              paddingBottom: insets.bottom,
              paddingHorizontal: 20,
              paddingTop: headerHeight + insets.top,
            }}
            showsVerticalScrollIndicator={false}
          />
        ) : (
          <FlashList
            key={view}
            data={groupedPreferences}
            renderItem={renderItem}
            getItemType={(item) => (typeof item === 'string' ? `sectionHeader` : `item`)}
            keyExtractor={(item) =>
              typeof item === 'string' ? `sectionHeader-${item}` : `item-${item.notificationType}`
            }
            contentContainerStyle={{
              paddingBottom: insets.bottom,
              paddingHorizontal: 20,
              paddingTop: headerHeight + insets.top,
            }}
            showsVerticalScrollIndicator={false}
            }
          />
        )}
      </View>)
```

<!-- Please provide a way to reproduce the problem if it's possible. Use the fixture app to create an example that reproduces the bug and provide a link to a GitHub repository under your username. -->

## Platform:

- [X] iOS
- [ ] Android

## Environment
Flashlist Version: 2.0.1
Expo Go client version: 1017702
<!-- What is the exact version of @shopify/flash-list that you are using? -->

===
