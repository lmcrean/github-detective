issue title: Natural language to YAML workflow generation
labels: brainstorm, epic/developer-experience
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/158
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Epic: Developer Experience Core

### Summary
Enable users to describe workflows in natural language and automatically convert them to valid Roast YAML configurations.

### Acceptance Criteria
- [ ] Natural language → YAML workflow conversion
- [ ] Support common patterns like "When PR lands, summarize changes"
- [ ] Generate valid Roast YAML with proper structure
- [ ] Include validation and suggestions for improvement
- [ ] Provide explanations of generated workflow

### Implementation Notes
- Use LLM to parse intent and generate YAML
- Should validate generated YAML against schema
- Provide interactive refinement process
- Include library of common workflow patterns
- Consider generating documentation alongside YAML

===
