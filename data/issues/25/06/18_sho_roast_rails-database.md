issue title: Rails Database Session Storage Adapter
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/281
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 8, there are examples showing ActiveRecord being used directly with Roast sessions, suggesting deeper database integration.

## Feature Details
The book shows direct SQL queries on session data:
```ruby
# Direct SQL query for complex analysis
sessions = ActiveRecord::Base.connection.execute(<<~SQL)
  SELECT id, started_at, ended_at, status, error_message
  FROM sessions
  WHERE workflow_name = '#{workflow_name}'
    AND status = 'failed'
    AND started_at > '#{cutoff.iso8601}'
  ORDER BY started_at DESC
SQL
```

This suggests Roast could have an ActiveRecord adapter for session storage:
```ruby
# config/initializers/roast.rb
Roast.configure do |config|
  config.session_store = :active_record
end

# Or with custom table
Roast.configure do |config|
  config.session_store = Roast::SessionStore::ActiveRecord.new(
    table_name: 'roast_sessions'
  )
end
```

## Benefits
- Query sessions with ActiveRecord/SQL
- Integrate with existing database backups
- Use database indexes for performance
- Easier reporting and analytics
- Transaction support

## Schema
```ruby
class CreateRoastSessions < ActiveRecord::Migration[7.0]
  def change
    create_table :roast_sessions do |t|
      t.string :workflow_name, null: false
      t.string :workflow_id
      t.json :inputs
      t.json :outputs
      t.string :status
      t.text :error_message
      t.datetime :started_at
      t.datetime :ended_at
      t.json :metadata
      
      t.timestamps
      
      t.index :workflow_name
      t.index :status
      t.index :started_at
    end
  end
end
```

## Rationale
Rails apps already have databases. Using ActiveRecord for session storage enables powerful querying and reporting capabilities.

## Acceptance Criteria
- [ ] ActiveRecord adapter for session storage
- [ ] Migration generator for sessions table
- [ ] Session model with query scopes
- [ ] Support for JSON columns for inputs/outputs
- [ ] Performance optimization with indexes
- [ ] Documentation and examples
- [ ] Backwards compatibility with SQLite storage

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
