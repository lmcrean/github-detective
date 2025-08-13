issue title: ActiveJob Integration for Background Workflow Processing
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/271
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 1, Roast is described as having first-class integration with Rails background job systems through ActiveJob.

## Feature Details
The book mentions:
"Background Jobs: Works with Sidekiq, GoodJob, or any ActiveJob backend. Long-running workflows? Just `ProductDescriptionWorkflow.perform_async(product_id)`"

This suggests workflows can be easily queued as background jobs:

```ruby
# Synchronous execution
ProductDescriptionWorkflow.new(product_id: 123).execute

# Asynchronous via ActiveJob
ProductDescriptionWorkflow.perform_async(product_id: 123)

# Or with delay
ProductDescriptionWorkflow.perform_later(product_id: 123)
```

## Implementation Ideas
Base workflow class could include ActiveJob integration:

```ruby
class ApplicationWorkflow < Roast::BaseWorkflow
  include ActiveJob::Base if defined?(ActiveJob)
  
  def perform(*args)
    execute(*args)
  end
end
```

## Rationale
Many AI workflows are long-running and should be processed asynchronously. Rails developers expect ActiveJob integration for background processing.

## Acceptance Criteria
- [ ] Workflows can be queued using standard ActiveJob methods
- [ ] Support for all ActiveJob backends (Sidekiq, GoodJob, DelayedJob, etc.)
- [ ] Proper serialization of workflow parameters
- [ ] Job status tracking and error handling
- [ ] Documentation showing ActiveJob integration patterns
- [ ] Configurable job options (queue, priority, retry)

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
