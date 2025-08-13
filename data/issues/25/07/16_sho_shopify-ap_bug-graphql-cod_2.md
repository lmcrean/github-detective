issue title: Bug: GraphQL codegen failing, `callbackUrl` missing from `WebhookSubscriptionInput`
labels: none
comment count: 2
hyperlink: https://github.com/shopify/shopify-app-js/issues/2682
status: open
date opened: 2025-07-16
repo 30d_merge_rate: 10

====

description:
# Issue summary

Before opening this issue, I have:

- [x] Upgraded to the latest version of the relevant packages  
  - `@shopify/*` package and version: N/A (GraphQL API usage directly)
  - Node version: 22.17.0
  - Operating system: MacOs 15.5
- [x] Set `{ logger: { level: LogSeverity.Debug } }` in my configuration, when applicable
- [x] Found a reliable way to reproduce the problem that indicates it's a problem with the package
- [x] Looked for similar issues in this repository
- [x] Checked that this isn't an issue with a Shopify API  
  ⚠️ **This is an issue with the Shopify Admin GraphQL API schema**

The `callbackUrl` field is still accepted and functional when using the `webhookSubscriptionCreate` mutation, but it is missing from the GraphQL schema for version `2025-07`.

## Expected behavior

The `callbackUrl` field should be present in the schema under `WebhookSubscriptionInput`, as documented here:  
https://shopify.dev/docs/api/admin-graphql/latest/input-objects/WebhookSubscriptionInput

## Actual behavior

- The `callbackUrl` field is **not** present in the schema:  
  https://shopify.dev/admin-graphql-direct-proxy/2025-07
- But sending it in the mutation works as expected — the webhook is created and uses the correct URL.
- ❗ This **breaks GraphQL tooling**, especially **code generation** tools like GraphQL Code Generator (`@graphql-codegen/...`), which rely on the schema and fail when undocumented fields are used.

## Steps to reproduce the problem

1. Open the Admin GraphQL schema explorer for version `2025-07`
2. Search for the `WebhookSubscriptionInput` input type — `callbackUrl` is missing
3. Try running the following mutation anyway:

```graphql
mutation {
  webhookSubscriptionCreate(
    topic: APP_UNINSTALLED
    webhookSubscription: {
      callbackUrl: "https://example.com/webhooks/uninstalled"
      format: JSON
    }
  ) {
    webhookSubscription {
      id
      endpoint {
        __typename
        ... on WebhookHttpEndpoint {
          callbackUrl
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```
4.	The webhook is created successfully.
5.	However, tools like GraphQL Codegen will throw errors due to callbackUrl not being defined in the schema.

## Debug logs
```
error TS2353: Object literal may only specify known properties, and 'callbackUrl' does not exist in type 'WebhookSubscriptionInput'.
```

<img width="1068" height="908" alt="Image" src="https://github.com/user-attachments/assets/33b92a10-28b4-421b-ba00-38496b81d46e" />

===

comment #1 by sle-c, 2025-07-17, 18:06:09
hi @dauran 

this is due to the introspection not returning deprecated input fields by default, you can specify a custom introspection query to pass the introspection schema to the graphql-codegen tool


1. Create a file named `fetch-introspection.js` at the root of your project.

```js
const fetch = require('node-fetch');
const fs = require('fs');

const ENDPOINT = 'https://your-graphql-endpoint.com/graphql';

const INTROSPECTION_QUERY = `
query IntrospectionQuery {
  __schema {
    queryType {
      name
    }
    mutationType {
      name
    }
    subscriptionType {
      name
    }
    types {
      ...FullType
    }
    directives {
      name
      description
      locations
      args(includeDeprecated: true) {
        ...InputValue
      }
    }
  }
}
fragment FullType on __Type {
  kind
  name
  description
  fields(includeDeprecated: true) {
    name
    description
    args(includeDeprecated: true) {
      ...InputValue
    }
    type {
      ...TypeRef
    }
    isDeprecated
    deprecationReason
  }
  inputFields(includeDeprecated: true) {
    ...InputValue
  }
  interfaces {
    ...TypeRef
  }
  enumValues(includeDeprecated: true) {
    name
    description
    isDeprecated
    deprecationReason
  }
  possibleTypes {
    ...TypeRef
  }
}
fragment InputValue on __InputValue {
  name
  description
  type {
    ...TypeRef
  }
  defaultValue
}
fragment TypeRef on __Type {
  kind
  name
  ofType {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
              }
            }
          }
        }
      }
    }
  }
}
`;

async function fetchIntrospection() {
  const response = await fetch(ENDPOINT, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query: INTROSPECTION_QUERY }),
  });

  if (!response.ok) {
    console.error(`Failed to fetch: ${response.status} ${response.statusText}`);
    process.exit(1);
  }

  const result = await response.json();

  if (result.errors) {
    console.error('Errors in introspection response:', result.errors);
    process.exit(1);
  }

  fs.writeFileSync(
    'schema.json',
    JSON.stringify(result, null, 2),
    { encoding: 'utf8' }
  );
  console.log('Introspection result written to schema.json');
}

fetchIntrospection();
```

2. Install dependencies:

```sh
npm install node-fetch@2
```

3. Run the script to fetch the schema and write it to `schema.json`:

```sh
node fetch-introspection.js
```

4. In your project root, create a `codegen.yml` file:

```yaml
schema: ./schema.json
documents: src/**/*.graphql
generates:
  src/generated/types.ts:
    plugins:
      - typescript
      - typescript-operations
```

5. Install GraphQL Code Generator dependencies if you haven't:

```sh
npm install @graphql-codegen/cli @graphql-codegen/typescript @graphql-codegen/typescript-operations
```

6. Run GraphQL Code Generator:

```sh
npx graphql-codegen
```

comment #2 by tgensol, 2025-07-22, 07:52:27
@sle-c Thank you for your reply. I can see the depreciation for `uri`, but the new RC still have callbackUrl everywhere : https://shopify.dev/docs/api/admin-graphql/2025-10/input-objects/WebhookSubscriptionInput#fields-uri ?
