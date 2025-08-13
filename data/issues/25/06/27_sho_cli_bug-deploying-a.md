issue title: [Bug]: Deploying app succeeds but does not update the web pixel
labels: Type: Bug
comment count: 1
hyperlink: https://github.com/shopify/cli/issues/6034
status: open
date opened: 2025-06-27
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Extension

### Expected behavior

According to [Shopify Docs](https://shopify.dev/docs/apps/launch/deployment/deploy-app-versions), the web pixel should update within a few minutes after successful deployment across all stores.

### Actual behavior

Deploying app succeed, a new version is created, but the web pixel has not updated. It's been hours since the last production deployment.

### Verbose output

<details>
  <summary>Verbose output</summary>

  ```
  yarn deploy -f --source-control-url "$COMMIT_URL" --verbose
  2025-07-01T12:38:08.774Z: Checking if there's a version of @shopify/cli newer than 3.81.2
  2025-07-01T12:38:08.775Z: Getting the latest version of NPM package: @shopify/cli
  2025-07-01T12:38:08.794Z: Running command app deploy
  2025-07-01T12:38:08.816Z: Reading cached app information for directory /home/runner/work/shopify-integration/shopify-integration/convert-app-v1...
  2025-07-01T12:38:08.819Z: Reading the content of file at shopify.app.production.toml...
  2025-07-01T12:38:08.824Z: Reading the content of file at shopify.app.production.toml...
  2025-07-01T12:38:08.828Z: Reading cached app information for directory /home/runner/work/shopify-integration/shopify-integration/convert-app-v1...
  2025-07-01T12:38:08.828Z: Reading the content of file at shopify.app.production.toml...
  2025-07-01T12:38:08.831Z: Reading the content of file at shopify.app.production.toml...
  2025-07-01T12:38:08.832Z: Ensuring that the user is authenticated with the Partners API with the following scopes:
  []

  2025-07-01T12:38:08.834Z: Sending POST request to URL https://accounts.shopify.com/oauth/token?grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3&audience=271e16d403dfa18082ffb3d197bd2b5f4479c3fc32736d69296829cbb28d41a6&scope=https%3A%2F%2Fapi.shopify.com%2Fauth%2Fpartners.app.cli.access&subject_token=****
  With request headers:


  2025-07-01T12:38:08.991Z: Request to https://accounts.shopify.com/oauth/token?grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3&audience=271e16d403dfa18082ffb3d197bd2b5f4479c3fc32736d69296829cbb28d41a6&scope=https%3A%2F%2Fapi.shopify.com%2Fauth%2Fpartners.app.cli.access&subject_token=**** completed in 157 ms
  With response headers:
  - cache-control: no-cache, no-store, private, must-revalidate, max-age=0
  - content-type: application/json; charset=utf-8
  - etag: W/"c70a576a510e21a93ed65d87e36b9780"
  - server-timing: processing;dur=33, socket_queue;dur=1.216, edge;dur=1.034, util;dur=0.05, cfRequestDuration;dur=122.999907
  - x-request-id: abfb4871-8922-4962-bf49-102df8dd65fa-1751373488
      
  2025-07-01T12:38:09.001Z: Sending "Partners" GraphQL request:
    query currentAccountInfo {
      currentAccountInfo {
        __typename
        ... on ServiceAccount {
          orgName
        }
        ... on UserAccount {
          email
        }
      }
    }

  With request headers:
  - User-Agent: Shopify CLI; v=3.81.2
  - Keep-Alive: timeout=30
    "app_web_framework": "remix",
    "app_web_frontend_any": true,
    "app_web_frontend_count": 1,
    "env_package_manager_workspaces": true,
    "partner_id": 3561226,
    "api_key": "****",
    "cmd_app_reset_used": false,
    "cmd_deploy_include_config_used": true,
    "cmd_deploy_config_modules_breakdown": "[\"access_scopes\",\"application_url\",\"auth\",\"embedded\",\"handle\",\"name\",\"pos\",\"webhooks\"]",
    "cmd_all_timing_network_ms": 7608,
    "cmd_all_timing_prompts_ms": 0,
    "cmd_all_launcher": "yarn",
    "cmd_all_topic": "app",
    "cmd_all_plugin": "@shopify/app",
    "cmd_all_force": false,
    "cmd_all_verbose": true,
    "cmd_all_path_override": true,
    "cmd_all_path_override_hash": "380368d62993732d832d29e726168cdff935fcda",
    "cmd_all_last_graphql_request_id": "84ce36c3-ca85-48c2-a77d-fcd345bff2b8-1751373496",
    "cmd_all_timing_active_ms": 2606,
    "cmd_all_exit": "ok",
    "user_id": "5e81f37d-e1ab-0da7-77f2-d6025fed9b39d0e9bba4",
    "request_ids": [
      "d0068f10-33ef-42a9-9d5d-88dcdc59d212-1751373489",
      "d7fef988-232d-4631-b26f-7e485c62f5af-1751373489",
      "e00ab66b-d287-4cc3-8c95-9834fd5dd6b6-1751373490",
      "4501ade0-f28e-43e9-86ac-2d14bdb60d9f-1751373490",
      "a4dace3e-dfdd-4b81-a40f-471feabf0f3c-1751373492",
      "f5de852e-e60d-4c6b-ae19-3a773763b909-1751373493",
      "a067ce55-3de5-42df-b561-4956023d3ebc-1751373495",
      "84ce36c3-ca85-48c2-a77d-fcd345bff2b8-1751373496"
    ],
    "args": "--config production -f --source-control-url https://github.com/convertcom/shopify-integration/commit/43d859007020d65edcaa2d217e740e66b2ae83aa --verbose",
    "app_name": "convert-web-pixel",
    "env_plugin_installed_all": "[\"@shopify/cli\"]",
    "metadata": "{\"extraPublic\":{},\"extraSensitive\":{}}"
  }
  2025-07-01T12:38:19.208Z: Completed command app deploy
  ```

</details>

### Reproduction steps

1. Open any of the following stores:
   - https://onyxcookware.de/collections/bratpfannen
   - https://scandinavianbiolabs.com/
   - https://letsliveitup.com/
2. Console logs should contain the following message: `Convert Web Pixel #80: Registering...` - instead it shows `Convert Web Pixel: Registering...` (_that's from the outdated version_).

Note that the above test store is having the app [Convert Experiences](https://apps.shopify.com/convert-experiences) already installed and the deploy happens though CI/CD pipeline via GitHub Actions (_deploy succeeds as shown at the verbose output above_).

### Operating System

Ubuntu 24.04

### Shopify CLI version (`shopify --version`)

3.81.2

### Shell

Git Bash

### Node version (run `node -v` if you're not sure)

v20.19.2

### What language and version are you using in your application?

_No response_

===

comment #1 by abbaseya, 2025-07-02, 10:31:05
**Update:** We suspect that when the web pixel TOML settings schema contains new fields that are not present in the existing GraphQL schema for installed stores, Shopify is silently failing to update the web pixel code after publishing a new app version. 

The deployment process completes successfully (CLI reports success, new version is created and released), but customers' stores continue running the old web pixel code while theme extensions update correctly.

If this is the case, it means we need to manually update the web pixel for all existing app installations whenever we add new settings fields, but it's unclear:
1. How to programmatically update web pixels for all installed stores
2. Whether webPixelUpdate can handle schema mismatches gracefully
3. If there's a way to detect which stores failed to update
4. Whether delete/recreate is the only solution (which would lose customer settings)

This creates a significant deployment problem for apps that need to evolve their web pixel settings over time.
