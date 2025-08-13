issue title: Checkpoint and resume capability
labels: brainstorm, epic/reliability
comment count: 1
hyperlink: https://github.com/shopify/roast/issues/229
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Description
Enable workflows to checkpoint progress and resume from failure points.

## Acceptance Criteria
- [ ] Automatic checkpoint creation
- [ ] State persistence mechanism
- [ ] Resume from checkpoint command
- [ ] Checkpoint management tools

Epic: epic/reliability

## Context
Checkpoint/resume would allow recovery from failures without rerunning completed steps.

===

comment #1 by obie, 2025-06-12, 16:35:42
Some of this is already implemented as sessions and replay.
