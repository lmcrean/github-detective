issue title: [Bug]: The script file generated for the `javascript` Liquid tags has a syntax error. It is missing a closing brace and parentheses
labels: Severity: 3, Type: Bug, Area: @shopify/theme
comment count: 0
hyperlink: https://github.com/shopify/cli/issues/5921
status: open
date opened: 2025-06-02
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Theme

### Expected behavior

My scripts file (`http://127.0.0.1:9292/cdn/shop/t/23/compiled_assets/scripts.js?<some number>`) not to have a syntax error.

### Actual behavior

My scripts file (`http://127.0.0.1:9292/cdn/shop/t/23/compiled_assets/scripts.js?<some number>`) has a syntax error. It is missing a trailing `})();`.

### Verbose output

The log output of `shopify theme dev` does not have any errors. The `Console` tab on the browser reveals the syntax error.

### Reproduction steps

I don't know under which conditions this occurs but it occurs with my theme. You can go to store ID `dbstdz-9k` and try to develop the master branch locally to reveal the issue. It works without any issues on live or when previewed using Shopify Admin. However, when developing locally using `shopify theme dev`, the issue occurs. More details are as follows:

Since Friday, I started getting weird behaviors when developing locally using Shopify CLI. Today I investigated the issue and discovered that there is an error log for the scripts file (`http://127.0.0.1:9292/cdn/shop/t/23/compiled_assets/scripts.js?<some number>`). Investigating it further revealed that the file has a syntax error: It is missing a final `})();`.

I monkey patched the issue by going to the `handleBlockScriptsJs` function at `/Users/username/.nvm/versions/node/v24.1.0/lib/node_modules/@shopify/cli/dist/index.js` and adding another `javascripts.push("})();");` line right after the already existing `javascripts.push("})();");` line. This fixed the issue for me locally.

### Operating System

macOS 14.7.4

### Shopify CLI version (`shopify --version`)

3.80.7

### Shell

Bash

### Node version (run `node -v` if you're not sure)

v24.1.0

### What language and version are you using in your application?

_No response_

===
