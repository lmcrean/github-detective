issue title: [Bug]:  JavaScript Shopify Functions deployment fails with canonical_abi_realloc runtime version mismatch
labels: Type: Bug, Area: Functions
comment count: 2
hyperlink: https://github.com/shopify/cli/issues/6167
status: open
date opened: 2025-07-26
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Function

### Expected behavior

JavaScript Shopify Functions should deploy successfully to Shopify after building locally without errors. The deployment process should use compatible WASM runtime versions.

### Actual behavior

Deployment fails with different canonical_abi_realloc import errors depending on @shopify/shopify_function version:

- v2.0.0: "unknown import: `javy_quickjs_provider_v3::canonical_abi_realloc` has not been defined"
- v1.0.6: "unknown import: `shopify_functions_javy_v2::canonical_abi_realloc` has not been defined"  
- Same build: "unknown import: `shopify_functions_javy_v1::canonical_abi_realloc` has not been defined"

Functions build successfully locally but fail during `shopify app deploy`.

### Verbose output

<details>
  <summary>Deployment Error Output</summary>

╭─ error ───────────────────────────────────────────────────────────────────────────────────╮
│                                                                                           │
│  Version couldn't be created.                                                             │
│                                                                                           │
│  cart-checkout-validation                                                                 │
│                                                                                           │
│  Validation errors                                                                        │
│    • unknown import: `shopify_functions_javy_v1::canonical_abi_realloc` has not been      │
│      defined                                                                              │
│    • Try the following actions:                                                           │
│      - Upgrade your Shopify CLI (see https://shopify.dev/docs/api/shopify-cli#upgrade)    │
│      - Update your shopify_function dependency version                                    │
│        - Rust (see https://shopify.dev/docs/apps/build/functions/programming-languages/r  │
│      ust-for-functions)                                                                   │
│        - JavaScript (see https://shopify.dev/docs/apps/build/functions/programming-langu  │
│      ages/javascript-for-functions)                                                       │
│      - Look for help on the Shopify Functions community forum (see                        │
│      https://community.shopify.dev/c/shopify-functions)                                   │
│                                                                                           │
│                                                                                           │
╰───────────────────────────────────────────────────────────────────────────────────────────╯


### Reproduction steps

1. Create a JavaScript Shopify Function (purchase.validation.run or purchase.cart-transform.run)
2. Configure with @shopify/shopify_function version 1.0.6 or 2.0.0
3. Build function locally with `npm run build` (succeeds)
4. Deploy with `shopify app deploy`
5. Observe canonical_abi_realloc import error during deployment validation

### Operating System

macOS Sequoia (darwin 24.5.0)

### Shopify CLI version (`shopify --version`)

3.83.0

### Shell

zsh

### Node version (run `node -v` if you're not sure)

v24.0.0

### What language and version are you using in your application?

JavaScript/TypeScript with @shopify/shopify_function 1.0.6-2.0.0

===

comment #1 by AlexanderKharchenko, 2025-07-26, 01:04:27
Same 


Version couldn't be created.                                                │
│                                                                              │
│  ship-date-first-order                                                       │
│                                                                              │
│  Validation errors                                                           │
│    • unknown import: `shopify_functions_javy_v1::canonical_abi_realloc` has  │
│      not been defined                                                        │
│    • Try the following actions:                                              │
│      - Upgrade your Shopify CLI (see                                         │
│      https://shopify.dev/docs/api/shopify-cli#upgrade)                       │
│      - Update your shopify_function dependency version                       │
│        - Rust (see https://shopify.dev/docs/apps/build/functions/programmin  │
│      g-languages/rust-for-functions)                                         │
│        - JavaScript (see https://shopify.dev/docs/apps/build/functions/prog  │
│      ramming-languages/javascript-for-functions)                             │
│      - Look for help on the Shopify Functions community forum (see           │
│      https://community.shopify.dev/c/shopify-functions)        

comment #2 by AndrewKuktenko, 2025-07-26, 01:59:42
Confirm same issue.

`"@shopify/cli": "3.83.0"`

`"@shopify/shopify_function": "2.0.0"`

<img width="1034" height="368" alt="Image" src="https://github.com/user-attachments/assets/c80b2e5a-246c-456a-9146-ba7b09c7b84b" />
