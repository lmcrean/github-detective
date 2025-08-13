issue title: Plain ruby step de-pluralizes to get constant
labels: deficiency
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/335
status: open
date opened: 2025-07-23
repo 30d_merge_rate: 13

====

description:
```
Executing: generate_tests (Resource type: none)
Requiring step file: /Users/nathanfaber-good/world/trees/local-testgen-basic-functionality/src/areas/core/shopify/roast/ci-coverage/generate_tests.rb

❌ Step failed: 'generate_tests'
   Error: uninitialized constant GenerateTest
   This may be an issue with the step's implementation.
bundler: failed to load command: roast (/Users/nathanfaber-good/.dev/gem/5363350hi5f719harw2bnznq2gmjdilb-nix-shell/bin/roast)


🛑 Workflow stopped due to step failure.
   Check the error message above for details.

For debugging, you can run with --verbose for more details.
/Users/nathanfaber-good/.dev/gem/5363350hi5f719harw2bnznq2gmjdilb-nix-shell/bundler/gems/roast-48e5c8ef9f59/lib/roast/workflow/error_handler.rb:103:in 'Roast::Workflow::ErrorHandler#handle_generic_error': Failed to execute step 'generate_tests': uninitialized constant GenerateTest (Roast::Workflow::WorkflowExecutor::StepExecutionError)
```

===
