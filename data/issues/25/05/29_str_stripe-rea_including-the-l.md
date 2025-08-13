issue title: Including the library without using it breaks expo web
labels: none
comment count: 7
hyperlink: https://github.com/stripe/stripe-react-native/issues/1954
status: open
date opened: 2025-05-29
repo 30d_merge_rate: 34

====

description:
As title

We use Expo for web as well as iOS and Android.

When I include this library, nothing else, without even using it, it completely breaks web.

```
Web Bundling failed 893ms node_modules/expo-router/entry.js (2742 modules)
Unable to resolve "../../Utilities/Platform" from "node_modules/react-native/Libraries/Components/TextInput/TextInputState.js"
```

Would be great if we could use this library with iOS/Android, we will use another with Web, so no need to support it.

===

comment #1 by porter-stripe, 2025-05-29, 16:18:12
Hi @ollyde I tried to repro your issue but I am unable to. Can you please share steps on how to repro or share an example repo with the issue?

Thanks!

comment #2 by ollyde, 2025-05-30, 10:43:00
@porter-stripe  thnaks; Just include this dependency in a default project, and then launch web and you'll see it errors.

comment #3 by Felipe-OT, 2025-06-22, 14:35:27
Did you find a solution? I have a _layout.tsx and _layout.web.tsx. Importing @stripe/stripe-react-native into _layout.tsx causes this error on web.


comment #4 by ollyde, 2025-06-22, 14:38:23
@Felipe-OT no solution yet, makes Stripe library fairly useless for Expo.

comment #5 by Felipe-OT, 2025-06-22, 15:06:16
I partialy resolved the issue creating a wrapper:

```// src/components/screens/dashboard/subscription/StripeWrapper.tsx
import { Platform } from 'react-native';

const StripeWrapper = Platform.select({
  web: require('./StripeWrapper.web').default,
  default: require('./StripeWrapper.native').default,
});

export default StripeWrapper;
```

But i have to do this every time i have to import @stripe/stripe-react-native

comment #6 by horyd, 2025-08-04, 20:57:16
I have limited use of the Stripe package itself, isolated to a shop page, so I implemented a metro custom resolver to ensure the native file (shop.tsx) did not get bundled

```js
const { getDefaultConfig } = require('expo/metro-config');

/** @type {import('expo/metro-config').MetroConfig} */
const config = getDefaultConfig(__dirname);

config.resolver.resolveRequest = (context, moduleName, platform) => {
    if (platform === 'web') {
        // Ensure that we do not load the native shop module on web, as it includes native stripe packages
        // that are incompatible with web.
        if (moduleName.includes('shop') && !moduleName.includes('shop.web')) {
            return context.resolveRequest(context, moduleName.replace('shop', 'shop.web'), platform);
        }
    }
    // Ensure you call the default resolver.
    return context.resolveRequest(context, moduleName, platform);
  };

module.exports = config;
```

comment #7 by ollyde, 2025-08-05, 08:43:11
Thanks for the solutions but neither of them worked.
