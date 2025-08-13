issue title: [Bug]: Theme check in CLI does not report cross-file LiquidDoc errors
labels: Severity: 3, Windows
comment count: 0
hyperlink: https://github.com/shopify/theme-tools/issues/1022
status: open
date opened: 2025-07-30
repo 30d_merge_rate: 11

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Theme

### Expected behavior

- When you run `shopify theme check` I want to see all the theme-checks that show up in VSCode


### Actual behavior

- LiquidDoc error **does** show up when its within the same file
- Cross-file LiquidDoc errors (like when one is referenced via `render` or `content_for` tag do not show up)

NOTE: This only happened on my Windows, but it works on my Mac

<img width="1102" height="1140" alt="Image" src="https://github.com/user-attachments/assets/6ddc8a7a-945e-4186-ba29-91d6ae7ed0ca" />

### Verbose output

- not needed

### Reproduction steps

1. Create a snippet with LiquidDoc with at least 1 required param
2. Render that snippet, without passing in the required args
3. See the error in VSCode
4. Run `shopify theme check` and notice it does not appear in the logs

### Operating System

Windows 11

### Shopify CLI version (`shopify --version`)

3.83.1

### Shell

_No response_

### Node version (run `node -v` if you're not sure)

_No response_

### What language and version are you using in your application?

_No response_

===
