issue title: Migrate from .roast directory to XDG Base Directory Specification
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/247
status: open
date opened: 2025-06-12
repo 30d_merge_rate: 13

====

description:
## Summary

This proposal argues for migrating Roast from using a custom `.roast` directory to following the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html). This change would improve consistency, customizability, and simplify our codebase.

## Current State

Roast currently uses a `.roast` directory for three main purposes:

1. **Function caching** - Tool function call results cached in `.roast/cache/`
2. **Session caching** - Workflow session state stored in `.roast/sessions/`  
3. **Project initializers** - Custom project configuration in `.roast/initializers/`

### Current Implementation Details

- `lib/roast/dot_roast.rb` handles directory traversal to find `.roast` directories
- `lib/roast/tools.rb:8-9` sets up function cache in `.roast/cache/`
- `lib/roast/workflow/session_manager.rb:74` stores sessions in `.roast/sessions/`
- `lib/roast/initializers.rb:7` loads initializers from `.roast/initializers/`

## Proposed XDG Migration

### Configuration (Initializers)
- **Current**: `.roast/initializers/`
- **Proposed**: 
  - Workflow-specific: `{workflow_directory}/initializers/`
    - This would mean either there can be no step named "initializers", and/or we'd need to support `{workflow_directory}/steps`. 
  - Global: `$XDG_CONFIG_HOME/roast/initializers/` (default: `~/.config/roast/initializers/`)

### Cache Storage
- **Current**: `.roast/cache/` and `.roast/sessions/`
- **Proposed**: 
  - Function cache: `$XDG_CACHE_HOME/roast/functions/` (default: `~/.cache/roast/functions/`)
  - Session cache: `$XDG_STATE_HOME/roast/sessions/` (default: `~/.local/state/roast/sessions/`)

## Benefits of XDG Adoption

### 1. **Easier Shopify-wide Configuration**
Our internal `dev` CLI tool could easily place global Roast initializers in the standard XDG config directory, allowing Shopify-wide defaults without requiring per-project setup.

### 2. **User Customizability**
Users can set `XDG_*` environment variables to customize where Roast stores its data:
```bash
export XDG_CONFIG_HOME="/custom/config"
export XDG_CACHE_HOME="/fast/ssd/cache"
export XDG_STATE_HOME="/persistent/state"
```

### 3. **Standard, Discoverable Locations**
XDG directories are well-known locations that follow Unix conventions. Users and system administrators know where to find configuration and cache files.

### 4. **Simplified Code**
We can eliminate the directory traversal logic in `dot_roast.rb` since XDG paths are deterministic. No more searching up the directory tree for `.roast` folders.

## References

- [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
- [Arch Wiki: XDG Base Directory](https://wiki.archlinux.org/title/XDG_Base_Directory)

This change aligns Roast with modern Unix conventions and provides a better foundation for both individual users and organization-wide deployment.

===
