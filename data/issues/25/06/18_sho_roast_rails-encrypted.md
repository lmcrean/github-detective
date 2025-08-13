issue title: Rails Encrypted Credentials Support
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/270
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 2, Roast is described as supporting Rails encrypted credentials for API key management.

## Feature Details
The book shows using Rails credentials for API keys:

```bash
# Edit credentials
rails credentials:edit

# Add your API keys:
# openai:
#   api_key: sk-proj-abc123...
# anthropic:
#   api_key: sk-ant-abc123...
```

Access in code:
```ruby
Rails.application.credentials.openai[:api_key]
```

## Integration with Roast
Roast should automatically detect and use Rails credentials when available:

```ruby
# config/initializers/roast.rb (Rails)
Roast.configure do |config|
  # Automatically use Rails credentials if available
  config.openai_api_key ||= Rails.application.credentials.dig(:openai, :api_key)
  config.anthropic_api_key ||= Rails.application.credentials.dig(:anthropic, :api_key)
end
```

## Rationale
Rails applications use encrypted credentials for production secrets. Roast should integrate seamlessly with this Rails feature rather than requiring separate environment variables.

## Acceptance Criteria
- [ ] Roast automatically checks Rails.application.credentials for API keys
- [ ] Falls back to environment variables if credentials not found
- [ ] Support for all provider API keys (OpenAI, Anthropic, etc.)
- [ ] Clear documentation on Rails credentials integration
- [ ] Works with Rails 6.0+ encrypted credentials system

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
