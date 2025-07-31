# github-library
A library of Major Players on Github, with a focus on Artificial Intelligence sectors with KPI statistics

A standalone tool for collecting and analyzing GitHub repository statistics.

## Features

- Collect repository statistics (stars, forks, contributors, issues, PRs)
- Support for rate limiting and authentication
- Export data to CSV format
- Language breakdown analysis
- Automated data collection via GitHub Actions

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure repositories in `src/config/repositories.yml`

3. Set GitHub token (optional but recommended):
   ```bash
   export GITHUB_TOKEN=your_token_here
   ```

## Usage

### Manual Collection
```bash
python scripts/run_collection.py
```

### Running Tests
```bash
python -m pytest tests/ -v
```

## Data Output

- CSV data: `data/output/github_repository_stats.csv`
- Metadata: `data/output/github_stats_metadata.json`

## Configuration

Edit `src/config/repositories.yml` to specify which repositories to track:

```yaml
repositories:
  AI/ML:
    - tensorflow/tensorflow
    - pytorch/pytorch
  TypeScript:
    - nestjs/nest
    - prisma/prisma
```

## Automated Collection

GitHub Actions workflow runs weekly and on pushes to collect fresh data automatically.