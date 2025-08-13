issue title: "Argument list too long" from ShellScriptStep on large `workflow.output`
labels: Bug, deficiency
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/337
status: open
date opened: 2025-07-24
repo 30d_merge_rate: 13

====

description:
ShellScripStep sets an [env var with the entire content of output at that time](https://github.com/Shopify/roast/blob/c9508815c5a2ddb6e27700675dfdf3232e57752c/lib/roast/workflow/shell_script_step.rb#L66). If the current output is large, this can result in "Argument list too long":

```
❌ Step failed: 'uhh'
   Error: Argument list too long - /Users/nathanfaber-good/world/trees/root/src/areas/core/shopify/roast/ci-coverage/uhh.sh
   This may be an issue with the step's implementation.
bundler: failed to load command: roast (/Users/nathanfaber-good/.dev/gem/5363350hi5f719harw2bnznq2gmjdilb-nix-shell/bin/roast)


🛑 Workflow stopped due to step failure.
   Check the error message above for details.

For debugging, you can run with --verbose for more details.
/Users/nathanfaber-good/.dev/gem/5363350hi5f719harw2bnznq2gmjdilb-nix-shell/bundler/gems/roast-48e5c8ef9f59/lib/roast/workflow/error_handler.rb:103:in 'Roast::Workflow::ErrorHandler#handle_generic_error': Failed to execute step 'uhh': Argument list too long - /Users/nathanfaber-good/world/trees/root/src/areas/core/shopify/roast/ci-coverage/uhh.sh (Roast::Workflow::WorkflowExecutor::StepExecutionError)
```

workflow.yml
```yaml
name: CI Coverage
model: anthropic:claude-opus-4-20250514
tools:
  - Roast::Tools::Bash
  - Roast::Tools::ReadFile
  - Roast::Tools::WriteFile

steps:
  - set_output
  - uhh
```

uhh.sh
```shell
echo 'uhh'
```

set_output.rb
```ruby
# typed: true
# frozen_string_literal: true

require "json"
require "open3"

class SetOutput < Roast::Workflow::BaseStep
  def call
    append_to_final_output(big_content)
  end

  def big_content
    "big content, big content, bit content, big contente\n" * 100_000
  end
end

```

===
