issue title: Crash on web with Next.js
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1783
status: open
date opened: 2025-07-16
repo 30d_merge_rate: 7

====

description:
## Current behavior

Our web app is crashing in the Next.js dev server when using a basic FlashList. The following is logged to the console:

```
index.js:644 Uncaught SyntaxError: Unexpected token 'typeof'
    at compileSourceTextModule (node:internal/modules/esm/utils:344:16)
    at ModuleLoader.importSyncForRequire (node:internal/modules/esm/loader:420:18)
    at loadESMFromCJS (node:internal/modules/cjs/loader:1565:24)
    at Module._compile (node:internal/modules/cjs/loader:1716:5)
    at <unknown> (node:internal/modules/cjs/loader:1899:10)
    at newLoader (file:///Users/kris.wong/Dev/astoria-frontend/node_modules/esbuild-register/dist/node.js:2262:9)
    at newLoader (file:///Users/kris.wong/Dev/astoria-frontend/node_modules/esbuild-register/dist/node.js:2262:9)
    at newLoader (file:///Users/kris.wong/Dev/astoria-frontend/node_modules/esbuild-register/dist/node.js:2262:9)
    at Object.newLoader [as .js] (file:///Users/kris.wong/Dev/astoria-frontend/node_modules/esbuild-register/dist/node.js:2262:9)
    at Module.load (node:internal/modules/cjs/loader:1469:32)
    at Function._load (node:internal/modules/cjs/loader:1286:12)
    at TracingChannel.traceSync (node:diagnostics_channel:322:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:235:24)
    at Module.<anonymous> (node:internal/modules/cjs/loader:1491:12)
    at mod.require (file:///Users/kris.wong/Dev/astoria-frontend/node_modules/next/dist/server/require-hook.js:65:28)
```

## Expected behavior

No crash.

## To Reproduce

I am rendering quite a simple flash list with only a few items in it. The items are also quite simple (icon & text).

## Platform:

- [ ] iOS
- [ ] Android
- [x] Web

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

2.0.0-rc.11 via the RC channel


===
