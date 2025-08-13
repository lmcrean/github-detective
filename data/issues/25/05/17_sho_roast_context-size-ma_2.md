issue title: Context Size Management / Auto-Compaction for Workflows
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/45
status: open
date opened: 2025-05-17
repo 30d_merge_rate: 13

====

description:
Roast workflows maintain shared context throughout execution, allowing steps to build upon each other's outputs. However, this leads to a common challenge: as workflows progress through multiple steps, the conversation history grows, potentially causing workflows to fail when they exceed the LLM's context window limits (e.g., 128K tokens for GPT-4o).

## Problem Statement

Long-running workflows or those with extensive output can exhaust the available context window, causing API errors or degraded performance. Currently, there is no automated mechanism to manage context size within a workflow's lifecycle, requiring manual pruning or workflow restructuring.

## Proposed Solution: Adaptive Context Management

Implement an intelligent context management system that automatically monitors and optimizes the context window usage during workflow execution through several mechanisms:

### Feature Components

  1. Context Size Monitoring
    - Track token usage across each step's execution
    - Provide runtime warnings when approaching configurable thresholds (e.g., 80% of context window)
    - Expose metrics through the existing instrumentation system
  2. Automatic Compaction Strategies
    - Summarization: When context exceeds thresholds, automatically generate concise summaries of previous steps
    - Selective Retention: Intelligently determine which previous exchanges are most relevant to retain
    - Pruning: Remove irrelevant or redundant information while preserving critical context
  3. Configuration Options

```yaml
  name: My Workflow
  context_management:
    enabled: true
    strategy: "auto"  # Options: auto, summarize, prune, none
    threshold: 0.8    # Percentage of context window to trigger compaction
    max_tokens: 100000  # Hard limit on context size
    retain_steps: ["critical_step_1", "critical_step_2"]  # Steps to always keep in full
```

  4. Tool Integration
    - compact_context: A new tool allowing explicit compaction during workflow execution
    - Integration with existing state repository for persisting important information
  5. Step Annotations
  analyze_data:
    context_importance: high  # Options: high, medium, low

###  Implementation Details

  1. Token Counting Service
    - Add a lightweight service that tracks token usage without requiring API calls
    - Intelligently estimate token counts using ratio-based algorithms
    - Cache token counts to avoid repeated calculations
  2. State Management Extensions
    - Enhance FileStateRepository to store critical information outside the context window
    - Extend SessionManager to manage context snapshots across steps
  3. Compaction Algorithms
    - Summarization: Request the LLM to summarize previous exchanges when context threshold is reached
    - Selective Pruning: Keep exchanges with special tags, remove oldest non-critical ones
    - Hybrid Approach: Combine summarization and pruning based on content relevance
  4. Session Resumption Enhancements
    - During replay, intelligently reconstruct context from compacted states
    - Support backfilling context when needed for specific steps

##  User Experience

  1. Transparent Operation
    - Context management operations happen automatically between steps
    - Users can enable/disable or configure via workflow YAML
  2. Feedback and Logging
    - Add verbose logging of context management activities
    - Provide statistics on tokens saved through compaction
  3. Manual Control
    - Support explicit context management via tools and step configurations
    - Allow configuration of context reduction via CLI flag

##  Implementation Path

  1. Implement basic token counting and monitoring
  2. Add configurable thresholds and warning system
  3. Implement the summarization strategy
  4. Add selective pruning capabilities
  5. Integrate with existing state repository
  6. Extend workflow configuration schema
  7. Create documentation and examples

##  Benefits

  1. Reliability: Prevents workflow failures due to context overflow
  2. Performance: Reduces token usage and improves response times
  3. Cost Efficiency: Minimizes token consumption for long-running workflows
  4. Flexibility: Adapts to different workflow requirements through configuration

##  Technical Considerations

  - Integration with different LLM providers and their token counting mechanisms
  - Balancing context preservation with reduction
  - Ensuring consistent behavior across different models
  - Graceful fallback when context management fails

##  Future Considerations (to keep in mind when implementing)

  - Learn from workflow execution patterns to optimize context retention
  - Provide context visualization tools in the command-line interface. Would require live updating screen, which is currently out of scope.
  - Support custom compaction strategies through extensions


===
