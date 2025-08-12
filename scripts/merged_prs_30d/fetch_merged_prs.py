"""Fetch merged PRs for repositories in the last 30 days."""

import os
import requests
import time
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional

try:
    from dotenv import load_dotenv
    load_dotenv()  # Load environment variables from .env file
except ImportError:
    pass  # python-dotenv not installed, continue without it


class MergedPRsFetcher:
    """Fetch merged pull requests from GitHub API."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize with GitHub token."""
        self.token = token or os.getenv('API_GITHUB_TOKEN') or os.getenv('GITHUB_TOKEN')
        self.headers = {'Authorization': f'token {self.token}'} if self.token else {}
        self.base_url = 'https://api.github.com'
        
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        if not self.token:
            self.logger.warning("No GitHub token found. API requests will be limited.")
    
    def _make_request_with_retry(self, url: str, params: Dict, max_retries: int = 3) -> Optional[requests.Response]:
        """
        Make HTTP request with exponential backoff retry logic.
        
        Args:
            url: API endpoint URL
            params: Query parameters
            max_retries: Maximum number of retry attempts
        
        Returns:
            Response object or None if all retries failed
        """
        for attempt in range(max_retries + 1):
            try:
                response = requests.get(url, headers=self.headers, params=params)
                
                if response.status_code == 200:
                    return response
                elif response.status_code == 403:
                    # Check if it's rate limiting
                    if 'rate limit' in response.text.lower() or 'api rate limit' in response.text.lower():
                        if attempt < max_retries:
                            wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                            self.logger.warning(f"Rate limit hit. Waiting {wait_time}s before retry {attempt + 1}/{max_retries}")
                            time.sleep(wait_time)
                            continue
                        else:
                            self.logger.error(f"Rate limit exceeded after {max_retries} retries")
                            return None
                    else:
                        self.logger.error(f"Access forbidden (403). Check token permissions.")
                        return None
                elif response.status_code == 422:
                    self.logger.error(f"Unprocessable entity (422). Check query syntax.")
                    return None
                else:
                    if attempt < max_retries:
                        wait_time = 1 + attempt
                        self.logger.warning(f"HTTP {response.status_code}. Retrying in {wait_time}s...")
                        time.sleep(wait_time)
                        continue
                    else:
                        self.logger.error(f"Request failed with status {response.status_code} after {max_retries} retries")
                        return None
                        
            except Exception as e:
                if attempt < max_retries:
                    wait_time = 1 + attempt
                    self.logger.warning(f"Request exception: {str(e)}. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                else:
                    self.logger.error(f"Request failed with exception: {str(e)}")
                    return None
        
        return None
    
    def get_merged_prs_count(self, org: str, repo: str, days: int = 30) -> int:
        """
        Get count of merged PRs in the last N days.
        
        Args:
            org: Organization name
            repo: Repository name
            days: Number of days to look back (default 30)
        
        Returns:
            Count of merged PRs, or -1 if failed after retries
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
        
        self.logger.info(f"Fetching merged PRs for {org}/{repo} (last {days} days)")
        
        response = self._make_request_with_retry(search_url, params)
        
        if response:
            try:
                data = response.json()
                count = data.get('total_count', 0)
                self.logger.info(f"Found {count} merged PRs for {org}/{repo}")
                return count
            except Exception as e:
                self.logger.error(f"Failed to parse response for {org}/{repo}: {str(e)}")
                return -1
        else:
            self.logger.error(f"Failed to fetch merged PRs for {org}/{repo} after retries")
            return -1
    
    def get_batch_merged_prs(self, repos: List[Dict[str, str]], days: int = 30, batch_size: int = 5, batch_delay: int = 10) -> Dict[str, int]:
        """
        Get merged PRs count for multiple repositories with improved rate limiting.
        
        Args:
            repos: List of dicts with 'org_name' and 'repo_name' keys
            days: Number of days to look back
            batch_size: Number of repos to process before taking a break
            batch_delay: Seconds to wait between batches
        
        Returns:
            Dictionary mapping "org/repo" to merged PR count
        """
        results = {}
        failed_repos = []
        
        self.logger.info(f"Starting batch processing for {len(repos)} repositories")
        self.logger.info(f"Batch size: {batch_size}, batch delay: {batch_delay}s")
        
        for i, repo in enumerate(repos, 1):
            org = repo['org_name']
            repo_name = repo['repo_name']
            key = f"{org}/{repo_name}"
            
            self.logger.info(f"Processing {key} ({i}/{len(repos)})")
            count = self.get_merged_prs_count(org, repo_name, days)
            results[key] = count
            
            if count == -1:
                failed_repos.append(key)
            
            # Delay between requests to be gentle on API
            if i < len(repos):  # Don't sleep after the last request
                time.sleep(2)  # 2 seconds between each request
            
            # Longer delay every batch_size requests
            if i % batch_size == 0 and i < len(repos):
                self.logger.info(f"Completed batch. Taking {batch_delay}s break...")
                time.sleep(batch_delay)
        
        self.logger.info(f"Batch processing complete. Success: {len(repos) - len(failed_repos)}, Failed: {len(failed_repos)}")
        if failed_repos:
            self.logger.warning(f"Failed repositories: {failed_repos[:5]}{'...' if len(failed_repos) > 5 else ''}")
        
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