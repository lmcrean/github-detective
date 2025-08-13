issue title: [Bug]: Theme commands hitting network issues
labels: Severity: 2, Type: Bug, Area: @shopify/theme
comment count: 34
hyperlink: https://github.com/shopify/cli/issues/6062
status: open
date opened: 2025-07-03
repo 30d_merge_rate: 77

====

description:
This serves as the main issue for network-related problems that have been hindering developers using `theme` commands (in particular `theme dev` and `theme push`). We're going to colocate all problems here to make sure we have a single point of entry.

## Known Issues

### GraphQL requests fail

There are a few specific issues that we're currently tracking:

No reason:
```
Failed to perform the initial theme synchronization.
request to https://<shop>.myshopify.com/admin/api/2025-04/graphql.json failed, reason:
```

Timeout:
```
request to https://<shop>.myshopify.com/admin/api/unstable/themes.json failed, 
reason: read ETIMEDOUT
```

```
Error while polling for changes.  
request to https://<shop>.myshopify.com/admin/api/2025-04/graphql.json failed, reason: 
AggregateError [ETIMEDOUT]
```

TLS:

```
request to https://<shop>.myshopify.com/admin/api/2025-04/graphql.json failed,
reason: Client network socket disconnected before secure TLS connection was established  
```

### Large themes

Some large themes are also potentially experiencing either exacerbated issues of the above or different issues altogether like hanging on `theme dev` due to a separate Liquid parsing issue.

## How to help

If you'd like to provide a comment on this issue please make sure to include important information like:

- Use the snapshotted version of the CLI that contains a potential fix: https://github.com/Shopify/cli/issues/6062#issuecomment-3089008358
- Verbose logs, please use the following format to keep the logs condensed:
    ````
    <details>
        <summary>Verbose output</summary>
        ```
        your logs here
        ```
    </details>
    ````
- (Optional) Your location, network connection, and any other additional pieces like VPN, hotspot, etc (we're trying to understand if this is a latency issue of some kind)

===

comment #1 by mcnabsystems, 2025-07-04, 08:00:22
I'm glad it isn't just me, having a nightmare yesterday and today with both `theme dev` and `theme push`, tried downgrading the CLI to various past versions to no effect.  My error seems to stem from a very slow connection to graphql.json;

<details>
    <summary>Verbose output</summary>

`    2025-07-04T07:43:48.801Z: Request to https://performancelab-dev.myshopify.com/admin/api/2025-07/graphql.json completed in 31621 ms
With response headers:

error

Failed to perform the initial theme synchronization.  

The user aborted a request. `

</details>

File changes are being successfully pushed to the theme despite the error being thrown.  The commands appear to work (but slowly) the error is thrown afterwards when it fails to access graphql.json again. 

Also had to use ThemeKit to upload a large theme, the CLI kept failing with `The user aborted a request. `

Based in UK, not using a VPN.


comment #2 by MaxDesignFR, 2025-07-04, 08:13:15
@mcnabsystems have you tried 3.79.2? That's the version where the CLI is usable for me (otherwise 30+ seconds delay from 3.8 and up). But I reckon for months I've had issues with network, and I believe at some point changing my node version + reinstalling the CLI (or vice-versa) did improve my experience with the CLI, as I was constantly facing that issue: https://github.com/Shopify/cli/issues/5760

comment #3 by mcnabsystems, 2025-07-04, 08:40:06
@MaxDesignFR - thanks for the reply.  3.79.2 was one that I tried, I saw your previous issue #5760 and tried rolling back.  Unfortunately it doesn't seem to have fixed it, I will try a node change to the LTS version and see if that helps.  Appreciate your help, cheers!

Edit: Downgrade to node v22 LTS  and Shopify CLI 3.79.2 made no difference in my case.


comment #4 by gabrieljadeau, 2025-07-04, 13:27:09
<details>
    <summary>Verbose output</summary>
    ```
2025-07-04T13:23:06.803Z: Running command theme dev
2025-07-04T13:23:06.805Z: Running system process in background:
  · Command: /Users/gabrieljadeau/.nvm/versions/node/v22.14.0/bin/node /Users/gabrieljadeau/.nvm/versions/node/v22.14.0/bin/shopify notifications list --ignore-errors
  · Working directory: /Users/gabrieljadeau/Sites/shopify-loulousaison

2025-07-04T13:23:06.809Z: Notifications to show: 0
2025-07-04T13:23:06.818Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-04T13:23:06.818Z: Ensuring that the user is authenticated with the Admin API with the following scopes for the store louloudesaison.myshopify.com:
[]

2025-07-04T13:23:06.818Z: Getting session store...
2025-07-04T13:23:06.819Z: Validating existing session against the scopes:
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
  "adminApi": {
    "scopes": [],
    "storeFqdn": "louloudesaison.myshopify.com"
  }
}

2025-07-04T13:23:06.820Z: - Token validation -> It's expired: false
2025-07-04T13:23:06.820Z: Getting development theme...
2025-07-04T13:23:06.821Z: Sending "Admin" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://louloudesaison.myshopify.com/admin/api/unstable/graphql.json
2025-07-04T13:23:21.876Z: Request to https://louloudesaison.myshopify.com/admin/api/unstable/graphql.json completed in 15054 ms
With response headers:

    
2025-07-04T13:23:21.876Z: Error fetching theme with ID: 183623647580
2025-07-04T13:23:21.877Z: Removing development theme...
2025-07-04T13:23:21.894Z: Sending "Admin" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://louloudesaison.myshopify.com/admin/api/unstable/graphql.json
2025-07-04T13:23:22.105Z: Request to https://louloudesaison.myshopify.com/admin/api/unstable/graphql.json completed in 210 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=48, graphql;desc="admin/query/other", cfRequestDuration;dur=104.000092
 - x-request-id: ab036e80-8423-4e77-99bc-b57c8485a81f-1751635402
    
2025-07-04T13:23:22.105Z: Sending "Admin" GraphQL request:
  mutation themeCreate($name: String!, $source: URL!, $role: ThemeRole!) {
  themeCreate(name: $name, source: $source, role: $role) {
    theme {
      id
      name
      role
      __typename
    }
    userErrors {
      field
      message
      __typename
    }
    __typename
  }
}

With variables:
{
  "name": "Development (34fc5a-Gabriels-MacBook-Pro)",
  "source": "https://cdn.shopify.com/static/online-store/theme-skeleton.zip",
  "role": "DEVELOPMENT"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://louloudesaison.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:23:23.311Z: Request to https://louloudesaison.myshopify.com/admin/api/2025-07/graphql.json completed in 1206 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=1080, graphql;desc="admin/mutation/other", cfRequestDuration;dur=1129.999876
 - x-request-id: 87a2e00a-9e3e-4c85-b954-81b52223c609-1751635402
    
2025-07-04T13:23:23.312Z: Setting development theme...
2025-07-04T13:23:23.347Z: Sending "Admin" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://louloudesaison.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:23:23.526Z: Request to https://louloudesaison.myshopify.com/admin/api/2025-07/graphql.json completed in 179 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=59, graphql;desc="admin/query/other", cfRequestDuration;dur=108.999968
 - x-request-id: 3dff9f31-a79a-46d0-bfac-88a0e70a58fb-1751635403
    
2025-07-04T13:23:23.527Z: Getting storefront password for shop louloudesaison.myshopify.com...
2025-07-04T13:23:23.528Z: Sending POST request to URL https://louloudesaison.myshopify.com/password
With request headers:
 - cache-control: no-cache
 - content-type: application/x-www-form-urlencoded

2025-07-04T13:23:23.706Z: Request to https://louloudesaison.myshopify.com/password completed in 177 ms
With response headers:
 - content-type: text/html; charset=utf-8
 - server-timing: processing;dur=37, db;dur=4, db_async;dur=1.469, asn;desc="3352", edge;desc="MAD", country;desc="ES", pageType;desc="password", servedBy;desc="d8kd", requestID;desc="113cb86b-e87c-4289-ad4b-901fc1d85d91-1751635403", cfRequestDuration;dur=88.999987
 - x-request-id: 113cb86b-e87c-4289-ad4b-901fc1d85d91-1751635403
    
2025-07-04T13:23:23.706Z: Setting storefront password for shop louloudesaison.myshopify.com...
2025-07-04T13:23:23.739Z: Port 9292 is free
2025-07-04T13:23:23.739Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-04T13:23:23.739Z: Ensuring that the user is authenticated with the Admin API with the following scopes for the store louloudesaison.myshopify.com:
[]

2025-07-04T13:23:23.740Z: Getting session store...
2025-07-04T13:23:23.740Z: Validating existing session against the scopes:
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
  "adminApi": {
    "scopes": [],
    "storeFqdn": "louloudesaison.myshopify.com"
  }
}

2025-07-04T13:23:23.741Z: - Token validation -> It's expired: false
2025-07-04T13:23:23.741Z: Ensuring that the user is authenticated with the Storefront API with the following scopes:
[]

2025-07-04T13:23:23.741Z: Getting session store...
2025-07-04T13:23:23.741Z: Validating existing session against the scopes:
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
  "storefrontRendererApi": {
    "scopes": []
  }
}

2025-07-04T13:23:23.741Z: - Token validation -> It's expired: false
2025-07-04T13:23:23.742Z: Sending HEAD request to URL https://louloudesaison.myshopify.com/?preview_theme_id=183623680348&_fd=0&pb=0
With request headers:
 - X-Shopify-Shop: louloudesaison.myshopify.com
 - User-Agent: Shopify CLI; v=3.82.0

2025-07-04T13:23:23.755Z: Reading the content of file at assets/_ui.css...
2025-07-04T13:23:23.755Z: Reading the content of file at assets/ajaxinate.min.js...
2025-07-04T13:23:23.755Z: Reading the content of file at assets/checkmark-inverted.svg...
2025-07-04T13:23:23.755Z: Reading the content of file at assets/checkmark-inverted.svg.liquid...
2025-07-04T13:23:23.755Z: Reading the content of file at assets/checkmark.svg...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/checkmark.svg.liquid...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/clip-blob.css...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/component-add-to-cart-mobile.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/component-custom-cart-drawer.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/component-custom-product-list.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/component-estimate-delivery_date.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/component-product-gallery-custom.css...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/component-product-gallery-custom.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/component-quick-add-to-cart.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/component-scrollbar-navigation-scrollbar.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/component-toast.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/component-variant-changer.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/custom.css...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/custom.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/documentation.txt...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/font-albra_thin.otf...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/font-cormorantGaramond_light.ttf...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/font-mignon_regular.otf...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/photoswipe.min.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/theme.css...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/theme.js...
2025-07-04T13:23:23.756Z: Reading the content of file at assets/vendor.min.js...
2025-07-04T13:23:23.756Z: Reading the content of file at config/settings_data.json...
2025-07-04T13:23:23.756Z: Reading the content of file at config/settings_schema.json...
2025-07-04T13:23:23.756Z: Reading the content of file at layout/theme.liquid...
2025-07-04T13:23:23.756Z: Reading the content of file at locales/ar.json...
2025-07-04T13:23:23.756Z: Reading the content of file at locales/cs.json...
2025-07-04T13:23:23.756Z: Reading the content of file at locales/da.json...
2025-07-04T13:23:23.756Z: Reading the content of file at locales/de.json...
2025-07-04T13:23:23.756Z: Reading the content of file at locales/el.json...
2025-07-04T13:23:23.756Z: Reading the content of file at locales/en.default.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/en.default.schema.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/es.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/fi.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/fr.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/fr.schema.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/he.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/it.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/ja.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/ko.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/lt.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/lv.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/nb.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/nl.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/pl.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/pt-BR.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/ro.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/ru.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/sk.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/sl.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/sv.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/tr.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/uk.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/zh-CN.json...
2025-07-04T13:23:23.757Z: Reading the content of file at locales/zh-TW.json...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/age-verifier-popup.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/announcement-bar.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/apps.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/before-after.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/blog-banner.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/blog-post-banner.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/blog-post-prev-next.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/blog-posts.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/cart-drawer.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/cart-drawer-custom.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/collection-banner.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/collection-list.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/collection-submenu.liquid...
2025-07-04T13:23:23.757Z: Reading the content of file at sections/contact.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/countdown-condensed.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/countdown.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/custom-liquid.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/dynamic-grid.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/faq.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/featured-collections.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/featured-links.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/featured-product-list.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/featured-product.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/footer-group.json...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/footer.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/header-group.json...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/header.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/hot-spots.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/image-with-text-overlay.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/links-with-image.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/logo-list.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-account.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-article.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-blog.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-cart.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-collection.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-customers-activate-account.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-customers-addresses.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-customers-login.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-customers-account.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-customers-order.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-customers-register.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-customers-reset-password.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-gift-card.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-list-collections.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-not-found.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-page.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-password.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-product.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/main-search.liquid...
2025-07-04T13:23:23.758Z: Reading the content of file at sections/media-blocks.liquid...
2025-07-04T13:23:23.759Z: Reading the content of file at sections/multi-column.liquid...
2025-07-04T13:23:23.759Z: Reading the content of file at sections/news-modal.liquid...
2025-07-04T13:23:23.759Z: Reading the content of file at sections/newsletter-popup.liquid...
2025-07-04T13:23:23.759Z: Reading the content of file at sections/newsletter.liquid...
2025-07-04T13:23:23.759Z: Reading the content of file at sections/overlay-group.json...
2025-07-04T13:23:23.759Z: Reading the content of file at sections/predictive-search.liquid...
2025-07-04T13:23:23.759Z: Reading the content of file at sections/press.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/products-with-image.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/reading-text.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/recently-viewed-products.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/related-products.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/rich-text.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/scrolling-content.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/search-drawer.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/slideshow.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/specifications.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/testimonials.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/text-with-fixed-background.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/text-with-icons.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/text-with-media.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/timeline.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/trust-icons.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at sections/video.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/_dynamic-grid-heading.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/_dynamic-grid-item.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/_hot-spot-content-item.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/_hot-spot-content-product.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/_multi-column-column.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/_multi-column-spacer.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/_placeable-content.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/_section-header.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/_slideshow-controls.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/_slideshow-image-slide.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/accordion.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/_slideshow-video-slide.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/button-group.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/button.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/collection-card.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/heading.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/icon.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/image-with-caption.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/image.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/liquid.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/page-content.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/rich-text.liquid...
2025-07-04T13:23:23.760Z: Reading the content of file at blocks/separator.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at blocks/spacer.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at blocks/subheading.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at blocks/video-with-caption.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at blocks/video.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/accordion.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/active-facets.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/address-form.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/banner.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/blog-post-card.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/breadcrumb.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/button.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/buy-buttons.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/cart-custom-selector.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/checkbox.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/collection-faceting-button.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/collection-facets-floating-button.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/collection-toolbar.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/color-links.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/css-variables.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/direction.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/estimate-delivery-date.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/facets.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/free-shipping-bar.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/heading.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/hulkapps-wishlist-account-btn.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/hulkapps-wishlist-cart-btn.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/hulkapps-wishlist-collection-btn.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/hulkapps-wishlist-header-icon.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/hulkapps-wishlist-product-btn.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/hulkapps-wishlist-saveforlater-allitems.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/hulkappsWishlistPopup.liquid...
2025-07-04T13:23:23.761Z: Reading the content of file at snippets/icon.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/input.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/inventory.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/js-variables.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/line-item.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/localization-selector.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/main-menu-drawer.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/main-menu-dropdown-sidebar.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/media.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/mega-menu.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/menu-promo.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/microdata-schema.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/offers.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/option-value.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/pagination.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/pickup-availability.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/popup-added-to-cart.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/price-list.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/price-range.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-badges.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-card-placeholder.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-card.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-cross-sell.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-gallery.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-info-tabs.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-info.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-item__image.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-item__name.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-item__sizes.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-list.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-quick-buy.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-rating.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-item__price.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/product-sticky-add-to-cart.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/promo-block.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/quantity-selector.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/quick-add-to-cart.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/select.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/shadow-dom-templates.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/share-buttons.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/shipping-estimator.liquid...
2025-07-04T13:23:23.762Z: Reading the content of file at snippets/social-media.liquid...
2025-07-04T13:23:23.763Z: Reading the content of file at snippets/social-meta-tags.liquid...
2025-07-04T13:23:23.763Z: Reading the content of file at snippets/style-with.liquid...
2025-07-04T13:23:23.763Z: Reading the content of file at snippets/subheading.liquid...
2025-07-04T13:23:23.763Z: Reading the content of file at snippets/surface.liquid...
2025-07-04T13:23:23.763Z: Reading the content of file at snippets/variant-picker.liquid...
2025-07-04T13:23:23.763Z: Reading the content of file at snippets/vendor.liquid...
2025-07-04T13:23:23.763Z: Reading the content of file at snippets/volume-pricing-table.liquid...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/404.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/article.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/blog.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/cart.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/collection.all.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/collection.fall-winter.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/collection.high-summer.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/collection.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/gift_card.liquid...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/index.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/list-collections.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/page.contact.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/page.faq.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/page.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/page.list-collections.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/page.the-brand.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/password.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/page.the-looks-hs.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/product.added-to-cart.liquid...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/product.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/product.pre-order.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/search.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/customers/activate_account.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/customers/account.json...
2025-07-04T13:23:23.763Z: Reading the content of file at templates/customers/addresses.json...
2025-07-04T13:23:23.764Z: Reading the content of file at templates/customers/login.json...
2025-07-04T13:23:23.764Z: Reading the content of file at templates/customers/order.json...
2025-07-04T13:23:23.764Z: Reading the content of file at templates/customers/register.json...
2025-07-04T13:23:23.764Z: Reading the content of file at templates/customers/reset_password.json...
2025-07-04T13:23:23.922Z: Request to https://louloudesaison.myshopify.com/?preview_theme_id=183623680348&_fd=0&pb=0 completed in 180 ms
With response headers:
 - content-type: text/plain; charset=utf-8
 - server-timing: processing;dur=35;desc="gc:1", db;dur=5, db_async;dur=1.527, asn;desc="3352", edge;desc="MAD", country;desc="ES", theme;desc="183623680348", pageType;desc="index", servedBy;desc="vfxf", requestID;desc="8b4d92c6-66e7-47ce-94ce-d8bf44c91ad9-1751635403", cfRequestDuration;dur=82.999945
 - x-request-id: 8b4d92c6-66e7-47ce-94ce-d8bf44c91ad9-1751635403
    
2025-07-04T13:23:23.923Z: Failed to obtain _shopify_essential cookie.

       -Request ID: 8b4d92c6-66e7-47ce-94ce-d8bf44c91ad9-1751635403

       -Body: 

       -Status: 422

2025-07-04T13:23:23.923Z: Retrying to obtain the _shopify_essential cookie...
2025-07-04T13:23:24.923Z: Sending HEAD request to URL https://louloudesaison.myshopify.com/?preview_theme_id=183623680348&_fd=0&pb=0
With request headers:
 - X-Shopify-Shop: louloudesaison.myshopify.com
 - User-Agent: Shopify CLI; v=3.82.0

2025-07-04T13:23:39.963Z: Request to https://louloudesaison.myshopify.com/?preview_theme_id=183623680348&_fd=0&pb=0 completed in 15039 ms
With response headers:

    
╭─ error ───────────────────────────────────────────────────────────────────────────╮
│                                                                                   │
│  request to                                                                       │
│  https://louloudesaison.myshopify.com/?preview_theme_id=183623680348&_fd=0&pb=0   │
│  failed, reason: Client network socket disconnected before secure TLS connection  │
│   was established                                                                 │
│                                                                                   │
╰───────────────────────────────────────────────────────────────────────────────────╯

2025-07-04T13:23:39.987Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/gabrieljadeau/Sites/shopify-loulousaison

2025-07-04T13:23:40.111Z: Obtaining the dependency manager in directory ../.....
2025-07-04T13:23:40.437Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 191 ms
With response headers:
 - x-request-id: fea72b48-3d34-4ce3-a86c-81a8350bf4ea
    
2025-07-04T13:23:40.437Z: Analytics event sent: {
  "command": "theme dev",
  "time_start": 1751635386803,
  "time_end": 1751635419982,
  "total_time": 33179,
  "success": false,
  "cli_version": "3.82.0",
  "ruby_version": "",
  "node_version": "22.14.0",
  "is_employee": false,
  "uname": "darwin arm64",
  "env_ci": false,
  "env_plugin_installed_any_custom": false,
  "env_plugin_installed_shopify": "[\"@shopify/app\",\"@shopify/cli\",\"@shopify/plugin-cloudflare\"]",
  "env_shell": "zsh",
  "env_device_id": "600ae94c5c4f473631e33810cb3d79939d7707d9",
  "env_cloud": "localhost",
  "env_package_manager": "npm",
  "env_is_global": false,
  "env_auth_method": "device_auth",
  "env_is_wsl": false,
  "cmd_app_warning_api_key_deprecation_displayed": false,
  "cmd_all_timing_network_ms": 32046,
  "cmd_all_timing_prompts_ms": 0,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "theme",
  "cmd_all_plugin": "@shopify/theme",
  "cmd_all_force": false,
  "cmd_all_verbose": true,
  "cmd_all_path_override": true,
  "cmd_all_path_override_hash": "f1db15b00f9f1526873ade26c266b1a1409ed4b1",
  "cmd_all_last_graphql_request_id": "3dff9f31-a79a-46d0-bfac-88a0e70a58fb-1751635403",
  "cmd_all_timing_active_ms": 1132,
  "cmd_all_exit": "expected_error",
  "user_id": "ae9f7283-c904-45d8-9638-747273e416c9",
  "request_ids": [
    "ab036e80-8423-4e77-99bc-b57c8485a81f-1751635402",
    "87a2e00a-9e3e-4c85-b954-81b52223c609-1751635402",
    "3dff9f31-a79a-46d0-bfac-88a0e70a58fb-1751635403"
  ],
  "args": "--store=louloudesaison --verbose",
  "error_message": "request to https://louloudesaison.myshopify.com/?preview_theme_id=183623680348&_fd=0&pb=0 failed, reason: Client network socket disconnected before secure TLS connection was established",
  "env_plugin_installed_all": "[\"@shopify/app\",\"@shopify/cli\",\"@shopify/plugin-cloudflare\"]",
  "metadata": "{\"extraPublic\":{\"@shopify/app\":{\"cmd_app_warning_api_key_deprecation_displayed\":false}},\"extraSensitive\":{\"@shopify/app\":{}}}"
}
2025-07-04T13:23:40.452Z: Reporting handled error to Bugsnag: request to https://louloudesaison.myshopify.com/?preview_theme_id=183623680348&_fd=0&pb=0 failed, reason: Client network socket disconnected before secure TLS connection was established
2025-07-04T13:23:40.483Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/gabrieljadeau/Sites/shopify-loulousaison

2025-07-04T13:23:40.605Z: Obtaining the dependency manager in directory ../.....

```
</details>

comment #5 by MaxDesignFR, 2025-07-04, 13:46:49
Worked in the morning, no longer works in the evening. Been like that for months, some good days some bad days.

<details>
<summary>Verbose output</summary>

   ```
   With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
╭─ success ──────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                            │
│  Preview your theme (t)                                                                                    │
│    • http://127.0.0.1:9292                                                                                 │
│                                                                                                            │
│  Next steps                                                                                                │
│    • Share your theme preview (p) https://miye-care.myshopify.com/?preview_theme_id=180623311228           │
│    • Customize your theme at the theme editor (e)                                                          │
│    • Preview your gift cards (g)                                                                           │
│                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-07-04T13:40:39.923Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-04T13:40:39.923Z: Ensuring that the user is authenticated with the Admin API with the following scopes for the store miye-care.myshopify.com:
[]

2025-07-04T13:40:39.923Z: Getting session store...
2025-07-04T13:40:39.924Z: Validating existing session against the scopes:
[
  "openid",
  "https://api.shopify.com/auth/shop.admin.graphql",
  "https://api.shopify.com/auth/shop.admin.themes",
  "https://api.shopify.com/auth/partners.collaborator-relationships.readonly",
  "https://api.shopify.com/auth/shop.storefront-renderer.devtools",
  "https://api.shopify.com/auth/partners.app.cli.access",
  "https://api.shopify.com/auth/destinations.readonly",
  "https://api.shopify.com/auth/organization.store-management",
  "https://api.shopify.com/auth/organization.apps.manage"
]
For applications:
{
  "adminApi": {
    "scopes": [],
    "storeFqdn": "miye-care.myshopify.com"
  }
}

2025-07-04T13:40:39.924Z: - Token validation -> It's expired: false
2025-07-04T13:40:39.996Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "ARTICLE"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:39.996Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "BLOG"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:39.997Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COLLECTION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:39.997Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COMPANY"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:39.997Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COMPANY_LOCATION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:39.998Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "LOCATION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:39.998Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "MARKET"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:39.998Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "ORDER"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:39.999Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PAGE"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:39.999Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PRODUCT"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:39.999Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PRODUCTVARIANT"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:39.999Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "SHOP"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json
2025-07-04T13:40:40.865Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 866 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=78, graphql;desc="admin/query/other", cfRequestDuration;dur=498.999834
 - x-request-id: 1e5361fc-9845-42f9-ab55-20de8ffdfc25-1751636440
    
2025-07-04T13:40:40.890Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 890 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=93, graphql;desc="admin/query/other", cfRequestDuration;dur=492.999792
 - x-request-id: ce4e5153-afe4-4f38-b055-c41f93fb213b-1751636440
    
2025-07-04T13:40:40.913Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 914 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=90, graphql;desc="admin/query/other", cfRequestDuration;dur=503.000021
 - x-request-id: 64f7ba17-c1cb-4fdf-bafa-3b7ae47a8ad3-1751636440
    
2025-07-04T13:40:40.945Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 945 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=83, graphql;desc="admin/query/other", cfRequestDuration;dur=551.999807
 - x-request-id: 95891206-fad9-44db-bc65-97012d70cbb6-1751636440
    
2025-07-04T13:40:41.047Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 1047 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=75, graphql;desc="admin/query/other", cfRequestDuration;dur=557.999849
 - x-request-id: d6e370cc-21ed-407c-adcb-56285585a243-1751636440
    
2025-07-04T13:40:41.051Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 1051 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=148, graphql;desc="admin/query/other", cfRequestDuration;dur=565.000057
 - x-request-id: 8f6093d5-f674-4753-bec8-cd750c854bf1-1751636440
    
2025-07-04T13:40:41.073Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 1073 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=109, graphql;desc="admin/query/other", cfRequestDuration;dur=600.999832
 - x-request-id: abad3918-70f9-439c-8c90-14bbe9445640-1751636440
    
2025-07-04T13:40:41.114Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 1114 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=93, graphql;desc="admin/query/other", cfRequestDuration;dur=526.999950
 - x-request-id: cd8569f2-870a-4a9a-b6c3-13694082419c-1751636440
    
2025-07-04T13:40:41.159Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 1159 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=69, graphql;desc="admin/query/other", cfRequestDuration;dur=519.999981
 - x-request-id: 0ca954c8-3a14-42c8-9cb6-267e1e8626f5-1751636440
    
2025-07-04T13:40:41.234Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 1235 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=94, graphql;desc="admin/query/other", cfRequestDuration;dur=552.000046
 - x-request-id: 75454e43-761b-4cbe-abae-e86dd0cca341-1751636440
    
2025-07-04T13:40:41.280Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 1281 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=76, graphql;desc="admin/query/other", cfRequestDuration;dur=550.999880
 - x-request-id: 27544746-3455-4941-a7fb-5ddba50c313c-1751636441
    
2025-07-04T13:40:41.311Z: Request to https://miye-care.myshopify.com/admin/api/2025-07/graphql.json completed in 1312 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=73, graphql;desc="admin/query/other", cfRequestDuration;dur=528.999805
 - x-request-id: 6d3a7860-217b-406d-970a-7ec95caeb3fb-1751636441
    
2025-07-04T13:40:41.312Z: File-writing some content to file at .shopify/metafields.json...
2025-07-04T13:40:41.321Z: Running system process:
  · Command: npm prefix
  · Working directory: /home/maxdesign/shopify/stores/Miye-Care

2025-07-04T13:40:41.408Z: Obtaining the dependency manager in directory /home/maxdesign...
AggregateError [ETIMEDOUT]: 
    at internalConnectMultiple (node:net:1134:18)
    at internalConnectMultiple (node:net:1210:5)
    at Timeout.internalConnectMultipleTimeout (node:net:1742:5)
    at listOnTimeout (node:internal/timers:590:11)
    at process.processTimers (node:internal/timers:523:7)
```
</details>


comment #6 by christtigroup, 2025-07-11, 19:59:24
Any new updates to resolving this? I keep hoping back and forth from my mac to my hotspot in order to sync my themes to my store. Slight inconvenience. 

comment #7 by gabrieljadeau, 2025-07-14, 09:01:56
Guys ..  When can we have it fixed ? it's getting impossible to work, it costs me 15 minutes to start a project and be able to work ! 

Can we have a deadline on this one ?

comment #8 by karreiro, 2025-07-17, 12:06:56
Thank you for reporting these issues, everyone!

The connection problems have been resolved through a combination of https://github.com/Shopify/cli/pull/6112 and https://github.com/Shopify/cli/pull/6125.

The fix will be available in the next release, but you can access it right away by installing this version:

```bash
pnpm i -g @shopify/cli@0.0.0-snapshot-20250717120134
```

If you’re still experiencing any network issues, please feel free to reach out to me directly here or on Partners Slack.

Thanks again for sharing the details and for your patience.


comment #9 by gabrieljadeau, 2025-07-17, 12:15:01
Hi @karreiro ,

Just tried it ... and it's not working !! Maybe you should ask people to test first before clausing the issue. What should I do, reopen a new one ??? 🙂‍↕️

➜  shopify-louyetu git:(master) ✗ shopify theme dev --store=louyetu-paris

<details>
    <summary>Verbose output</summary>
    ```
╭─ error ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                            │
│  request to https://louyetu-paris.myshopify.com/admin/api/2025-07/graphql.json failed, reason: Client network socket disconnected before   │
│  secure TLS connection was established                                                                                                     │
│                                                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

➜  shopify-louyetu git:(master) ✗ 
➜  shopify-louyetu git:(master) ✗ 
➜  shopify-louyetu git:(master) ✗ shopify --version
@shopify/cli/0.0.0-snapshot-20250717120134 darwin-arm64 node-v22.14.0
    ```
</details>

comment #10 by gabrieljadeau, 2025-07-17, 12:17:15
Please see the verbose bellow ...

<details>
    <summary>Verbose output</summary>
    ```
    ➜  shopify-louyetu git:(master) ✗ shopify theme dev --store=louyetu-paris --verbose
2025-07-17T12:16:40.986Z: Running command theme dev
2025-07-17T12:16:40.988Z: Running system process in background:
  · Command: /Users/gabrieljadeau/.nvm/versions/node/v22.14.0/bin/node /Users/gabrieljadeau/.nvm/versions/node/v22.14.0/bin/shopify notifications list --ignore-errors
  · Working directory: /Users/gabrieljadeau/Sites/shopify-louyetu

2025-07-17T12:16:40.993Z: Notifications to show: 0
2025-07-17T12:16:41.001Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-17T12:16:41.001Z: Ensuring that the user is authenticated with the Admin API with the following scopes for the store louyetu-paris.myshopify.com:
[]

2025-07-17T12:16:41.002Z: Getting session store...
2025-07-17T12:16:41.003Z: Validating existing session against the scopes:
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
  "adminApi": {
    "scopes": [],
    "storeFqdn": "louyetu-paris.myshopify.com"
  }
}

2025-07-17T12:16:41.003Z: - Token validation -> It's expired: false
2025-07-17T12:16:41.003Z: Getting development theme...
2025-07-17T12:16:41.005Z: Sending "Admin" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://louyetu-paris.myshopify.com/admin/api/unstable/graphql.json
2025-07-17T12:16:41.187Z: Request to https://louyetu-paris.myshopify.com/admin/api/unstable/graphql.json completed in 182 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=56, graphql;desc="admin/query/other", cfRequestDuration;dur=102.999926
 - x-request-id: 1962fe6d-9e40-4f4f-9817-621c5d050f1c-1752754601
    
2025-07-17T12:16:41.188Z: Sending "Admin" GraphQL request:
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
  "id": "gid://shopify/OnlineStoreTheme/180069990778"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://louyetu-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-17T12:16:41.402Z: Request to https://louyetu-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 214 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=72, graphql;desc="admin/query/other", cfRequestDuration;dur=151.000023
 - x-request-id: eb39d409-6665-45a0-a699-62e5646f16f8-1752754601
    
2025-07-17T12:16:41.409Z: Sending "Admin" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://louyetu-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-17T12:16:41.642Z: Request to https://louyetu-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 233 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=65, graphql;desc="admin/query/other", cfRequestDuration;dur=170.000076
 - x-request-id: 3ad8205b-8e58-4e34-b575-1015cf52167b-1752754601
    
2025-07-17T12:16:41.643Z: Getting storefront password for shop louyetu-paris.myshopify.com...
2025-07-17T12:16:41.643Z: Sending POST request to URL https://louyetu-paris.myshopify.com/password
With request headers:
 - cache-control: no-cache
 - content-type: application/x-www-form-urlencoded

2025-07-17T12:16:41.794Z: Request to https://louyetu-paris.myshopify.com/password completed in 151 ms
With response headers:
 - content-type: text/html; charset=utf-8
 - server-timing: processing;dur=19, db;dur=6, db_async;dur=1.148, asn;desc="3352", edge;desc="MAD", country;desc="ES", pageType;desc="password", servedBy;desc="b7vc", requestID;desc="1dc39ec5-aa43-435e-b732-9ed158b328c8-1752754601", _y;desc="00000000-0000-0000-5000-000000000000", _s;desc="00000000-0000-0000-5000-000000000000", cfRequestDuration;dur=66.999912
 - x-request-id: 1dc39ec5-aa43-435e-b732-9ed158b328c8-1752754601
    
2025-07-17T12:16:41.794Z: Setting storefront password for shop louyetu-paris.myshopify.com...
2025-07-17T12:16:41.812Z: Port 9292 is free
2025-07-17T12:16:41.812Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-17T12:16:41.812Z: Ensuring that the user is authenticated with the Admin API with the following scopes for the store louyetu-paris.myshopify.com:
[]

2025-07-17T12:16:41.812Z: Getting session store...
2025-07-17T12:16:41.813Z: Validating existing session against the scopes:
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
  "adminApi": {
    "scopes": [],
    "storeFqdn": "louyetu-paris.myshopify.com"
  }
}

2025-07-17T12:16:41.813Z: - Token validation -> It's expired: false
2025-07-17T12:16:41.813Z: Ensuring that the user is authenticated with the Storefront API with the following scopes:
[]

2025-07-17T12:16:41.813Z: Getting session store...
2025-07-17T12:16:41.813Z: Validating existing session against the scopes:
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
  "storefrontRendererApi": {
    "scopes": []
  }
}

2025-07-17T12:16:41.813Z: - Token validation -> It's expired: false
2025-07-17T12:16:41.814Z: Sending HEAD request to URL https://louyetu-paris.myshopify.com/?preview_theme_id=180069990778&_fd=0&pb=0
With request headers:
 - X-Shopify-Shop: louyetu-paris.myshopify.com
 - User-Agent: Shopify CLI; v=3.82.0

2025-07-17T12:16:41.823Z: Reading the content of file at assets/Inter-VariableFont.otf...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/Inter-VariableFont.ttf...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/Inter-VariableFont.woff...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/Inter-VariableFont.woff2...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/KeplerStd-LightCnDisp.otf...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/KeplerStd-LightCnDisp.ttf...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/KeplerStd-LightCnDisp.woff...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/KeplerStd-LightCnDisp.woff2...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/Louize-Italic.eot...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/Louize-Italic.svg...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/Louize-Italic.ttf...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/Louize-Italic.woff2...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/Louize-Italic.woff...
2025-07-17T12:16:41.823Z: Reading the content of file at assets/Louize-italic.otf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/Louize-regular.otf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/Louize.eot...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/Louize.ttf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/Louize.woff...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/Louize.woff2...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-55Rg.eot...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/Louize.svg...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-55Rg.otf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-55Rg.svg...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-55Rg.woff...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-55Rg.ttf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-56It.eot...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-55Rg.woff2...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-56It.otf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-56It.svg...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-56It.ttf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-56It.woff...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-56It.woff2...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-65Md.eot...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-65Md.otf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-65Md.svg...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-65Md.ttf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-65Md.woff...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NHaasGroteskTXPro-65Md.woff2...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NotoSerifDisplayCondensed-Regular.eot...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NotoSerifDisplayCondensed-Regular.svg...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NotoSerifDisplayCondensed-Regular.ttf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NotoSerifDisplayCondensed-Regular.woff...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/NotoSerifDisplayCondensed-Regular.woff2...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/Tesla.otf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/Tesla.ttf...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/Tesla.woff...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/Tesla.woff2...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/_ui-kit.css...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/arrow-left.svg.liquid...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/arrow-right.svg.liquid...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/astro-aquarius.png...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/astro-balance.png...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/astro-belier.png...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/astro-cancer.png...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/astro-capricorne.png...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/astro-gemini.png...
2025-07-17T12:16:41.824Z: Reading the content of file at assets/astro-leo.png...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/astro-piscis.png...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/astro-sagittaire.png...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/astro-scorpio.png...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/astro-taurus.png...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/astro-virgo.png...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/color-links.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-accordion.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-accordion.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-cart.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-cart.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-custom-contact.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-custom-contact.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-customer-account-menu.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-customer-account-menu.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-customer-information.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-customer-account.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-customer-register.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-gallery-swiper.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-gallery-swiper.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-gift-box-item.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-gift-box-item.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-gift-card.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-google-autocomplete.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-intl-tel-input.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-klaviyo-backinstock.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-klaviyo-subscription.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-minicart-login.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-loader.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-klaviyo-backinstock.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-pair-unit.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-minicart.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-product-engraving.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-product-engraving.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-product-loveletter.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-product-loveletter.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-selectric.css...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-selectric.js...
2025-07-17T12:16:41.825Z: Reading the content of file at assets/component-size-guide.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/component-size-guide.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/component-sort-by-popover.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/component-store-notification.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/component-store-notification.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/component-swiper.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/component-swiper.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/component-view-switch.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/component-zoom-indicator.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/component-view-switch.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/component-zoom-indicator.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/custom.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/custom.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/flags.png...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/flickity.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/image-uploader.min.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/flags@2x.png...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/intl-tel-input.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/intl-tel-input.min.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/iu.svg...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/iu.ttf...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/iu.woff...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/image-uploader.min.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/jquery.min.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/iu.eot...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/main-search.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/main.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/notifications.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/photoswipe.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/section-gallery-carousel.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/section-gallery-grid.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/made-in-fr.png...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/selectric.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/selectric.min.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/swiper.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/swiper.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/theme.css...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/theme.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/thumbs.svg...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/vendor.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/wetrust.js...
2025-07-17T12:16:41.826Z: Reading the content of file at assets/wt-script.js...
2025-07-17T12:16:41.826Z: Reading the content of file at config/settings_data.json...
2025-07-17T12:16:41.826Z: Reading the content of file at config/settings_schema.json...
2025-07-17T12:16:41.827Z: Reading the content of file at layout/theme.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/ar.json...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/de.json...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/en.default.json...
2025-07-17T12:16:41.827Z: Reading the content of file at assets/zoom-cursor.svg.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/es.json...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/fi.json...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/fr.json...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/it.json...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/ja.json...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/nb.json...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/pl.json...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/pt-BR.json...
2025-07-17T12:16:41.827Z: Reading the content of file at locales/sv.json...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/announcement-bar.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/apps.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/banner-accordion.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/blog-post-banner.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/blog-post-comments.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/blog-post-prev-next.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/blog-posts.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/cart-recommendations.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/collection-banner.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/collection-carousel.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/collection-list.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/contact-form.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/custom-html.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/custom-liquid.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/faq.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/featured-collections.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/featured-product.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/footer-group.json...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/footer-logo.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/footer-menu.liquid...
2025-07-17T12:16:41.827Z: Reading the content of file at sections/footer.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/gallery-carousel.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/gallery-grid.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/gallery.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/header-group.json...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/header.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/image-text-blocks.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/image-with-text-block.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/image-with-text-half.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/image-with-text-overlay.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/image-with-text.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/logo-list.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/lookbook.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/main-article.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/main-blog.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/main-cart.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/main-collection.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/main-customers-account.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/main-customers-activate-account.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/main-customers-addresses.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/main-customers-login.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/main-customers-order.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/main-customers-register.liquid...
2025-07-17T12:16:41.828Z: Reading the content of file at sections/main-customers-reset-password.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/main-gift-card.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/main-list-collections.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/main-login.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/main-not-found.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/main-page.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/main-password.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/main-product.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/main-search.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/mini-cart.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/multi-column.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/newsletter-inline-klaviyo.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/newsletter-inline.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/newsletter-klaviyo.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/newsletter-popup.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/newsletter.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/overlay-group.json...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/predictive-search-compatibility.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/predictive-search.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/press-slider.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/privacy-banner.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/press.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/product-accordions.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/product-bundle.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/product-content.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/product-recommendations-carousel.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/product-recommendations.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/product-reviews.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/promotion-blocks.liquid...
2025-07-17T12:16:41.829Z: Reading the content of file at sections/recently-viewed-products.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at sections/rich-text.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at sections/shop-the-look-mobile.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at sections/shop-the-look.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at sections/slideshow.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at sections/store-availability.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at sections/testimonials.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at sections/text-with-icons.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at sections/timeline.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at sections/transparent-header.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at sections/video-with-text-blocks.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/article-item.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/astro-dates.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at sections/video.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/astro-icons.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/bundle-item.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/collection-submenu.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/color-count.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/color-links.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/color-swatch-style.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/cookie-gdpr-popup-translations.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/css-variables.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/customer-account-menu.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/customer-addresses.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/customer-gift-cards.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/customer-information.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/customer-links.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/customer-order-detail.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/customer-orders.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/customer-returns.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/discount-code-update.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/customer-stock-alerts.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/facet-active-filters.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/desktop-menu.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/facet-filters.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/form-contact__incomplete-order.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/form-contact__jewel-damaged.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/form-contact__return.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/form-contact__standard.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/form-contact__information.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/gift-box-item.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/header-notification.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/form-login.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/icon.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/js-variables.liquid...
2025-07-17T12:16:41.830Z: Reading the content of file at snippets/klaviyo-popover.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/klaviyo-snippet.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/locale-selector.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/microdata-schema.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/minicart_switcher-component.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/mobile-menu.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/pagination.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/predictive-search.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/price.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-characteristics.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-form.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-item-placeholder.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-info.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-item.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-labels.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-loveletter.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-media.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-preorder-panel.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-rating.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-sticky-form.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-tags.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/product-usp.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/shipping_preorder_notification.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/size-guide.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/social-media.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/social-meta-tags.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at snippets/store-availability.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/404.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/article.bijoux_a_composer.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/article.grandes_vacances.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/article.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/article.plaque_argent.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/article.plein_soleil.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/article.poema.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/article.temps_des_fleurs.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/blog.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/cart.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/collection.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/gift_card.liquid...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/index.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/list-collections.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/page.contact.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/page.creatrice.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/page.conseils.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/page.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/page.faq.json...
2025-07-17T12:16:41.831Z: Reading the content of file at templates/page.equipe_produit.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.list-collections.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.lookbook-2.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.lookbook-3.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.lookbook-sept-2023.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.lookbook.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.marque.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.manifesto.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.meet_the_team.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.partenaires.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.q-a-2507.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.savoir_faire.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.size_chart.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.track-my-order.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.the-manifesto.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/page.vos_questions.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/password.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/product.bundle.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/product.love-letters.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/product.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/product.nac.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/product.pre-order.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/product.quick-buy-drawer.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/product.context.fr.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/product.quick-buy-popover.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/search.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/metaobject/email_css.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/metaobject/look.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/customers/account.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/metaobject/press.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/customers/activate_account.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/customers/addresses.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/customers/login.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/customers/order.json...
2025-07-17T12:16:41.832Z: Reading the content of file at templates/customers/register.json...
2025-07-17T12:16:41.833Z: Reading the content of file at templates/customers/reset_password.json...
2025-07-17T12:16:42.004Z: Request to https://louyetu-paris.myshopify.com/?preview_theme_id=180069990778&_fd=0&pb=0 completed in 190 ms
With response headers:
 - content-type: text/html; charset=utf-8
 - server-timing: processing;dur=18, db;dur=5, asn;desc="3352", edge;desc="MAD", country;desc="ES", theme;desc="180069990778", pageType;desc="index", servedBy;desc="r6kp", requestID;desc="a84765d1-a734-44bf-8802-fd6527d54753-1752754602", _y;desc="00000000-0000-0000-5000-000000000000", _s;desc="00000000-0000-0000-5000-000000000000", cfRequestDuration;dur=70.999861
 - x-request-id: a84765d1-a734-44bf-8802-fd6527d54753-1752754602
    
2025-07-17T12:16:42.005Z: Sending POST request to URL https://louyetu-paris.myshopify.com/password
With request headers:
 - X-Shopify-Shop: louyetu-paris.myshopify.com
 - User-Agent: Shopify CLI; v=3.82.0
 - Cookie: _shopify_essential=:AZgYUMBoAAH_D6i41RvVGryR57uTly-ypGkM0F-Az786H1V9TksFQHnWipNoN9Rp8vtXoXw8v44ZqFyfTO7NI0WK2Kto3djKDKtRBOlRLuYFsY3Wtq81c3eTw6KH:

2025-07-17T12:16:57.089Z: Request to https://louyetu-paris.myshopify.com/password completed in 15084 ms
With response headers:

    
╭─ error ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                            │
│  request to https://louyetu-paris.myshopify.com/password failed, reason: Client network socket disconnected before secure TLS connection   │
│  was established                                                                                                                           │
│                                                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-07-17T12:16:57.121Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/gabrieljadeau/Sites/shopify-louyetu

2025-07-17T12:16:57.245Z: Obtaining the dependency manager in directory ../.....
2025-07-17T12:16:57.591Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 182 ms
With response headers:
 - x-request-id: a89d7b9d-3499-4c96-bf86-69f56b45a6e0
    
2025-07-17T12:16:57.591Z: Analytics event sent: {
  "command": "theme dev",
  "time_start": 1752754600986,
  "time_end": 1752754617115,
  "total_time": 16129,
  "success": false,
  "cli_version": "3.82.0",
  "ruby_version": "",
  "node_version": "22.14.0",
  "is_employee": false,
  "uname": "darwin arm64",
  "env_ci": false,
  "env_plugin_installed_any_custom": false,
  "env_plugin_installed_shopify": "[\"@shopify/app\",\"@shopify/cli\",\"@shopify/plugin-cloudflare\"]",
  "env_shell": "zsh",
  "env_device_id": "600ae94c5c4f473631e33810cb3d79939d7707d9",
  "env_cloud": "localhost",
  "env_package_manager": "npm",
  "env_is_global": false,
  "env_auth_method": "device_auth",
  "env_is_wsl": false,
  "env_build_repository": "Shopify/cli",
  "cmd_app_warning_api_key_deprecation_displayed": false,
  "cmd_all_timing_network_ms": 16054,
  "cmd_all_timing_prompts_ms": 0,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "theme",
  "cmd_all_plugin": "@shopify/theme",
  "cmd_all_force": false,
  "cmd_all_verbose": true,
  "cmd_all_path_override": true,
  "cmd_all_path_override_hash": "f135ca0cc0b3f641f5ef5de94715cc0f173d0460",
  "cmd_all_last_graphql_request_id": "3ad8205b-8e58-4e34-b575-1015cf52167b-1752754601",
  "cmd_all_timing_active_ms": 74,
  "cmd_all_exit": "expected_error",
  "user_id": "ae9f7283-c904-45d8-9638-747273e416c9",
  "request_ids": [
    "1962fe6d-9e40-4f4f-9817-621c5d050f1c-1752754601",
    "eb39d409-6665-45a0-a699-62e5646f16f8-1752754601",
    "3ad8205b-8e58-4e34-b575-1015cf52167b-1752754601"
  ],
  "args": "--store=louyetu-paris --verbose",
  "error_message": "request to https://louyetu-paris.myshopify.com/password failed, reason: Client network socket disconnected before secure TLS connection was established",
  "env_plugin_installed_all": "[\"@shopify/app\",\"@shopify/cli\",\"@shopify/plugin-cloudflare\"]",
  "metadata": "{\"extraPublic\":{\"@shopify/app\":{\"cmd_app_warning_api_key_deprecation_displayed\":false}},\"extraSensitive\":{\"@shopify/app\":{}}}"
}
2025-07-17T12:16:57.603Z: Reporting handled error to Bugsnag: request to https://louyetu-paris.myshopify.com/password failed, reason: Client network socket disconnected before secure TLS connection was established
2025-07-17T12:16:57.627Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/gabrieljadeau/Sites/shopify-louyetu

2025-07-17T12:16:57.737Z: Obtaining the dependency manager in directory ../.....
    ```
</details>

comment #11 by karreiro, 2025-07-17, 13:22:39
👋 Hey @gabrieljadeau,

Thank you for your quick feedback and for sharing the `--verbose` output!

There's no need to open a new issue, we can continue here. We're currently reviewing your logs and your theme, and we'll post an update in this thread as soon as we have more information.

Thanks again for the details!

comment #12 by karreiro, 2025-07-18, 10:40:18
👋 Hey @gabrieljadeau,

Could you please share your feedback on this version?

```bash
pnpm i -g @shopify/cli@0.0.0-snapshot-20250718094441
```

We've been having trouble reproducing the error you're experiencing. So, your feedback, along with the extra logs we've added, will really help us narrow down the issue.

Thank you!

comment #13 by MaxDesignFR, 2025-07-18, 13:18:38
This issue is getting out of hand. New errors coming my way, I didn't even upgrade my version (3.79.2). I also tried on the new snapshot version, some other errors. Stuck! Loosing patience with this tool, it just has not once be stable for basic use... **Is this taken seriously?** Today I'm jobless because of it, tomorrow who knows.

I'm wondering if it's because I'm on a large project with many assets, anyways I can't seem to find a way to run local dev with any version (I used to be able). Theme preview link also broken (assets and snippets missing), so really no way out of this one.

One of the error I got on 3.79.2 (node 18):

<details>
<summary>Verbose output</summary>

```
tment.value\n                    endcase\n                  endif\n                endif\n              endif\n            -%}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = 0 %}<!-- -->{% if reploSelectedVariant.compare_at_price != blank %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploSelectedVariant.compare_at_price | minus: reploSelectedVariant.price | at_least: 0 | times: 100.0 | divided_by: reploSelectedVariant.compare_at_price | round %}<!-- -->{% endif %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<div data-rid=\"3e33de33-35fe-4377-9b2e-1d524583f211\" tabindex=\"0\" role=\"button\" class=\"r-3wqav1\" data-replo-product-container=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" data-replo-product-handle=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.handle}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"><product-form style=\"display:none\"><form id=\"product-form-{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" method=\"post\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" encType=\"multipart/form-data\" action=\"/cart/add\" data-type=\"add-to-cart-form\"><input type=\"hidden\" name=\"id\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{reploSelectedVariant.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/><input type=\"hidden\" name=\"quantity\" value=\"1\"/><input type=\"hidden\" name=\"selling_plan\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- if reploSelectedSellingPlan != blank -%}{{reploSelectedSellingPlan.id}}{%- endif -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/></form></product-form><div data-rid=\"fbbe34de-df28-4f44-9b7e-4ed4dc8236a5\" class=\"r-1mpddo7\"><picture data-rid=\"d3142973-6c0e-43a0-920e-29876fa7d278\" style=\"--replo-attributes-product-featured-image:{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-k1cg7v\"><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 820  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(max-width: 640px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1024  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1800  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-1q9wyug\" loading=\"lazy\"/></picture></div><div data-rid=\"957b0ef9-ea5d-4546-8313-c1a19abf2251\" class=\"r-1t9z0rt\"><div data-rid=\"22f41a95-057b-435c-a610-efd07877de2d\" class=\"r-1hv3zq0\"><div data-rid=\"1c1dd2f1-95fa-42f5-a096-a360409ed374\" class=\"r-b3etsn\"><div data-rid=\"1345cec2-2fc7-4b0d-9862-577da99e0b4a\" class=\"r-1tl33ne alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.title }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div></div><div data-rid=\"6e8bc39b-9c5f-46d9-9f94-acb4661c792a\" class=\"r-3ahe6n\"><div data-rid=\"e451734e-3106-4d93-b1a4-c915b55aabd8\" class=\"r-13zoknt\"><div data-rid=\"aef8c280-53e4-4f72-8a43-5ffa7e12b847\" class=\"r-tkc5vq\"><div data-rid=\"3f5a9e55-6e10-4cd6-bace-425ffa91b244\" class=\"r-1t3wmhi alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}ml{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div><div data-rid=\"eceb06ee-7dae-4be5-a498-bfc7ffc50ba5\" class=\"r-1eg4q9m\"><div data-rid=\"f6b9750d-6dcb-43d6-9f88-a98fa2cd27b2\" class=\"r-f0cd5i alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}made_in_france{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div></div><div data-rid=\"fb440d47-8823-40ec-a826-1d3768015813\" class=\"r-3lgm8x\"><div data-rid=\"a7652791-463d-4d29-822f-b4ec07848824\" class=\"r-1hp0s62\"><div data-rid=\"86c45cb5-197e-473e-972f-06d91d51c4b2\" class=\"r-14ja0os alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ reploSelectedSellingPlanPrice  | divided_by: 100.0 | round | times: 100.0 | money_without_trailing_zeros}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div><div data-rid=\"1b1b9ba2-c533-4afb-9a76-b8fe293a4368\" class=\"r-b1rhd6\"><div data-rid=\"0608cac0-cb36-4ec7-88ef-2c7d4beacc3d\" class=\"r-1xj1yl2\"><span style=\"display:contents\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-arrow-up-right\" style=\"fill: none;stroke: currentColor;width: var(--rsw, 100%);height: 100%\" role=\"presentation\"><line x1=\"7\" y1=\"17\" x2=\"17\" y2=\"7\"></line><polyline points=\"7 7 17 7 17 17\"></polyline></svg></span></div></div></div></div></div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign product = reploOriginalProductR2qr2 %}<!-- -->{% assign reploSelectedVariant = reploOriginalProductVariantR2qr2 %}<!-- -->{% assign reploSortedSellingPlans = reploOriginalSPGR2qr2 %}<!-- -->{% assign reploSelectedSellingPlan = reploOriginalSSPR2qr2 %}<!-- -->{% assign reploSelectedSellingPlanPrice = reploOriginalSSPPriceR2qr2 %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploOriginalComparePricePercentR2qr2 %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign reploOriginalProductR3qr2 = product %}<!-- -->{% capture productHandle %}gel-creme-jour{% endcapture %}<!-- -->{% assign product = all_products[productHandle] %}<!-- -->{% assign reploOriginalProductVariantR3qr2 = reploSelectedVariant %}<!-- -->{% assign reploSelectedVariant = blank %}<!-- -->{% assign reploOriginalSPGR3qr2 = reploSortedSellingPlans %}<!-- -->{% assign reploSortedSellingPlans = blank %}<!-- -->{% assign reploOriginalSSPR3qr2 = reploSelectedSellingPlan %}<!-- -->{% assign reploSelectedSellingPlan = blank %}<!-- -->{% assign reploOriginalSSPPriceR3qr2 = reploSelectedSellingPlanPrice %}<!-- -->{% assign reploSelectedSellingPlanPrice = blank %}<!-- -->{% assign reploOriginalComparePricePercentR3qr2 = reploCompareAtPriceDifferencePercentage %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = blank %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<!-- -->{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% capture reploVariantIdString %}null{% endcapture %}<!-- -->{% capture reploSellingPlanIdString %}null{% endcapture %}<!-- -->{% capture reploIdKey %}id{% endcapture %}<!-- -->{% capture reploPercentageKey %}percentage{% endcapture %}<!-- -->{% capture reploPriceKey %}price{% endcapture %}<!-- -->{% capture reploFixedAmountKey %}fixed_amount{% endcapture %}<!-- -->{% capture spKey %}selling_plan{% endcapture %}<!-- -->{%- liquid\n              assign reploVariantId = reploVariantIdString | times: 1\n              assign reploSelectedVariant = product.variants | where: reploIdKey, reploVariantId | first\n              if reploSelectedVariant == blank\n                assign reploSelectedVariant = product.selected_or_first_available_variant\n              endif\n              assign reploSelectedSellingPlanPrice = reploSelectedVariant.price\n              if product.selling_plan_groups[0]\n                assign reploAllSellingPlans = reploSelectedVariant.selling_plan_allocations | map: spKey\n                assign reploSortedSellingPlans = reploAllSellingPlans | sort: reploIdKey\n                if true\n                  assign reploSellingPlanId = reploSellingPlanIdString | times: 1\n                  assign reploSelectedSellingPlan = reploSortedSellingPlans | where: reploIdKey, reploSellingPlanId | first\n                  if reploSelectedSellingPlan.price_adjustments[0]\n                    assign adjustment = reploSelectedSellingPlan.price_adjustments[0]\n                    case adjustment.value_type\n                      when reploPercentageKey\n                        assign amountOff = 100 | minus: adjustment.value\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | times: amountOff | divided_by: 100\n                      when reploFixedAmountKey\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | minus: adjustment.value\n                      when reploPriceKey\n                        assign reploSelectedSellingPlanPrice = adjustment.value\n                    endcase\n                  endif\n                endif\n              endif\n            -%}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = 0 %}<!-- -->{% if reploSelectedVariant.compare_at_price != blank %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploSelectedVariant.compare_at_price | minus: reploSelectedVariant.price | at_least: 0 | times: 100.0 | divided_by: reploSelectedVariant.compare_at_price | round %}<!-- -->{% endif %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<div data-rid=\"3e33de33-35fe-4377-9b2e-1d524583f211\" tabindex=\"0\" role=\"button\" class=\"r-3wqav1\" data-replo-product-container=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" data-replo-product-handle=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.handle}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"><product-form style=\"display:none\"><form id=\"product-form-{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" method=\"post\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" encType=\"multipart/form-data\" action=\"/cart/add\" data-type=\"add-to-cart-form\"><input type=\"hidden\" name=\"id\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{reploSelectedVariant.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/><input type=\"hidden\" name=\"quantity\" value=\"1\"/><input type=\"hidden\" name=\"selling_plan\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- if reploSelectedSellingPlan != blank -%}{{reploSelectedSellingPlan.id}}{%- endif -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/></form></product-form><div data-rid=\"fbbe34de-df28-4f44-9b7e-4ed4dc8236a5\" class=\"r-1mpddo7\"><picture data-rid=\"d3142973-6c0e-43a0-920e-29876fa7d278\" style=\"--replo-attributes-product-featured-image:{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-k1cg7v\"><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 820  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(max-width: 640px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1024  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1800  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-1q9wyug\" loading=\"lazy\"/></picture></div><div data-rid=\"957b0ef9-ea5d-4546-8313-c1a19abf2251\" class=\"r-1t9z0rt\"><div data-rid=\"22f41a95-057b-435c-a610-efd07877de2d\" class=\"r-1hv3zq0\"><div data-rid=\"1c1dd2f1-95fa-42f5-a096-a360409ed374\" class=\"r-b3etsn\"><div data-rid=\"1345cec2-2fc7-4b0d-9862-577da99e0b4a\" class=\"r-1tl33ne alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.title }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div></div><div data-rid=\"6e8bc39b-9c5f-46d9-9f94-acb4661c792a\" class=\"r-3ahe6n\"><div data-rid=\"e451734e-3106-4d93-b1a4-c915b55aabd8\" class=\"r-13zoknt\"><div data-rid=\"aef8c280-53e4-4f72-8a43-5ffa7e12b847\" class=\"r-tkc5vq\"><div data-rid=\"3f5a9e55-6e10-4cd6-bace-425ffa91b244\" class=\"r-1t3wmhi alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}ml{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div><div data-rid=\"eceb06ee-7dae-4be5-a498-bfc7ffc50ba5\" class=\"r-1eg4q9m\"><div data-rid=\"f6b9750d-6dcb-43d6-9f88-a98fa2cd27b2\" class=\"r-f0cd5i alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}made_in_france{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div></div><div data-rid=\"fb440d47-8823-40ec-a826-1d3768015813\" class=\"r-3lgm8x\"><div data-rid=\"a7652791-463d-4d29-822f-b4ec07848824\" class=\"r-1hp0s62\"><div data-rid=\"86c45cb5-197e-473e-972f-06d91d51c4b2\" class=\"r-14ja0os alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ reploSelectedSellingPlanPrice  | divided_by: 100.0 | round | times: 100.0 | money_without_trailing_zeros}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div><div data-rid=\"1b1b9ba2-c533-4afb-9a76-b8fe293a4368\" class=\"r-b1rhd6\"><div data-rid=\"0608cac0-cb36-4ec7-88ef-2c7d4beacc3d\" class=\"r-1xj1yl2\"><span style=\"display:contents\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-arrow-up-right\" style=\"fill: none;stroke: currentColor;width: var(--rsw, 100%);height: 100%\" role=\"presentation\"><line x1=\"7\" y1=\"17\" x2=\"17\" y2=\"7\"></line><polyline points=\"7 7 17 7 17 17\"></polyline></svg></span></div></div></div></div></div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign product = reploOriginalProductR3qr2 %}<!-- -->{% assign reploSelectedVariant = reploOriginalProductVariantR3qr2 %}<!-- -->{% assign reploSortedSellingPlans = reploOriginalSPGR3qr2 %}<!-- -->{% assign reploSelectedSellingPlan = reploOriginalSSPR3qr2 %}<!-- -->{% assign reploSelectedSellingPlanPrice = reploOriginalSSPPriceR3qr2 %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploOriginalComparePricePercentR3qr2 %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign reploOriginalProductR4qr2 = product %}<!-- -->{% capture productHandle %}gel-creme-nuit{% endcapture %}<!-- -->{% assign product = all_products[productHandle] %}<!-- -->{% assign reploOriginalProductVariantR4qr2 = reploSelectedVariant %}<!-- -->{% assign reploSelectedVariant = blank %}<!-- -->{% assign reploOriginalSPGR4qr2 = reploSortedSellingPlans %}<!-- -->{% assign reploSortedSellingPlans = blank %}<!-- -->{% assign reploOriginalSSPR4qr2 = reploSelectedSellingPlan %}<!-- -->{% assign reploSelectedSellingPlan = blank %}<!-- -->{% assign reploOriginalSSPPriceR4qr2 = reploSelectedSellingPlanPrice %}<!-- -->{% assign reploSelectedSellingPlanPrice = blank %}<!-- -->{% assign reploOriginalComparePricePercentR4qr2 = reploCompareAtPriceDifferencePercentage %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = blank %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<!-- -->{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% capture reploVariantIdString %}null{% endcapture %}<!-- -->{% capture reploSellingPlanIdString %}null{% endcapture %}<!-- -->{% capture reploIdKey %}id{% endcapture %}<!-- -->{% capture reploPercentageKey %}percentage{% endcapture %}<!-- -->{% capture reploPriceKey %}price{% endcapture %}<!-- -->{% capture reploFixedAmountKey %}fixed_amount{% endcapture %}<!-- -->{% capture spKey %}selling_plan{% endcapture %}<!-- -->{%- liquid\n              assign reploVariantId = reploVariantIdString | times: 1\n              assign reploSelectedVariant = product.variants | where: reploIdKey, reploVariantId | first\n              if reploSelectedVariant == blank\n                assign reploSelectedVariant = product.selected_or_first_available_variant\n              endif\n              assign reploSelectedSellingPlanPrice = reploSelectedVariant.price\n              if product.selling_plan_groups[0]\n                assign reploAllSellingPlans = reploSelectedVariant.selling_plan_allocations | map: spKey\n                assign reploSortedSellingPlans = reploAllSellingPlans | sort: reploIdKey\n                if true\n                  assign reploSellingPlanId = reploSellingPlanIdString | times: 1\n                  assign reploSelectedSellingPlan = reploSortedSellingPlans | where: reploIdKey, reploSellingPlanId | first\n                  if reploSelectedSellingPlan.price_adjustments[0]\n                    assign adjustment = reploSelectedSellingPlan.price_adjustments[0]\n                    case adjustment.value_type\n                      when reploPercentageKey\n                        assign amountOff = 100 | minus: adjustment.value\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | times: amountOff | divided_by: 100\n                      when reploFixedAmountKey\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | minus: adjustment.value\n                      when reploPriceKey\n                        assign reploSelectedSellingPlanPrice = adjustment.value\n                    endcase\n                  endif\n                endif\n              endif\n            -%}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = 0 %}<!-- -->{% if reploSelectedVariant.compare_at_price != blank %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploSelectedVariant.compare_at_price | minus: reploSelectedVariant.price | at_least: 0 | times: 100.0 | divided_by: reploSelectedVariant.compare_at_price | round %}<!-- -->{% endif %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<div data-rid=\"3e33de33-35fe-4377-9b2e-1d524583f211\" tabindex=\"0\" role=\"button\" class=\"r-3wqav1\" data-replo-product-container=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" data-replo-product-handle=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.handle}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"><product-form style=\"display:none\"><form id=\"product-form-{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" method=\"post\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" encType=\"multipart/form-data\" action=\"/cart/add\" data-type=\"add-to-cart-form\"><input type=\"hidden\" name=\"id\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{reploSelectedVariant.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/><input type=\"hidden\" name=\"quantity\" value=\"1\"/><input type=\"hidden\" name=\"selling_plan\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- if reploSelectedSellingPlan != blank -%}{{reploSelectedSellingPlan.id}}{%- endif -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/></form></product-form><div data-rid=\"fbbe34de-df28-4f44-9b7e-4ed4dc8236a5\" class=\"r-1mpddo7\"><picture data-rid=\"d3142973-6c0e-43a0-920e-29876fa7d278\" style=\"--replo-attributes-product-featured-image:{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-k1cg7v\"><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 820  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(max-width: 640px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1024  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1800  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-1q9wyug\" loading=\"lazy\"/></picture></div><div data-rid=\"957b0ef9-ea5d-4546-8313-c1a19abf2251\" class=\"r-1t9z0rt\"><div data-rid=\"22f41a95-057b-435c-a610-efd07877de2d\" class=\"r-1hv3zq0\"><div data-rid=\"1c1dd2f1-95fa-42f5-a096-a360409ed374\" class=\"r-b3etsn\"><div data-rid=\"1345cec2-2fc7-4b0d-9862-577da99e0b4a\" class=\"r-1tl33ne alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.title }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div></div><div data-rid=\"6e8bc39b-9c5f-46d9-9f94-acb4661c792a\" class=\"r-3ahe6n\"><div data-rid=\"e451734e-3106-4d93-b1a4-c915b55aabd8\" class=\"r-13zoknt\"><div data-rid=\"aef8c280-53e4-4f72-8a43-5ffa7e12b847\" class=\"r-tkc5vq\"><div data-rid=\"3f5a9e55-6e10-4cd6-bace-425ffa91b244\" class=\"r-1t3wmhi alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}ml{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div><div data-rid=\"eceb06ee-7dae-4be5-a498-bfc7ffc50ba5\" class=\"r-1eg4q9m\"><div data-rid=\"f6b9750d-6dcb-43d6-9f88-a98fa2cd27b2\" class=\"r-f0cd5i alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}made_in_france{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div></div><div data-rid=\"fb440d47-8823-40ec-a826-1d3768015813\" class=\"r-3lgm8x\"><div data-rid=\"a7652791-463d-4d29-822f-b4ec07848824\" class=\"r-1hp0s62\"><div data-rid=\"86c45cb5-197e-473e-972f-06d91d51c4b2\" class=\"r-14ja0os alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ reploSelectedSellingPlanPrice  | divided_by: 100.0 | round | times: 100.0 | money_without_trailing_zeros}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div><div data-rid=\"1b1b9ba2-c533-4afb-9a76-b8fe293a4368\" class=\"r-b1rhd6\"><div data-rid=\"0608cac0-cb36-4ec7-88ef-2c7d4beacc3d\" class=\"r-1xj1yl2\"><span style=\"display:contents\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-arrow-up-right\" style=\"fill: none;stroke: currentColor;width: var(--rsw, 100%);height: 100%\" role=\"presentation\"><line x1=\"7\" y1=\"17\" x2=\"17\" y2=\"7\"></line><polyline points=\"7 7 17 7 17 17\"></polyline></svg></span></div></div></div></div></div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign product = reploOriginalProductR4qr2 %}<!-- -->{% assign reploSelectedVariant = reploOriginalProductVariantR4qr2 %}<!-- -->{% assign reploSortedSellingPlans = reploOriginalSPGR4qr2 %}<!-- -->{% assign reploSelectedSellingPlan = reploOriginalSSPR4qr2 %}<!-- -->{% assign reploSelectedSellingPlanPrice = reploOriginalSSPPriceR4qr2 %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploOriginalComparePricePercentR4qr2 %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div></div></div></div></div></div></div></div></div></div><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Medium\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Medium\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Medium.woff?v=1749641057\") format(\"woff\");\n        }\n      </style><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Light\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Light\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Light.woff?v=1749641057\") format(\"woff\");\n        }\n      </style><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Regular\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Regular\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Regular.woff?v=1749641058\") format(\"woff\");\n        }\n      </style><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Bold\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Bold\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Bold.woff?v=1749641058\") format(\"woff\");\n        }\n      </style></div>\n{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}\n  <script type=\"application/json\" id=\"replo-deps-products\">\n    [{\"id\":\"10094474395991\",\"handle\": \"granite-demaquillant\",\"data\":{{ all_products['granite-demaquillant'] | json }}},{\"id\":\"10094475477335\",\"handle\": \"mousse-nettoyante\",\"data\":{{ all_products['mousse-nettoyante'] | json }}},{\"id\":\"10094478000471\",\"handle\": \"gel-creme-jour\",\"data\":{{ all_products['gel-creme-jour'] | json }}},{\"id\":\"10094478688599\",\"handle\": \"gel-creme-nuit\",\"data\":{{ all_products['gel-creme-nuit'] | json }}}]\n  </script>\n  {%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\n    <script type=\"application/json\" id=\"replo-deps-products-metafields\">\n      {%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture replo_double_tick -%}\"{%- endcapture -%}{\"10094474395991\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['granite-demaquillant'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['granite-demaquillant'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}},\"10094475477335\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['mousse-nettoyante'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['mousse-nettoyante'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}},\"10094478000471\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-jour'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-jour'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}},\"10094478688599\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-nuit'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-nuit'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\n    </script>\n  \n    <script type=\"application/json\" id=\"replo-deps-variant-metafields\">\n    {%- capture replo_double_tick -%}\"{%- endcapture -%}{}\n    </script>\n  {%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<script type=\"application/json\" id=\"replo-deps-shopify-store\">{ \"shop\": { \"moneyFormat\": {{ shop.money_format | json }}, \"moneyWithCurrencyFormat\": {{ shop.money_with_currency_format | json }} } }</script>{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div>\n\n{% schema %}\n{\n  \"name\": \"[collection]sensibilité\",\n  \"presets\": [\n    {\n      \"name\": \"[collection]sensibilité\"\n    }\n  ],\n  \"settings\": [\n    {\n      \"type\": \"header\",\n      \"content\": \"Created in Replo\",\n      \"info\": \"This Section was created using [Replo](https://www.replo.app/). If you would like to make any changes to the structure or design of this Section, you can [edit it in Replo](https://dashboard.replo.app/editor/07bd1984-3d87-4861-82a3-4f94a264d106/0bcad7f9-4a39-4fc3-b06f-45951fdf9431).\"\n    }\n  ]\n}\n{% endschema %}\n    "
      }
    }
  ]
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
╭─ success ────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                          │
│  Preview your theme (t)                                                                                  │
│    • http://127.0.0.1:9292                                                                               │
│                                                                                                          │
│  Next steps                                                                                              │
│    • Share your theme preview (p) https://aloe-paris.myshopify.com/?preview_theme_id=184608981335        │
│    • Customize your theme at the theme editor (e)                                                        │
│    • Preview your gift cards (g)                                                                         │
│                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-07-18T12:46:53.231Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-18T12:46:53.232Z: Ensuring that the user is authenticated with the Admin API with the following scopes for the store aloe-paris.myshopify.com:
[]

2025-07-18T12:46:53.232Z: Getting session store...
2025-07-18T12:46:53.234Z: Validating existing session against the scopes:
[
  "openid",
  "https://api.shopify.com/auth/shop.admin.graphql",
  "https://api.shopify.com/auth/shop.admin.themes",
  "https://api.shopify.com/auth/partners.collaborator-relationships.readonly",
  "https://api.shopify.com/auth/shop.storefront-renderer.devtools",
  "https://api.shopify.com/auth/partners.app.cli.access",
  "https://api.shopify.com/auth/destinations.readonly",
  "https://api.shopify.com/auth/organization.store-management",
  "https://api.shopify.com/auth/organization.apps.manage"
]
For applications:
{
  "adminApi": {
    "scopes": [],
    "storeFqdn": "aloe-paris.myshopify.com"
  }
}

2025-07-18T12:46:53.234Z: - Token validation -> It's expired: false
2025-07-18T12:46:54.214Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "ARTICLE"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:54.214Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "BLOG"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:54.214Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COLLECTION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:54.215Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COMPANY"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:54.215Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COMPANY_LOCATION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:54.215Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "LOCATION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:54.216Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "MARKET"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:54.216Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "ORDER"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:54.216Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PAGE"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:54.217Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PRODUCT"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:54.217Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PRODUCTVARIANT"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:54.217Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "SHOP"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:46:56.240Z: Sending "Admin" GraphQL request:
  query getThemeFileChecksums($id: ID!, $after: String) {
  theme(id: $id) {
    files(first: 250, after: $after) {
      nodes {
        filename
        size
        checksumMd5
        __typename
      }
      userErrors {
        filename
        code
        __typename
      }
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "id": "gid://shopify/OnlineStoreTheme/184608981335",
  "after": null
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:47:00.565Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 6347 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=68, graphql;desc="admin/query/other", cfRequestDuration;dur=526.999950
 - x-request-id: 81b9247b-48ce-4e9b-9cb2-cc57eca28de7-1752842820
    
2025-07-18T12:47:00.696Z: → Rendering https://aloe-paris.myshopify.com/?_fd=0&pb=0 (with config/settings_data.json,config/settings_schema.json,sections/footer-group.json,sections/header-group.json,sections/maxdesign.json,sections/overlay-group.json,sections/replo-collection-best-seller.liquid,sections/replo-collection-contour.liquid,sections/replo-collection-deshydratati.liquid,sections/replo-collection-nouveautes.liquid,sections/replo-collectionimperfections.liquid,sections/replo-collectionroutine-compl.liquid,sections/replo-collectiondemaquillants.liquid,sections/replo-collectionhydratant.liquid,sections/replo-collectionroutine-minim.liquid,sections/replo-gua-sha-full-page.liquid,sections/replo-gua-sha.liquid,sections/replo-home-page-full.liquid,sections/replo-home-page.liquid,sections/replo-collectionsensibilite.liquid,snippets/reploChunk.060a43f3-16b2-464c-ada3-7e3999e7a8ca.2.liquid,snippets/reploChunk.0bbef5f6-ce6b-4da8-89ab-d8a169129126.1.liquid,snippets/reploChunk.0e305fb3-17a1-4655-a0a5-42c5f34ee925.1.liquid,snippets/reploChunk.0eb96234-9035-46e2-9577-6dde534c7491.0.liquid,snippets/reploChunk.0eb96234-9035-46e2-9577-6dde534c7491.2.liquid,snippets/reploChunk.290ae22c-aed0-4225-9028-66727faef951.0.liquid,snippets/reploChunk.14c26584-65b6-475b-8c33-755bc834ca30.0.liquid,snippets/reploChunk.14c26584-65b6-475b-8c33-755bc834ca30.1.liquid,snippets/reploChunk.290ae22c-aed0-4225-9028-66727faef951.1.liquid,snippets/reploChunk.3180adf2-4979-4b40-9fdc-6ecf92cfda14.0.liquid,snippets/reploChunk.3180adf2-4979-4b40-9fdc-6ecf92cfda14.1.liquid,snippets/reploChunk.3180adf2-4979-4b40-9fdc-6ecf92cfda14.2.liquid,snippets/reploChunk.3180adf2-4979-4b40-9fdc-6ecf92cfda14.3.liquid,snippets/reploChunk.32e885b4-7241-49a0-a967-44507d611922.2.liquid,snippets/reploChunk.32e885b4-7241-49a0-a967-44507d611922.0.liquid,snippets/reploChunk.4785765d-2ec6-46cc-a50f-6c1fccabefd2.1.liquid,snippets/reploChunk.49b05d93-ef36-4211-8229-47ae5d6bca43.2.liquid,snippets/reploChunk.49f797d7-0af0-453d-89c6-16eacb27be4b.1.liquid,snippets/reploChunk.49f797d7-0af0-453d-89c6-16eacb27be4b.3.liquid,snippets/reploChunk.4eabc0b1-7304-4a42-8a9b-d8568c705d20.2.liquid,snippets/reploChunk.4eabc0b1-7304-4a42-8a9b-d8568c705d20.0.liquid,snippets/reploChunk.4eabc0b1-7304-4a42-8a9b-d8568c705d20.3.liquid,snippets/reploChunk.58bb53cb-ed79-4ebd-8730-a8b93b0855df.3.liquid,snippets/reploChunk.5d51e195-915e-4585-90af-128902b5730a.2.liquid,snippets/reploChunk.5d51e195-915e-4585-90af-128902b5730a.0.liquid,snippets/reploChunk.58bb53cb-ed79-4ebd-8730-a8b93b0855df.4.liquid,snippets/reploChunk.5ec3bcab-7f59-4559-8883-9883c9538797.0.liquid,snippets/reploChunk.5ec3bcab-7f59-4559-8883-9883c9538797.1.liquid,snippets/reploChunk.5d51e195-915e-4585-90af-128902b5730a.1.liquid,snippets/reploChunk.5ec3bcab-7f59-4559-8883-9883c9538797.4.liquid,snippets/reploChunk.5ec3bcab-7f59-4559-8883-9883c9538797.2.liquid,snippets/reploChunk.5ec3bcab-7f59-4559-8883-9883c9538797.3.liquid,snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.0.liquid,snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.2.liquid,snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.5.liquid,snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.4.liquid,snippets/reploChunk.9068947d-baae-4de2-9c07-ac612987d696.1.liquid,snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.1.liquid,snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.3.liquid,snippets/reploChunk.9068947d-baae-4de2-9c07-ac612987d696.0.liquid,snippets/reploChunk.9068947d-baae-4de2-9c07-ac612987d696.2.liquid,snippets/reploChunk.9068947d-baae-4de2-9c07-ac612987d696.3.liquid,snippets/reploChunk.91f057eb-81a7-41c6-8400-b16a5d3312db.0.liquid,snippets/reploChunk.91f057eb-81a7-41c6-8400-b16a5d3312db.5.liquid,snippets/reploChunk.91f057eb-81a7-41c6-8400-b16a5d3312db.3.liquid,snippets/reploChunk.9c34a797-ff6e-405f-95fc-c31ef9eee0cf.3.liquid,snippets/reploChunk.a3a6df35-52d6-4564-b41a-8f780dfa9643.1.liquid,snippets/reploChunk.aacb5a11-aa62-459e-ab73-43a996b6844c.1.liquid,snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.2.liquid,snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.3.liquid,snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.4.liquid,snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.6.liquid,snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.0.liquid,snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.2.liquid,snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.1.liquid,snippets/reploChunk.aacb5a11-aa62-459e-ab73-43a996b6844c.2.liquid,snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.4.liquid,snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.3.liquid,snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.6.liquid,snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.5.liquid,snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.5.liquid,snippets/reploChunk.b3e927dc-9473-4fdd-a91b-3b8e339331a0.0.liquid,snippets/reploChunk.b3e927dc-9473-4fdd-a91b-3b8e339331a0.1.liquid,snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.0.liquid,snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.2.liquid,snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.1.liquid,snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.5.liquid,snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.3.liquid,snippets/reploChunk.cc823b0c-07e5-4fb7-8e46-2833c8ca81cb.0.liquid,snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.4.liquid,snippets/reploChunk.b3e927dc-9473-4fdd-a91b-3b8e339331a0.2.liquid,snippets/reploChunk.cc823b0c-07e5-4fb7-8e46-2833c8ca81cb.2.liquid,snippets/reploChunk.cc823b0c-07e5-4fb7-8e46-2833c8ca81cb.3.liquid,snippets/reploChunk.cc823b0c-07e5-4fb7-8e46-2833c8ca81cb.1.liquid,snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.0.liquid,snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.1.liquid,snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.5.liquid,snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.2.liquid,snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.4.liquid,snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.0.liquid,snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.3.liquid,snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.1.liquid,snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.2.liquid,snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.3.liquid,snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.6.liquid,snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.4.liquid,snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.5.liquid,snippets/reploChunk.d878c8e0-65c2-4df9-ba78-b5093050352d.1.liquid,snippets/reploChunk.d878c8e0-65c2-4df9-ba78-b5093050352d.0.liquid,snippets/reploChunk.de3d2b17-4441-466d-8ea8-735cb139f93d.1.liquid,snippets/reploChunk.de3d2b17-4441-466d-8ea8-735cb139f93d.0.liquid,snippets/reploChunk.e19d72ce-6c07-4057-91f3-928ad106aa82.0.liquid,snippets/reploChunk.e813f58e-a823-4650-abeb-167cfd964417.1.liquid,snippets/reploChunk.e31fccdc-20c9-426b-af0b-034c2e86b134.0.liquid,snippets/reploChunk.e96b7b3b-963e-4b22-a962-db81c2de69ac.0.liquid,snippets/reploChunk.e813f58e-a823-4650-abeb-167cfd964417.0.liquid,snippets/reploChunk.e96b7b3b-963e-4b22-a962-db81c2de69ac.1.liquid,snippets/reploChunk.eb957753-1d92-466e-ab11-d44078c5740a.1.liquid,snippets/reploChunk.eb957753-1d92-466e-ab11-d44078c5740a.0.liquid,snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.0.liquid,snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.1.liquid,snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.2.liquid,snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.4.liquid,snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.3.liquid,snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.5.liquid,snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.6.liquid,snippets/reploChunk.e31fccdc-20c9-426b-af0b-034c2e86b134.1.liquid,snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.4.liquid,snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.0.liquid,snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.2.liquid,snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.6.liquid,snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.1.liquid,snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.3.liquid,snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.5.liquid,snippets/reploChunk.f29ab7b3-2a18-4771-b61a-a7d4228f5d1b.4.liquid,snippets/reploChunk.f29ab7b3-2a18-4771-b61a-a7d4228f5d1b.1.liquid,snippets/reploChunk.f29ab7b3-2a18-4771-b61a-a7d4228f5d1b.0.liquid,snippets/reploChunk.f29ab7b3-2a18-4771-b61a-a7d4228f5d1b.2.liquid,snippets/reploChunk.aacb5a11-aa62-459e-ab73-43a996b6844c.3.liquid,snippets/reploChunk.f29ab7b3-2a18-4771-b61a-a7d4228f5d1b.3.liquid,snippets/reploChunk.f795dec7-1517-4072-8183-47a6f47e0f51.0.liquid,snippets/scrollbar.liquid,snippets/section-properties.liquid,snippets/section-header.liquid,snippets/section-spacing-collapsing.liquid,snippets/select.liquid,snippets/shadow-dom-templates.liquid,snippets/shipping-estimator.liquid,snippets/share-link.liquid,snippets/social-media.liquid,snippets/social-meta-tags.liquid,snippets/source-tracking-script.liquid,snippets/styled-text.liquid,snippets/surface.liquid,snippets/variant-picker.liquid,snippets/ultimate-datalayer.liquid,snippets/vendor.liquid,snippets/reploChunk.f795dec7-1517-4072-8183-47a6f47e0f51.1.liquid,snippets/reploChunk.f795dec7-1517-4072-8183-47a6f47e0f51.2.liquid,snippets/reploChunk.f795dec7-1517-4072-8183-47a6f47e0f51.3.liquid,snippets/reploChunk.e19d72ce-6c07-4057-91f3-928ad106aa82.1.liquid,templates/gift_card.liquid,templates/index.json,templates/page.replo.32e885b4-7241-49a0-a967-44507d611922.liquid,templates/page.replo.060a43f3-16b2-464c-ada3-7e3999e7a8ca.liquid,templates/page.replo.3b06b51f-bb9e-4c19-926e-4092cd9a945c.liquid,templates/page.replo.4785765d-2ec6-46cc-a50f-6c1fccabefd2.liquid,templates/page.replo.49b05d93-ef36-4211-8229-47ae5d6bca43.liquid,templates/page.replo.4eabc0b1-7304-4a42-8a9b-d8568c705d20.liquid,templates/page.replo.60541709-52f5-445c-861d-fe76a406b264.liquid,templates/page.replo.82f1f6c0-d775-4dc7-808d-b358219e3aba.liquid,templates/page.replo.634ff841-0f6c-429d-9b0a-6ca269a441e8.liquid,templates/page.replo.92faf019-cb9f-4e75-8426-1f2ea882d482.liquid,templates/page.replo.85a4b83b-8dcc-4a2c-8a6b-b34e1cd989d1.liquid,templates/page.replo.9068947d-baae-4de2-9c07-ac612987d696.liquid,templates/page.replo.9c34a797-ff6e-405f-95fc-c31ef9eee0cf.liquid,templates/page.replo.9f889b88-fce0-4904-9fd3-e2563abca319.liquid,templates/page.replo.aacb5a11-aa62-459e-ab73-43a996b6844c.liquid,templates/page.replo.b06086a5-34f6-4c4d-babd-edd23e97975a.liquid,templates/page.replo.b0b6630b-5d57-4fde-af92-423699a42aba.liquid,templates/page.replo.b5195668-e4bc-42c3-808d-a3b1517643d1.liquid,templates/page.replo.d45cc921-9524-451f-a691-424125b3017a.liquid)...
2025-07-18T12:47:02.206Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 7988 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=92, graphql;desc="admin/query/other", cfRequestDuration;dur=523.999929
 - x-request-id: 1398fb1c-c664-4282-a5cf-cb090be70c23-1752842820
    
2025-07-18T12:47:03.601Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 9383 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=63, graphql;desc="admin/query/other", cfRequestDuration;dur=483.000040
 - x-request-id: f51d8b55-c8f0-467b-af54-65d07c59933e-1752842822
    
2025-07-18T12:47:03.601Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 9383 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=58, graphql;desc="admin/query/other", cfRequestDuration;dur=507.000208
 - x-request-id: 3474fac2-44b7-481b-945a-1ca69856cbd1-1752842822
    
2025-07-18T12:47:03.615Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 9397 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=201, graphql;desc="admin/query/other", cfRequestDuration;dur=605.999947
 - x-request-id: c4929a92-ffb9-43ae-ac04-75af6f698ef9-1752842822
    
2025-07-18T12:47:04.633Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 10416 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=61, graphql;desc="admin/query/other", cfRequestDuration;dur=460.000038
 - x-request-id: 06f712de-a380-4a45-a43b-da081749647a-1752842824
    
2025-07-18T12:47:04.660Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 10443 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=63, graphql;desc="admin/query/other", cfRequestDuration;dur=504.999876
 - x-request-id: 46b3cbc0-73cb-4d7f-a714-4b93fdfe3bb5-1752842824
    
2025-07-18T12:47:04.696Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 10478 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=51, graphql;desc="admin/query/other", cfRequestDuration;dur=444.999933
 - x-request-id: b08b6f92-45ef-4a79-bb50-3cc2a9461cdb-1752842824
    
2025-07-18T12:47:04.798Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 10581 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=70, graphql;desc="admin/query/other", cfRequestDuration;dur=526.000023
 - x-request-id: b6709274-4134-4989-9f6d-43195a7afa44-1752842824
    
2025-07-18T12:47:04.884Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 10666 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=57, graphql;desc="admin/query/other", cfRequestDuration;dur=481.000185
 - x-request-id: fcb867d1-3c30-4b53-ab1e-4105161cabd4-1752842824
    
2025-07-18T12:47:05.891Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 11673 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=56, graphql;desc="admin/query/other", cfRequestDuration;dur=468.999863
 - x-request-id: 920030ab-b59f-47b7-8a59-b114f8068f0c-1752842825
    
2025-07-18T12:47:06.286Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 10045 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=120, graphql;desc="admin/query/other", cfRequestDuration;dur=588.000059
 - x-request-id: 748dc0fd-860f-49b0-bbb8-d576e3702ccd-1752842825
    
2025-07-18T12:47:06.287Z: Sending "Admin" GraphQL request:
  query getThemeFileChecksums($id: ID!, $after: String) {
  theme(id: $id) {
    files(first: 250, after: $after) {
      nodes {
        filename
        size
        checksumMd5
        __typename
      }
      userErrors {
        filename
        code
        __typename
      }
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "id": "gid://shopify/OnlineStoreTheme/184608981335",
  "after": "InNuaXBwZXRzXC9yZXBsby5zZWN0aW9uLXNldHRpbmdzLmViOTU3NzUzLTFkOTItNDY2ZS1hYjExLWQ0NDA3OGM1NzQwYS5saXF1aWQi"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:47:06.778Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 12560 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=52, graphql;desc="admin/query/other", cfRequestDuration;dur=463.000059
 - x-request-id: 70a38445-c033-4579-9249-7ce728f610fb-1752842826
    
2025-07-18T12:47:06.779Z: File-writing some content to file at .shopify/metafields.json...
2025-07-18T12:47:06.797Z: Running system process:
  · Command: npm prefix
  · Working directory: /home/maxdesign/shopify/stores/Aloe-Paris

2025-07-18T12:47:06.892Z: Obtaining the dependency manager in directory /home/maxdesign...
2025-07-18T12:47:07.746Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 1459 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=90, graphql;desc="admin/query/other", cfRequestDuration;dur=492.999792
 - x-request-id: d14c1f53-c08f-4592-92a0-cae22049ad47-1752842827
    
2025-07-18T12:47:08.585Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 1582 ms
With response headers:
 - x-request-id: 1f39fca8-9d5a-4bdd-8d10-2c174be6042c
    
2025-07-18T12:47:08.585Z: Analytics event sent: {
  "command": "theme dev",
  "time_start": 1752842775545,
  "time_end": 1752842826784,
  "total_time": 51239,
  "success": true,
  "cli_version": "3.79.2",
  "ruby_version": "",
  "node_version": "18.20.8",
  "is_employee": false,
  "uname": "linux amd64",
  "env_ci": false,
  "env_plugin_installed_any_custom": false,
  "env_plugin_installed_shopify": "[\"@shopify/cli\"]",
  "env_shell": "bash",
  "env_device_id": "bcf6b6129e2354402cc7a61ab8fc7bc2af7e9dc7",
  "env_cloud": "localhost",
  "env_package_manager": "npm",
  "env_is_global": false,
  "env_auth_method": "device_auth",
  "env_is_wsl": true,
  "cmd_app_warning_api_key_deprecation_displayed": false,
  "cmd_all_timing_network_ms": 31998,
  "cmd_all_timing_prompts_ms": 3963,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "theme",
  "cmd_all_plugin": "@shopify/theme",
  "cmd_all_force": false,
  "cmd_all_verbose": true,
  "cmd_all_path_override": true,
  "cmd_all_path_override_hash": "4dd385ba972ce70efd189ec39f75352d17fda9ff",
  "cmd_all_last_graphql_request_id": "70a38445-c033-4579-9249-7ce728f610fb-1752842826",
  "cmd_all_timing_active_ms": 15277,
  "cmd_all_exit": "ok",
  "user_id": "1d15a73e-3ba4-45ce-bd47-1dece53355fd",
  "request_ids": [
    "94e57e2a-156c-4834-a902-8c568cf55efd-1752842775",
    "b427bfb7-1a4e-463c-976d-9d40e04b6b1d-1752842777",
    "a78417f9-1820-4e58-adf4-712d5d8b7808-1752842777",
    "a859f93b-18cc-4a1f-87c5-faef185f62de-1752842780",
    "0218977d-ffe2-4bd6-b11d-7f7ebca662f5-1752842781",
    "0e1f1cb5-3434-4d9c-af5c-f99144aed87e-1752842786",
    "836b9fbd-7255-462a-a467-3837b67415ba-1752842786",
    "81b9247b-48ce-4e9b-9cb2-cc57eca28de7-1752842820",
    "1398fb1c-c664-4282-a5cf-cb090be70c23-1752842820",
    "f51d8b55-c8f0-467b-af54-65d07c59933e-1752842822",
    "3474fac2-44b7-481b-945a-1ca69856cbd1-1752842822",
    "c4929a92-ffb9-43ae-ac04-75af6f698ef9-1752842822",
    "06f712de-a380-4a45-a43b-da081749647a-1752842824",
    "46b3cbc0-73cb-4d7f-a714-4b93fdfe3bb5-1752842824",
    "b08b6f92-45ef-4a79-bb50-3cc2a9461cdb-1752842824",
    "b6709274-4134-4989-9f6d-43195a7afa44-1752842824",
    "fcb867d1-3c30-4b53-ab1e-4105161cabd4-1752842824",
    "920030ab-b59f-47b7-8a59-b114f8068f0c-1752842825",
    "748dc0fd-860f-49b0-bbb8-d576e3702ccd-1752842825",
    "70a38445-c033-4579-9249-7ce728f610fb-1752842826"
  ],
  "args": "--theme-editor-sync --store=aloe-paris --verbose",
  "env_plugin_installed_all": "[\"@shopify/cli\"]",
  "metadata": "{\"extraPublic\":{},\"extraSensitive\":{}}"
}
2025-07-18T12:47:08.585Z: Completed command theme dev
2025-07-18T12:47:10.748Z: Sending "Admin" GraphQL request:
  query getThemeFileChecksums($id: ID!, $after: String) {
  theme(id: $id) {
    files(first: 250, after: $after) {
      nodes {
        filename
        size
        checksumMd5
        __typename
      }
      userErrors {
        filename
        code
        __typename
      }
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "id": "gid://shopify/OnlineStoreTheme/184608981335",
  "after": null
}

With request headers:
 - User-Agent: Shopify CLI; v=3.79.2
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T12:47:10.947Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 17735 ms
With response headers:
 - content-type: text/html
    
╭─ error ──────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                          │
│  Failed to perform the initial theme synchronization.                                                    │
│                                                                                                          │
│  The Admin GraphQL API responded unsuccessfully with the HTTP status 502 and errors:                     │
│                                                                                                          │
│  {}                                                                                                      │
│                                                                                                          │
│                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
</details>

One of the error I got on last snapshot shared above (node 22):
<details>
<summary>Verbose output</summary>

```
XMlJoZEdFdGNtbGtYU3hjYmlBZ1kyRnVkbUZ6VzJSaGRHRXRjbWxrWFN4Y2JpQWdaR1YwWVdsc2MxdGtZWFJoTFhKcFpGMHNYRzRnSUdWdFltVmtXMlJoZEdFdGNtbGtYU3hjYmlBZ1ptbG5kWEpsVzJSaGRHRXRjbWxrWFN4Y2JpQWdabWxuWTJGd2RHbHZibHRrWVhSaExYSnBaRjBzWEc0Z0lHWnZiM1JsY2x0a1lYUmhMWEpwWkYwc1hHNGdJR2hsWVdSbGNsdGtZWFJoTFhKcFpGMHNYRzRnSUdobmNtOTFjRnRrWVhSaExYSnBaRjBzWEc0Z0lHMWxiblZiWkdGMFlTMXlhV1JkTEZ4dUlDQnVZWFpiWkdGMFlTMXlhV1JkTEZ4dUlDQnZkWFJ3ZFhSYlpHRjBZUzF5YVdSZExGeHVJQ0J5ZFdKNVcyUmhkR0V0Y21sa1hTeGNiaUFnYzJWamRHbHZibHRrWVhSaExYSnBaRjBzWEc0Z0lITjFiVzFoY25sYlpHRjBZUzF5YVdSZExGeHVJQ0IwYVcxbFcyUmhkR0V0Y21sa1hTeGNiaUFnYldGeWExdGtZWFJoTFhKcFpGMHNYRzRnSUdGMVpHbHZXMlJoZEdFdGNtbGtYU3hjYmlBZ2RtbGtaVzliWkdGMFlTMXlhV1JkTEZ4dUlDQmlkWFIwYjI1YlpHRjBZUzF5YVdSZExGeHVJQ0J6Wld4bFkzUmJaR0YwWVMxeWFXUmRMRnh1SUNCYlpHRjBZUzF5YVdSZElENGdjQ0I3WEc0Z0lDQWdabTl1ZEMxemRIbHNaVG9nYVc1b1pYSnBkRHRjYmlBZ0lDQjBaWGgwTFdSbFkyOXlZWFJwYjI0NklHbHVhR1Z5YVhRN1hHNGdJQ0FnWTI5c2IzSTZJR2x1YUdWeWFYUTdYRzRnSUNBZ1ltRmphMmR5YjNWdVpDMWpiMnh2Y2pvZ2RISmhibk53WVhKbGJuUTdYRzRnSUgxY2JseHVJQ0F1WVd4amFHVnRlUzF5ZEdVZ2UxeHVJQ0FnSUVCcGJtTnNkV1JsSUhKMFpTNXlhV05vTFhSbGVIUXRjM1I1YkdWek8xeHVJQ0I5WEc1Y2JpQWdMeW9nU0ZSTlREVWdaR2x6Y0d4aGVTMXliMnhsSUhKbGMyVjBJR1p2Y2lCdmJHUmxjaUJpY205M2MyVnljeUFxTDF4dUlDQmhjblJwWTJ4bFcyUmhkR0V0Y21sa1hTeGNiaUFnWVhOcFpHVmJaR0YwWVMxeWFXUmRMRnh1SUNCa1pYUmhhV3h6VzJSaGRHRXRjbWxrWFN4Y2JpQWdabWxuWTJGd2RHbHZibHRrWVhSaExYSnBaRjBzWEc0Z0lHWnBaM1Z5WlZ0a1lYUmhMWEpwWkYwc1hHNGdJR1p2YjNSbGNsdGtZWFJoTFhKcFpGMHNYRzRnSUdobFlXUmxjbHRrWVhSaExYSnBaRjBzWEc0Z0lHaG5jbTkxY0Z0a1lYUmhMWEpwWkYwc1hHNGdJRzFsYm5WYlpHRjBZUzF5YVdSZExGeHVJQ0J1WVhaYlpHRjBZUzF5YVdSZExGeHVJQ0J6WldOMGFXOXVXMlJoZEdFdGNtbGtYU0I3WEc0Z0lDQWdaR2x6Y0d4aGVUb2dZbXh2WTJzN1hHNGdJSDFjYmlBZ1ltOWtlU0I3WEc0Z0lDQWdiR2x1WlMxb1pXbG5hSFE2SURFN1hHNGdJSDFjYmx4dUlDQmliRzlqYTNGMWIzUmxMRnh1SUNCeElIdGNiaUFnSUNCeGRXOTBaWE02SUc1dmJtVTdYRzRnSUNBZ2JXRnlaMmx1T2lBd08xeHVJQ0FnSUhCaFpHUnBibWM2SURBN1hHNGdJQ0FnWW05eVpHVnlPaUF3TzF4dUlDQjlYRzRnSUdKc2IyTnJjWFZ2ZEdVNlltVm1iM0psTEZ4dUlDQmliRzlqYTNGMWIzUmxPbUZtZEdWeUxGeHVJQ0J4T21KbFptOXlaU3hjYmlBZ2NUcGhablJsY2lCN1hHNGdJQ0FnWTI5dWRHVnVkRG9nWENKY0lqdGNiaUFnSUNCamIyNTBaVzUwT2lCdWIyNWxPMXh1SUNCOVhHNGdJSFJoWW14bElIdGNiaUFnSUNCaWIzSmtaWEl0WTI5c2JHRndjMlU2SUdOdmJHeGhjSE5sTzF4dUlDQWdJR0p2Y21SbGNpMXpjR0ZqYVc1bk9pQXdPMXh1SUNCOVhHNWNiaUFnWW5WMGRHOXVJRDRnY0dsamRIVnlaU3hjYmlBZ1luVjBkRzl1SUQ0Z2FXMW5MRnh1SUNCaElENGdjR2xqZEhWeVpTeGNiaUFnWVNBK0lHbHRaeUI3WEc0Z0lDQWdaR2x6Y0d4aGVUb2dabXhsZUR0Y2JpQWdmVnh1ZlZ4dVhHNGpjbVZ3Ykc4dFpuVnNiSEJoWjJVdFpXeGxiV1Z1ZENCN1hHNGdJQzh2SUU1dmRHVWdLRTV2WVdnc0lESXdNakl0TVRFdE1EWXNJRkpGVUV3dE5Ea3pMQ0JTUlZCTUxUVXdOamNwT2lCVGIyMWxJSFJvWlcxbGN5QmtiMjRuZENCeVpYTjBjbWxqZENCMGFHVWdkMmxrZEdoY2JpQWdMeThnYjJZZ2RHaGxJRzFoYVc0Z1kyOXVkR1Z1ZEN3Z2MyOGdiMjRnY0dGblpYTWdkMmhsY21VZ2RHaGxjbVVuY3lCaElHMWhlQzEzYVdSMGFDQnZaaUF4TURBbElHOXVJR05sY25SaGFXNWNiaUFnTHk4Z1pXeGxiV1Z1ZEhNc0lIUm9aWGtnWTJGdUlHRmpkSFZoYkd4NUlHOTJaWEptYkc5M0xpQkViMlZ6YmlkMElHMWhhMlVnYzJWdWMyVWdabTl5SUhSb1pTQnliMjkwSUZKbGNHeHZYRzRnSUM4dklHVnNaVzFsYm5RZ2FYUnpaV3htSUhSdklHOTJaWEptYkc5M0lDaDBhRzkxWjJnZ1pHVndaVzVrYVc1bklHOXVJSFJvWlNCamIyNTBaVzUwSUc5bUlIUm9aU0J3WVdkbExDQnpiMjFsWEc0Z0lDOHZJR05vYVd4a2NtVnVJRzFwWjJoMEtTQnpieUJ6WlhSMGFXNW5JSFJvYVhNZ2RHOGdiV0Y0TFhkcFpIUm9PaUF4TURCM2RpQm1hWGhsY3lCMGFHVWdhWE56ZFdVdVhHNGdJRzFoZUMxM2FXUjBhRG9nTVRBd2RuYzdYRzVjYmlBZ0x5OGdUbTkwWlNBb1QzWnBjMmhsYXl3Z01qQXlNeTB3TWkweU55d2dVa1ZRVEMwMk5ERTNLVG9nU1c0Z2RHaHBjeUJqWVhObElIZG9aWEpsSUdKdlpIa2daV3hsYldWdWRDQm9ZWE1nWkdsemNHeGhlU0JtYkdWNExGeHVJQ0F2THlCM1pTQnphRzkxYkdRZ1lXUmtJR1pzWlhndFozSnZkem9nTVNCaGJtUWdZV3hwWjI0dGMyVnNaam9nYzNSeVpYUmphQ0IwYnlCMGFHVWdJM0psY0d4dkxXWjFiR3h3WVdkbExXVnNaVzFsYm5SY2JpQWdMeThnZEc4Z1pXNXpkWEpsSUhSb1pTQndaWEptWldOMElHeGhlVzkxZEM1Y2JpQWdMeThnVkdocGN5QmphR0Z1WjJVZ2NtVnpiMngyWlhNZ2RHaGxJR2h2YldWd1lXZGxJRzl1SUhSb1pTQnRaVzUwYVc5dVpXUWdkR2xqYTJWMElHWnliMjBnYUdGMmFXNW5JSGRsYVhKa0lHZGhjQ0J2YmlCMGFHVWdjbWxuYUhRZ2MybGtaVnh1SUNBdkx5QnZaaUIwYUdVZ2NHRm5aUzVjYmlBZ1pteGxlQzFuY205M09pQXhPMXh1SUNCaGJHbG5iaTF6Wld4bU9pQnpkSEpsZEdOb08xeHVmVnh1WEc0dWIzVjBiR2x1WlMwdFlteDFaU0I3WEc0Z0lHOTFkR3hwYm1VNklESndlQ0J6YjJ4cFpDQWpNalUyTTJWaU8xeHVmVnh1WEc0dWMzUnlhV3RsT2pwaFpuUmxjaUI3WEc0Z0lHTnZiblJsYm5RNklGd2lYQ0k3WEc0Z0lHSnZjbVJsY2kxaWIzUjBiMjA2SUROd2VDQnpiMnhwWkNCaWJHRmphenRjYmlBZ2NHOXphWFJwYjI0NklHRmljMjlzZFhSbE8xeHVJQ0JzWldaME9pQXdPMXh1SUNCMGIzQTZJR05oYkdNb05UQWxJQzBnTTNCNEtUdGNiaUFnZDJsa2RHZzZJREV3TUNVN1hHNTlYRzVjYmk1U1pXRmpkRTF2WkdGc1gxOVBkbVZ5YkdGNUxTMWhablJsY2kxdmNHVnVJSHRjYmlBZ2IzQmhZMmwwZVRvZ01UdGNiaUFnZEhKaGJuTm1iM0p0T2lCMGNtRnVjMnhoZEdWWktEQndlQ2s3WEc1OVhHNWNiaTVTWldGamRFMXZaR0ZzWDE5UGRtVnliR0Y1TFMxaVpXWnZjbVV0WTJ4dmMyVWdlMXh1SUNCdmNHRmphWFI1T2lBd08xeHVJQ0IwY21GdWMyWnZjbTA2SUhSeVlXNXpiR0YwWlZrb01UQXdjSGdwTzF4dWZWeHVYRzR1Y21Wd2JHOHRiVzlrWVd3dFlXWjBaWEl0YjNCbGJpQjdYRzRnSUc5MlpYSm1iRzkzTFhrNklHaHBaR1JsYmlBaGFXMXdiM0owWVc1ME8xeHVJQ0J6WTNKdmJHd3RZbVZvWVhacGIzSTZJR0YxZEc4Z0lXbHRjRzl5ZEdGdWREdGNibjFjYmx4dUx5OGdUbTkwWlNBb1RtOWhhQ3dnTWpBeU5DMHhNaTB3TkN3Z1ZWTkZMVEUwTkRVcE9pQklZWEprWTI5a1pTQnpZM0p2Ykd3dFltVm9ZWFpwYjNJZ2IyWWdZbTlrZVZ4dUx5OGdZVzVrSUdoMGJXd2dkRzhnWVhWMGJ5QjNhR1Z1SUdFZ2JXOWtZV3dnYVhNZ2IzQmxiaXdnWW1WallYVnpaU0JwWmlCMGFHVWdkR2hsYldVZ2FHRnpJSE5sZEZ4dUx5OGdjMk55YjJ4c0xXSmxhR0YyYVc5eU9pQnpiVzl2ZEdnc0lIUm9aVzRnZEdobElIUnlZVzV6YVhScGIyNXpJSFJvWVhRZ2NtVmhZM1F0Ylc5a1lXd2dZV1JrYzF4dUx5OGdkRzhnZEdobElHaDBiV3d2WW05a2VTQmxiR1Z0Wlc1MGN5QjNhV3hzSUdOaGRYTmxJSFJvWlNCd1lXZGxJSFJ2SUhOamNtOXNiQ0J5WldGc2JIa2dabUZ6ZEZ4dUx5OGdabkp2YlNCMGIzQWdkRzhnWW05MGRHOXRYRzVvZEcxc09taGhjeWcrSUM1eVpYQnNieTF0YjJSaGJDMWhablJsY2kxdmNHVnVLU0I3WEc0Z0lITmpjbTlzYkMxaVpXaGhkbWx2Y2pvZ1lYVjBieUFoYVcxd2IzSjBZVzUwTzF4dWZWeHVYRzR1WTJGeWIzVnpaV3hXTXkwdGMyeHBaR1V0Y21WelpYUWdlMXh1SUNCdFlYZ3RkMmxrZEdnNklHNXZibVVnSVdsdGNHOXlkR0Z1ZER0Y2JuMWNibHh1TG1OaGNtOTFjMlZzVmpNdGJtOHRkSEpoYm5OcGRHbHZiaUI3WEc0Z0lIUnlZVzV6YVhScGIyNDZJRzV2Ym1VN1hHNTlYRzVjYmk1allYSnZkWE5sYkZZekxXWmhaR1V0ZEhKaGJuTnBkR2x2YmlCN1hHNGdJSFJ5WVc1emFYUnBiMjQ2SUc5d1lXTnBkSGtnTVRBd01HMXpPMXh1ZlZ4dVhHNHVZMkZ5YjNWelpXeFdNeTFvYVdSa1pXNHRjMnhwWkdVZ2UxeHVJQ0IwY21GdWMybDBhVzl1T2lCdmNHRmphWFI1SURFd01EQnRjenRjYmlBZ2IzQmhZMmwwZVRvZ01EdGNibjFjYmk1allYSnZkWE5sYkZZekxYWnBjMmxpYkdVdGMyeHBaR1VnZTF4dUlDQjBjbUZ1YzJsMGFXOXVPaUJ2Y0dGamFYUjVJREV3TURCdGN6dGNiaUFnYjNCaFkybDBlVG9nTVR0Y2JuMWNibHh1THk4Z1RtOTBaU0FvVG05aGFDd2dNakF5TWkweE1TMHhNeXdnVWtWUVRDMDFNRFF3S1RvZ1UyOXRaU0IwYUdWdFpYTWdhVzVxWldOMElITjBlV3hsY3lCMGJ5QnRZV3RsSUdGc2JDQThiR2srSUdWc1pXMWxiblJ6WEc0dkx5Qm9ZWFpsSUdKMWJHeGxkQ0J3YjJsdWRITXNJR0oxZENCMGFHRjBJRzFsYzNObGN5QjNhWFJvSUc5MWNpQmpZWEp2ZFhObGJITWdkMmhwWTJnZ2NtVnVaR1Z5SUR4c2FUNXpMaUJVYUdseklISmxjMlYwYzF4dUx5OGdkR2h2YzJVZ2MzUjViR1Z6WEc0dWMzQnNhV1JsSUh0Y2JpQWdiR2tnZTF4dUlDQWdJSEJoWkdScGJtYzZJREFnSVdsdGNHOXlkR0Z1ZER0Y2JpQWdJQ0F2THlCT2IzUmxJQ2hPYjJGb0xDQXlNREl5TFRFeExURTNMQ0JTUlZCTUxUVXhNeklwT2lCRWIyNG5kQ0J2ZG1WeWNtbGtaU0J0WVhKbmFXNGdkMmwwYUNBaGFXMXdiM0owWVc1MElHSmxZMkYxYzJWY2JpQWdJQ0F2THlCcGRDQjNhV3hzSUhKbGJXOTJaU0IwYUdVZ1lYVjBiMjFoZEdsaklHMWhjbWRwYmlCMGFHRjBJRk53Ykdsa1pTQmhaR1J6SUhSdklHaGhkbVVnZEdobElHZGhjQ0IzYjNKckxseHVJQ0FnSUM4dklGUlBSRTg2SUdseklIUm9aWEpsSUdFZ1ltVjBkR1Z5SUhkaGVTQjBieUJ6YjJ4MlpTQjBhR2x6UHlCVVpXTm9ibWxqWVd4c2VTQnBaaUIwYUdWeVpTZHpJRzFoY21kcGJpQnZiaUIwYUdWY2JpQWdJQ0F2THlCMGFHVnRaU0J2YmlCc2FTZHpJSGRwZEdnZ2FHbG5hQ0JsYm05MVoyZ2djM0JsWTJsbWFXTnBkSGtzSUdsMElIZHBiR3dnYzNScGJHd2diM1psY25KcFpHVWdkR2hwY3k1Y2JpQWdJQ0J0WVhKbmFXNDZJREE3WEc0Z0lDQWdKam82WW1WbWIzSmxJSHRjYmlBZ0lDQWdJR1JwYzNCc1lYazZJRzV2Ym1VZ0lXbHRjRzl5ZEdGdWREdGNiaUFnSUNCOVhHNGdJSDFjYmx4dUlDQXVjM0JzYVdSbFgxOXNhWE4wSUh0Y2JpQWdJQ0F2THlCT2IzUmxJQ2hPYjJGb0xDQXlNREl5TFRFeUxUQTNMQ0JTUlZCTUxUVTBNREFwT2lCVGIyMWxJSFJvWlcxbGN5QnpaWFFnWVd4c0lIVnNKM01nZEc4Z2IzWmxjbVpzYjNjZ2FHbGtaR1Z1SUNoc2JXRnZLVnh1SUNBZ0lDOHZJR0oxZENCVGNHeHBaR1VnYm1WbFpITWdkRzhnWW1VZ2RtbHphV0pzWlNCcGJpQnZjbVJsY2lCbWIzSWdhWFFnZEc4Z2QyOXlheUJ3Y205d1pYSnNlU0IzYVhSb0lHbDBjeUJoYm1sdFlYUmxaQ0IwY21GdWMyWnZjbTFjYmlBZ0lDQXZMeUJ3Y205d1pYSjBlUzRnU1dZZ2QyVWdaRzl1SjNRZ2MyVjBJSFJvYVhNc0lHOXVJSE52YldVZ2RHaGxiV1Z6SUdOaGNtOTFjMlZzY3lCM2FXeHNJR3h2YjJzZ2FXNWpiM0p5WldOMElHRm1kR1Z5SUhSb1pTQm1hWEp6ZEZ4dUlDQWdJQzh2SUhOc2FXUmxYRzRnSUNBZ2IzWmxjbVpzYjNjNklIWnBjMmxpYkdVZ0lXbHRjRzl5ZEdGdWREdGNiaUFnZlZ4dWZWeHVYRzVBYTJWNVpuSmhiV1Z6SUhKbGNHeHZMVzFoY25GMVpXVWdlMXh1SUNCbWNtOXRJSHRjYmlBZ0lDQjBjbUZ1YzJadmNtMDZJSFJ5WVc1emJHRjBaVmdvTUNrN1hHNGdJSDFjYmlBZ2RHOGdlMXh1SUNBZ0lIUnlZVzV6Wm05eWJUb2dkSEpoYm5Oc1lYUmxXQ2hjYmlBZ0lDQWdJR05oYkdNb1hHNGdJQ0FnSUNBZ0lIWmhjaWd0TFhKbGNHeHZMVzFoY25GMVpXVXRkMmxrZEdnc0lERXdNQ1VwSUNvZ0xURWdMMXh1SUNBZ0lDQWdJQ0FnSUhaaGNpZ3RMWEpsY0d4dkxXMWhjbkYxWldVdGNtVndaWFJwZEdsdmJuTXNJREl3S1Z4dUlDQWdJQ0FnS1Z4dUlDQWdJQ2s3WEc0Z0lIMWNibjFjYmx4dUx5OGdUbTkwWlNBb1EyaGhibU5sTENBeU1ESXpMVEE0TFRBektTQk5ZWEp4ZFdWbElHNXZJR3h2Ym1kbGNpQjFjMlZ6SUhSb1pYTmxJR3RsZVdaeVlXMWxjeXdnWW5WMElIUm9aWGxjYmk4dklHRnlaU0JvWlhKbElHWnZjaUJpWVdOcklHTnZiWEJoZENCcWRYTjBJR2x1SUdOaGMyVWdZU0IxYzJWeUlISmxabVZ5Wlc1alpYTWdkR2hsYlNCbWIzSWdjMjl0WlNCeVpXRnpiMjR1WEc0dkwxeHVMeThnVG05MFpTQW9UbTloYUN3Z01qQXlNUzB3T1Mwd09TazZJRlJvWlNCMGNtRnVjMnhoZEdWWUlIWmhiSFZsSUdobGNtVWdhWE1nWkdseVpXTjBiSGtnWTI5eWNtVnNZWFJsWkZ4dUx5OGdkMmwwYUNCMGFHVWdaR1ZtYVc1cGRHbHZiaUJ2WmlCdFlYSnhkV1ZsVkhKaFkydE9kVzFpWlhKUFprbDBaVzF6TENCcGRDQnVaV1ZrY3lCMGJ5QmlaU0JsZUdGamRHeDVPbHh1THk4Z0xURXdNQzl0WVhKeGRXVmxWSEpoWTJ0T2RXMWlaWEpQWmtsMFpXMXpJQ1VnWm05eUlIUm9aU0JoYm1sdFlYUnBiMjRnZEc4Z1kzbGpiR1VnYzJWaGJXeGxjM05zZVZ4dVFHdGxlV1p5WVcxbGN5QmhiR05vWlcxNUxXMWhjbkYxWldVdGJHVm1kQ0I3WEc0Z0lHWnliMjBnZTF4dUlDQWdJSFJ5WVc1elptOXliVG9nZEhKaGJuTnNZWFJsV0Nnd0tUdGNiaUFnZlZ4dUlDQjBieUI3WEc0Z0lDQWdkSEpoYm5ObWIzSnRPaUIwY21GdWMyeGhkR1ZZS0Z4dUlDQWdJQ0FnWTJGc1l5aGNiaUFnSUNBZ0lDQWdkbUZ5S0MwdGNtVndiRzh0YldGeWNYVmxaUzEzYVdSMGFDd2dNVEF3SlNrZ0tpQXRNU0F2WEc0Z0lDQWdJQ0FnSUNBZ2RtRnlLQzB0Y21Wd2JHOHRiV0Z5Y1hWbFpTMXlaWEJsZEdsMGFXOXVjeXdnTWpBcFhHNGdJQ0FnSUNBcFhHNGdJQ0FnS1R0Y2JpQWdmVnh1ZlZ4dVhHNUFhMlY1Wm5KaGJXVnpJR0ZzWTJobGJYa3RiV0Z5Y1hWbFpTMXlhV2RvZENCN1hHNGdJR1p5YjIwZ2UxeHVJQ0FnSUhSeVlXNXpabTl5YlRvZ2RISmhibk5zWVhSbFdDZ3ROVEFsS1R0Y2JpQWdmVnh1SUNCMGJ5QjdYRzRnSUNBZ2RISmhibk5tYjNKdE9pQjBjbUZ1YzJ4aGRHVllLRnh1SUNBZ0lDQWdZMkZzWXloY2JpQWdJQ0FnSUNBZ0xUVXdKU0FySUhaaGNpZ3RMWEpsY0d4dkxXMWhjbkYxWldVdGQybGtkR2dzSURFd01DVXBJQzhnZG1GeUtDMHRjbVZ3Ykc4dGJXRnljWFZsWlMxeVpYQmxkR2wwYVc5dWN5d2dNakFwWEc0Z0lDQWdJQ0FwWEc0Z0lDQWdLVHRjYmlBZ2ZWeHVmVnh1WEc1QWEyVjVabkpoYldWeklHRnNZMmhsYlhrdFptRmtaU0I3WEc0Z0lHWnliMjBnZTF4dUlDQWdJRzl3WVdOcGRIazZJSFpoY2lndExXbHVhWFJwWVd3dGIzQmhZMmwwZVNrN1hHNGdJSDFjYmlBZ2RHOGdlMXh1SUNBZ0lHOXdZV05wZEhrNklIWmhjaWd0TFdacGJtRnNMVzl3WVdOcGRIa3BPMXh1SUNCOVhHNTlYRzVjYmtCclpYbG1jbUZ0WlhNZ1lXeGphR1Z0ZVMxemJHbGtaUzE1SUh0Y2JpQWdabkp2YlNCN1hHNGdJQ0FnYjNCaFkybDBlVG9nZG1GeUtDMHRhVzVwZEdsaGJDMXZjR0ZqYVhSNUtUdGNiaUFnSUNCMGNtRnVjMlp2Y20wNklIUnlZVzV6YkdGMFpWa29kbUZ5S0MwdGIyWm1jMlYwS1NrN1hHNGdJSDFjYmlBZ2RHOGdlMXh1SUNBZ0lHOXdZV05wZEhrNklIWmhjaWd0TFdacGJtRnNMVzl3WVdOcGRIa3BPMXh1SUNBZ0lIUnlZVzV6Wm05eWJUb2dkSEpoYm5Oc1lYUmxXU2d3S1R0Y2JpQWdmVnh1ZlZ4dVhHNUFhMlY1Wm5KaGJXVnpJR0ZzWTJobGJYa3RjMnhwWkdVdGVDQjdYRzRnSUdaeWIyMGdlMXh1SUNBZ0lHOXdZV05wZEhrNklIWmhjaWd0TFdsdWFYUnBZV3d0YjNCaFkybDBlU2s3WEc0Z0lDQWdkSEpoYm5ObWIzSnRPaUIwY21GdWMyeGhkR1ZZS0haaGNpZ3RMVzltWm5ObGRDa3BPMXh1SUNCOVhHNGdJSFJ2SUh0Y2JpQWdJQ0J2Y0dGamFYUjVPaUIyWVhJb0xTMW1hVzVoYkMxdmNHRmphWFI1S1R0Y2JpQWdJQ0IwY21GdWMyWnZjbTA2SUhSeVlXNXpiR0YwWlZnb01DazdYRzRnSUgxY2JuMWNibHh1UUd0bGVXWnlZVzFsY3lCaGJHTm9aVzE1TFdac2FYQXRlU0I3WEc0Z0lHWnliMjBnZTF4dUlDQWdJRzl3WVdOcGRIazZJSFpoY2lndExXbHVhWFJwWVd3dGIzQmhZMmwwZVNrN1hHNGdJQ0FnZEhKaGJuTm1iM0p0T2lCeWIzUmhkR1ZaS0haaGNpZ3RMV0Z1WjJ4bEtTazdYRzRnSUgxY2JpQWdkRzhnZTF4dUlDQWdJRzl3WVdOcGRIazZJSFpoY2lndExXWnBibUZzTFc5d1lXTnBkSGtwTzF4dUlDQWdJSFJ5WVc1elptOXliVG9nY205MFlYUmxXU2d3S1R0Y2JpQWdmVnh1ZlZ4dVhHNUFhMlY1Wm5KaGJXVnpJR0ZzWTJobGJYa3RabXhwY0MxNElIdGNiaUFnWm5KdmJTQjdYRzRnSUNBZ2IzQmhZMmwwZVRvZ2RtRnlLQzB0YVc1cGRHbGhiQzF2Y0dGamFYUjVLVHRjYmlBZ0lDQjBjbUZ1YzJadmNtMDZJSEp2ZEdGMFpWZ29kbUZ5S0MwdFlXNW5iR1VwS1R0Y2JpQWdmVnh1SUNCMGJ5QjdYRzRnSUNBZ2IzQmhZMmwwZVRvZ2RtRnlLQzB0Wm1sdVlXd3RiM0JoWTJsMGVTazdYRzRnSUNBZ2RISmhibk5tYjNKdE9pQnliM1JoZEdWWUtEQXBPMXh1SUNCOVhHNTlYRzVjYmtCclpYbG1jbUZ0WlhNZ1lXeGphR1Z0ZVMxbmNtOTNJSHRjYmlBZ1puSnZiU0I3WEc0Z0lDQWdiM0JoWTJsMGVUb2dkbUZ5S0MwdGFXNXBkR2xoYkMxdmNHRmphWFI1S1R0Y2JpQWdJQ0IwY21GdWMyWnZjbTA2SUhOallXeGxLSFpoY2lndExXbHVhWFJwWVd3dGMyTmhiR1VwS1R0Y2JpQWdmVnh1SUNCMGJ5QjdYRzRnSUNBZ2IzQmhZMmwwZVRvZ2RtRnlLQzB0Wm1sdVlXd3RiM0JoWTJsMGVTazdYRzRnSUNBZ2RISmhibk5tYjNKdE9pQnpZMkZzWlNoMllYSW9MUzFtYVc1aGJDMXpZMkZzWlNrcE8xeHVJQ0I5WEc1OVhHNWNia0JyWlhsbWNtRnRaWE1nWVd4amFHVnRlUzF6Y0dsdUlIdGNiaUFnWm5KdmJTQjdYRzRnSUNBZ2IzQmhZMmwwZVRvZ2RtRnlLQzB0YVc1cGRHbGhiQzF2Y0dGamFYUjVLVHRjYmlBZ0lDQjBjbUZ1YzJadmNtMDZJSEp2ZEdGMFpTaDJZWElvTFMxcGJtbDBhV0ZzTFdGdVoyeGxLU2s3WEc0Z0lIMWNiaUFnZEc4Z2UxeHVJQ0FnSUc5d1lXTnBkSGs2SUhaaGNpZ3RMV1pwYm1Gc0xXOXdZV05wZEhrcE8xeHVJQ0FnSUhSeVlXNXpabTl5YlRvZ2NtOTBZWFJsS0haaGNpZ3RMV1pwYm1Gc0xXRnVaMnhsS1NrN1hHNGdJSDFjYm4xY2JseHVRR3RsZVdaeVlXMWxjeUJoYkdOb1pXMTVMV1pzZVMxNUlIdGNiaUFnWm5KdmJTQjdYRzRnSUNBZ2IzQmhZMmwwZVRvZ2RtRnlLQzB0YVc1cGRHbGhiQzF2Y0dGamFYUjVLVHRjYmlBZ0lDQjBjbUZ1YzJadmNtMDZJSFJ5WVc1emJHRjBaVmtvZG1GeUtDMHRiMlptYzJWMEtTa2djMk5oYkdVb01DazdYRzRnSUgxY2JpQWdkRzhnZTF4dUlDQWdJRzl3WVdOcGRIazZJSFpoY2lndExXWnBibUZzTFc5d1lXTnBkSGtwTzF4dUlDQWdJSFJ5WVc1elptOXliVG9nZEhKaGJuTnNZWFJsV1Nnd0tTQnpZMkZzWlNneEtUdGNiaUFnZlZ4dWZWeHVYRzVBYTJWNVpuSmhiV1Z6SUdGc1kyaGxiWGt0Wm14NUxYZ2dlMXh1SUNCbWNtOXRJSHRjYmlBZ0lDQnZjR0ZqYVhSNU9pQjJZWElvTFMxcGJtbDBhV0ZzTFc5d1lXTnBkSGtwTzF4dUlDQWdJSFJ5WVc1elptOXliVG9nZEhKaGJuTnNZWFJsV0NoMllYSW9MUzF2Wm1aelpYUXBLU0J6WTJGc1pTZ3dLVHRjYmlBZ2ZWeHVJQ0IwYnlCN1hHNGdJQ0FnYjNCaFkybDBlVG9nZG1GeUtDMHRabWx1WVd3dGIzQmhZMmwwZVNrN1hHNGdJQ0FnZEhKaGJuTm1iM0p0T2lCMGNtRnVjMnhoZEdWWUtEQXBJSE5qWVd4bEtERXBPMXh1SUNCOVhHNTlYRzVjYmtCclpYbG1jbUZ0WlhNZ1lXeGphR1Z0ZVMxa2NtOXdJSHRjYmlBZ1puSnZiU0I3WEc0Z0lDQWdiM0JoWTJsMGVUb2dkbUZ5S0MwdGFXNXBkR2xoYkMxdmNHRmphWFI1S1R0Y2JpQWdJQ0IwY21GdWMyWnZjbTA2SUhSeVlXNXpiR0YwWlZrb2RtRnlLQzB0YjJabWMyVjBLU2s3WEc0Z0lIMWNiaUFnZEc4Z2UxeHVJQ0FnSUc5d1lXTnBkSGs2SUhaaGNpZ3RMV1pwYm1Gc0xXOXdZV05wZEhrcE8xeHVJQ0FnSUhSeVlXNXpabTl5YlRvZ2RISmhibk5zWVhSbFdTZ3dLVHRjYmlBZ2ZWeHVmVnh1WEc1QWEyVjVabkpoYldWeklISmxjR3h2TFhOd2FXNGdlMXh1SUNCMGJ5QjdYRzRnSUNBZ2RISmhibk5tYjNKdE9pQnliM1JoZEdVb016WXdaR1ZuS1R0Y2JpQWdmVnh1ZlZ4dVhHNUFhMlY1Wm5KaGJXVnpJSE5vYVcxdFpYSWdlMXh1SUNBeE1EQWxJSHRjYmlBZ0lDQnRZWE5yTFhCdmMybDBhVzl1T2lCc1pXWjBYRzRnSUgxY2JuMWNibHh1TG5KbGNHeHZMV0Z1YVcxaGRHVXRjM0JwYm01bGNpQjdYRzRnSUdGdWFXMWhkR2x2YmpvZ2NtVndiRzh0YzNCcGJpQXhjeUJzYVc1bFlYSWdhVzVtYVc1cGRHVTdYRzU5WEc1Y2JpOHZJRTVQVkVVZ0tFcGhZMnR6YjI0c0lESXdNalF0TVRFdE1qRXBPaUJVYUdseklIQnpaWFZrYnkxbGJHVnRaVzUwSUdoaFkyc2dhWE1nYUdWeVpTQnBiaUJ5WldkaGNtUnpJSFJ2SUZKRlVFd3RNVEkyT0RRZ0xWeHVMeThnZEdobGNtVWdjMlZsYlhNZ2RHOGdZbVVnWVNCaWRXY2dkMmwwYUNCMGFHVWdZWEpwWVd0cGRDQjBiMjlzZEdsd0lHTnZiWEJ2Ym1WdWRDQjBhR0YwSUdOaGJtNXZkQ0JpWlNCbWFYaGxaQ0IzYVhSb1hHNHZMeUJ6ZEdGdVpHRnlaQ0JqYzNNZ2JtOXlJR2x6SUdsMElIZHZjblJvSUhWeklIZHlhWFJwYm1jZ1lTQmpkWE4wYjIwZ1kyOXRjRzl1Wlc1MElHWnZjaUJoZENCMGFHbHpJSFJwYldWY2JpNTBiMjlzZEdsd0xXRnljbTkzT2pwaVpXWnZjbVVnZTF4dUlDQmpiMjUwWlc1ME9pQmNJbHdpTzF4dUlDQndiM05wZEdsdmJqb2dZV0p6YjJ4MWRHVTdYRzRnSUhSdmNEb2dMVEF1TjNCNE8xeHVJQ0JzWldaME9pQXdPMXh1SUNCeWFXZG9kRG9nTUR0Y2JpQWdhR1ZwWjJoME9pQXhjSGc3WEc0Z0lHSmhZMnRuY205MWJtUTZJSGRvYVhSbE8xeHVJQ0IzYVdSMGFEb2dOekVsTzF4dUlDQnRZWEpuYVc0dGJHVm1kRG9nWVhWMGJ6dGNiaUFnYldGeVoybHVMWEpwWjJoME9pQmhkWFJ2TzF4dWZWeHVYRzR2THlCRGIyeHNZWEJ6YVdKc1pTQmhibWx0WVhScGIyNGdjM1I1YkdWelhHNWJaR0YwWVMxeVpYQnNieTFqYjJ4c1lYQnphV0pzWlYwZ0xuSmxjR3h2TFdGdWFXMWhkR1ZrSUh0Y2JpQWdiM1psY21ac2IzYzZJR2hwWkdSbGJqdGNibjFjYmx0a1lYUmhMWEpsY0d4dkxXTnZiR3hoY0hOcFlteGxYU0F1Y21Wd2JHOHRZVzVwYldGMFpXUmJaR0YwWVMxemRHRjBaVDFjSW05d1pXNWNJbDBnZTF4dUlDQmhibWx0WVhScGIyNDZJSE5zYVdSbFJHOTNiaUF5TURCdGN5QmpkV0pwWXkxaVpYcHBaWElvTUM0MExDQXdMQ0F3TGpJc0lERXBPMXh1ZlZ4dVcyUmhkR0V0Y21Wd2JHOHRZMjlzYkdGd2MybGliR1ZkSUM1eVpYQnNieTFoYm1sdFlYUmxaRnRrWVhSaExYTjBZWFJsUFZ3aVkyeHZjMlZrWENKZElIdGNiaUFnWVc1cGJXRjBhVzl1T2lCemJHbGtaVlZ3SURJd01HMXpJR04xWW1sakxXSmxlbWxsY2lnd0xqUXNJREFzSURBdU1pd2dNU2s3WEc1OVhHNWNia0JyWlhsbWNtRnRaWE1nYzJ4cFpHVkViM2R1SUh0Y2JpQWdabkp2YlNCN1hHNGdJQ0FnYUdWcFoyaDBPaUF3TzF4dUlDQjlYRzRnSUhSdklIdGNiaUFnSUNCb1pXbG5hSFE2SUhaaGNpZ3RMWEpoWkdsNExXTnZiR3hoY0hOcFlteGxMV052Ym5SbGJuUXRhR1ZwWjJoMEtUdGNiaUFnZlZ4dWZWeHVYRzVBYTJWNVpuSmhiV1Z6SUhOc2FXUmxWWEFnZTF4dUlDQm1jbTl0SUh0Y2JpQWdJQ0JvWldsbmFIUTZJSFpoY2lndExYSmhaR2w0TFdOdmJHeGhjSE5wWW14bExXTnZiblJsYm5RdGFHVnBaMmgwS1R0Y2JpQWdmVnh1SUNCMGJ5QjdYRzRnSUNBZ2FHVnBaMmgwT2lBd08xeHVJQ0I5WEc1OVhHNWNiaTV5WlhCc2J5MXpjaTF2Ym14NUlIdGNiaUFnY0c5emFYUnBiMjQ2SUdGaWMyOXNkWFJsTzF4dUlDQjNhV1IwYURvZ01YQjRPMXh1SUNCb1pXbG5hSFE2SURGd2VEdGNiaUFnY0dGa1pHbHVaem9nTUR0Y2JpQWdiV0Z5WjJsdU9pQXRNWEI0TzF4dUlDQnZkbVZ5Wm14dmR6b2dhR2xrWkdWdU8xeHVJQ0JqYkdsd09pQnlaV04wS0RBc0lEQXNJREFzSURBcE8xeHVJQ0IzYUdsMFpTMXpjR0ZqWlRvZ2JtOTNjbUZ3TzF4dUlDQmliM0prWlhJdGQybGtkR2c2SURBN1hHNTlYRzVjYmx0a1lYUmhMWEpsY0d4dkxXTnZiWEJ2Ym1WdWRDMXliMjkwUFZ3aVkyRnliM1Z6Wld4Y0lsMGdlMXh1SUNBbU9uZG9aWEpsS0Z0a1lYUmhMWEpsY0d4dkxYQmhjblF0YVdROVhDSnpiR2xrWlMxMGNtRmphMXdpWFNrZ2UxeHVJQ0FnSUhOamNtOXNiR0poY2kxM2FXUjBhRG9nYm05dVpUdGNiaUFnSUNBbU9qb3RkMlZpYTJsMExYTmpjbTlzYkdKaGNpQjdYRzRnSUNBZ0lDQmthWE53YkdGNU9pQnViMjVsTzF4dUlDQWdJSDFjYmlBZ2ZWeHVmVnh1SWl3aVFHMXBlR2x1SUhKcFkyZ3RkR1Y0ZEMxemRIbHNaWE1nZTF4dUlDQmhMRnh1SUNCd0xGeHVJQ0J6TEZ4dUlDQjFMRnh1SUNCaUxGeHVJQ0JwTEZ4dUlDQm9NU3hjYmlBZ2FESXNYRzRnSUdnekxGeHVJQ0JvTkN4Y2JpQWdhRFVzWEc0Z0lHZzJMRnh1SUNCdFlYSnJJSHRjYmlBZ0lDQm1iMjUwTFhOMGVXeGxPaUJwYm1obGNtbDBPMXh1SUNBZ0lHWnZiblF0Wm1GdGFXeDVPaUJwYm1obGNtbDBPMXh1SUNBZ0lIUmxlSFF0WkdWamIzSmhkR2x2YmpvZ2FXNW9aWEpwZER0Y2JpQWdJQ0IwWlhoMExXRnNhV2R1T2lCcGJtaGxjbWwwTzF4dUlDQWdJSFJsZUhRdGRISmhibk5tYjNKdE9pQnBibWhsY21sME8xeHVJQ0FnSUdOdmJHOXlPaUJwYm1obGNtbDBPMXh1SUNBZ0lHeHBibVV0YUdWcFoyaDBPaUJwYm1obGNtbDBPMXh1WEc0Z0lDQWdiR1YwZEdWeUxYTndZV05wYm1jNklHbHVhR1Z5YVhRN1hHNGdJQ0FnYldGeVoybHVPaUF3TzF4dUlDQWdJSEJoWkdScGJtYzZJREE3WEc0Z0lDQWdZbTl5WkdWeU9pQXdPMXh1SUNBZ0lHWnZiblF0ZDJWcFoyaDBPaUJwYm1obGNtbDBPMXh1SUNBZ0lIWmxjblJwWTJGc0xXRnNhV2R1T2lCaVlYTmxiR2x1WlR0Y2JpQWdJQ0JtYjI1MExYTnBlbVU2SURFd01DVTdYRzRnSUNBZ0x5OGdUbTkwWlNBb1RtOWhhQ3dnVWtWUVRDMDBNRGszS1RvZ2RHVjRkQzF6YVhwbExXRmthblZ6ZENCd2NtVjJaVzUwY3lCcFQxTWdjMkZtWVhKcElHWnliMjFjYmlBZ0lDQXZMeUJwYm1ac1lYUnBibWNnZEdWNGRDQnphWHBsWEc0Z0lDQWdMeThnYUhSMGNITTZMeTlyYVd4cFlXNTJZV3hyYUc5bUxtTnZiUzh5TURJeUwyTnpjeTFvZEcxc0wzbHZkWEl0WTNOekxYSmxjMlYwTFc1bFpXUnpMWFJsZUhRdGMybDZaUzFoWkdwMWMzUXRjSEp2WW1GaWJIa3ZYRzRnSUNBZ0xXMXZlaTEwWlhoMExYTnBlbVV0WVdScWRYTjBPaUJ1YjI1bE8xeHVJQ0FnSUMxM1pXSnJhWFF0ZEdWNGRDMXphWHBsTFdGa2FuVnpkRG9nYm05dVpUdGNiaUFnSUNCMFpYaDBMWE5wZW1VdFlXUnFkWE4wT2lCdWIyNWxPMXh1WEc0Z0lDQWdMeThnU0dsa1pTQnpZM0p2Ykd4aVlYSnpJR0o1SUdSbFptRjFiSFJjYmlBZ0lDQW1Pam90ZDJWaWEybDBMWE5qY205c2JHSmhjaUI3WEc0Z0lDQWdJQ0JrYVhOd2JHRjVPaUJ1YjI1bE8xeHVJQ0FnSUgxY2JpQWdJQ0F0YlhNdGIzWmxjbVpzYjNjdGMzUjViR1U2SUc1dmJtVTdYRzRnSUNBZ2MyTnliMnhzWW1GeUxYZHBaSFJvT2lCdWIyNWxPMXh1SUNCOVhHNWNiaUFnWWl4Y2JpQWdjM1J5YjI1bkxGeHVJQ0IxTEZ4dUlDQnBMRnh1SUNCbGJTeGNiaUFnY3l4Y2JpQWdaR1ZzTEZ4dUlDQnNhU3hjYmlBZ2MzQmhiaUI3WEc0Z0lDQWdabTl1ZEMxbVlXMXBiSGs2SUdsdWFHVnlhWFE3WEc0Z0lIMWNibHh1SUNCMUlIdGNiaUFnSUNCMFpYaDBMV1JsWTI5eVlYUnBiMjQ2SUhWdVpHVnliR2x1WlR0Y2JpQWdmVnh1WEc0Z0lITXNYRzRnSUdSbGJDQjdYRzRnSUNBZ2RHVjRkQzFrWldOdmNtRjBhVzl1T2lCc2FXNWxMWFJvY205MVoyZzdYRzRnSUgxY2JseHVJQ0JwSUh0Y2JpQWdJQ0JtYjI1MExYTjBlV3hsT2lCcGRHRnNhV003WEc0Z0lIMWNibHh1SUNCaUlIdGNiaUFnSUNCbWIyNTBMWGRsYVdkb2REb2dZbTlzWkR0Y2JpQWdmVnh1WEc0Z0lDOHZJRTV2ZEdVZ0tFNXZZV2dzSURJd01qRXRNRGt0TURrcE9pQlVhR2x6SUdseklHNWxZMlZ6YzJGeWVTQmlaV05oZFhObElITnZiV1VnZEdobGJXVnpJQ2hzYVd0bElHUmxZblYwUHo4cElHaGhkbVVnWTNOeklISmxjMlYwYzF4dUlDQXZMeUIzYUdsamFDQnpaWFFnYkdsemRDMXpkSGxzWlNCMGJ5QnViMjVsTGlCWFpTQnlaWE5sZENCaVlXTnJJSFJ2SUdsdWFHVnlhWFFnYzI4Z2RHaGhkQ0JpZFd4c1pYUWdiR2x6ZENCaWRXeHNaWFJ6SUdGamRIVmhiR3g1SUhOb2IzY2dkWEJjYmlBZ2RXd3NYRzRnSUd4cElIdGNiaUFnSUNCc2FYTjBMWE4wZVd4bE9pQnBibWhsY21sME8xeHVJQ0FnSUM4dklGUm9hWE1nYVhNZ2QyVnBjbVFzSUdKMWRDQmlkV3hzWlhRZ2NHOXBiblJ6SUdSdmJpZDBJR2hoZG1VZ2NHRmtaR2x1WnlCaWVTQmtaV1poZFd4MElHbHVJRkpVUlZ4dUlDQWdJQzh2SUhOcGJtTmxJSGRsSUhKbGMyVjBJSFJvWldseUlIQmhaR1JwYm1jZ1lXSnZkbVVzSUhkb2FXTm9JRzFsWVc1eklIUm9aWGtnY21WdVpHVnlJR2x1WTI5eWNtVmpkR3g1WEc0Z0lDQWdMeThnZEc4Z2RHaGxJR3hsWm5RdUlGTmxkQ0IwYUdWdElIUnZJR0Z1SUdGeVltbDBjbUZ5ZVNCMllXeDFaU0IwYnlCdFlXdGxJSFJvWlcwZ2JHOXZheUJuYjI5a0lDaDFjMlZjYmlBZ0lDQXZMeUJsYlNCMGJ5QnpZMkZzWlNCM2FYUm9JSFJvWlNCbWIyNTBJSE5wZW1VcFhHNGdJQ0FnY0dGa1pHbHVaeTFzWldaME9pQXhMamRsYlR0Y2JpQWdmVnh1WEc0Z0lHTnZaR1VnZTF4dUlDQWdJR0poWTJ0bmNtOTFibVF0WTI5c2IzSTZJSEpuWW1Fb0l6WXhOakUyTVN3Z01DNHhLVHRjYmlBZ0lDQmpiMnh2Y2pvZ0l6WXhOakUyTVR0Y2JpQWdmVnh1WEc0Z0lIQnlaU0I3WEc0Z0lDQWdZbUZqYTJkeWIzVnVaRG9nSXpCa01HUXdaRHRjYmlBZ0lDQmpiMnh2Y2pvZ0kyWm1aanRjYmlBZ0lDQm1iMjUwTFdaaGJXbHNlVG9nWENKS1pYUkNjbUZwYm5OTmIyNXZYQ0lzSUcxdmJtOXpjR0ZqWlR0Y2JpQWdJQ0J3WVdSa2FXNW5PaUF3TGpjMWNtVnRJREZ5WlcwN1hHNGdJQ0FnWW05eVpHVnlMWEpoWkdsMWN6b2dNQzQxY21WdE8xeHVYRzRnSUNBZ1kyOWtaU0I3WEc0Z0lDQWdJQ0JqYjJ4dmNqb2dhVzVvWlhKcGREdGNiaUFnSUNBZ0lIQmhaR1JwYm1jNklEQTdYRzRnSUNBZ0lDQmlZV05yWjNKdmRXNWtPaUJ1YjI1bE8xeHVJQ0FnSUNBZ1ptOXVkQzF6YVhwbE9pQXdMamh5WlcwN1hHNGdJQ0FnZlZ4dUlDQjlYRzVjYmlBZ2FXMW5JSHRjYmlBZ0lDQnRZWGd0ZDJsa2RHZzZJREV3TUNVN1hHNGdJQ0FnYUdWcFoyaDBPaUJoZFhSdk8xeHVJQ0I5WEc1Y2JpQWdZbXh2WTJ0eGRXOTBaU0I3WEc0Z0lDQWdjR0ZrWkdsdVp5MXNaV1owT2lBeGNtVnRPMXh1SUNBZ0lHSnZjbVJsY2kxc1pXWjBPaUF5Y0hnZ2MyOXNhV1FnY21kaVlTZ2pNR1F3WkRCa0xDQXdMakVwTzF4dUlDQjlYRzVjYmlBZ2FISWdlMXh1SUNBZ0lHSnZjbVJsY2pvZ2JtOXVaVHRjYmlBZ0lDQmliM0prWlhJdGRHOXdPaUF5Y0hnZ2MyOXNhV1FnY21kaVlTZ2pNR1F3WkRCa0xDQXdMakVwTzF4dUlDQWdJRzFoY21kcGJqb2dNbkpsYlNBd08xeHVJQ0I5WEc1OVhHNGlYWDA9ICovIiwiQG1peGluIHJpY2gtdGV4dC1zdHlsZXMge1xuICBhLFxuICBwLFxuICBzLFxuICB1LFxuICBiLFxuICBpLFxuICBoMSxcbiAgaDIsXG4gIGgzLFxuICBoNCxcbiAgaDUsXG4gIGg2LFxuICBtYXJrIHtcbiAgICBmb250LXN0eWxlOiBpbmhlcml0O1xuICAgIGZvbnQtZmFtaWx5OiBpbmhlcml0O1xuICAgIHRleHQtZGVjb3JhdGlvbjogaW5oZXJpdDtcbiAgICB0ZXh0LWFsaWduOiBpbmhlcml0O1xuICAgIHRleHQtdHJhbnNmb3JtOiBpbmhlcml0O1xuICAgIGNvbG9yOiBpbmhlcml0O1xuICAgIGxpbmUtaGVpZ2h0OiBpbmhlcml0O1xuXG4gICAgbGV0dGVyLXNwYWNpbmc6IGluaGVyaXQ7XG4gICAgbWFyZ2luOiAwO1xuICAgIHBhZGRpbmc6IDA7XG4gICAgYm9yZGVyOiAwO1xuICAgIGZvbnQtd2VpZ2h0OiBpbmhlcml0O1xuICAgIHZlcnRpY2FsLWFsaWduOiBiYXNlbGluZTtcbiAgICBmb250LXNpemU6IDEwMCU7XG4gICAgLy8gTm90ZSAoTm9haCwgUkVQTC00MDk3KTogdGV4dC1zaXplLWFkanVzdCBwcmV2ZW50cyBpT1Mgc2FmYXJpIGZyb21cbiAgICAvLyBpbmZsYXRpbmcgdGV4dCBzaXplXG4gICAgLy8gaHR0cHM6Ly9raWxpYW52YWxraG9mLmNvbS8yMDIyL2Nzcy1odG1sL3lvdXItY3NzLXJlc2V0LW5lZWRzLXRleHQtc2l6ZS1hZGp1c3QtcHJvYmFibHkvXG4gICAgLW1vei10ZXh0LXNpemUtYWRqdXN0OiBub25lO1xuICAgIC13ZWJraXQtdGV4dC1zaXplLWFkanVzdDogbm9uZTtcbiAgICB0ZXh0LXNpemUtYWRqdXN0OiBub25lO1xuXG4gICAgLy8gSGlkZSBzY3JvbGxiYXJzIGJ5IGRlZmF1bHRcbiAgICAmOjotd2Via2l0LXNjcm9sbGJhciB7XG4gICAgICBkaXNwbGF5OiBub25lO1xuICAgIH1cbiAgICAtbXMtb3ZlcmZsb3ctc3R5bGU6IG5vbmU7XG4gICAgc2Nyb2xsYmFyLXdpZHRoOiBub25lO1xuICB9XG5cbiAgYixcbiAgc3Ryb25nLFxuICB1LFxuICBpLFxuICBlbSxcbiAgcyxcbiAgZGVsLFxuICBsaSxcbiAgc3BhbiB7XG4gICAgZm9udC1mYW1pbHk6IGluaGVyaXQ7XG4gIH1cblxuICB1IHtcbiAgICB0ZXh0LWRlY29yYXRpb246IHVuZGVybGluZTtcbiAgfVxuXG4gIHMsXG4gIGRlbCB7XG4gICAgdGV4dC1kZWNvcmF0aW9uOiBsaW5lLXRocm91Z2g7XG4gIH1cblxuICBpIHtcbiAgICBmb250LXN0eWxlOiBpdGFsaWM7XG4gIH1cblxuICBiIHtcbiAgICBmb250LXdlaWdodDogYm9sZDtcbiAgfVxuXG4gIC8vIE5vdGUgKE5vYWgsIDIwMjEtMDktMDkpOiBUaGlzIGlzIG5lY2Vzc2FyeSBiZWNhdXNlIHNvbWUgdGhlbWVzIChsaWtlIGRlYnV0Pz8pIGhhdmUgY3NzIHJlc2V0c1xuICAvLyB3aGljaCBzZXQgbGlzdC1zdHlsZSB0byBub25lLiBXZSByZXNldCBiYWNrIHRvIGluaGVyaXQgc28gdGhhdCBidWxsZXQgbGlzdCBidWxsZXRzIGFjdHVhbGx5IHNob3cgdXBcbiAgdWwsXG4gIGxpIHtcbiAgICBsaXN0LXN0eWxlOiBpbmhlcml0O1xuICAgIC8vIFRoaXMgaXMgd2VpcmQsIGJ1dCBidWxsZXQgcG9pbnRzIGRvbid0IGhhdmUgcGFkZGluZyBieSBkZWZhdWx0IGluIFJURVxuICAgIC8vIHNpbmNlIHdlIHJlc2V0IHRoZWlyIHBhZGRpbmcgYWJvdmUsIHdoaWNoIG1lYW5zIHRoZXkgcmVuZGVyIGluY29ycmVjdGx5XG4gICAgLy8gdG8gdGhlIGxlZnQuIFNldCB0aGVtIHRvIGFuIGFyYml0cmFyeSB2YWx1ZSB0byBtYWtlIHRoZW0gbG9vayBnb29kICh1c2VcbiAgICAvLyBlbSB0byBzY2FsZSB3aXRoIHRoZSBmb250IHNpemUpXG4gICAgcGFkZGluZy1sZWZ0OiAxLjdlbTtcbiAgfVxuXG4gIGNvZGUge1xuICAgIGJhY2tncm91bmQtY29sb3I6IHJnYmEoIzYxNjE2MSwgMC4xKTtcbiAgICBjb2xvcjogIzYxNjE2MTtcbiAgfVxuXG4gIHByZSB7XG4gICAgYmFja2dyb3VuZDogIzBkMGQwZDtcbiAgICBjb2xvcjogI2ZmZjtcbiAgICBmb250LWZhbWlseTogXCJKZXRCcmFpbnNNb25vXCIsIG1vbm9zcGFjZTtcbiAgICBwYWRkaW5nOiAwLjc1cmVtIDFyZW07XG4gICAgYm9yZGVyLXJhZGl1czogMC41cmVtO1xuXG4gICAgY29kZSB7XG4gICAgICBjb2xvcjogaW5oZXJpdDtcbiAgICAgIHBhZGRpbmc6IDA7XG4gICAgICBiYWNrZ3JvdW5kOiBub25lO1xuICAgICAgZm9udC1zaXplOiAwLjhyZW07XG4gICAgfVxuICB9XG5cbiAgaW1nIHtcbiAgICBtYXgtd2lkdGg6IDEwMCU7XG4gICAgaGVpZ2h0OiBhdXRvO1xuICB9XG5cbiAgYmxvY2txdW90ZSB7XG4gICAgcGFkZGluZy1sZWZ0OiAxcmVtO1xuICAgIGJvcmRlci1sZWZ0OiAycHggc29saWQgcmdiYSgjMGQwZDBkLCAwLjEpO1xuICB9XG5cbiAgaHIge1xuICAgIGJvcmRlcjogbm9uZTtcbiAgICBib3JkZXItdG9wOiAycHggc29saWQgcmdiYSgjMGQwZDBkLCAwLjEpO1xuICAgIG1hcmdpbjogMnJlbSAwO1xuICB9XG59XG4iXX0= */</style><style id=\"alchemy-runtime-css\">\n    html,\n    body {\n      zoom: unset !important;\n    }\n\n    body {\n      overflow-y: visible !important;\n    }\n      \n     </style><div class=\"alchemy__element alchemy-reset overflow-clip\" style=\"--replo-library-e922e3a7-4a8e-4498-8076-ba24179a7c0d-styles-0c0ddff2-0cf2-49fe-9286-c0e56e24d535-attributes-color:linear-gradient(0deg, #F9D6E6FF 0%, #FBF0F5FF 45.54455445544554%, #FFCDFFFF 99.00990099009901%)\"><div data-rid=\"bea1f1b1-0834-4988-af8b-0a766a46d4eb\" class=\"r-7j4tqq\"><div data-rid=\"9721d159-58fc-4472-ba38-4c245085b98a\" class=\"r-j2sy39\"><div data-rid=\"c03ab775-a6d5-4683-9957-c14601a53cc4\" class=\"r-r27skf\"><div data-rid=\"2271bd9d-ff05-4c84-8423-d9c7dbb4a2fb\" class=\"r-ezfs0b\"><div data-rid=\"58d1a395-d6a5-4fa1-9325-0b509a3e98b7\" class=\"r-1bo4aav\"><picture data-rid=\"9247a029-6bef-4f90-8026-2e38c06217f3\" class=\"r-1s78z59\"><source srcSet=\"https://assets.replocdn.com/projects/07bd1984-3d87-4861-82a3-4f94a264d106/3c101d37-3fae-4792-97ae-36a821708b16?width=820\" media=\"(max-width: 640px)\"/><source srcSet=\"https://assets.replocdn.com/projects/07bd1984-3d87-4861-82a3-4f94a264d106/3c101d37-3fae-4792-97ae-36a821708b16?width=1024\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"https://assets.replocdn.com/projects/07bd1984-3d87-4861-82a3-4f94a264d106/3c101d37-3fae-4792-97ae-36a821708b16?width=1800\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"https://assets.replocdn.com/projects/07bd1984-3d87-4861-82a3-4f94a264d106/3c101d37-3fae-4792-97ae-36a821708b16\" class=\"r-lw7hi5\" loading=\"eager\"/></picture></div><div data-rid=\"02081aed-e906-482e-8fd8-d770b93db6db\" class=\"r-a6k0t4\"><div data-rid=\"487d18db-eaa2-4647-8859-ef27579d7e78\" class=\"r-hif9da alchemy-rte\"><span style=\"width:100%\"><p>SÉLECTION > Sensibilités</p></span></div><div data-rid=\"ca5f1e20-947b-4351-9f7a-8f0b175c92bc\" class=\"r-149zdz0 alchemy-rte\"><span style=\"width:100%\"><h4>Sensibilités</h4></span></div></div></div><div class=\"r-1qycgw5\" data-rid=\"1\"><div data-rid=\"5cfd7743-305e-4676-9f25-7e24e3cbcafe\" class=\"r-l6nzmn\"><div data-rid=\"eed1e599-bf12-4e99-ac49-1d67a047e996\" class=\"r-91w9n\"><div data-rid=\"7adcb3cd-fd4c-4e3d-9946-ff2c08ce200f\" class=\"r-4zqa5c\"><div data-rid=\"1787c519-7b4a-40a2-abd4-965381728b3a\" class=\"r-yytsoj alchemy-rte\"><span style=\"width:100%\"><p>La douceur comme base</p></span></div><div data-rid=\"d6385b83-18bf-49c6-bee5-819ed7590d4a\" class=\"r-1m8udl0 alchemy-rte\"><span style=\"width:100%\"><p>Rougeurs, tiraillements, inconfort ? Tous nos soins sont formulés sans parfum, sans perturbateurs et testés sur peaux sensibles pour un apaisement immédiat.</p></span></div></div></div><div data-rid=\"eba9db1d-6942-47d2-a9b0-ca7461da72f2\" class=\"r-10qskm8\"><div class=\"r-7vb50c\" data-rid=\"1\"><div data-rid=\"b78bc5a1-6313-4b76-a713-def2a924ba10\" class=\"r-18oi2t1\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign reploOriginalProductR1qr2 = product %}<!-- -->{% capture productHandle %}granite-demaquillant{% endcapture %}<!-- -->{% assign product = all_products[productHandle] %}<!-- -->{% assign reploOriginalProductVariantR1qr2 = reploSelectedVariant %}<!-- -->{% assign reploSelectedVariant = blank %}<!-- -->{% assign reploOriginalSPGR1qr2 = reploSortedSellingPlans %}<!-- -->{% assign reploSortedSellingPlans = blank %}<!-- -->{% assign reploOriginalSSPR1qr2 = reploSelectedSellingPlan %}<!-- -->{% assign reploSelectedSellingPlan = blank %}<!-- -->{% assign reploOriginalSSPPriceR1qr2 = reploSelectedSellingPlanPrice %}<!-- -->{% assign reploSelectedSellingPlanPrice = blank %}<!-- -->{% assign reploOriginalComparePricePercentR1qr2 = reploCompareAtPriceDifferencePercentage %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = blank %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<!-- -->{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% capture reploVariantIdString %}null{% endcapture %}<!-- -->{% capture reploSellingPlanIdString %}null{% endcapture %}<!-- -->{% capture reploIdKey %}id{% endcapture %}<!-- -->{% capture reploPercentageKey %}percentage{% endcapture %}<!-- -->{% capture reploPriceKey %}price{% endcapture %}<!-- -->{% capture reploFixedAmountKey %}fixed_amount{% endcapture %}<!-- -->{% capture spKey %}selling_plan{% endcapture %}<!-- -->{%- liquid\n              assign reploVariantId = reploVariantIdString | times: 1\n              assign reploSelectedVariant = product.variants | where: reploIdKey, reploVariantId | first\n              if reploSelectedVariant == blank\n                assign reploSelectedVariant = product.selected_or_first_available_variant\n              endif\n              assign reploSelectedSellingPlanPrice = reploSelectedVariant.price\n              if product.selling_plan_groups[0]\n                assign reploAllSellingPlans = reploSelectedVariant.selling_plan_allocations | map: spKey\n                assign reploSortedSellingPlans = reploAllSellingPlans | sort: reploIdKey\n                if true\n                  assign reploSellingPlanId = reploSellingPlanIdString | times: 1\n                  assign reploSelectedSellingPlan = reploSortedSellingPlans | where: reploIdKey, reploSellingPlanId | first\n                  if reploSelectedSellingPlan.price_adjustments[0]\n                    assign adjustment = reploSelectedSellingPlan.price_adjustments[0]\n                    case adjustment.value_type\n                      when reploPercentageKey\n                        assign amountOff = 100 | minus: adjustment.value\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | times: amountOff | divided_by: 100\n                      when reploFixedAmountKey\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | minus: adjustment.value\n                      when reploPriceKey\n                        assign reploSelectedSellingPlanPrice = adjustment.value\n                    endcase\n                  endif\n                endif\n              endif\n            -%}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = 0 %}<!-- -->{% if reploSelectedVariant.compare_at_price != blank %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploSelectedVariant.compare_at_price | minus: reploSelectedVariant.price | at_least: 0 | times: 100.0 | divided_by: reploSelectedVariant.compare_at_price | round %}<!-- -->{% endif %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<div data-rid=\"3e33de33-35fe-4377-9b2e-1d524583f211\" tabindex=\"0\" role=\"button\" class=\"r-3wqav1\" data-replo-product-container=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" data-replo-product-handle=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.handle}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"><product-form style=\"display:none\"><form id=\"product-form-{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" method=\"post\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" encType=\"multipart/form-data\" action=\"/cart/add\" data-type=\"add-to-cart-form\"><input type=\"hidden\" name=\"id\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{reploSelectedVariant.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/><input type=\"hidden\" name=\"quantity\" value=\"1\"/><input type=\"hidden\" name=\"selling_plan\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- if reploSelectedSellingPlan != blank -%}{{reploSelectedSellingPlan.id}}{%- endif -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/></form></product-form><div data-rid=\"fbbe34de-df28-4f44-9b7e-4ed4dc8236a5\" class=\"r-1mpddo7\"><picture data-rid=\"d3142973-6c0e-43a0-920e-29876fa7d278\" style=\"--replo-attributes-product-featured-image:{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-k1cg7v\"><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 820  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(max-width: 640px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1024  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1800  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-1q9wyug\" loading=\"lazy\"/></picture></div><div data-rid=\"957b0ef9-ea5d-4546-8313-c1a19abf2251\" class=\"r-1t9z0rt\"><div data-rid=\"22f41a95-057b-435c-a610-efd07877de2d\" class=\"r-1hv3zq0\"><div data-rid=\"1c1dd2f1-95fa-42f5-a096-a360409ed374\" class=\"r-b3etsn\"><div data-rid=\"1345cec2-2fc7-4b0d-9862-577da99e0b4a\" class=\"r-1tl33ne alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.title }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div></div><div data-rid=\"6e8bc39b-9c5f-46d9-9f94-acb4661c792a\" class=\"r-3ahe6n\"><div data-rid=\"e451734e-3106-4d93-b1a4-c915b55aabd8\" class=\"r-13zoknt\"><div data-rid=\"aef8c280-53e4-4f72-8a43-5ffa7e12b847\" class=\"r-tkc5vq\"><div data-rid=\"3f5a9e55-6e10-4cd6-bace-425ffa91b244\" class=\"r-1t3wmhi alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}ml{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div><div data-rid=\"eceb06ee-7dae-4be5-a498-bfc7ffc50ba5\" class=\"r-1eg4q9m\"><div data-rid=\"f6b9750d-6dcb-43d6-9f88-a98fa2cd27b2\" class=\"r-f0cd5i alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}made_in_france{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div></div><div data-rid=\"fb440d47-8823-40ec-a826-1d3768015813\" class=\"r-3lgm8x\"><div data-rid=\"a7652791-463d-4d29-822f-b4ec07848824\" class=\"r-1hp0s62\"><div data-rid=\"86c45cb5-197e-473e-972f-06d91d51c4b2\" class=\"r-14ja0os alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ reploSelectedSellingPlanPrice  | divided_by: 100.0 | round | times: 100.0 | money_without_trailing_zeros}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div><div data-rid=\"1b1b9ba2-c533-4afb-9a76-b8fe293a4368\" class=\"r-b1rhd6\"><div data-rid=\"0608cac0-cb36-4ec7-88ef-2c7d4beacc3d\" class=\"r-1xj1yl2\"><span style=\"display:contents\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-arrow-up-right\" style=\"fill: none;stroke: currentColor;width: var(--rsw, 100%);height: 100%\" role=\"presentation\"><line x1=\"7\" y1=\"17\" x2=\"17\" y2=\"7\"></line><polyline points=\"7 7 17 7 17 17\"></polyline></svg></span></div></div></div></div></div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign product = reploOriginalProductR1qr2 %}<!-- -->{% assign reploSelectedVariant = reploOriginalProductVariantR1qr2 %}<!-- -->{% assign reploSortedSellingPlans = reploOriginalSPGR1qr2 %}<!-- -->{% assign reploSelectedSellingPlan = reploOriginalSSPR1qr2 %}<!-- -->{% assign reploSelectedSellingPlanPrice = reploOriginalSSPPriceR1qr2 %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploOriginalComparePricePercentR1qr2 %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign reploOriginalProductR2qr2 = product %}<!-- -->{% capture productHandle %}mousse-nettoyante{% endcapture %}<!-- -->{% assign product = all_products[productHandle] %}<!-- -->{% assign reploOriginalProductVariantR2qr2 = reploSelectedVariant %}<!-- -->{% assign reploSelectedVariant = blank %}<!-- -->{% assign reploOriginalSPGR2qr2 = reploSortedSellingPlans %}<!-- -->{% assign reploSortedSellingPlans = blank %}<!-- -->{% assign reploOriginalSSPR2qr2 = reploSelectedSellingPlan %}<!-- -->{% assign reploSelectedSellingPlan = blank %}<!-- -->{% assign reploOriginalSSPPriceR2qr2 = reploSelectedSellingPlanPrice %}<!-- -->{% assign reploSelectedSellingPlanPrice = blank %}<!-- -->{% assign reploOriginalComparePricePercentR2qr2 = reploCompareAtPriceDifferencePercentage %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = blank %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<!-- -->{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% capture reploVariantIdString %}null{% endcapture %}<!-- -->{% capture reploSellingPlanIdString %}null{% endcapture %}<!-- -->{% capture reploIdKey %}id{% endcapture %}<!-- -->{% capture reploPercentageKey %}percentage{% endcapture %}<!-- -->{% capture reploPriceKey %}price{% endcapture %}<!-- -->{% capture reploFixedAmountKey %}fixed_amount{% endcapture %}<!-- -->{% capture spKey %}selling_plan{% endcapture %}<!-- -->{%- liquid\n              assign reploVariantId = reploVariantIdString | times: 1\n              assign reploSelectedVariant = product.variants | where: reploIdKey, reploVariantId | first\n              if reploSelectedVariant == blank\n                assign reploSelectedVariant = product.selected_or_first_available_variant\n              endif\n              assign reploSelectedSellingPlanPrice = reploSelectedVariant.price\n              if product.selling_plan_groups[0]\n                assign reploAllSellingPlans = reploSelectedVariant.selling_plan_allocations | map: spKey\n                assign reploSortedSellingPlans = reploAllSellingPlans | sort: reploIdKey\n                if true\n                  assign reploSellingPlanId = reploSellingPlanIdString | times: 1\n                  assign reploSelectedSellingPlan = reploSortedSellingPlans | where: reploIdKey, reploSellingPlanId | first\n                  if reploSelectedSellingPlan.price_adjustments[0]\n                    assign adjustment = reploSelectedSellingPlan.price_adjustments[0]\n                    case adjustment.value_type\n                      when reploPercentageKey\n                        assign amountOff = 100 | minus: adjustment.value\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | times: amountOff | divided_by: 100\n                      when reploFixedAmountKey\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | minus: adjustment.value\n                      when reploPriceKey\n                        assign reploSelectedSellingPlanPrice = adjustment.value\n                    endcase\n                  endif\n                endif\n              endif\n            -%}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = 0 %}<!-- -->{% if reploSelectedVariant.compare_at_price != blank %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploSelectedVariant.compare_at_price | minus: reploSelectedVariant.price | at_least: 0 | times: 100.0 | divided_by: reploSelectedVariant.compare_at_price | round %}<!-- -->{% endif %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<div data-rid=\"3e33de33-35fe-4377-9b2e-1d524583f211\" tabindex=\"0\" role=\"button\" class=\"r-3wqav1\" data-replo-product-container=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" data-replo-product-handle=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.handle}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"><product-form style=\"display:none\"><form id=\"product-form-{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" method=\"post\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" encType=\"multipart/form-data\" action=\"/cart/add\" data-type=\"add-to-cart-form\"><input type=\"hidden\" name=\"id\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{reploSelectedVariant.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/><input type=\"hidden\" name=\"quantity\" value=\"1\"/><input type=\"hidden\" name=\"selling_plan\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- if reploSelectedSellingPlan != blank -%}{{reploSelectedSellingPlan.id}}{%- endif -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/></form></product-form><div data-rid=\"fbbe34de-df28-4f44-9b7e-4ed4dc8236a5\" class=\"r-1mpddo7\"><picture data-rid=\"d3142973-6c0e-43a0-920e-29876fa7d278\" style=\"--replo-attributes-product-featured-image:{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-k1cg7v\"><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 820  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(max-width: 640px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1024  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1800  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-1q9wyug\" loading=\"lazy\"/></picture></div><div data-rid=\"957b0ef9-ea5d-4546-8313-c1a19abf2251\" class=\"r-1t9z0rt\"><div data-rid=\"22f41a95-057b-435c-a610-efd07877de2d\" class=\"r-1hv3zq0\"><div data-rid=\"1c1dd2f1-95fa-42f5-a096-a360409ed374\" class=\"r-b3etsn\"><div data-rid=\"1345cec2-2fc7-4b0d-9862-577da99e0b4a\" class=\"r-1tl33ne alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.title }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div></div><div data-rid=\"6e8bc39b-9c5f-46d9-9f94-acb4661c792a\" class=\"r-3ahe6n\"><div data-rid=\"e451734e-3106-4d93-b1a4-c915b55aabd8\" class=\"r-13zoknt\"><div data-rid=\"aef8c280-53e4-4f72-8a43-5ffa7e12b847\" class=\"r-tkc5vq\"><div data-rid=\"3f5a9e55-6e10-4cd6-bace-425ffa91b244\" class=\"r-1t3wmhi alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}ml{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div><div data-rid=\"eceb06ee-7dae-4be5-a498-bfc7ffc50ba5\" class=\"r-1eg4q9m\"><div data-rid=\"f6b9750d-6dcb-43d6-9f88-a98fa2cd27b2\" class=\"r-f0cd5i alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}made_in_france{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div></div><div data-rid=\"fb440d47-8823-40ec-a826-1d3768015813\" class=\"r-3lgm8x\"><div data-rid=\"a7652791-463d-4d29-822f-b4ec07848824\" class=\"r-1hp0s62\"><div data-rid=\"86c45cb5-197e-473e-972f-06d91d51c4b2\" class=\"r-14ja0os alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ reploSelectedSellingPlanPrice  | divided_by: 100.0 | round | times: 100.0 | money_without_trailing_zeros}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div><div data-rid=\"1b1b9ba2-c533-4afb-9a76-b8fe293a4368\" class=\"r-b1rhd6\"><div data-rid=\"0608cac0-cb36-4ec7-88ef-2c7d4beacc3d\" class=\"r-1xj1yl2\"><span style=\"display:contents\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-arrow-up-right\" style=\"fill: none;stroke: currentColor;width: var(--rsw, 100%);height: 100%\" role=\"presentation\"><line x1=\"7\" y1=\"17\" x2=\"17\" y2=\"7\"></line><polyline points=\"7 7 17 7 17 17\"></polyline></svg></span></div></div></div></div></div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign product = reploOriginalProductR2qr2 %}<!-- -->{% assign reploSelectedVariant = reploOriginalProductVariantR2qr2 %}<!-- -->{% assign reploSortedSellingPlans = reploOriginalSPGR2qr2 %}<!-- -->{% assign reploSelectedSellingPlan = reploOriginalSSPR2qr2 %}<!-- -->{% assign reploSelectedSellingPlanPrice = reploOriginalSSPPriceR2qr2 %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploOriginalComparePricePercentR2qr2 %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign reploOriginalProductR3qr2 = product %}<!-- -->{% capture productHandle %}gel-creme-jour{% endcapture %}<!-- -->{% assign product = all_products[productHandle] %}<!-- -->{% assign reploOriginalProductVariantR3qr2 = reploSelectedVariant %}<!-- -->{% assign reploSelectedVariant = blank %}<!-- -->{% assign reploOriginalSPGR3qr2 = reploSortedSellingPlans %}<!-- -->{% assign reploSortedSellingPlans = blank %}<!-- -->{% assign reploOriginalSSPR3qr2 = reploSelectedSellingPlan %}<!-- -->{% assign reploSelectedSellingPlan = blank %}<!-- -->{% assign reploOriginalSSPPriceR3qr2 = reploSelectedSellingPlanPrice %}<!-- -->{% assign reploSelectedSellingPlanPrice = blank %}<!-- -->{% assign reploOriginalComparePricePercentR3qr2 = reploCompareAtPriceDifferencePercentage %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = blank %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<!-- -->{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% capture reploVariantIdString %}null{% endcapture %}<!-- -->{% capture reploSellingPlanIdString %}null{% endcapture %}<!-- -->{% capture reploIdKey %}id{% endcapture %}<!-- -->{% capture reploPercentageKey %}percentage{% endcapture %}<!-- -->{% capture reploPriceKey %}price{% endcapture %}<!-- -->{% capture reploFixedAmountKey %}fixed_amount{% endcapture %}<!-- -->{% capture spKey %}selling_plan{% endcapture %}<!-- -->{%- liquid\n              assign reploVariantId = reploVariantIdString | times: 1\n              assign reploSelectedVariant = product.variants | where: reploIdKey, reploVariantId | first\n              if reploSelectedVariant == blank\n                assign reploSelectedVariant = product.selected_or_first_available_variant\n              endif\n              assign reploSelectedSellingPlanPrice = reploSelectedVariant.price\n              if product.selling_plan_groups[0]\n                assign reploAllSellingPlans = reploSelectedVariant.selling_plan_allocations | map: spKey\n                assign reploSortedSellingPlans = reploAllSellingPlans | sort: reploIdKey\n                if true\n                  assign reploSellingPlanId = reploSellingPlanIdString | times: 1\n                  assign reploSelectedSellingPlan = reploSortedSellingPlans | where: reploIdKey, reploSellingPlanId | first\n                  if reploSelectedSellingPlan.price_adjustments[0]\n                    assign adjustment = reploSelectedSellingPlan.price_adjustments[0]\n                    case adjustment.value_type\n                      when reploPercentageKey\n                        assign amountOff = 100 | minus: adjustment.value\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | times: amountOff | divided_by: 100\n                      when reploFixedAmountKey\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | minus: adjustment.value\n                      when reploPriceKey\n                        assign reploSelectedSellingPlanPrice = adjustment.value\n                    endcase\n                  endif\n                endif\n              endif\n            -%}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = 0 %}<!-- -->{% if reploSelectedVariant.compare_at_price != blank %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploSelectedVariant.compare_at_price | minus: reploSelectedVariant.price | at_least: 0 | times: 100.0 | divided_by: reploSelectedVariant.compare_at_price | round %}<!-- -->{% endif %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<div data-rid=\"3e33de33-35fe-4377-9b2e-1d524583f211\" tabindex=\"0\" role=\"button\" class=\"r-3wqav1\" data-replo-product-container=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" data-replo-product-handle=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.handle}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"><product-form style=\"display:none\"><form id=\"product-form-{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" method=\"post\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" encType=\"multipart/form-data\" action=\"/cart/add\" data-type=\"add-to-cart-form\"><input type=\"hidden\" name=\"id\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{reploSelectedVariant.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/><input type=\"hidden\" name=\"quantity\" value=\"1\"/><input type=\"hidden\" name=\"selling_plan\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- if reploSelectedSellingPlan != blank -%}{{reploSelectedSellingPlan.id}}{%- endif -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/></form></product-form><div data-rid=\"fbbe34de-df28-4f44-9b7e-4ed4dc8236a5\" class=\"r-1mpddo7\"><picture data-rid=\"d3142973-6c0e-43a0-920e-29876fa7d278\" style=\"--replo-attributes-product-featured-image:{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-k1cg7v\"><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 820  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(max-width: 640px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1024  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1800  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-1q9wyug\" loading=\"lazy\"/></picture></div><div data-rid=\"957b0ef9-ea5d-4546-8313-c1a19abf2251\" class=\"r-1t9z0rt\"><div data-rid=\"22f41a95-057b-435c-a610-efd07877de2d\" class=\"r-1hv3zq0\"><div data-rid=\"1c1dd2f1-95fa-42f5-a096-a360409ed374\" class=\"r-b3etsn\"><div data-rid=\"1345cec2-2fc7-4b0d-9862-577da99e0b4a\" class=\"r-1tl33ne alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.title }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div></div><div data-rid=\"6e8bc39b-9c5f-46d9-9f94-acb4661c792a\" class=\"r-3ahe6n\"><div data-rid=\"e451734e-3106-4d93-b1a4-c915b55aabd8\" class=\"r-13zoknt\"><div data-rid=\"aef8c280-53e4-4f72-8a43-5ffa7e12b847\" class=\"r-tkc5vq\"><div data-rid=\"3f5a9e55-6e10-4cd6-bace-425ffa91b244\" class=\"r-1t3wmhi alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}ml{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div><div data-rid=\"eceb06ee-7dae-4be5-a498-bfc7ffc50ba5\" class=\"r-1eg4q9m\"><div data-rid=\"f6b9750d-6dcb-43d6-9f88-a98fa2cd27b2\" class=\"r-f0cd5i alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}made_in_france{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div></div><div data-rid=\"fb440d47-8823-40ec-a826-1d3768015813\" class=\"r-3lgm8x\"><div data-rid=\"a7652791-463d-4d29-822f-b4ec07848824\" class=\"r-1hp0s62\"><div data-rid=\"86c45cb5-197e-473e-972f-06d91d51c4b2\" class=\"r-14ja0os alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ reploSelectedSellingPlanPrice  | divided_by: 100.0 | round | times: 100.0 | money_without_trailing_zeros}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div><div data-rid=\"1b1b9ba2-c533-4afb-9a76-b8fe293a4368\" class=\"r-b1rhd6\"><div data-rid=\"0608cac0-cb36-4ec7-88ef-2c7d4beacc3d\" class=\"r-1xj1yl2\"><span style=\"display:contents\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-arrow-up-right\" style=\"fill: none;stroke: currentColor;width: var(--rsw, 100%);height: 100%\" role=\"presentation\"><line x1=\"7\" y1=\"17\" x2=\"17\" y2=\"7\"></line><polyline points=\"7 7 17 7 17 17\"></polyline></svg></span></div></div></div></div></div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign product = reploOriginalProductR3qr2 %}<!-- -->{% assign reploSelectedVariant = reploOriginalProductVariantR3qr2 %}<!-- -->{% assign reploSortedSellingPlans = reploOriginalSPGR3qr2 %}<!-- -->{% assign reploSelectedSellingPlan = reploOriginalSSPR3qr2 %}<!-- -->{% assign reploSelectedSellingPlanPrice = reploOriginalSSPPriceR3qr2 %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploOriginalComparePricePercentR3qr2 %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign reploOriginalProductR4qr2 = product %}<!-- -->{% capture productHandle %}gel-creme-nuit{% endcapture %}<!-- -->{% assign product = all_products[productHandle] %}<!-- -->{% assign reploOriginalProductVariantR4qr2 = reploSelectedVariant %}<!-- -->{% assign reploSelectedVariant = blank %}<!-- -->{% assign reploOriginalSPGR4qr2 = reploSortedSellingPlans %}<!-- -->{% assign reploSortedSellingPlans = blank %}<!-- -->{% assign reploOriginalSSPR4qr2 = reploSelectedSellingPlan %}<!-- -->{% assign reploSelectedSellingPlan = blank %}<!-- -->{% assign reploOriginalSSPPriceR4qr2 = reploSelectedSellingPlanPrice %}<!-- -->{% assign reploSelectedSellingPlanPrice = blank %}<!-- -->{% assign reploOriginalComparePricePercentR4qr2 = reploCompareAtPriceDifferencePercentage %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = blank %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<!-- -->{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% capture reploVariantIdString %}null{% endcapture %}<!-- -->{% capture reploSellingPlanIdString %}null{% endcapture %}<!-- -->{% capture reploIdKey %}id{% endcapture %}<!-- -->{% capture reploPercentageKey %}percentage{% endcapture %}<!-- -->{% capture reploPriceKey %}price{% endcapture %}<!-- -->{% capture reploFixedAmountKey %}fixed_amount{% endcapture %}<!-- -->{% capture spKey %}selling_plan{% endcapture %}<!-- -->{%- liquid\n              assign reploVariantId = reploVariantIdString | times: 1\n              assign reploSelectedVariant = product.variants | where: reploIdKey, reploVariantId | first\n              if reploSelectedVariant == blank\n                assign reploSelectedVariant = product.selected_or_first_available_variant\n              endif\n              assign reploSelectedSellingPlanPrice = reploSelectedVariant.price\n              if product.selling_plan_groups[0]\n                assign reploAllSellingPlans = reploSelectedVariant.selling_plan_allocations | map: spKey\n                assign reploSortedSellingPlans = reploAllSellingPlans | sort: reploIdKey\n                if true\n                  assign reploSellingPlanId = reploSellingPlanIdString | times: 1\n                  assign reploSelectedSellingPlan = reploSortedSellingPlans | where: reploIdKey, reploSellingPlanId | first\n                  if reploSelectedSellingPlan.price_adjustments[0]\n                    assign adjustment = reploSelectedSellingPlan.price_adjustments[0]\n                    case adjustment.value_type\n                      when reploPercentageKey\n                        assign amountOff = 100 | minus: adjustment.value\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | times: amountOff | divided_by: 100\n                      when reploFixedAmountKey\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | minus: adjustment.value\n                      when reploPriceKey\n                        assign reploSelectedSellingPlanPrice = adjustment.value\n                    endcase\n                  endif\n                endif\n              endif\n            -%}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = 0 %}<!-- -->{% if reploSelectedVariant.compare_at_price != blank %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploSelectedVariant.compare_at_price | minus: reploSelectedVariant.price | at_least: 0 | times: 100.0 | divided_by: reploSelectedVariant.compare_at_price | round %}<!-- -->{% endif %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<div data-rid=\"3e33de33-35fe-4377-9b2e-1d524583f211\" tabindex=\"0\" role=\"button\" class=\"r-3wqav1\" data-replo-product-container=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" data-replo-product-handle=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.handle}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"><product-form style=\"display:none\"><form id=\"product-form-{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" method=\"post\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" encType=\"multipart/form-data\" action=\"/cart/add\" data-type=\"add-to-cart-form\"><input type=\"hidden\" name=\"id\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{reploSelectedVariant.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/><input type=\"hidden\" name=\"quantity\" value=\"1\"/><input type=\"hidden\" name=\"selling_plan\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- if reploSelectedSellingPlan != blank -%}{{reploSelectedSellingPlan.id}}{%- endif -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/></form></product-form><div data-rid=\"fbbe34de-df28-4f44-9b7e-4ed4dc8236a5\" class=\"r-1mpddo7\"><picture data-rid=\"d3142973-6c0e-43a0-920e-29876fa7d278\" style=\"--replo-attributes-product-featured-image:{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-k1cg7v\"><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 820  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(max-width: 640px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1024  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1800  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-1q9wyug\" loading=\"lazy\"/></picture></div><div data-rid=\"957b0ef9-ea5d-4546-8313-c1a19abf2251\" class=\"r-1t9z0rt\"><div data-rid=\"22f41a95-057b-435c-a610-efd07877de2d\" class=\"r-1hv3zq0\"><div data-rid=\"1c1dd2f1-95fa-42f5-a096-a360409ed374\" class=\"r-b3etsn\"><div data-rid=\"1345cec2-2fc7-4b0d-9862-577da99e0b4a\" class=\"r-1tl33ne alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.title }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div></div><div data-rid=\"6e8bc39b-9c5f-46d9-9f94-acb4661c792a\" class=\"r-3ahe6n\"><div data-rid=\"e451734e-3106-4d93-b1a4-c915b55aabd8\" class=\"r-13zoknt\"><div data-rid=\"aef8c280-53e4-4f72-8a43-5ffa7e12b847\" class=\"r-tkc5vq\"><div data-rid=\"3f5a9e55-6e10-4cd6-bace-425ffa91b244\" class=\"r-1t3wmhi alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}ml{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div><div data-rid=\"eceb06ee-7dae-4be5-a498-bfc7ffc50ba5\" class=\"r-1eg4q9m\"><div data-rid=\"f6b9750d-6dcb-43d6-9f88-a98fa2cd27b2\" class=\"r-f0cd5i alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}made_in_france{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div></div><div data-rid=\"fb440d47-8823-40ec-a826-1d3768015813\" class=\"r-3lgm8x\"><div data-rid=\"a7652791-463d-4d29-822f-b4ec07848824\" class=\"r-1hp0s62\"><div data-rid=\"86c45cb5-197e-473e-972f-06d91d51c4b2\" class=\"r-14ja0os alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ reploSelectedSellingPlanPrice  | divided_by: 100.0 | round | times: 100.0 | money_without_trailing_zeros}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div><div data-rid=\"1b1b9ba2-c533-4afb-9a76-b8fe293a4368\" class=\"r-b1rhd6\"><div data-rid=\"0608cac0-cb36-4ec7-88ef-2c7d4beacc3d\" class=\"r-1xj1yl2\"><span style=\"display:contents\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-arrow-up-right\" style=\"fill: none;stroke: currentColor;width: var(--rsw, 100%);height: 100%\" role=\"presentation\"><line x1=\"7\" y1=\"17\" x2=\"17\" y2=\"7\"></line><polyline points=\"7 7 17 7 17 17\"></polyline></svg></span></div></div></div></div></div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign product = reploOriginalProductR4qr2 %}<!-- -->{% assign reploSelectedVariant = reploOriginalProductVariantR4qr2 %}<!-- -->{% assign reploSortedSellingPlans = reploOriginalSPGR4qr2 %}<!-- -->{% assign reploSelectedSellingPlan = reploOriginalSSPR4qr2 %}<!-- -->{% assign reploSelectedSellingPlanPrice = reploOriginalSSPPriceR4qr2 %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploOriginalComparePricePercentR4qr2 %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div></div></div></div></div></div></div></div></div></div><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Medium\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Medium\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Medium.woff?v=1749641057\") format(\"woff\");\n        }\n      </style><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Light\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Light\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Light.woff?v=1749641057\") format(\"woff\");\n        }\n      </style><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Regular\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Regular\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Regular.woff?v=1749641058\") format(\"woff\");\n        }\n      </style><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Bold\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Bold\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Bold.woff?v=1749641058\") format(\"woff\");\n        }\n      </style></div>\n{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}\n  <script type=\"application/json\" id=\"replo-deps-products\">\n    [{\"id\":\"10094474395991\",\"handle\": \"granite-demaquillant\",\"data\":{{ all_products['granite-demaquillant'] | json }}},{\"id\":\"10094475477335\",\"handle\": \"mousse-nettoyante\",\"data\":{{ all_products['mousse-nettoyante'] | json }}},{\"id\":\"10094478000471\",\"handle\": \"gel-creme-jour\",\"data\":{{ all_products['gel-creme-jour'] | json }}},{\"id\":\"10094478688599\",\"handle\": \"gel-creme-nuit\",\"data\":{{ all_products['gel-creme-nuit'] | json }}}]\n  </script>\n  {%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\n    <script type=\"application/json\" id=\"replo-deps-products-metafields\">\n      {%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture replo_double_tick -%}\"{%- endcapture -%}{\"10094474395991\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['granite-demaquillant'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['granite-demaquillant'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}},\"10094475477335\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['mousse-nettoyante'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['mousse-nettoyante'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}},\"10094478000471\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-jour'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-jour'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}},\"10094478688599\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-nuit'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-nuit'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\n    </script>\n  \n    <script type=\"application/json\" id=\"replo-deps-variant-metafields\">\n    {%- capture replo_double_tick -%}\"{%- endcapture -%}{}\n    </script>\n  {%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<script type=\"application/json\" id=\"replo-deps-shopify-store\">{ \"shop\": { \"moneyFormat\": {{ shop.money_format | json }}, \"moneyWithCurrencyFormat\": {{ shop.money_with_currency_format | json }} } }</script>{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div>\n\n{% schema %}\n{\n  \"name\": \"[collection]sensibilité\",\n  \"presets\": [\n    {\n      \"name\": \"[collection]sensibilité\"\n    }\n  ],\n  \"settings\": [\n    {\n      \"type\": \"header\",\n      \"content\": \"Created in Replo\",\n      \"info\": \"This Section was created using [Replo](https://www.replo.app/). If you would like to make any changes to the structure or design of this Section, you can [edit it in Replo](https://dashboard.replo.app/editor/07bd1984-3d87-4861-82a3-4f94a264d106/0bcad7f9-4a39-4fc3-b06f-45951fdf9431).\"\n    }\n  ]\n}\n{% endschema %}\n    "
      }
    }
  ]
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:25.488Z: Sending "Admin" GraphQL request:
  mutation themeFilesUpsert($files: [OnlineStoreThemeFilesUpsertFileInput!]!, $themeId: ID!) {
  themeFilesUpsert(files: $files, themeId: $themeId) {
    upsertedThemeFiles {
      filename
      __typename
    }
    userErrors {
      filename
      message
      __typename
    }
    __typename
  }
}

With variables:
{
  "themeId": "gid://shopify/OnlineStoreTheme/184608981335",
  "files": [
    {
      "filename": "sections/replo-home-page-full.liquid",
      "body": {
        "type": "TEXT",
        "value": "{% comment %}\n  Autogenerated by Replo at 03/26/2025, 14:42:19, please do not modify. Questions?\n  Please get in touch at support@replo.app\n{% endcomment %}\n{% include \"replo.section-settings.0bbef5f6-ce6b-4da8-89ab-d8a169129126\" %}\n<div id=\"replo-section-0bbef5f6-ce6b-4da8-89ab-d8a169129126\" data-runtime-version=\"8186ec50-0a50-11f0-8143-b32426f13452\" data-section-id=\"{{ section.id }}\" style=\"display:block !important;\">{% include \"reploChunk.0bbef5f6-ce6b-4da8-89ab-d8a169129126.0\" %}{% include \"reploChunk.0bbef5f6-ce6b-4da8-89ab-d8a169129126.1\" %}{% include \"reploChunk.0bbef5f6-ce6b-4da8-89ab-d8a169129126.2\" %}</div>\n\n{% schema %}\n{\n  \"name\": \"Home-page-full\",\n  \"presets\": [\n    {\n      \"name\": \"Home-page-full\"\n    }\n  ],\n  \"settings\": [\n    {\n      \"type\": \"header\",\n      \"content\": \"Created in Replo\",\n      \"info\": \"This Section was created using [Replo](https://www.replo.app/). If you would like to make any changes to the structure or design of this Section, you can [edit it in Replo](https://dashboard.replo.app/editor/07bd1984-3d87-4861-82a3-4f94a264d106/0bbef5f6-ce6b-4da8-89ab-d8a169129126).\"\n    }\n  ],\n  \"blocks\": [\n    {\n      \"type\": \"@app\"\n    }\n  ]\n}\n{% endschema %}\n    "
      }
    },
    {
      "filename": "sections/replo-gua-sha.liquid",
      "body": {
        "type": "TEXT",
        "value": "{% comment %}\n  Autogenerated by Replo at 07/25/2024, 12:52:15, please do not modify. Questions?\n  Please get in touch at support@replo.app\n{% endcomment %}\n{% include \"replo.section-settings.b3e927dc-9473-4fdd-a91b-3b8e339331a0\" %}\n<div id=\"replo-section-b3e927dc-9473-4fdd-a91b-3b8e339331a0\" data-runtime-version=\"b4735310-4a84-11ef-8f83-9748fb67f218\" data-section-id=\"{{ section.id }}\" style=\"display:block !important;\">{% include \"reploChunk.b3e927dc-9473-4fdd-a91b-3b8e339331a0.0\" %}{% include \"reploChunk.b3e927dc-9473-4fdd-a91b-3b8e339331a0.1\" %}{% include \"reploChunk.b3e927dc-9473-4fdd-a91b-3b8e339331a0.2\" %}</div>\n\n{% schema %}\n{\n  \"name\": \"Gua Sha\",\n  \"presets\": [\n    {\n      \"name\": \"Gua Sha\"\n    }\n  ],\n  \"settings\": [\n    {\n      \"type\": \"header\",\n      \"content\": \"Created in Replo\",\n      \"info\": \"This Section was created using [Replo](https://www.replo.app/). If you would like to make any changes to the structure or design of this Section, you can [edit it in Replo](https://dashboard.replo.app/editor/07bd1984-3d87-4861-82a3-4f94a264d106/b3e927dc-9473-4fdd-a91b-3b8e339331a0).\"\n    }\n  ]\n}\n{% endschema %}\n    "
      }
    },
    {
      "filename": "sections/replo-home-page.liquid",
      "body": {
        "type": "TEXT",
        "value": "{% comment %}\n  Autogenerated by Replo at 08/24/2024, 10:10:19, please do not modify. Questions?\n  Please get in touch at support@replo.app\n{% endcomment %}\n{% include \"replo.section-settings.0bbef5f6-ce6b-4da8-89ab-d8a169129126\" %}\n<div id=\"replo-section-0bbef5f6-ce6b-4da8-89ab-d8a169129126\" data-runtime-version=\"0d70a470-6201-11ef-baf4-5d555e263821\" data-section-id=\"{{ section.id }}\" style=\"display:block !important;\">{% include \"reploChunk.0bbef5f6-ce6b-4da8-89ab-d8a169129126.0\" %}{% include \"reploChunk.0bbef5f6-ce6b-4da8-89ab-d8a169129126.1\" %}{% include \"reploChunk.0bbef5f6-ce6b-4da8-89ab-d8a169129126.2\" %}</div>\n\n{% schema %}\n{\n  \"name\": \"Home-page\",\n  \"presets\": [\n    {\n      \"name\": \"Home-page\"\n    }\n  ],\n  \"settings\": [\n    {\n      \"type\": \"header\",\n      \"content\": \"Created in Replo\",\n      \"info\": \"This Section was created using [Replo](https://www.replo.app/). If you would like to make any changes to the structure or design of this Section, you can [edit it in Replo](https://dashboard.replo.app/editor/07bd1984-3d87-4861-82a3-4f94a264d106/0bbef5f6-ce6b-4da8-89ab-d8a169129126).\"\n    }\n  ],\n  \"blocks\": [\n    {\n      \"type\": \"@app\"\n    }\n  ]\n}\n{% endschema %}\n    "
      }
    }
  ]
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
╭─ success ────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                          │
│  Preview your theme (t)                                                                                  │
│    • http://127.0.0.1:9292                                                                               │
│                                                                                                          │
│  Next steps                                                                                              │
│    • Share your theme preview (p) https://aloe-paris.myshopify.com/?preview_theme_id=184608981335        │
│    • Customize your theme at the theme editor (e)                                                        │
│    • Preview your gift cards (g)                                                                         │
│                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-07-18T13:14:25.502Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-18T13:14:25.502Z: Ensuring that the user is authenticated with the Admin API with the following scopes for the store aloe-paris.myshopify.com:
[]

2025-07-18T13:14:25.502Z: Getting session store...
2025-07-18T13:14:25.503Z: Validating existing session against the scopes:
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
  "adminApi": {
    "scopes": [],
    "storeFqdn": "aloe-paris.myshopify.com"
  }
}

2025-07-18T13:14:25.503Z: - Token validation -> It's expired: false
2025-07-18T13:14:26.201Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "ARTICLE"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.201Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "BLOG"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.201Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COLLECTION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.201Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COMPANY"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.202Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COMPANY_LOCATION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.202Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "LOCATION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.202Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "MARKET"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.202Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "ORDER"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.202Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PAGE"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.203Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PRODUCT"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.203Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PRODUCTVARIANT"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.203Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "SHOP"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-18T13:14:26.811Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 17529 ms
With response headers:

    
╭─ error ──────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                          │
│  Failed to perform the initial theme synchronization.                                                    │
│                                                                                                          │
│  request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json failed, reason:              │
│                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯

2025-07-18T13:14:26.817Z: Failed to perform the initial theme synchronization.
FetchError: request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json failed, reason: 
    at ClientRequest.<anonymous> (file:///home/maxdesign/.nvm/versions/node/v22.17.0/lib/node_modules/@shopify/cli/dist/chunk-2OFXKVRT.js:17594:18)
    at ClientRequest.emit (node:events:518:28)
    at ClientRequest.emit (node:domain:489:12)
    at emitErrorEvent (node:_http_client:104:11)
    at TLSSocket.socketErrorListener (node:_http_client:518:5)
    at TLSSocket.emit (node:events:518:28)
    at TLSSocket.emit (node:domain:489:12)
    at emitErrorNT (node:internal/streams/destroy:170:8)
    at emitErrorCloseNT (node:internal/streams/destroy:129:3)
    at processTicksAndRejections (node:internal/process/task_queues:90:21)
```
</details>

comment #14 by karreiro, 2025-07-21, 08:41:32
Thank you for sharing the new `--verbose` outputs and details, @MaxDesignFR.

I noticed in your logs that you're not running [this build](https://github.com/Shopify/cli/issues/6062#issuecomment-3089008358).

Could you please try that one?

The `@shopify/cli@0.0.0-snapshot-20250718094441` build has changes in the network policy that aim to fix the problem you’re facing. We’ve also included extra logs to help us better understand your local theme and environment, in case those policies do not impact your setup.

Thank you for reporting this 🙇

comment #15 by gabrieljadeau, 2025-07-22, 08:56:02
Hello @karreiro, 

Sadly this is still not working ... please see the log bellow.

<details>
    <summary>Verbose output</summary>
    ```
➜  shopify-loulousaison git:(main) shopify theme dev --store=louloudesaison  --verbose
2025-07-22T08:54:43.412Z: Running command theme dev
2025-07-22T08:54:43.414Z: Running system process in background:
  · Command: /Users/gabrieljadeau/.nvm/versions/node/v22.14.0/bin/node /Users/gabrieljadeau/.nvm/versions/node/v22.14.0/bin/shopify notifications list --ignore-errors
  · Working directory: /Users/gabrieljadeau/Sites/shopify-loulousaison

2025-07-22T08:54:43.420Z: Notifications to show: 0
2025-07-22T08:54:43.428Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-22T08:54:43.428Z: Ensuring that the user is authenticated with the Admin API with the following scopes for the store louloudesaison.myshopify.com:
[]

2025-07-22T08:54:43.428Z: Getting session store...
2025-07-22T08:54:43.429Z: Validating existing session against the scopes:
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
  "adminApi": {
    "scopes": [],
    "storeFqdn": "louloudesaison.myshopify.com"
  }
}

2025-07-22T08:54:43.429Z: - Token validation -> It's expired: false
2025-07-22T08:54:43.430Z: Getting development theme...
2025-07-22T08:54:43.431Z: Sending "Admin" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://louloudesaison.myshopify.com/admin/api/unstable/graphql.json
2025-07-22T08:54:58.500Z: Request to https://louloudesaison.myshopify.com/admin/api/unstable/graphql.json completed in 15068 ms
With response headers:

    
2025-07-22T08:54:58.502Z: Error fetching theme with ID: 184354144604
2025-07-22T08:54:58.502Z: Removing development theme...
2025-07-22T08:54:58.512Z: Sending "Admin" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: darwin
 - Content-Type: application/json

to https://louloudesaison.myshopify.com/admin/api/unstable/graphql.json
2025-07-22T08:55:13.569Z: Request to https://louloudesaison.myshopify.com/admin/api/unstable/graphql.json completed in 15056 ms
With response headers:

    
╭─ error ──────────────────────────────────────────────────────────────────────╮
│                                                                              │
│  Unknown error connecting to your store louloudesaison.myshopify.com:        │
│  request to                                                                  │
│  https://louloudesaison.myshopify.com/admin/api/unstable/graphql.json        │
│  failed, reason: Client network socket disconnected before secure TLS        │
│  connection was established                                                  │
│                                                                              │
│  To investigate the issue, examine this stack trace:                         │
│    at fetchApiVersions (Users/gabrieljadeau/.nvm/versions/node/v22.14.0/lib  │
│    /node_modules/@shopify/cli/dist/index.js:194224)                          │
│    at processTicksAndRejections (node:internal/process/task_queues:105)      │
│    at async supportedApiVersions (Users/gabrieljadeau/.nvm/versions/node/v2  │
│    2.14.0/lib/node_modules/@shopify/cli/dist/index.js:194208)                │
│    at async fetchLatestSupportedApiVersion (Users/gabrieljadeau/.nvm/versio  │
│    ns/node/v22.14.0/lib/node_modules/@shopify/cli/dist/index.js:194204)      │
│    at async adminRequestDoc (Users/gabrieljadeau/.nvm/versions/node/v22.14.  │
│    0/lib/node_modules/@shopify/cli/dist/index.js:194184)                     │
│    at async themeCreate (Users/gabrieljadeau/.nvm/versions/node/v22.14.0/li  │
│    b/node_modules/@shopify/cli/dist/index.js:194285)                         │
│    at create (Users/gabrieljadeau/.nvm/versions/node/v22.14.0/lib/node_modu  │
│    les/@shopify/cli/dist/index.js:194715)                                    │
│    at findOrCreate (Users/gabrieljadeau/.nvm/versions/node/v22.14.0/lib/nod  │
│    e_modules/@shopify/cli/dist/index.js:194703)                              │
│    at run (Users/gabrieljadeau/.nvm/versions/node/v22.14.0/lib/node_modules  │
│    /@shopify/cli/dist/index.js:199069)                                       │
│    at _run (Users/gabrieljadeau/.nvm/versions/node/v22.14.0/lib/node_module  │
│    s/@shopify/cli/dist/chunk-3FBDJEGD.js:169541)                             │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

2025-07-22T08:55:13.613Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/gabrieljadeau/Sites/shopify-loulousaison

2025-07-22T08:55:13.732Z: Obtaining the dependency manager in directory ../.....
2025-07-22T08:55:14.058Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 200 ms
With response headers:
 - x-request-id: cdf6c6f4-53d2-4cc3-b22c-965f56eedc8d
    
2025-07-22T08:55:14.058Z: Analytics event sent: {
  "command": "theme dev",
  "time_start": 1753174483412,
  "time_end": 1753174513606,
  "total_time": 30194,
  "success": false,
  "cli_version": "3.82.0",
  "ruby_version": "",
  "node_version": "22.14.0",
  "is_employee": false,
  "uname": "darwin arm64",
  "env_ci": false,
  "env_plugin_installed_any_custom": false,
  "env_plugin_installed_shopify": "[\"@shopify/app\",\"@shopify/cli\",\"@shopify/plugin-cloudflare\"]",
  "env_shell": "zsh",
  "env_device_id": "b3a1d4d3bd46c5b2eeeaf7e1b777bfeba91bf275",
  "env_cloud": "localhost",
  "env_package_manager": "npm",
  "env_is_global": false,
  "env_auth_method": "device_auth",
  "env_is_wsl": false,
  "env_build_repository": "Shopify/cli",
  "cmd_app_warning_api_key_deprecation_displayed": false,
  "cmd_all_timing_network_ms": 30125,
  "cmd_all_timing_prompts_ms": 0,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "theme",
  "cmd_all_plugin": "@shopify/theme",
  "cmd_all_force": false,
  "cmd_all_verbose": true,
  "cmd_all_path_override": true,
  "cmd_all_path_override_hash": "f1db15b00f9f1526873ade26c266b1a1409ed4b1",
  "cmd_all_timing_active_ms": 68,
  "cmd_all_exit": "unexpected_error",
  "user_id": "ae9f7283-c904-45d8-9638-747273e416c9",
  "request_ids": [],
  "args": "--store=louloudesaison --verbose",
  "error_message": "Unknown error connecting to your store louloudesaison.myshopify.com: request to https://louloudesaison.myshopify.com/admin/api/unstable/graphql.json failed, reason: Client network socket disconnected before secure TLS connection was established",
  "env_plugin_installed_all": "[\"@shopify/app\",\"@shopify/cli\",\"@shopify/plugin-cloudflare\"]",
  "metadata": "{\"extraPublic\":{\"@shopify/app\":{\"cmd_app_warning_api_key_deprecation_displayed\":false}},\"extraSensitive\":{\"@shopify/app\":{}}}"
}
2025-07-22T08:55:14.066Z: Reporting unhandled error to Bugsnag: Unknown error connecting to your store louloudesaison.myshopify.com: request to https://louloudesaison.myshopify.com/admin/api/unstable/graphql.json failed, reason: Client network socket disconnected before secure TLS connection was established
2025-07-22T08:55:14.504Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/gabrieljadeau/Sites/shopify-loulousaison

2025-07-22T08:55:14.615Z: Obtaining the dependency manager in directory ../.....

    ```
</details>

comment #16 by MaxDesignFR, 2025-07-22, 11:08:00
@karreiro I installed this build `@shopify/cli@0.0.0-snapshot-20250718094441` but it shows as `3.82.0` when I lookup for `shopify version`. I was on `3.79.2` so it did update.

I still have the problem, it seems to me somehow related to this project. They use [Replo ](https://www.replo.app/) in many parts of the website, so lots of assets and templates, and when I reach the reconciliation strategy (keep local version), the verbose goes crazy, have not seen that before. So it may have to do with the size of the project. I recorded a video snapshot from A to Z so that you can see what's going on: https://files.maxdesign.expert/2025/07/Code_FP2Zqa1hWa

Some more verbose I could catch:

<details>
<summary>Verbose output</summary>

```
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-customers-activate-account.liquid (size: 2045 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-customers-addresses.liquid (size: 3239 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-customers-login.liquid (size: 6804 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-customers-order.liquid (size: 7805 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-customers-register.liquid (size: 5997 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-customers-reset-password.liquid (size: 1782 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-gift-card.liquid (size: 5718 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-list-collections.liquid (size: 4639 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-not-found.liquid (size: 433 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-page.liquid (size: 1074 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-password.liquid (size: 10482 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-product.liquid (size: 35811 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/main-search.liquid (size: 9926 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/maxdesign.json (size: 13691 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/media-grid.liquid (size: 20626 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/media-with-text.liquid (size: 33008 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/modal-maxdesign.liquid (size: 36096 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/multi-column.liquid (size: 9854 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/multiple-images-with-text.liquid (size: 10634 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/newsletter-popup.liquid (size: 4684 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/newsletter.liquid (size: 5389 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/overlay-group.json (size: 2007 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/pickup-availability.liquid (size: 230 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/press.liquid (size: 8408 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/privacy-banner.liquid (size: 1849 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/recently-viewed-products.liquid (size: 7550 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/related-products.liquid (size: 9733 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-box-de-noel.liquid (size: 1078 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-brume.liquid (size: 1389 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-bundle-v5.liquid (size: 1124 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collection-accessoires.liquid (size: 214318 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collection-best-seller.liquid (size: 202310 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collection-contour.liquid (size: 191405 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collection-deshydratati.liquid (size: 215500 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collection-nouveautes.liquid (size: 250917 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collectioncernespoches.liquid (size: 191200 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collectiondemaquillants.liquid (size: 190364 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collectionhydratant.liquid (size: 231423 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collectionimperfections.liquid (size: 191121 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collectionroutine-compl.liquid (size: 251909 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collectionroutine-minim.liquid (size: 215520 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collectionsensibilite.liquid (size: 215413 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collectionserum.liquid (size: 231326 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-collectionteint-terne.liquid (size: 191243 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-gua-sha-full-page.liquid (size: 1157 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-gua-sha.liquid (size: 1133 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-home-page-full.liquid (size: 1199 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-home-page.liquid (size: 1189 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-page-detail-abonnement.liquid (size: 1102 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-page-notre-vision.liquid (size: 178906 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-product-page-full.liquid (size: 1153 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-rejoignez-abonnes.liquid (size: 189637 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-section-001.liquid (size: 1340 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-section-002.liquid (size: 1340 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-section-003.liquid (size: 1340 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-section-004.liquid (size: 1340 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-section-005.liquid (size: 1340 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-section-006.liquid (size: 1340 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-section-007.liquid (size: 1340 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-section-abonnement-v2.liquid (size: 1100 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-section-accueil-v2.liquid (size: 1289 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/replo-section-hydralise-v2.liquid (size: 1280 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/revealed-image-on-scroll.liquid (size: 3887 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/rich-text.liquid (size: 21736 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/scrolling-text.liquid (size: 4477 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/search-drawer.liquid (size: 11881 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/shop-the-look.liquid (size: 9331 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/slideshow.liquid (size: 27221 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/source-tracking.liquid (size: 460 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/specification-table.liquid (size: 10052 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/tabs.liquid (size: 6627 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/testimonials.liquid (size: 9137 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/text-with-icons.liquid (size: 18041 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/timeline.liquid (size: 6346 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/variant-added.liquid (size: 2586 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/sections/video.liquid (size: 12880 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/accordion.liquid (size: 1951 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/active-facets.liquid (size: 3072 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/address-form.liquid (size: 5947 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/article-banner.liquid (size: 2461 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/article-comments.liquid (size: 3856 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/article-navigation.liquid (size: 1230 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/banner.liquid (size: 1661 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/blog-post-card.liquid (size: 4877 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/button.liquid (size: 4069 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/buy-buttons.liquid (size: 4963 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/checkbox.liquid (size: 2029 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/collection-top-bar.liquid (size: 8829 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/css-variables.liquid (size: 22023 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/direction.liquid (size: 347 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/facets-vertical.liquid (size: 7595 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/free-shipping-bar.liquid (size: 1848 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/horizontal-product.liquid (size: 3686 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/icon.liquid (size: 96041 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/input.liquid (size: 3726 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/inventory.liquid (size: 3433 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/js-variables.liquid (size: 4763 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/line-item.liquid (size: 4662 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/live-visitors.liquid (size: 1375 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/localization-selector.liquid (size: 5434 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/media.liquid (size: 3324 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/mega-menu-horizontal.liquid (size: 5970 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/mega-menu-mobile-banner.liquid (size: 1071 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/microdata-schema.liquid (size: 4252 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/navigation-panel.liquid (size: 14942 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/navigation-promo-block.liquid (size: 13143 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/offer.liquid (size: 2794 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/omega_custom_code.liquid (size: 784 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/option-value.liquid (size: 7858 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/pagination.liquid (size: 2206 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/pickup-availability.liquid (size: 4707 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/predictive-search-result-item.liquid (size: 3328 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/price-list.liquid (size: 9289 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/price-range.liquid (size: 3178 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/product-badges.liquid (size: 3703 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/product-card-placeholder.liquid (size: 4145 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/product-card.liquid (size: 13868 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/product-gallery.liquid (size: 10387 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/product-info.liquid (size: 20387 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/product-rating.liquid (size: 2308 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo-head.liquid (size: 902 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.01712e65-bc10-4d64-9c90-925ae02b9c05.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.02cadca1-0db1-45a4-b7f9-5658d574dffa.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.04487cac-6674-4a43-a1c8-99333d5f358e.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.0468bf1e-32c5-4cc8-8ade-aeb7dbfe9846.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.091e3207-894b-4d1c-9786-354926a7e19f.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.0bbef5f6-ce6b-4da8-89ab-d8a169129126.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.0bcad7f9-4a39-4fc3-b06f-45951fdf9431.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.0e305fb3-17a1-4655-a0a5-42c5f34ee925.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.0eb96234-9035-46e2-9577-6dde534c7491.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.14c26584-65b6-475b-8c33-755bc834ca30.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.161fd10e-1e0e-4234-9829-e61cc00c9a13.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.16fe5c6f-7d78-4d89-8b3f-f88b8f50e39c.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.17292e6a-ebab-4aa1-8008-f7c90197b09c.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.244160e3-678a-4ea3-9057-3555e3e53984.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.290ae22c-aed0-4225-9028-66727faef951.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.2e1b719d-cb29-4c1a-a3f8-23ea2fa006ef.liquid (size: 17480 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.31299c28-fffa-45d8-b8da-f350bf0e9351.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.3180adf2-4979-4b40-9fdc-6ecf92cfda14.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.346f3b57-5609-43a2-9be8-eeb4535abc44.liquid (size: 7617 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.4380f2e0-8e80-4b78-9a91-200d5f78b97f.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.4415cd3f-654c-47b3-9cc9-3a7fd4a6633b.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.49f797d7-0af0-453d-89c6-16eacb27be4b.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.4fe80c8a-476d-4057-a64f-944eb790ab4e.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.58bb53cb-ed79-4ebd-8730-a8b93b0855df.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.5d51e195-915e-4585-90af-128902b5730a.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.5ec3bcab-7f59-4559-8883-9883c9538797.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.5ef5727d-ef7f-437f-94cc-ffd2f88961af.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.6240bc69-54e3-4d2a-bc67-57a63a686336.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.6271a843-f5c5-4791-8ad0-0006b4c298a0.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.631a51de-62a2-4ab1-a143-29cda0b1f694.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.75efd4a7-37fa-485d-bd70-d532c7695b79.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.788f0af5-6f31-4fb6-8c75-fe564d5c64b3.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.792a22a0-d29a-4626-ae55-51ac514057e3.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.7fb19b08-214b-45d6-a059-a1350d60cb77.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.8b4a360e-c998-48a5-945b-a25a58e8784c.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.8b8666ac-3ec2-4a1b-9e55-fa0f3796bd5a.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.8cfd9255-50bc-48df-876f-e352fa99cd9f.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.9004bd6e-c665-417b-a995-a0d918d3f201.liquid (size: 1437 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.91f057eb-81a7-41c6-8400-b16a5d3312db.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.968e3f17-75dc-4b88-af68-22248b3e7c19.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.a3a6df35-52d6-4564-b41a-8f780dfa9643.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.ae926d2a-1476-4413-8644-e06810b8bf30.liquid (size: 839 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.b3e927dc-9473-4fdd-a91b-3b8e339331a0.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.b90902c0-e2ae-4b03-a8d6-8e6d7665cf81.liquid (size: 4665 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.c06ddc28-8fc8-4980-a098-70b7984786bf.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.c1a2e38c-73a7-4581-9e82-e1dfa4c2e422.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.c326d4ee-35fa-433e-a417-5fac26dda8f4.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.c38b1d65-0d66-4abc-9f76-100de1fcaf8a.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.c7377517-497e-41ff-85a8-13c2600babf2.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.c8a1ab65-4b63-43ac-b1b8-3c9dc0161fcc.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.cd7465ea-efcd-47a9-9937-ba7e10c350ef.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.d32e0a56-91c2-428c-bf08-a41fb837f9ae.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.d3823940-3988-4206-ae35-e3d368a98fa0.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.d3ca38b8-3d94-45d2-89fe-33666df7af3b.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.d506429c-e03a-4e99-b4cc-97491f43f719.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.d61588b5-8f0e-4c20-bd79-ff03b01afc37.liquid (size: 841 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.d878c8e0-65c2-4df9-ba78-b5093050352d.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.db41dd03-a7f4-44b9-a1e8-6380a2f2586e.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.e19d72ce-6c07-4057-91f3-928ad106aa82.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.e31fccdc-20c9-426b-af0b-034c2e86b134.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.e4cf55c4-47e0-4081-8bc6-195df4966962.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.e96b7b3b-963e-4b22-a962-db81c2de69ac.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.eb957753-1d92-466e-ab11-d44078c5740a.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.ec55daa6-f112-4212-ba8a-df69b3acbdfc.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/replo.section-settings.f1ce0e85-ab6e-4482-a244-e059db125003.liquid (size: 219 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.0468bf1e-32c5-4cc8-8ade-aeb7dbfe9846.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.0468bf1e-32c5-4cc8-8ade-aeb7dbfe9846.1.liquid (size: 102333 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.060a43f3-16b2-464c-ada3-7e3999e7a8ca.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.060a43f3-16b2-464c-ada3-7e3999e7a8ca.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.060a43f3-16b2-464c-ada3-7e3999e7a8ca.2.liquid (size: 256281 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.060a43f3-16b2-464c-ada3-7e3999e7a8ca.3.liquid (size: 26501 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.0bbef5f6-ce6b-4da8-89ab-d8a169129126.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.0bbef5f6-ce6b-4da8-89ab-d8a169129126.1.liquid (size: 256147 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.0bbef5f6-ce6b-4da8-89ab-d8a169129126.2.liquid (size: 35887 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.0e305fb3-17a1-4655-a0a5-42c5f34ee925.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.0e305fb3-17a1-4655-a0a5-42c5f34ee925.1.liquid (size: 25966 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.0eb96234-9035-46e2-9577-6dde534c7491.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.0eb96234-9035-46e2-9577-6dde534c7491.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.0eb96234-9035-46e2-9577-6dde534c7491.2.liquid (size: 256113 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.0eb96234-9035-46e2-9577-6dde534c7491.3.liquid (size: 76019 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.14c26584-65b6-475b-8c33-755bc834ca30.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.14c26584-65b6-475b-8c33-755bc834ca30.1.liquid (size: 204198 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.290ae22c-aed0-4225-9028-66727faef951.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.290ae22c-aed0-4225-9028-66727faef951.1.liquid (size: 248498 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.3180adf2-4979-4b40-9fdc-6ecf92cfda14.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.3180adf2-4979-4b40-9fdc-6ecf92cfda14.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.3180adf2-4979-4b40-9fdc-6ecf92cfda14.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.3180adf2-4979-4b40-9fdc-6ecf92cfda14.3.liquid (size: 187124 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.32e885b4-7241-49a0-a967-44507d611922.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.32e885b4-7241-49a0-a967-44507d611922.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.32e885b4-7241-49a0-a967-44507d611922.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.32e885b4-7241-49a0-a967-44507d611922.3.liquid (size: 255837 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.32e885b4-7241-49a0-a967-44507d611922.4.liquid (size: 182752 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.3b06b51f-bb9e-4c19-926e-4092cd9a945c.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.3b06b51f-bb9e-4c19-926e-4092cd9a945c.1.liquid (size: 78806 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4380f2e0-8e80-4b78-9a91-200d5f78b97f.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4380f2e0-8e80-4b78-9a91-200d5f78b97f.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4380f2e0-8e80-4b78-9a91-200d5f78b97f.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4380f2e0-8e80-4b78-9a91-200d5f78b97f.3.liquid (size: 256045 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4380f2e0-8e80-4b78-9a91-200d5f78b97f.4.liquid (size: 256336 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4380f2e0-8e80-4b78-9a91-200d5f78b97f.5.liquid (size: 15703 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4785765d-2ec6-46cc-a50f-6c1fccabefd2.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4785765d-2ec6-46cc-a50f-6c1fccabefd2.1.liquid (size: 243431 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.49b05d93-ef36-4211-8229-47ae5d6bca43.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.49b05d93-ef36-4211-8229-47ae5d6bca43.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.49b05d93-ef36-4211-8229-47ae5d6bca43.2.liquid (size: 256005 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.49b05d93-ef36-4211-8229-47ae5d6bca43.3.liquid (size: 209876 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.49f797d7-0af0-453d-89c6-16eacb27be4b.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.49f797d7-0af0-453d-89c6-16eacb27be4b.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.49f797d7-0af0-453d-89c6-16eacb27be4b.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.49f797d7-0af0-453d-89c6-16eacb27be4b.3.liquid (size: 256053 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.49f797d7-0af0-453d-89c6-16eacb27be4b.4.liquid (size: 256315 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.49f797d7-0af0-453d-89c6-16eacb27be4b.5.liquid (size: 14481 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4eabc0b1-7304-4a42-8a9b-d8568c705d20.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4eabc0b1-7304-4a42-8a9b-d8568c705d20.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4eabc0b1-7304-4a42-8a9b-d8568c705d20.2.liquid (size: 254646 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.4eabc0b1-7304-4a42-8a9b-d8568c705d20.3.liquid (size: 212394 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.58bb53cb-ed79-4ebd-8730-a8b93b0855df.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.58bb53cb-ed79-4ebd-8730-a8b93b0855df.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.58bb53cb-ed79-4ebd-8730-a8b93b0855df.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.58bb53cb-ed79-4ebd-8730-a8b93b0855df.3.liquid (size: 256004 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.58bb53cb-ed79-4ebd-8730-a8b93b0855df.4.liquid (size: 256352 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.58bb53cb-ed79-4ebd-8730-a8b93b0855df.5.liquid (size: 27410 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.5d51e195-915e-4585-90af-128902b5730a.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.5d51e195-915e-4585-90af-128902b5730a.1.liquid (size: 256075 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.5d51e195-915e-4585-90af-128902b5730a.2.liquid (size: 615 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.5ec3bcab-7f59-4559-8883-9883c9538797.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.5ec3bcab-7f59-4559-8883-9883c9538797.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.5ec3bcab-7f59-4559-8883-9883c9538797.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.5ec3bcab-7f59-4559-8883-9883c9538797.3.liquid (size: 255285 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.5ec3bcab-7f59-4559-8883-9883c9538797.4.liquid (size: 182761 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.3.liquid (size: 256053 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.4.liquid (size: 256336 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.896cd9cf-3fa7-4a0c-8a3f-5d9434aebc24.5.liquid (size: 10010 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.9068947d-baae-4de2-9c07-ac612987d696.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.9068947d-baae-4de2-9c07-ac612987d696.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.9068947d-baae-4de2-9c07-ac612987d696.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.9068947d-baae-4de2-9c07-ac612987d696.3.liquid (size: 244647 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.91f057eb-81a7-41c6-8400-b16a5d3312db.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.91f057eb-81a7-41c6-8400-b16a5d3312db.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.91f057eb-81a7-41c6-8400-b16a5d3312db.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.91f057eb-81a7-41c6-8400-b16a5d3312db.3.liquid (size: 256043 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.91f057eb-81a7-41c6-8400-b16a5d3312db.4.liquid (size: 256327 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.91f057eb-81a7-41c6-8400-b16a5d3312db.5.liquid (size: 17027 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.92faf019-cb9f-4e75-8426-1f2ea882d482.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.92faf019-cb9f-4e75-8426-1f2ea882d482.1.liquid (size: 253394 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.9c34a797-ff6e-405f-95fc-c31ef9eee0cf.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.9c34a797-ff6e-405f-95fc-c31ef9eee0cf.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.9c34a797-ff6e-405f-95fc-c31ef9eee0cf.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.9c34a797-ff6e-405f-95fc-c31ef9eee0cf.3.liquid (size: 222030 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.9c65c337-a31b-4bf5-873a-8423608ff900.0.liquid (size: 173245 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.9c65c337-a31b-4bf5-873a-8423608ff900.1.liquid (size: 173279 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.a3a6df35-52d6-4564-b41a-8f780dfa9643.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.a3a6df35-52d6-4564-b41a-8f780dfa9643.1.liquid (size: 86694 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.aacb5a11-aa62-459e-ab73-43a996b6844c.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.aacb5a11-aa62-459e-ab73-43a996b6844c.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.aacb5a11-aa62-459e-ab73-43a996b6844c.2.liquid (size: 256004 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.aacb5a11-aa62-459e-ab73-43a996b6844c.3.liquid (size: 213136 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.3.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.4.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.5.liquid (size: 256571 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b06086a5-34f6-4c4d-babd-edd23e97975a.6.liquid (size: 126727 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.3.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.4.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.5.liquid (size: 256576 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b0b6630b-5d57-4fde-af92-423699a42aba.6.liquid (size: 126164 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b3e927dc-9473-4fdd-a91b-3b8e339331a0.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b3e927dc-9473-4fdd-a91b-3b8e339331a0.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.b3e927dc-9473-4fdd-a91b-3b8e339331a0.2.liquid (size: 228325 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.3.liquid (size: 256004 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.4.liquid (size: 256363 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.c7377517-497e-41ff-85a8-13c2600babf2.5.liquid (size: 27711 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.cc823b0c-07e5-4fb7-8e46-2833c8ca81cb.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.cc823b0c-07e5-4fb7-8e46-2833c8ca81cb.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.cc823b0c-07e5-4fb7-8e46-2833c8ca81cb.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.cc823b0c-07e5-4fb7-8e46-2833c8ca81cb.3.liquid (size: 222978 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.3.liquid (size: 256004 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.4.liquid (size: 256348 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d1afcc45-0b95-47ac-8a09-f7f5cbf28046.5.liquid (size: 26558 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.3.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.4.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.5.liquid (size: 256883 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d45cc921-9524-451f-a691-424125b3017a.6.liquid (size: 47601 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d878c8e0-65c2-4df9-ba78-b5093050352d.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.d878c8e0-65c2-4df9-ba78-b5093050352d.1.liquid (size: 174409 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.de3d2b17-4441-466d-8ea8-735cb139f93d.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.de3d2b17-4441-466d-8ea8-735cb139f93d.1.liquid (size: 203355 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.e19d72ce-6c07-4057-91f3-928ad106aa82.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.e19d72ce-6c07-4057-91f3-928ad106aa82.1.liquid (size: 204851 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.e31fccdc-20c9-426b-af0b-034c2e86b134.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.e31fccdc-20c9-426b-af0b-034c2e86b134.1.liquid (size: 247738 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.e813f58e-a823-4650-abeb-167cfd964417.0.liquid (size: 256023 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.e813f58e-a823-4650-abeb-167cfd964417.1.liquid (size: 11965 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.e96b7b3b-963e-4b22-a962-db81c2de69ac.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.e96b7b3b-963e-4b22-a962-db81c2de69ac.1.liquid (size: 242820 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.eb957753-1d92-466e-ab11-d44078c5740a.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.eb957753-1d92-466e-ab11-d44078c5740a.1.liquid (size: 100311 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.3.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.4.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.5.liquid (size: 256576 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.ec91902e-02a8-4459-961d-96cb3b4e0b88.6.liquid (size: 130787 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.3.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.4.liquid (size: 255989 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.5.liquid (size: 257054 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f1ce0e85-ab6e-4482-a244-e059db125003.6.liquid (size: 9436 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f29ab7b3-2a18-4771-b61a-a7d4228f5d1b.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f29ab7b3-2a18-4771-b61a-a7d4228f5d1b.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f29ab7b3-2a18-4771-b61a-a7d4228f5d1b.2.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f29ab7b3-2a18-4771-b61a-a7d4228f5d1b.3.liquid (size: 256262 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f29ab7b3-2a18-4771-b61a-a7d4228f5d1b.4.liquid (size: 29048 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f795dec7-1517-4072-8183-47a6f47e0f51.0.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f795dec7-1517-4072-8183-47a6f47e0f51.1.liquid (size: 256000 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f795dec7-1517-4072-8183-47a6f47e0f51.2.liquid (size: 256029 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/reploChunk.f795dec7-1517-4072-8183-47a6f47e0f51.3.liquid (size: 205312 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/scrollbar.liquid (size: 1531 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/section-header.liquid (size: 2137 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/section-properties.liquid (size: 3894 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/section-spacing-collapsing.liquid (size: 2714 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/select.liquid (size: 1728 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/shadow-dom-templates.liquid (size: 1746 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/share-link.liquid (size: 1368 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/shipping-estimator.liquid (size: 1658 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/social-media.liquid (size: 7440 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/social-meta-tags.liquid (size: 3458 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/source-tracking-script.liquid (size: 1210 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/styled-text.liquid (size: 1844 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/surface.liquid (size: 2029 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/ultimate-datalayer.liquid (size: 43582 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/variant-picker.liquid (size: 8924 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/snippets/vendor.liquid (size: 1073 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/404.json (size: 489 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/article.gua-sha-template.json (size: 5222 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/article.json (size: 5232 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/article.patch-template.json (size: 5222 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/blog.json (size: 1620 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/cart.json (size: 1080 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.accessoires.json (size: 1803 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.cernes-poches.json (size: 1803 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.contour-des-yeux.json (size: 1786 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.demaquillants-nettoyant.json (size: 1807 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.deshydratation.json (size: 1807 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.exfoliants-masques.json (size: 1807 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.hydratants-jour-nuit.json (size: 1790 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.imperfections.json (size: 1806 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.json (size: 583 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.meilleures-ventes.json (size: 1802 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.nouveautes.json (size: 1799 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.routine-complete.json (size: 1806 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.routine-minimaliste.json (size: 1806 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.sensibilites.json (size: 1799 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.serums-soins-cibles.json (size: 1775 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/collection.teint-terne.json (size: 1798 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/gift_card.liquid (size: 30 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/index.json (size: 1252 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/list-collections.json (size: 496 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.contact.json (size: 1653 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.faq.json (size: 484 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.formulaire-klaviyo.json (size: 547 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.json (size: 14515 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.judgeme_reviews.json (size: 5853 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.landing-page-auto.json (size: 4849 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.list-collections.json (size: 496 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.notre-vision.json (size: 755 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.pre-inscription-bf.json (size: 9184 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo-details-abonnemen.json (size: 775 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.060a43f3-16b2-464c-ada3-7e3999e7a8ca.liquid (size: 444 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.32e885b4-7241-49a0-a967-44507d611922.liquid (size: 509 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.3b06b51f-bb9e-4c19-926e-4092cd9a945c.liquid (size: 314 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.4785765d-2ec6-46cc-a50f-6c1fccabefd2.liquid (size: 314 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.49b05d93-ef36-4211-8229-47ae5d6bca43.liquid (size: 444 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.4eabc0b1-7304-4a42-8a9b-d8568c705d20.liquid (size: 444 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.60541709-52f5-445c-861d-fe76a406b264.liquid (size: 131546 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.634ff841-0f6c-429d-9b0a-6ca269a441e8.liquid (size: 132119 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.82f1f6c0-d775-4dc7-808d-b358219e3aba.liquid (size: 164336 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.85a4b83b-8dcc-4a2c-8a6b-b34e1cd989d1.liquid (size: 177387 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.9068947d-baae-4de2-9c07-ac612987d696.liquid (size: 444 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.92faf019-cb9f-4e75-8426-1f2ea882d482.liquid (size: 314 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.9c34a797-ff6e-405f-95fc-c31ef9eee0cf.liquid (size: 444 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.9c65c337-a31b-4bf5-873a-8423608ff900.liquid (size: 314 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.9f889b88-fce0-4904-9fd3-e2563abca319.liquid (size: 123693 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.aacb5a11-aa62-459e-ab73-43a996b6844c.liquid (size: 444 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.b06086a5-34f6-4c4d-babd-edd23e97975a.liquid (size: 639 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.b0b6630b-5d57-4fde-af92-423699a42aba.liquid (size: 639 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.b5195668-e4bc-42c3-808d-a3b1517643d1.liquid (size: 132031 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.cc823b0c-07e5-4fb7-8e46-2833c8ca81cb.liquid (size: 444 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.d45cc921-9524-451f-a691-424125b3017a.liquid (size: 639 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.de3d2b17-4441-466d-8ea8-735cb139f93d.liquid (size: 314 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.e813f58e-a823-4650-abeb-167cfd964417.liquid (size: 314 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.ec91902e-02a8-4459-961d-96cb3b4e0b88.liquid (size: 639 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.eeda25b2-825d-466d-8520-62cb631dcabf.liquid (size: 194411 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.f29ab7b3-2a18-4771-b61a-a7d4228f5d1b.liquid (size: 509 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo.f795dec7-1517-4072-8183-47a6f47e0f51.liquid (size: 444 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/page.replo_abonnement_educ.json (size: 771 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/password.json (size: 802 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.accessoire-product.json (size: 3430 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.brume-collagene.json (size: 2672 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.dod-hydralise-abonnemen.json (size: 2408 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.dod-special-offer.json (size: 1214 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.hydralise-unitaire.json (size: 2537 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.json (size: 2537 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.kit-gua-sha-replo.json (size: 2261 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.pre-order.json (size: 1887 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.replo-product-page.json (size: 2678 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.replo-product_001.json (size: 2721 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.replo_product_002.json (size: 2721 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.replo_product_003.json (size: 2721 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.replo_product_004.json (size: 2721 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.replo_product_005.json (size: 2721 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.replo_product_006.json (size: 2721 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.replo_product_007.json (size: 2721 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/product.replo_product_hydralise.json (size: 2757 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/search.json (size: 486 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/customers/account.json (size: 656 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/customers/activate_account.json (size: 506 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/customers/addresses.json (size: 499 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/customers/login.json (size: 654 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/customers/order.json (size: 495 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/customers/register.json (size: 657 bytes)...
Reading the content of file at /home/maxdesign/shopify/stores/Aloe-Paris/templates/customers/reset_password.json (size: 504 bytes)...
2025-07-22T10:48:51.162Z: Request to https://aloe-paris.myshopify.com/?preview_theme_id=184608981335&_fd=0&pb=0 completed in 1089 ms
With response headers:
 - content-type: text/html; charset=utf-8
 - server-timing: processing;dur=41;desc="gc:2", db;dur=31, db_async;dur=1.96, asn;desc="21788", edge;desc="BOM", country;desc="IN", theme;desc="184608981335", pageType;desc="index", servedBy;desc="hnqh", requestID;desc="6b2734d7-a981-43bb-8327-c368dacef883-1753181330", _y;desc="6a777086-12a6-49e6-af35-f98a765bb273", _s;desc="b1a5981d-5c5e-4cdf-a878-bb91ffb4b5ac", cfRequestDuration;dur=509.999990
 - x-request-id: 6b2734d7-a981-43bb-8327-c368dacef883-1753181330
    
2025-07-22T10:48:51.463Z: Sending "Admin" GraphQL request:
  query getThemeFileChecksums($id: ID!, $after: String) {
  theme(id: $id) {
    files(first: 250, after: $after) {
      nodes {
        filename
        size
        checksumMd5
        __typename
      }
      userErrors {
        filename
        code
        __typename
      }
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "id": "gid://shopify/OnlineStoreTheme/184608981335",
  "after": null
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:48:52.343Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 879 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=144, graphql;desc="admin/query/other", cfRequestDuration;dur=589.999914
 - x-request-id: 94c8c5bf-cd78-4ec0-a90e-93e1ddad4794-1753181331
    
2025-07-22T10:48:52.344Z: Sending "Admin" GraphQL request:
  query getThemeFileChecksums($id: ID!, $after: String) {
  theme(id: $id) {
    files(first: 250, after: $after) {
      nodes {
        filename
        size
        checksumMd5
        __typename
      }
      userErrors {
        filename
        code
        __typename
      }
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "id": "gid://shopify/OnlineStoreTheme/184608981335",
  "after": "InNlY3Rpb25zXC9tYWluLWFydGljbGUubGlxdWlkIg=="
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:48:53.191Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 847 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=107, graphql;desc="admin/query/other", cfRequestDuration;dur=542.000055
 - x-request-id: 942ee76f-1348-4703-a9bd-dd391a54bd22-1753181332
    
2025-07-22T10:48:53.191Z: Sending "Admin" GraphQL request:
  query getThemeFileChecksums($id: ID!, $after: String) {
  theme(id: $id) {
    files(first: 250, after: $after) {
      nodes {
        filename
        size
        checksumMd5
        __typename
      }
      userErrors {
        filename
        code
        __typename
      }
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "id": "gid://shopify/OnlineStoreTheme/184608981335",
  "after": "InNuaXBwZXRzXC9yZXBsby5zZWN0aW9uLXNldHRpbmdzLmUzMWZjY2RjLTIwYzktNDI2Yi1hZjBiLTAzNGMyZTg2YjEzNC5saXF1aWQi"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:48:53.930Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 739 ms
With response headers:
 - content-type: application/json; charset=utf-8
 - server-timing: processing;dur=83, graphql;desc="admin/query/other", cfRequestDuration;dur=516.000032
 - x-request-id: 164c80b1-d8fd-4fde-8b90-e61e9d903814-1753181333
    
2025-07-22T10:48:53.931Z: Initiating theme asset reconciliation process
2025-07-22T10:48:53.931Z: Initiating theme asset reconciliation process
╭─ info ──────────────────────────────────────────────────────────────────────────────╮
│                                                                                     │
│  The files listed below are only present locally. What would you like to do?        │
│    • locales/ar.json                                                                │
│    • locales/he.json                                                                │
│    • locales/lv.json                                                                │
│    • locales/uk.json                                                                │
│    • sections/maxdesign.json                                                        │
│    • sections/overlay-group.json                                                    │
│    • templates/article.gua-sha-template.json                                        │
│    • templates/article.patch-template.json                                          │
│    • templates/collection.accessoires.json                                          │
│    • templates/collection.cernes-poches.json                                        │
│    • templates/collection.contour-des-yeux.json                                     │
│    • templates/collection.deshydratation.json                                       │
│    • templates/collection.exfoliants-masques.json                                   │
│    • templates/collection.demaquillants-nettoyant.json                              │
│    • templates/collection.hydratants-jour-nuit.json                                 │
│    • templates/collection.imperfections.json                                        │
│    • templates/collection.meilleures-ventes.json                                    │
│    • templates/collection.nouveautes.json                                           │
│    • templates/collection.routine-minimaliste.json                                  │
│    • templates/collection.sensibilites.json                                         │
│    • templates/collection.routine-complete.json                                     │
│    • templates/collection.teint-terne.json                                          │
│    • templates/collection.serums-soins-cibles.json                                  │
│    • templates/page.formulaire-klaviyo.json                                         │
│    • templates/page.faq.json                                                        │
│    • templates/page.landing-page-auto.json                                          │
│    • templates/page.judgeme_reviews.json                                            │
│    • templates/page.list-collections.json                                           │
│    • templates/page.notre-vision.json                                               │
│    • templates/page.replo-details-abonnemen.json                                    │
│    • templates/page.pre-inscription-bf.json                                         │
│    • templates/page.replo_abonnement_educ.json                                      │
│    • templates/product.accessoire-product.json                                      │
│    • templates/product.brume-collagene.json                                         │
│    • templates/product.dod-special-offer.json                                       │
│    • templates/product.dod-hydralise-abonnemen.json                                 │
│    • templates/product.hydralise-unitaire.json                                      │
│    • templates/product.pre-order.json                                               │
│    • templates/product.kit-gua-sha-replo.json                                       │
│    • templates/product.replo_product_002.json                                       │
│    • templates/product.replo_product_003.json                                       │
│    • templates/product.replo_product_004.json                                       │
│    • templates/product.replo_product_005.json                                       │
│    • templates/product.replo_product_006.json                                       │
│    • templates/product.replo_product_007.json                                       │
│    • templates/product.replo_product_hydralise.json                                 │
│    • templates/customers/account.json                                               │
│    • templates/customers/activate_account.json                                      │
│    • templates/customers/login.json                                                 │
│    • templates/customers/order.json                                                 │
│    • templates/customers/addresses.json                                             │
│    • templates/customers/register.json                                              │
│    • templates/customers/reset_password.json                                        │
│                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────╯

?  Reconciliation Strategy:

>  Delete files from the local directory
   Upload local files to the remote theme

╭─ info ──────────────────────────────────────────────────────────────────────────────╮
│                                                                                     │
│  The files listed below differ between the local and remote versions. What would    │
│  you like to do?                                                                    │
│    • config/settings_data.json                                                      │
│    • config/settings_schema.json                                                    │
│    • locales/cs.json                                                                │
│    • locales/da.json                                                                │
│    • locales/de.json                                                                │
│    • locales/el.json                                                                │
│    • locales/en.default.json                                                        │
│    • locales/es.json                                                                │
│    • locales/fi.json                                                                │
│    • locales/fr.json                                                                │
│    • locales/it.json                                                                │
│    • locales/ja.json                                                                │
│    • locales/ko.json                                                                │
│    • locales/lt.json                                                                │
│    • locales/nb.json                                                                │
│    • locales/nl.json                                                                │
│    • locales/pl.json                                                                │
│    • locales/pt-BR.json                                                             │
│    • locales/ro.json                                                                │
│    • locales/ru.json                                                                │
│    • locales/sk.json                                                                │
│    • locales/sl.json                                                                │
│    • locales/sv.json                                                                │
│    • locales/tr.json                                                                │
│    • locales/zh-CN.json                                                             │
│    • locales/zh-TW.json                                                             │
│    • sections/footer-group.json                                                     │
│    • sections/header-group.json                                                     │
│    • templates/404.json                                                             │
│    • templates/article.json                                                         │
│    • templates/blog.json                                                            │
│    • templates/cart.json                                                            │
│    • templates/collection.json                                                      │
│    • templates/index.json                                                           │
│    • templates/list-collections.json                                                │
│    • templates/page.contact.json                                                    │
│    • templates/page.json                                                            │
│    • templates/password.json                                                        │
│    • templates/product.json                                                         │
│    • templates/product.replo-product-page.json                                      │
│    • templates/product.replo-product_001.json                                       │
│    • templates/search.json                                                          │
│                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────╯

?  Reconciliation Strategy:

>  Keep the remote version
   Keep the local version

   Press ↑↓ arrows to select, enter to confirm.


Wlc1MGN5QjNhV3hzSUdOaGRYTmxJSFJvWlNCd1lXZGxJSFJ2SUhOamNtOXNiQ0J5WldGc2JIa2dabUZ6ZEZ4dUx5OGdabkp2YlNCMGIzQWdkRzhnWW05MGRHOXRYRzVvZEcxc09taGhjeWcrSUM1eVpYQnNieTF0YjJSaGJDMWhablJsY2kxdmNHVnVLU0I3WEc0Z0lITmpjbTlzYkMxaVpXaGhkbWx2Y2pvZ1lYVjBieUFoYVcxd2IzSjBZVzUwTzF4dWZWeHVYRzR1WTJGeWIzVnpaV3hXTXkwdGMyeHBaR1V0Y21WelpYUWdlMXh1SUNCdFlYZ3RkMmxrZEdnNklHNXZibVVnSVdsdGNHOXlkR0Z1ZER0Y2JuMWNibHh1TG1OaGNtOTFjMlZzVmpNdGJtOHRkSEpoYm5OcGRHbHZiaUI3WEc0Z0lIUnlZVzV6YVhScGIyNDZJRzV2Ym1VN1hHNTlYRzVjYmk1allYSnZkWE5sYkZZekxXWmhaR1V0ZEhKaGJuTnBkR2x2YmlCN1hHNGdJSFJ5WVc1emFYUnBiMjQ2SUc5d1lXTnBkSGtnTVRBd01HMXpPMXh1ZlZ4dVhHNHVZMkZ5YjNWelpXeFdNeTFvYVdSa1pXNHRjMnhwWkdVZ2UxeHVJQ0IwY21GdWMybDBhVzl1T2lCdmNHRmphWFI1SURFd01EQnRjenRjYmlBZ2IzQmhZMmwwZVRvZ01EdGNibjFjYmk1allYSnZkWE5sYkZZekxYWnBjMmxpYkdVdGMyeHBaR1VnZTF4dUlDQjBjbUZ1YzJsMGFXOXVPaUJ2Y0dGamFYUjVJREV3TURCdGN6dGNiaUFnYjNCaFkybDBlVG9nTVR0Y2JuMWNibHh1THk4Z1RtOTBaU0FvVG05aGFDd2dNakF5TWkweE1TMHhNeXdnVWtWUVRDMDFNRFF3S1RvZ1UyOXRaU0IwYUdWdFpYTWdhVzVxWldOMElITjBlV3hsY3lCMGJ5QnRZV3RsSUdGc2JDQThiR2srSUdWc1pXMWxiblJ6WEc0dkx5Qm9ZWFpsSUdKMWJHeGxkQ0J3YjJsdWRITXNJR0oxZENCMGFHRjBJRzFsYzNObGN5QjNhWFJvSUc5MWNpQmpZWEp2ZFhObGJITWdkMmhwWTJnZ2NtVnVaR1Z5SUR4c2FUNXpMaUJVYUdseklISmxjMlYwYzF4dUx5OGdkR2h2YzJVZ2MzUjViR1Z6WEc0dWMzQnNhV1JsSUh0Y2JpQWdiR2tnZTF4dUlDQWdJSEJoWkdScGJtYzZJREFnSVdsdGNHOXlkR0Z1ZER0Y2JpQWdJQ0F2THlCT2IzUmxJQ2hPYjJGb0xDQXlNREl5TFRFeExURTNMQ0JTUlZCTUxUVXhNeklwT2lCRWIyNG5kQ0J2ZG1WeWNtbGtaU0J0WVhKbmFXNGdkMmwwYUNBaGFXMXdiM0owWVc1MElHSmxZMkYxYzJWY2JpQWdJQ0F2THlCcGRDQjNhV3hzSUhKbGJXOTJaU0IwYUdVZ1lYVjBiMjFoZEdsaklHMWhjbWRwYmlCMGFHRjBJRk53Ykdsa1pTQmhaR1J6SUhSdklHaGhkbVVnZEdobElHZGhjQ0IzYjNKckxseHVJQ0FnSUM4dklGUlBSRTg2SUdseklIUm9aWEpsSUdFZ1ltVjBkR1Z5SUhkaGVTQjBieUJ6YjJ4MlpTQjBhR2x6UHlCVVpXTm9ibWxqWVd4c2VTQnBaaUIwYUdWeVpTZHpJRzFoY21kcGJpQnZiaUIwYUdWY2JpQWdJQ0F2THlCMGFHVnRaU0J2YmlCc2FTZHpJSGRwZEdnZ2FHbG5hQ0JsYm05MVoyZ2djM0JsWTJsbWFXTnBkSGtzSUdsMElIZHBiR3dnYzNScGJHd2diM1psY25KcFpHVWdkR2hwY3k1Y2JpQWdJQ0J0WVhKbmFXNDZJREE3WEc0Z0lDQWdKam82WW1WbWIzSmxJSHRjYmlBZ0lDQWdJR1JwYzNCc1lYazZJRzV2Ym1VZ0lXbHRjRzl5ZEdGdWREdGNiaUFnSUNCOVhHNGdJSDFjYmx4dUlDQXVjM0JzYVdSbFgxOXNhWE4wSUh0Y2JpQWdJQ0F2THlCT2IzUmxJQ2hPYjJGb0xDQXlNREl5TFRFeUxUQTNMQ0JTUlZCTUxUVTBNREFwT2lCVGIyMWxJSFJvWlcxbGN5QnpaWFFnWVd4c0lIVnNKM01nZEc4Z2IzWmxjbVpzYjNjZ2FHbGtaR1Z1SUNoc2JXRnZLVnh1SUNBZ0lDOHZJR0oxZENCVGNHeHBaR1VnYm1WbFpITWdkRzhnWW1VZ2RtbHphV0pzWlNCcGJpQnZjbVJsY2lCbWIzSWdhWFFnZEc4Z2QyOXlheUJ3Y205d1pYSnNlU0IzYVhSb0lHbDBjeUJoYm1sdFlYUmxaQ0IwY21GdWMyWnZjbTFjYmlBZ0lDQXZMeUJ3Y205d1pYSjBlUzRnU1dZZ2QyVWdaRzl1SjNRZ2MyVjBJSFJvYVhNc0lHOXVJSE52YldVZ2RHaGxiV1Z6SUdOaGNtOTFjMlZzY3lCM2FXeHNJR3h2YjJzZ2FXNWpiM0p5WldOMElHRm1kR1Z5SUhSb1pTQm1hWEp6ZEZ4dUlDQWdJQzh2SUhOc2FXUmxYRzRnSUNBZ2IzWmxjbVpzYjNjNklIWnBjMmxpYkdVZ0lXbHRjRzl5ZEdGdWREdGNiaUFnZlZ4dWZWeHVYRzVBYTJWNVpuSmhiV1Z6SUhKbGNHeHZMVzFoY25GMVpXVWdlMXh1SUNCbWNtOXRJSHRjYmlBZ0lDQjBjbUZ1YzJadmNtMDZJSFJ5WVc1emJHRjBaVmdvTUNrN1hHNGdJSDFjYmlBZ2RHOGdlMXh1SUNBZ0lIUnlZVzV6Wm05eWJUb2dkSEpoYm5Oc1lYUmxXQ2hjYmlBZ0lDQWdJR05oYkdNb1hHNGdJQ0FnSUNBZ0lIWmhjaWd0TFhKbGNHeHZMVzFoY25GMVpXVXRkMmxrZEdnc0lERXdNQ1VwSUNvZ0xURWdMMXh1SUNBZ0lDQWdJQ0FnSUhaaGNpZ3RMWEpsY0d4dkxXMWhjbkYxWldVdGNtVndaWFJwZEdsdmJuTXNJREl3S1Z4dUlDQWdJQ0FnS1Z4dUlDQWdJQ2s3WEc0Z0lIMWNibjFjYmx4dUx5OGdUbTkwWlNBb1EyaGhibU5sTENBeU1ESXpMVEE0TFRBektTQk5ZWEp4ZFdWbElHNXZJR3h2Ym1kbGNpQjFjMlZ6SUhSb1pYTmxJR3RsZVdaeVlXMWxjeXdnWW5WMElIUm9aWGxjYmk4dklHRnlaU0JvWlhKbElHWnZjaUJpWVdOcklHTnZiWEJoZENCcWRYTjBJR2x1SUdOaGMyVWdZU0IxYzJWeUlISmxabVZ5Wlc1alpYTWdkR2hsYlNCbWIzSWdjMjl0WlNCeVpXRnpiMjR1WEc0dkwxeHVMeThnVG05MFpTQW9UbTloYUN3Z01qQXlNUzB3T1Mwd09TazZJRlJvWlNCMGNtRnVjMnhoZEdWWUlIWmhiSFZsSUdobGNtVWdhWE1nWkdseVpXTjBiSGtnWTI5eWNtVnNZWFJsWkZ4dUx5OGdkMmwwYUNCMGFHVWdaR1ZtYVc1cGRHbHZiaUJ2WmlCdFlYSnhkV1ZsVkhKaFkydE9kVzFpWlhKUFprbDBaVzF6TENCcGRDQnVaV1ZrY3lCMGJ5QmlaU0JsZUdGamRHeDVPbHh1THk4Z0xURXdNQzl0WVhKeGRXVmxWSEpoWTJ0T2RXMWlaWEpQWmtsMFpXMXpJQ1VnWm05eUlIUm9aU0JoYm1sdFlYUnBiMjRnZEc4Z1kzbGpiR1VnYzJWaGJXeGxjM05zZVZ4dVFHdGxlV1p5WVcxbGN5QmhiR05vWlcxNUxXMWhjbkYxWldVdGJHVm1kQ0I3WEc0Z0lHWnliMjBnZTF4dUlDQWdJSFJ5WVc1elptOXliVG9nZEhKaGJuTnNZWFJsV0Nnd0tUdGNiaUFnZlZ4dUlDQjBieUI3WEc0Z0lDQWdkSEpoYm5ObWIzSnRPaUIwY21GdWMyeGhkR1ZZS0Z4dUlDQWdJQ0FnWTJGc1l5aGNiaUFnSUNBZ0lDQWdkbUZ5S0MwdGNtVndiRzh0YldGeWNYVmxaUzEzYVdSMGFDd2dNVEF3SlNrZ0tpQXRNU0F2WEc0Z0lDQWdJQ0FnSUNBZ2RtRnlLQzB0Y21Wd2JHOHRiV0Z5Y1hWbFpTMXlaWEJsZEdsMGFXOXVjeXdnTWpBcFhHNGdJQ0FnSUNBcFhHNGdJQ0FnS1R0Y2JpQWdmVnh1ZlZ4dVhHNUFhMlY1Wm5KaGJXVnpJR0ZzWTJobGJYa3RiV0Z5Y1hWbFpTMXlhV2RvZENCN1hHNGdJR1p5YjIwZ2UxeHVJQ0FnSUhSeVlXNXpabTl5YlRvZ2RISmhibk5zWVhSbFdDZ3ROVEFsS1R0Y2JpQWdmVnh1SUNCMGJ5QjdYRzRnSUNBZ2RISmhibk5tYjNKdE9pQjBjbUZ1YzJ4aGRHVllLRnh1SUNBZ0lDQWdZMkZzWXloY2JpQWdJQ0FnSUNBZ0xUVXdKU0FySUhaaGNpZ3RMWEpsY0d4dkxXMWhjbkYxWldVdGQybGtkR2dzSURFd01DVXBJQzhnZG1GeUtDMHRjbVZ3Ykc4dGJXRnljWFZsWlMxeVpYQmxkR2wwYVc5dWN5d2dNakFwWEc0Z0lDQWdJQ0FwWEc0Z0lDQWdLVHRjYmlBZ2ZWeHVmVnh1WEc1QWEyVjVabkpoYldWeklHRnNZMmhsYlhrdFptRmtaU0I3WEc0Z0lHWnliMjBnZTF4dUlDQWdJRzl3WVdOcGRIazZJSFpoY2lndExXbHVhWFJwWVd3dGIzQmhZMmwwZVNrN1hHNGdJSDFjYmlBZ2RHOGdlMXh1SUNBZ0lHOXdZV05wZEhrNklIWmhjaWd0TFdacGJtRnNMVzl3WVdOcGRIa3BPMXh1SUNCOVhHNTlYRzVjYmtCclpYbG1jbUZ0WlhNZ1lXeGphR1Z0ZVMxemJHbGtaUzE1SUh0Y2JpQWdabkp2YlNCN1hHNGdJQ0FnYjNCaFkybDBlVG9nZG1GeUtDMHRhVzVwZEdsaGJDMXZjR0ZqYVhSNUtUdGNiaUFnSUNCMGNtRnVjMlp2Y20wNklIUnlZVzV6YkdGMFpWa29kbUZ5S0MwdGIyWm1jMlYwS1NrN1hHNGdJSDFjYmlBZ2RHOGdlMXh1SUNBZ0lHOXdZV05wZEhrNklIWmhjaWd0TFdacGJtRnNMVzl3WVdOcGRIa3BPMXh1SUNBZ0lIUnlZVzV6Wm05eWJUb2dkSEpoYm5Oc1lYUmxXU2d3S1R0Y2JpQWdmVnh1ZlZ4dVhHNUFhMlY1Wm5KaGJXVnpJR0ZzWTJobGJYa3RjMnhwWkdVdGVDQjdYRzRnSUdaeWIyMGdlMXh1SUNBZ0lHOXdZV05wZEhrNklIWmhjaWd0TFdsdWFYUnBZV3d0YjNCaFkybDBlU2s3WEc0Z0lDQWdkSEpoYm5ObWIzSnRPaUIwY21GdWMyeGhkR1ZZS0haaGNpZ3RMVzltWm5ObGRDa3BPMXh1SUNCOVhHNGdJSFJ2SUh0Y2JpQWdJQ0J2Y0dGamFYUjVPaUIyWVhJb0xTMW1hVzVoYkMxdmNHRmphWFI1S1R0Y2JpQWdJQ0IwY21GdWMyWnZjbTA2SUhSeVlXNXpiR0YwWlZnb01DazdYRzRnSUgxY2JuMWNibHh1UUd0bGVXWnlZVzFsY3lCaGJHTm9aVzE1TFdac2FYQXRlU0I3WEc0Z0lHWnliMjBnZTF4dUlDQWdJRzl3WVdOcGRIazZJSFpoY2lndExXbHVhWFJwWVd3dGIzQmhZMmwwZVNrN1hHNGdJQ0FnZEhKaGJuTm1iM0p0T2lCeWIzUmhkR1ZaS0haaGNpZ3RMV0Z1WjJ4bEtTazdYRzRnSUgxY2JpQWdkRzhnZTF4dUlDQWdJRzl3WVdOcGRIazZJSFpoY2lndExXWnBibUZzTFc5d1lXTnBkSGtwTzF4dUlDQWdJSFJ5WVc1elptOXliVG9nY205MFlYUmxXU2d3S1R0Y2JpQWdmVnh1ZlZ4dVhHNUFhMlY1Wm5KaGJXVnpJR0ZzWTJobGJYa3RabXhwY0MxNElIdGNiaUFnWm5KdmJTQjdYRzRnSUNBZ2IzQmhZMmwwZVRvZ2RtRnlLQzB0YVc1cGRHbGhiQzF2Y0dGamFYUjVLVHRjYmlBZ0lDQjBjbUZ1YzJadmNtMDZJSEp2ZEdGMFpWZ29kbUZ5S0MwdFlXNW5iR1VwS1R0Y2JpQWdmVnh1SUNCMGJ5QjdYRzRnSUNBZ2IzQmhZMmwwZVRvZ2RtRnlLQzB0Wm1sdVlXd3RiM0JoWTJsMGVTazdYRzRnSUNBZ2RISmhibk5tYjNKdE9pQnliM1JoZEdWWUtEQXBPMXh1SUNCOVhHNTlYRzVjYmtCclpYbG1jbUZ0WlhNZ1lXeGphR1Z0ZVMxbmNtOTNJSHRjYmlBZ1puSnZiU0I3WEc0Z0lDQWdiM0JoWTJsMGVUb2dkbUZ5S0MwdGFXNXBkR2xoYkMxdmNHRmphWFI1S1R0Y2JpQWdJQ0IwY21GdWMyWnZjbTA2SUhOallXeGxLSFpoY2lndExXbHVhWFJwWVd3dGMyTmhiR1VwS1R0Y2JpQWdmVnh1SUNCMGJ5QjdYRzRnSUNBZ2IzQmhZMmwwZVRvZ2RtRnlLQzB0Wm1sdVlXd3RiM0JoWTJsMGVTazdYRzRnSUNBZ2RISmhibk5tYjNKdE9pQnpZMkZzWlNoMllYSW9MUzFtYVc1aGJDMXpZMkZzWlNrcE8xeHVJQ0I5WEc1OVhHNWNia0JyWlhsbWNtRnRaWE1nWVd4amFHVnRlUzF6Y0dsdUlIdGNiaUFnWm5KdmJTQjdYRzRnSUNBZ2IzQmhZMmwwZVRvZ2RtRnlLQzB0YVc1cGRHbGhiQzF2Y0dGamFYUjVLVHRjYmlBZ0lDQjBjbUZ1YzJadmNtMDZJSEp2ZEdGMFpTaDJZWElvTFMxcGJtbDBhV0ZzTFdGdVoyeGxLU2s3WEc0Z0lIMWNiaUFnZEc4Z2UxeHVJQ0FnSUc5d1lXTnBkSGs2SUhaaGNpZ3RMV1pwYm1Gc0xXOXdZV05wZEhrcE8xeHVJQ0FnSUhSeVlXNXpabTl5YlRvZ2NtOTBZWFJsS0haaGNpZ3RMV1pwYm1Gc0xXRnVaMnhsS1NrN1hHNGdJSDFjYm4xY2JseHVRR3RsZVdaeVlXMWxjeUJoYkdOb1pXMTVMV1pzZVMxNUlIdGNiaUFnWm5KdmJTQjdYRzRnSUNBZ2IzQmhZMmwwZVRvZ2RtRnlLQzB0YVc1cGRHbGhiQzF2Y0dGamFYUjVLVHRjYmlBZ0lDQjBjbUZ1YzJadmNtMDZJSFJ5WVc1emJHRjBaVmtvZG1GeUtDMHRiMlptYzJWMEtTa2djMk5oYkdVb01DazdYRzRnSUgxY2JpQWdkRzhnZTF4dUlDQWdJRzl3WVdOcGRIazZJSFpoY2lndExXWnBibUZzTFc5d1lXTnBkSGtwTzF4dUlDQWdJSFJ5WVc1elptOXliVG9nZEhKaGJuTnNZWFJsV1Nnd0tTQnpZMkZzWlNneEtUdGNiaUFnZlZ4dWZWeHVYRzVBYTJWNVpuSmhiV1Z6SUdGc1kyaGxiWGt0Wm14NUxYZ2dlMXh1SUNCbWNtOXRJSHRjYmlBZ0lDQnZjR0ZqYVhSNU9pQjJZWElvTFMxcGJtbDBhV0ZzTFc5d1lXTnBkSGtwTzF4dUlDQWdJSFJ5WVc1elptOXliVG9nZEhKaGJuTnNZWFJsV0NoMllYSW9MUzF2Wm1aelpYUXBLU0J6WTJGc1pTZ3dLVHRjYmlBZ2ZWeHVJQ0IwYnlCN1hHNGdJQ0FnYjNCaFkybDBlVG9nZG1GeUtDMHRabWx1WVd3dGIzQmhZMmwwZVNrN1hHNGdJQ0FnZEhKaGJuTm1iM0p0T2lCMGNtRnVjMnhoZEdWWUtEQXBJSE5qWVd4bEtERXBPMXh1SUNCOVhHNTlYRzVjYmtCclpYbG1jbUZ0WlhNZ1lXeGphR1Z0ZVMxa2NtOXdJSHRjYmlBZ1puSnZiU0I3WEc0Z0lDQWdiM0JoWTJsMGVUb2dkbUZ5S0MwdGFXNXBkR2xoYkMxdmNHRmphWFI1S1R0Y2JpQWdJQ0IwY21GdWMyWnZjbTA2SUhSeVlXNXpiR0YwWlZrb2RtRnlLQzB0YjJabWMyVjBLU2s3WEc0Z0lIMWNiaUFnZEc4Z2UxeHVJQ0FnSUc5d1lXTnBkSGs2SUhaaGNpZ3RMV1pwYm1Gc0xXOXdZV05wZEhrcE8xeHVJQ0FnSUhSeVlXNXpabTl5YlRvZ2RISmhibk5zWVhSbFdTZ3dLVHRjYmlBZ2ZWeHVmVnh1WEc1QWEyVjVabkpoYldWeklISmxjR3h2TFhOd2FXNGdlMXh1SUNCMGJ5QjdYRzRnSUNBZ2RISmhibk5tYjNKdE9pQnliM1JoZEdVb016WXdaR1ZuS1R0Y2JpQWdmVnh1ZlZ4dVhHNUFhMlY1Wm5KaGJXVnpJSE5vYVcxdFpYSWdlMXh1SUNBeE1EQWxJSHRjYmlBZ0lDQnRZWE5yTFhCdmMybDBhVzl1T2lCc1pXWjBYRzRnSUgxY2JuMWNibHh1TG5KbGNHeHZMV0Z1YVcxaGRHVXRjM0JwYm01bGNpQjdYRzRnSUdGdWFXMWhkR2x2YmpvZ2NtVndiRzh0YzNCcGJpQXhjeUJzYVc1bFlYSWdhVzVtYVc1cGRHVTdYRzU5WEc1Y2JpOHZJRTVQVkVVZ0tFcGhZMnR6YjI0c0lESXdNalF0TVRFdE1qRXBPaUJVYUdseklIQnpaWFZrYnkxbGJHVnRaVzUwSUdoaFkyc2dhWE1nYUdWeVpTQnBiaUJ5WldkaGNtUnpJSFJ2SUZKRlVFd3RNVEkyT0RRZ0xWeHVMeThnZEdobGNtVWdjMlZsYlhNZ2RHOGdZbVVnWVNCaWRXY2dkMmwwYUNCMGFHVWdZWEpwWVd0cGRDQjBiMjlzZEdsd0lHTnZiWEJ2Ym1WdWRDQjBhR0YwSUdOaGJtNXZkQ0JpWlNCbWFYaGxaQ0IzYVhSb1hHNHZMeUJ6ZEdGdVpHRnlaQ0JqYzNNZ2JtOXlJR2x6SUdsMElIZHZjblJvSUhWeklIZHlhWFJwYm1jZ1lTQmpkWE4wYjIwZ1kyOXRjRzl1Wlc1MElHWnZjaUJoZENCMGFHbHpJSFJwYldWY2JpNTBiMjlzZEdsd0xXRnljbTkzT2pwaVpXWnZjbVVnZTF4dUlDQmpiMjUwWlc1ME9pQmNJbHdpTzF4dUlDQndiM05wZEdsdmJqb2dZV0p6YjJ4MWRHVTdYRzRnSUhSdmNEb2dMVEF1TjNCNE8xeHVJQ0JzWldaME9pQXdPMXh1SUNCeWFXZG9kRG9nTUR0Y2JpQWdhR1ZwWjJoME9pQXhjSGc3WEc0Z0lHSmhZMnRuY205MWJtUTZJSGRvYVhSbE8xeHVJQ0IzYVdSMGFEb2dOekVsTzF4dUlDQnRZWEpuYVc0dGJHVm1kRG9nWVhWMGJ6dGNiaUFnYldGeVoybHVMWEpwWjJoME9pQmhkWFJ2TzF4dWZWeHVYRzR2THlCRGIyeHNZWEJ6YVdKc1pTQmhibWx0WVhScGIyNGdjM1I1YkdWelhHNWJaR0YwWVMxeVpYQnNieTFqYjJ4c1lYQnphV0pzWlYwZ0xuSmxjR3h2TFdGdWFXMWhkR1ZrSUh0Y2JpQWdiM1psY21ac2IzYzZJR2hwWkdSbGJqdGNibjFjYmx0a1lYUmhMWEpsY0d4dkxXTnZiR3hoY0hOcFlteGxYU0F1Y21Wd2JHOHRZVzVwYldGMFpXUmJaR0YwWVMxemRHRjBaVDFjSW05d1pXNWNJbDBnZTF4dUlDQmhibWx0WVhScGIyNDZJSE5zYVdSbFJHOTNiaUF5TURCdGN5QmpkV0pwWXkxaVpYcHBaWElvTUM0MExDQXdMQ0F3TGpJc0lERXBPMXh1ZlZ4dVcyUmhkR0V0Y21Wd2JHOHRZMjlzYkdGd2MybGliR1ZkSUM1eVpYQnNieTFoYm1sdFlYUmxaRnRrWVhSaExYTjBZWFJsUFZ3aVkyeHZjMlZrWENKZElIdGNiaUFnWVc1cGJXRjBhVzl1T2lCemJHbGtaVlZ3SURJd01HMXpJR04xWW1sakxXSmxlbWxsY2lnd0xqUXNJREFzSURBdU1pd2dNU2s3WEc1OVhHNWNia0JyWlhsbWNtRnRaWE1nYzJ4cFpHVkViM2R1SUh0Y2JpQWdabkp2YlNCN1hHNGdJQ0FnYUdWcFoyaDBPaUF3TzF4dUlDQjlYRzRnSUhSdklIdGNiaUFnSUNCb1pXbG5hSFE2SUhaaGNpZ3RMWEpoWkdsNExXTnZiR3hoY0hOcFlteGxMV052Ym5SbGJuUXRhR1ZwWjJoMEtUdGNiaUFnZlZ4dWZWeHVYRzVBYTJWNVpuSmhiV1Z6SUhOc2FXUmxWWEFnZTF4dUlDQm1jbTl0SUh0Y2JpQWdJQ0JvWldsbmFIUTZJSFpoY2lndExYSmhaR2w0TFdOdmJHeGhjSE5wWW14bExXTnZiblJsYm5RdGFHVnBaMmgwS1R0Y2JpQWdmVnh1SUNCMGJ5QjdYRzRnSUNBZ2FHVnBaMmgwT2lBd08xeHVJQ0I5WEc1OVhHNWNiaTV5WlhCc2J5MXpjaTF2Ym14NUlIdGNiaUFnY0c5emFYUnBiMjQ2SUdGaWMyOXNkWFJsTzF4dUlDQjNhV1IwYURvZ01YQjRPMXh1SUNCb1pXbG5hSFE2SURGd2VEdGNiaUFnY0dGa1pHbHVaem9nTUR0Y2JpQWdiV0Z5WjJsdU9pQXRNWEI0TzF4dUlDQnZkbVZ5Wm14dmR6b2dhR2xrWkdWdU8xeHVJQ0JqYkdsd09pQnlaV04wS0RBc0lEQXNJREFzSURBcE8xeHVJQ0IzYUdsMFpTMXpjR0ZqWlRvZ2JtOTNjbUZ3TzF4dUlDQmliM0prWlhJdGQybGtkR2c2SURBN1hHNTlYRzVjYmx0a1lYUmhMWEpsY0d4dkxXTnZiWEJ2Ym1WdWRDMXliMjkwUFZ3aVkyRnliM1Z6Wld4Y0lsMGdlMXh1SUNBbU9uZG9aWEpsS0Z0a1lYUmhMWEpsY0d4dkxYQmhjblF0YVdROVhDSnpiR2xrWlMxMGNtRmphMXdpWFNrZ2UxeHVJQ0FnSUhOamNtOXNiR0poY2kxM2FXUjBhRG9nYm05dVpUdGNiaUFnSUNBbU9qb3RkMlZpYTJsMExYTmpjbTlzYkdKaGNpQjdYRzRnSUNBZ0lDQmthWE53YkdGNU9pQnViMjVsTzF4dUlDQWdJSDFjYmlBZ2ZWeHVmVnh1SWl3aVFHMXBlR2x1SUhKcFkyZ3RkR1Y0ZEMxemRIbHNaWE1nZTF4dUlDQmhMRnh1SUNCd0xGeHVJQ0J6TEZ4dUlDQjFMRnh1SUNCaUxGeHVJQ0JwTEZ4dUlDQm9NU3hjYmlBZ2FESXNYRzRnSUdnekxGeHVJQ0JvTkN4Y2JpQWdhRFVzWEc0Z0lHZzJMRnh1SUNCdFlYSnJJSHRjYmlBZ0lDQm1iMjUwTFhOMGVXeGxPaUJwYm1obGNtbDBPMXh1SUNBZ0lHWnZiblF0Wm1GdGFXeDVPaUJwYm1obGNtbDBPMXh1SUNBZ0lIUmxlSFF0WkdWamIzSmhkR2x2YmpvZ2FXNW9aWEpwZER0Y2JpQWdJQ0IwWlhoMExXRnNhV2R1T2lCcGJtaGxjbWwwTzF4dUlDQWdJSFJsZUhRdGRISmhibk5tYjNKdE9pQnBibWhsY21sME8xeHVJQ0FnSUdOdmJHOXlPaUJwYm1obGNtbDBPMXh1SUNBZ0lHeHBibVV0YUdWcFoyaDBPaUJwYm1obGNtbDBPMXh1WEc0Z0lDQWdiR1YwZEdWeUxYTndZV05wYm1jNklHbHVhR1Z5YVhRN1hHNGdJQ0FnYldGeVoybHVPaUF3TzF4dUlDQWdJSEJoWkdScGJtYzZJREE3WEc0Z0lDQWdZbTl5WkdWeU9pQXdPMXh1SUNBZ0lHWnZiblF0ZDJWcFoyaDBPaUJwYm1obGNtbDBPMXh1SUNBZ0lIWmxjblJwWTJGc0xXRnNhV2R1T2lCaVlYTmxiR2x1WlR0Y2JpQWdJQ0JtYjI1MExYTnBlbVU2SURFd01DVTdYRzRnSUNBZ0x5OGdUbTkwWlNBb1RtOWhhQ3dnVWtWUVRDMDBNRGszS1RvZ2RHVjRkQzF6YVhwbExXRmthblZ6ZENCd2NtVjJaVzUwY3lCcFQxTWdjMkZtWVhKcElHWnliMjFjYmlBZ0lDQXZMeUJwYm1ac1lYUnBibWNnZEdWNGRDQnphWHBsWEc0Z0lDQWdMeThnYUhSMGNITTZMeTlyYVd4cFlXNTJZV3hyYUc5bUxtTnZiUzh5TURJeUwyTnpjeTFvZEcxc0wzbHZkWEl0WTNOekxYSmxjMlYwTFc1bFpXUnpMWFJsZUhRdGMybDZaUzFoWkdwMWMzUXRjSEp2WW1GaWJIa3ZYRzRnSUNBZ0xXMXZlaTEwWlhoMExYTnBlbVV0WVdScWRYTjBPaUJ1YjI1bE8xeHVJQ0FnSUMxM1pXSnJhWFF0ZEdWNGRDMXphWHBsTFdGa2FuVnpkRG9nYm05dVpUdGNiaUFnSUNCMFpYaDBMWE5wZW1VdFlXUnFkWE4wT2lCdWIyNWxPMXh1WEc0Z0lDQWdMeThnU0dsa1pTQnpZM0p2Ykd4aVlYSnpJR0o1SUdSbFptRjFiSFJjYmlBZ0lDQW1Pam90ZDJWaWEybDBMWE5qY205c2JHSmhjaUI3WEc0Z0lDQWdJQ0JrYVhOd2JHRjVPaUJ1YjI1bE8xeHVJQ0FnSUgxY2JpQWdJQ0F0YlhNdGIzWmxjbVpzYjNjdGMzUjViR1U2SUc1dmJtVTdYRzRnSUNBZ2MyTnliMnhzWW1GeUxYZHBaSFJvT2lCdWIyNWxPMXh1SUNCOVhHNWNiaUFnWWl4Y2JpQWdjM1J5YjI1bkxGeHVJQ0IxTEZ4dUlDQnBMRnh1SUNCbGJTeGNiaUFnY3l4Y2JpQWdaR1ZzTEZ4dUlDQnNhU3hjYmlBZ2MzQmhiaUI3WEc0Z0lDQWdabTl1ZEMxbVlXMXBiSGs2SUdsdWFHVnlhWFE3WEc0Z0lIMWNibHh1SUNCMUlIdGNiaUFnSUNCMFpYaDBMV1JsWTI5eVlYUnBiMjQ2SUhWdVpHVnliR2x1WlR0Y2JpQWdmVnh1WEc0Z0lITXNYRzRnSUdSbGJDQjdYRzRnSUNBZ2RHVjRkQzFrWldOdmNtRjBhVzl1T2lCc2FXNWxMWFJvY205MVoyZzdYRzRnSUgxY2JseHVJQ0JwSUh0Y2JpQWdJQ0JtYjI1MExYTjBlV3hsT2lCcGRHRnNhV003WEc0Z0lIMWNibHh1SUNCaUlIdGNiaUFnSUNCbWIyNTBMWGRsYVdkb2REb2dZbTlzWkR0Y2JpQWdmVnh1WEc0Z0lDOHZJRTV2ZEdVZ0tFNXZZV2dzSURJd01qRXRNRGt0TURrcE9pQlVhR2x6SUdseklHNWxZMlZ6YzJGeWVTQmlaV05oZFhObElITnZiV1VnZEdobGJXVnpJQ2hzYVd0bElHUmxZblYwUHo4cElHaGhkbVVnWTNOeklISmxjMlYwYzF4dUlDQXZMeUIzYUdsamFDQnpaWFFnYkdsemRDMXpkSGxzWlNCMGJ5QnViMjVsTGlCWFpTQnlaWE5sZENCaVlXTnJJSFJ2SUdsdWFHVnlhWFFnYzI4Z2RHaGhkQ0JpZFd4c1pYUWdiR2x6ZENCaWRXeHNaWFJ6SUdGamRIVmhiR3g1SUhOb2IzY2dkWEJjYmlBZ2RXd3NYRzRnSUd4cElIdGNiaUFnSUNCc2FYTjBMWE4wZVd4bE9pQnBibWhsY21sME8xeHVJQ0FnSUM4dklGUm9hWE1nYVhNZ2QyVnBjbVFzSUdKMWRDQmlkV3hzWlhRZ2NHOXBiblJ6SUdSdmJpZDBJR2hoZG1VZ2NHRmtaR2x1WnlCaWVTQmtaV1poZFd4MElHbHVJRkpVUlZ4dUlDQWdJQzh2SUhOcGJtTmxJSGRsSUhKbGMyVjBJSFJvWldseUlIQmhaR1JwYm1jZ1lXSnZkbVVzSUhkb2FXTm9JRzFsWVc1eklIUm9aWGtnY21WdVpHVnlJR2x1WTI5eWNtVmpkR3g1WEc0Z0lDQWdMeThnZEc4Z2RHaGxJR3hsWm5RdUlGTmxkQ0IwYUdWdElIUnZJR0Z1SUdGeVltbDBjbUZ5ZVNCMllXeDFaU0IwYnlCdFlXdGxJSFJvWlcwZ2JHOXZheUJuYjI5a0lDaDFjMlZjYmlBZ0lDQXZMeUJsYlNCMGJ5QnpZMkZzWlNCM2FYUm9JSFJvWlNCbWIyNTBJSE5wZW1VcFhHNGdJQ0FnY0dGa1pHbHVaeTFzWldaME9pQXhMamRsYlR0Y2JpQWdmVnh1WEc0Z0lHTnZaR1VnZTF4dUlDQWdJR0poWTJ0bmNtOTFibVF0WTI5c2IzSTZJSEpuWW1Fb0l6WXhOakUyTVN3Z01DNHhLVHRjYmlBZ0lDQmpiMnh2Y2pvZ0l6WXhOakUyTVR0Y2JpQWdmVnh1WEc0Z0lIQnlaU0I3WEc0Z0lDQWdZbUZqYTJkeWIzVnVaRG9nSXpCa01HUXdaRHRjYmlBZ0lDQmpiMnh2Y2pvZ0kyWm1aanRjYmlBZ0lDQm1iMjUwTFdaaGJXbHNlVG9nWENKS1pYUkNjbUZwYm5OTmIyNXZYQ0lzSUcxdmJtOXpjR0ZqWlR0Y2JpQWdJQ0J3WVdSa2FXNW5PaUF3TGpjMWNtVnRJREZ5WlcwN1hHNGdJQ0FnWW05eVpHVnlMWEpoWkdsMWN6b2dNQzQxY21WdE8xeHVYRzRnSUNBZ1kyOWtaU0I3WEc0Z0lDQWdJQ0JqYjJ4dmNqb2dhVzVvWlhKcGREdGNiaUFnSUNBZ0lIQmhaR1JwYm1jNklEQTdYRzRnSUNBZ0lDQmlZV05yWjNKdmRXNWtPaUJ1YjI1bE8xeHVJQ0FnSUNBZ1ptOXVkQzF6YVhwbE9pQXdMamh5WlcwN1hHNGdJQ0FnZlZ4dUlDQjlYRzVjYmlBZ2FXMW5JSHRjYmlBZ0lDQnRZWGd0ZDJsa2RHZzZJREV3TUNVN1hHNGdJQ0FnYUdWcFoyaDBPaUJoZFhSdk8xeHVJQ0I5WEc1Y2JpQWdZbXh2WTJ0eGRXOTBaU0I3WEc0Z0lDQWdjR0ZrWkdsdVp5MXNaV1owT2lBeGNtVnRPMXh1SUNBZ0lHSnZjbVJsY2kxc1pXWjBPaUF5Y0hnZ2MyOXNhV1FnY21kaVlTZ2pNR1F3WkRCa0xDQXdMakVwTzF4dUlDQjlYRzVjYmlBZ2FISWdlMXh1SUNBZ0lHSnZjbVJsY2pvZ2JtOXVaVHRjYmlBZ0lDQmliM0prWlhJdGRHOXdPaUF5Y0hnZ2MyOXNhV1FnY21kaVlTZ2pNR1F3WkRCa0xDQXdMakVwTzF4dUlDQWdJRzFoY21kcGJqb2dNbkpsYlNBd08xeHVJQ0I5WEc1OVhHNGlYWDA9ICovIiwiQG1peGluIHJpY2gtdGV4dC1zdHlsZXMge1xuICBhLFxuICBwLFxuICBzLFxuICB1LFxuICBiLFxuICBpLFxuICBoMSxcbiAgaDIsXG4gIGgzLFxuICBoNCxcbiAgaDUsXG4gIGg2LFxuICBtYXJrIHtcbiAgICBmb250LXN0eWxlOiBpbmhlcml0O1xuICAgIGZvbnQtZmFtaWx5OiBpbmhlcml0O1xuICAgIHRleHQtZGVjb3JhdGlvbjogaW5oZXJpdDtcbiAgICB0ZXh0LWFsaWduOiBpbmhlcml0O1xuICAgIHRleHQtdHJhbnNmb3JtOiBpbmhlcml0O1xuICAgIGNvbG9yOiBpbmhlcml0O1xuICAgIGxpbmUtaGVpZ2h0OiBpbmhlcml0O1xuXG4gICAgbGV0dGVyLXNwYWNpbmc6IGluaGVyaXQ7XG4gICAgbWFyZ2luOiAwO1xuICAgIHBhZGRpbmc6IDA7XG4gICAgYm9yZGVyOiAwO1xuICAgIGZvbnQtd2VpZ2h0OiBpbmhlcml0O1xuICAgIHZlcnRpY2FsLWFsaWduOiBiYXNlbGluZTtcbiAgICBmb250LXNpemU6IDEwMCU7XG4gICAgLy8gTm90ZSAoTm9haCwgUkVQTC00MDk3KTogdGV4dC1zaXplLWFkanVzdCBwcmV2ZW50cyBpT1Mgc2FmYXJpIGZyb21cbiAgICAvLyBpbmZsYXRpbmcgdGV4dCBzaXplXG4gICAgLy8gaHR0cHM6Ly9raWxpYW52YWxraG9mLmNvbS8yMDIyL2Nzcy1odG1sL3lvdXItY3NzLXJlc2V0LW5lZWRzLXRleHQtc2l6ZS1hZGp1c3QtcHJvYmFibHkvXG4gICAgLW1vei10ZXh0LXNpemUtYWRqdXN0OiBub25lO1xuICAgIC13ZWJraXQtdGV4dC1zaXplLWFkanVzdDogbm9uZTtcbiAgICB0ZXh0LXNpemUtYWRqdXN0OiBub25lO1xuXG4gICAgLy8gSGlkZSBzY3JvbGxiYXJzIGJ5IGRlZmF1bHRcbiAgICAmOjotd2Via2l0LXNjcm9sbGJhciB7XG4gICAgICBkaXNwbGF5OiBub25lO1xuICAgIH1cbiAgICAtbXMtb3ZlcmZsb3ctc3R5bGU6IG5vbmU7XG4gICAgc2Nyb2xsYmFyLXdpZHRoOiBub25lO1xuICB9XG5cbiAgYixcbiAgc3Ryb25nLFxuICB1LFxuICBpLFxuICBlbSxcbiAgcyxcbiAgZGVsLFxuICBsaSxcbiAgc3BhbiB7XG4gICAgZm9udC1mYW1pbHk6IGluaGVyaXQ7XG4gIH1cblxuICB1IHtcbiAgICB0ZXh0LWRlY29yYXRpb246IHVuZGVybGluZTtcbiAgfVxuXG4gIHMsXG4gIGRlbCB7XG4gICAgdGV4dC1kZWNvcmF0aW9uOiBsaW5lLXRocm91Z2g7XG4gIH1cblxuICBpIHtcbiAgICBmb250LXN0eWxlOiBpdGFsaWM7XG4gIH1cblxuICBiIHtcbiAgICBmb250LXdlaWdodDogYm9sZDtcbiAgfVxuXG4gIC8vIE5vdGUgKE5vYWgsIDIwMjEtMDktMDkpOiBUaGlzIGlzIG5lY2Vzc2FyeSBiZWNhdXNlIHNvbWUgdGhlbWVzIChsaWtlIGRlYnV0Pz8pIGhhdmUgY3NzIHJlc2V0c1xuICAvLyB3aGljaCBzZXQgbGlzdC1zdHlsZSB0byBub25lLiBXZSByZXNldCBiYWNrIHRvIGluaGVyaXQgc28gdGhhdCBidWxsZXQgbGlzdCBidWxsZXRzIGFjdHVhbGx5IHNob3cgdXBcbiAgdWwsXG4gIGxpIHtcbiAgICBsaXN0LXN0eWxlOiBpbmhlcml0O1xuICAgIC8vIFRoaXMgaXMgd2VpcmQsIGJ1dCBidWxsZXQgcG9pbnRzIGRvbid0IGhhdmUgcGFkZGluZyBieSBkZWZhdWx0IGluIFJURVxuICAgIC8vIHNpbmNlIHdlIHJlc2V0IHRoZWlyIHBhZGRpbmcgYWJvdmUsIHdoaWNoIG1lYW5zIHRoZXkgcmVuZGVyIGluY29ycmVjdGx5XG4gICAgLy8gdG8gdGhlIGxlZnQuIFNldCB0aGVtIHRvIGFuIGFyYml0cmFyeSB2YWx1ZSB0byBtYWtlIHRoZW0gbG9vayBnb29kICh1c2VcbiAgICAvLyBlbSB0byBzY2FsZSB3aXRoIHRoZSBmb250IHNpemUpXG4gICAgcGFkZGluZy1sZWZ0OiAxLjdlbTtcbiAgfVxuXG4gIGNvZGUge1xuICAgIGJhY2tncm91bmQtY29sb3I6IHJnYmEoIzYxNjE2MSwgMC4xKTtcbiAgICBjb2xvcjogIzYxNjE2MTtcbiAgfVxuXG4gIHByZSB7XG4gICAgYmFja2dyb3VuZDogIzBkMGQwZDtcbiAgICBjb2xvcjogI2ZmZjtcbiAgICBmb250LWZhbWlseTogXCJKZXRCcmFpbnNNb25vXCIsIG1vbm9zcGFjZTtcbiAgICBwYWRkaW5nOiAwLjc1cmVtIDFyZW07XG4gICAgYm9yZGVyLXJhZGl1czogMC41cmVtO1xuXG4gICAgY29kZSB7XG4gICAgICBjb2xvcjogaW5oZXJpdDtcbiAgICAgIHBhZGRpbmc6IDA7XG4gICAgICBiYWNrZ3JvdW5kOiBub25lO1xuICAgICAgZm9udC1zaXplOiAwLjhyZW07XG4gICAgfVxuICB9XG5cbiAgaW1nIHtcbiAgICBtYXgtd2lkdGg6IDEwMCU7XG4gICAgaGVpZ2h0OiBhdXRvO1xuICB9XG5cbiAgYmxvY2txdW90ZSB7XG4gICAgcGFkZGluZy1sZWZ0OiAxcmVtO1xuICAgIGJvcmRlci1sZWZ0OiAycHggc29saWQgcmdiYSgjMGQwZDBkLCAwLjEpO1xuICB9XG5cbiAgaHIge1xuICAgIGJvcmRlcjogbm9uZTtcbiAgICBib3JkZXItdG9wOiAycHggc29saWQgcmdiYSgjMGQwZDBkLCAwLjEpO1xuICAgIG1hcmdpbjogMnJlbSAwO1xuICB9XG59XG4iXX0= */</style><style id=\"alchemy-runtime-css\">\n    html,\n    body {\n      zoom: unset !important;\n    }\n\n    body {\n      overflow-y: visible !important;\n    }\n      \n     </style><div class=\"alchemy__element alchemy-reset overflow-clip\" style=\"--replo-library-e922e3a7-4a8e-4498-8076-ba24179a7c0d-styles-0c0ddff2-0cf2-49fe-9286-c0e56e24d535-attributes-color:linear-gradient(0deg, #F9D6E6FF 0%, #FBF0F5FF 45.54455445544554%, #FFCDFFFF 99.00990099009901%)\"><div data-rid=\"bea1f1b1-0834-4988-af8b-0a766a46d4eb\" class=\"r-7j4tqq\"><div data-rid=\"9721d159-58fc-4472-ba38-4c245085b98a\" class=\"r-j2sy39\"><div data-rid=\"c03ab775-a6d5-4683-9957-c14601a53cc4\" class=\"r-r27skf\"><div data-rid=\"2271bd9d-ff05-4c84-8423-d9c7dbb4a2fb\" class=\"r-ezfs0b\"><div data-rid=\"58d1a395-d6a5-4fa1-9325-0b509a3e98b7\" class=\"r-1bo4aav\"><picture data-rid=\"9247a029-6bef-4f90-8026-2e38c06217f3\" class=\"r-1s78z59\"><source srcSet=\"https://assets.replocdn.com/projects/07bd1984-3d87-4861-82a3-4f94a264d106/3c101d37-3fae-4792-97ae-36a821708b16?width=820\" media=\"(max-width: 640px)\"/><source srcSet=\"https://assets.replocdn.com/projects/07bd1984-3d87-4861-82a3-4f94a264d106/3c101d37-3fae-4792-97ae-36a821708b16?width=1024\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"https://assets.replocdn.com/projects/07bd1984-3d87-4861-82a3-4f94a264d106/3c101d37-3fae-4792-97ae-36a821708b16?width=1800\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"https://assets.replocdn.com/projects/07bd1984-3d87-4861-82a3-4f94a264d106/3c101d37-3fae-4792-97ae-36a821708b16\" class=\"r-lw7hi5\" loading=\"eager\"/></picture></div><div data-rid=\"02081aed-e906-482e-8fd8-d770b93db6db\" class=\"r-a6k0t4\"><div data-rid=\"487d18db-eaa2-4647-8859-ef27579d7e78\" class=\"r-hif9da alchemy-rte\"><span style=\"width:100%\"><p>SÉLECTION > Sensibilités</p></span></div><div data-rid=\"ca5f1e20-947b-4351-9f7a-8f0b175c92bc\" class=\"r-149zdz0 alchemy-rte\"><span style=\"width:100%\"><h4>Sensibilités</h4></span></div></div></div><div class=\"r-1qycgw5\" data-rid=\"1\"><div data-rid=\"5cfd7743-305e-4676-9f25-7e24e3cbcafe\" class=\"r-l6nzmn\"><div data-rid=\"eed1e599-bf12-4e99-ac49-1d67a047e996\" class=\"r-91w9n\"><div data-rid=\"7adcb3cd-fd4c-4e3d-9946-ff2c08ce200f\" class=\"r-4zqa5c\"><div data-rid=\"1787c519-7b4a-40a2-abd4-965381728b3a\" class=\"r-yytsoj alchemy-rte\"><span style=\"width:100%\"><p>La douceur comme base</p></span></div><div data-rid=\"d6385b83-18bf-49c6-bee5-819ed7590d4a\" class=\"r-1m8udl0 alchemy-rte\"><span style=\"width:100%\"><p>Rougeurs, tiraillements, inconfort ? Tous nos soins sont formulés sans parfum, sans perturbateurs et testés sur peaux sensibles pour un apaisement immédiat.</p></span></div></div></div><div data-rid=\"eba9db1d-6942-47d2-a9b0-ca7461da72f2\" class=\"r-10qskm8\"><div class=\"r-7vb50c\" data-rid=\"1\"><div data-rid=\"b78bc5a1-6313-4b76-a713-def2a924ba10\" class=\"r-18oi2t1\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign reploOriginalProductR1qr2 = product %}<!-- -->{% capture productHandle %}granite-demaquillant{% endcapture %}<!-- -->{% assign product = all_products[productHandle] %}<!-- -->{% assign reploOriginalProductVariantR1qr2 = reploSelectedVariant %}<!-- -->{% assign reploSelectedVariant = blank %}<!-- -->{% assign reploOriginalSPGR1qr2 = reploSortedSellingPlans %}<!-- -->{% assign reploSortedSellingPlans = blank %}<!-- -->{% assign reploOriginalSSPR1qr2 = reploSelectedSellingPlan %}<!-- -->{% assign reploSelectedSellingPlan = blank %}<!-- -->{% assign reploOriginalSSPPriceR1qr2 = reploSelectedSellingPlanPrice %}<!-- -->{% assign reploSelectedSellingPlanPrice = blank %}<!-- -->{% assign reploOriginalComparePricePercentR1qr2 = reploCompareAtPriceDifferencePercentage %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = blank %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<!-- -->{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% capture reploVariantIdString %}null{% endcapture %}<!-- -->{% capture reploSellingPlanIdString %}null{% endcapture %}<!-- -->{% capture reploIdKey %}id{% endcapture %}<!-- -->{% capture reploPercentageKey %}percentage{% endcapture %}<!-- -->{% capture reploPriceKey %}price{% endcapture %}<!-- -->{% capture reploFixedAmountKey %}fixed_amount{% endcapture %}<!-- -->{% capture spKey %}selling_plan{% endcapture %}<!-- -->{%- liquid\n              assign reploVariantId = reploVariantIdString | times: 1\n              assign reploSelectedVariant = product.variants | where: reploIdKey, reploVariantId | first\n              if reploSelectedVariant == blank\n                assign reploSelectedVariant = product.selected_or_first_available_variant\n              endif\n              assign reploSelectedSellingPlanPrice = reploSelectedVariant.price\n              if product.selling_plan_groups[0]\n                assign reploAllSellingPlans = reploSelectedVariant.selling_plan_allocations | map: spKey\n                assign reploSortedSellingPlans = reploAllSellingPlans | sort: reploIdKey\n                if true\n                  assign reploSellingPlanId = reploSellingPlanIdString | times: 1\n                  assign reploSelectedSellingPlan = reploSortedSellingPlans | where: reploIdKey, reploSellingPlanId | first\n                  if reploSelectedSellingPlan.price_adjustments[0]\n                    assign adjustment = reploSelectedSellingPlan.price_adjustments[0]\n                    case adjustment.value_type\n                      when reploPercentageKey\n                        assign amountOff = 100 | minus: adjustment.value\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | times: amountOff | divided_by: 100\n                      when reploFixedAmountKey\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | minus: adjustment.value\n                      when reploPriceKey\n                        assign reploSelectedSellingPlanPrice = adjustment.value\n                    endcase\n                  endif\n                endif\n              endif\n            -%}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = 0 %}<!-- -->{% if reploSelectedVariant.compare_at_price != blank %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploSelectedVariant.compare_at_price | minus: reploSelectedVariant.price | at_least: 0 | times: 100.0 | divided_by: reploSelectedVariant.compare_at_price | round %}<!-- -->{% endif %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<div data-rid=\"3e33de33-35fe-4377-9b2e-1d524583f211\" tabindex=\"0\" role=\"button\" class=\"r-3wqav1\" data-replo-product-container=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" data-replo-product-handle=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.handle}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"><product-form style=\"display:none\"><form id=\"product-form-{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" method=\"post\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" encType=\"multipart/form-data\" action=\"/cart/add\" data-type=\"add-to-cart-form\"><input type=\"hidden\" name=\"id\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{reploSelectedVariant.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/><input type=\"hidden\" name=\"quantity\" value=\"1\"/><input type=\"hidden\" name=\"selling_plan\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- if reploSelectedSellingPlan != blank -%}{{reploSelectedSellingPlan.id}}{%- endif -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/></form></product-form><div data-rid=\"fbbe34de-df28-4f44-9b7e-4ed4dc8236a5\" class=\"r-1mpddo7\"><picture data-rid=\"d3142973-6c0e-43a0-920e-29876fa7d278\" style=\"--replo-attributes-product-featured-image:{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-k1cg7v\"><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 820  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(max-width: 640px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1024  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1800  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-1q9wyug\" loading=\"lazy\"/></picture></div><div data-rid=\"957b0ef9-ea5d-4546-8313-c1a19abf2251\" class=\"r-1t9z0rt\"><div data-rid=\"22f41a95-057b-435c-a610-efd07877de2d\" class=\"r-1hv3zq0\"><div data-rid=\"1c1dd2f1-95fa-42f5-a096-a360409ed374\" class=\"r-b3etsn\"><div data-rid=\"1345cec2-2fc7-4b0d-9862-577da99e0b4a\" class=\"r-1tl33ne alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.title }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div></div><div data-rid=\"6e8bc39b-9c5f-46d9-9f94-acb4661c792a\" class=\"r-3ahe6n\"><div data-rid=\"e451734e-3106-4d93-b1a4-c915b55aabd8\" class=\"r-13zoknt\"><div data-rid=\"aef8c280-53e4-4f72-8a43-5ffa7e12b847\" class=\"r-tkc5vq\"><div data-rid=\"3f5a9e55-6e10-4cd6-bace-425ffa91b244\" class=\"r-1t3wmhi alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}ml{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div><div data-rid=\"eceb06ee-7dae-4be5-a498-bfc7ffc50ba5\" class=\"r-1eg4q9m\"><div data-rid=\"f6b9750d-6dcb-43d6-9f88-a98fa2cd27b2\" class=\"r-f0cd5i alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}made_in_france{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div></div><div data-rid=\"fb440d47-8823-40ec-a826-1d3768015813\" class=\"r-3lgm8x\"><div data-rid=\"a7652791-463d-4d29-822f-b4ec07848824\" class=\"r-1hp0s62\"><div data-rid=\"86c45cb5-197e-473e-972f-06d91d51c4b2\" class=\"r-14ja0os alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ reploSelectedSellingPlanPrice  | divided_by: 100.0 | round | times: 100.0 | money_without_trailing_zeros}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div><div data-rid=\"1b1b9ba2-c533-4afb-9a76-b8fe293a4368\" class=\"r-b1rhd6\"><div data-rid=\"0608cac0-cb36-4ec7-88ef-2c7d4beacc3d\" class=\"r-1xj1yl2\"><span style=\"display:contents\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-arrow-up-right\" style=\"fill: none;stroke: currentColor;width: var(--rsw, 100%);height: 100%\" role=\"presentation\"><line x1=\"7\" y1=\"17\" x2=\"17\" y2=\"7\"></line><polyline points=\"7 7 17 7 17 17\"></polyline></svg></span></div></div></div></div></div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign product = reploOriginalProductR1qr2 %}<!-- -->{% assign reploSelectedVariant = reploOriginalProductVariantR1qr2 %}<!-- -->{% assign reploSortedSellingPlans = reploOriginalSPGR1qr2 %}<!-- -->{% assign reploSelectedSellingPlan = reploOriginalSSPR1qr2 %}<!-- -->{% assign reploSelectedSellingPlanPrice = reploOriginalSSPPriceR1qr2 %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploOriginalComparePricePercentR1qr2 %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign reploOriginalProductR2qr2 = product %}<!-- -->{% capture productHandle %}mousse-nettoyante{% endcapture %}<!-- -->{% assign product = all_products[productHandle] %}<!-- -->{% assign reploOriginalProductVariantR2qr2 = reploSelectedVariant %}<!-- -->{% assign reploSelectedVariant = blank %}<!-- -->{% assign reploOriginalSPGR2qr2 = reploSortedSellingPlans %}<!-- -->{% assign reploSortedSellingPlans = blank %}<!-- -->{% assign reploOriginalSSPR2qr2 = reploSelectedSellingPlan %}<!-- -->{% assign reploSelectedSellingPlan = blank %}<!-- -->{% assign reploOriginalSSPPriceR2qr2 = reploSelectedSellingPlanPrice %}<!-- -->{% assign reploSelectedSellingPlanPrice = blank %}<!-- -->{% assign reploOriginalComparePricePercentR2qr2 = reploCompareAtPriceDifferencePercentage %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = blank %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<!-- -->{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% capture reploVariantIdString %}null{% endcapture %}<!-- -->{% capture reploSellingPlanIdString %}null{% endcapture %}<!-- -->{% capture reploIdKey %}id{% endcapture %}<!-- -->{% capture reploPercentageKey %}percentage{% endcapture %}<!-- -->{% capture reploPriceKey %}price{% endcapture %}<!-- -->{% capture reploFixedAmountKey %}fixed_amount{% endcapture %}<!-- -->{% capture spKey %}selling_plan{% endcapture %}<!-- -->{%- liquid\n              assign reploVariantId = reploVariantIdString | times: 1\n              assign reploSelectedVariant = product.variants | where: reploIdKey, reploVariantId | first\n              if reploSelectedVariant == blank\n                assign reploSelectedVariant = product.selected_or_first_available_variant\n              endif\n              assign reploSelectedSellingPlanPrice = reploSelectedVariant.price\n              if product.selling_plan_groups[0]\n                assign reploAllSellingPlans = reploSelectedVariant.selling_plan_allocations | map: spKey\n                assign reploSortedSellingPlans = reploAllSellingPlans | sort: reploIdKey\n                if true\n                  assign reploSellingPlanId = reploSellingPlanIdString | times: 1\n                  assign reploSelectedSellingPlan = reploSortedSellingPlans | where: reploIdKey, reploSellingPlanId | first\n                  if reploSelectedSellingPlan.price_adjustments[0]\n                    assign adjustment = reploSelectedSellingPlan.price_adjustments[0]\n                    case adjustment.value_type\n                      when reploPercentageKey\n                        assign amountOff = 100 | minus: adjustment.value\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | times: amountOff | divided_by: 100\n                      when reploFixedAmountKey\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | minus: adjustment.value\n                      when reploPriceKey\n                        assign reploSelectedSellingPlanPrice = adjustment.value\n                    endcase\n                  endif\n                endif\n              endif\n            -%}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = 0 %}<!-- -->{% if reploSelectedVariant.compare_at_price != blank %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploSelectedVariant.compare_at_price | minus: reploSelectedVariant.price | at_least: 0 | times: 100.0 | divided_by: reploSelectedVariant.compare_at_price | round %}<!-- -->{% endif %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<div data-rid=\"3e33de33-35fe-4377-9b2e-1d524583f211\" tabindex=\"0\" role=\"button\" class=\"r-3wqav1\" data-replo-product-container=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" data-replo-product-handle=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.handle}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"><product-form style=\"display:none\"><form id=\"product-form-{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" method=\"post\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" encType=\"multipart/form-data\" action=\"/cart/add\" data-type=\"add-to-cart-form\"><input type=\"hidden\" name=\"id\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{reploSelectedVariant.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/><input type=\"hidden\" name=\"quantity\" value=\"1\"/><input type=\"hidden\" name=\"selling_plan\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- if reploSelectedSellingPlan != blank -%}{{reploSelectedSellingPlan.id}}{%- endif -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/></form></product-form><div data-rid=\"fbbe34de-df28-4f44-9b7e-4ed4dc8236a5\" class=\"r-1mpddo7\"><picture data-rid=\"d3142973-6c0e-43a0-920e-29876fa7d278\" style=\"--replo-attributes-product-featured-image:{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-k1cg7v\"><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 820  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(max-width: 640px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1024  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1800  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-1q9wyug\" loading=\"lazy\"/></picture></div><div data-rid=\"957b0ef9-ea5d-4546-8313-c1a19abf2251\" class=\"r-1t9z0rt\"><div data-rid=\"22f41a95-057b-435c-a610-efd07877de2d\" class=\"r-1hv3zq0\"><div data-rid=\"1c1dd2f1-95fa-42f5-a096-a360409ed374\" class=\"r-b3etsn\"><div data-rid=\"1345cec2-2fc7-4b0d-9862-577da99e0b4a\" class=\"r-1tl33ne alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.title }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div></div><div data-rid=\"6e8bc39b-9c5f-46d9-9f94-acb4661c792a\" class=\"r-3ahe6n\"><div data-rid=\"e451734e-3106-4d93-b1a4-c915b55aabd8\" class=\"r-13zoknt\"><div data-rid=\"aef8c280-53e4-4f72-8a43-5ffa7e12b847\" class=\"r-tkc5vq\"><div data-rid=\"3f5a9e55-6e10-4cd6-bace-425ffa91b244\" class=\"r-1t3wmhi alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}ml{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div><div data-rid=\"eceb06ee-7dae-4be5-a498-bfc7ffc50ba5\" class=\"r-1eg4q9m\"><div data-rid=\"f6b9750d-6dcb-43d6-9f88-a98fa2cd27b2\" class=\"r-f0cd5i alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}made_in_france{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div></div><div data-rid=\"fb440d47-8823-40ec-a826-1d3768015813\" class=\"r-3lgm8x\"><div data-rid=\"a7652791-463d-4d29-822f-b4ec07848824\" class=\"r-1hp0s62\"><div data-rid=\"86c45cb5-197e-473e-972f-06d91d51c4b2\" class=\"r-14ja0os alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ reploSelectedSellingPlanPrice  | divided_by: 100.0 | round | times: 100.0 | money_without_trailing_zeros}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div><div data-rid=\"1b1b9ba2-c533-4afb-9a76-b8fe293a4368\" class=\"r-b1rhd6\"><div data-rid=\"0608cac0-cb36-4ec7-88ef-2c7d4beacc3d\" class=\"r-1xj1yl2\"><span style=\"display:contents\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-arrow-up-right\" style=\"fill: none;stroke: currentColor;width: var(--rsw, 100%);height: 100%\" role=\"presentation\"><line x1=\"7\" y1=\"17\" x2=\"17\" y2=\"7\"></line><polyline points=\"7 7 17 7 17 17\"></polyline></svg></span></div></div></div></div></div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign product = reploOriginalProductR2qr2 %}<!-- -->{% assign reploSelectedVariant = reploOriginalProductVariantR2qr2 %}<!-- -->{% assign reploSortedSellingPlans = reploOriginalSPGR2qr2 %}<!-- -->{% assign reploSelectedSellingPlan = reploOriginalSSPR2qr2 %}<!-- -->{% assign reploSelectedSellingPlanPrice = reploOriginalSSPPriceR2qr2 %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploOriginalComparePricePercentR2qr2 %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign reploOriginalProductR3qr2 = product %}<!-- -->{% capture productHandle %}gel-creme-jour{% endcapture %}<!-- -->{% assign product = all_products[productHandle] %}<!-- -->{% assign reploOriginalProductVariantR3qr2 = reploSelectedVariant %}<!-- -->{% assign reploSelectedVariant = blank %}<!-- -->{% assign reploOriginalSPGR3qr2 = reploSortedSellingPlans %}<!-- -->{% assign reploSortedSellingPlans = blank %}<!-- -->{% assign reploOriginalSSPR3qr2 = reploSelectedSellingPlan %}<!-- -->{% assign reploSelectedSellingPlan = blank %}<!-- -->{% assign reploOriginalSSPPriceR3qr2 = reploSelectedSellingPlanPrice %}<!-- -->{% assign reploSelectedSellingPlanPrice = blank %}<!-- -->{% assign reploOriginalComparePricePercentR3qr2 = reploCompareAtPriceDifferencePercentage %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = blank %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<!-- -->{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% capture reploVariantIdString %}null{% endcapture %}<!-- -->{% capture reploSellingPlanIdString %}null{% endcapture %}<!-- -->{% capture reploIdKey %}id{% endcapture %}<!-- -->{% capture reploPercentageKey %}percentage{% endcapture %}<!-- -->{% capture reploPriceKey %}price{% endcapture %}<!-- -->{% capture reploFixedAmountKey %}fixed_amount{% endcapture %}<!-- -->{% capture spKey %}selling_plan{% endcapture %}<!-- -->{%- liquid\n              assign reploVariantId = reploVariantIdString | times: 1\n              assign reploSelectedVariant = product.variants | where: reploIdKey, reploVariantId | first\n              if reploSelectedVariant == blank\n                assign reploSelectedVariant = product.selected_or_first_available_variant\n              endif\n              assign reploSelectedSellingPlanPrice = reploSelectedVariant.price\n              if product.selling_plan_groups[0]\n                assign reploAllSellingPlans = reploSelectedVariant.selling_plan_allocations | map: spKey\n                assign reploSortedSellingPlans = reploAllSellingPlans | sort: reploIdKey\n                if true\n                  assign reploSellingPlanId = reploSellingPlanIdString | times: 1\n                  assign reploSelectedSellingPlan = reploSortedSellingPlans | where: reploIdKey, reploSellingPlanId | first\n                  if reploSelectedSellingPlan.price_adjustments[0]\n                    assign adjustment = reploSelectedSellingPlan.price_adjustments[0]\n                    case adjustment.value_type\n                      when reploPercentageKey\n                        assign amountOff = 100 | minus: adjustment.value\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | times: amountOff | divided_by: 100\n                      when reploFixedAmountKey\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | minus: adjustment.value\n                      when reploPriceKey\n                        assign reploSelectedSellingPlanPrice = adjustment.value\n                    endcase\n                  endif\n                endif\n              endif\n            -%}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = 0 %}<!-- -->{% if reploSelectedVariant.compare_at_price != blank %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploSelectedVariant.compare_at_price | minus: reploSelectedVariant.price | at_least: 0 | times: 100.0 | divided_by: reploSelectedVariant.compare_at_price | round %}<!-- -->{% endif %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<div data-rid=\"3e33de33-35fe-4377-9b2e-1d524583f211\" tabindex=\"0\" role=\"button\" class=\"r-3wqav1\" data-replo-product-container=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" data-replo-product-handle=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.handle}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"><product-form style=\"display:none\"><form id=\"product-form-{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" method=\"post\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" encType=\"multipart/form-data\" action=\"/cart/add\" data-type=\"add-to-cart-form\"><input type=\"hidden\" name=\"id\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{reploSelectedVariant.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/><input type=\"hidden\" name=\"quantity\" value=\"1\"/><input type=\"hidden\" name=\"selling_plan\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- if reploSelectedSellingPlan != blank -%}{{reploSelectedSellingPlan.id}}{%- endif -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/></form></product-form><div data-rid=\"fbbe34de-df28-4f44-9b7e-4ed4dc8236a5\" class=\"r-1mpddo7\"><picture data-rid=\"d3142973-6c0e-43a0-920e-29876fa7d278\" style=\"--replo-attributes-product-featured-image:{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-k1cg7v\"><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 820  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(max-width: 640px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1024  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1800  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-1q9wyug\" loading=\"lazy\"/></picture></div><div data-rid=\"957b0ef9-ea5d-4546-8313-c1a19abf2251\" class=\"r-1t9z0rt\"><div data-rid=\"22f41a95-057b-435c-a610-efd07877de2d\" class=\"r-1hv3zq0\"><div data-rid=\"1c1dd2f1-95fa-42f5-a096-a360409ed374\" class=\"r-b3etsn\"><div data-rid=\"1345cec2-2fc7-4b0d-9862-577da99e0b4a\" class=\"r-1tl33ne alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.title }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div></div><div data-rid=\"6e8bc39b-9c5f-46d9-9f94-acb4661c792a\" class=\"r-3ahe6n\"><div data-rid=\"e451734e-3106-4d93-b1a4-c915b55aabd8\" class=\"r-13zoknt\"><div data-rid=\"aef8c280-53e4-4f72-8a43-5ffa7e12b847\" class=\"r-tkc5vq\"><div data-rid=\"3f5a9e55-6e10-4cd6-bace-425ffa91b244\" class=\"r-1t3wmhi alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}ml{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div><div data-rid=\"eceb06ee-7dae-4be5-a498-bfc7ffc50ba5\" class=\"r-1eg4q9m\"><div data-rid=\"f6b9750d-6dcb-43d6-9f88-a98fa2cd27b2\" class=\"r-f0cd5i alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}made_in_france{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div></div><div data-rid=\"fb440d47-8823-40ec-a826-1d3768015813\" class=\"r-3lgm8x\"><div data-rid=\"a7652791-463d-4d29-822f-b4ec07848824\" class=\"r-1hp0s62\"><div data-rid=\"86c45cb5-197e-473e-972f-06d91d51c4b2\" class=\"r-14ja0os alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ reploSelectedSellingPlanPrice  | divided_by: 100.0 | round | times: 100.0 | money_without_trailing_zeros}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div><div data-rid=\"1b1b9ba2-c533-4afb-9a76-b8fe293a4368\" class=\"r-b1rhd6\"><div data-rid=\"0608cac0-cb36-4ec7-88ef-2c7d4beacc3d\" class=\"r-1xj1yl2\"><span style=\"display:contents\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-arrow-up-right\" style=\"fill: none;stroke: currentColor;width: var(--rsw, 100%);height: 100%\" role=\"presentation\"><line x1=\"7\" y1=\"17\" x2=\"17\" y2=\"7\"></line><polyline points=\"7 7 17 7 17 17\"></polyline></svg></span></div></div></div></div></div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign product = reploOriginalProductR3qr2 %}<!-- -->{% assign reploSelectedVariant = reploOriginalProductVariantR3qr2 %}<!-- -->{% assign reploSortedSellingPlans = reploOriginalSPGR3qr2 %}<!-- -->{% assign reploSelectedSellingPlan = reploOriginalSSPR3qr2 %}<!-- -->{% assign reploSelectedSellingPlanPrice = reploOriginalSSPPriceR3qr2 %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploOriginalComparePricePercentR3qr2 %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign reploOriginalProductR4qr2 = product %}<!-- -->{% capture productHandle %}gel-creme-nuit{% endcapture %}<!-- -->{% assign product = all_products[productHandle] %}<!-- -->{% assign reploOriginalProductVariantR4qr2 = reploSelectedVariant %}<!-- -->{% assign reploSelectedVariant = blank %}<!-- -->{% assign reploOriginalSPGR4qr2 = reploSortedSellingPlans %}<!-- -->{% assign reploSortedSellingPlans = blank %}<!-- -->{% assign reploOriginalSSPR4qr2 = reploSelectedSellingPlan %}<!-- -->{% assign reploSelectedSellingPlan = blank %}<!-- -->{% assign reploOriginalSSPPriceR4qr2 = reploSelectedSellingPlanPrice %}<!-- -->{% assign reploSelectedSellingPlanPrice = blank %}<!-- -->{% assign reploOriginalComparePricePercentR4qr2 = reploCompareAtPriceDifferencePercentage %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = blank %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<!-- -->{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% capture reploVariantIdString %}null{% endcapture %}<!-- -->{% capture reploSellingPlanIdString %}null{% endcapture %}<!-- -->{% capture reploIdKey %}id{% endcapture %}<!-- -->{% capture reploPercentageKey %}percentage{% endcapture %}<!-- -->{% capture reploPriceKey %}price{% endcapture %}<!-- -->{% capture reploFixedAmountKey %}fixed_amount{% endcapture %}<!-- -->{% capture spKey %}selling_plan{% endcapture %}<!-- -->{%- liquid\n              assign reploVariantId = reploVariantIdString | times: 1\n              assign reploSelectedVariant = product.variants | where: reploIdKey, reploVariantId | first\n              if reploSelectedVariant == blank\n                assign reploSelectedVariant = product.selected_or_first_available_variant\n              endif\n              assign reploSelectedSellingPlanPrice = reploSelectedVariant.price\n              if product.selling_plan_groups[0]\n                assign reploAllSellingPlans = reploSelectedVariant.selling_plan_allocations | map: spKey\n                assign reploSortedSellingPlans = reploAllSellingPlans | sort: reploIdKey\n                if true\n                  assign reploSellingPlanId = reploSellingPlanIdString | times: 1\n                  assign reploSelectedSellingPlan = reploSortedSellingPlans | where: reploIdKey, reploSellingPlanId | first\n                  if reploSelectedSellingPlan.price_adjustments[0]\n                    assign adjustment = reploSelectedSellingPlan.price_adjustments[0]\n                    case adjustment.value_type\n                      when reploPercentageKey\n                        assign amountOff = 100 | minus: adjustment.value\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | times: amountOff | divided_by: 100\n                      when reploFixedAmountKey\n                        assign reploSelectedSellingPlanPrice = reploSelectedSellingPlanPrice | minus: adjustment.value\n                      when reploPriceKey\n                        assign reploSelectedSellingPlanPrice = adjustment.value\n                    endcase\n                  endif\n                endif\n              endif\n            -%}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = 0 %}<!-- -->{% if reploSelectedVariant.compare_at_price != blank %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploSelectedVariant.compare_at_price | minus: reploSelectedVariant.price | at_least: 0 | times: 100.0 | divided_by: reploSelectedVariant.compare_at_price | round %}<!-- -->{% endif %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}<div data-rid=\"3e33de33-35fe-4377-9b2e-1d524583f211\" tabindex=\"0\" role=\"button\" class=\"r-3wqav1\" data-replo-product-container=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" data-replo-product-handle=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.handle}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"><product-form style=\"display:none\"><form id=\"product-form-{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" method=\"post\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" encType=\"multipart/form-data\" action=\"/cart/add\" data-type=\"add-to-cart-form\"><input type=\"hidden\" name=\"id\" data-productid=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{product.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{reploSelectedVariant.id}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/><input type=\"hidden\" name=\"quantity\" value=\"1\"/><input type=\"hidden\" name=\"selling_plan\" value=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- if reploSelectedSellingPlan != blank -%}{{reploSelectedSellingPlan.id}}{%- endif -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\"/></form></product-form><div data-rid=\"fbbe34de-df28-4f44-9b7e-4ed4dc8236a5\" class=\"r-1mpddo7\"><picture data-rid=\"d3142973-6c0e-43a0-920e-29876fa7d278\" style=\"--replo-attributes-product-featured-image:{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-k1cg7v\"><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 820  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(max-width: 640px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1024  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 641px) and (max-width: 1024px)\"/><source srcSet=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url: width: 1800  }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" media=\"(min-width: 1025px) and (max-width: 2400px)\"/><img src=\"{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.featured_image | image_url }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\" class=\"r-1q9wyug\" loading=\"lazy\"/></picture></div><div data-rid=\"957b0ef9-ea5d-4546-8313-c1a19abf2251\" class=\"r-1t9z0rt\"><div data-rid=\"22f41a95-057b-435c-a610-efd07877de2d\" class=\"r-1hv3zq0\"><div data-rid=\"1c1dd2f1-95fa-42f5-a096-a360409ed374\" class=\"r-b3etsn\"><div data-rid=\"1345cec2-2fc7-4b0d-9862-577da99e0b4a\" class=\"r-1tl33ne alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ product.title }}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div></div><div data-rid=\"6e8bc39b-9c5f-46d9-9f94-acb4661c792a\" class=\"r-3ahe6n\"><div data-rid=\"e451734e-3106-4d93-b1a4-c915b55aabd8\" class=\"r-13zoknt\"><div data-rid=\"aef8c280-53e4-4f72-8a43-5ffa7e12b847\" class=\"r-tkc5vq\"><div data-rid=\"3f5a9e55-6e10-4cd6-bace-425ffa91b244\" class=\"r-1t3wmhi alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}ml{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div><div data-rid=\"eceb06ee-7dae-4be5-a498-bfc7ffc50ba5\" class=\"r-1eg4q9m\"><div data-rid=\"f6b9750d-6dcb-43d6-9f88-a98fa2cd27b2\" class=\"r-f0cd5i alchemy-rte\"><span style=\"width:100%\">{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture fileReference -%}file_reference{%- endcapture -%}\n      {%- capture multiLineTextField -%}multi_line_text_field{%- endcapture -%}\n      {%- capture richTextField -%}rich_text_field{%- endcapture -%}\n      {%- capture reploMetafieldNamespace -%}custom{%- endcapture -%}\n      {%- capture reploMetafieldKey -%}made_in_france{%- endcapture -%}\n      {%- capture htmlOpenTag -%}<{%- endcapture -%}\n      {%- capture htmlCloseTag -%}>{%- endcapture -%}\n      {%- liquid\n         assign reploMetafield = product.metafields[reploMetafieldNamespace][reploMetafieldKey]\n         if reploMetafield.type == fileReference\n          echo reploMetafield | file_url\n         elsif reploMetafield.type == multiLineTextField\n           if reploMetafield.value contains htmlOpenTag and reploMetafield.value contains htmlCloseTag\n            echo reploMetafield.value\n           else\n            echo reploMetafield.value | newline_to_br\n           endif\n         elsif reploMetafield.type == richTextField\n          echo reploMetafield | metafield_tag\n         else\n          echo reploMetafield.value\n         endif\n      -%}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</span></div></div></div><div data-rid=\"fb440d47-8823-40ec-a826-1d3768015813\" class=\"r-3lgm8x\"><div data-rid=\"a7652791-463d-4d29-822f-b4ec07848824\" class=\"r-1hp0s62\"><div data-rid=\"86c45cb5-197e-473e-972f-06d91d51c4b2\" class=\"r-14ja0os alchemy-rte\"><span style=\"width:100%\"><p>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{{ reploSelectedSellingPlanPrice  | divided_by: 100.0 | round | times: 100.0 | money_without_trailing_zeros}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</p></span></div></div><div data-rid=\"1b1b9ba2-c533-4afb-9a76-b8fe293a4368\" class=\"r-b1rhd6\"><div data-rid=\"0608cac0-cb36-4ec7-88ef-2c7d4beacc3d\" class=\"r-1xj1yl2\"><span style=\"display:contents\"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-arrow-up-right\" style=\"fill: none;stroke: currentColor;width: var(--rsw, 100%);height: 100%\" role=\"presentation\"><line x1=\"7\" y1=\"17\" x2=\"17\" y2=\"7\"></line><polyline points=\"7 7 17 7 17 17\"></polyline></svg></span></div></div></div></div></div>{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<!-- -->{% assign product = reploOriginalProductR4qr2 %}<!-- -->{% assign reploSelectedVariant = reploOriginalProductVariantR4qr2 %}<!-- -->{% assign reploSortedSellingPlans = reploOriginalSPGR4qr2 %}<!-- -->{% assign reploSelectedSellingPlan = reploOriginalSSPR4qr2 %}<!-- -->{% assign reploSelectedSellingPlanPrice = reploOriginalSSPPriceR4qr2 %}<!-- -->{% assign reploCompareAtPriceDifferencePercentage = reploOriginalComparePricePercentR4qr2 %}<!-- -->{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div></div></div></div></div></div></div></div></div></div><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Medium\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Medium\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Medium.woff?v=1749641057\") format(\"woff\");\n        }\n      </style><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Light\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Light\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Light.woff?v=1749641057\") format(\"woff\");\n        }\n      </style><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Regular\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Regular\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Regular.woff?v=1749641058\") format(\"woff\");\n        }\n      </style><style id=\"replo-fonts-ABCMonumentGroteskSemiMono-Bold\">\n        @font-face {\n          font-family: \"ABCMonumentGroteskSemiMono-Bold\";\n          src: url(\"https://cdn.shopify.com/s/files/1/0727/3427/7975/files/ABCMonumentGroteskSemiMono-Bold.woff?v=1749641058\") format(\"woff\");\n        }\n      </style></div>\n{%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}\n  <script type=\"application/json\" id=\"replo-deps-products\">\n    [{\"id\":\"10094474395991\",\"handle\": \"granite-demaquillant\",\"data\":{{ all_products['granite-demaquillant'] | json }}},{\"id\":\"10094475477335\",\"handle\": \"mousse-nettoyante\",\"data\":{{ all_products['mousse-nettoyante'] | json }}},{\"id\":\"10094478000471\",\"handle\": \"gel-creme-jour\",\"data\":{{ all_products['gel-creme-jour'] | json }}},{\"id\":\"10094478688599\",\"handle\": \"gel-creme-nuit\",\"data\":{{ all_products['gel-creme-nuit'] | json }}}]\n  </script>\n  {%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\n    <script type=\"application/json\" id=\"replo-deps-products-metafields\">\n      {%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}{%- capture replo_double_tick -%}\"{%- endcapture -%}{\"10094474395991\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['granite-demaquillant'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['granite-demaquillant'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}},\"10094475477335\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['mousse-nettoyante'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['mousse-nettoyante'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}},\"10094478000471\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-jour'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-jour'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}},\"10094478688599\":{\"custom\":{\"ml\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-nuit'].metafields['custom']['ml'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"},\"made_in_france\":{\"type\":\"single_line_text_field\",\"value\":\"{{- all_products['gel-creme-nuit'].metafields['custom']['made_in_france'].value | default: null | json | replace_first: replo_double_tick, '' | replace_last: replo_double_tick, '' -}}\"}}}}{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}\n    </script>\n  \n    <script type=\"application/json\" id=\"replo-deps-variant-metafields\">\n    {%- capture replo_double_tick -%}\"{%- endcapture -%}{}\n    </script>\n  {%- comment -%}replo-liquid-chunk-begin{%- endcomment -%}<script type=\"application/json\" id=\"replo-deps-shopify-store\">{ \"shop\": { \"moneyFormat\": {{ shop.money_format | json }}, \"moneyWithCurrencyFormat\": {{ shop.money_with_currency_format | json }} } }</script>{%- comment -%}replo-liquid-chunk-end{%- endcomment -%}</div>\n\n{% schema %}\n{\n  \"name\": \"[collection]sensibilité\",\n  \"presets\": [\n    {\n      \"name\": \"[collection]sensibilité\"\n    }\n  ],\n  \"settings\": [\n    {\n      \"type\": \"header\",\n      \"content\": \"Created in Replo\",\n      \"info\": \"This Section was created using [Replo](https://www.replo.app/). If you would like to make any changes to the structure or design of this Section, you can [edit it in Replo](https://dashboard.replo.app/editor/07bd1984-3d87-4861-82a3-4f94a264d106/0bcad7f9-4a39-4fc3-b06f-45951fdf9431).\"\n    }\n  ]\n}\n{% endschema %}\n    "
      }
    }
  ]
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
╭─ success ───────────────────────────────────────────────────────────────────────────╮
│                                                                                     │
│  Preview your theme (t)                                                             │
│    • http://127.0.0.1:9292                                                          │
│                                                                                     │
│  Next steps                                                                         │
│    • Share your theme preview (p)                                                   │
│      https://aloe-paris.myshopify.com/?preview_theme_id=184608981335                │
│    • Customize your theme at the theme editor (e)                                   │
│    • Preview your gift cards (g)                                                    │
│                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────╯

2025-07-22T10:50:22.398Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-22T10:50:22.398Z: Ensuring that the user is authenticated with the Admin API with the following scopes for the store aloe-paris.myshopify.com:
[]

2025-07-22T10:50:22.399Z: Getting session store...
2025-07-22T10:50:22.402Z: Validating existing session against the scopes:
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
  "adminApi": {
    "scopes": [],
    "storeFqdn": "aloe-paris.myshopify.com"
  }
}

2025-07-22T10:50:22.402Z: - Token validation -> It's expired: false
2025-07-22T10:50:23.570Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "ARTICLE"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:23.571Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "BLOG"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:23.571Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COLLECTION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:23.571Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COMPANY"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:23.571Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "COMPANY_LOCATION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:23.571Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "LOCATION"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:23.571Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "MARKET"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:23.571Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "ORDER"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:23.571Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PAGE"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:23.572Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PRODUCT"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:23.572Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "PRODUCTVARIANT"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:23.572Z: Sending "Admin" GraphQL request:
  query metafieldDefinitionsByOwnerType($ownerType: MetafieldOwnerType!) {
  metafieldDefinitions(ownerType: $ownerType, first: 250) {
    nodes {
      key
      name
      namespace
      description
      type {
        category
        name
        __typename
      }
      __typename
    }
    __typename
  }
}

With variables:
{
  "ownerType": "SHOP"
}

With request headers:
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: linux
 - Content-Type: application/json

to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json
2025-07-22T10:50:24.097Z: Request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json completed in 25504 ms
With response headers:

    
╭─ error ─────────────────────────────────────────────────────────────────────────────╮
│                                                                                     │
│  Failed to perform the initial theme synchronization.                               │
│                                                                                     │
│  request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json         │
│  failed, reason:                                                                    │
│                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────╯

2025-07-22T10:50:24.104Z: Failed to perform the initial theme synchronization.
FetchError: request to https://aloe-paris.myshopify.com/admin/api/2025-07/graphql.json failed, reason: 
    at ClientRequest.<anonymous> (file:///home/maxdesign/.nvm/versions/node/v20.19.2/lib/node_modules/@shopify/cli/dist/chunk-F7QK7DZ4.js:17594:18)
    at ClientRequest.emit (node:events:524:28)
    at ClientRequest.emit (node:domain:489:12)
    at emitErrorEvent (node:_http_client:101:11)
    at TLSSocket.socketErrorListener (node:_http_client:504:5)
    at TLSSocket.emit (node:events:524:28)
    at TLSSocket.emit (node:domain:489:12)
    at emitErrorNT (node:internal/streams/destroy:169:8)
    at emitErrorCloseNT (node:internal/streams/destroy:128:3)
    at processTicksAndRejections (node:internal/process/task_queues:82:21)

```
</details>



comment #17 by driespieters, 2025-07-22, 13:48:12
Same issue and not fixed in `3.82.1`. I always get a network error on first try of `shopify theme dev`. Second try it works after some delay.

` request to https://store.myshopify.com/admin/api/2025-07/graphql.json failed, reason: socket hang up    `

It's a very large theme (lots of templates, Replo, etc.). When running in verbose mode, I notice it takes a while to parse the Liquid files. I assume it takes too long and the network times out. Is it necessary to parse all files to run `theme dev`?

@karreiro I shared my verbose privately via Slack. Thanks!


comment #18 by graygilmore, 2025-07-22, 16:16:53
> I installed this build @shopify/cli@0.0.0-snapshot-20250718094441 but it shows as 3.82.0 when I lookup for shopify version. I was on 3.79.2 so it did update.

@MaxDesignFR if you install a snapshotted version it should return the snapshot version in when running `shopify version`:

```sh
➜  test-theme git:(main) npm i -g @shopify/cli@0.0.0-snapshot-20250718094441
➜  test-theme git:(main) shopify --version
@shopify/cli/0.0.0-snapshot-20250718094441 darwin-arm64 node-v22.15.1
```

The `Analytics event sent` object in the verbose logs may show an incorrect version, however.

comment #19 by sole-unique, 2025-07-23, 03:44:19
I have run the command pnpm i -g @shopify/cli@0.0.0-snapshot-20250717120134
But I ran the shopify theme dev and got the same error. The node version is v22.17.0, which should not have any impact. I have tried multiple VPNs and got the same error. I am really confused. Please take the time to check it.
<details>
    <summary>Verbose output</summary>
    ```
PS D:\test> shopify theme dev --store eh05ec-b5 --verbose
2025-07-23T03:30:01.245Z: Running command theme dev
2025-07-23T03:30:01.254Z: Running system process:
  · Command: D:\nodejs\node.exe C:\Users\selo.luo\AppData\Roaming\npm\node_modules\@shopify\cli\bin\run.js notifications list --ignore-errors
  · Working directory: D:/test

2025-07-23T03:30:01.263Z: Notifications to show: 0
2025-07-23T03:30:01.272Z: Ensuring that the user is authenticated with the Theme API with the following scopes:        
[]

2025-07-23T03:30:01.273Z: Ensuring that the user is authenticated with the Admin API with the following scopes for the store eh05ec-b5.myshopify.com:
[]

2025-07-23T03:30:01.273Z: Getting session store...
2025-07-23T03:30:01.274Z: Validating existing session against the scopes:
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
  "adminApi": {
    "scopes": [],
    "storeFqdn": "eh05ec-b5.myshopify.com"
  }
}

2025-07-23T03:30:01.275Z: - Token validation -> It's expired: false
2025-07-23T03:30:01.275Z: Getting development theme...
2025-07-23T03:30:01.279Z: Sending "Admin" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: win32
 - Content-Type: application/json

to https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json
2025-07-23T03:30:22.339Z: Retrying request to https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json due to network error FetchError: request to https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json failed, reason: connect ETIMEDOUT 23.227.38.74:443
2025-07-23T03:30:22.340Z: Request to https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json completed in 21060 ms
With response headers:

    
╭─ error ──────────────────────────────────────────────────────────────────────╮
│                                                                              │
│  Unknown error connecting to your store eh05ec-b5.myshopify.com: request to  │
│   https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json failed,    │
│  reason: connect ETIMEDOUT 23.227.38.74:443                                  │
│                                                                              │
│  To investigate the issue, examine this stack trace:                         │
│    at fetchApiVersions (Users/selo.luo/AppData/Roaming/npm/node_modules/@sh  │
│    opify/cli/dist/index.js:194224)                                           │
│    at processTicksAndRejections (node:internal/process/task_queues:105)      │
│    at async supportedApiVersions (Users/selo.luo/AppData/Roaming/npm/node_m  │
│    odules/@shopify/cli/dist/index.js:194208)                                 │
│    at async fetchLatestSupportedApiVersion (Users/selo.luo/AppData/Roaming/  │
│    npm/node_modules/@shopify/cli/dist/index.js:194204)                       │
│    at async adminRequestDoc (Users/selo.luo/AppData/Roaming/npm/node_module  │
│    s/@shopify/cli/dist/index.js:194184)                                      │
│    at async themeCreate (Users/selo.luo/AppData/Roaming/npm/node_modules/@s  │
│    hopify/cli/dist/index.js:194285)                                          │
│    at create (Users/selo.luo/AppData/Roaming/npm/node_modules/@shopify/cli/  │
│    dist/index.js:194715)                                                     │
│    at findOrCreate (Users/selo.luo/AppData/Roaming/npm/node_modules/@shopif  │
│    y/cli/dist/index.js:194703)                                               │
│    at run (Users/selo.luo/AppData/Roaming/npm/node_modules/@shopify/cli/dis  │
│    t/index.js:199061)                                                        │
│    at _run (Users/selo.luo/AppData/Roaming/npm/node_modules/@shopify/cli/di  │
│    st/chunk-3FBDJEGD.js:169541)                                              │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

2025-07-23T03:30:22.419Z: Running system process:
  · Command: npm prefix
  · Working directory: D:/test

2025-07-23T03:30:22.655Z: Obtaining the dependency manager in directory D:\test...
2025-07-23T03:30:33.986Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 11081 ms
With response headers:


2025-07-23T03:30:33.987Z: Failed to report usage analytics: request to https://monorail-edge.shopifysvc.com/v1/produce failed, reason: getaddrinfo ENOTFOUND monorail-edge.shopifysvc.com
2025-07-23T03:30:33.987Z: Failed to report usage analytics: request to https://monorail-edge.shopifysvc.com/v1/produce failed, reason: getaddrinfo ENOTFOUND monorail-edge.shopifysvc.com
2025-07-23T03:30:33.993Z: Reporting unhandled error to Bugsnag: Unknown error connecting to your store eh05ec-b5.myshopify.com: request to https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json failed, reason: connect ETIMEDOUT 23.227.38.74:443
2025-07-23T03:30:34.029Z: Running system process:
  · Command: npm prefix
  · Working directory: D:/test

2025-07-23T03:30:34.262Z: Obtaining the dependency manager in directory D:\test...
    ```
</details>
    
**I try this command ： npm install -g  @shopify/cli@0.0.0-snapshot-20250718094441**
<details>
    <summary>Verbose output</summary>
    ```
 shopify theme dev --store eh05ec-b5 --verbose
2025-07-23T03:54:47.968Z: Running command theme dev
2025-07-23T03:54:47.977Z: Running system process:
  · Command: D:\nodejs\node.exe C:\Users\selo.luo\AppData\Roaming\npm\node_modules\@shopify\cli\bin\run.js notifications list --ignore-errors
  · Working directory: D:/test

2025-07-23T03:54:47.986Z: Notifications to show: 0
2025-07-23T03:54:47.996Z: Ensuring that the user is authenticated with the Theme API with the following scopes:
[]

2025-07-23T03:54:47.996Z: Ensuring that the user is authenticated with the Admin API with the following scopes for the store eh05ec-b5.myshopify.com:
[]

2025-07-23T03:54:47.997Z: Getting session store...
2025-07-23T03:54:47.998Z: Validating existing session against the scopes:
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
  "adminApi": {
    "scopes": [],
    "storeFqdn": "eh05ec-b5.myshopify.com"
  }
}

2025-07-23T03:54:47.999Z: - Token validation -> It's expired: false
2025-07-23T03:54:47.999Z: Getting development theme...
2025-07-23T03:54:48.006Z: Sending "Admin" GraphQL request:
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
 - User-Agent: Shopify CLI; v=3.82.0
 - Keep-Alive: timeout=30
 - Sec-CH-UA-PLATFORM: win32
 - Content-Type: application/json

to https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json
2025-07-23T03:55:09.064Z: Retrying request to https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json due to network error FetchError: request to https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json failed, reason: connect ETIMEDOUT 23.227.38.74:443
2025-07-23T03:55:09.065Z: Request to https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json completed in 21058 ms
With response headers:


╭─ error ──────────────────────────────────────────────────────────────────────╮
│                                                                              │
│  Unknown error connecting to your store eh05ec-b5.myshopify.com: request to  │
│   https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json failed,    │
│  reason: connect ETIMEDOUT 23.227.38.74:443                                  │
│                                                                              │
│  To investigate the issue, examine this stack trace:                         │
│    at fetchApiVersions (Users/selo.luo/AppData/Roaming/npm/node_modules/@sh  │
│    opify/cli/dist/index.js:194224)                                           │
│    at processTicksAndRejections (node:internal/process/task_queues:105)      │
│    at async supportedApiVersions (Users/selo.luo/AppData/Roaming/npm/node_m  │
│    odules/@shopify/cli/dist/index.js:194208)                                 │
│    at async fetchLatestSupportedApiVersion (Users/selo.luo/AppData/Roaming/  │
│    npm/node_modules/@shopify/cli/dist/index.js:194204)                       │
│    at async adminRequestDoc (Users/selo.luo/AppData/Roaming/npm/node_module  │
│    s/@shopify/cli/dist/index.js:194184)                                      │
│    at async themeCreate (Users/selo.luo/AppData/Roaming/npm/node_modules/@s  │
│    hopify/cli/dist/index.js:194285)                                          │
│    at create (Users/selo.luo/AppData/Roaming/npm/node_modules/@shopify/cli/  │
│    dist/index.js:194715)                                                     │
│    at findOrCreate (Users/selo.luo/AppData/Roaming/npm/node_modules/@shopif  │
│    y/cli/dist/index.js:194703)                                               │
│    at run (Users/selo.luo/AppData/Roaming/npm/node_modules/@shopify/cli/dis  │
│    t/index.js:199069)                                                        │
│    at _run (Users/selo.luo/AppData/Roaming/npm/node_modules/@shopify/cli/di  │
│    st/chunk-3FBDJEGD.js:169541)                                              │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

2025-07-23T03:55:09.140Z: Running system process:
  · Command: npm prefix
  · Working directory: D:/test

2025-07-23T03:55:09.376Z: Obtaining the dependency manager in directory D:\test...
2025-07-23T03:55:10.590Z: Request to https://monorail-edge.shopifysvc.com/v1/produce completed in 964 ms
With response headers:
 - x-request-id: 313a56d2-c3c0-418d-bb3f-93a98e8cc8d7

2025-07-23T03:55:10.590Z: Analytics event sent: {
  "command": "theme dev",
  "time_start": 1753242887969,
  "time_end": 1753242909120,
  "total_time": 21151,
  "success": false,
  "cli_version": "3.82.0",
  "ruby_version": "",
  "node_version": "22.17.0",
  "is_employee": false,
  "uname": "windows amd64",
  "env_ci": false,
  "env_plugin_installed_any_custom": false,
  "env_plugin_installed_shopify": "[\"@shopify/cli\"]",
  "env_shell": "powershell",
  "env_device_id": "e2fb59fe7d7cc8cedabe385ee27f8e9d61e0033f",
  "env_cloud": "localhost",
  "env_package_manager": "unknown",
  "env_is_global": true,
  "env_auth_method": "device_auth",
  "env_is_wsl": false,
  "env_build_repository": "Shopify/cli",
  "cmd_app_warning_api_key_deprecation_displayed": false,
  "cmd_all_timing_network_ms": 21058,
  "cmd_all_timing_prompts_ms": 0,
  "cmd_all_launcher": "unknown",
  "cmd_all_topic": "theme",
  "cmd_all_plugin": "@shopify/theme",
  "cmd_all_force": false,
  "cmd_all_verbose": true,
  "cmd_all_path_override": true,
  "cmd_all_path_override_hash": "bd10a61a6f8f4e60568584dc0c59d3b015a1db51",
  "cmd_all_timing_active_ms": 92,
  "cmd_all_exit": "unexpected_error",
  "user_id": "77ae64f2-b9af-43b6-8c39-870726003a15",
  "request_ids": [],
  "args": "--store eh05ec-b5 --verbose",
  "error_message": "Unknown error connecting to your store eh05ec-b5.myshopify.com: request to https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json failed, reason: connect ETIMEDOUT 23.227.38.74:443",
  "env_plugin_installed_all": "[\"@shopify/cli\"]",
  "metadata": "{\"extraPublic\":{},\"extraSensitive\":{}}"
}
2025-07-23T03:55:10.598Z: Reporting unhandled error to Bugsnag: Unknown error connecting to your store eh05ec-b5.myshopify.com: request to https://eh05ec-b5.myshopify.com/admin/api/unstable/graphql.json failed, reason: connect ETIMEDOUT 23.227.38.74:443
2025-07-23T03:55:10.632Z: Running system process:
  · Command: npm prefix
  · Working directory: D:/test

2025-07-23T03:55:10.864Z: Obtaining the dependency manager in directory D:\test...
2025-07-23T03:55:21.972Z: Error reporting to Bugsnag: Error: getaddrinfo ENOTFOUND error-analytics-production.shopifysvc.com
    ```
</details>

comment #20 by Othmane-Menad, 2025-07-26, 22:44:47
I'm getting same error.

AggregateError [ETIMEDOUT]:
at internalConnectMultiple (node:net:1134:18)
at afterConnectMultiple (node:net:1715:7)

Operating System
Linux Mint 21.3

Shopify CLI version (shopify --version)
3.83.0

Shell
Bash

Node version (run node -v if you're not sure)
v22.17.1

comment #21 by He110te4m, 2025-07-29, 03:17:08
same here
```
$ shopify --version    
@shopify/cli/3.83.1 darwin-arm64 node-v20.19.2
```

comment #22 by graygilmore, 2025-07-29, 16:08:50
Hey folks! Please make sure you're using the snapshotted version that @karreiro provided above to let us know if that fixes the issue. 

```
pnpm i -g @shopify/cli@0.0.0-snapshot-20250718094441
```

You can double check the version by running: `shopify --version` and you should see the snapshot. If you don't see the snapshot version then you have multiple versions of `shopify` on your system and you'll need to rectify that before providing feedback.

comment #23 by Othmane-Menad, 2025-07-29, 16:17:16
@graygilmore  I did tried it

`shopify --version
@shopify/cli/0.0.0-snapshot-20250718094441 linux-x64 node-v22.17.1
`

`shopify theme dev 
💡 Version 3.83.0 available! Run npm install -g @shopify/cli@latest
[SHOPIFY_#6062_DEBUG] {
  node: 'v22.17.1',
  platform: 'linux',
  arch: 'x64',
  openssl: '3.0.16',
  env: {
    HTTP_PROXY: 'not set',
    HTTPS_PROXY: 'not set',
    NO_PROXY: 'not set',
    NODE_TLS_REJECT_UNAUTHORIZED: 'not set',
    NODE_OPTIONS: 'not set',
    NODE_EXTRA_CA_CERTS: 'not set'
  }
}

Error: getaddrinfo ENOTFOUND otlp-http-production-cli.shopifysvc.com
    at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)
`

comment #24 by He110te4m, 2025-07-30, 01:15:27
It look nothing change

```
$ shopify --version              
@shopify/cli/0.0.0-snapshot-20250718094441 darwin-arm64 node-v20.19.2
```

<details><summary>shopify hydrogen init ouput</summary>
<p>

$ shopify hydrogen init          
💡 Version 3.83.1 available! Run `npm install -g @shopify/cli@latest`
Reading the content of file at /Users/mine/.nvm/versions/node/v20.19.2/lib/node_modules/@shopify/cli/package.json (size: 5949 bytes)...
?  Connect to Shopify:
✔  Link your Shopify account

?  Select a shop to log in to:
✔  test-narwal-headless (test-narwal-headless.myshopify.com)

╭─ success ────────────────────────────────────────────────────────────────────╮
│                                                                              │
│  Shopify authentication complete                                             │
│                                                                              │
│  You are logged in to test-narwal-headless as example@mail.com        │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

╭─ error ──────────────────────────────────────────────────────────────────────╮
│                                                                              │
│  request to                                                                  │
│  https://test-narwal-headless.myshopify.com/admin/api/unstable/graphql.json  │
│   failed, reason: Client network socket disconnected before secure TLS       │
│  connection was established                                                  │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

AggregateError [ETIMEDOUT]: 
    at internalConnectMultiple (node:net:1122:18)
    at internalConnectMultiple (node:net:1190:5)
    at Timeout.internalConnectMultipleTimeout (node:net:1716:5)
    at listOnTimeout (node:internal/timers:583:11)
    at process.processTimers (node:internal/timers:519:7)

</p>
</details> 

<details><summary>shopify theme init --verbose output</summary>
<p>

$ shopify theme init --verbose
2025-07-30T01:13:55.856Z: Running command theme init
?  Name of the new theme:
✔  test-theme

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Cloning https://github.com/Shopify/skeleton-theme into
/Users/user/codes/shopify/test-theme ...
2025-07-30T01:13:59.249Z: Git-cloning repository https://github.com/Shopify/skeleton-theme into test-theme...
2025-07-30T01:13:59.252Z: Running system process:
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Cloning https://github.com/Shopify/skeleton-theme into
/Users/user/codes/shopify/test-theme ...
2025-07-30T01:14:01.250Z: Removing git remote origin from test-theme...
2025-07-30T01:14:01.251Z: Running system process:

?  Set up AI dev support?
✔  Skip

2025-07-30T01:14:03.632Z: Running system process:
  · Command: npm prefix
  · Working directory: /Users/user/codes/shopify

2025-07-30T01:14:03.748Z: Obtaining the dependency manager in directory /Users/user/codes/shopify...
2025-07-30T01:14:03.845Z: Getting session store...
2025-07-30T01:14:03.848Z: Getting session store...
AggregateError [ETIMEDOUT]: 
    at internalConnectMultiple (node:net:1122:18)
    at internalConnectMultiple (node:net:1190:5)
    at Timeout.internalConnectMultipleTimeout (node:net:1716:5)
    at listOnTimeout (node:internal/timers:583:11)
    at process.processTimers (node:internal/timers:519:7)

</p>
</details> 

comment #25 by philkendallsimba, 2025-08-06, 13:27:03
@graygilmore  I was having the same issues, and have just tried the snaphot
@shopify/cli/0.0.0-snapshot-20250718094441 wsl-x64 node-v22.15.0

and shopify theme dev is now working correctly for me

comment #26 by vinay-vissh, 2025-08-12, 06:05:25
Just wanted to add that `shopify theme dev --legacy` using version `3.68.1`  have been and still works on my end.
While the latest version _(`@shopify/cli/3.83.3 linux-x64 node-v22.18.0`)_ and above mentioned snapshot version _(`@shopify/cli/0.0.0-snapshot-20250718094441 linux-x64 node-v22.18.0`)_ throws exact same error _(`...api/2025-07/graphql.json failed, reason:`)_ no matter how many times I try.

Long live `legacy` flag though it got deprecated.

comment #27 by EvilGenius13, 2025-08-12, 14:27:44
> Just wanted to add that `shopify theme dev --legacy` using version `3.68.1` have been and still works on my end. While the latest version _(`@shopify/cli/3.83.3 linux-x64 node-v22.18.0`)_ and above mentioned snapshot version _(`@shopify/cli/0.0.0-snapshot-20250718094441 linux-x64 node-v22.18.0`)_ throws exact same error _(`...api/2025-07/graphql.json failed, reason:`)_ no matter how many times I try.
> 
> Long live `legacy` flag though it got deprecated.

I'd like to ask a few questions about this.

- What command(s) are you running when you hit that error
- If you are running commands like push, how long does it take you to complete the upload?
- Is there anything you that is easily noticeable (aside from the consistent errors) when running in the old version vs new? (for example in the dev command, does it take 15 seconds to completely boot up in legacy but fails within the first few seconds when you try a newer version?
- Is there anything that stands out in terms of the themes you are running (large assets, high amount of files, etc)

Thanks!

comment #28 by EvilGenius13, 2025-08-12, 19:03:58
Hello everyone. We have a new build to test.

To install:
```
pnpm i -g @shopify/cli@0.0.0-snapshot-20250812183036
```
Please make sure you run a version check to confirm you are on the same version
```
shopify --version
```
<img width="565" height="55" alt="Image" src="https://github.com/user-attachments/assets/508d6ba5-badc-49b8-a80e-6fa864ecf4a8" />

If you don't see that snapshot as the version you likely have another version installed via pnpm/homebrew/npm:
- Run `which shopify` 
   - For PNPM: `pnpm rm -g @shopify/cli`
   - For NPM: `npm uninstall -g @shopify/cli`
   - For Homebrew: `brew uninstall shopify-cli`

This is targeting socket disconnects, and the errors where we see `failed, reason:`. If you are able to test it out, it would be very valuable to us.

If this fixes your issue:
- Please let us know

If this doesn't fix your issue:
- Please let us know and also tell us if you are running behind a Proxy or VPN.

comment #29 by Othmane-Menad, 2025-08-12, 19:14:45
@EvilGenius13 
not running any Proxy or VPN

<img width="731" height="554" alt="Image" src="https://github.com/user-attachments/assets/1a75a993-79fd-4e20-9e61-96ce5fb6c522" />

comment #30 by EvilGenius13, 2025-08-12, 19:23:45
> [@EvilGenius13](https://github.com/EvilGenius13) not running any Proxy or VPN
> 
> <img alt="Image" width="731" height="554" src="https://private-user-images.githubusercontent.com/36086187/477231080-1a75a993-79fd-4e20-9e61-96ce5fb6c522.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTUwMjY4NTUsIm5iZiI6MTc1NTAyNjU1NSwicGF0aCI6Ii8zNjA4NjE4Ny80NzcyMzEwODAtMWE3NWE5OTMtNzlmZC00ZTIwLTllNjEtOTZjZTVmYjZjNTIyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA4MTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwODEyVDE5MjIzNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTc1NzMzYTc0ZDJjNzQ5ZjY4OTExODRkMjRiYjUxZWVkYTBkY2QwZWY2N2M3OGM5YmFmNmY0OTJmNzg2ODU5OTkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.3y54FECoNfjKLT43XCgEud1l3Xz-2KGXz7orGOd-kjY">

Could you run that again with the verbose flag? `shopify theme dev --verbose`. I would like to see if anything else shows up in the logs`

comment #31 by EvilGenius13, 2025-08-12, 19:53:51
@Othmane-Menad on top of the verbose logs, could you also try running `SHOPIFY_CLI_NO_ANALYTICS=1 shopify theme dev` and tell me if the app still crashes. Both logs and that test would be helpful for your case.

comment #32 by Othmane-Menad, 2025-08-12, 20:33:56
@EvilGenius13 
It did work now, no crashes
Thanks

<img width="1110" height="388" alt="Image" src="https://github.com/user-attachments/assets/2cb2c67f-8e4c-49a8-87e7-a5a1929b7aea" />

comment #33 by vinay-vissh, 2025-08-13, 06:25:29
@EvilGenius13 

I should mention that I do not use any VPN or proxy.

1. **What command(s) are you running when you hit that error**
In my workflow, I use `shopify theme pull -store mystore.myshopify.com` and `shopify theme dev --legacy -store mystore.myshopify.com`.
I do not require `shopify theme push`.
Never faced any issue with `theme pull` in any version.
Its `theme dev` which has been resulting in errors since `--legacy` flag was deprecated after `v3.68.1`.

2. **If you are running commands like push, how long does it take you to complete the upload?**
Not using `theme push`.

3. **Is there anything you that is easily noticeable (aside from the consistent errors) when running in the old version vs new? (for example in the dev command, does it take 15 seconds to completely boot up in legacy but fails within the first few seconds when you try a newer version?**
Both versions appear to take same amount of time but the newer versions end up throwing error and terminating.
Like one of the network requests failed _(say, network packet loss at right moment)_ and the command did not retry few times with delay and just gave up.

4. **Is there anything that stands out in terms of the themes you are running (large assets, high amount of files, etc)**
The themes on which I work have around `800` files with a combined size of `56.6 MB`. Max size among files is `3.5 MB`.

Thanks!

<br/>
<br/>

Just now, I uninstalled the cli and got latest version _(`npm install -g @shopify/cli@latest`)_ _(`@shopify/cli/3.83.3 linux-x64 node-v22.18.0`)_.
I logged out from cli _(`shopify auth logout`)_ and ran `shopify theme dev --store mystore.myshopify.com` five times.
`1st`, `4th` and `5th` runs threw error while `2nd` and `3rd` ran successfully.

`1st` run
```s
To run this command, log in to Shopify.
User verification code: AAAA-BBBB
👉 Press any key to open the login page on your browser
Opened link to start the auth process: https://accounts.shopify.com/activate-with-code?device_code%5Buser_code%5D=AAAA-BBBB
✔ Logged in.
╭─ success ────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                          │
│  Preview your theme (t)                                                                                                  │
│    • http://127.0.0.1:9292                                                                                               │
│                                                                                                                          │
│  Next steps                                                                                                              │
│    • Share your theme preview (p) https://mystore.myshopify.com/?preview_theme_id=180395475261                 │
│    • Customize your theme at the theme editor (e)                                                                        │
│    • Preview your gift cards (g)                                                                                         │
│                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

AggregateError [ETIMEDOUT]: 
    at internalConnectMultiple (node:net:1134:18)
    at internalConnectMultiple (node:net:1210:5)
    at Timeout.internalConnectMultipleTimeout (node:net:1742:5)
    at listOnTimeout (node:internal/timers:590:11)
    at process.processTimers (node:internal/timers:523:7)
```

`4th` and `5th` run
```s
╭─ success ────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                          │
│  Preview your theme (t)                                                                                                  │
│    • http://127.0.0.1:9292                                                                                               │
│                                                                                                                          │
│  Next steps                                                                                                              │
│    • Share your theme preview (p) https://mystore.myshopify.com/?preview_theme_id=180395475261                 │
│    • Customize your theme at the theme editor (e)                                                                        │
│    • Preview your gift cards (g)                                                                                         │
│                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭─ error ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                          │
│  Failed to perform the initial theme synchronization.                                                                    │
│                                                                                                                          │
│  request to https://green-soul-online.myshopify.com/admin/api/2025-07/graphql.json failed, reason:                       │
│                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

So, I should change from `new versions do not work on my end` to `new versions work sometimes`.
Though `--legacy` _(`v3.68.1`)_ works all the time!

comment #34 by vinay-vissh, 2025-08-13, 06:43:34
@EvilGenius13 

Oh wow.
Just ran `SHOPIFY_CLI_NO_ANALYTICS=1 shopify theme dev --store mystore.myshopify.com` many times using version `@shopify/cli/0.0.0-snapshot-20250812183036 linux-x64 node-v22.18.0` and no errors - All successful runs!

Tried with latest version again but I guess `SHOPIFY_CLI_NO_ANALYTICS=1` variable is only processed by this snaphsot version.

Thanks!
