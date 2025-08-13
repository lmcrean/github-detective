issue title: [Epic] Improve workflow resiliency for transient failures
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/143
status: open
date opened: 2025-06-05
repo 30d_merge_rate: 13

====

description:
## Epic: Workflow Resiliency

### Problem Statement
Roast workflows, especially long-running ones, currently fail and stop execution when encountering transient issues such as:
- Network disconnections
- Temporary API unavailability
- Rate limiting
- Timeout errors

This lack of resiliency means users must restart entire workflows from scratch, losing progress and incurring additional costs for LLM API calls.

### Goals
- Make Roast workflows resilient to transient failures
- Implement intelligent retry mechanisms
- Preserve workflow progress to enable resumption
- Minimize user frustration and API costs

### Proposed Solutions

#### 1. Automatic Retry Mechanism
- Implement exponential backoff for API calls
- Configure maximum retry attempts per step
- Add jitter to prevent thundering herd
- Support retry policies in workflow configuration

#### 2. Network Resilience
- Handle connection timeouts gracefully
- Implement connection pooling and keep-alive
- Add circuit breaker pattern for repeated failures
- Support offline mode with queued operations

#### 3. Progress Persistence
- Enhance state management to checkpoint after each step
- Allow workflows to resume from last successful step
- Implement transaction-like semantics for step groups
- Add rollback capabilities for failed operations

#### 4. Error Classification
- Distinguish between transient and permanent failures
- Only retry on transient errors (network, rate limits)
- Fail fast on permanent errors (auth, validation)
- Provide clear error messages and recovery suggestions

#### 5. Configuration Options
```yaml
resiliency:
  retry:
    max_attempts: 3
    backoff: exponential
    initial_delay: 1s
    max_delay: 30s
  timeouts:
    step: 5m
    total: 1h
  checkpoint:
    enabled: true
    interval: after_each_step
```

### Success Criteria
- Workflows automatically recover from common transient failures
- Users can resume interrupted workflows without data loss
- Clear visibility into retry attempts and failure reasons
- Minimal performance impact for successful operations
- Comprehensive test coverage for failure scenarios

### Implementation Phases

**Phase 1: Basic Retry Logic**
- Add retry wrapper for API calls
- Implement exponential backoff
- Handle common HTTP errors

**Phase 2: State Persistence**
- Enhance checkpoint mechanism
- Add workflow resume capability
- Implement progress tracking

**Phase 3: Advanced Resilience**
- Circuit breaker implementation
- Offline mode support
- Sophisticated error classification

**Phase 4: Configuration & Monitoring**
- YAML configuration support
- Retry metrics and logging
- User-facing retry status

### Related Issues
- #71 (exit_on_error configuration)
- State persistence improvements
- API client enhancements

### Labels
- enhancement
- epic
- resilience
- high-priority

===
