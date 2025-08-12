# GitHub Library - Claude Code Extension

## Project Overview
A GitHub statistics collection tool designed to work as an extension of Claude Code. This allows Claude to collect and analyze GitHub repository data on demand during interactions, providing real-time insights about any repository requested by the user.

## How Claude Should Use This Tool

### Collecting Data for Specific Repositories
When a user asks for GitHub statistics about specific repositories:

1. **Add repositories to configuration**: 
   - Edit `scripts/config/repositories.yml` to add the requested repositories
   - Use format: `owner/repo` (e.g., `facebook/react`)

2. **Run data collection**:
   ```bash
   python scripts/run_collection.py
   ```

3. **Access the collected data**:
   - CSV output: `data/output/github_repository_stats.csv`
   - JSON metadata: `data/output/github_stats_metadata.json`

4. **Save analysis and findings**:
   - Create `.notes/` directory if it doesn't exist
   - Save all analysis, findings, and reports as markdown files in `.notes/`
   - Use descriptive filenames like `.notes/react-analysis-2025-08-11.md`
   - This keeps findings organized and separate from the codebase

### Quick Repository Data Collection
For ad-hoc repository analysis:
```python
# Example: Collect data for a single repository
from scripts.github_client.client import GitHubClient
client = GitHubClient()
stats = client.get_repository_stats("owner/repo")
```

## Key Files & Structure
- `scripts/github_client/` - Core GitHub API client and data collection logic see `.env` in the root
- `.env` uses API_GITHUB_TOKEN 
- `scripts/config/repositories.yml` - Repository configuration (dynamically updated)
- `scripts/run_collection.py` - Main entry point for batch data collection
- `data/output/` - CSV and JSON output files with collected statistics
- `tests/` - Unit and integration tests
- `requirements.txt` - Python dependencies

## Available Data Points
The tool collects:
- Stars, forks, watchers
- Open/closed issues and PRs
- Contributor count
- Repository metadata (language, creation date, last update)
- License information
- Topics/tags

## Commands for Claude
- **Collect data for configured repos**: `python scripts/run_collection.py`
- **Run tests**: `python -m pytest tests/ -v`
- **Install dependencies**: `pip install -r requirements.txt`

## Usage Examples

### Example 1: User asks for stats on AI/ML repositories
1. Add requested repos to `scripts/config/repositories.yml`
2. Run `python scripts/run_collection.py`
3. Read and analyze the CSV output to provide insights

### Example 2: User wants trending Python projects
1. Update configuration with trending Python repos
2. Collect data
3. Sort by stars/recent activity to identify trends

### Example 3: Compare multiple frameworks
1. Add framework repositories to configuration
2. Run collection
3. Generate comparative analysis from the data

## Environment Setup
- Ensure `GITHUB_TOKEN` is set for better API rate limits (60 requests/hour without, 5000 with token)
- All dependencies should be installed via `pip install -r requirements.txt`

## Important Notes
- Always check API rate limits before large collections
- Data is cached in output files - check timestamps before re-collecting
- The tool respects GitHub's API guidelines and rate limits automatically

# prompt guide

- `notes` refers to any files in `./notes`