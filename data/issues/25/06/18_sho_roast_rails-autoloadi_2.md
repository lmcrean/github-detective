issue title: Rails Autoloading Support for Workflows
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/280
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 2, workflows in Rails apps should work with Rails autoloading, but this needs explicit support.

## Feature Details
The book mentions workflows should "work seamlessly with Rails autoloading" and shows this structure:
```
app/workflows/
├── application_workflow.rb
├── product_description_workflow.rb
└── order_analysis_workflow.rb
```

These should be autoloaded like other Rails components:
```ruby
# Should work without explicit requires
workflow = ProductDescriptionWorkflow.new(product: @product)
result = workflow.execute
```

## Technical Requirements
1. Workflows in app/workflows should be autoloaded
2. Follow Rails naming conventions (file name matches class name)
3. Work with Rails class reloading in development
4. Support for namespaced workflows

## Example with Namespaces
```ruby
# app/workflows/admin/report_workflow.rb
module Admin
  class ReportWorkflow < ApplicationWorkflow
    # ...
  end
end

# Usage
Admin::ReportWorkflow.new.execute
```

## Rationale
Rails developers expect components in the app/ directory to be autoloaded. Manual requires break the Rails development experience.

## Acceptance Criteria
- [ ] Workflows in app/workflows are autoloaded in Rails apps
- [ ] Support for Rails development mode reloading
- [ ] Namespaced workflows work correctly
- [ ] No manual requires needed for workflows
- [ ] Clear error messages when workflows can't be found
- [ ] Documentation on Rails autoloading behavior

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
