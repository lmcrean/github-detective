issue title: ActiveSupport::Notifications Integration for APM
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/276
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 1 and Chapter 19, Roast is described as integrating with Rails APM through ActiveSupport::Notifications.

## Feature Details
The book states: "Integrates with your existing APM through ActiveSupport::Notifications. Every step, tool call, and completion shows up in your dashboards."

Chapter 19 shows detailed instrumentation:
```ruby
ActiveSupport::Notifications.subscribe(/^roast\./) do |name, start, finish, id, payload|
  duration = finish - start
  
  # Log to monitoring system
  case name
  when 'roast.workflow.completed'
    Rails.logger.info "Workflow completed", {
      workflow: payload[:workflow_name],
      duration: duration,
      success: payload[:success]
    }
  when 'roast.step.executed'
    Rails.logger.info "Step executed", {
      step: payload[:step_name],
      duration: duration
    }
  when 'roast.ai.completion'
    Rails.logger.info "AI completion", {
      prompt_tokens: payload[:prompt_tokens],
      completion_tokens: payload[:completion_tokens],
      model: payload[:model]
    }
  end
end
```

## Events to Instrument
- `roast.workflow.started`
- `roast.workflow.completed`
- `roast.step.started`
- `roast.step.completed`
- `roast.tool.executed`
- `roast.ai.completion`
- `roast.cache.hit`
- `roast.cache.miss`
- `roast.error.raised`

## Rationale
Rails applications use ActiveSupport::Notifications for instrumentation. This integrates with:
- Rails logs
- APM tools (New Relic, DataDog, etc.)
- Custom monitoring dashboards

## Acceptance Criteria
- [ ] All major Roast operations emit ActiveSupport::Notifications events
- [ ] Consistent event naming convention (roast.*)
- [ ] Rich payload data for each event
- [ ] Documentation of all events and payloads
- [ ] Example subscribers for common use cases
- [ ] Performance overhead is minimal
- [ ] Works without Rails (graceful degradation)

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
