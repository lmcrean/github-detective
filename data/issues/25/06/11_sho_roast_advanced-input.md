issue title: Advanced input types for input steps
labels: enhancement, epic/developer-experience
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/240
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Summary
Extend the basic CLI input step with advanced input types and validation capabilities.

## Requirements
Building on the basic CLI input (#102), add:

### Advanced Input Types
1. **File Path Input**
   ```yaml
   - input:
       name: config_file
       prompt: "Select configuration file:"
       type: file
       filter: "*.yml"
       must_exist: true
   ```

2. **Multi-select**
   ```yaml
   - input:
       name: features
       prompt: "Select features to enable:"
       type: multi_choice
       options:
         - logging
         - monitoring
         - caching
         - security
       min_selections: 1
   ```

3. **Numeric Input**
   ```yaml
   - input:
       name: port
       prompt: "Enter port number:"
       type: number
       min: 1024
       max: 65535
       default: 3000
   ```

4. **Date/Time Input**
   ```yaml
   - input:
       name: schedule_date
       prompt: "When to run?"
       type: datetime
       format: "YYYY-MM-DD HH:mm"
       min: "now"
   ```

### Advanced Validation
- Regular expression patterns
- Custom validation scripts
- Cross-field validation
- Async validation (e.g., checking if username exists)

### Enhanced Features
- Input history/suggestions
- Tab completion for file paths
- Smart defaults based on context
- Input templates for common patterns

## Related Issues
- #102: User input step (basic CLI implementation)
- Depends on #102 being completed first

## Milestone
Suggested: v0.5 (Core Platform Features)

===
