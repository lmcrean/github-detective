# Scripts Directory

This directory contains essential scripts for GitHub repository data collection, processing, and analysis.

## Core Scripts

### `run_collection.py`
**Primary entry point for GitHub repository data collection**
- Main script referenced in CLAUDE.md
- Collects stats for repositories configured in `src/config/repositories.yml`
- Outputs data to `data/output/github_repository_stats.csv`

Usage:
```bash
python scripts/run_collection.py
```

### `orchestrator.py`
**Pipeline orchestrator for batch data processing**
- Manages complete filtering pipeline for organization data
- Applies date filters, PR activity filters, and percentile filters
- Processes multiple organizations through standardized workflow

Usage:
```bash
python scripts/orchestrator.py
```

### `collect_issues.py`
**GitHub issues collection tool**
- Extracts repository URLs from `.notes/` files
- Fetches GitHub issues data via API
- Saves results as markdown files in `.notes/issues/`

Usage:
```bash
python scripts/collect_issues.py
```

## Subdirectories

### `filters/`
Contains reusable filtering modules:
- `filter_by_date.py` - Date-based repository filtering
- `filter_by_pr_activity.py` - PR activity filtering
- `filter_top_percentile.py` - Top percentile selection

### `org-research/`
Organization-wide data collection tools:
- `collect_org_repos.py` - Collect all repositories from GitHub organizations
- `models.py` - Data models for organization repository data

### `merged_prs_30d/`
PR metrics collection and processing:
- `fetch_merged_prs.py` - Core PR data fetching from GitHub API
- `add_pr_column.py` - Add merged PR counts to existing CSV data
- `batch_processor.py` - Batch processing for multiple organizations

## Architecture

```
scripts/
├── README.md              # This documentation
├── run_collection.py      # Main entry point (Claude Code integration)
├── orchestrator.py        # Pipeline orchestrator
├── collect_issues.py      # Issues collection
├── filters/              # Reusable filtering modules
├── org-research/         # Organization data collection
└── merged_prs_30d/       # PR metrics processing
```

## Dependencies

All scripts require:
- Python 3.7+
- Dependencies from `requirements.txt`
- GitHub API token in environment (`GITHUB_TOKEN` or `API_GITHUB_TOKEN`)

## Integration with Claude Code

These scripts are designed to be called by Claude during interactive sessions:

1. **Repository Analysis**: Use `run_collection.py` for specific repos
2. **Organization Research**: Use `org-research/collect_org_repos.py` for org-wide analysis  
3. **Issue Analysis**: Use `collect_issues.py` for issue-based insights
4. **Data Processing**: Use `orchestrator.py` for complex filtering pipelines

All analysis results should be saved to `.notes/` directory for organization and future reference.