issue title: [Bug]: shopify app deploy fails with "Version couldn't be created" with theme and web pixel extension.
labels: Type: Bug
comment count: 6
hyperlink: https://github.com/shopify/cli/issues/6069
status: open
date opened: 2025-07-04
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Extension, Other

### Expected behavior

When an app has 2 extensions (theme & web pixel) "shopify app deploy" shall be able to deploy both extensions without issue.

### Actual behavior

When both extensions are present, the deployment process fails and no extension is deployed with:

```
 error │                                                                                                                                                                                                                                                  │
│  Version couldn't be created.                                                                                                                                                                                                                    │
│                                                                                                                                                                                                                                                  │
│  There was an error creating an app version.
```

No additional information is given why it failed. 

### Verbose output

<details>
  <summary>shopify app deploy --verbose</summary>

  ```
$ shopify app deploy --verbose
2025-07-04T11:44:36.981Z: Running command app deploy
2025-07-04T11:44:36.990Z: Running system process in background:
  · Command: /usr/bin/node /usr/bin/shopify notifications list --ignore-errors
  · Working directory: /home/myuser/bug-test

2025-07-04T11:44:37.007Z: Notifications to show: 0
2025-07-04T11:44:37.028Z: Reading cached app information for directory /home/myuser/bug-test...
2025-07-04T11:44:37.030Z: Reading the content of file at shopify.app.toml...
2025-07-04T11:44:37.035Z: Reading the content of file at shopify.app.toml...
2025-07-04T11:44:37.040Z: Reading cached app information for directory /home/myuser/bug-test...
2025-07-04T11:44:37.041Z: Reading the content of file at shopify.app.toml...
2025-07-04T11:44:37.043Z: Reading the content of file at shopify.app.toml...
2025-07-04T11:44:37.046Z: Ensuring that the user is authenticated with the Partners API with the following scopes:
[]

2025-07-04T11:44:37.046Z: Getting session store...
2025-07-04T11:44:37.048Z: Validating existing session against the scopes:
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

2025-07-04T11:44:37.049Z: - Token validation -> It's expired: false
2025-07-04T11:44:37.050Z: Getting partner account info from cache
2025-07-04T11:44:37.058Z: Sending "Partners" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T11:44:37.922Z: Request to https://partners.shopify.com/api/cli/graphql completed in 863 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"ba6dfbb3015e975fb871d6e7564c75d9"
 - server-timing: processing;dur=595, socket_queue;dur=2.842, util;dur=0.2, cfRequestDuration;dur=746.999979
 - x-request-id: xxxxxx-97b7-4e49-8fe8-29a5ceb806ef-1751629477

2025-07-04T11:44:37.930Z: Sending "Partners" GraphQL request:
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
  "id": "2368202"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T11:44:38.079Z: Sending "Partners" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T11:44:38.370Z: Request to https://partners.shopify.com/api/cli/graphql completed in 291 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"9af44f976738e1ba7550be4915afe001"
 - server-timing: processing;dur=72, socket_queue;dur=8.059, util;dur=0.4, cfRequestDuration;dur=236.999989
 - x-request-id: xxxxxxxx-53ed-4dca-bf0d-9a89ac116b36-1751629478

2025-07-04T11:44:38.391Z: The following extension specifications were defined locally but not found in the remote specifications: payments_extension, tax_calculation
2025-07-04T11:44:38.395Z: Reading the content of file at .gitignore...
2025-07-04T11:44:38.407Z: Reading the .env file at .env
2025-07-04T11:44:38.408Z: Reading the content of file at .env...
2025-07-04T11:44:38.420Z: Reading the content of file at extensions/theme-app-ext/shopify.extension.toml...
2025-07-04T11:44:38.421Z: Reading the content of file at extensions/web-p-ext/shopify.extension.toml...
2025-07-04T11:44:38.428Z: Reading the content of file at package.json...
2025-07-04T11:44:38.430Z: Reading the content of file at package.json...
2025-07-04T11:44:38.443Z: Running system process:
  · Command: npm prefix
  · Working directory: /home/myuser/bug-test

2025-07-04T11:44:38.632Z: Obtaining the dependency manager in directory /home/myuser/bug-test...
2025-07-04T11:44:38.633Z: Reading the content of file at package.json...
2025-07-04T11:44:38.634Z: Reading the content of file at .shopify/project.json...
2025-07-04T11:44:38.641Z: Reading the content of file at shopify.web.toml...
2025-07-04T11:44:38.645Z: Notifications to show: 0
2025-07-04T11:44:38.648Z: Reading cached app information for directory /home/myuser/bug-test...
2025-07-04T11:44:38.648Z: Storing app information for directory /home/myuser/bug-test:{
  "appId": "26adaee2c9c36a5c0313c5af0cfd0c3a",
  "title": "bug-test",
  "directory": "/home/myuser/bug-test",
  "orgId": "2368202"
}
2025-07-04T11:44:38.657Z: Sending "Partners" GraphQL request:
  query activeAppVersion($apiKey: String!) {
    app(apiKey: $apiKey) {
      activeAppVersion {
        appModuleVersions {
          registrationId
          registrationUuid
          registrationTitle
          type
          config
          specification {
            identifier
            name
            experience
            options {
              managementExperience
            }
          }
        }
      }
    }
  }

With variables:
{
  "apiKey": "*****"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T11:44:39.247Z: Request to https://partners.shopify.com/api/cli/graphql completed in 590 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"80a5665d8a9f6c6b94b695323bb8116d"
 - server-timing: processing;dur=379, socket_queue;dur=2.442, util;dur=0.1, cfRequestDuration;dur=555.999756
 - x-request-id: xxxxxxx-2de0-4073-8ff3-1194a1bca513-1751629478

╭─ info ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                                                                                                  │
│  Using .env for default values:                                                                                                                                                                                                                  │
│                                                                                                                                                                                                                                                  │
│    • Org:             classified                                                                                                                                                                                                    │
│    • App:             bug-test                                                                                                                                                                                                                    │
│    • Include config:  Yes                                                                                                                                                                                                                        │
│                                                                                                                                                                                                                                                  │
│   You can pass `--reset` to your command to reset your app configuration.                                                                                                                                                                        │
│                                                                                                                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-07-04T11:44:39.367Z: Sending "Partners" GraphQL request:
  query allAppExtensionRegistrations($apiKey: String!) {
    app(apiKey: $apiKey) {
      extensionRegistrations {
        id
        uuid
        title
        type
        draftVersion {
          config
          context
        }
        activeVersion {
          config
          context
        }
      }
      configurationRegistrations {
        id
        uuid
        title
        type
        draftVersion {
          config
          context
        }
        activeVersion {
          config
          context
        }
      }
      dashboardManagedExtensionRegistrations {
        id
        uuid
        title
        type
        activeVersion {
          config
          context
        }
        draftVersion {
          config
          context
        }
      }
    }
  }

With variables:
{
  "apiKey": "*****"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T11:44:41.156Z: Request to https://partners.shopify.com/api/cli/graphql completed in 1785 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"88bc238b91ede114493955696329911f"
 - server-timing: processing;dur=1608, socket_queue;dur=7.518, util;dur=0.5, cfRequestDuration;dur=1759.999990
 - x-request-id: xxxxxxx-ec3d-4cd7-a82a-1f9ff6768e6c-1751629479

?  Release a new version of bug-test?
✔  Yes, release this new version

2025-07-04T11:44:42.971Z: Sending "Partners" GraphQL request:
  mutation ExtensionCreate(
    $apiKey: String!
    $type: ExtensionType!
    $title: String!
    $config: JSON!
    $context: String
    $handle: String
  ) {
    extensionCreate(
      input: {apiKey: $apiKey, type: $type, title: $title, config: $config, context: $context, handle: $handle}
    ) {
      extensionRegistration {
        id
        uuid
        type
        title
        draftVersion {
          config
          registrationId
          lastUserInteractionAt
          validationErrors {
            field
            message
          }
        }
      }
      userErrors {
        field
        message
      }
    }
  }

With variables:
{
  "apiKey": "*****",
  "type": "WEBHOOK_SUBSCRIPTION",
  "title": "xxxxxxxx7ac513f42a23183acf8fae610f56f29e",
  "config": "{}",
  "context": "",
  "handle": "xxxxxxxxc513f42a23183acf8fae610f56f29e"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T11:44:43.355Z: Request to https://partners.shopify.com/api/cli/graphql completed in 383 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"f815e5e1a17759a0e820345aae7269d0"
 - server-timing: processing;dur=191, socket_queue;dur=4.682, util;dur=0.5, cfRequestDuration;dur=355.999947
 - x-request-id: xxxxxxxxx-79a5-4c8d-9bcc-0845f27b9ed4-1751629482

2025-07-04T11:44:43.361Z: Sending "Partners" GraphQL request:
  mutation ExtensionCreate(
    $apiKey: String!
    $type: ExtensionType!
    $title: String!
    $config: JSON!
    $context: String
    $handle: String
  ) {
    extensionCreate(
      input: {apiKey: $apiKey, type: $type, title: $title, config: $config, context: $context, handle: $handle}
    ) {
      extensionRegistration {
        id
        uuid
        type
        title
        draftVersion {
          config
          registrationId
          lastUserInteractionAt
          validationErrors {
            field
            message
          }
        }
      }
      userErrors {
        field
        message
      }
    }
  }

With variables:
{
  "apiKey": "*****",
  "type": "WEBHOOK_SUBSCRIPTION",
  "title": "xxxxxxxxxx6cc0eb5164b8e4d2301cbf",
  "config": "{}",
  "context": "",
  "handle": "xxxxxxxxb5a6cc0eb5164b8e4d2301cbf"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T11:44:43.708Z: Request to https://partners.shopify.com/api/cli/graphql completed in 347 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"9a9fb180acefcba275db9273ceb74708"
 - server-timing: processing;dur=186, socket_queue;dur=2.678, util;dur=0.5, cfRequestDuration;dur=326.999903
 - x-request-id: xxxxxxxx-0ee7-4c45-ada2-7232c111ccd9-1751629483


Releasing a new app version as part of bug-test

2025-07-04T11:44:43.711Z: Creating directory at .shopify...
2025-07-04T11:44:43.715Z: Removing directory at .shopify/deploy-bundle...
2025-07-04T11:44:43.722Z: Creating directory at .shopify/deploy-bundle...
2025-07-04T11:44:43.733Z: Deduplicating React dependency for /home/myuser/bug-test/extensions/web-p-ext, using /home/myuser/bug-test/node_modules/react/index.js
            theme-app-ext │ Running theme check on your Theme app extension...
                web-p-ext │ Bundling UI extension web-p-ext...

                web-p-ext │ web-p-ext successfully built
            theme-app-ext │
            theme-app-ext │ Bundling theme extension theme-app-ext...

2025-07-04T11:44:43.978Z: Copying file from extensions/theme-app-ext/assets/thumbs-up.png to .shopify/deploy-bundle/2b95a90e-b7da-4df7-9318-ebb65a75b47f/assets/thumbs-up.png...
2025-07-04T11:44:43.978Z: Copying file from extensions/theme-app-ext/blocks/star_rating.liquid to .shopify/deploy-bundle/2b95a90e-b7da-4df7-9318-ebb65a75b47f/blocks/star_rating.liquid...
2025-07-04T11:44:43.979Z: Copying file from extensions/theme-app-ext/locales/en.default.json to .shopify/deploy-bundle/2b95a90e-b7da-4df7-9318-ebb65a75b47f/locales/en.default.json...
2025-07-04T11:44:43.979Z: Copying file from extensions/theme-app-ext/snippets/stars.liquid to .shopify/deploy-bundle/2b95a90e-b7da-4df7-9318-ebb65a75b47f/snippets/stars.liquid...
2025-07-04T11:44:43.984Z: Zipping .shopify/deploy-bundle into .shopify/deploy-bundle.zip
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Running validation ...
2025-07-04T11:44:44.039Z: Getting the size of file file at extensions/theme-app-ext/assets/thumbs-up.png...
2025-07-04T11:44:44.039Z: Getting the size of file file at extensions/theme-app-ext/locales/en.default.json...
2025-07-04T11:44:44.039Z: Getting the size of file file at extensions/theme-app-ext/snippets/stars.liquid...
2025-07-04T11:44:44.040Z: Getting the size of file file at extensions/theme-app-ext/blocks/star_rating.liquid...
2025-07-04T11:44:44.041Z: Sending "Partners" GraphQL request:
  mutation GenerateSignedUploadUrl($apiKey: String!, $bundleFormat: Int!) {
    appVersionGenerateSignedUploadUrl(input: {apiKey: $apiKey, bundleFormat: $bundleFormat}) {
      signedUploadUrl
      userErrors {
        field
        message
      }
    }
  }

With variables:
{
  "apiKey": "*****",
  "bundleFormat": 1
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Releasing an app version ...
2025-07-04T11:44:44.407Z: Request to https://partners.shopify.com/api/cli/graphql completed in 366 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"5e850d3a533c8486ce873e6f8de26ef3"
 - server-timing: processing;dur=193, socket_queue;dur=2.566, util;dur=0.8, cfRequestDuration;dur=338.000059
 - x-request-id: xxxxxxxx-813e-4c27-8b7b-ea1e57d3363c-1751629484
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Releasing an app version ...
2025-07-04T11:44:44.625Z: Request to https://partners-extensions-scripts-bucket.storage.googleapis.com/deployments/264960540673/e2f657ec-10c1-42fa-a9ca-4056d4c2818c/bundle.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=argo-project-sa%40shopify-tiers.iam.gserviceaccount.com%2F20250704%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250704T114444Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=7e93c8bb65c2ebbe29f70b70ec4a325a460d8b5f0bf9e48743d25ce3a1e7aa834c5231452219769b224a11cc75747e07540072e65a7c9b3efc68f4b8c2d99139555b3123810d68af1435b6e1cfb578d458f82fb94763008d9d8657e2ed95e04e8dde71b2ddb6c79c7bc36ef1414e1e003377ae3498a189eb31c1a4385d7bf058fdf0e6cf3b9c60a7d13a8bfdd4f4157581cf544f1535c8c194d69c92c6dd3910c80ba0687c943ba5987905f5081f83bafc623492b34e9c01a2705b90905fc074e236e03b5db5434f3b3406e5898a8062300544963152cc0a624201a2d1e588dc916f3819d322fedd8287cc1e5bfd8cb88ce158b40748462a12a963fa41d1737b completed in 214 ms
With response headers:
 - content-type: application/xml; charset=UTF-8

2025-07-04T11:44:44.632Z: Sending "Partners" GraphQL request:
  mutation AppDeploy(
    $apiKey: String!
    $bundleUrl: String
    $appModules: [AppModuleSettings!]
    $skipPublish: Boolean
    $message: String
    $versionTag: String
    $commitReference: String
  ) {
    appDeploy(
      input: {
        apiKey: $apiKey
        bundleUrl: $bundleUrl
        appModules: $appModules
        skipPublish: $skipPublish
        message: $message
        versionTag: $versionTag
        commitReference: $commitReference
      }
    ) {
      appVersion {
        uuid
        id
        message
        versionTag
        location
        appModuleVersions {
          uuid
          registrationUuid
          validationErrors {
            message
            field
          }
        }
      }
      userErrors {
        message
        field
        category
        details
      }
    }
  }

With variables:
{
  "appId": "264960540673",
  "apiKey": "*****",
  "name": "bug-test",
  "skipPublish": false,
  "bundleUrl": "https://partners-extensions-scripts-bucket.storage.googleapis.com/deployments/264960540673/e2f657ec-10c1-42fa-a9ca-4056d4c2818c/bundle.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=argo-project-sa%40shopify-tiers.iam.gserviceaccount.com%2F20250704%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250704T114444Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=7e93c8bb65c2ebbe29f70b70ec4a325a460d8b5f0bf9e48743d25ce3a1e7aa834c5231452219769b224a11cc75747e07540072e65a7c9b3efc68f4b8c2d99139555b3123810d68af1435b6e1cfb578d458f82fb94763008d9d8657e2ed95e04e8dde71b2ddb6c79c7bc36ef1414e1e003377ae3498a189eb31c1a4385d7bf058fdf0e6cf3b9c60a7d13a8bfdd4f4157581cf544f1535c8c194d69c92c6dd3910c80ba0687c943ba5987905f5081f83bafc623492b34e9c01a2705b90905fc074e236e03b5db5434f3b3406e5898a8062300544963152cc0a624201a2d1e588dc916f3819d322fedd8287cc1e5bfd8cb88ce158b40748462a12a963fa41d1737b",
  "appModules": [
    {
      "config": "{\"theme_extension\":{\"files\":{}}}",
      "context": "",
      "handle": "theme-app-ext",
      "uuid": "2b95a90e-b7da-4df7-9318-ebb65a75b47f",
      "specificationIdentifier": "THEME_APP_EXTENSION"
    },
    {
      "config": "{\"runtime_context\":\"strict\",\"runtime_configuration_definition\":{\"type\":\"object\",\"fields\":{\"accountID\":{\"name\":\"Account ID\",\"description\":\"Account ID\",\"type\":\"single_line_text_field\",\"validations\":[{\"name\":\"min\",\"value\":\"1\"}]}}}}",
      "context": "",
      "handle": "web-p-ext",
      "uuid": "48b47d41-140d-4821-8641-923adc7c187f",
      "specificationIdentifier": "WEB_PIXEL_EXTENSION"
    },
    {
      "config": "{\"scopes\":\"write_products\",\"redirect_url_allowlist\":[\"https://example.com/api/auth\"]}",
      "context": "",
      "handle": "app_access",
      "uuid": "7ee6b952-60d2-470d-9cc1-f42ed24450b2",
      "specificationIdentifier": "APP_ACCESS"
    },
    {
      "config": "{\"api_version\":\"2025-07\"}",
      "context": "",
      "handle": "webhooks",
      "uuid": "f7783a3e-00aa-4100-95e6-883bf62ee00d",
      "specificationIdentifier": "WEBHOOKS"
    },
    {
      "config": "{\"embedded\":false}",
      "context": "",
      "handle": "point_of_sale",
      "uuid": "002ddb53-bff7-4275-bcb0-a814b9bed25f",
      "specificationIdentifier": "POINT_OF_SALE"
    },
    {
      "config": "{\"app_url\":\"https://example.com/\",\"embedded\":true}",
      "context": "",
      "handle": "app_home",
      "uuid": "3c21d600-ff88-44d6-b5fd-1b25bea70ea0",
      "specificationIdentifier": "APP_HOME"
    },
    {
      "config": "{\"name\":\"bug-test\",\"app_handle\":\"bug-test-8\"}",
      "context": "",
      "handle": "branding",
      "uuid": "93e68960-a8c6-44cb-bd8a-d64b0653f8c0",
      "specificationIdentifier": "BRANDING"
    },
    {
      "config": "{\"topic\":\"app/scopes_update\",\"api_version\":\"2025-07\",\"uri\":\"https://example.com/webhooks/app/scopes_update\"}",
      "context": "",
      "handle": "4103dafc7ac513f42a23183acf8fae610f56f29e",
      "uuid": "511610d9-f45c-4da8-83dc-15ccc09a41cd",
      "specificationIdentifier": "WEBHOOK_SUBSCRIPTION"
    },
    {
      "config": "{\"topic\":\"app/uninstalled\",\"api_version\":\"2025-07\",\"uri\":\"https://example.com/webhooks/app/uninstalled\"}",
      "context": "",
      "handle": "09711dbb6e24902b5a6cc0eb5164b8e4d2301cbf",
      "uuid": "d96a7a1f-f4be-4c73-acef-a70352f9e2a7",
      "specificationIdentifier": "WEBHOOK_SUBSCRIPTION"
    }
  ]
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Releasing an app version ...
2025-07-04T11:44:45.367Z: Request to https://partners.shopify.com/api/cli/graphql completed in 735 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"00bbbb03539261b6d393e15ea76e07e5"
 - server-timing: processing;dur=553, socket_queue;dur=6.657, util;dur=0.7, cfRequestDuration;dur=710.000038

╭─ error ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                                                                                                  │
│  Version couldn't be created.                                                                                                                                                                                                                    │
│                                                                                                                                                                                                                                                  │
│  There was an error creating an app version.                                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-07-04T11:44:45.389Z: Running system process:
  · Command: npm prefix
  · Working directory: /home/myuser/bug-test

2025-07-04T11:44:45.544Z: Obtaining the dependency manager in directory /home/myuser/bug-test...
2025-07-04T11:44:45.876Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 165 ms
With response headers:
 - x-request-id: xxxxxxxx-f90d-4b01-ada6-69105b3955a0

2025-07-04T11:44:45.877Z: Analytics event sent: {
  "command": "app deploy",
  "time_start": 1751629476982,
  "time_end": 1751629485379,
  "total_time": 8397,
  "success": false,
  "cli_version": "3.82.0",
  "ruby_version": "",
  "node_version": "22.17.0",
  "is_employee": false,
  "uname": "linux arm64",
  "env_ci": false,
  "env_plugin_installed_any_custom": false,
  "env_plugin_installed_shopify": "[\"@shopify/cli\"]",
  "env_shell": "bash",
  "env_device_id": "53bcf023a3375353d8022460c25252b236ed180d",
  "env_cloud": "localhost",
  "env_package_manager": "npm",
  "env_is_global": true,
  "env_auth_method": "device_auth",
  "env_is_wsl": false,
  "cmd_app_warning_api_key_deprecation_displayed": false,
  "cmd_deploy_flag_message_used": false,
  "cmd_deploy_flag_version_used": false,
  "cmd_deploy_flag_source_url_used": false,
  "cmd_app_all_configs_any": true,
  "cmd_app_all_configs_clients": "{\"shopify.app.toml\":\"26adaee2c9c36a5c0313c5af0cfd0c3a\"}",
  "cmd_app_linked_config_used": true,
  "cmd_app_linked_config_name": "shopify.app.toml",
  "cmd_app_linked_config_git_tracked": true,
  "cmd_app_linked_config_source": "cached",
  "project_type": "node",
  "app_extensions_any": true,
  "app_extensions_breakdown": "{\"theme\":1,\"web_pixel_extension\":1}",
  "app_extensions_count": 2,
  "app_extensions_custom_layout": false,
  "app_extensions_function_any": false,
  "app_extensions_function_count": 0,
  "app_extensions_theme_any": true,
  "app_extensions_theme_count": 1,
  "app_extensions_ui_any": true,
  "app_extensions_ui_count": 1,
  "app_name_hash": "41c486b7750e760b358cf8ccd898ab193f996525",
  "app_path_hash": "d52936dec1a7922dc6ab66b3ff3c07163f3f9d9b",
  "app_scopes": "[\"write_products\"]",
  "app_web_backend_any": true,
  "app_web_backend_count": 1,
  "app_web_custom_layout": true,
  "app_web_framework": "remix",
  "app_web_frontend_any": true,
  "app_web_frontend_count": 1,
  "env_package_manager_workspaces": true,
  "partner_id": 2368202,
  "api_key": "****",
  "cmd_app_reset_used": false,
  "cmd_deploy_include_config_used": true,
  "cmd_deploy_config_modules_breakdown": "[\"access_scopes\",\"application_url\",\"auth\",\"embedded\",\"handle\",\"name\",\"pos\",\"webhooks\"]",
  "cmd_deploy_config_modules_updated": "[\"webhooks\"]",
  "cmd_deploy_confirm_new_registrations": 2,
  "cmd_deploy_confirm_updated_registrations": 0,
  "cmd_deploy_confirm_removed_registrations": 0,
  "cmd_deploy_confirm_cancelled": false,
  "cmd_deploy_confirm_time_to_complete_ms": 1795,
  "cmd_all_timing_network_ms": 5576,
  "cmd_all_timing_prompts_ms": 1793,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "app",
  "cmd_all_plugin": "@shopify/app",
  "cmd_all_force": false,
  "cmd_all_verbose": true,
  "cmd_all_path_override": true,
  "cmd_all_path_override_hash": "d52936dec1a7922dc6ab66b3ff3c07163f3f9d9b",
  "cmd_all_last_graphql_request_id": "799e0403-9fb9-4dab-9a58-1111aaea2233-1751629484",
  "cmd_all_timing_active_ms": 1026,
  "cmd_all_exit": "expected_error",
  "user_id": "360a61e1-48d3-4226-9b80-042ec08455cf",
  "request_ids": [
    "31ddc7dd-97b7-4e49-8fe8-29a5ceb806ef-1751629477",
    "c763f840-53ed-4dca-bf0d-9a89ac116b36-1751629478",
    "24a6cebd-2de0-4073-8ff3-1194a1bca513-1751629478",
    "f6ae6649-ec3d-4cd7-a82a-1f9ff6768e6c-1751629479",
    "86667b83-79a5-4c8d-9bcc-0845f27b9ed4-1751629482",
    "e52185ef-0ee7-4c45-ada2-7232c111ccd9-1751629483",
    "be03c12d-813e-4c27-8b7b-ea1e57d3363c-1751629484",
    "799e0403-9fb9-4dab-9a58-1111aaea2233-1751629484"
  ],
  "args": "--verbose",
  "error_message": "Version couldn't be created.",
  "app_name": "bug-test",
  "env_plugin_installed_all": "[\"@shopify/cli\"]",
  "metadata": "{\"extraPublic\":{},\"extraSensitive\":{}}"
}
2025-07-04T11:44:45.886Z: Reporting handled error to Bugsnag: Version couldn't be created.
2025-07-04T11:44:46.343Z: Running system process:
  · Command: npm prefix
  · Working directory: /home/myuser/bug-test

2025-07-04T11:44:46.505Z: Obtaining the dependency manager in directory ### /home/myuser/bug-test...
  ```

</details>

### Reproduction steps

1. create a new app: `shopify app init`
2. add a theme extension: `shopify app generate extension` -> select "Theme app extension" and add a name
3. add a web pixel extension: `shopify app generate extension` -> select "Web pixel" and add a name
4. run "shopify app deploy" 

### Operating System

Ubuntu 24.04.2 LTS (ARM)

### Shopify CLI version (`shopify --version`)

@shopify/cli/3.82.0 linux-arm64 node-v22.17.0

### Shell

bash

### Node version (run `node -v` if you're not sure)

v22.17.0

### What language and version are you using in your application?

Shopoify remix template with javascript

===

comment #1 by alexanderMontague, 2025-07-04, 15:11:18
Hi @themazim, I'm unfortunately not able to reproduce this error. Could you try one more time to rule out a flaky request and paste the verbose output again? Thanks!

comment #2 by themazim, 2025-07-04, 15:28:34
> Hi [@themazim](https://github.com/themazim), I'm unfortunately not able to reproduce this error. Could you try one more time to rule out a flaky request and paste the verbose output again? Thanks!

thanks for checking. I tested again with a clean app. Added theme and web pixel extension again and had the same issue again.

Then I tested further and removed the theme extension just to be sure, and it seems a single web pixel extension fails. So maybe it is just related to the web pixel only.

The issue is, I still do not get proper output why it fails. either way. here is the full output with proper request IDs:

<details>
  <summary>shopify app deploy --verbose</summary>

  ```
$ shopify app debug --verbose
2025-07-04T15:24:01.377Z: 'Did you mean' options: [{"score":5,"cmd":"app:dev"},{"score":5,"cmd":"app:deploy"},{"score":5,"cmd":"app:dev:clean"},{"score":5,"cmd":"hydrogen:debug:cpu"},{"score":4,"cmd":"app:build"},{"score":4,"cmd":"app:function:build"},{"score":4,"cmd":"app:webhook:trigger"},{"score":3,"cmd":"app:info"},{"score":3,"cmd":"app:init"},{"score":3,"cmd":"app:logs"},{"score":3,"cmd":"app:release"},{"score":3,"cmd":"app:env:pull"},{"score":3,"cmd":"app:env:show"},{"score":3,"cmd":"app:config:use"},{"score":3,"cmd":"app:config:link"},{"score":3,"cmd":"app:function:run"},{"score":3,"cmd":"app:logs:sources"},{"score":3,"cmd":"app:versions:list"},{"score":3,"cmd":"app:function:replay"},{"score":3,"cmd":"app:function:schema"},{"score":3,"cmd":"app:function:typegen"},{"score":3,"cmd":"app:import-extensions"},{"score":3,"cmd":"app:generate:extension"},{"score":2,"cmd":"theme:dev"},{"score":2,"cmd":"hydrogen:dev"},{"score":2,"cmd":"theme:delete"},{"score":2,"cmd":"hydrogen:deploy"}]
?  Command `app debug` not found. Did you mean `app dev`?

>  (y) Yes, confirm
   (n) No, cancel

   Press ↑↓ arrows to select, enter or a shortcut to confirm.

2025-07-04T15:24:04.258Z: Killing process 70924: ps -o pid command --no-headers --ppid 70911
forge@dev-better-bounce:~/debug-again$ shopify app deploy --verbose
2025-07-04T15:24:11.898Z: Running command app deploy
2025-07-04T15:24:11.909Z: Running system process in background:
  · Command: /usr/bin/node /usr/bin/shopify notifications list --ignore-errors
  · Working directory: /home/forge/debug-again

2025-07-04T15:24:11.934Z: Notifications to show: 0
2025-07-04T15:24:11.956Z: Reading cached app information for directory /home/forge/debug-again...
2025-07-04T15:24:11.957Z: Reading the content of file at shopify.app.toml...
2025-07-04T15:24:11.962Z: Reading the content of file at shopify.app.toml...
2025-07-04T15:24:11.966Z: Reading cached app information for directory /home/forge/debug-again...
2025-07-04T15:24:11.967Z: Reading the content of file at shopify.app.toml...
2025-07-04T15:24:11.969Z: Reading the content of file at shopify.app.toml...
2025-07-04T15:24:11.971Z: Ensuring that the user is authenticated with the Partners API with the following scopes:
[]

2025-07-04T15:24:11.972Z: Getting session store...
2025-07-04T15:24:11.974Z: Validating existing session against the scopes:
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

2025-07-04T15:24:11.974Z: - Token validation -> It's expired: false
2025-07-04T15:24:11.975Z: Getting partner account info from cache
2025-07-04T15:24:11.982Z: Sending "Partners" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T15:24:12.753Z: Request to https://partners.shopify.com/api/cli/graphql completed in 769 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"12055939e45cee8cbccfb35c462eb896"
 - server-timing: processing;dur=561, socket_queue;dur=2.225, util;dur=0.9, cfRequestDuration;dur=713.000059
 - x-request-id: 71e706f0-8c89-4546-958a-101dcde50cf1-1751642652

2025-07-04T15:24:12.759Z: Sending "Partners" GraphQL request:
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
  "id": "2368202"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T15:24:12.909Z: Sending "Partners" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T15:24:13.215Z: Request to https://partners.shopify.com/api/cli/graphql completed in 306 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"9af44f976738e1ba7550be4915afe001"
 - server-timing: processing;dur=101, socket_queue;dur=1.94, util;dur=0.4, cfRequestDuration;dur=256.999969
 - x-request-id: 4d03bee4-38d2-4117-a7d0-f22533443180-1751642652

2025-07-04T15:24:13.254Z: The following extension specifications were defined locally but not found in the remote specifications: payments_extension, tax_calculation
2025-07-04T15:24:13.267Z: Reading the content of file at .gitignore...
2025-07-04T15:24:13.271Z: Reading the .env file at .env
2025-07-04T15:24:13.275Z: Reading the content of file at .env...
2025-07-04T15:24:13.285Z: Reading the content of file at extensions/web-pixel-test/shopify.extension.toml...
2025-07-04T15:24:13.290Z: Reading the content of file at package.json...
2025-07-04T15:24:13.291Z: Reading the content of file at package.json...
2025-07-04T15:24:13.298Z: Running system process:
  · Command: npm prefix
  · Working directory: /home/forge/debug-again

2025-07-04T15:24:13.496Z: Obtaining the dependency manager in directory /home/forge/debug-again...
2025-07-04T15:24:13.497Z: Reading the content of file at package.json...
2025-07-04T15:24:13.498Z: Reading the content of file at .shopify/project.json...
2025-07-04T15:24:13.504Z: Reading the content of file at shopify.web.toml...
2025-07-04T15:24:13.508Z: Notifications to show: 0
2025-07-04T15:24:13.511Z: Reading cached app information for directory /home/forge/debug-again...
2025-07-04T15:24:13.512Z: Storing app information for directory /home/forge/debug-again:{
  "appId": "db9f2123734eefc362fb7b3e5c6238db",
  "title": "debug-again",
  "directory": "/home/forge/debug-again",
  "orgId": "2368202"
}
2025-07-04T15:24:13.521Z: Sending "Partners" GraphQL request:
  query activeAppVersion($apiKey: String!) {
    app(apiKey: $apiKey) {
      activeAppVersion {
        appModuleVersions {
          registrationId
          registrationUuid
          registrationTitle
          type
          config
          specification {
            identifier
            name
            experience
            options {
              managementExperience
            }
          }
        }
      }
    }
  }

With variables:
{
  "apiKey": "*****"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T15:24:14.099Z: Request to https://partners.shopify.com/api/cli/graphql completed in 578 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"f71f905e5168288aa8e95c03a3a9cf74"
 - server-timing: processing;dur=394, socket_queue;dur=1.786, util;dur=0.9, cfRequestDuration;dur=543.999910
 - x-request-id: 2805bd40-77f5-4266-8738-e3532ec9e0eb-1751642653

╭─ info ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                  │
│  Using .env for default values:                                                                                                  │
│                                                                                                                                  │
│    • Org:             Gravity Technologies AG                                                                                    │
│    • App:             debug-again                                                                                                │
│    • Include config:  Yes                                                                                                        │
│                                                                                                                                  │
│   You can pass `--reset` to your command to reset your app configuration.                                                        │
│                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-07-04T15:24:14.267Z: Sending "Partners" GraphQL request:
  query allAppExtensionRegistrations($apiKey: String!) {
    app(apiKey: $apiKey) {
      extensionRegistrations {
        id
        uuid
        title
        type
        draftVersion {
          config
          context
        }
        activeVersion {
          config
          context
        }
      }
      configurationRegistrations {
        id
        uuid
        title
        type
        draftVersion {
          config
          context
        }
        activeVersion {
          config
          context
        }
      }
      dashboardManagedExtensionRegistrations {
        id
        uuid
        title
        type
        activeVersion {
          config
          context
        }
        draftVersion {
          config
          context
        }
      }
    }
  }

With variables:
{
  "apiKey": "*****"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-07-04T15:24:15.947Z: Request to https://partners.shopify.com/api/cli/graphql completed in 1679 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"93791941eaf58e46d851dbeb699715f3"
 - server-timing: processing;dur=1488, socket_queue;dur=6.106, util;dur=0.2, cfRequestDuration;dur=1657.999992
 - x-request-id: e933675a-ef56-4489-978c-a2ff7cec4535-1751642654

?  Release a new version of debug-again?
✔  Confirmed


Releasing a new app version as part of debug-again

2025-07-04T15:24:19.654Z: Creating directory at .shopify...
2025-07-04T15:24:19.658Z: Removing directory at .shopify/deploy-bundle...
2025-07-04T15:24:19.664Z: Creating directory at .shopify/deploy-bundle...
2025-07-04T15:24:19.673Z: Deduplicating React dependency for /home/forge/debug-again/extensions/web-pixel-test, using /home/forge/debug-again/node_modules/react/index.js
           web-pixel-test │ Bundling UI extension web-pixel-test...

           web-pixel-test │ web-pixel-test successfully built

2025-07-04T15:24:19.706Z: Zipping .shopify/deploy-bundle into .shopify/deploy-bundle.zip
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Running validation ...
2025-07-04T15:24:19.744Z: Sending "Partners" GraphQL request:
  mutation GenerateSignedUploadUrl($apiKey: String!, $bundleFormat: Int!) {
    appVersionGenerateSignedUploadUrl(input: {apiKey: $apiKey, bundleFormat: $bundleFormat}) {
      signedUploadUrl
      userErrors {
        field
        message
      }
    }
  }

With variables:
{
  "apiKey": "*****",
  "bundleFormat": 1
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Releasing an app version ...
2025-07-04T15:24:20.090Z: Request to https://partners.shopify.com/api/cli/graphql completed in 346 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"d999002f823de3b3d914803998ec70ef"
 - server-timing: processing;dur=179, socket_queue;dur=2.571, util;dur=0.5, cfRequestDuration;dur=322.999954
 - x-request-id: 04769992-e55c-4d73-bbe2-0e6e861a1096-1751642659
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Releasing an app version ...
2025-07-04T15:24:20.253Z: Request to https://partners-extensions-scripts-bucket.storage.googleapis.com/deployments/265009561601/aaf2fe6c-7cb9-4cb3-9259-1614aa4047f6/bundle.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=argo-project-sa%40shopify-tiers.iam.gserviceaccount.com%2F20250704%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250704T152419Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=2af5026021b77f2a845ce7ef0cb94812bd550b9f641e65215160123cddc75078e538110e7b818f45fbc670f0cbfffbb908f913ea5615eff06767405edbac231dc397359008ed3f5a1cac43d401e543a726aa2451d4b399a1a2d6f3df9e4d59c2e40f15a3b8d9f3f5417c04423277d70c303f9b61a53f8fe74a959201927c7a739aebf68f9981c5541e6d74c8caf96bd23b6edc552fc86a2e1a523e7e23ca808e4d16462e3fe1e0127f4027a4835bd313c2dde277c491751a5a0364a2a6e7e381f623aef33e8a352a600dba7934e4031bf0824892c9e81b18fa3f856e50e039a849beeca88ddd248d061da8a7f31298736e461f17dd545e7a199375185634d77b completed in 159 ms
With response headers:
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Releasing an app version ...
2025-07-04T15:24:20.261Z: Sending "Partners" GraphQL request:
  mutation AppDeploy(
    $apiKey: String!
    $bundleUrl: String
    $appModules: [AppModuleSettings!]
    $skipPublish: Boolean
    $message: String
    $versionTag: String
    $commitReference: String
  ) {
    appDeploy(
      input: {
        apiKey: $apiKey
        bundleUrl: $bundleUrl
        appModules: $appModules
        skipPublish: $skipPublish
        message: $message
        versionTag: $versionTag
        commitReference: $commitReference
      }
    ) {
      appVersion {
        uuid
        id
        message
        versionTag
        location
        appModuleVersions {
          uuid
          registrationUuid
          validationErrors {
            message
            field
          }
        }
      }
      userErrors {
        message
        field
        category
        details
      }
    }
  }

With variables:
{
  "appId": "265009561601",
  "apiKey": "*****",
  "name": "debug-again",
  "skipPublish": false,
  "bundleUrl": "https://partners-extensions-scripts-bucket.storage.googleapis.com/deployments/265009561601/aaf2fe6c-7cb9-4cb3-9259-1614aa4047f6/bundle.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=argo-project-sa%40shopify-tiers.iam.gserviceaccount.com%2F20250704%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250704T152419Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=2af5026021b77f2a845ce7ef0cb94812bd550b9f641e65215160123cddc75078e538110e7b818f45fbc670f0cbfffbb908f913ea5615eff06767405edbac231dc397359008ed3f5a1cac43d401e543a726aa2451d4b399a1a2d6f3df9e4d59c2e40f15a3b8d9f3f5417c04423277d70c303f9b61a53f8fe74a959201927c7a739aebf68f9981c5541e6d74c8caf96bd23b6edc552fc86a2e1a523e7e23ca808e4d16462e3fe1e0127f4027a4835bd313c2dde277c491751a5a0364a2a6e7e381f623aef33e8a352a600dba7934e4031bf0824892c9e81b18fa3f856e50e039a849beeca88ddd248d061da8a7f31298736e461f17dd545e7a199375185634d77b",
  "appModules": [
    {
      "config": "{\"runtime_context\":\"strict\",\"runtime_configuration_definition\":{\"type\":\"object\",\"fields\":{\"accountID\":{\"name\":\"Account ID\",\"description\":\"Account ID\",\"type\":\"single_line_text_field\",\"validations\":[{\"name\":\"min\",\"value\":\"1\"}]}}}}",
      "context": "",
      "handle": "web-pixel-test",
      "uuid": "e2a24c0d-9e2e-44ec-aded-f89ed2054514",
      "specificationIdentifier": "WEB_PIXEL_EXTENSION"
    },
    {
      "config": "{\"scopes\":\"write_products\",\"redirect_url_allowlist\":[\"https://example.com/api/auth\"]}",
      "context": "",
      "handle": "app_access",
      "uuid": "74af65af-611b-4ad5-a506-eb05899619a2",
      "specificationIdentifier": "APP_ACCESS"
    },
    {
      "config": "{\"api_version\":\"2025-07\"}",
      "context": "",
      "handle": "webhooks",
      "uuid": "b148fc20-eaf0-4c5f-8550-e55c74d2ceb0",
      "specificationIdentifier": "WEBHOOKS"
    },
    {
      "config": "{\"embedded\":false}",
      "context": "",
      "handle": "point_of_sale",
      "uuid": "f37c5c2c-f2d7-48f0-b2a6-5fb9d00b6d85",
      "specificationIdentifier": "POINT_OF_SALE"
    },
    {
      "config": "{\"app_url\":\"https://example.com/\",\"embedded\":true}",
      "context": "",
      "handle": "app_home",
      "uuid": "770d6edf-f1f8-4c4d-97d9-3d26861b1b1c",
      "specificationIdentifier": "APP_HOME"
    },
    {
      "config": "{\"name\":\"debug-again\",\"app_handle\":\"debug-again\"}",
      "context": "",
      "handle": "branding",
      "uuid": "4f5ea8f1-4301-455b-828c-6f71387988bc",
      "specificationIdentifier": "BRANDING"
    },
    {
      "config": "{\"topic\":\"app/scopes_update\",\"api_version\":\"2025-07\",\"uri\":\"https://example.com/webhooks/app/scopes_update\"}",
      "context": "",
      "handle": "4103dafc7ac513f42a23183acf8fae610f56f29e",
      "uuid": "7575a075-820a-415a-978d-f803c811a4ee",
      "specificationIdentifier": "WEBHOOK_SUBSCRIPTION"
    },
    {
      "config": "{\"topic\":\"app/uninstalled\",\"api_version\":\"2025-07\",\"uri\":\"https://example.com/webhooks/app/uninstalled\"}",
      "context": "",
      "handle": "09711dbb6e24902b5a6cc0eb5164b8e4d2301cbf",
      "uuid": "052bf8bb-07de-4c93-a848-06cb39e4f8bf",
      "specificationIdentifier": "WEBHOOK_SUBSCRIPTION"
    }
  ]
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Releasing an app version ...
2025-07-04T15:24:20.933Z: Request to https://partners.shopify.com/api/cli/graphql completed in 672 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"00bbbb03539261b6d393e15ea76e07e5"
 - server-timing: processing;dur=515, socket_queue;dur=3.444, util;dur=0.8, cfRequestDuration;dur=656.000137

╭─ error ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                  │
│  Version couldn't be created.                                                                                                    │
│                                                                                                                                  │
│  There was an error creating an app version.                                                                                     │
│                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-07-04T15:24:20.955Z: Running system process:
  · Command: npm prefix
  · Working directory: /home/forge/debug-again

2025-07-04T15:24:21.111Z: Obtaining the dependency manager in directory /home/forge/debug-again...
2025-07-04T15:24:21.476Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 186 ms
With response headers:
 - x-request-id: 4ae068d9-d0a7-4bbd-8da1-60a458b4fa99

2025-07-04T15:24:21.477Z: Analytics event sent: {
  "command": "app deploy",
  "time_start": 1751642651898,
  "time_end": 1751642660944,
  "total_time": 9046,
  "success": false,
  "cli_version": "3.82.0",
  "ruby_version": "",
  "node_version": "22.17.0",
  "is_employee": false,
  "uname": "linux arm64",
  "env_ci": false,
  "env_plugin_installed_any_custom": false,
  "env_plugin_installed_shopify": "[\"@shopify/cli\"]",
  "env_shell": "bash",
  "env_device_id": "53bcf023a3375353d8022460c25252b236ed180d",
  "env_cloud": "localhost",
  "env_package_manager": "npm",
  "env_is_global": true,
  "env_auth_method": "device_auth",
  "env_is_wsl": false,
  "cmd_app_warning_api_key_deprecation_displayed": false,
  "cmd_deploy_flag_message_used": false,
  "cmd_deploy_flag_version_used": false,
  "cmd_deploy_flag_source_url_used": false,
  "cmd_app_all_configs_any": true,
  "cmd_app_all_configs_clients": "{\"shopify.app.toml\":\"db9f2123734eefc362fb7b3e5c6238db\"}",
  "cmd_app_linked_config_used": true,
  "cmd_app_linked_config_name": "shopify.app.toml",
  "cmd_app_linked_config_git_tracked": true,
  "cmd_app_linked_config_source": "cached",
  "project_type": "node",
  "app_extensions_any": true,
  "app_extensions_breakdown": "{\"web_pixel_extension\":1}",
  "app_extensions_count": 1,
  "app_extensions_custom_layout": false,
  "app_extensions_function_any": false,
  "app_extensions_function_count": 0,
  "app_extensions_theme_any": false,
  "app_extensions_theme_count": 0,
  "app_extensions_ui_any": true,
  "app_extensions_ui_count": 1,
  "app_name_hash": "9e0310934265919f2bc8727cb4e2d3bd310d94c4",
  "app_path_hash": "263ca8efcb8b541587e731836703a8e57c63732d",
  "app_scopes": "[\"write_products\"]",
  "app_web_backend_any": true,
  "app_web_backend_count": 1,
  "app_web_custom_layout": true,
  "app_web_framework": "remix",
  "app_web_frontend_any": true,
  "app_web_frontend_count": 1,
  "env_package_manager_workspaces": true,
  "partner_id": 2368202,
  "api_key": "****",
  "cmd_app_reset_used": false,
  "cmd_deploy_include_config_used": true,
  "cmd_deploy_config_modules_breakdown": "[\"access_scopes\",\"application_url\",\"auth\",\"embedded\",\"handle\",\"name\",\"pos\",\"webhooks\"]",
  "cmd_deploy_confirm_new_registrations": 1,
  "cmd_deploy_confirm_updated_registrations": 0,
  "cmd_deploy_confirm_removed_registrations": 1,
  "cmd_deploy_confirm_cancelled": false,
  "cmd_deploy_confirm_time_to_complete_ms": 3692,
  "cmd_all_timing_network_ms": 4512,
  "cmd_all_timing_prompts_ms": 3691,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "app",
  "cmd_all_plugin": "@shopify/app",
  "cmd_all_force": false,
  "cmd_all_verbose": true,
  "cmd_all_path_override": true,
  "cmd_all_path_override_hash": "263ca8efcb8b541587e731836703a8e57c63732d",
  "cmd_all_last_graphql_request_id": "943cdc4c-bd6c-407e-9c5d-0160a991140b-1751642660",
  "cmd_all_timing_active_ms": 841,
  "cmd_all_exit": "expected_error",
  "user_id": "360a61e1-48d3-4226-9b80-042ec08455cf",
  "request_ids": [
    "71e706f0-8c89-4546-958a-101dcde50cf1-1751642652",
    "4d03bee4-38d2-4117-a7d0-f22533443180-1751642652",
    "2805bd40-77f5-4266-8738-e3532ec9e0eb-1751642653",
    "e933675a-ef56-4489-978c-a2ff7cec4535-1751642654",
    "04769992-e55c-4d73-bbe2-0e6e861a1096-1751642659",
    "943cdc4c-bd6c-407e-9c5d-0160a991140b-1751642660"
  ],
  "args": "--verbose",
  "error_message": "Version couldn't be created.",
  "app_name": "debug-again",
  "env_plugin_installed_all": "[\"@shopify/cli\"]",
  "metadata": "{\"extraPublic\":{},\"extraSensitive\":{}}"
}
2025-07-04T15:24:21.487Z: Reporting handled error to Bugsnag: Version couldn't be created.
2025-07-04T15:24:21.971Z: Running system process:
  · Command: npm prefix
  · Working directory: /home/forge/debug-again

2025-07-04T15:24:22.126Z: Obtaining the dependency manager in directory /home/forge/debug-again...

  ```

</details>

edit:

I tested this once again with another machine (@shopify/cli/3.81.2 darwin-arm64 node-v22.14.0) and there the issue does not exist. also updated to latest version too (@shopify/cli/3.82.0 darwin-arm64 node-v22.14.0) still no issue here. 



comment #3 by themazim, 2025-07-04, 20:22:38
I tried to replicate the issue on an x64 server with the exact same setup. no issue there. was able to deploy the extensions there. 

Not sure if it is actual an issue with ubuntu 24 on ARM or a hiccup with the setup.  Either way. hope this info helps.

comment #4 by themazim, 2025-07-07, 19:25:22
I just ran into the issue again, but this time on a x64 server, so this is not related to ARM. 

I basically pulled and app and tried to setup (relink it) a staging env. 

comment #5 by themazim, 2025-07-08, 21:23:26
Some more information, it seems this issue happens usually if a app re-linked by using: `shopify app config link`


Afterwards every try to deploy an extension ends in the mentioned error.


comment #6 by isaacroldan, 2025-07-10, 11:10:54
I wasn't able to reproduce either, tried to follow the same steps (deploying after a `config link`), but it works fine for me 🤔 

Looking at the logs I think it could be related to the upload of the extension built files, if they are not uploaded correctly to GCS, then the version creation will fail. 

Do you have some full reproduction steps I can follow? from app creation to deploy i mean. 
