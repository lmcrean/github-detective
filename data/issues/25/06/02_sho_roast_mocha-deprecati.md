issue title: Mocha deprecation warnings
labels: Bug
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/127
status: open
date opened: 2025-06-02
repo 30d_merge_rate: 13

====

description:
```
Mocha deprecation warning at roast/lib/roast/workflow/step_runner.rb:19:in 'Roast::Workflow::StepRunner#execute_step': Expectation defined at roast/test/roast/workflow/step_executors/hash_step_executor_test.rb:26:in 'Roast::Workflow::StepExecutors::HashStepExecutorTest#test_executes_simple_command_step' expected keyword arguments (exit_on_error: true), but received positional hash ({:exit_on_error => true}). These will stop matching when strict keyword argument matching is enabled. See the documentation for Mocha::Configuration#strict_keyword_argument_matching=.
Mocha deprecation warning at roast/lib/roast/workflow/step_runner.rb:19:in 'Roast::Workflow::StepRunner#execute_step': Expectation defined at roast/test/roast/workflow/step_executors/hash_step_executor_test.rb:45:in 'Roast::Workflow::StepExecutors::HashStepExecutorTest#test_respects_exit_on_error_configuration' expected keyword arguments (exit_on_error: false), but received positional hash ({:exit_on_error => false}). These will stop matching when strict keyword argument matching is enabled. See the documentation for Mocha::Configuration#strict_keyword_argument_matching=.
Mocha deprecation warning at roast/lib/roast/workflow/workflow_initializer.rb:95:in 'Roast::Workflow::WorkflowInitializer#configure_openrouter_client': Expectation defined at roast/test/roast/workflow/configuration_parser_openrouter_test.rb:15:in 'Roast::Workflow::ConfigurationParserOpenRouterTest#test_configure_openrouter_client' expected keyword arguments (access_token: "test_openrouter_token"), but received positional hash ({:access_token => "test_openrouter_token"}). These will stop matching when strict keyword argument matching is enabled. See the documentation for Mocha::Configuration#strict_keyword_argument_matching=.
Mocha deprecation warning at roast/lib/roast/workflow/workflow_initializer.rb:107:in 'Roast::Workflow::WorkflowInitializer#configure_openai_client': Expectation defined at roast/test/roast/workflow/workflow_initializer_test.rb:59:in 'RoastWorkflowInitializerTest#test_configures_api_client_when_api_token_present_and_not_already_configured' expected keyword arguments (access_token: "test-token"), but received positional hash ({:access_token => "test-token"}). These will stop matching when strict keyword argument matching is enabled. See the documentation for Mocha::Configuration#strict_keyword_argument_matching=.
Mocha deprecation warning at roast/lib/roast/workflow/workflow_initializer.rb:107:in 'Roast::Workflow::WorkflowInitializer#configure_openai_client': Expectation defined at roast/test/roast/workflow/workflow_initializer_test.rb:204:in 'RoastWorkflowInitializerTest#test_raises_authentication_error_when_api_token_invalid' expected keyword arguments (access_token: "invalid-token"), but received positional hash ({:access_token => "invalid-token"}). These will stop matching when strict keyword argument matching is enabled. See the documentation for Mocha::Configuration#strict_keyword_argument_matching=.
Mocha deprecation warning at roast/lib/roast/workflow/workflow_initializer.rb:107:in 'Roast::Workflow::WorkflowInitializer#configure_openai_client': Expectation defined at roast/test/roast/workflow/workflow_initializer_test.rb:78:in 'RoastWorkflowInitializerTest#test_configures_api_client_with_uri_base' expected keyword arguments (access_token: "test-token", uri_base: "https://custom-api.example.com"), but received positional hash ({:access_token => "test-token", :uri_base => "https://custom-api.example.com"}). These will stop matching when strict keyword argument matching is enabled. See the documentation for Mocha::Configuration#strict_keyword_argument_matching=.
```

===
