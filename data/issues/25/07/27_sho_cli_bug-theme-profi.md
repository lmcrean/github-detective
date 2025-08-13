issue title: [Bug]: `theme profile` returns error when authenticating with Theme Access Token
labels: Type: Bug, Area: @shopify/theme
comment count: 0
hyperlink: https://github.com/shopify/cli/issues/6168
status: open
date opened: 2025-07-27
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Theme

### Expected behavior

When running `shopify theme profile` with the [documented](https://shopify.dev/docs/api/shopify-cli/theme/theme-profile#flags-propertydetail-passwordvalue) `--password` flag, or the equivalent `SHOPIFY_CLI_THEME_TOKEN` environment variable, and a confirmed valid Theme Access token value, the command should successfully return Liquid profiler results.

### Actual behavior

When running `shopify theme profile` with the [documented](https://shopify.dev/docs/api/shopify-cli/theme/theme-profile#flags-propertydetail-passwordvalue) `--password` flag, or the equivalent `SHOPIFY_CLI_THEME_TOKEN` environment variable, and a confirmed valid Theme Access token value, the command returns `Bad response: 500` as a response (see Verbose output below).

I have tested the following, to rule out the simplest causes:
- Utilizing the default local authentication method (i.e.: logging in to Shopify CLI with browser-based authentication) for the exact same store, theme, and url returns the expected results.
- Confirming that the Theme Access token is valid, utilizing other commands (i.e.: `theme list`)
- Utilizing the `--store-password` flag in conjunction with the `--password` flag, in case that was a required input

I am seeking to leverage this command in CI/CD in order to report on Liquid rendering time, hence the need to use the Theme Access token.

### Verbose output

<details>
  <summary>Verbose output</summary>

  ```bash
$ shopify theme profile -s ******************.myshopify.com --url / --theme ************ --password=*************************************** --store-password=****** --verbose --json
2025-07-27T21:18:41.739Z: Checking if there's a version of @shopify/cli newer than 3.83.0
2025-07-27T21:18:41.740Z: Getting the latest version of NPM package: @shopify/cli
2025-07-27T21:18:41.754Z: Running command theme profile
2025-07-27T21:18:41.757Z: Running system process in background:
  · Command: /usr/local/share/nvm/versions/node/v22.16.0/bin/node /usr/local/share/nvm/versions/node/v22.16.0/bin/shopify notifications list --ignore-errors
  · Working directory: /workspaces/shopify-theme

2025-07-27T21:18:41.765Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-27T21:18:41.767Z: Sending "Admin" GraphQL request:
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
 - X-Shopify-Shop: ******************.myshopify.com
 - User-Agent: Shopify CLI; v=3.83.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://theme-kit-access.shopifyapps.com/cli/admin/api/unstable/graphql.json
2025-07-27T21:18:42.148Z: Request to https://theme-kit-access.shopifyapps.com/cli/admin/api/unstable/graphql.json completed in 381 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"51a35fddd6cc9b76595d10ba952be668"
 - server-timing: processing;dur=87, socket_queue;dur=1.774, cfRequestDuration;dur=161.999941
 - x-request-id: 0f1c392a-6688-469b-95aa-1d4923edb6a3-1753651122

2025-07-27T21:18:42.149Z: Sending "Admin" GraphQL request:
  query getThemes($after: String) {
  themes(first: 50, after: $after) {
    nodes {
      id
      name
      role
      processing
      __typename
    }
    pageInfo {
      hasNextPage
      endCursor
      __typename
    }
    __typename
  }
}

With variables:
{
  "after": null
}

With request headers:
 - X-Shopify-Shop: ******************.myshopify.com
 - User-Agent: Shopify CLI; v=3.83.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://theme-kit-access.shopifyapps.com/cli/admin/api/2025-07/graphql.json
2025-07-27T21:18:42.525Z: Request to https://theme-kit-access.shopifyapps.com/cli/admin/api/2025-07/graphql.json completed in 376 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"b79a80062cc20953fc83e958128914c3"
 - server-timing: processing;dur=85, socket_queue;dur=2.513, cfRequestDuration;dur=272.000313
 - x-request-id: 5e85061a-ef5b-40ab-9af5-84aa494d4d9e-1753651122

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Generating Liquid profile for ******************.myshopify.com/ ...
2025-07-27T21:18:42.547Z: Sending "Admin" GraphQL request:
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
 - X-Shopify-Shop: ******************.myshopify.com
 - User-Agent: Shopify CLI; v=3.83.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Generating Liquid profile for ******************.myshopify.com/ ...
2025-07-27T21:18:42.851Z: Request to https://theme-kit-access.shopifyapps.com/cli/admin/api/2025-07/graphql.json completed in 304 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"b59fd44f355bc2db926b5a373dae4ffa"
 - server-timing: processing;dur=77, socket_queue;dur=2.505, cfRequestDuration;dur=161.000013
 - x-request-id: 04009162-67e8-4c03-b7ff-ffa9dc9dcfc6-1753651122

2025-07-27T21:18:42.857Z: Sending POST request to URL https://******************.myshopify.com/password
With request headers:
 - cache-control: no-cache
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Generating Liquid profile for ******************.myshopify.com/ ...
2025-07-27T21:18:43.205Z: Request to https://******************.myshopify.com/password completed in 347 ms
With response headers:
 - content-type: text/html; charset=utf-8
 - server-timing: processing;dur=54;desc="gc:1", db;dur=10, db_async;dur=3.285, asn;desc="5645", edge;desc="ORD", country;desc="CA", pageType;desc="password", servedBy;desc="fwsl", requestID;desc="8de3a1df-a086-4aa0-a7c4-aa89a067b708-1753651123", _y;desc="ddd2a284-3784-47d3-9d98-268dbca0b9ab", _s;desc="1c30150a-a9ba-4223-8c7d-8db06fbb994d", cfRequestDuration;dur=129.999876
 - x-request-id: 8de3a1df-a086-4aa0-a7c4-aa89a067b708-1753651123

2025-07-27T21:18:43.205Z: Setting storefront password for shop ******************.myshopify.com...
2025-07-27T21:18:43.207Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-27T21:18:43.208Z: Sending HEAD request to URL https://theme-kit-access.shopifyapps.com/cli/sfr?preview_theme_id=************&_fd=0&pb=0
With request headers:
 - X-Shopify-Shop: ******************.myshopify.com
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Generating Liquid profile for ******************.myshopify.com/ ...
2025-07-27T21:18:43.476Z: Request to https://theme-kit-access.shopifyapps.com/cli/sfr?preview_theme_id=************&_fd=0&pb=0 completed in 269 ms
With response headers:
 - cache-control: no-cache
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=88, socket_queue;dur=1.988, cfRequestDuration;dur=175.000191
 - x-request-id: f632f0b5-761f-433d-a0e7-db342b744707-1753651123

2025-07-27T21:18:43.477Z: Sending POST request to URL https://theme-kit-access.shopifyapps.com/cli/sfr/password
With request headers:
 - X-Shopify-Shop: ******************.myshopify.com
 - User-Agent: Shopify CLI; v=3.83.0
 - Cookie: _shopify_essential=:AZhNwJVOAAH_uhKXNykB8pun9LsW2QfWJcBrxgVc_RxQgdwXMoTXPnmXr0UOfNnZ39BCy0314CBi3JhvnNVS5fuUTvNoOUlh1jgyngVfY5cg0IwLMb-p20r5Do_Ew2jSikYlGejdfZZANCb5cgkQ
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Generating Liquid profile for ******************.myshopify.com/ ...
2025-07-27T21:18:43.709Z: Request to https://theme-kit-access.shopifyapps.com/cli/sfr/password completed in 232 ms
With response headers:
 - cache-control: no-cache
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=54, socket_queue;dur=1.956, cfRequestDuration;dur=128.000021
 - x-request-id: 120352fd-2088-46c7-8789-fda0a4375d1c-1753651123
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

╭─ error ─────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                     │
│  Bad response: 500:                                                                                                 │
│                                                                                                                     │
│  To investigate the issue, examine this stack trace:                                                                │
│    at profile (usr/local/share/nvm/versions/node/v22.16.0/lib/node_modules/@shopify/cli/dist/index.js:199938)       │
│    at processTicksAndRejections (node:internal/process/task_queues:105)                                             │
│    at task (usr/local/share/nvm/versions/node/v22.16.0/lib/node_modules/@shopify/cli/dist/index.js:199964)          │
│    at async runTask2                                                                                                │
│    (usr/local/share/nvm/versions/node/v22.16.0/lib/node_modules/@shopify/cli/dist/chunk-D5BJW27F.js:31654)          │
│    at (usr/local/share/nvm/versions/node/v22.16.0/lib/node_modules/@shopify/cli/dist/chunk-D5BJW27F.js:31670)       │
│                                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-07-27T21:18:43.961Z: Running system process:
  · Command: npm prefix
  · Working directory: /workspaces/shopify-theme

2025-07-27T21:18:44.019Z: Obtaining the dependency manager in directory /workspaces/shopify-theme...
2025-07-27T21:18:44.273Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 198 ms
With response headers:
 - x-request-id: df684242-7346-4ce9-9b46-5654c5c111d2

2025-07-27T21:18:44.274Z: Analytics event sent: {
  "command": "theme profile",
  "time_start": 1753651121754,
  "time_end": 1753651123955,
  "total_time": 2201,
  "success": false,
  "cli_version": "3.83.0",
  "ruby_version": "",
  "node_version": "22.16.0",
  "is_employee": false,
  "uname": "linux arm64",
  "env_ci": false,
  "env_plugin_installed_any_custom": false,
  "env_plugin_installed_shopify": "[\"@shopify/cli\"]",
  "env_shell": "bash",
  "env_device_id": "85dfb79db3e414e586b3f88a543807ad4c46fc0e",
  "env_cloud": "localhost",
  "env_package_manager": "npm",
  "env_is_global": true,
  "env_auth_method": "theme_access_token",
  "env_is_wsl": false,
  "env_build_repository": "Shopify/cli",
  "cmd_app_warning_api_key_deprecation_displayed": false,
  "cmd_all_timing_network_ms": 1988,
  "cmd_all_timing_prompts_ms": 0,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "theme",
  "cmd_all_plugin": "@shopify/theme",
  "cmd_all_verbose": true,
  "cmd_all_path_override": true,
  "cmd_all_path_override_hash": "841405a36b63ebc1816e23aac7dbc837e6317736",
  "cmd_all_last_graphql_request_id": "04009162-67e8-4c03-b7ff-ffa9dc9dcfc6-1753651122",
  "cmd_all_timing_active_ms": 212,
  "cmd_all_exit": "unexpected_error",
  "user_id": "7484a527-5cd9-30ef-0035-f9a74c2b5510ed95f3d3",
  "request_ids": [
    "0f1c392a-6688-469b-95aa-1d4923edb6a3-1753651122",
    "5e85061a-ef5b-40ab-9af5-84aa494d4d9e-1753651122",
    "04009162-67e8-4c03-b7ff-ffa9dc9dcfc6-1753651122"
  ],
  "args": "-s ******************.myshopify.com --url / --theme ************ --password=***** --store-password=****** --verbose --json",
  "error_message": "Bad response: 500: ",
  "env_plugin_installed_all": "[\"@shopify/cli\"]",
  "metadata": "{\"extraPublic\":{},\"extraSensitive\":{}}"
}
2025-07-27T21:18:44.278Z: Reporting unhandled error to Bugsnag: Bad response: 500:
2025-07-27T21:18:44.434Z: Running system process:
  · Command: npm prefix
  · Working directory: /workspaces/shopify-theme

2025-07-27T21:18:44.495Z: Obtaining the dependency manager in directory /workspaces/shopify-theme...
  ```
</details>

### Reproduction steps

1. Install the latest version of Shopify CLI `npm i -g @shopify/cli@latest`
2. Acquire a valid access token for a given store
3. Run the following command, replacing the values with ones relevant to your store:
    ```bash
    shopify theme profile -s yourstore.myshopify.com --url / --theme 123456789012 --password=shptka_abcdef01234567890 --store-password=abcdef --json
    ```

### Operating System

Ubuntu 22.04 LTS (`Linux 0347df773eb3 6.10.14-linuxkit #1 SMP Sat May 17 08:28:57 UTC 2025 aarch64 GNU/Linux`)

### Shopify CLI version (`shopify --version`)

@shopify/cli/3.83.0 linux-arm64 node-v22.16.0

### Shell

bash

### Node version (run `node -v` if you're not sure)

v22.16.0

### What language and version are you using in your application?

N/A

===
