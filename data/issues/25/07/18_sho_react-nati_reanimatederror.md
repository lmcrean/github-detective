issue title: ReanimatedError: Exception in HostFunction: bad_optional_access, js engine: reanimated
labels: bug
comment count: 1
hyperlink: https://github.com/shopify/react-native-skia/issues/3242
status: open
date opened: 2025-07-18
repo 30d_merge_rate: 22

====

description:
### Description

On iOS if I click outside the app and open it again, I'm getting the following error. This was not happening before. I'm not sure when the error was produced

https://github.com/user-attachments/assets/1ebfa2aa-761d-43dc-926f-d51a39fb5331

### React Native Skia Version

^2.1.1

### React Native Version

0.79.5

### Using New Architecture

- [x] Enabled

### Steps to Reproduce

Using expo click outside the builded app and open it again.

### Snack, Code Example, Screenshot, or Link to Repository

The only thing i can give its I'm using the above imports for my circular progress bar.
```
import {
  Canvas,
  Image,
  Path,
  Skia,
  Text,
  interpolateColors,
  useFont,
  useImage,
} from "@shopify/react-native-skia"
import { useEffect } from "react"
import {
  useDerivedValue,
  useSharedValue,
  withTiming,
} from "react-native-reanimated"
```

===

comment #1 by RafaelCENG, 2025-07-18, 09:08:35
Here is a more clear screenshot:
Also the path : node_modules -> shopify -> react-native-skia -> src -> sksg -> Container.ts -> function nativeDrawOnscreen
<img width="343" height="747" alt="Image" src="https://github.com/user-attachments/assets/3d43e9d7-a3ee-4c96-8f1c-86f7f7f8a707" />
