"""Script to collect GitHub issues from repositories listed in notes."""

import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from github_client.issue_collector import IssueCollector


def read_repositories_from_notes(filepath: str = ".notes/batch1.md") -> list:
    """Read repository URLs from notes file and extract owner/repo."""
    repositories = []
    
    if not os.path.exists(filepath):
        print(f"Notes file not found: {filepath}")
        return repositories
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('https://github.com/'):
            repo_path = line.replace('https://github.com/', '').strip('/')
            if '/' in repo_path:
                repositories.append(repo_path)
    
    return repositories


def main():
    """Main script to collect issues."""
    load_dotenv()
    github_token = os.getenv('GITHUB_TOKEN') or os.getenv('API_GITHUB_TOKEN')
    
    print("GitHub Issue Collector")
    print("=" * 50)
    print(f"Authentication: {'Enabled' if github_token else 'Disabled (60 requests/hour limit)'}")
    print()
    
    repositories = read_repositories_from_notes()
    
    if not repositories:
        print("No repositories found in notes file.")
        return
    
    print(f"Found {len(repositories)} repositories to process:")
    for repo in repositories:
        print(f"  - {repo}")
    print()
    
    collector = IssueCollector(github_token)
    
    print("Starting issue collection...")
    print("=" * 50)
    
    start_time = time.time()
    
    total_issues = 0
    for repo_path in repositories:
        owner, repo = repo_path.split('/')
        issues = collector.collect_repository_issues(owner, repo, max_issues=500)
        
        collector.save_issues_to_markdown(owner, repo, issues)
        total_issues += len(issues)
        
        time.sleep(1)
    
    end_time = time.time()
    
    print()
    print("=" * 50)
    print("Collection completed!")
    print(f"Total repositories processed: {len(repositories)}")
    print(f"Total issues collected: {total_issues}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Output directory: .notes/issues/")


if __name__ == '__main__':
    main()