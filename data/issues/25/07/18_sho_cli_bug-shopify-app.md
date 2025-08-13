issue title: [Bug]: shopify app generate extension with a Typescript flavor fails on the graphql-code-generator command
labels: Type: Bug
comment count: 5
hyperlink: https://github.com/shopify/cli/issues/6132
status: open
date opened: 2025-07-18
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Extension

### Expected behavior

Generating an extension targeting Typescript via the cli should succeed.

### Actual behavior

The `npm exec -- graphql-code-generator --config package.json` command fails to complete stating `Cannot convert undefined or null to object`



### Verbose output

<details>
  <summary>Verbose output</summary>

Running the command directly (not using the shopify cli)
  ```
npm exec -- graphql-code-generator --config package.json --verbose
(node:93831) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
(Use `node --trace-deprecation ...` to show where the warning was created)
  ✖ Parse configuration
    → Cannot convert undefined or null to object
    Generate outputs
Cannot convert undefined or null to object
Cannot convert undefined or null to object
  ```

</details>

### Reproduction steps

```
▶ shopify app generate extension
?  Type of extension?
✔  Cart and checkout validation — Function

?  Name your extension:
✔  purchase-validation

?  What would you like to work in?
✔  TypeScript

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Building GraphQL types ...
(node:93510) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.

── external error ──────────────────────────────────────────────────────────────

Error coming from `npm exec -- graphql-code-generator --config package.json`

Command failed with exit code 1: npm exec -- graphql-code-generator --config package.json
(node:93510) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland
alternative instead.
(Use `node --trace-deprecation ...` to show where the warning was created)
Cannot convert undefined or null to object
[07:57:31] Parse configuration [started]
[07:57:31] Parse configuration [failed]
[07:57:31] → Cannot convert undefined or null to object

────────────────────────────────────────────────────────────────────────────────
```

### Operating System

MacOS Sequoia Version 15.5 (24F74)

### Shopify CLI version (`shopify --version`)

@shopify/cli/3.82.1 darwin-arm64 node-v22.6.0

### Shell

iterm2 w/ zsh

### Node version (run `node -v` if you're not sure)

v22.6.0

### What language and version are you using in your application?

Typescript

===

comment #1 by kayluhb, 2025-07-18, 13:06:42
Note that Rust and wasm extension creation works

comment #2 by nickwesselman, 2025-07-18, 13:47:50
Can you confirm what package manager you are using with your app, and provide the `--verbose` output?

comment #3 by kayluhb, 2025-07-18, 17:01:38
pnpm 10.12.4

```sh
▶ shopify app generate extension --verbose
2025-07-18T16:59:43.746Z: Running command app generate extension
2025-07-18T16:59:43.748Z: Running system process in background:
  · Command: /Users/kayluhb/.nvm/versions/node/v22.6.0/bin/node /Users/kayluhb/Library/pnpm/global/5/.pnpm/@shopify+cli@3.82.1/node_modules/@shopify/cli/bin/run.js notifications list --ignore-errors
  · Working directory: /Users/kayluhb/Projects/checkout

2025-07-18T16:59:43.752Z: Notifications to show: 0
2025-07-18T16:59:43.759Z: Reading cached app information for directory /Users/kayluhb/Projects/checkout...
2025-07-18T16:59:43.759Z: Reading the content of file at shopify.app.toml...
2025-07-18T16:59:43.761Z: Reading the content of file at shopify.app.toml...
2025-07-18T16:59:43.762Z: Ensuring that the user is authenticated with the Partners API with the following scopes:
[]

2025-07-18T16:59:43.762Z: Getting session store...
2025-07-18T16:59:43.763Z: Validating existing session against the scopes:
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

2025-07-18T16:59:43.763Z: - Token validation -> It's expired: false
2025-07-18T16:59:43.763Z: Getting partner account info from cache
2025-07-18T16:59:43.768Z: Sending "Partners" GraphQL request:
  query FindApp($apiKey: String!) {
    app(apiKey: $apiKey) {
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
      developmentStorePreviewEnabled
      disabledFlags
    }
  }

With variables:
{
  "apiKey": "*****"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.1
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-18T16:59:44.496Z: Request to https://partners.shopify.com/api/cli/graphql completed in 728 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"27f8cc2dcb13340cd18223b138a07874"
 - server-timing: processing;dur=606, socket_queue;dur=2.263, util;dur=0.6, cfRequestDuration;dur=664.999962
 - x-request-id: 8836d5f8-223c-477a-bca9-1ae49b82d9af-1752857983

2025-07-18T16:59:44.502Z: Sending "Partners" GraphQL request:
  query FindOrganization($id: ID!) {
    organizations(id: $id, first: 1) {
      nodes {
        id
        businessName
      }
    }
  }

With variables:
{
  "id": "3341693"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.1
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-18T16:59:44.653Z: Sending "Partners" GraphQL request:
  query fetchSpecifications($apiKey: String!) {
    extensionSpecifications(apiKey: $apiKey) {
      name
      externalName
      externalIdentifier
      identifier
      gated
      experience
      options {
        managementExperience
        registrationLimit
      }
      features {
        argo {
          surface
        }
      }
      validationSchema {
        jsonSchema
      }
    }
  }

With variables:
{
  "apiKey": "*****"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.1
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-18T16:59:44.909Z: Request to https://partners.shopify.com/api/cli/graphql completed in 256 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"9af44f976738e1ba7550be4915afe001"
 - server-timing: processing;dur=51, socket_queue;dur=1.784, util;dur=0.2, cfRequestDuration;dur=197.000027
 - x-request-id: 1c5287df-17d7-4fe5-92bf-fd1d805759bf-1752857984

2025-07-18T16:59:44.919Z: The following extension specifications were defined locally but not found in the remote specifications: payments_extension, tax_calculation
2025-07-18T16:59:44.921Z: Reading the content of file at .gitignore...
2025-07-18T16:59:44.928Z: Reading the content of file at package.json...
2025-07-18T16:59:44.929Z: Reading the content of file at package.json...
2025-07-18T16:59:44.930Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/kayluhb/Projects/checkout

2025-07-18T16:59:45.064Z: Obtaining the dependency manager in directory /Users/kayluhb/Projects/checkout...
2025-07-18T16:59:45.065Z: Reading the content of file at package.json...
2025-07-18T16:59:45.065Z: Reading the content of file at .shopify/project.json...
2025-07-18T16:59:45.069Z: Reading the content of file at shopify.web.toml...
2025-07-18T16:59:45.070Z: Notifications to show: 0
2025-07-18T16:59:45.071Z: Reading cached app information for directory /Users/kayluhb/Projects/checkout...
2025-07-18T16:59:45.072Z: Storing app information for directory /Users/kayluhb/Projects/checkout:{
  "appId": "dc483f71094e4c3743c30bbedc95390e",
  "title": "checkout",
  "directory": "/Users/kayluhb/Projects/checkout",
  "orgId": "3341693"
}
2025-07-18T16:59:45.079Z: Sending "Partners" GraphQL request:
  query RemoteTemplateSpecifications($version: String, $apiKey: String) {
    templateSpecifications(version: $version, apiKey: $apiKey) {
      identifier
      name
      defaultName
      group
      sortPriority
      supportLinks
      types {
        url
        type
        extensionPoints
        supportedFlavors {
          name
          value
          path
        }
      }
    }
  }

With variables:
{
  "apiKey": "*****"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.1
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-18T16:59:45.647Z: Request to https://partners.shopify.com/api/cli/graphql completed in 568 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"7f8dd293a0bb5dc79d017afd9ca93ad3"
 - server-timing: processing;dur=227, socket_queue;dur=31.336, util;dur=0.5, cfRequestDuration;dur=508.999825
 - x-request-id: 66a73806-4127-4ded-affe-7264ac252b31-1752857985

?  Type of extension?
✔  Cart and checkout validation — Function

?  Name your extension:
✔  checkout-validator

?  What would you like to work in?
✔  TypeScript

2025-07-18T16:59:54.209Z: Creating directory at extensions/checkout-validator...
2025-07-18T16:59:54.209Z: Creating an empty file at extensions/checkout-validator/.shopify.lock...
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Generating function extension ...
2025-07-18T16:59:54.218Z: Creating directory at /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download...
2025-07-18T16:59:54.219Z: Git-cloning repository https://github.com/Shopify/extensions-templates into /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download...
2025-07-18T16:59:54.223Z: Running system process:
  · Command: git --version
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Generating function extension ...
2025-07-18T16:59:54.881Z: Copying template from directory /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js to extensions/checkout-validator
2025-07-18T16:59:54.885Z: Checking if /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/index.liquid is a directory...
2025-07-18T16:59:54.885Z: Checking if /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/cart_validations_generate_run.test.liquid is a directory...
2025-07-18T16:59:54.885Z: Checking if /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/cart_validations_generate_run.liquid is a directory...
2025-07-18T16:59:54.885Z: Checking if /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/cart_validations_generate_run.graphql.liquid is a directory...
2025-07-18T16:59:54.886Z: Checking if /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/locales/en.default.json.liquid is a directory...
2025-07-18T16:59:54.886Z: Checking if /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/vite.config.js is a directory...
2025-07-18T16:59:54.886Z: Checking if /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/shopify.extension.toml.liquid is a directory...
2025-07-18T16:59:54.886Z: Checking if /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/schema.graphql is a directory...
2025-07-18T16:59:54.886Z: Checking if /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/package.json.liquid is a directory...
2025-07-18T16:59:54.886Z: Checking if /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/.gitignore is a directory...
2025-07-18T16:59:54.886Z: Creating directory at extensions/checkout-validator/src...
2025-07-18T16:59:54.886Z: Creating directory at extensions/checkout-validator/src...
2025-07-18T16:59:54.886Z: Creating directory at extensions/checkout-validator/src...
2025-07-18T16:59:54.886Z: Creating directory at extensions/checkout-validator/src...
2025-07-18T16:59:54.886Z: Copying file from /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/vite.config.js to extensions/checkout-validator/vite.config.js...
2025-07-18T16:59:54.886Z: Creating directory at extensions/checkout-validator/locales...
2025-07-18T16:59:54.886Z: Creating directory at extensions/checkout-validator...
2025-07-18T16:59:54.886Z: Copying file from /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/schema.graphql to extensions/checkout-validator/schema.graphql...
2025-07-18T16:59:54.886Z: Creating directory at extensions/checkout-validator...
2025-07-18T16:59:54.886Z: Copying file from /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/.gitignore to extensions/checkout-validator/.gitignore...
2025-07-18T16:59:54.886Z: Reading the content of file at /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/cart_validations_generate_run.test.liquid...
2025-07-18T16:59:54.887Z: Reading the content of file at /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/locales/en.default.json.liquid...
2025-07-18T16:59:54.887Z: Reading the content of file at /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/cart_validations_generate_run.graphql.liquid...
2025-07-18T16:59:54.887Z: Reading the content of file at /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/cart_validations_generate_run.liquid...
2025-07-18T16:59:54.887Z: Reading the content of file at /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/index.liquid...
2025-07-18T16:59:54.887Z: Reading the content of file at /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/shopify.extension.toml.liquid...
2025-07-18T16:59:54.888Z: Reading the content of file at /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/package.json.liquid...
2025-07-18T16:59:54.891Z: Copying file from /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/cart_validations_generate_run.test.liquid to extensions/checkout-validator/src/cart_validations_generate_run.test...
2025-07-18T16:59:54.892Z: Copying file from /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/locales/en.default.json.liquid to extensions/checkout-validator/locales/en.default.json...
2025-07-18T16:59:54.892Z: Copying file from /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/cart_validations_generate_run.graphql.liquid to extensions/checkout-validator/src/cart_validations_generate_run.graphql...
2025-07-18T16:59:54.892Z: Copying file from /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/index.liquid to extensions/checkout-validator/src/index...
2025-07-18T16:59:54.892Z: Copying file from /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/src/cart_validations_generate_run.liquid to extensions/checkout-validator/src/cart_validations_generate_run...
2025-07-18T16:59:54.892Z: Copying file from /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/shopify.extension.toml.liquid to extensions/checkout-validator/shopify.extension.toml...
2025-07-18T16:59:54.892Z: Copying file from /private/var/folders/jy/kmd3x0yx13v6bwk5v7_m705m0000gn/T/7ac6e79f4189601f45e8ede7c78c2b94/download/functions-cart-checkout-validation-js/package.json.liquid to extensions/checkout-validator/package.json...
2025-07-18T16:59:54.893Z: Writing some content to file at extensions/checkout-validator/src/cart_validations_generate_run.test...
2025-07-18T16:59:54.894Z: Writing some content to file at extensions/checkout-validator/package.json...
2025-07-18T16:59:54.894Z: Writing some content to file at extensions/checkout-validator/shopify.extension.toml...
2025-07-18T16:59:54.894Z: Writing some content to file at extensions/checkout-validator/src/cart_validations_generate_run.graphql...
2025-07-18T16:59:54.894Z: Writing some content to file at extensions/checkout-validator/locales/en.default.json...
2025-07-18T16:59:54.894Z: Writing some content to file at extensions/checkout-validator/src/index...
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Generating function extension ...
2025-07-18T16:59:54.928Z: Adding the following dependencies if needed:
[
  {
    "name": "@shopify/shopify_function",
    "version": "~2.0.0"
  }
]
With options:
{
  "packageManager": "pnpm",
  "type": "prod",
  "directory": "/Users/kayluhb/Projects/checkout/extensions/checkout-validator"
}

2025-07-18T16:59:54.928Z: Reading the content of file at extensions/checkout-validator/package.json...
2025-07-18T16:59:54.930Z: Running system process:
  · Command: npm exec -- graphql-code-generator --config package.json
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Building GraphQL types ...
(node:4373) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.

2025-07-18T16:59:56.990Z: Removing file at extensions/checkout-validator...
── external error ──────────────────────────────────────────────────────────────

Error coming from `npm exec -- graphql-code-generator --config package.json`

Command failed with exit code 1: npm exec -- graphql-code-generator --config package.json
(node:4373) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland
alternative instead.
(Use `node --trace-deprecation ...` to show where the warning was created)
Cannot convert undefined or null to object
[11:59:56] Parse configuration [started]
[11:59:56] Parse configuration [failed]
[11:59:56] → Cannot convert undefined or null to object

────────────────────────────────────────────────────────────────────────────────

2025-07-18T16:59:56.995Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/kayluhb/Projects/checkout

2025-07-18T16:59:57.102Z: Obtaining the dependency manager in directory /Users/kayluhb/Projects/checkout...
2025-07-18T16:59:57.287Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 75 ms
With response headers:
 - x-request-id: cde799b6-f399-43ae-b3db-07f0d43cf16c

2025-07-18T16:59:57.288Z: Analytics event sent: {
  "command": "app scaffold extension",
  "time_start": 1752857983746,
  "time_end": 1752857996993,
  "total_time": 13247,
  "success": false,
  "cli_version": "3.82.1",
  "ruby_version": "",
  "node_version": "22.6.0",
  "is_employee": false,
  "uname": "darwin arm64",
  "env_ci": false,
  "env_plugin_installed_any_custom": false,
  "env_plugin_installed_shopify": "[\"@shopify/cli\"]",
  "env_shell": "zsh",
  "env_device_id": "e9a165296c1a0a8b6d568cab7dc6d678158becc1",
  "env_cloud": "localhost",
  "env_package_manager": "pnpm",
  "env_is_global": true,
  "env_auth_method": "device_auth",
  "env_is_wsl": false,
  "cmd_app_warning_api_key_deprecation_displayed": false,
  "cmd_scaffold_required_auth": true,
  "cmd_scaffold_template_custom": false,
  "cmd_scaffold_type_owner": "@shopify/app",
  "cmd_app_all_configs_any": true,
  "cmd_app_all_configs_clients": "{\"shopify.app.toml\":\"dc483f71094e4c3743c30bbedc95390e\"}",
  "cmd_app_linked_config_used": true,
  "cmd_app_linked_config_name": "shopify.app.toml",
  "cmd_app_linked_config_git_tracked": true,
  "cmd_app_linked_config_source": "cached",
  "cmd_app_linked_config_uses_cli_managed_urls": true,
  "project_type": "node",
  "app_extensions_any": false,
  "app_extensions_breakdown": "{}",
  "app_extensions_count": 0,
  "app_extensions_custom_layout": false,
  "app_extensions_function_any": false,
  "app_extensions_function_count": 0,
  "app_extensions_theme_any": false,
  "app_extensions_theme_count": 0,
  "app_extensions_ui_any": false,
  "app_extensions_ui_count": 0,
  "app_name_hash": "fe0fa9c92d0b0c3e2dd38b2172d174535a42afbc",
  "app_path_hash": "c0ba6dc46deec8e1bc918c1dca1cca326c985e0d",
  "app_scopes": "[\"write_products\"]",
  "app_web_backend_any": true,
  "app_web_backend_count": 1,
  "app_web_custom_layout": true,
  "app_web_framework": "remix",
  "app_web_frontend_any": true,
  "app_web_frontend_count": 1,
  "env_package_manager_workspaces": true,
  "partner_id": 3341693,
  "api_key": "****",
  "cmd_app_reset_used": false,
  "cmd_scaffold_template_flavor": "typescript",
  "cmd_scaffold_type": "cart_checkout_validation",
  "cmd_scaffold_used_prompts_for_type": true,
  "cmd_all_timing_network_ms": 4275,
  "cmd_all_timing_prompts_ms": 8549,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "app generate",
  "cmd_all_plugin": "@shopify/app",
  "cmd_all_verbose": true,
  "cmd_all_path_override": true,
  "cmd_all_path_override_hash": "c0ba6dc46deec8e1bc918c1dca1cca326c985e0d",
  "cmd_all_last_graphql_request_id": "66a73806-4127-4ded-affe-7264ac252b31-1752857985",
  "cmd_all_timing_active_ms": 421,
  "cmd_all_exit": "expected_error",
  "user_id": "5ad72b99-0689-473a-9a85-701d5a41bd8b",
  "request_ids": [
    "8836d5f8-223c-477a-bca9-1ae49b82d9af-1752857983",
    "1c5287df-17d7-4fe5-92bf-fd1d805759bf-1752857984",
    "66a73806-4127-4ded-affe-7264ac252b31-1752857985"
  ],
  "args": "--verbose",
  "error_message": "Command failed with exit code 1: npm exec -- graphql-code-generator --config package.json\n(node:4373) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.\n(Use `node --trace-deprecation ...` to show where the warning was created)\nCannot convert undefined or null to object\n\u001b[2m[11:59:56]\u001b[22m Parse configuration [started]\n\u001b[2m[11:59:56]\u001b[22m Parse configuration [failed]\n\u001b[2m[11:59:56]\u001b[22m → Cannot convert undefined or null to object",
  "app_name": "checkout",
  "env_plugin_installed_all": "[\"@shopify/cli\"]",
  "metadata": "{\"extraPublic\":{},\"extraSensitive\":{}}"
}
2025-07-18T16:59:57.295Z: Reporting handled error to Bugsnag: Command failed with exit code 1: npm exec -- graphql-code-generator --config package.json
(node:4373) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
(Use `node --trace-deprecation ...` to show where the warning was created)
Cannot convert undefined or null to object
[11:59:56] Parse configuration [started]
[11:59:56] Parse configuration [failed]
[11:59:56] → Cannot convert undefined or null to object
2025-07-18T16:59:57.391Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/kayluhb/Projects/checkout

2025-07-18T16:59:57.504Z: Obtaining the dependency manager in directory /Users/kayluhb/Projects/checkout...
```

comment #4 by kayluhb, 2025-07-19, 14:35:23
Just switched to `yarn` and it's working.

pnpm was working with a previous version.

comment #5 by mkupiniak, 2025-07-31, 20:27:37
I'm using `yarn` and it's not working, same error. 

Yarn 1.x.x, macOS, zsh, @shopify/cli/3.83.1 darwin-arm64 node-v22.17.0.

Edit: Worked when I created a new app and only then a new extension. It was not working with the old app.
