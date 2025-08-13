issue title: [Bug]: Missing wasm-opt.cjs and shopify-function-trampoline files after upgrading CLI ≥ 3.73 causing build/deploy failures
labels: Type: Bug, Area: Functions
comment count: 1
hyperlink: https://github.com/shopify/cli/issues/6044
status: open
date opened: 2025-07-01
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Function

### Expected behavior

Both files `wasm‑opt.cjs` and `shopify‑function‑trampoline‑v1.0.0` should be packaged with the CLI, ensuring they are always present after installing.
Enhance install scripts to always download these binaries reliably, so build/deploy processes don’t fail due to intermittent missing files.

### Actual behavior

After upgrading Shopify CLI from v3.69.3 to v3.81.2, our GitHub Actions and server builds (and occasionally local builds after clearing node_modules) started failing with errors such as:
`Failed to build function.
Command failed with ENOENT: '*/node_modules/@shopify/cli/bin/shopify-function-trampoline-v1.0.0'`
`Failed to build function.
Error: ENOENT: no such file or directory, open '*/node_modules/@shopify/cli/bin/wasm-opt.cjs'`

We traced this back to the change introduced in CLI v3.73.0, where wasm-opt optimization was enabled by default:
> “All function builds are now optimized with wasm‑opt by default. This can be disabled with wasm_opt = false in [extensions.build].”

Adding `wasm_opt = false` in our shopify.app.toml resolves the missing `wasm-opt.cjs` issue.
However, unlike wasm-opt.cjs, there is no available opt-out or workaround for the missing shopify-function-trampoline binary.
Although it's required during build and deploy, it is not consistently downloaded — this leads to ~90% failure rate in CI, and occasional failures in local builds (after reinstalling packages).
- `wasm_opt = false` resolves the missing `wasm-opt.cjs` issue.
- However, there is no opt-out or workaround for the missing shopify-function-trampoline binary.

### Verbose output

In CI environment:

<img width="661" alt="Image" src="https://github.com/user-attachments/assets/d205c947-24bf-4816-9acf-ada4c8ab2686" />
<img width="656" alt="Image" src="https://github.com/user-attachments/assets/c17baabe-98c6-42b1-a6e4-79d776301aa6" />
<img width="679" alt="Image" src="https://github.com/user-attachments/assets/72988e1f-dcc5-4b75-99fa-a0100e768a37" />

### Reproduction steps

1. Upgrade Shopify CLI to v3.73+ (e.g. via npm install @shopify/cli@latest).
2. Clean install (rm -rf node_modules && npm ci) in a CI environment.
3. Run shopify app build, shopify app deploy
4. Observe errors for missing files under node_modules/@shopify/cli/bin/

### Operating System

Ubuntu 24.04, Mac OS Sequoia

### Shopify CLI version (`shopify --version`)

Shopify CLI v3.73.0 through v3.81.2

### Shell

Bash

### Node version (run `node -v` if you're not sure)

v22.3.0

### What language and version are you using in your application?

Node v22.3.0, TypeScript v5.7.3

===

comment #1 by sebastianpisula, 2025-08-03, 13:56:33
I have same issue:

```
  Failed to build function.                                                   │
│                                                                              │
│  Command failed with ENOENT:                                                 │
│  /builds/node_modules/@shopify/cli/bin/shopify-function-trampoline-v1.0.2 -i              │
│  /builds/extensions/payment-customization/dist/function.wasm -o                           │
│  /builds/extensions/payment-customization/dist/function.wasm                              │
│  spawn /builds/node_modules/@shopify/cli/bin/shopify-function-trampoline-v1.0.2 ENOENT 
```
