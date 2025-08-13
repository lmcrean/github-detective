issue title: Advanced input features and patterns
labels: enhancement, epic/developer-experience
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/242
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Summary
Implement advanced features for the input step system including conditional inputs, bulk collection, and reusable templates.

## Requirements

### Conditional Inputs
```yaml
steps:
  - input:
      name: environment
      prompt: "Select environment:"
      type: choice
      options: [dev, staging, prod]
  
  - input:
      name: prod_password
      prompt: "Enter production password:"
      type: text
      masked: true
      when: "#{state.environment == 'prod'}"
```

### Bulk Input Collection
```yaml
steps:
  - input:
      name: team_members
      prompt: "Add team member"
      type: collection
      fields:
        - name: name
          type: text
          required: true
        - name: email
          type: text
          validation: email
        - name: role
          type: choice
          options: [dev, lead, manager]
      min_items: 1
      max_items: 10
```

### Input Templates
```yaml
# .roast/input_templates/deploy.yml
template: deploy_approval
fields:
  - name: approver
    type: text
    validation: email
  - name: reason
    type: multiline
  - name: emergency
    type: boolean
    default: false

# Usage in workflow:
steps:
  - input:
      template: deploy_approval
      timeout: 1800
```

### Dynamic Options
```yaml
steps:
  - input:
      name: branch
      prompt: "Select branch to deploy:"
      type: choice
      options_from: "git branch -r | grep -v HEAD"
```

### Input Pipelines
```yaml
steps:
  - input:
      name: config
      prompt: "Paste JSON configuration:"
      type: multiline
      transform:
        - validate: json
        - extract: "#{json.database.host}"
```

## Technical Approach
- Template registry system
- Dynamic field generation
- Input transformation pipeline
- Conditional evaluation engine

## Related Issues
- #102: Basic CLI input implementation
- #240: Advanced input types
- Builds upon the foundation of basic inputs

## Milestone
Suggested: v0.9 (Advanced capabilities)

===
