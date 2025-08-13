issue title: [Bug]: Incorrectly getting total size error on theme push
labels: Severity: 3, Type: Bug, Area: @shopify/theme
comment count: 2
hyperlink: https://github.com/shopify/cli/issues/6082
status: open
date opened: 2025-07-09
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Theme

### Expected behavior

Changes from main branch on connected github repository should be pushed to live main theme

### Actual behavior

We are trying to push changes to our live theme from a connected github repository, however when pushing we are getting a bunch of error messages in the theme log of "Validation failed: The total size of templates in blocks, config, layout, snippets, templates, locales, sections exceeds 250MB" when looking at the theme folder sizes it is only ~180mb so not sure why we are getting the error

<img width="482" height="333" alt="Image" src="https://github.com/user-attachments/assets/3e978bad-845b-451c-83f1-c7fdc040a30c" />

<img width="856" height="446" alt="Image" src="https://github.com/user-attachments/assets/0c4e3ae2-c54d-415b-a4a9-a6a27db3a6b7" />

### Verbose output

N/A

### Reproduction steps

1. Merged PR for pushing changes from our staging branch to main
2. When the changes were attempted to be pushed to the main live theme the above errors were thrown

### Operating System

Windows 10

### Shopify CLI version (`shopify --version`)

@shopify/cli/3.59.1 wsl-x64 node-v20.12.2

### Shell

zsh

### Node version (run `node -v` if you're not sure)

v20.12.2

### What language and version are you using in your application?

_No response_

===

comment #1 by karreiro, 2025-07-21, 08:13:25
👋 Hey @NiickFenske,

The fix for this issue won't live on Shopify CLI, since it actually comes from the Shopify API’s validation for asset uploads.

I've already reported this to the appropriate team. Once they update the Shopify validations, you’ll see an update here.

Thank you for reporting this.

comment #2 by lucyxiang, 2025-07-28, 21:08:30
Hello @NiickFenske, could you send me a copy of the theme as is that's causing this issue for us to verify the solution? You can email me at lucy.xiang@shopify.com thank you.
