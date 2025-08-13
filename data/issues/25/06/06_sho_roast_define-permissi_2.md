issue title: Define permissions for CodingAgent in tool config
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/145
status: open
date opened: 2025-06-06
repo 30d_merge_rate: 13

====

description:
The CodingAgent (Claude) inherits whatever permissions the user has already granted to Claude in interactive sessions. During a Roast workflow, Claude will attempt to ask for permissions that it doesn't have, which will always fail. If the user has never run Claude in the given project, this can result in complete failure of the CodingAgent to do anything.

Roast workflows should be able to define "expected permissions" for the coding agent, so we can either validate against `.claude/settings.json` that these permissions are present, or pass them explicitly in the cli Claude invocation.

===
