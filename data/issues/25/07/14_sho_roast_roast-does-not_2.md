issue title: Roast does not give more details about 500 errors
labels: none
comment count: 1
hyperlink: https://github.com/shopify/roast/issues/323
status: open
date opened: 2025-07-14
repo 30d_merge_rate: 13

====

description:
Running into a 500 error during a step. This is the error:
```
| /tmp/bundle/ruby/3.4.0/bundler/gems/roast-1cdfd8c1b44b/lib/roast/workflow/error_handler.rb:103:in 'Roast::Workflow::ErrorHandler#handle_generic_error': Failed to execute step 'run_coverage': the server responded with status 500 (Roast::Workflow::WorkflowExecutor::StepExecutionError)
  | from /tmp/bundle/ruby/3.4.0/bundler/gems/roast-1cdfd8c1b44b/lib/roast/workflow/error_handler.rb:39:in 'Roast::Workflow::ErrorHandler#with_error_handling'
  | from /tmp/bundle/ruby/3.4.0/bundler/gems/roast-1cdfd8c1b44b/lib/roast/workflow/step_orchestrator.rb:28:in 'Roast::Workflow::StepOrchestrator#execute_step'
  | from /tmp/bundle/ruby/3.4.0/bundler/gems/roast-1cdfd8c1b44b/lib/roast/workflow/step_executor_coordinator.rb:262:in 'Roast::Workflow::StepExecutorCoordinator#execute_standard_step'
  | from /tmp/bundle/ruby/3.4.0/bundler/gems/roast-1cdfd8c1b44b/lib/roast/workflow/step_executor_coordinator.rb:254:in 'Roast::Workflow::StepExecutorCoordinator#execute_string_step'
  | from /tmp/bundle/ruby/3.4.0/bundler/gems/roast-1cdfd8c1b44b/lib/roast/workflow/step_executor_coordinator.rb:81:in 'Roast::Workflow::StepExecutorCoordinator#execute'
```

Roast should give more information about that error.

===

comment #1 by dblock, 2025-07-14, 18:16:23
This was caused by an AI proxy returning a 500. The error log should show which URL caused the problem and potentially the detail from the response.
