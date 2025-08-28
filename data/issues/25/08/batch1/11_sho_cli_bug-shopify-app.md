issue title: [Bug]: shopify app dev --reset HTTP 500 error
labels: Type: Bug
comment count: 0
hyperlink: https://github.com/shopify/cli/issues/6238
status: open
date opened: 2025-08-11
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

App

### Expected behavior

The app in question is a payment app with an offsite extension ready to be submitted.
Running the command should have allowed me to create a new app along the existing one.
The reason is to have a development version on a development domain while keeping the production version on the production domain.
Each version with its own .env and .toml config files

### Actual behavior

After choosing the organization, confirming it is a new app and filling the new name the cli crashes with a 500 HTTP error.
` `

### Verbose output

<details>
  <summary>The Partners GraphQL API responded unsuccessfully with errors:              
                                                                              
  [                                                                           
    {                                                                         
      "message": "Unexpected system error",                                   
      "extensions": {                                                         
        "code": "500"                                                         
      }                                                                       
    }                                                                         
  ] </summary>

  ```
  2025-08-11T09:34:52.979Z: Running command app dev
2025-08-11T09:34:52.990Z: Running system process in background:
  · Command: /home/robert/.nvm/versions/node/v22.16.0/bin/node /home/robert/.nvm/versions/node/v22.16.0/bin/shopify notifications list --ignore-errors
  · Working directory: /home/robert/payabl-checkout

2025-08-11T09:34:53.004Z: Notifications to show: 0
2025-08-11T09:34:53.045Z: Reading cached app information for directory /home/robert/payabl-checkout...
2025-08-11T09:34:53.046Z: Reading the content of file at shopify.app.development.toml...
2025-08-11T09:34:53.054Z: Reading the content of file at shopify.app.development.toml...
2025-08-11T09:34:53.057Z: Reading cached app information for directory /home/robert/payabl-checkout...
2025-08-11T09:34:53.058Z: Reading the content of file at shopify.app.development.toml...
2025-08-11T09:34:53.060Z: Reading the content of file at shopify.app.development.toml...
2025-08-11T09:34:53.068Z: Reading the content of file at shopify.app.production.toml...
2025-08-11T09:34:53.069Z: Reading the content of file at .gitignore...
2025-08-11T09:34:53.077Z: Reading cached app information for directory /home/robert/payabl-checkout...
2025-08-11T09:34:53.077Z: Reading the content of file at shopify.app.development.toml...
2025-08-11T09:34:53.079Z: Reading the content of file at shopify.app.development.toml...
2025-08-11T09:34:53.081Z: Reading the content of file at shopify.app.production.toml...
2025-08-11T09:34:53.089Z: Reading the content of file at .gitignore...
2025-08-11T09:34:53.091Z: Reading the .env file at .env.development
2025-08-11T09:34:53.092Z: Reading the content of file at .env.development...
2025-08-11T09:34:53.107Z: Reading the content of file at extensions/hosted-payment/shopify.extension.toml...
2025-08-11T09:34:53.108Z: Reading the content of file at extensions/hosted-payment/shopify.extension.toml...
2025-08-11T09:34:53.110Z: Reading the content of file at package.json...
2025-08-11T09:34:53.111Z: Reading the content of file at package.json...
2025-08-11T09:34:53.116Z: Running system process:
  · Command: npm prefix
  · Working directory: /home/robert/payabl-checkout

2025-08-11T09:34:53.307Z: Obtaining the dependency manager in directory /home/robert/payabl-checkout...
2025-08-11T09:34:53.308Z: Reading the content of file at package.json...
2025-08-11T09:34:53.309Z: Reading the content of file at .shopify/project.json...
2025-08-11T09:34:53.464Z: Reading the content of file at shopify.web.toml...
2025-08-11T09:34:53.477Z: Notifications to show: 0
2025-08-11T09:34:53.484Z: Ensuring that the user is authenticated with the Partners API with the following scopes:
[]

2025-08-11T09:34:53.486Z: Getting session store...
2025-08-11T09:34:53.491Z: Validating existing session against the scopes:
[
  "openid",
  "https://api.shopify.com/auth/shop.admin.graphql",
  "https://api.shopify.com/auth/shop.admin.themes",
  "https://api.shopify.com/auth/partners.collaborator-relationships.readonly",
  "https://api.shopify.com/auth/shop.storefront-renderer.devtools",
  "https://api.shopify.com/auth/partners.app.cli.access",
  "https://api.shopify.com/auth/destinations.readonly",
  "https://api.shopify.com/auth/organization.store-management",
  "https://api.shopify.com/auth/organization.on-demand-user-access",
  "https://api.shopify.com/auth/organization.apps.manage"
]
For applications:
{
  "partnersApi": {
    "scopes": []
  }
}

2025-08-11T09:34:53.495Z: - Token validation -> It's expired: false
2025-08-11T09:34:53.497Z: Getting partner account info from cache
2025-08-11T09:34:53.509Z: Sending "Partners" GraphQL request:
  query AllOrgs {
  organizations(first: 200) {
    nodes {
      id
      businessName
      __typename
    }
    __typename
  }
}

With request headers:
 - User-Agent: Shopify CLI; v=3.83.3
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-08-11T09:34:54.200Z: Request to https://partners.shopify.com/api/cli/graphql completed in 689 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"30a47c6aaae77f9039381b96512dcc74"
 - server-timing: processing;dur=212, socket_queue;dur=1.844, util;dur=0.5, cfRequestDuration;dur=328.999996
 - x-request-id: 387d9665-3502-4183-a28f-322e339d8989-1754904893
    
2025-08-11T09:34:54.204Z: Ensuring that the user is authenticated with the App Management API with the following scopes:
[]

2025-08-11T09:34:54.205Z: Getting session store...
2025-08-11T09:34:54.206Z: Validating existing session against the scopes:
[
  "openid",
  "https://api.shopify.com/auth/shop.admin.graphql",
  "https://api.shopify.com/auth/shop.admin.themes",
  "https://api.shopify.com/auth/partners.collaborator-relationships.readonly",
  "https://api.shopify.com/auth/shop.storefront-renderer.devtools",
  "https://api.shopify.com/auth/partners.app.cli.access",
  "https://api.shopify.com/auth/destinations.readonly",
  "https://api.shopify.com/auth/organization.store-management",
  "https://api.shopify.com/auth/organization.on-demand-user-access",
  "https://api.shopify.com/auth/organization.apps.manage"
]
For applications:
{
  "appManagementApi": {
    "scopes": []
  },
  "businessPlatformApi": {
    "scopes": []
  }
}

2025-08-11T09:34:54.207Z: - Token validation -> It's expired: false
2025-08-11T09:34:54.208Z: Sending "BusinessPlatform" GraphQL request:
  query UserInfo {
  currentUserAccount {
    uuid
    email
    organizations(first: 2) {
      nodes {
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With request headers:
 - User-Agent: Shopify CLI; v=3.83.3
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://destinations.shopifysvc.com/destinations/api/2020-07/graphql
2025-08-11T09:34:54.210Z: Sending "BusinessPlatform" GraphQL request:
  query ListOrganizations {
  currentUserAccount {
    uuid
    organizations(hasAccessToDestination: DEVELOPER_DASHBOARD) {
      nodes {
        id
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With request headers:
 - User-Agent: Shopify CLI; v=3.83.3
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://destinations.shopifysvc.com/destinations/api/2020-07/graphql
2025-08-11T09:34:54.450Z: Request to https://destinations.shopifysvc.com/destinations/api/2020-07/graphql completed in 239 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"8bc9b683cc3610f4cd72d5c5765e2b04"
 - server-timing: processing;dur=83, socket_queue;dur=2.245, util;dur=0.0, cfRequestDuration;dur=200.999975
 - x-request-id: 2f5fad2f-f86e-4638-8652-d763759ebbd9-1754904894
    
?  Which organization is this work for?
✔  payabl. CY Limited  (Partner Dashboard)

2025-08-11T09:34:58.507Z: Ensuring that the user is authenticated with the Partners API with the following scopes:
[]

2025-08-11T09:34:58.507Z: Getting session store...
2025-08-11T09:34:58.508Z: Validating existing session against the scopes:
[
  "openid",
  "https://api.shopify.com/auth/shop.admin.graphql",
  "https://api.shopify.com/auth/shop.admin.themes",
  "https://api.shopify.com/auth/partners.collaborator-relationships.readonly",
  "https://api.shopify.com/auth/shop.storefront-renderer.devtools",
  "https://api.shopify.com/auth/partners.app.cli.access",
  "https://api.shopify.com/auth/destinations.readonly",
  "https://api.shopify.com/auth/organization.store-management",
  "https://api.shopify.com/auth/organization.on-demand-user-access",
  "https://api.shopify.com/auth/organization.apps.manage"
]
For applications:
{
  "partnersApi": {
    "scopes": []
  }
}

2025-08-11T09:34:58.508Z: - Token validation -> It's expired: false
2025-08-11T09:34:58.509Z: Getting partner account info from cache
2025-08-11T09:34:58.514Z: Sending "Partners" GraphQL request:
  query FindOrganization($id: ID!, $title: String) {
    organizations(id: $id, first: 1) {
      nodes {
        id
        businessName
        apps(first: 25, title: $title) {
          pageInfo {
            hasNextPage
          }
          nodes {
            id
            title
            apiKey
          }
        }
      }
    }
  }

With variables:
{
  "id": "4153850"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.83.3
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-08-11T09:34:58.758Z: Request to https://partners.shopify.com/api/cli/graphql completed in 244 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"d240c5fd2fb3c169abc94a32ba16f3ae"
 - server-timing: processing;dur=91, socket_queue;dur=2.237, util;dur=0.3, cfRequestDuration;dur=214.999914
 - x-request-id: bc20b3e9-4b55-4b2a-8db1-62933e6d9a69-1754904898
    
?  Create this project as a new app on Shopify?
✔  Yes, create it as a new app

?  App name:
✔  payabl-dev

2025-08-11T09:35:09.285Z: Sending "Partners" GraphQL request:
  mutation AppCreate(
    $org: Int!
    $title: String!
    $appUrl: Url!
    $redir: [Url]!
    $type: AppType
    $requestedAccessScopes: [String!]
  ) {
    appCreate(
      input: {
        organizationID: $org
        title: $title
        applicationUrl: $appUrl
        redirectUrlWhitelist: $redir
        appType: $type
        requestedAccessScopes: $requestedAccessScopes
      }
    ) {
      app {
        id
        title
        apiKey
        organizationId
        apiSecretKeys {
          secret
        }
        appType
        grantedScopes
        applicationUrl
        redirectUrlWhitelist
        requestedAccessScopes
        webhookApiVersion
        embedded
        posEmbedded
        preferencesUrl
        gdprWebhooks {
          customerDeletionUrl
          customerDataRequestUrl
          shopDeletionUrl
        }
        appProxy {
          subPath
          subPathPrefix
          url
        }
        disabledFlags
      }
      userErrors {
        field
        message
      }
    }
  }

With variables:
{
  "org": 4153850,
  "title": "payabl-dev",
  "appUrl": "https://example.com",
  "redir": [
    "https://example.com/api/auth"
  ],
  "requestedAccessScopes": [
    "read_payment_gateways",
    "read_payment_sessions",
    "write_payment_gateways",
    "write_payment_sessions"
  ],
  "type": "undecided"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.83.3
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-08-11T09:35:09.756Z: Request to https://partners.shopify.com/api/cli/graphql completed in 469 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"307ce8c20eb717c29fecaea0a7e9e910"
 - server-timing: processing;dur=326, socket_queue;dur=1.667, util;dur=0.5, cfRequestDuration;dur=451.999903
 - x-request-id: 3a71f017-442c-4c05-8aab-e6c3dc386b11-1754904909
    
╭─ error ──────────────────────────────────────────────────────────────────────╮
│                                                                              │
│                                                                              │
│  The Partners GraphQL API responded unsuccessfully with errors:              │
│                                                                              │
│  [                                                                           │
│    {                                                                         │
│      "message": "Unexpected system error",                                   │
│      "extensions": {                                                         │
│        "code": "500"                                                         │
│      }                                                                       │
│    }                                                                         │
│  ]                                                                           │
│                                                                              │
│  Request ID: 3a71f017-442c-4c05-8aab-e6c3dc386b11-1754904909                 │
│                                                                              │
│                                                                              │
│  To investigate the issue, examine this stack trace:                         │
│    at makeRequest (home/robert/.nvm/versions/node/v22.16.0/lib/node_modules  │
│    /@shopify/cli/dist/chunk-DRATBB26.js:27347)                               │
│    at processTicksAndRejections (node:internal/process/task_queues:105)      │
│    at rawGraphQLRequest [as request] (home/robert/.nvm/versions/node/v22.16  │
│    .0/lib/node_modules/@shopify/cli/dist/chunk-JEQ7HZCS.js:136554)           │
│    at async runRequestWithNetworkLevelRetry (home/robert/.nvm/versions/node  │
│    /v22.16.0/lib/node_modules/@shopify/cli/dist/chunk-DRATBB26.js:27402)     │
│    at async makeVerboseRequest (home/robert/.nvm/versions/node/v22.16.0/lib  │
│    /node_modules/@shopify/cli/dist/chunk-DRATBB26.js:27413)                  │
│    at async retryAwareRequest (home/robert/.nvm/versions/node/v22.16.0/lib/  │
│    node_modules/@shopify/cli/dist/chunk-DRATBB26.js:27500)                   │
│    at (home/robert/.nvm/versions/node/v22.16.0/lib/node_modules/@shopify/cl  │
│    i/dist/chunk-JEQ7HZCS.js:136572)                                          │
│    at (home/robert/.nvm/versions/node/v22.16.0/lib/node_modules/@shopify/cl  │
│    i/dist/chunk-UNQM4BV5.js:30309)                                           │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

2025-08-11T09:35:09.853Z: Running system process:
  · Command: npm prefix
  · Working directory: /home/robert/payabl-checkout

2025-08-11T09:35:10.009Z: Obtaining the dependency manager in directory /home/robert/payabl-checkout...
2025-08-11T09:35:10.306Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 145 ms
With response headers:
 - x-request-id: d9b55ea8-ae88-4813-b760-456ed60263ca
    
2025-08-11T09:35:10.307Z: Analytics event sent: {
  "command": "app dev",
  "time_start": 1754904892980,
  "time_end": 1754904909818,
  "total_time": 16838,
  "success": false,
  "cli_version": "3.83.3",
  "ruby_version": "",
  "node_version": "22.16.0",
  "is_employee": false,
  "uname": "linux amd64",
  "env_ci": false,
  "env_plugin_installed_any_custom": false,
  "env_plugin_installed_shopify": "[\"@shopify/cli\"]",
  "env_shell": "bash",
  "env_device_id": "05cc4c35f9d0f7e4440cc23d370a04fc279bc095",
  "env_cloud": "localhost",
  "env_package_manager": "npm",
  "env_is_global": true,
  "env_auth_method": "device_auth",
  "env_is_wsl": false,
  "env_build_repository": "Shopify/cli",
  "cmd_app_warning_api_key_deprecation_displayed": false,
  "cmd_app_all_configs_any": true,
  "cmd_app_all_configs_clients": "{\"shopify.app.development.toml\":\"69f3732db324c20533d3af1b49cfa316\",\"shopify.app.production.toml\":\"69f3732db324c20533d3af1b49cfa316\"}",
  "cmd_app_linked_config_used": true,
  "cmd_app_linked_config_name": "shopify.app.development.toml",
  "cmd_app_linked_config_git_tracked": true,
  "cmd_app_linked_config_source": "cached",
  "cmd_app_linked_config_uses_cli_managed_urls": false,
  "project_type": "node",
  "app_extensions_any": true,
  "app_extensions_breakdown": "{\"payments_extension\":1}",
  "app_extensions_count": 1,
  "app_extensions_custom_layout": false,
  "app_extensions_function_any": false,
  "app_extensions_function_count": 0,
  "app_extensions_theme_any": false,
  "app_extensions_theme_count": 0,
  "app_extensions_ui_any": false,
  "app_extensions_ui_count": 0,
  "app_name_hash": "c0e74e030cf7fa181c0c6fa46ed7ee6a889df25d",
  "app_path_hash": "f4e8ae25bab712c13181933928083f2049e64475",
  "app_scopes": "[\"read_payment_gateways\",\"read_payment_sessions\",\"write_payment_gateways\",\"write_payment_sessions\"]",
  "app_web_backend_any": true,
  "app_web_backend_count": 1,
  "app_web_custom_layout": true,
  "app_web_framework": "remix",
  "app_web_frontend_any": true,
  "app_web_frontend_count": 1,
  "env_package_manager_workspaces": true,
  "cmd_all_timing_network_ms": 1674,
  "cmd_all_timing_prompts_ms": 14571,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "app",
  "cmd_all_plugin": "@shopify/app",
  "cmd_all_verbose": true,
  "cmd_all_path_override": true,
  "cmd_all_path_override_hash": "f4e8ae25bab712c13181933928083f2049e64475",
  "cmd_app_dependency_installation_skipped": false,
  "cmd_app_reset_used": true,
  "cmd_dev_tunnel_type": "auto",
  "cmd_all_last_graphql_request_id": "3a71f017-442c-4c05-8aab-e6c3dc386b11-1754904909",
  "cmd_all_timing_active_ms": 592,
  "cmd_all_exit": "unexpected_error",
  "user_id": "51048e06-7113-4f68-bc31-0609f202a4c0",
  "request_ids": [
    "387d9665-3502-4183-a28f-322e339d8989-1754904893",
    "2f5fad2f-f86e-4638-8652-d763759ebbd9-1754904894",
    "bc20b3e9-4b55-4b2a-8db1-62933e6d9a69-1754904898",
    "3a71f017-442c-4c05-8aab-e6c3dc386b11-1754904909"
  ],
  "args": "--reset --verbose",
  "error_message": "\nThe Partners GraphQL API responded unsuccessfully with errors:\n\n\u001b[33m[\n  {\n    \u001b[0m\u001b[37m\"message\":\u001b[33m \u001b[0m\u001b[32m\"Unexpected system error\"\u001b[33m,\n    \u001b[0m\u001b[37m\"extensions\":\u001b[33m {\n      \u001b[0m\u001b[37m\"code\":\u001b[33m \u001b[0m\u001b[32m\"500\"\u001b[33m\n    }\n  }\n]\u001b[0m\n      \nRequest ID: 3a71f017-442c-4c05-8aab-e6c3dc386b11-1754904909\n",
  "app_name": "payabl-checkout",
  "env_plugin_installed_all": "[\"@shopify/cli\"]",
  "metadata": "{\"extraPublic\":{},\"extraSensitive\":{}}"
}
2025-08-11T09:35:10.312Z: Reporting unhandled error to Bugsnag: 
The Partners GraphQL API responded unsuccessfully with errors:

[
  {
    "message": "Unexpected system error",
    "extensions": {
      "code": "500"
    }
  }
]
      
Request ID: 3a71f017-442c-4c05-8aab-e6c3dc386b11-1754904909

2025-08-11T09:35:10.527Z: Running system process:
  · Command: npm prefix
  · Working directory: /home/robert/payabl-checkout

2025-08-11T09:35:10.663Z: Obtaining the dependency manager in directory /home/robert/payabl-checkout..
  ```

</details>

### Reproduction steps

1.
2.
3.

### Operating System

Debian GNU/Linux 12

### Shopify CLI version (`shopify --version`)

3.83.3

### Shell

bash

### Node version (run `node -v` if you're not sure)

v22.16.0

### What language and version are you using in your application?

_No response_

===
