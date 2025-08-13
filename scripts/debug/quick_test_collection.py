"""Quick test to collect issues from a few repositories."""

import os
import sys
import time
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from scripts.github_client.issue_collector import IssueCollector
from scripts.collect_issues_to_csv import save_issues_to_csv

def main():
    """Test collection from a few repos."""
    load_dotenv()
    github_token = os.getenv('API_GITHUB_TOKEN')
    
    print(f"Quick test collection - Auth: {'Enabled' if github_token else 'Disabled'}")
    
    # Just test with a couple of repos
    test_repos = [
        'shopify/flash-list',
        'stripe/stripe-go'
    ]
    
    collector = IssueCollector(github_token)
    
    for repo_path in test_repos:
        owner, repo = repo_path.split('/')
        print(f"Collecting from {repo_path}...")
        
        try:
            issues = collector.collect_repository_issues(owner, repo, max_issues=50)
            filepath = save_issues_to_csv(owner, repo, issues)
            print(f"  -> Saved {len(issues)} issues to {filepath}")
        except Exception as e:
            print(f"  -> Error: {e}")

if __name__ == '__main__':
    main()