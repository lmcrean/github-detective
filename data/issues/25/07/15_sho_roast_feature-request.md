issue title: Feature Request: Parallel Execution for Iterated Steps
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/325
status: open
date opened: 2025-07-15
repo 30d_merge_rate: 13

====

description:
# Feature Request: Parallel Execution for Iterated Steps

## Summary
Add support for parallel execution of iterations in `each` and `repeat` loops, allowing multiple iterations to run concurrently while maintaining sequential execution within each iteration.

## Background
Currently, Roast supports parallel execution for individual steps (by nesting them in arrays), but there's no way to execute iterations of a loop in parallel. When processing multiple items or repeating steps with independent iterations, this becomes a performance bottleneck.

## Proposed Syntax

```yaml
# Parallel each loop
- process_files:
    each: "{{Dir.glob('**/*.rb')}}"
    as: current_file
    steps:
      - analyze_file
      - optimize_code
      - run_tests
    parallel: true  # NEW: Run all iterations concurrently

# Parallel repeat loop  
- improve_variants:
    repeat:
      until: "{{all_passing}}"
      max_iterations: 5
      steps:
        - generate_variant
        - test_variant
      parallel: true  # NEW: Run iterations concurrently
```

## Use Cases

1. **File Processing**: When processing multiple files independently (linting, formatting, analysis)
2. **API Calls**: Making multiple API requests that don't depend on each other
3. **Test Variations**: Running multiple test scenarios or configurations in parallel
4. **Code Generation**: Generating multiple variations or implementations concurrently
5. **Data Processing**: Processing large datasets where each item can be handled independently

## Expected Behavior

- When `parallel: true` is set on an iteration step:
  - All iterations execute concurrently (up to a reasonable thread pool limit)
  - Within each iteration, steps still execute sequentially
  - The parent workflow waits for all iterations to complete before proceeding
  - Output from each iteration is properly isolated and aggregated

## Example Workflow

```yaml
name: optimize_multiple_files
tools:
  - Roast::Tools::ReadFile
  - Roast::Tools::WriteFile

steps:
  - find_files: $(find . -name "*.rb" -type f | head -10)
  
  - process_in_parallel:
      each: "{{output.find_files.split('\n')}}"
      as: file_path
      steps:
        - Read and analyze {{file_path}}
        - Optimize the code for performance
        - Write the optimized version
      parallel: true
  
  - summarize_results
```

## Implementation Considerations

1. **Thread Safety**: Ensure proper isolation between parallel iterations
2. **Resource Limits**: Consider maximum thread pool size to prevent resource exhaustion
3. **Error Handling**: How to handle failures in individual iterations
4. **Output Management**: Properly collect and organize outputs from parallel executions
5. **Progress Tracking**: How to report progress when iterations run concurrently

## Benefits

- **Performance**: Significant speedup for workflows processing multiple independent items
- **Efficiency**: Better resource utilization for I/O-bound operations
- **Flexibility**: Opt-in feature that doesn't change existing behavior
- **Consistency**: Uses familiar syntax pattern from existing parallel step execution

## Alternative Considered

While it's possible to manually structure workflows to achieve parallelism, this requires complex workarounds and loses the benefits of iteration constructs. The proposed feature provides a clean, declarative way to express parallel iteration intent.

===
