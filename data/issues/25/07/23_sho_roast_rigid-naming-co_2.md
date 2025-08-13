issue title: Rigid naming convention for plain ruby steps
labels: deficiency
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/334
status: open
date opened: 2025-07-23
repo 30d_merge_rate: 13

====

description:
In a plain ruby step, the loaded class must abide a rigid naming structure:
```
❌ Step failed: 'coverage_for_llm'
   Error: uninitialized constant CoverageForLlm
   This may be an issue with the step's implementation.
bundler: failed to load command: roast (/Users/nathanfaber-good/.dev/gem/5363350hi5f719harw2bnznq2gmjdilb-nix-shell/bin/roast)


🛑 Workflow stopped due to step failure.
   Check the error message above for details.

For debugging, you can run with --verbose for more details.
/Users/nathanfaber-good/.dev/gem/5363350hi5f719harw2bnznq2gmjdilb-nix-shell/bundler/gems/roast-48e5c8ef9f59/lib/roast/workflow/error_handler.rb:103:in 'Roast::Workflow::ErrorHandler#handle_generic_error': Failed to execute step 'coverage_for_llm': uninitialized constant CoverageForLlm (Roast::Workflow::WorkflowExecutor::StepExecutionError)
```

Ideally the naming wouldn't matter, or atleast be configurable.

===
