issue title: Add wait_for_event step type for external event synchronization
labels: enhancement, epic/developer-experience
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/251
status: open
date opened: 2025-06-12
repo 30d_merge_rate: 13

====

description:
## Summary

Add a new `wait_for_event` step type that pauses workflow execution until an external event is received via the CLI. This enables workflows to wait for human approval, external system notifications, or other asynchronous triggers.

## Design

### Step Declaration

The `wait_for_event` step uses a hash where keys are event identifiers and values are workflow sequences to execute when that event is triggered:

```yaml
steps:
  - process_data
  - wait_for_event:
      approved:
        - "Changes have been approved\!"
        - notify_team
        - deploy_to_production
      rejected:
        - log_rejection
        - email_author  
        - "Changes rejected, please revise"
      escalated:
        - alert_manager
        - create_incident
  - cleanup_resources
```

### Configuration

Optional timeout and other settings follow Roast's standard configuration pattern:

```yaml
steps:
  - wait_for_event:
      approved:
        - continue_deployment
      rejected:
        - rollback_changes

wait_for_event:
  timeout: 30m  # Optional timeout duration
  on_timeout:   # Optional workflow to run on timeout
    - "Approval timed out after 30 minutes"
    - notify_timeout
```

### CLI Commands

Resume a paused workflow with an event:

```bash
# Initial execution pauses at wait_for_event
roast execute workflow.yml

# Resume with event (uses most recent session)
roast resume workflow.yml --event approved

# Resume specific session
roast resume workflow.yml --session-id abc123 --event approved
```

## Implementation Notes

1. **Session State**: Leverage existing replay/session infrastructure to persist workflow state
2. **Event Validation**: Only accept events defined in the wait_for_event hash
3. **Workflow Continuation**: After event steps complete, continue with remaining workflow steps
4. **Multiple Wait States**: Support multiple wait_for_event steps in a single workflow
5. **State Storage**: Automatically persist state when reaching a wait_for_event step

## Use Cases

- **Approval Workflows**: Wait for human approval before proceeding with deployments
- **External System Integration**: Pause until webhook or callback is received  
- **Multi-Stage Pipelines**: Coordinate between different systems or teams
- **Quality Gates**: Wait for external validation before continuing

## Example: Deployment Approval Workflow

```yaml
name: deploy_with_approval
description: Deploy application with manual approval gate

steps:
  - run_tests
  - build_application
  - deploy_to_staging
  - run_smoke_tests
  - wait_for_event:
      approved:
        - "Deployment approved by {{event.approver}}"
        - deploy_to_production
        - notify_success
      rejected:
        - "Deployment rejected by {{event.approver}}"
        - rollback_staging
        - notify_rejection
      timeout:
        - "Approval timeout after 2 hours"
        - rollback_staging
        - alert_on_call

wait_for_event:
  timeout: 2h

# ... rest of step definitions ...
```

## Technical Considerations

- Event data could be passed as JSON: `--event-data '{"approver": "john.doe"}'`
- Consider adding event webhooks in future iterations
- State files should be cleaned up after successful completion
- Add `roast sessions` command to list active wait states

===
