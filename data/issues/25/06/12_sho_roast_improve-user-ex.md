issue title: Improve user experience when API key is missing or invalid
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/249
status: open
date opened: 2025-06-12
repo 30d_merge_rate: 13

====

description:
I filed https://github.com/Shopify/roast/issues/130 and was pointed to https://github.com/Shopify/roast/issues/10 . That was fixed in https://github.com/Shopify/roast/pull/56 and is a lot more clear what is happening.

Here is what it looks like now:

```
Configuring OpenAI client with token from workflow
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/response/raise_error.rb:30:in 'Faraday::Response::RaiseError#on_complete': API authentication failed: No API token provided or token is invalid (Roast::Errors::AuthenticationError)
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/middleware.rb:57:in 'block in Faraday::Middleware#call'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/response.rb:42:in 'Faraday::Response#on_complete'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/middleware.rb:56:in 'Faraday::Middleware#call'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/rack_builder.rb:153:in 'Faraday::RackBuilder#build_response'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/connection.rb:452:in 'Faraday::Connection#run_request'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/connection.rb:200:in 'Faraday::Connection#get'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/ruby-openai-7.4.0/lib/openai/http.rb:10:in 'OpenAI::HTTP#get'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/ruby-openai-7.4.0/lib/openai/models.rb:8:in 'OpenAI::Models#list'
        from /Users/josh.nichols/workspace/roast/lib/roast/workflow/workflow_initializer.rb:157:in 'Roast::Workflow::WorkflowInitializer#validate_api_client'
        from /Users/josh.nichols/workspace/roast/lib/roast/workflow/workflow_initializer.rb:97:in 'Roast::Workflow::WorkflowInitializer#configure_api_client'
        from /Users/josh.nichols/workspace/roast/lib/roast/workflow/workflow_initializer.rb:14:in 'Roast::Workflow::WorkflowInitializer#setup'
        from /Users/josh.nichols/workspace/roast/lib/roast/workflow/configuration_parser.rb:17:in 'Roast::Workflow::ConfigurationParser#initialize'
        from /Users/josh.nichols/workspace/roast/lib/roast.rb:67:in 'Class#new'
        from /Users/josh.nichols/workspace/roast/lib/roast.rb:67:in 'Roast::CLI#execute'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/thor-1.3.2/lib/thor/command.rb:28:in 'Thor::Command#run'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/thor-1.3.2/lib/thor/invocation.rb:127:in 'Thor::Invocation#invoke_command'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/thor-1.3.2/lib/thor.rb:538:in 'Thor.dispatch'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/thor-1.3.2/lib/thor/base.rb:584:in 'Thor::Base::ClassMethods#start'
        from /Users/josh.nichols/workspace/roast/exe/roast:17:in '<top (required)>'
        from bin/roast:27:in 'Kernel#load'
        from bin/roast:27:in '<main>'
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/response/raise_error.rb:30:in 'Faraday::Response::RaiseError#on_complete': the server responded with status 401 (Faraday::UnauthorizedError)
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/middleware.rb:57:in 'block in Faraday::Middleware#call'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/response.rb:42:in 'Faraday::Response#on_complete'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/middleware.rb:56:in 'Faraday::Middleware#call'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/rack_builder.rb:153:in 'Faraday::RackBuilder#build_response'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/connection.rb:452:in 'Faraday::Connection#run_request'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/faraday-2.13.1/lib/faraday/connection.rb:200:in 'Faraday::Connection#get'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/ruby-openai-7.4.0/lib/openai/http.rb:10:in 'OpenAI::HTTP#get'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/ruby-openai-7.4.0/lib/openai/models.rb:8:in 'OpenAI::Models#list'
        from /Users/josh.nichols/workspace/roast/lib/roast/workflow/workflow_initializer.rb:157:in 'Roast::Workflow::WorkflowInitializer#validate_api_client'
        from /Users/josh.nichols/workspace/roast/lib/roast/workflow/workflow_initializer.rb:97:in 'Roast::Workflow::WorkflowInitializer#configure_api_client'
        from /Users/josh.nichols/workspace/roast/lib/roast/workflow/workflow_initializer.rb:14:in 'Roast::Workflow::WorkflowInitializer#setup'
        from /Users/josh.nichols/workspace/roast/lib/roast/workflow/configuration_parser.rb:17:in 'Roast::Workflow::ConfigurationParser#initialize'
        from /Users/josh.nichols/workspace/roast/lib/roast.rb:67:in 'Class#new'
        from /Users/josh.nichols/workspace/roast/lib/roast.rb:67:in 'Roast::CLI#execute'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/thor-1.3.2/lib/thor/command.rb:28:in 'Thor::Command#run'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/thor-1.3.2/lib/thor/invocation.rb:127:in 'Thor::Invocation#invoke_command'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/thor-1.3.2/lib/thor.rb:538:in 'Thor.dispatch'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.4/lib/ruby/gems/3.4.0/gems/thor-1.3.2/lib/thor/base.rb:584:in 'Thor::Base::ClassMethods#start'
        from /Users/josh.nichols/workspace/roast/exe/roast:17:in '<top (required)>'
        from bin/roast:27:in 'Kernel#load'
        from bin/roast:27:in '<main>'
```

I think that it should be a known and expected type of error for users to be missing ehe env or having it be incorrect. In cases like that, for CLI tools, I think it makes sense to give a more human readable explaination of what failed and how to fix it.

Here is some examples of what could happen.

For invalid token:

```
Configuring OpenAI client with token from workflow (`OPEN_AI_TOKEN`)...
Failed to authenticate: Received HTTP 501 Unauthorized from https://whatever

This means that OPEN_AI_TOKEN is set in the environment, but is not being accepted. Double check:
- the token is correct
- that the token has not expired
```

And for the token being absent:
```
Configuring OpenAI client with token from workflow (`OPEN_AI_TOKEN`)...
Failed to authenticate: Received HTTP 501 Unauthorized from https://whatever

OPEN_AI_TOKEN is missing from the environment . This workflow requires it to be set to a valid 
- go to http://whatever to create a key
- set OPEN_AI_TOKEN=whatever
- try again
```

I started a PR to try to move towards this, but not sure how I like the implementation. So, I wanted to get feedback on the idea before spending more time, or maybe there are better ways to do it?

===
