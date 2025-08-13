issue title: [Feature]: Command-Specific Environment Flags
labels: Type: Enhancement, Area: @shopify/theme
comment count: 1
hyperlink: https://github.com/shopify/cli/issues/5889
status: open
date opened: 2025-05-22
repo 30d_merge_rate: 77

====

description:
### What area(s) will this request affect?

Other

### What type of change do you want to see?

New feature

### Overview

Reposting @stijns96 original request - [link](https://github.com/Shopify/develop-app-inner-loop/issues/2799)

Feature request
We’re wondering if it would be possible for the CLI to:

Ignore ignore rules when running shopify theme dev, or
Provide a flag like --no-ignore for theme dev, or
Support command-specific config overrides in shopify.theme.toml, allowing us to treat dev and push differently.
This would allow for more flexible, environment-aware workflows without needing external scripting or duplicate config files.

Let us know if this is something you'd consider or if there's a better approach we're overlooking. Thanks!

### Motivation

We use shopify.theme.toml with multiple environments (e.g. dev, stage, prod) and have configured per-environment ignore rules — which works well for commands like theme push.

However, we’ve run into a limitation:

On theme push, we want to ignore specific files (e.g. .json templates/settings on production).
On theme dev, we want to serve everything, without ignoring any files — especially .json.
The problem is that theme dev also respects the ignore rules defined in shopify.theme.toml, even though in a development workflow, we want the exact opposite behavior.

Current workaround
To get around this, we've built a wrapper CLI that temporarily removes or renames .shopifyignore (or modifies the environment config) when running theme dev, then restores it afterward.

This works, but it's fragile — and ideally we’d like to drop .shopifyignore entirely and use shopify.theme.toml as the single source of truth for all environments and workflows.

===

comment #1 by isaacroldan, 2025-06-12, 11:47:57
@jamesmengo  please move this issue to an internal board for proper tracking.
