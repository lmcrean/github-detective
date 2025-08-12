"""Collect GitHub issues and save to CSV format."""

import os
import csv
import yaml
import time
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from typing import List

# Add parent directory to path for imports
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from github_client.issue_collector import IssueCollector
from github_client.models import IssueData


def load_repositories(config_file: str = 'scripts/config/issue_collection_repos.yml') -> List[str]:
    """Load repository list from YAML configuration."""
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config['repositories']


def save_issues_to_csv(owner: str, repo: str, issues: List[IssueData], output_dir: str = 'data/repos') -> str:
    """Save issues to CSV file with metadata header."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    filename = f"{owner}_{repo}.csv"
    filepath = os.path.join(output_dir, filename)
    repo_path = f"{owner}/{repo}"
    
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        # Write metadata header as comments
        csvfile.write(f"# Issues Total: {len(issues)}\n")
        csvfile.write(f"# Repository: https://github.com/{repo_path}\n")
        csvfile.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d')}\n")
        csvfile.write("#\n")
        
        writer = csv.writer(csvfile)
        
        # Write CSV header
        writer.writerow(['issue_title', 'comments_count', 'labels', 'opened_date', 'hyperlink'])
        
        # Write issue data (sorted by most recently updated first)
        issues_sorted = sorted(issues, key=lambda x: x.updated_at, reverse=True)
        for issue in issues_sorted:
            writer.writerow(issue.to_csv_row(repo_path))
    
    return filepath


def main():
    """Main execution function."""
    load_dotenv()
    github_token = os.getenv('GITHUB_TOKEN') or os.getenv('API_GITHUB_TOKEN')
    
    print("GitHub Issues Collection to CSV")
    print("=" * 50)
    print(f"Authentication: {'Enabled' if github_token else 'Disabled (60 requests/hour limit)'}")
    print()
    
    # Load repositories from config
    try:
        repositories = load_repositories()
        print(f"Loaded {len(repositories)} repositories from config:")
        for i, repo in enumerate(repositories, 1):
            print(f"  {i:2d}. {repo}")
        print()
    except Exception as e:
        print(f"Error loading repositories: {e}")
        return
    
    # Initialize collector
    collector = IssueCollector(github_token)
    
    print("Starting issue collection...")
    print("=" * 50)
    
    start_time = time.time()
    total_issues = 0
    processed_files = []
    
    for i, repo_path in enumerate(repositories, 1):
        owner, repo = repo_path.split('/')
        print(f"Processing {i}/{len(repositories)}: {repo_path}...")
        
        try:
            # Collect issues (up to 500 most recent)
            issues = collector.collect_repository_issues(owner, repo, max_issues=500)
            
            # Save to CSV
            filepath = save_issues_to_csv(owner, repo, issues)
            processed_files.append(filepath)
            total_issues += len(issues)
            
            print(f"  -> Saved {len(issues)} issues to {filepath}")
            
        except Exception as e:
            print(f"  -> Error processing {repo_path}: {e}")
            continue
    
    end_time = time.time()
    
    print()
    print("=" * 50)
    print("Collection completed!")
    print(f"Repositories processed: {len(processed_files)}/{len(repositories)}")
    print(f"Total issues collected: {total_issues}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Output directory: data/repos/")
    print()
    print("Generated files:")
    for filepath in processed_files:
        print(f"  - {filepath}")


if __name__ == '__main__':
    main()