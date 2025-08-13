issue title: Generate self-contained HTML run reports with cloud storage upload
labels: brainstorm, epic/cost-observability
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/236
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 13

====

description:
## Summary
Create a self-contained HTML file that captures the complete workflow execution, including visual representation, logs, metrics, and timing, that can be uploaded to cloud storage (GCS/S3) with a shareable URL displayed in the terminal.

## Acceptance Criteria
- [ ] Generate a single HTML file containing all workflow run data (no external dependencies)
- [ ] Include visual DAG representation of the workflow with execution status
- [ ] Embed all logs, outputs, and error messages
- [ ] Show timing information and token usage per step
- [ ] Include cost breakdown and total cost
- [ ] Support automatic upload to GCS and S3 buckets
- [ ] Display shareable URL in terminal after successful upload
- [ ] Make upload optional via CLI flag (--upload-report)

## Technical Details
- Use inline CSS and JavaScript (no CDN dependencies)
- Embed workflow visualization using SVG
- Include collapsible sections for logs per step
- Support syntax highlighting for code outputs
- Generate unique filenames with timestamp and workflow name
- Use cloud SDKs for GCS/S3 upload
- Support bucket configuration via environment variables or config file

## Benefits
- Permanent record of workflow executions
- Easy sharing with team members
- Visual debugging of complex workflows
- Audit trail for compliance
- No need for separate logging infrastructure

**Labels:** brainstorm, epic/cost-observability
**Epic:** Cost Management & Observability

===
