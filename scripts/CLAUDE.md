# Scripts Directory - Claude Usage Guide

## Overview
This directory contains Python scripts for GitHub data collection, analysis, and processing. These scripts are designed to work seamlessly with Claude Code for on-demand repository analysis.

## Primary Scripts

### 1. Repository Data Collection
**Script**: `run_collection.py`
**Purpose**: Collect GitHub statistics for specified repositories
**Usage**:
```bash
python scripts/run_collection.py
```
**When to use**: When user asks for stats on specific repositories
**Prerequisites**: 
- Add repositories to `scripts/config/repositories.yml`
- Ensure `API_GITHUB_TOKEN` is set in `.env`

### 2. Issue Collection & Analysis
**Script**: `analyse/collect_issues.py`
**Purpose**: Fetch and analyze GitHub issues from repositories
**Usage**:
```bash
python scripts/analyse/collect_issues.py
```
**When to use**: When user needs issue analysis or bug tracking insights
**Output**: Markdown files in `.notes/issues/`

### 3. Organization Repository Collection
**Script**: `org-research/collect_org_repos.py`
**Purpose**: Collect all repositories from a GitHub organization
**Usage**:
```bash
python scripts/org-research/collect_org_repos.py <org_name>
```
**When to use**: When user wants to analyze an entire organization's repositories
**Output**: CSV file with all org repositories

### 4. Data Processing Pipeline
**Script**: `orchestrator.py`
**Purpose**: Run complete filtering pipeline on collected data
**Usage**:
```bash
python scripts/orchestrator.py
```
**When to use**: When processing large datasets with multiple filters
**Filters applied**:
- Date-based filtering
- PR activity filtering  
- Top percentile selection

## Specialized Tools

### CSV Operations
- **`combine/csv_combiner.py`**: Merge multiple CSV files
- **`analyse/analyze_csv_issues.py`**: Analyze issues in CSV data

### Data Fixing Scripts
Located in `fix/` directory:
- **`fix_csv_counts.py`**: Correct count discrepancies
- **`fix_github_counts_accurate.py`**: Accurate GitHub API count fixes
- **`fix_pr_counts.py`**: Fix PR count issues
- **`targeted_fix.py`**: Apply targeted fixes to specific data issues

### Filtering Scripts
Located in `filters/` directory:
- **`filter_by_date.py`**: Filter repos by date ranges
- **`filter_by_pr_activity.py`**: Filter by PR activity levels
- **`filter_top_percentile.py`**: Get top performing repositories

### PR Metrics
Located in `merged_prs_30d/` directory:
- **`fetch_merged_prs.py`**: Get merged PRs from last 30 days
- **`add_pr_column.py`**: Add PR metrics to existing data
- **`batch_processor.py`**: Process multiple organizations

## Debug Tools
Located in `debug/` directory:
- **`test_api_with_token.py`**: Verify GitHub API token
- **`debug_shopify_api.py`**: Debug API issues

## Data Flow

```
1. Collection Phase:
   run_collection.py → data/output/github_repository_stats.csv
   
2. Enhancement Phase:
   merged_prs_30d/add_pr_column.py → Adds PR metrics
   
3. Filtering Phase:
   filters/*.py → Apply various filters
   
4. Analysis Phase:
   analyse/*.py → Generate insights and reports
```

## Configuration

### Repository Configuration
Edit `scripts/config/repositories.yml`:
```yaml
repositories:
  - facebook/react
  - vuejs/vue
  - angular/angular
```

### Environment Setup
Required in `.env`:
```
API_GITHUB_TOKEN=your_github_token_here
```

## Common Workflows for Claude

### Workflow 1: Quick Repository Analysis
```bash
# 1. Update config
# Edit scripts/config/repositories.yml

# 2. Collect data
python scripts/run_collection.py

# 3. Analyze output
# Read data/output/github_repository_stats.csv
```

### Workflow 2: Organization Deep Dive
```bash
# 1. Collect org repos
python scripts/org-research/collect_org_repos.py microsoft

# 2. Add PR metrics
python scripts/merged_prs_30d/add_pr_column.py

# 3. Apply filters
python scripts/orchestrator.py
```

### Workflow 3: Issue Analysis
```bash
# 1. Collect issues
python scripts/analyse/collect_issues.py

# 2. Results in .notes/issues/
```

## Output Locations
- **Repository stats**: `data/output/github_repository_stats.csv`
- **Organization data**: `data/orgs/<org_name>/`
- **Issue reports**: `.notes/issues/`
- **Analysis reports**: `.notes/`

## Error Handling
- Scripts handle GitHub API rate limits automatically
- Check `API_GITHUB_TOKEN` if getting authentication errors -- it's in parent dir from here under .env
- Use debug scripts in `debug/` for troubleshooting

## Quick Commands Reference
```bash
# Collect repository data
python scripts/run_collection.py

# Collect organization repos
python scripts/org-research/collect_org_repos.py <org>

# Collect issues
python scripts/analyse/collect_issues.py

# Run full pipeline
python scripts/orchestrator.py

# Test API token
python scripts/debug/test_api_with_token.py

# Combine CSV files
python scripts/combine/csv_combiner.py file1.csv file2.csv

# Add PR metrics
python scripts/merged_prs_30d/add_pr_column.py

# Apply date filter
python scripts/filters/filter_by_date.py input.csv

# Get top percentile
python scripts/filters/filter_top_percentile.py input.csv
```

## Important Notes
- All scripts respect GitHub API rate limits
- Data is cached locally - check timestamps before re-collecting
- Scripts are designed for defensive use only (analysis, not exploitation)
- Always verify data accuracy for critical decisions
- be aware of how to access .env API_GITHUB_TOKEN in parent dir from here