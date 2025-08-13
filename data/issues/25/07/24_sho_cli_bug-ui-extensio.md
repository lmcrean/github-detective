issue title: [Bug]: UI Extension Metafield Config has Higher Minimum Length For Key String Than Admin API or Admin Web UI- Blocks Extension Access To Metafield
labels: Type: Bug
comment count: 1
hyperlink: https://github.com/shopify/cli/issues/6159
status: open
date opened: 2025-07-24
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Extension

### Expected behavior

Able to reference all app metafield definitions in extension.toml file according to the same spec listed for the Admin API:

> key String! non-null
> Must be 2-64 characters long and only contain alphanumeric, hyphen, and underscore characters.

[https://shopify.dev/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key](url)

### Actual behavior

Requesting the custom id metafield:
`  [[extensions.metafields]]
  namespace = "custom"
  key = "id"
`
per [https://shopify.dev/docs/apps/build/custom-data/metafields/working-with-custom-ids](url)

results in this error when deploying:
`╭─ error 
│  Version couldn't be created.
│
│  Each entry needs a 'key' value between 3 and 64 characters.
│
╰─────
`

### Verbose output

<details>
  <summary>Verbose output</summary>

  ```
  Paste the output here!
  ```

</details>

### Reproduction steps

1. Create custom ID metafield definition with key = "id"
2. Request same custom.id metafield in shopify.extension.toml
3. Observe error message

### Operating System

Windows 11 - Ubuntu 24.04 LTS in WSL2

### Shopify CLI version (`shopify --version`)

3.83.0

### Shell

Bash

### Node version (run `node -v` if you're not sure)

v20.0.17

### What language and version are you using in your application?

_No response_

===

comment #1 by greatestape, 2025-08-12, 18:21:32
So we tracked down the issue to here: https://github.com/shop/world/blob/e2fe401e4c0563c16f92df20d7346105c6fcf8af/areas/core/shopify/components/apps/app/services/apps/models/ui_extension/validators/extension_metafield_config_validator.rb#L23

We reduced the key length from 3 to 2 and it looks like that wasn't replicated to the separate validation logic for metafields in UI Extensions.
