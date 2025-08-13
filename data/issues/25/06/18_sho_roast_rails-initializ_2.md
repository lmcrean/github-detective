issue title: Rails Initializer for Roast Configuration
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/274
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 2, Roast configuration in Rails apps is shown using an initializer file with Rails-specific patterns.

## Feature Details
The book shows this configuration pattern:

```ruby
# config/initializers/roast.rb (Rails)
Roast.configure do |config|
  # Use Claude for complex reasoning
  config.provider_for(:reasoning) do
    { provider: :anthropic, model: "claude-3-opus-20240229" }
  end
  
  # Use GPT-4 Turbo for general tasks
  config.provider_for(:general) do
    { provider: :openai, model: "gpt-4-turbo-preview" }
  end
  
  # Use GPT-3.5 for simple, high-volume tasks
  config.provider_for(:simple) do
    { provider: :openai, model: "gpt-3.5-turbo", temperature: 0.3 }
  end
end
```

## Rails-Specific Features
1. Configuration through Rails initializers
2. Environment-specific settings using Rails.env
3. Integration with Rails credentials
4. Automatic reloading in development

## Example Extended Configuration
```ruby
# config/initializers/roast.rb
Roast.configure do |config|
  # Use Rails credentials
  config.openai_api_key = Rails.application.credentials.dig(:openai, :api_key)
  
  # Environment-specific settings
  config.cache_enabled = \!Rails.env.development?
  config.verbose_logging = Rails.env.development?
  
  # Use Rails cache
  config.cache_store = Rails.cache
  
  # Instrumentation through Rails
  config.instrumenter = ActiveSupport::Notifications
end
```

## Rationale
Rails developers expect configuration through initializers with access to Rails-specific features like credentials, caching, and environment detection.

## Acceptance Criteria
- [ ] Roast configuration works in Rails initializers
- [ ] Access to Rails.env for environment-specific config
- [ ] Integration with Rails.application.credentials
- [ ] Support for Rails.cache as cache store
- [ ] Proper reloading in development mode
- [ ] Documentation for Rails-specific configuration

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
