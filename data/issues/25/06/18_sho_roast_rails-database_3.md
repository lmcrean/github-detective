issue title: Rails Database Migration Analysis Workflow Example
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/277
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 9, there's an extensive example of using Roast to analyze Rails database migrations with ActiveRecord integration.

## Feature Details
The book shows a sophisticated workflow that:
1. Validates migration syntax
2. Tests migrations in a sandboxed environment
3. Captures SQL statements
4. Checks for dangerous operations
5. Tests reversibility

Example code from the book:
```ruby
post :validate_migration do
  ruby(isolation: :require) { |workflow|
    # Extract migration class name
    content = File.read(migration_file)
    class_match = content.match(/class (\w+) < ActiveRecord::Migration/)
    
    # Check for dangerous operations
    dangerous = %w[drop_table remove_column change_column]
    found_dangerous = dangerous.select { |op| content.include?(op) }
    
    {
      class_name: class_match[1],
      dangerous_operations: found_dangerous,
      reversible: content.include?('reversible')
    }
  }
end

post :test_migration do
  ruby(isolation: :fork) { |workflow|
    ActiveRecord::Base.establish_connection(
      adapter: 'postgresql',
      database: 'roast_migration_test'
    )
    
    ActiveRecord::Base.transaction do
      # Run migration
      migration_class = output.pre_validation['class_name'].constantize
      migration = migration_class.new
      
      # Capture SQL
      queries = []
      ActiveRecord::Base.connection.class.set_callback(:log, :before) do |_, _, _, _, details|
        queries << details[:sql] if details[:sql]
      end
      
      migration.up
      migration.down
      
      raise ActiveRecord::Rollback  # Don't actually change test DB
    end
  }
end
```

## Rationale
This showcases deep Rails integration possibilities and provides a valuable real-world example of Roast analyzing Rails code.

## Implementation Requirements
- [ ] Ability to analyze Ruby/Rails code safely
- [ ] ActiveRecord integration for migration testing
- [ ] SQL query capture and analysis
- [ ] Sandboxed execution environment
- [ ] Integration with Rails migration API

## Acceptance Criteria
- [ ] Document this as an example workflow
- [ ] Ensure necessary Rails integration points exist
- [ ] Provide safe execution environment for testing
- [ ] Include in examples directory
- [ ] Add to Rails integration guide

## Note
This sophisticated example from "The Roast Book" demonstrates deep Rails integration that doesn't currently exist in the codebase.

===
