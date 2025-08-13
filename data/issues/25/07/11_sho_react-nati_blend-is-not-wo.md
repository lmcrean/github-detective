issue title: Blend is not working
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/react-native-skia/issues/3237
status: open
date opened: 2025-07-11
repo 30d_merge_rate: 22

====

description:
### Description

I am trying to blend two rects but nothing is happening.

<details>

<summary>Example App</summary>

```tsx
import { Blend, Canvas, Rect } from '@shopify/react-native-skia';
import { StyleSheet, View } from 'react-native';

function App() {
  return (
    <View style={styles.container}>
      <Canvas style={{ width: 250, height: 250 }}>
        <Blend mode="multiply">
          <Rect x={0} y={0} width={100} height={100} color="red" />
          <Rect x={50} y={50} width={100} height={100} color="blue" />
        </Blend>
      </Canvas>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

</details>

### React Native Skia Version

2.1.1

### React Native Version

0.80.1

### Using New Architecture

- [x] Enabled

### Steps to Reproduce

1. Initialize a new project and copy example provided or clone repo and run it
2. Notice that the are where the two rects overlap, it is not blending

### Snack, Code Example, Screenshot, or Link to Repository

https://github.com/itsramiel/RNSkia

===
