issue title: Establish consistent test folder structure and naming conventions
labels: enhancement, developer-experience
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/262
status: open
date opened: 2025-06-13
repo 30d_merge_rate: 13

====

description:
## Summary

Establishing consistent test folder structure and naming conventions will enable fast static analysis for test coverage, easier automation, and better tooling support. We can fail early if files lack corresponding tests without running the test suite, and the obvious structure makes it much easier for LLMs and other tools to understand the codebase.

## Proposed Standards

### Directory Structure Rules
1. **Mirror lib structure**: `test/` should exactly mirror `lib/` directory structure
2. **Namespace correspondence**: Every module directory in `lib/roast/` should have a matching `test/roast/` directory
3. **File correspondence**: Every `.rb` file should have a corresponding `*_test.rb` file

### Naming Conventions
1. **Test files**: Always use `*_test.rb` suffix
2. **Test classes**: Should match the class being tested with `Test` suffix
   - `Roast::Workflow` → `Roast::WorkflowTest`
   - `Roast::Tools::Bash` → `Roast::Tools::BashTest`
3. **Test directories**: Should match module names exactly

### Exceptions
Files that should NOT have corresponding tests:
- `bin/` directory scripts  
- `exe/` directory executables
- Version files (`version.rb`)
- Entry point files that only require other files

## Key Benefits

### Static Analysis & Fast Feedback
- **Instant coverage validation**: Check test coverage without running tests by comparing file structures
- **Early CI failures**: Fail builds immediately if new files lack corresponding tests
- **Automated test scaffolding**: Generate skeleton test files automatically based on class structure

### Developer & Tooling Experience  
- **LLM-friendly structure**: Clear conventions make it trivial for AI tools to understand and work with tests
- **Predictable navigation**: Developers can instantly locate tests for any given class
- **Loading conventions**: Standardized structure enables automatic test helper loading and setup

### Current Structure Analysis
The roast gem already follows many good practices with its `test/roast/` structure mirroring `lib/roast/` and consistent `*_test.rb` naming. Some gaps exist where test files could be added to achieve complete correspondence.

## Missing Test Files
Based on current lib structure:
- `test/roast/errors_test.rb`
- `test/roast/tools_test.rb` 
- `test/roast/value_objects_test.rb`
- Various workflow-related test files
- Complete helpers test coverage

🤖 Generated with [Claude Code](https://claude.ai/code)

===
