issue title: Rails Generator for Roast Installation
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/268
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 2, a Rails generator is described that sets up Roast in Rails applications.

## Feature Details
The generator should be invoked with:
```bash
rails generate roast:install
```

## What it creates:
- `config/roast.yml` - Configuration file
- `app/workflows/` - Directory for workflow classes  
- `app/roast/` - Directory for prompts and workflow-specific files
- `.env.example` - Example environment variables (if not exists)
- Updates `.gitignore` 
- `spec/support/roast.rb` - RSpec support file

## Rationale
Rails developers expect generators for easy integration. This follows Rails conventions and provides a quick setup path.

## Example from the book:
```bash
# Inside your Rails app directory
rails generate roast:install

# This creates:
# create  config/roast.yml
# create  app/workflows/
# create  app/roast/
# create  .env.example (if not exists)
# append  .gitignore
# create  spec/support/roast.rb
```

## Acceptance Criteria
- [ ] Generator creates all necessary directories and files
- [ ] Generator respects existing files (doesn't overwrite)
- [ ] Generator output follows Rails conventions
- [ ] Generator works with Rails 6.1+ and Ruby 3.0+
- [ ] Generated structure matches Rails conventions

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
