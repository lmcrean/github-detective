"""Fetch merged PRs for repositories in the last 30 days."""

import os
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class MergedPRsFetcher:
    """Fetch merged pull requests from GitHub API."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize with GitHub token."""
        self.token = token or os.getenv('GITHUB_TOKEN')
        self.headers = {'Authorization': f'token {self.token}'} if self.token else {}
        self.base_url = 'https://api.github.com'
    
    def get_merged_prs_count(self, org: str, repo: str, days: int = 30) -> int:
        """
        Get count of merged PRs in the last N days.
        
        Args:
            org: Organization name
            repo: Repository name
            days: Number of days to look back (default 30)
        
        Returns:
            Count of merged PRs
        """
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Format dates for GitHub API
        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = end_date.strftime('%Y-%m-%d')
        
        # Use GitHub search API to find merged PRs
        query = (
            f'repo:{org}/{repo} '
            f'is:pr '
            f'is:merged '
            f'merged:{start_date_str}..{end_date_str}'
        )
        
        search_url = f'{self.base_url}/search/issues'
        params = {'q': query, 'per_page': 1}  # We only need the count
        
        try:
            response = requests.get(search_url, headers=self.headers, params=params)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('total_count', 0)
            elif response.status_code == 403:
                print(f"Rate limit hit for {org}/{repo}. Returning -1")
                return -1
            else:
                print(f"Error fetching merged PRs for {org}/{repo}: {response.status_code}")
                return 0
                
        except Exception as e:
            print(f"Exception fetching merged PRs for {org}/{repo}: {str(e)}")
            return 0
    
    def get_batch_merged_prs(self, repos: List[Dict[str, str]], days: int = 30) -> Dict[str, int]:
        """
        Get merged PRs count for multiple repositories.
        
        Args:
            repos: List of dicts with 'org_name' and 'repo_name' keys
            days: Number of days to look back
        
        Returns:
            Dictionary mapping "org/repo" to merged PR count
        """
        results = {}
        
        for i, repo in enumerate(repos, 1):
            org = repo['org_name']
            repo_name = repo['repo_name']
            key = f"{org}/{repo_name}"
            
            print(f"Fetching merged PRs for {key} ({i}/{len(repos)})...")
            count = self.get_merged_prs_count(org, repo_name, days)
            results[key] = count
            
            # Small delay to avoid rate limiting
            if i % 10 == 0:
                import time
                time.sleep(1)
        
        return results


if __name__ == "__main__":
    # Test with a known repository
    fetcher = MergedPRsFetcher()
    
    # Test single repo
    count = fetcher.get_merged_prs_count("stripe", "stripe-python", 30)
    print(f"Stripe Python merged PRs (last 30 days): {count}")
    
    # Test batch
    test_repos = [
        {"org_name": "stripe", "repo_name": "stripe-python"},
        {"org_name": "stripe", "repo_name": "stripe-ruby"},
    ]
    
    results = fetcher.get_batch_merged_prs(test_repos)
    print(f"\nBatch results: {results}")