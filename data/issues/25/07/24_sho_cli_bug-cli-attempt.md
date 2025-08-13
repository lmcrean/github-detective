issue title: [Bug]: CLI attempts to match with removed extension
labels: Type: Bug
comment count: 1
hyperlink: https://github.com/shopify/cli/issues/6155
status: open
date opened: 2025-07-24
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Extension

### Expected behavior

We had an extension named `checkout-ui`. We deleted it and split it into multiple individual extensions. However, every time we add a new extension, the CLI attempts to match the new extension to this no-longer-existing extension. While we can manually match this when deploying locally, this breaks our CI pipeline every time we add a new extension.

<img width="604" height="299" alt="Image" src="https://github.com/user-attachments/assets/51544060-8344-4438-ac2a-c5c8cebb48a3" />

### Actual behavior

Old extension should be deleted or new extensions should not attempt to match against them.

### Verbose output

I resolved this manually for now because we needed to deploy the new extension so I don't have verbose output. I can capture this next time this issue pops up.

### Reproduction steps

1. Create an extension
2. Remove that extension
3. Create a new extension with a different name

### Operating System

MacOS Sequoia 15.5

### Shopify CLI version (`shopify --version`)

@shopify/cli/3.76.2 darwin-arm64 node-v23.7.0

### Shell

bash

### Node version (run `node -v` if you're not sure)

23.7.0

### What language and version are you using in your application?

Node 20

===

comment #1 by isaacroldan, 2025-07-25, 08:14:13
Hi @mAAdhaTTah, sorry you are facing this problem, this is a known issue, fortunately it will go away with the migration to the new dev platform :) 

In the meantime, you can fix it by either:
- Commiting your `.env` file after a local deploy: this file contains the necessary identifiers for the CLI to not need to ask on every deploy.
- Instead of committing your `.env` file, you can also add the contents of it as secrets in Github actions and passing them as environment variables when calling the CLI


