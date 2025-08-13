issue title: [Bug]: Version couldn't be created
labels: Type: Bug, Area: @shopify/app
comment count: 3
hyperlink: https://github.com/shopify/cli/issues/6210
status: closed
date opened: 2025-08-05
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

App

### Expected behavior

Creating a new version was working fine a few days ago, just changed the URLs to route traffic from dev to local environment

### Actual behavior

While running `shopify app deploy` got the below error

Version couldn't be created.  
Following payment methods not permitted: ["naps"]  

### Verbose output

<details>
  <summary>Verbose output</summary>

  ```
 2025-08-05T14:47:15.729Z: Running command app deploy
2025-08-05T14:47:15.731Z: Running system process in background:
  · Command: /opt/homebrew/Cellar/node/22.9.0/bin/node /opt/homebrew/bin/shopify notifications list --ignore-errors
  · Working directory: /Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev

2025-08-05T14:47:15.736Z: Notifications to show: 0
2025-08-05T14:47:15.744Z: Reading cached app information for directory /Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev...
2025-08-05T14:47:15.744Z: Reading the content of file at shopify.app.toml...
2025-08-05T14:47:15.746Z: Reading the content of file at shopify.app.toml...
2025-08-05T14:47:15.747Z: Reading cached app information for directory /Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev...
2025-08-05T14:47:15.747Z: Reading the content of file at shopify.app.toml...
2025-08-05T14:47:15.747Z: Reading the content of file at shopify.app.toml...
2025-08-05T14:47:15.748Z: Ensuring that the user is authenticated with the Partners API with the following scopes:
[]

2025-08-05T14:47:15.748Z: Getting session store...
2025-08-05T14:47:15.749Z: Validating existing session against the scopes:
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

2025-08-05T14:47:15.749Z: - Token validation -> It's expired: true
2025-08-05T14:47:15.749Z: The current session is valid but needs refresh. Refreshing...
2025-08-05T14:47:15.750Z: Sending POST request to URL https://accounts.shopify.com/oauth/token?grant_type=refresh_token&access_token=atkn_CjQIlIjHxAYQtMDHxAZSJggBEhDKFePvyAtF7LMgntYVTcfFGhAgNcggLItMboBhyTnDYkYuEkAKwyYBmuZZa9u0do28TWsKwL4LU_In9tew-YOwc2EdjyT1oKVpgeyxRX3YmqvDJx2aYGcECmsowTEw-uTEMIcP&refresh_token=atkn_CiEIlIjHxAYQlKLlxQaiARIKECA1yCAsi0xugGHJOcNiRi4SQBGkj1wEggIKnNMUc1OxQu0RyUewnxDLzme8hac5wZR2gJKLZqLidNp44fX6ywvWRlV1mKcoT99dtx4hCzGohgA&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3
With request headers:


2025-08-05T14:47:16.166Z: Request to https://accounts.shopify.com/oauth/token?grant_type=refresh_token&access_token=atkn_CjQIlIjHxAYQtMDHxAZSJggBEhDKFePvyAtF7LMgntYVTcfFGhAgNcggLItMboBhyTnDYkYuEkAKwyYBmuZZa9u0do28TWsKwL4LU_In9tew-YOwc2EdjyT1oKVpgeyxRX3YmqvDJx2aYGcECmsowTEw-uTEMIcP&refresh_token=atkn_CiEIlIjHxAYQlKLlxQaiARIKECA1yCAsi0xugGHJOcNiRi4SQBGkj1wEggIKnNMUc1OxQu0RyUewnxDLzme8hac5wZR2gJKLZqLidNp44fX6ywvWRlV1mKcoT99dtx4hCzGohgA&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3 completed in 416 ms
With response headers:
 - cache-control: no-cache, no-store, private, must-revalidate, max-age=0
 - content-type: application/json; charset=utf-8
 - etag: W/"a6662ee031655258e62459fff3162b12"
 - server-timing: processing;dur=83, socket_queue;dur=1.59, edge;dur=1.036, util;dur=0.3, cfRequestDuration;dur=325.999975
 - x-request-id: 4f1008c8-5ee3-44d4-9e3a-df974a113bd4-1754405236
    
2025-08-05T14:47:16.169Z: Sending POST request to URL https://accounts.shopify.com/oauth/token?grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3&audience=271e16d403dfa18082ffb3d197bd2b5f4479c3fc32736d69296829cbb28d41a6&scope=https%3A%2F%2Fapi.shopify.com%2Fauth%2Fpartners.app.cli.access&subject_token=****
With request headers:


2025-08-05T14:47:16.169Z: Sending POST request to URL https://accounts.shopify.com/oauth/token?grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3&audience=ee139b3d-5861-4d45-b387-1bc3ada7811c&scope=https%3A%2F%2Fapi.shopify.com%2Fauth%2Fshop.storefront-renderer.devtools&subject_token=****
With request headers:


2025-08-05T14:47:16.169Z: Sending POST request to URL https://accounts.shopify.com/oauth/token?grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3&audience=32ff8ee5-82b8-4d93-9f8a-c6997cefb7dc&scope=https%3A%2F%2Fapi.shopify.com%2Fauth%2Fdestinations.readonly+https%3A%2F%2Fapi.shopify.com%2Fauth%2Forganization.store-management+https%3A%2F%2Fapi.shopify.com%2Fauth%2Forganization.on-demand-user-access&subject_token=****
With request headers:


2025-08-05T14:47:16.169Z: Sending POST request to URL https://accounts.shopify.com/oauth/token?grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3&audience=7ee65a63608843c577db8b23c4d7316ea0a01bd2f7594f8a9c06ea668c1b775c&scope=https%3A%2F%2Fapi.shopify.com%2Fauth%2Forganization.apps.manage&subject_token=****
With request headers:


2025-08-05T14:47:16.508Z: Request to https://accounts.shopify.com/oauth/token?grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3&audience=ee139b3d-5861-4d45-b387-1bc3ada7811c&scope=https%3A%2F%2Fapi.shopify.com%2Fauth%2Fshop.storefront-renderer.devtools&subject_token=**** completed in 339 ms
With response headers:
 - cache-control: no-cache, no-store, private, must-revalidate, max-age=0
 - content-type: application/json; charset=utf-8
 - etag: W/"5efa1a0c63555634b5e632f69fa1919e"
 - server-timing: processing;dur=40, socket_queue;dur=1.072, edge;dur=1.037, util;dur=0.05, cfRequestDuration;dur=267.999887
 - x-request-id: e68e675d-de54-40ed-9fd0-0d7632fcd39e-1754405236
    
2025-08-05T14:47:16.512Z: Request to https://accounts.shopify.com/oauth/token?grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3&audience=32ff8ee5-82b8-4d93-9f8a-c6997cefb7dc&scope=https%3A%2F%2Fapi.shopify.com%2Fauth%2Fdestinations.readonly+https%3A%2F%2Fapi.shopify.com%2Fauth%2Forganization.store-management+https%3A%2F%2Fapi.shopify.com%2Fauth%2Forganization.on-demand-user-access&subject_token=**** completed in 343 ms
With response headers:
 - cache-control: no-cache, no-store, private, must-revalidate, max-age=0
 - content-type: application/json; charset=utf-8
 - etag: W/"798a55f195a9511f92775b1f71c1ac99"
 - server-timing: processing;dur=43, socket_queue;dur=1.621, edge;dur=1.034, util;dur=0.1, cfRequestDuration;dur=273.000002
 - x-request-id: edfc4a11-275f-461e-b112-54c38d72bcd9-1754405236
    
2025-08-05T14:47:16.514Z: Request to https://accounts.shopify.com/oauth/token?grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3&audience=271e16d403dfa18082ffb3d197bd2b5f4479c3fc32736d69296829cbb28d41a6&scope=https%3A%2F%2Fapi.shopify.com%2Fauth%2Fpartners.app.cli.access&subject_token=**** completed in 345 ms
With response headers:
 - cache-control: no-cache, no-store, private, must-revalidate, max-age=0
 - content-type: application/json; charset=utf-8
 - etag: W/"b286d3c551818d256d7cf6b1a17f747b"
 - server-timing: processing;dur=45, socket_queue;dur=1.49, edge;dur=1.037, util;dur=0.05, cfRequestDuration;dur=273.999929
 - x-request-id: b977fc34-ba49-4917-bb71-5724ed6a65e0-1754405236
    
2025-08-05T14:47:16.583Z: Request to https://accounts.shopify.com/oauth/token?grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&client_id=fbdb2649-e327-4907-8f67-908d24cfd7e3&audience=7ee65a63608843c577db8b23c4d7316ea0a01bd2f7594f8a9c06ea668c1b775c&scope=https%3A%2F%2Fapi.shopify.com%2Fauth%2Forganization.apps.manage&subject_token=**** completed in 414 ms
With response headers:
 - cache-control: no-cache, no-store, private, must-revalidate, max-age=0
 - content-type: application/json; charset=utf-8
 - etag: W/"f11b2470c987d775a33b43265a86da2c"
 - server-timing: processing;dur=65, socket_queue;dur=1.296, edge;dur=2.043, util;dur=0.1, cfRequestDuration;dur=345.999956
 - x-request-id: b87ab7f9-362a-42ad-a738-ddc9a44bd510-1754405236
    
2025-08-05T14:47:16.584Z: Setting session store...
2025-08-05T14:47:16.592Z: Getting partner account info from cache
2025-08-05T14:47:16.597Z: Sending "Partners" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.81.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-08-05T14:47:17.661Z: Request to https://partners.shopify.com/api/cli/graphql completed in 1063 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"f0404ad319293a5ab65ec60b31406d9c"
 - server-timing: processing;dur=685, socket_queue;dur=5.557, util;dur=0.9, cfRequestDuration;dur=904.999971
 - x-request-id: fc26dcef-0575-43fe-a93f-fd91d64476ab-1754405236
    
2025-08-05T14:47:17.668Z: Sending "Partners" GraphQL request:
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
  "id": "2107579"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.81.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-08-05T14:47:18.098Z: Request to https://partners.shopify.com/api/cli/graphql completed in 428 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"870700c9c7111997680349be20f8175e"
 - server-timing: processing;dur=81, socket_queue;dur=27.266, util;dur=0.4, cfRequestDuration;dur=346.000195
 - x-request-id: ccab2a52-593b-416b-b3d7-5eb9b6c7b583-1754405238
    
2025-08-05T14:47:18.112Z: Sending "Partners" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.81.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-08-05T14:47:18.474Z: Request to https://partners.shopify.com/api/cli/graphql completed in 361 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"e6335d7138251958db585f7729a62d76"
 - server-timing: processing;dur=54, socket_queue;dur=1.871, util;dur=0.2, cfRequestDuration;dur=279.000044
 - x-request-id: dea4c334-4fa9-42d7-98ba-0f94d5f058e8-1754405238
    
2025-08-05T14:47:18.488Z: The following extension specifications were defined locally but not found in the remote specifications: tax_calculation
2025-08-05T14:47:18.495Z: Reading the content of file at .gitignore...
2025-08-05T14:47:18.499Z: Reading the .env file at .env
2025-08-05T14:47:18.499Z: Reading the content of file at .env...
2025-08-05T14:47:18.502Z: Reading the content of file at extensions/payments-app-credit-card-payment-extension-testing/shopify.extension.toml...
2025-08-05T14:47:18.506Z: Reading the content of file at extensions/payments-app-credit-card-payment-extension-testing/shopify.extension.toml...
2025-08-05T14:47:18.508Z: Reading the content of file at package.json...
2025-08-05T14:47:18.508Z: Reading the content of file at package.json...
2025-08-05T14:47:18.510Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev

2025-08-05T14:47:18.604Z: Obtaining the dependency manager in directory /Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev...
2025-08-05T14:47:18.604Z: Reading the content of file at package.json...
2025-08-05T14:47:18.605Z: Reading the content of file at .shopify/project.json...
2025-08-05T14:47:18.607Z: Notifications to show: 0
2025-08-05T14:47:18.608Z: Unable to decide project type as no web backend
2025-08-05T14:47:18.608Z: Reading cached app information for directory /Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev...
2025-08-05T14:47:18.608Z: Storing app information for directory /Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev:{
  "appId": "0e1c676b13ea0bcf7fef0da965371e53",
  "title": "Native Checkout | Dev",
  "directory": "/Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev",
  "orgId": "2107579"
}
2025-08-05T14:47:18.615Z: Sending "Partners" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.81.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-08-05T14:47:19.398Z: Request to https://partners.shopify.com/api/cli/graphql completed in 783 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"0989ce0ef93f8b1cd481a70e27eaa1e5"
 - server-timing: processing;dur=389, socket_queue;dur=2.168, util;dur=0.4, cfRequestDuration;dur=606.999874
 - x-request-id: 94866034-eee4-48b7-8deb-705ed735c8b9-1754405238
    
╭─ info ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                            │
│  Using .env for default values:                                                                                                            │
│                                                                                                                                            │
│    • Org:             Tap Payments                                                                                                         │
│    • App:             Native Checkout | Dev                                                                                                │
│    • Include config:  Yes                                                                                                                  │
│                                                                                                                                            │
│   You can pass `--reset` to your command to reset your app configuration.                                                                  │
│                                                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-08-05T14:47:19.443Z: Sending "Partners" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.81.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://partners.shopify.com/api/cli/graphql
2025-08-05T14:47:20.816Z: Request to https://partners.shopify.com/api/cli/graphql completed in 1373 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"250339a82ff0dc4aae8fb53493464e11"
 - server-timing: processing;dur=1063, socket_queue;dur=1.632, util;dur=0.6, cfRequestDuration;dur=1295.000076
 - x-request-id: 0c5be617-f02d-46e0-8416-b9597a46b605-1754405239
    
?  Release a new version of Native Checkout | Dev?
✔  Yes, release this new version


Releasing a new app version as part of Native Checkout | Dev

2025-08-05T14:47:23.549Z: Removing directory at .shopify/deploy-bundle...
2025-08-05T14:47:23.553Z: Creating directory at .shopify/deploy-bundle...
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Running validation ...
2025-08-05T14:47:23.569Z: Sending "Partners" GraphQL request:
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
  "appId": "48729063425",
  "apiKey": "*****",
  "name": "onsite-dev",
  "skipPublish": false,
  "appModules": [
    {
      "config": "{\"api_version\":\"2025-07\",\"start_payment_session_url\":\"https://d75df9762dd6.ngrok-free.app/v2/platform/shopify/onsite/payment\",\"start_refund_session_url\":\"https://d75df9762dd6.ngrok-free.app/v2/platform/shopify/onsite/refund\",\"start_capture_session_url\":\"https://d75df9762dd6.ngrok-free.app/v2/platform/shopify/onsite/capture\",\"start_void_session_url\":\"https://d75df9762dd6.ngrok-free.app/v2/platform/shopify/onsite/void\",\"confirmation_callback_url\":\"https://d75df9762dd6.ngrok-free.app/v2/platform/shopify/onsite/confirm\",\"multiple_capture\":false,\"merchant_label\":\"Tap Payments | Native Dev\",\"supported_countries\":[\"AF\",\"AZ\",\"BH\",\"BD\",\"BT\",\"BN\",\"KH\",\"CN\",\"CX\",\"CC\",\"HK\",\"IN\",\"ID\",\"IQ\",\"IL\",\"JP\",\"JO\",\"KZ\",\"KW\",\"KG\",\"LA\",\"LB\",\"MO\",\"MY\",\"MV\",\"MN\",\"MM\",\"NP\",\"OM\",\"PK\",\"PS\",\"PH\",\"QA\",\"SA\",\"SG\",\"KR\",\"LK\",\"TW\",\"TJ\",\"TH\",\"TM\",\"AE\",\"UZ\",\"VN\",\"YE\",\"FR\",\"DE\",\"IE\",\"IT\",\"NL\",\"ES\",\"TR\",\"GB\",\"CA\",\"MX\",\"US\",\"DZ\",\"EG\",\"MA\",\"TN\",\"KE\",\"LY\",\"NG\",\"ZA\",\"SD\",\"AU\",\"NZ\",\"AR\",\"BR\",\"CL\",\"UY\"],\"supported_payment_methods\":[\"american_express\",\"visa\",\"master\",\"mada\",\"naps\"],\"test_mode_available\":true,\"supports_3ds\":true,\"supports_moto\":true,\"supports_deferred_payments\":false,\"encryption_certificate_fingerprint\":\"Test Certificate\",\"supports_installments\":false}",
      "context": "payments.credit-card.render",
      "handle": "paymentsapp-credit-card-paymen",
      "uuid": "faa1b499-22cf-498f-99ab-a9e5a1fdf330",
      "specificationIdentifier": "PAYMENTS_EXTENSION"
    },
    {
      "config": "{\"api_version\":\"2025-07\",\"customers_redact_url\":\"https://api.dev.tap.company/v2/platform/shopify/onsite/event/customers/redact\",\"customers_data_request_url\":\"https://api.dev.tap.company/v2/platform/shopify/onsite/event/customers/data_request\",\"shop_redact_url\":\"https://d75df9762dd6.ngrok-free.app/v2/platform/shopify/onsite/event/shop/redact\"}",
      "context": "",
      "handle": "privacy_compliance_webhooks",
      "uuid": "ee0408ab-ad62-4bea-bbe1-2370720d3ed5",
      "specificationIdentifier": "PRIVACY_COMPLIANCE_WEBHOOKS"
    },
    {
      "config": "{\"redirect_url_allowlist\":[\"https://api.dev.tap.company/v2/platform/shopify/onsite/success\"]}",
      "context": "",
      "handle": "app_access",
      "uuid": "08d5d2d2-0b1d-42d5-9d27-e7a5fc46a68b",
      "specificationIdentifier": "APP_ACCESS"
    },
    {
      "config": "{\"api_version\":\"2025-07\"}",
      "context": "",
      "handle": "webhooks",
      "uuid": "2e1650fd-45a1-4432-99fa-c0438fd4c96c",
      "specificationIdentifier": "WEBHOOKS"
    },
    {
      "config": "{\"embedded\":false}",
      "context": "",
      "handle": "point_of_sale",
      "uuid": "431ba77c-5ed6-4542-86e1-564f1363515c",
      "specificationIdentifier": "POINT_OF_SALE"
    },
    {
      "config": "{\"app_url\":\"https://api.dev.tap.company/v2/platform/shopify/onsite/\",\"embedded\":true}",
      "context": "",
      "handle": "app_home",
      "uuid": "f5f76d0e-fb32-4f76-8cbb-58e146838bef",
      "specificationIdentifier": "APP_HOME"
    },
    {
      "config": "{\"name\":\"Native Checkout | Dev\",\"app_handle\":\"dev-tap-paymentsonsite\"}",
      "context": "",
      "handle": "branding",
      "uuid": "c492f7c7-3cc7-45af-81c7-ef699d2efcae",
      "specificationIdentifier": "BRANDING"
    }
  ]
}

With request headers:
 - User-Agent: Shopify CLI; v=3.81.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Releasing an app version ...
2025-08-05T14:47:24.441Z: Request to https://partners.shopify.com/api/cli/graphql completed in 872 ms
With response headers:
 - cache-control: max-age=0, private, must-revalidate
 - content-type: application/json; charset=utf-8
 - etag: W/"b6bc841ff6a9d3340c03ec198c850622"
 - server-timing: processing;dur=546, socket_queue;dur=2.501, util;dur=0.7, cfRequestDuration;dur=793.999910

╭─ error ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                            │
│  Version couldn't be created.                                                                                                              │
│                                                                                                                                            │
│  Following payment methods not permitted: ["naps"]                                                                                         │
│                                                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-08-05T14:47:24.459Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev

2025-08-05T14:47:24.564Z: Obtaining the dependency manager in directory /Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev...
2025-08-05T14:47:25.159Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 508 ms
With response headers:
 - x-request-id: ad059ed1-7369-4751-a3c8-0156dace706a
    
2025-08-05T14:47:25.160Z: Analytics event sent: {
  "command": "app deploy",
  "time_start": 1754405235730,
  "time_end": 1754405244454,
  "total_time": 8724,
  "success": false,
  "cli_version": "3.81.2",
  "ruby_version": "",
  "node_version": "22.9.0",
  "is_employee": false,
  "uname": "darwin arm64",
  "env_ci": false,
  "env_plugin_installed_any_custom": false,
  "env_plugin_installed_shopify": "[\"@shopify/cli\"]",
  "env_shell": "zsh",
  "env_device_id": "aa2695f6cfed1e1e0c9d07e8c359755d79f68e83",
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
  "cmd_app_all_configs_clients": "{\"shopify.app.toml\":\"0e1c676b13ea0bcf7fef0da965371e53\"}",
  "cmd_app_linked_config_used": true,
  "cmd_app_linked_config_name": "shopify.app.toml",
  "cmd_app_linked_config_git_tracked": true,
  "cmd_app_linked_config_source": "cached",
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
  "app_name_hash": "95bd69c0546b9cc92912a75c2d72207a8378130a",
  "app_path_hash": "d92fcd39e8a9d7190475c86505b996ae96961150",
  "app_scopes": "[]",
  "app_web_backend_any": false,
  "app_web_backend_count": 0,
  "app_web_custom_layout": false,
  "app_web_frontend_any": false,
  "app_web_frontend_count": 0,
  "env_package_manager_workspaces": true,
  "partner_id": 2107579,
  "api_key": "****",
  "cmd_app_reset_used": false,
  "cmd_deploy_include_config_used": true,
  "cmd_deploy_config_modules_breakdown": "[\"application_url\",\"auth\",\"embedded\",\"handle\",\"name\",\"pos\",\"webhooks\"]",
  "cmd_deploy_config_modules_updated": "[\"webhooks\"]",
  "cmd_deploy_confirm_new_registrations": 0,
  "cmd_deploy_confirm_updated_registrations": 1,
  "cmd_deploy_confirm_removed_registrations": 0,
  "cmd_deploy_confirm_cancelled": false,
  "cmd_deploy_confirm_time_to_complete_ms": 2711,
  "cmd_all_timing_network_ms": 5711,
  "cmd_all_timing_prompts_ms": 2710,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "app",
  "cmd_all_plugin": "@shopify/app",
  "cmd_all_force": false,
  "cmd_all_verbose": true,
  "cmd_all_path_override": true,
  "cmd_all_path_override_hash": "d92fcd39e8a9d7190475c86505b996ae96961150",
  "cmd_all_last_graphql_request_id": "dd4b5c8f-ea1e-4d5a-985f-93379f5fdd2a-1754405243",
  "cmd_all_timing_active_ms": 301,
  "cmd_all_exit": "expected_error",
  "user_id": "98bc067a-b4cb-47f9-82e0-46cbea0c840a",
  "request_ids": [
    "fc26dcef-0575-43fe-a93f-fd91d64476ab-1754405236",
    "ccab2a52-593b-416b-b3d7-5eb9b6c7b583-1754405238",
    "dea4c334-4fa9-42d7-98ba-0f94d5f058e8-1754405238",
    "94866034-eee4-48b7-8deb-705ed735c8b9-1754405238",
    "0c5be617-f02d-46e0-8416-b9597a46b605-1754405239",
    "dd4b5c8f-ea1e-4d5a-985f-93379f5fdd2a-1754405243"
  ],
  "args": "--verbose",
  "error_message": "Version couldn't be created.",
  "app_name": "onsite-dev",
  "env_plugin_installed_all": "[\"@shopify/cli\"]",
  "metadata": "{\"extraPublic\":{},\"extraSensitive\":{}}"
}
2025-08-05T14:47:25.175Z: Reporting handled error to Bugsnag: Version couldn't be created.
2025-08-05T14:47:25.312Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev

2025-08-05T14:47:25.391Z: Obtaining the dependency manager in directory /Users/mtariq-pk/shopify-migration/shopify-onsite-dev/onsite-dev...
  ```

</details>

### Reproduction steps

1. Change URLs in toml file
2. shopify app deploy
3. Error pops up

### Operating System

Mac OS Sequoia

### Shopify CLI version (`shopify --version`)

3.81.2

### Shell

_No response_

### Node version (run `node -v` if you're not sure)

_No response_

### What language and version are you using in your application?

_No response_

===

comment #1 by mjtariq9, 2025-08-05, 14:50:14
@isaacroldan  can you please help, naps was in the toml file since the beginning but it never gave the error.

comment #2 by gonzaloriestra, 2025-08-06, 06:43:32
Hi! The internal validation system was updated for payments and it looks like there is an issue with NAPS. We are working on it, I'll let you know once it's fixed. Sorry for the inconvenience!

comment #3 by gonzaloriestra, 2025-08-13, 09:37:28
It should be working now. Otherwise, please let me know!
