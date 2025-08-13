issue title: Enhanced CLI feedback and progress indicators
labels: brainstorm, epic/developer-experience
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/154
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Epic: Developer Experience Core

### Summary
Improve the CLI user experience by providing real-time feedback during LLM operations to prevent the interface from appearing hung during long-running tasks.

### Acceptance Criteria
- [ ] Show dynamic spinner/progress indicator during LLM calls
- [ ] Display model name, token count, and cost estimation in real-time
- [ ] Prevent CLI from appearing hung during long operations
- [ ] Provide clear visual feedback that processing is ongoing

### Implementation Notes
- Should integrate with existing CLI output system
- Consider using cli-ui spinner functionality
- Token counting and cost estimation should be based on model-specific pricing

===
