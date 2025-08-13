issue title: [Expo 53] "useColorBuffer" throwing " Value is undefined, expected an Object, js engine: hermes"
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/react-native-skia/issues/3275
status: open
date opened: 2025-08-08
repo 30d_merge_rate: 22

====

description:
### Description

After bumping expo to SDK 53 `useColorBuffer` is throwing `Value is undefined, expected an Object` error;
And on hot reload will throw `Should not already be working`:

Reproduced using recommended by Expo SDK 53 `v2.0.0-next.4` version and latest `2.2.2` version.

### React Native Skia Version

v2.0.0-next.4

### React Native Version

0.79.5

### Using New Architecture

- [ ] Enabled

### Steps to Reproduce

1. Use `Hello World` example from the Skia examples: https://shopify.github.io/react-native-skia/docs/shapes/atlas/#hello-world
2. Declare colors using `useColorBuffer`:
```
    import { useColorBuffer } from '@shopify/react-native-skia';

    const colors = useColorBuffer(numberOfBoxes, (color: SkColor, i: number) => {
        'worklet';
        color.set(Skia.Color('red'));
    });
```
3. See thrown error: `Value is undefined, expected an Object`

### Snack, Code Example, Screenshot, or Link to Repository

**NOTE**: Can't create a Snack with the Expo SDK 53 recommended Skia package version `v2.0.0-next.4` because of the error:
```
Failed to resolve dependency '@shopify/react-native-skia@v2.0.0-next.4' (Version 'v2.0.0-next.4' for package '@shopify/react-native-skia' not found)
```

`Hello World` example from Skia docs: https://shopify.github.io/react-native-skia/docs/shapes/atlas/#hello-world with few changes, because in expo `await drawAsImage` outside of the component will throw an error `ReferenceError: Property 'await' doesn't exist, js engine: hermes`;

```tsx
import React, { useEffect, useState } from 'react';
import {
    Atlas,
    Canvas,
    drawAsImage,
    Group,
    rect,
    Rect,
    SkColor,
    Skia,
    useColorBuffer,
} from '@shopify/react-native-skia';

const size = { width: 25, height: 11.25 };
const strokeWidth = 2;
const imageSize = {
    width: size.width + strokeWidth,
    height: size.height + strokeWidth,
};

export const Demo = () => {
    const [image, setImage] = useState();

    useEffect(() => {
        const init = async () => {
            const res = await drawAsImage(
                <Group>
                    <Rect rect={rect(strokeWidth / 2, strokeWidth / 2, size.width, size.height)} color="cyan" />
                    <Rect
                        rect={rect(strokeWidth / 2, strokeWidth / 2, size.width, size.height)}
                        color="blue"
                        style="stroke"
                        strokeWidth={strokeWidth}
                    />
                </Group>,
                imageSize,
            );

            setImage(res);
        };

        init();
    }, []);

    const numberOfBoxes = 150;

    // Will work fine
    const colors_v1 = new Array(numberOfBoxes).fill(0).map(() => Skia.Color('red'));
    
    // Will throw an error: "Value is undefined, expected an Object"
    const colors_v2 = useColorBuffer(numberOfBoxes, (color: SkColor, i: number) => {
        'worklet';
        color.set(Skia.Color('red'));
    });

    if (!image) {
        return null;
    }

    const pos = { x: 128, y: 128 };
    const width = 256;
    const sprites = new Array(numberOfBoxes).fill(0).map(() => rect(0, 0, imageSize.width, imageSize.height));
    const transforms = new Array(numberOfBoxes).fill(0).map((_, i) => {
        const tx = 5 + ((i * size.width) % width);
        const ty = 25 + Math.floor(i / (width / size.width)) * size.width;
        const r = Math.atan2(pos.y - ty, pos.x - tx);
        return Skia.RSXform(Math.cos(r), Math.sin(r), tx, ty);
    });

    return (
        <Canvas style={{ flex: 1 }}>
            <Atlas image={image} sprites={sprites} transforms={transforms} colors={colors_v1} />
        </Canvas>
    );
};
```

===
