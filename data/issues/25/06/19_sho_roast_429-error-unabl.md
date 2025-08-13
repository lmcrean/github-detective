issue title: 429 error - unable to run "Try it" workflow
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/286
status: open
date opened: 2025-06-19
repo 30d_merge_rate: 13

====

description:
As a brand new user, using the [Try it](https://github.com/Shopify/roast?tab=readme-ov-file#try-it) workflow results in a 429 error. I assume this is due to the OpenAI's 3RPM limit on some plans, including the free trial.

```bash
Executing: generate_grades (Resource type: none)

❌ Step failed: 'generate_grades'
   Error: the server responded with status 429
   This may be an issue with the step's implementation.


🛑 Workflow stopped due to step failure.
   Check the error message above for details.
```

I'm able to get through all steps by re-starting from the failed step 1 minute later. I had to re-start the workflow twice.

A README word of warning, and ideally some advice on suggested RPM/RPD limits, could be helpful for folks either unfamiliar with more intensive LLM integrations (like me) or who are working within their organization's OpenAI billing restrictions (also me).

<details>
  <summary>Full failure output</summary>

```bash
$ ./exe/roast execute examples/grading/workflow.yml test/roast/resources_test.rb --verbose
🔥🔥🔥 Everyone loves a good roast 🔥🔥🔥

Configuring OpenAI client with token from workflow
Starting workflow...
Workflow: {...}/roast/examples/grading/workflow.yml
Options: {verbose: true}
Running workflow for file: test/roast/resources_test.rb
Executing: read_dependencies (Resource type: none)
🔍 Searching for: '**/resources.rb' in '{...}roast'
✓ Complete: read_dependencies (consumed 1,799 tokens, total 1,799)


Executing: run_coverage - analyze_coverage - verify_test_helpers - verify_mocks_and_stubs (Resource type: none)
✓ Complete: run_coverage - analyze_coverage - verify_test_helpers - verify_mocks_and_stubs (consumed 468 tokens, total 2,267)


Executing: generate_grades (Resource type: none)

❌ Step failed: 'generate_grades'
   Error: the server responded with status 429
   This may be an issue with the step's implementation.


🛑 Workflow stopped due to step failure.
   Check the error message above for details.

For debugging, you can run with --verbose for more details.
{...}/roast/lib/roast/workflow/error_handler.rb:103:in 'Roast::Workflow::ErrorHandler#handle_generic_error': Failed to execute step 'generate_grades': the server responded with status 429 (Roast::Workflow::WorkflowExecutor::StepExecutionError)
	from {...}/roast/lib/roast/workflow/error_handler.rb:39:in 'Roast::Workflow::ErrorHandler#with_error_handling'
	from {...}/roast/lib/roast/workflow/step_orchestrator.rb:28:in 'Roast::Workflow::StepOrchestrator#execute_step'
	from {...}/roast/lib/roast/workflow/step_executor_coordinator.rb:262:in 'Roast::Workflow::StepExecutorCoordinator#execute_standard_step'
	from {...}/roast/lib/roast/workflow/step_executor_coordinator.rb:254:in 'Roast::Workflow::StepExecutorCoordinator#execute_string_step'
	from {...}/roast/lib/roast/workflow/step_executor_coordinator.rb:81:in 'Roast::Workflow::StepExecutorCoordinator#execute'
	from {...}/roast/lib/roast/workflow/step_executor_with_reporting.rb:19:in 'Roast::Workflow::StepExecutorWithReporting#execute'
	from {...}/roast/lib/roast/workflow/step_executor_with_reporting.rb:42:in 'block in Roast::Workflow::StepExecutorWithReporting#execute_steps'
	from {...}/roast/lib/roast/workflow/step_executor_with_reporting.rb:34:in 'Array#each'
	from {...}/roast/lib/roast/workflow/step_executor_with_reporting.rb:34:in 'Enumerable#each_with_index'
	from {...}/roast/lib/roast/workflow/step_executor_with_reporting.rb:34:in 'Roast::Workflow::StepExecutorWithReporting#execute_steps'
	from {...}/roast/lib/roast/workflow/workflow_executor.rb:114:in 'Roast::Workflow::WorkflowExecutor#execute_steps'
	from {...}/roast/lib/roast/workflow/workflow_runner.rb:92:in 'Roast::Workflow::WorkflowRunner#execute_workflow'
	from {...}/roast/lib/roast/workflow/workflow_runner.rb:110:in 'Roast::Workflow::WorkflowRunner#run_single_workflow'
	from {...}/roast/lib/roast/workflow/workflow_runner.rb:28:in 'block in Roast::Workflow::WorkflowRunner#run_for_files'
	from {...}/roast/lib/roast/workflow/workflow_runner.rb:26:in 'Array#each'
	from {...}/roast/lib/roast/workflow/workflow_runner.rb:26:in 'Roast::Workflow::WorkflowRunner#run_for_files'
	from {...}/roast/lib/roast/workflow/configuration_parser.rb:35:in 'Roast::Workflow::ConfigurationParser#begin!'
	from {...}/roast/lib/roast.rb:69:in 'Roast::CLI#execute'
	from {...}/.gem/ruby/3.4.2/gems/thor-1.3.2/lib/thor/command.rb:28:in 'Thor::Command#run'
	from {...}/.gem/ruby/3.4.2/gems/thor-1.3.2/lib/thor/invocation.rb:127:in 'Thor::Invocation#invoke_command'
	from {...}/.gem/ruby/3.4.2/gems/thor-1.3.2/lib/thor.rb:538:in 'Thor.dispatch'
	from {...}/.gem/ruby/3.4.2/gems/thor-1.3.2/lib/thor/base.rb:584:in 'Thor::Base::ClassMethods#start'
	from ./exe/roast:17:in '<main>'
{...}/.gem/ruby/3.4.2/gems/faraday-2.13.1/lib/faraday/response/raise_error.rb:30:in 'Faraday::Response::RaiseError#on_complete': the server responded with status 429 (Faraday::TooManyRequestsError)
	from {...}/.gem/ruby/3.4.2/gems/faraday-2.13.1/lib/faraday/middleware.rb:57:in 'block in Faraday::Middleware#call'
	from {...}/.gem/ruby/3.4.2/gems/faraday-2.13.1/lib/faraday/response.rb:42:in 'Faraday::Response#on_complete'
	from {...}/.gem/ruby/3.4.2/gems/faraday-2.13.1/lib/faraday/middleware.rb:56:in 'Faraday::Middleware#call'
	from {...}/.gem/ruby/3.4.2/gems/faraday-2.13.1/lib/faraday/rack_builder.rb:153:in 'Faraday::RackBuilder#build_response'
	from {...}/.gem/ruby/3.4.2/gems/faraday-2.13.1/lib/faraday/connection.rb:452:in 'Faraday::Connection#run_request'
	from {...}/.gem/ruby/3.4.2/gems/faraday-2.13.1/lib/faraday/connection.rb:280:in 'Faraday::Connection#post'
	from {...}/.gem/ruby/3.4.2/gems/ruby-openai-7.4.0/lib/openai/http.rb:22:in 'OpenAI::HTTP#json_post'
	from {...}/.gem/ruby/3.4.2/gems/ruby-openai-7.4.0/lib/openai/client.rb:24:in 'OpenAI::Client#chat'
	from {...}/.gem/ruby/3.4.2/gems/raix-1.0.1/lib/raix/chat_completion.rb:323:in 'Raix::ChatCompletion#openai_request'
	from {...}/.gem/ruby/3.4.2/gems/raix-1.0.1/lib/raix/chat_completion.rb:147:in 'Raix::ChatCompletion#chat_completion'
	from {...}/.gem/ruby/3.4.2/gems/raix-1.0.1/lib/raix/function_dispatch.rb:116:in 'Raix::FunctionDispatch#chat_completion'
	from {...}/roast/lib/roast/workflow/base_workflow.rb:82:in 'block in Roast::Workflow::BaseWorkflow#chat_completion'
	from {...}/roast/lib/roast/workflow/base_workflow.rb:119:in 'Roast::Workflow::BaseWorkflow#with_model'
	from {...}/roast/lib/roast/workflow/base_workflow.rb:59:in 'Roast::Workflow::BaseWorkflow#chat_completion'
	from {...}/roast/lib/roast/workflow/base_step.rb:43:in 'Roast::Workflow::BaseStep#chat_completion'
	from {...}/roast/lib/roast/workflow/base_step.rb:28:in 'Roast::Workflow::BaseStep#call'
	from {...}/roast/lib/roast/workflow/step_orchestrator.rb:35:in 'block in Roast::Workflow::StepOrchestrator#execute_step'
	from {...}/roast/lib/roast/workflow/error_handler.rb:19:in 'Roast::Workflow::ErrorHandler#with_error_handling'
	from {...}/roast/lib/roast/workflow/step_orchestrator.rb:28:in 'Roast::Workflow::StepOrchestrator#execute_step'
	from {...}/roast/lib/roast/workflow/step_executor_coordinator.rb:262:in 'Roast::Workflow::StepExecutorCoordinator#execute_standard_step'
	from {...}/roast/lib/roast/workflow/step_executor_coordinator.rb:254:in 'Roast::Workflow::StepExecutorCoordinator#execute_string_step'
	from {...}/roast/lib/roast/workflow/step_executor_coordinator.rb:81:in 'Roast::Workflow::StepExecutorCoordinator#execute'
	from {...}/roast/lib/roast/workflow/step_executor_with_reporting.rb:19:in 'Roast::Workflow::StepExecutorWithReporting#execute'
	from {...}/roast/lib/roast/workflow/step_executor_with_reporting.rb:42:in 'block in Roast::Workflow::StepExecutorWithReporting#execute_steps'
	from {...}/roast/lib/roast/workflow/step_executor_with_reporting.rb:34:in 'Array#each'
	from {...}/roast/lib/roast/workflow/step_executor_with_reporting.rb:34:in 'Enumerable#each_with_index'
	from {...}/roast/lib/roast/workflow/step_executor_with_reporting.rb:34:in 'Roast::Workflow::StepExecutorWithReporting#execute_steps'
	from {...}/roast/lib/roast/workflow/workflow_executor.rb:114:in 'Roast::Workflow::WorkflowExecutor#execute_steps'
	from {...}/roast/lib/roast/workflow/workflow_runner.rb:92:in 'Roast::Workflow::WorkflowRunner#execute_workflow'
	from {...}/roast/lib/roast/workflow/workflow_runner.rb:110:in 'Roast::Workflow::WorkflowRunner#run_single_workflow'
	from {...}/roast/lib/roast/workflow/workflow_runner.rb:28:in 'block in Roast::Workflow::WorkflowRunner#run_for_files'
	from {...}/roast/lib/roast/workflow/workflow_runner.rb:26:in 'Array#each'
	from {...}/roast/lib/roast/workflow/workflow_runner.rb:26:in 'Roast::Workflow::WorkflowRunner#run_for_files'
	from {...}/roast/lib/roast/workflow/configuration_parser.rb:35:in 'Roast::Workflow::ConfigurationParser#begin!'
	from {...}/roast/lib/roast.rb:69:in 'Roast::CLI#execute'
	from {...}/.gem/ruby/3.4.2/gems/thor-1.3.2/lib/thor/command.rb:28:in 'Thor::Command#run'
	from {...}/.gem/ruby/3.4.2/gems/thor-1.3.2/lib/thor/invocation.rb:127:in 'Thor::Invocation#invoke_command'
	from {...}/.gem/ruby/3.4.2/gems/thor-1.3.2/lib/thor.rb:538:in 'Thor.dispatch'
	from {...}/.gem/ruby/3.4.2/gems/thor-1.3.2/lib/thor/base.rb:584:in 'Thor::Base::ClassMethods#start'
	from ./exe/roast:17:in '<main>'
```
</details>



===
