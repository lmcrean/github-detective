issue title: [Bug]: POS UI Extension
labels: Type: Bug, State: Waiting for feedback
comment count: 1
hyperlink: https://github.com/shopify/cli/issues/6068
status: open
date opened: 2025-07-03
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Extension

### Expected behavior

I can't seem to get around this error:

[Error] Unhandled Promise Rejection: InsecureUrlError: URL must be secure (HTTPS)

(anonymous function) (data:text/javascript;charset=UTF-8,%22…%0A:1:15574)

While I'm trying to test my POS UI Extension on Dev

### Actual behavior

[Error] Unhandled Promise Rejection: InsecureUrlError: URL must be secure (HTTPS)

(anonymous function) (data:text/javascript;charset=UTF-8,%22…%0A:1:15574)

### Verbose output

<details>
  <summary>Verbose output</summary>

  ```
  Paste the output here!
  ```

</details>

### Reproduction steps

1.
2.
3.

### Operating System

Mac OS 15.5 - testing on iPhone IOS 18.6

### Shopify CLI version (`shopify --version`)

3.82.0.

### Shell

_No response_

### Node version (run `node -v` if you're not sure)

_No response_

### What language and version are you using in your application?

_No response_

===

comment #1 by alexanderMontague, 2025-07-03, 21:26:54
Hi @troydmorgan73, I can't seem to reproduce the error on version `3.82.0`. If the problem is still persisting, would you mind specifying what "flavour" of POS UI Extension you chose to develop with, as well as the output of `shopify app dev --verbose`? Thanks!
