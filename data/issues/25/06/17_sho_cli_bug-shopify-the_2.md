issue title: [Bug]: Shopify Theme Console keeps logging me out
labels: Type: Bug, Area: @shopify/theme
comment count: 3
hyperlink: https://github.com/shopify/cli/issues/5995
status: open
date opened: 2025-06-17
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Theme

### Expected behavior

`shopify theme console` allows me to inspect liquid objects

### Actual behavior

`shopify theme dev`, or other commands like `shopify theme list` work like a charm.

With `shopify theme console` the console starts up without a problem but when inserting a liquid object like `shop` or `product` it breaks with the message "Session expired. Please initiate a new one."
I tried `shopify auth logout` and `shopify hydrogen login` but I can't figure out how to properly sign in?

(Context: I am a user in multiple partner organizations and I'm assigned to multiple shops where I switch between regularly)

![Image](https://github.com/user-attachments/assets/edcdcac1-df6c-4d93-a468-cce22eac30d3)
![Image](https://github.com/user-attachments/assets/c74b92a8-1ac6-4ec6-9746-b6cd92fb9bcd)

### Verbose output

<details>
  <summary>Verbose output</summary>

  ```
2025-06-17T13:37:47.141Z: Evaluating snippet - product
2025-06-17T13:37:47.143Z: → Rendering https://xxxxx.myshopify.com/?_fd=0&pb=0&section_id=announcement-bar (with sections/announcement-bar.liquid,snippets/eval.liquid)...
2025-06-17T13:37:47.426Z: ← 401 (request_id: dded2b88-15d6-45db-ab1a-60e970a50d12-1750167467)
2025-06-17T13:37:47.428Z: Error: Session expired. Please initiate a new one.
    at expiredSessionError (file:///Users/sipperts/.nvm/versions/node/v23.11.0/lib/node_modules/@shopify/cli/dist/index.js:197006:9)
    at makeRequest (file:///Users/sipperts/.nvm/versions/node/v23.11.0/lib/node_modules/@shopify/cli/dist/index.js:196974:40)
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async evalResult (file:///Users/sipperts/.nvm/versions/node/v23.11.0/lib/node_modules/@shopify/cli/dist/index.js:196929:92)
    at async evaluateSnippet (file:///Users/sipperts/.nvm/versions/node/v23.11.0/lib/node_modules/@shopify/cli/dist/index.js:196925:10)
    at async handleInput (file:///Users/sipperts/.nvm/versions/node/v23.11.0/lib/node_modules/@shopify/cli/dist/index.js:197066:26)
╭─ error ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                            │
│  Session expired. Please initiate a new one.                                                                               │
│                                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
  ```

</details>

### Reproduction steps

1. `shopify theme console`
2. Input a liquid object

### Operating System

macOS 15.5 (24F74)

### Shopify CLI version (`shopify --version`)

@shopify/cli/3.81.2 darwin-arm64 node-v23.11.0

### Shell

zsh

### Node version (run `node -v` if you're not sure)

v23.11.0

### What language and version are you using in your application?

_No response_

===

comment #1 by sippsolutions, 2025-06-17, 13:59:10
Addition:

my `shopify.theme.toml` looks like this:
```
[environments.default]
store = "0XXX"
store-password = "nXXX"
password = "shpat_XXXX"
ignore = []
open = true
auto-correct = true
```

When I remove the `password`, `shopify theme console` seems to work again.

comment #2 by EvilGenius13, 2025-06-17, 16:20:56
Hi @sippsolutions, if you could replicate this again using the `--verbose` flag, could you please provide us with the entire verbose log? 

comment #3 by sippsolutions, 2025-06-18, 08:31:38
@EvilGenius13 
```
2025-06-18T08:29:12.347Z: Running command theme console
2025-06-18T08:29:12.349Z: Running system process in background:
  · Command: /Users/myuser/.nvm/versions/node/v23.11.0/bin/node /Users/myuser/.nvm/versions/node/v23.11.0/bin/shopify notifications list --ignore-errors
  · Working directory: /Volumes/workspace/customerABC/shopify-customerABC-frontend

2025-06-18T08:29:12.353Z: Notifications to show: 0
2025-06-18T08:29:12.355Z: Reading the content of file at shopify.theme.toml...
╭─ info ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                            │
│  Using applicable flags from default environment:                                                                          │
│                                                                                                                            │
│    • store: XXXXXXX.myshopify.com                                                                                        │
│    • password: ********XXXX                                                                                                │
│    • store-password: XXXXX                                                                                                │
│                                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-06-18T08:29:12.379Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-06-18T08:29:12.379Z: Getting REPL theme...
2025-06-18T08:29:12.381Z: Sending "Admin" GraphQL request:
  query publicApiVersions {
  publicApiVersions {
    handle
    supported
    __typename
  }
}

With variables:
{}

With request headers:
 - User-Agent: Shopify CLI; v=3.81.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://XXXXXXX.myshopify.com/admin/api/unstable/graphql.json
2025-06-18T08:29:12.561Z: Request to https://XXXXXXX.myshopify.com/admin/api/unstable/graphql.json completed in 180 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=65, graphql;desc="admin/query/other", cfRequestDuration;dur=115.999937
 - x-request-id: 023877dc-1d58-426f-92a5-b89df3d97c95-1750235352
    
2025-06-18T08:29:12.561Z: Sending "Admin" GraphQL request:
  query getTheme($id: ID!) {
  theme(id: $id) {
    id
    name
    role
    processing
    __typename
  }
}

With variables:
{
  "id": "gid://shopify/OnlineStoreTheme/183949820168"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.81.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://XXXXXXX.myshopify.com/admin/api/2025-04/graphql.json
2025-06-18T08:29:12.675Z: Request to https://XXXXXXX.myshopify.com/admin/api/2025-04/graphql.json completed in 114 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=49, graphql;desc="admin/query/other", cfRequestDuration;dur=78.999996
 - x-request-id: 960030c2-db59-4875-9eb0-03546b6c39f8-1750235352
    
2025-06-18T08:29:12.676Z: Sending "Admin" GraphQL request:
  query OnlineStorePasswordProtection {
  onlineStore {
    passwordProtection {
      enabled
      __typename
    }
    __typename
  }
}

With request headers:
 - User-Agent: Shopify CLI; v=3.81.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://XXXXXXX.myshopify.com/admin/api/2025-04/graphql.json
2025-06-18T08:29:12.787Z: Request to https://XXXXXXX.myshopify.com/admin/api/2025-04/graphql.json completed in 112 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=43, graphql;desc="admin/query/other", cfRequestDuration;dur=72.999954
 - x-request-id: ba8c7e81-12ce-44b2-982c-9e7c3bb2fde7-1750235352
    
2025-06-18T08:29:12.788Z: Sending POST request to URL https://XXXXXXX.myshopify.com/password
With request headers:
 - cache-control: no-cache
 - content-type: application/x-www-form-urlencoded

2025-06-18T08:29:12.893Z: Request to https://XXXXXXX.myshopify.com/password completed in 105 ms
With response headers:
 - content-type: text/html; charset=utf-8
 - server-timing: processing;dur=14;desc="gc:1", db;dur=3, db_async;dur=1.675, asn;desc="3320", edge;desc="MUC", country;desc="DE", pageType;desc="password", servedBy;desc="5qj2", requestID;desc="74add6ab-0d58-4638-b82c-31db9d7ab39a-1750235352", cfRequestDuration;dur=52.000046
 - x-request-id: 74add6ab-0d58-4638-b82c-31db9d7ab39a-1750235352
    
2025-06-18T08:29:12.893Z: Setting storefront password for shop XXXXXXX.myshopify.com...
Welcome to Shopify Liquid console
(press Ctrl + C to exit)
2025-06-18T08:29:12.899Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-06-18T08:29:12.900Z: Sending HEAD request to URL https://XXXXXXX.myshopify.com/?preview_theme_id=183949820168&_fd=0&pb=0
With request headers:
 - X-Shopify-Shop: XXXXXXX.myshopify.com
 - User-Agent: Shopify CLI; v=3.81.2

2025-06-18T08:29:12.985Z: Request to https://XXXXXXX.myshopify.com/?preview_theme_id=183949820168&_fd=0&pb=0 completed in 86 ms
With response headers:
 - content-type: text/html; charset=utf-8
 - server-timing: processing;dur=12, db;dur=4, db_async;dur=1.802, asn;desc="3320", edge;desc="MUC", country;desc="DE", theme;desc="183949820168", pageType;desc="index", servedBy;desc="5btq", requestID;desc="853e23cb-8a5a-4f69-a593-10c37b170c35-1750235352", cfRequestDuration;dur=48.999786
 - x-request-id: 853e23cb-8a5a-4f69-a593-10c37b170c35-1750235352
    
2025-06-18T08:29:12.986Z: Sending POST request to URL https://XXXXXXX.myshopify.com/password
With request headers:
 - X-Shopify-Shop: XXXXXXX.myshopify.com
 - User-Agent: Shopify CLI; v=3.81.2
 - Cookie: _shopify_essential=:AZeCKA-ZAAH_6L7URsA2hLfrKP7oG433pc2LkbAYpPoHP3plWr61pcSMYVPc9FeIG8S32yU_QFks2MUozE9lsRCLD5OP1i2mUs3cSyA9hWl96aaVTjzgKw-l5fbrl_qbq6GFVyc:

2025-06-18T08:29:13.073Z: Request to https://XXXXXXX.myshopify.com/password completed in 88 ms
With response headers:
 - content-type: text/html; charset=utf-8
 - server-timing: processing;dur=13, db;dur=3, db_async;dur=1.531, asn;desc="3320", edge;desc="MUC", country;desc="DE", pageType;desc="password", servedBy;desc="9cbb", requestID;desc="935eea63-9d7e-41f1-b956-940ba7993252-1750235353", cfRequestDuration;dur=51.999807
 - x-request-id: 935eea63-9d7e-41f1-b956-940ba7993252-1750235353
    
> 2025-06-18T08:29:13.079Z: Running system process:
  · Command: npm prefix
  · Working directory: /Volumes/workspace/customerABC/shopify-customerABC-frontend

2025-06-18T08:29:13.175Z: Obtaining the dependency manager in directory /Volumes/workspace/customerABC/shopify-customerABC-frontend...
2025-06-18T08:29:13.419Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 144 ms
With response headers:
 - x-request-id: 06f9b38f-8d23-4770-b796-2aae1dab39b7
    
2025-06-18T08:29:13.419Z: Analytics event sent: {
  "command": "theme console",
  "time_start": 1750235352347,
  "time_end": 1750235353077,
  "total_time": 730,
  "success": true,
  "cli_version": "3.81.2",
  "ruby_version": "",
  "node_version": "23.11.0",
  "is_employee": false,
  "uname": "darwin arm64",
  "env_ci": false,
  "env_plugin_installed_any_custom": true,
  "env_plugin_installed_shopify": "[\"@shopify/cli\"]",
  "env_shell": "zsh",
  "env_device_id": "a2ae3353bd534facd4d9e4711b71e2d822e3ee45",
  "env_cloud": "localhost",
  "env_package_manager": "unknown",
  "env_is_global": true,
  "env_auth_method": "custom_app_token",
  "env_is_wsl": false,
  "cmd_app_warning_api_key_deprecation_displayed": false,
  "cmd_all_timing_network_ms": 683,
  "cmd_all_timing_prompts_ms": 0,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "theme",
  "cmd_all_plugin": "@shopify/theme",
  "cmd_all_verbose": true,
  "cmd_all_path_override": false,
  "cmd_all_last_graphql_request_id": "ba8c7e81-12ce-44b2-982c-9e7c3bb2fde7-1750235352",
  "cmd_all_timing_active_ms": 46,
  "cmd_all_exit": "ok",
  "user_id": "b7f0baf3-38fd-bdb4-fcf3-b0635fdc625ae19e330c",
  "request_ids": [
    "023877dc-1d58-426f-92a5-b89df3d97c95-1750235352",
    "960030c2-db59-4875-9eb0-03546b6c39f8-1750235352",
    "ba8c7e81-12ce-44b2-982c-9e7c3bb2fde7-1750235352"
  ],
  "args": "--url /products/michael-kors-gigi-handtasche-30s4g3gm5j-012 --verbose",
  "cmd_all_environment_flags": "{\"store\":\"XXXXXXX\",\"store-password\":\"XXXXX\",\"password\":\"shpat_XXXXXXXX\",\"ignore\":[],\"open\":true,\"auto-correct\":true}",
  "env_plugin_installed_all": "[\"@shopify/cli\",\"shopify-livereload\"]",
  "metadata": "{\"extraPublic\":{},\"extraSensitive\":{}}"
}
2025-06-18T08:29:13.419Z: Completed command theme console
product
2025-06-18T08:29:16.751Z: Evaluating snippet - product
2025-06-18T08:29:16.753Z: → Rendering https://XXXXXXX.myshopify.com/products/michael-kors-gigi-handtasche-30s4g3gm5j-012?_fd=0&pb=0&section_id=announcement-bar (with sections/announcement-bar.liquid,snippets/eval.liquid)...
2025-06-18T08:29:17.036Z: ← 401 (request_id: 200e7fc0-55f0-47f5-a76d-8128082c4dc9-1750235356)
2025-06-18T08:29:17.037Z: Error: Session expired. Please initiate a new one.
    at expiredSessionError (file:///Users/myuser/.nvm/versions/node/v23.11.0/lib/node_modules/@shopify/cli/dist/index.js:197006:9)
    at makeRequest (file:///Users/myuser/.nvm/versions/node/v23.11.0/lib/node_modules/@shopify/cli/dist/index.js:196974:40)
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async evalResult (file:///Users/myuser/.nvm/versions/node/v23.11.0/lib/node_modules/@shopify/cli/dist/index.js:196929:92)
    at async evaluateSnippet (file:///Users/myuser/.nvm/versions/node/v23.11.0/lib/node_modules/@shopify/cli/dist/index.js:196925:10)
    at async handleInput (file:///Users/myuser/.nvm/versions/node/v23.11.0/lib/node_modules/@shopify/cli/dist/index.js:197066:26)
╭─ error ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                            │
│  Session expired. Please initiate a new one.                                                                               │
│                                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
