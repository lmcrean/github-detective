issue title: [Bug]: app init is not usable in non-interactive environment
labels: Type: Enhancement
comment count: 1
hyperlink: https://github.com/shopify/cli/issues/6081
status: open
date opened: 2025-07-09
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

App

### Expected behavior

There should be a way to init a new app without user prompt. 

### Actual behavior

In non-interactive environment command `shopify app init` fails with `Failed to prompt: Create this project as a new app on Shopify?`.  There's no way to specify something like `--client-id=new`.

### Verbose output

<details>
  <summary>Verbose output</summary>

  ```
╭─ error ──────────────────────────────────────────────────────────────────────╮
│                                                                              │
│  Failed to prompt:                                                           │
│                                                                              │
│  Create this project as a new app on Shopify?                                │
│                                                                              │
│  This usually happens when running a command non-interactively, for example  │
│   in a CI environment, or when piping to or from another process.            │
│                                                                              │
│  To resolve this, specify the option in the command, or run the command in   │
│  an interactive environment such as your local terminal.                     │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

  ```

</details>

### Reproduction steps

1. `shopify app init` in non-interactive environment

### Operating System

Mac OS

### Shopify CLI version (`shopify --version`)

@shopify/cli/3.80.7 darwin-arm64 node-v24.1.0

### Shell

_No response_

### Node version (run `node -v` if you're not sure)

_No response_

### What language and version are you using in your application?

_No response_

===

comment #1 by isaacroldan, 2025-07-24, 09:33:13
Hi @aadamovskiy, this is great feedback, can't promise any dates but is in our list to fix.

Thank you!
