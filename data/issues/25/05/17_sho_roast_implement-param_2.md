issue title: Implement Parameterized Subroutines for Workflows
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/51
status: open
date opened: 2025-05-17
repo 30d_merge_rate: 13

====

description:
## Description

Implement parameterized subroutines (reusable step sequences) for Roast workflows to improve modularity, reusability, and maintainability of complex workflows.

## Problem

Currently, Roast workflows cannot define reusable sequences of steps that can be invoked multiple times with different parameters. This leads to duplicated step definitions and makes workflows harder to maintain when common operations need to be performed on different inputs.

## Proposed Solution

Implement a subroutine mechanism that allows defining reusable step sequences with parameters:

\\\

## Implementation Details

1. Extend the workflow schema to support subroutine definitions
2. Add parameter passing mechanisms to subroutines
3. Implement a calling mechanism with argument passing
4. Support local variable scoping within subroutines
5. Implement parameter validation
6. Update documentation with examples

## Acceptance Criteria

- [ ] Workflow schema supports defining subroutines with parameters
- [ ] Steps can call subroutines with specified arguments
- [ ] Variables created inside subroutines are properly scoped
- [ ] Parameters are validated when subroutines are called
- [ ] Subroutines can be nested (one subroutine can call another)
- [ ] Documentation is updated with comprehensive examples
- [ ] Tests cover all edge cases (parameter validation, scoping, nesting)

## Related Issues

Part of #46 (Enhanced Control Flow for Roast Workflows)

===
