issue title: Implement structured logging with separate output streams
labels: brainstorm, epic/cost-observability
comment count: 2
hyperlink: https://github.com/shopify/roast/issues/160
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Summary
Enhance logging capabilities with structured JSON formatting and separated output streams for better observability. Use the scope of this issue to standardize the mess that is current puts to STDOUT and STDERR.

## Acceptance Criteria
- [ ] Standardize Roast ouputs to STDOUT and STDERR for consistency
- [ ] JSON-formatted logs for better parsing and analysis
- [ ] Separate streams for workflow output vs errors/diagnostics
- [ ] Support for `roast logs --tail` command to follow workflow execution
- [ ] Structured log events with consistent schema
- [ ] Configurable log levels and output formats

## Technical Details
- Implement structured logger with JSON output option
- Use STDOUT for workflow results, STDERR for diagnostics
- Create log tailing functionality similar to `tail -f`
- Ensure all log entries include timestamp, step, level, and context

**Labels:** brainstorm, epic/cost-observability
**Epic:** Cost Management & Observability

===

comment #1 by technicalpickles, 2025-06-13, 01:21:09
I have been thinking about how to improve the CLI output when running, and wondering how to implement that. There's number of  `ActiveSupport::Notifications.instrument` across the code base which can be used for observability, which made me think those could be used for the CLI output.

More broadly, I suspect a combination of having loggers + subscriptions to post to the logs, it'd be possible to implement most of these.

comment #2 by technicalpickles, 2025-06-13, 13:15:21
Another good pattern I've seen recently is in [Karafka for it's Monitoring and Logging](https://karafka.io/docs/Monitoring-and-Logging/). Basically, you create a class, and define methods on it that correspond to events. 

For example, if you have [a `tool.complete` event](https://github.com/Shopify/roast/blob/50a3c94336d35c17cc94da4def40472222102305/lib/roast/helpers/function_caching_interceptor.rb#L65-L69), you could make a subscriber class that responds to `on_tool_complete`:

```ruby
class BasicLoggerSubscriber
  def initialize
    @logger = Logger.new
  end
  def on_tool_complete(function_name, execution_time, cache_enabled)
     @logger.info "#{function_name} completed in #{execution_time}"
  end
end
```

Thinking about it, I'm kinda surprised there isn't a way to do this directly with `ActiveSupport::Notifications` 🤔 
