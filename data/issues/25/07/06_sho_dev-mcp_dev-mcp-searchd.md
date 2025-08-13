issue title: dev-mcp search_dev_docs response exceeds maximum allowed tokens, making it unusable for large queries
labels: none
comment count: 6
hyperlink: https://github.com/shopify/dev-mcp/issues/58
status: open
date opened: 2025-07-06
repo 30d_merge_rate: 20

====

description:
I'm running Dev MCP using a claude code `.mcp.json` configuration with args: `-y @shopify/dev-mcp@latest`. When using the dev-mcp `search_dev_docs` tool, I encounter the following error for queries that return a large number of results:

`Error: MCP tool "search_dev_docs" response (56451 tokens) exceeds maximum allowed tokens (25000). Please use pagination, filtering, or limit parameters to reduce the response size.`

This makes the tool unusable for broad or schema-related queries, as there is no way to paginate or limit the results from the client side. For example, searching for "CartInputMetafieldInput schema fields" triggers this error.
### Steps to Reproduce:
Call the dev-mcp search_dev_docs tool with a query that returns a large result set (e.g., "CartInputMetafieldInput schema fields").
Observe the error about exceeding the maximum allowed tokens.
### Expected Behavior:
The tool should either:
Support pagination or result limiting parameters, or
Automatically chunk or filter results to avoid exceeding token limits.
### Actual Behavior:
The tool fails with a token limit error and does not return any results.
### Impact:
Makes it impossible to use dev-mcp search_dev_docs for large or schema-wide queries, significantly reducing its usefulness for development and documentation lookup.
### Suggested Solutions:
- Implement server-side pagination or filtering.
- Allow the client to specify a token response limit or page parameter.
- Return a partial result with a continuation token or similar mechanism.

===

comment #1 by michaelhaessig, 2025-07-11, 20:39:55
Also running into this issue.  This makes the whole mcp significantly less useful 👎 

````mcp__shopify-dev-mcp__search_dev_docs
Parameters:

{
  "prompt": "Shopify Draft Orders Admin API GraphQL create draft order mutation"
}
❌ Error: MCP tool "search_dev_docs" response (47651 tokens) exceeds maximum allowed tokens (25000). Please use pagination, filtering, or limit parameters to reduce the response size.
````

comment #2 by jonathanmoore, 2025-07-21, 15:12:59
@matteodepalo @Arkham This issue started happening 2 weeks ago around the same time that some of the tools were renamed.
get_started -> learn_shopify_api
search_dev_docs -> search_docs_chunks
fetch_docs_by_path -> fetch_full_docs
https://github.com/Shopify/dev-mcp/pull/63

Is there a plan on releasing a new updated package? As of right now the use of Shopify docs with the MCP is broken.

comment #3 by matteodepalo, 2025-07-21, 15:27:01
Those renames haven't been released yet. Are you using `@latest`?

comment #4 by matteodepalo, 2025-07-21, 15:43:29
In any case, this issue will be solved when we release https://github.com/Shopify/dev-mcp/pull/67.

comment #5 by jonathanmoore, 2025-07-22, 14:21:47
@matteodepalo It looks like #67 will fix the token issue. For now, I did go ahead and build dev-mcp locally and point to the version with the new tools. That seems to work flawlessly.

```json
{
  "mcpServers": {
    "shopify-dev-mcp": {
      "command": "node",
      "args": ["/Users/LOCAL-PATH/dev-mcp/dist/index.js"]
    }
  }
}
```

comment #6 by michaelhaessig, 2025-07-24, 19:52:07
@matteodepalo  is there a planned release date? 
