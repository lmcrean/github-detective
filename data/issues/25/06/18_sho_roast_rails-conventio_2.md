issue title: Rails Conventions for Workflow Organization
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/269
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 2, Roast is described as following Rails conventions for organizing workflows within Rails applications.

## Feature Details
The book describes this directory structure:
```
app/
├── workflows/          # Workflow classes (like controllers)
│   ├── application_workflow.rb
│   └── summarization_workflow.rb
├── roast/             # Prompts and workflow-specific files
│   └── summarization/
│       └── summarize/
│           └── prompt.md
└── models/            # Your existing models
    └── article.rb     # Can trigger workflows
```

## Naming Conventions
- Workflow class name: `SummarizationWorkflow`
- File location: `app/workflows/summarization_workflow.rb`
- Prompt location: `app/roast/summarization/[step_name]/prompt.md`

## Example from the book:
```ruby
class ArticleSummaryWorkflow < ApplicationWorkflow
  def execute
    step :extract_key_points do
      # Looks for: app/roast/article_summary/extract_key_points/prompt.md
    end
  end
end
```

## Rationale
Rails developers expect certain conventions:
- Workflows in `app/workflows` similar to controllers
- Base `ApplicationWorkflow` class for shared behavior
- Predictable file locations for prompts based on workflow and step names

## Acceptance Criteria
- [ ] Roast automatically looks for workflows in `app/workflows` when in a Rails app
- [ ] Prompt resolution follows the convention: `app/roast/[workflow_name]/[step_name]/prompt.md`
- [ ] Support for `ApplicationWorkflow` base class pattern
- [ ] Clear documentation on Rails conventions
- [ ] Works seamlessly with Rails autoloading

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
