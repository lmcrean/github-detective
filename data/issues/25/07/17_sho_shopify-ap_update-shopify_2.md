issue title: Update shopify app remix tutorial to recommend custom introspection
labels: none
comment count: 0
hyperlink: https://github.com/shopify/shopify-app-js/issues/2685
status: open
date opened: 2025-07-17
repo 30d_merge_rate: 10

====

description:
We need to update https://shopify.dev/docs/api/shopify-app-remix/v2/guide-graphql-types to include a workaround for getting deprecated fields in case fields are deprecated from the Shopify GQL API

> hi @dauran 
> 
> this is due to the introspection not returning deprecated input fields by default, you can specify a custom introspection query to pass the introspection schema to the graphql-codegen tool
> 
> 
> 1. Create a file named `fetch-introspection.js` at the root of your project.
> 
> ```js
> const fetch = require('node-fetch');
> const fs = require('fs');
> 
> const ENDPOINT = 'https://your-graphql-endpoint.com/graphql';
> 
> const INTROSPECTION_QUERY = `
> query IntrospectionQuery {
>   __schema {
>     queryType {
>       name
>     }
>     mutationType {
>       name
>     }
>     subscriptionType {
>       name
>     }
>     types {
>       ...FullType
>     }
>     directives {
>       name
>       description
>       locations
>       args(includeDeprecated: true) {
>         ...InputValue
>       }
>     }
>   }
> }
> fragment FullType on __Type {
>   kind
>   name
>   description
>   fields(includeDeprecated: true) {
>     name
>     description
>     args(includeDeprecated: true) {
>       ...InputValue
>     }
>     type {
>       ...TypeRef
>     }
>     isDeprecated
>     deprecationReason
>   }
>   inputFields(includeDeprecated: true) {
>     ...InputValue
>   }
>   interfaces {
>     ...TypeRef
>   }
>   enumValues(includeDeprecated: true) {
>     name
>     description
>     isDeprecated
>     deprecationReason
>   }
>   possibleTypes {
>     ...TypeRef
>   }
> }
> fragment InputValue on __InputValue {
>   name
>   description
>   type {
>     ...TypeRef
>   }
>   defaultValue
> }
> fragment TypeRef on __Type {
>   kind
>   name
>   ofType {
>     kind
>     name
>     ofType {
>       kind
>       name
>       ofType {
>         kind
>         name
>         ofType {
>           kind
>           name
>           ofType {
>             kind
>             name
>             ofType {
>               kind
>               name
>               ofType {
>                 kind
>                 name
>               }
>             }
>           }
>         }
>       }
>     }
>   }
> }
> `;
> 
> async function fetchIntrospection() {
>   const response = await fetch(ENDPOINT, {
>     method: 'POST',
>     headers: { 'Content-Type': 'application/json' },
>     body: JSON.stringify({ query: INTROSPECTION_QUERY }),
>   });
> 
>   if (!response.ok) {
>     console.error(`Failed to fetch: ${response.status} ${response.statusText}`);
>     process.exit(1);
>   }
> 
>   const result = await response.json();
> 
>   if (result.errors) {
>     console.error('Errors in introspection response:', result.errors);
>     process.exit(1);
>   }
> 
>   fs.writeFileSync(
>     'schema.json',
>     JSON.stringify(result, null, 2),
>     { encoding: 'utf8' }
>   );
>   console.log('Introspection result written to schema.json');
> }
> 
> fetchIntrospection();
> ```
> 
> 2. Install dependencies:
> 
> ```sh
> npm install node-fetch@2
> ```
> 
> 3. Run the script to fetch the schema and write it to `schema.json`:
> 
> ```sh
> node fetch-introspection.js
> ```
> 
> 4. In your project root, create a `codegen.yml` file:
> 
> ```yaml
> schema: ./schema.json
> documents: src/**/*.graphql
> generates:
>   src/generated/types.ts:
>     plugins:
>       - typescript
>       - typescript-operations
> ```
> 
> 5. Install GraphQL Code Generator dependencies if you haven't:
> 
> ```sh
> npm install @graphql-codegen/cli @graphql-codegen/typescript @graphql-codegen/typescript-operations
> ```
> 
> 6. Run GraphQL Code Generator:
> 
> ```sh
> npx graphql-codegen
> ``` 

 _Originally posted by @sle-c in [#2682](https://github.com/Shopify/shopify-app-js/issues/2682#issuecomment-3084972144)_

===
