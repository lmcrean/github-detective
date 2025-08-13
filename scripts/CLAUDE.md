# Scripts Directory - Claude Usage Guide

## Overview
This directory contains a modular Python framework for GitHub data collection, analysis, and processing. The architecture is designed to work seamlessly with Claude Code for on-demand repository analysis with clean separation of concerns.

## Modular Architecture

### Core Modules

#### 1. GitHub Client (`github_client/`)
**Purpose**: Core GitHub API interaction with authentication, rate limiting, and exception handling
**Key Components**:
- `client.py` - Main GitHub API client
- `auth.py` - Authentication handling  
- `rate_limiter.py` - API rate limit management
- `exceptions.py` - Custom exception classes
- `issue_collector.py` - Specialized issue collection
- `markdown_generator.py` - GitHub markdown processing

#### 2. Issues (`issues/`)
**Purpose**: Issue collection, analysis, and export functionality
**Key Components**:
- `collector.py` - Issue data collection
- `analyzer.py` - Issue analysis and insights
- `exporters/` - CSV and markdown export functionality
- `processors/` - Batch processing capabilities
- `analyzers/` - Specialized analysis tools

#### 3. Repositories (`repos/`)
**Purpose**: Repository analysis, filtering, and metrics
**Key Components**:
- `collector.py` - Repository data collection
- `analyzer.py` - Repository analysis and insights
- `filters/` - Activity, date, and percentile filtering
- `metrics/` - PR metrics and repository statistics
- `fixers/` - Data correction utilities

#### 4. Organizations (`orgs/`)
**Purpose**: Organization-level data collection and analysis
**Key Components**:
- `collector.py` - Organization repository collection
- `analyzer.py` - Organization-wide analysis
- `models.py` - Organization data models
- `processors/` - Batch processing for organizations
- `reports/` - Organization reporting tools

#### 5. Pipeline (`pipeline/`)
**Purpose**: Workflow orchestration for complex data processing
**Key Components**:
- `orchestrator.py` - Main pipeline orchestration
- `workflows/` - Predefined workflow templates

#### 6. Models (`models/`)
**Purpose**: Shared data models and base classes
**Key Components**:
- `github_models.py` - GitHub API data models
- `output_models.py` - Output format models
- `base.py` - Base classes and interfaces

#### 7. Utils (`utils/`)
**Purpose**: Common utilities and helper functions
**Key Components**:
- `csv_utils.py` - CSV processing utilities
- `file_utils.py` - File system operations
- `date_utils.py` - Date and time utilities
- `markdown_utils.py` - Markdown processing
- `validators.py` - Data validation functions

## Primary Entry Points

### 1. Repository Data Collection
**Script**: `run_collection.py`
**Purpose**: Main entry point for repository statistics collection
**Usage**:
```bash
python scripts/run_collection.py
```
**When to use**: When user asks for stats on specific repositories
**Prerequisites**: 
- Add repositories to `scripts/config/repositories.yml`
- Ensure `API_GITHUB_TOKEN` is set in `.env`

### 2. Pipeline Orchestration
**Script**: `pipeline/orchestrator.py`
**Purpose**: Run complete data processing pipelines
**Usage**:
```python
from scripts.pipeline.orchestrator import PipelineOrchestrator
orchestrator = PipelineOrchestrator()
orchestrator.run_workflow('repository_analysis')
```
**When to use**: When processing large datasets with multiple stages

## Programmatic Usage Examples

### Repository Collection
```python
from scripts.repos.collector import RepositoryCollector
from scripts.github_client.client import GitHubClient

client = GitHubClient()
collector = RepositoryCollector(client)
stats = collector.collect_repository_stats("facebook/react")
```

### Issue Collection
```python
from scripts.issues.collector import IssueCollector
from scripts.github_client.client import GitHubClient

client = GitHubClient()
collector = IssueCollector(client)
issues = collector.collect_repository_issues("facebook/react")
```

### Organization Analysis
```python
from scripts.orgs.collector import OrganizationCollector
from scripts.github_client.client import GitHubClient

client = GitHubClient()
collector = OrganizationCollector(client)
repos = collector.collect_org_repositories("microsoft")
```

## Data Flow

```
1. Collection Phase:
   github_client/ → Raw GitHub API data
   
2. Processing Phase:
   repos/collector.py → Repository statistics
   issues/collector.py → Issue data
   orgs/collector.py → Organization data
   
3. Filtering Phase:
   repos/filters/ → Apply date/activity/percentile filters
   
4. Analysis Phase:
   repos/analyzer.py → Repository insights
   issues/analyzer.py → Issue analysis
   orgs/analyzer.py → Organization analysis
   
5. Export Phase:
   exporters/ → CSV/Markdown output
   utils/ → File and format utilities
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

### Issue Collection Configuration
Edit `scripts/config/issue_collection_repos.yml`:
```yaml
repositories:
  - owner: facebook
    repo: react
  - owner: microsoft
    repo: typescript
```

### Environment Setup
Required in `.env` (parent directory):
```
API_GITHUB_TOKEN=your_github_token_here
```

## Common Workflows for Claude

### Workflow 1: Quick Repository Analysis
```python
from scripts.repos.collector import RepositoryCollector
from scripts.github_client.client import GitHubClient

# 1. Initialize client and collector
client = GitHubClient()
collector = RepositoryCollector(client)

# 2. Collect data for specific repositories
stats = collector.collect_multiple_repositories(['facebook/react', 'vuejs/vue'])

# 3. Export results
collector.export_to_csv(stats, 'data/output/repository_analysis.csv')
```

### Workflow 2: Organization Deep Dive
```python
from scripts.orgs.collector import OrganizationCollector
from scripts.repos.filters.activity_filter import ActivityFilter
from scripts.pipeline.orchestrator import PipelineOrchestrator

# 1. Collect organization repositories
collector = OrganizationCollector(client)
repos = collector.collect_org_repositories("microsoft")

# 2. Apply activity filtering
filter = ActivityFilter()
active_repos = filter.filter_by_pr_activity(repos)

# 3. Run analysis pipeline
orchestrator = PipelineOrchestrator()
orchestrator.process_repositories(active_repos)
```

### Workflow 3: Issue Analysis
```python
from scripts.issues.collector import IssueCollector
from scripts.issues.exporters.markdown_exporter import MarkdownExporter

# 1. Collect issues
collector = IssueCollector(client)
issues = collector.collect_repository_issues("facebook/react")

# 2. Export analysis
exporter = MarkdownExporter()
exporter.export_issue_analysis(issues, '.notes/issues/react_analysis.md')
```

## Module Import Patterns

### Core Client Setup
```python
from scripts.github_client.client import GitHubClient
from scripts.models.github_models import RepositoryStats, IssueData

# Initialize with automatic token loading
client = GitHubClient()  # Loads API_GITHUB_TOKEN from .env
```

### Collectors
```python
from scripts.repos.collector import RepositoryCollector
from scripts.issues.collector import IssueCollector  
from scripts.orgs.collector import OrganizationCollector
```

### Analyzers  
```python
from scripts.repos.analyzer import RepositoryAnalyzer
from scripts.issues.analyzer import IssueAnalyzer
from scripts.orgs.analyzer import OrganizationAnalyzer
```

### Filters and Processors
```python
from scripts.repos.filters.date_filter import DateFilter
from scripts.repos.filters.activity_filter import ActivityFilter
from scripts.repos.filters.percentile_filter import PercentileFilter
```

### Utilities
```python
from scripts.utils.csv_utils import CSVUtils
from scripts.utils.file_utils import FileUtils
from scripts.utils.date_utils import DateUtils
```

## Output Locations
- **Repository stats**: `data/output/github_repository_stats.csv`
- **Organization data**: `data/orgs/<org_name>/`
- **Issue reports**: `.notes/issues/`
- **Analysis reports**: `.notes/`
- **Pipeline outputs**: `data/pipeline/`

## Error Handling
- All modules handle GitHub API rate limits automatically via `github_client/rate_limiter.py`
- Custom exceptions defined in `github_client/exceptions.py`
- Authentication handled in `github_client/auth.py`
- Check `API_GITHUB_TOKEN` in parent directory `.env` if getting authentication errors
- Validation utilities in `utils/validators.py`

## Quick Commands Reference
```bash
# Main entry point - collect repository data
python scripts/run_collection.py

# Run pipeline orchestration
python -c "from scripts.pipeline.orchestrator import PipelineOrchestrator; PipelineOrchestrator().run_workflow('default')"

# Test GitHub client setup
python -c "from scripts.github_client.client import GitHubClient; print(GitHubClient().test_connection())"
```

## Module Development Guidelines
- All modules follow the same pattern: collector → analyzer → exporter
- Shared models in `models/` for consistent data structures
- Common utilities in `utils/` to avoid code duplication
- Configuration files in `config/` for easy modification
- Pipeline workflows in `pipeline/workflows/` for complex operations

## Important Notes
- All modules respect GitHub API rate limits automatically
- Data models ensure type safety and consistent data structures
- Pipeline orchestrator handles complex multi-stage workflows
- Modular design allows for easy extension and maintenance
- Scripts are designed for defensive use only (analysis, not exploitation)
- Always verify data accuracy for critical decisions
- API token (`API_GITHUB_TOKEN`) should be in `.env` file in parent directory