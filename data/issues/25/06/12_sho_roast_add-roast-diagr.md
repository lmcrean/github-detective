issue title: Add `roast diagram` command to generate workflow diagrams (MVP)
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/253
status: open
date opened: 2025-06-12
repo 30d_merge_rate: 13

====

description:
## Summary

Add a basic `roast diagram` command that generates a simple visual representation of a workflow's structure as a PNG image.

## Motivation

- Provide visual documentation for workflows in the examples directory
- Help users quickly understand workflow structure
- Enable basic debugging of control flow

## MVP Scope

### Command
```bash
bin/roast diagram path/to/workflow.yml
```

Outputs: `workflow_diagram.png` in the current directory

### What to Visualize
1. **Steps**: Simple boxes with step names
2. **Basic Control Flow**:
   - Sequential flow (arrows between steps)
   - `if/unless` as diamond shapes
   - `each/repeat` as boxes with loop indicators
3. **Inline prompts**: Shown as distinct colored/styled boxes

### Implementation
- Use ruby-graphviz gem
- Parse workflow with existing `Roast::Workflow::Configuration`
- Generate basic directed graph
- Output as PNG only

### Testing Strategy
**Integration Testing**: Generate diagrams for all workflows in `examples/` directory
- This serves as both integration testing and documentation
- Ensures the command works with all workflow patterns we support
- Generated diagrams can be committed to the repo for reference

### Out of Scope for MVP
- Multiple output formats
- Themes/styling options
- Interactive features
- Detailed step configurations
- Complex layouts
- Command options

## Future Enhancements
- SVG output
- Better layout algorithms
- Show step configurations (model, params)
- Color coding by step type
- Output path option

===
