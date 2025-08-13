issue title: ApplicationWorkflow Base Class Pattern
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/272
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 2, Roast is shown using an `ApplicationWorkflow` base class pattern similar to Rails' `ApplicationController`.

## Feature Details
The book shows this pattern:

```ruby
# app/workflows/application_workflow.rb
class ApplicationWorkflow < Roast::BaseWorkflow
  before_execute :sanitize_inputs
  
  private
  
  def sanitize_inputs
    params.each do |key, value|
      if value.is_a?(String)
        # Remove potential prompt injections
        params[key] = value.gsub(/\bignore previous instructions\b/i, "")
                          .gsub(/\bsystem prompt\b/i, "")
      end
    end
  end
end
```

Then specific workflows inherit from it:
```ruby
class ArticleSummaryWorkflow < ApplicationWorkflow
  def execute
    step :extract_key_points do
      # Workflow implementation
    end
  end
end
```

## Features Needed
1. Support for callback methods like `before_execute`, `after_execute`
2. Shared configuration and behavior across all workflows
3. Rails-like inheritance pattern

## Rationale
Rails developers are familiar with the Application* base class pattern. It provides:
- Central place for shared behavior
- Security measures (input sanitization)
- Logging and instrumentation
- Configuration defaults

## Acceptance Criteria
- [ ] Roast::BaseWorkflow supports callback methods (before_execute, after_execute, around_execute)
- [ ] Callbacks can be inherited and chained
- [ ] Documentation showing ApplicationWorkflow pattern
- [ ] Example ApplicationWorkflow with common patterns
- [ ] Support for shared configuration methods

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
