issue title: [Bug]: Logged in customer session issues while developing theme app blocks
labels: Type: Bug, Area: @shopify/theme
comment count: 0
hyperlink: https://github.com/shopify/cli/issues/6218
status: open
date opened: 2025-08-06
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

App

### Expected behavior

Should be able to log in (ideally with new customer accounts system) and retain the customer session while developing a theme app extension. This will allow developing extensions that depend on the customer being logged in.

### Actual behavior

New customer accounts does not appear to be supported - this doesn't seem to be documented.

After switching to legacy customer accounts, it is possible to visit http://127.0.0.1:9293/account/login and log in. The session is retained when navigating to other pages (ie. the page where the app extension is installed). However, this is temporary, and the user is logged out when the app encounters any errors or is idle for more than a few minutes. 

This leads to having to log in very frequently and is frustrating Dx.

### Verbose output

N/A

### Reproduction steps

1. Create theme app extension
2. Log in at http://127.0.0.1:9293/account/login
3. Add some conditional code that depends on the customer
4. See that the customer is frequently logged out during development
3.

### Operating System

Mac OS Ventura

### Shopify CLI version (`shopify --version`)

3.83.3

### Shell

zsh

### Node version (run `node -v` if you're not sure)

_No response_

### What language and version are you using in your application?

_No response_

===
