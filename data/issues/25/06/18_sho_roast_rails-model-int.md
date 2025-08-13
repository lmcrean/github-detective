issue title: Rails Model Integration for Triggering Workflows
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/273
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 2 and Chapter 19, models are shown triggering workflows directly, suggesting tight Rails integration.

## Feature Details
The book's directory structure shows:
```
└── models/            # Your existing models
    └── article.rb     # Can trigger workflows
```

This implies models can trigger workflows, potentially through callbacks:

```ruby
class Article < ApplicationRecord
  after_create :generate_summary
  after_update :regenerate_summary, if: :content_changed?
  
  private
  
  def generate_summary
    ArticleSummaryWorkflow.perform_later(article_id: id)
  end
  
  def regenerate_summary
    # Could also be synchronous for immediate feedback
    result = ArticleSummaryWorkflow.new(article: self).execute
    update_column(:summary, result.output[:summary])
  end
end
```

## Integration Features
1. Easy workflow triggering from model callbacks
2. Passing model instances to workflows
3. Updating models with workflow results
4. Transaction awareness

## Rationale
Rails developers often need to trigger AI workflows based on model lifecycle events (creation, updates, etc.). This should be seamless.

## Acceptance Criteria
- [ ] Clear patterns for triggering workflows from models
- [ ] Support for passing ActiveRecord objects to workflows
- [ ] Transaction-safe workflow execution
- [ ] Examples of common patterns (generate on create, update on change)
- [ ] Documentation on model-workflow integration
- [ ] Consider adding DSL helpers for common patterns

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
