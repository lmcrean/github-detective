issue title: [iOS] Canvas is cut off from the bottom
labels: bug
comment count: 1
hyperlink: https://github.com/shopify/react-native-skia/issues/3220
status: open
date opened: 2025-07-01
repo 30d_merge_rate: 22

====

description:
### Description

Hi,

I am having a weird issue where the canvas does not render the last ~ 1 point if  I render a button above the canvas. I know the issue sounds weird but it happens. I tried to replace the button with a Text or a View but it does not occur. Only with a button and only on iOS.

## Screenshots

| **iOS** | **Android** |
| ---------- | --------- |
| ![Image](https://github.com/user-attachments/assets/0c11b66f-31b4-42bb-9a73-b80eb5ea2905) | ![Image](https://github.com/user-attachments/assets/01bed0d1-a83d-4abb-8022-7a01e31890fb) |

If I remove the button it works fine:

| **iOS** | **Android** |
| ---------- | --------- |
| ![Image](https://github.com/user-attachments/assets/26fee845-d49c-456b-b92f-99aace4fd113) | ![Image](https://github.com/user-attachments/assets/1dc7e9fd-eb10-4fd1-bdb7-5031d377a72d) |


### React Native Skia Version

2.1.0

### React Native Version

0.80.1

### Using New Architecture

- [x] Enabled

### Steps to Reproduce

Use the repo or render the following app:

<details>
<summary>Example Code</summary

```tsx
import { Button, StyleSheet, View } from 'react-native';

import { Canvas, Rect, SkSize } from '@shopify/react-native-skia';
import { useDerivedValue, useSharedValue } from 'react-native-reanimated';

const STROKE_WIDTH = 1;

function App() {
  const size = useSharedValue<SkSize>({ width: 0, height: 0 });

  const rect = useDerivedValue(() => {
    const { width: canvasWidth, height: canvasHeight } = size.get();

    return {
      x: STROKE_WIDTH / 2,
      y: STROKE_WIDTH / 2,
      width: canvasWidth - STROKE_WIDTH,
      height: canvasHeight - STROKE_WIDTH,
    };
  }, []);

  return (
    <View style={styles.screen}>
      <Button title="Play" />
      <Canvas onSize={size} style={styles.canvas}>
        <Rect
          style={'stroke'}
          strokeWidth={STROKE_WIDTH}
          color={'rgba(0, 0, 0, 0.5)'}
          rect={rect}
        />
      </Canvas>
    </View>
  );
}

const styles = StyleSheet.create({
  screen: {
    flex: 1,
    justifyContent: 'center',
    padding: 16,
  },
  canvas: {
    width: '100%',
    aspectRatio: 2,
  },
});

export default App;
```

</details>


### Snack, Code Example, Screenshot, or Link to Repository

[Repo Link](https://github.com/itsramiel/SkiaCutOff)

===

comment #1 by itsramiel, 2025-07-02, 14:46:48
@wcandillon Please let me know if you need any more info or if you can't reproduce
