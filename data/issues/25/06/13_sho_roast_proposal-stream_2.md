issue title: Proposal: Streamlined Git Worktree Workflow Integration
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/258
status: open
date opened: 2025-06-13
repo 30d_merge_rate: 13

====

description:
## Summary

As developers work on Roast, it would be valuable to have a streamlined workflow that allows them to run multiple Claude Code sessions, each with their own dedicated task in isolated environments. Developers should be able to easily declare their intention to work on a new feature and be automatically set up in an isolated environment for that work.

## Proposal

Implement tooling that allows developers to:

1. **Declare intent**: A simple command like `bin/hack-on BRANCH_NAME` that expresses "I want to hack on new feature X"
2. **Automatic setup**: The tool should automatically:
   - Create a new git branch
   - Set up a git worktree for that branch
   - Launch a Claude Code session in that worktree
3. **Automatic cleanup**: When the developer is finished, the worktree should be cleaned up automatically

## Directory Convention

Worktrees would follow a consistent naming convention like `../roast@branch-name`, so from the parent directory you'd see:
- `roast/` (main repository)
- `roast@feature-foo/` (worktree for feature-foo branch)
- `roast@bugfix-bar/` (worktree for bugfix-bar branch)

This makes it easy to identify and navigate between different workspaces.

## Benefits

- **Parallel development**: Developers can work on multiple features simultaneously without branch switching
- **Multiple Claude sessions**: Each feature can have its own dedicated Claude Code session with focused context
- **Isolation**: Each feature gets its own workspace, preventing conflicts and confusion
- **Reduced friction**: Eliminates manual worktree management overhead
- **Clean workspace**: Automatic cleanup prevents worktree proliferation
- **Clear organization**: Consistent naming convention makes workspaces easy to identify

## Implementation Considerations

- Integration with Claude Code session lifecycle
- Cleanup workflow (potentially hooking into session exit)
- Branch management and cleanup policies
- Error handling for failed worktree creation

This would significantly improve the developer experience when working on multiple features or experiments in Roast.

===
