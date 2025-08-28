issue title: [Bug]: Codespaces `app dev` CSP error
labels: Type: Bug
comment count: 0
hyperlink: https://github.com/shopify/cli/issues/6235
status: open
date opened: 2025-08-09
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

App

### Expected behavior

`shopify app dev` should work correctly in a Codespaces environment.

### Actual behavior

The Shopify embedded app iframe shows "github.com refused to connect." The error message is:

```
Refused to frame 'https://github.com/' because an ancestor violates the following Content Security Policy directive: "frame-ancestors 'none'".
```

The root cause seems to be that GitHub auth cookies have `SameSite=Lax`, so the iframe will never see them.

I can work around it with `CODESPACE_NAME= pnpm exec shopify app dev` to force a Cloudflare tunnel (side note, I'd love a better way to configure the tunnel).

### Verbose output

N/A

### Reproduction steps

1. Start the embedded app template in Codespaces.
2. Run `shopify app dev` and open the preview URL.

### Operating System

Codespaces

### Shopify CLI version (`shopify --version`)

@shopify/cli/3.83.2

### Shell

_No response_

### Node version (run `node -v` if you're not sure)

_No response_

### What language and version are you using in your application?

_No response_

===
