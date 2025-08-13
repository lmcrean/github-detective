issue title: Bug: `@shopify/dev-mcp@latest` fails to run due to `import ... with { type: "json" }` — works with `1.0.2`
labels: Stale
comment count: 1
hyperlink: https://github.com/shopify/dev-mcp/issues/47
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 20

====

description:
## Description

I'm running Dev MCP using `npx` from a `cursor` configuration. When using `@shopify/dev-mcp@latest`, it fails with a `SyntaxError` related to `import ... with { type: "json" }`, even in Node.js versions that support import assertions. However, the command works fine when I explicitly pin it to version `1.0.2`.

## Cursor Configuration

```json
{
  "mcpServers": {
    "shopify-dev-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@shopify/dev-mcp@latest"
      ]
    }
  }
}
```

## Error Output
```shell
2025-06-11 16:49:56.178 [info] -mcp: Handling DeleteClient action
2025-06-11 16:49:57.009 [info] -mcp: Handling CreateClient action
2025-06-11 16:49:57.009 [info] -mcp: Starting new stdio process with command: npx -y @shopify/dev-mcp@latest
2025-06-11 16:49:57.585 [error] user-shopify-dev-mcp: file:///Users/lpaoloni/.npm/_npx/8f00c70bd5114901/node_modules/@shopify/dev-mcp/dist/instrumentation.js:1
import pkg from "../package.json" with { type: "json" };
                                  ^^^^

SyntaxError: Unexpected token 'with'
    at DefaultModuleLoader.moduleStrategy (node:internal/modules/esm/translators:116:18)
    at DefaultModuleLoader.moduleProvider (node:internal/modules/esm/loader:203:14)

Node.js v20.3.1

2025-06-11 16:49:57.590 [info] -mcp: Client closed for command
```

## Environment
- **OS**: macOS (Intel)
- **Node.js versions tried:**
  - v16.20.2 (expected to fail)
  - v20.3.1
  - v20.19.2
  - v24.2.0
- **Command:** `npx @shopify/dev-mcp@latest`
- ✅ `@shopify/dev-mcp@1.0.2` works correctly

## Request
Please confirm whether this is a packaging issue in the recent versions of `@shopify/dev-mcp`.

===

comment #1 by github-actions[bot], 2025-08-11, 02:13:30
We're labeling this issue as stale because there hasn't been any activity on it for 60 days. While the issue will stay open and we hope to resolve it, this helps us prioritize community requests.

You can add a comment to remove the label if it's still relevant, and we can re-evaluate it.
