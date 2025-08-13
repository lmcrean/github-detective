issue title: Rails Cache Store Integration
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/279
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 11 and other chapters, Roast is shown integrating with Rails.cache for caching AI responses.

## Feature Details
The book shows configuration like:
```ruby
# config/initializers/roast.rb
Roast.configure do |config|
  # Use Rails cache
  config.cache_store = Rails.cache
end
```

And usage in workflows:
```ruby
class ExpensiveAnalysisWorkflow < ApplicationWorkflow
  def execute
    step :analyze do
      cache_key = "analysis:#{params[:document_id]}"
      
      Rails.cache.fetch(cache_key, expires_in: 1.hour) do
        prompt template: "expensive_analysis"
        execute_step
      end
    end
  end
end
```

## Integration Points
1. Use Rails.cache as the default cache store in Rails apps
2. Support all Rails cache stores (Memory, Redis, Memcached)
3. Respect Rails cache configuration
4. Integrate with cache keys and expiration

## Benefits
- Reuse existing Rails cache infrastructure
- Consistent caching across the application
- Works with Rails cache debugging tools
- Supports cache warming and invalidation

## Rationale
Rails applications already have caching infrastructure. Roast should integrate seamlessly rather than requiring separate cache configuration.

## Acceptance Criteria
- [ ] Roast detects and uses Rails.cache when available
- [ ] Support for all Rails cache store types
- [ ] Cache key generation helpers for workflows
- [ ] Documentation on Rails cache integration
- [ ] Examples of caching patterns
- [ ] Performance benchmarks showing cache benefits

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
