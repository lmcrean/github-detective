issue title: [Feature]: Add `SHOPIFY_CLI_WASM_OPT_PATH` environment variable
labels: Type: Enhancement
comment count: 0
hyperlink: https://github.com/shopify/cli/issues/6180
status: open
date opened: 2025-07-29
repo 30d_merge_rate: 77

====

description:
### What area(s) will this request affect?

Running your code locally

### What type of change do you want to see?

New feature

### Overview

Currently, when you run `shopify app build` with the `cli` provided by `nixpkgs`, you'll most likely encounter a "permission denied" error in the end, as shown below:

```
╭─ error ──────────────────────────────────────────────────────────────────────╮
│                                                                              │
│  Failed to build function.                                                   │
│                                                                              │
│  EACCES: permission denied, copyfile '/private/var/folders/n0/j42l73_53r72s  │
│  sbwznn235000000gn/T/96c557d287a0fc8e4164efe2462dd947/binary' ->             │
│  '/nix/store/n7hrqlf1a4h421rv76z37adq7g53g7mv-shopify-3.82.1/lib/node_modul  │
│  es/shopify/node_modules/@shopify/cli/bin/wasm-opt.cjs'                      │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
```

This is because it tries to download and copy `wasm-opt` binary to the `nix` store.

This can also happen with `shopify app dev`, but that "permission denied" error is caused by its attempt to copy `cloudflared` to the `nix` store. 

### Motivation

However, since an environment variable, `SHOPIFY_CLI_CLOUDFLARED_PATH`, exists to help you get around this issue, I think it would be great to also have an environment variable like `SHOPIFY_CLI_WASM_OPT_PATH` for `wasm-opt`, similar to how `SHOPIFY_CLI_CLOUDFLARED_PATH` works for `cloudflared`.

===
