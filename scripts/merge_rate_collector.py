"""Base merge rate collection utility for GitHub repositories."""

import os
import csv
import time
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import pandas as pd
import sys
import requests

# Add the project root to sys.path to enable imports
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
if project_root not in sys.path:
    sys.path.append(project_root)

from scripts.github_client.client import GitHubClient
from scripts.github_client.exceptions import GitHubAPIError, RateLimitError


class MergeRateCollector:
    """Collects 30-day merge rates for GitHub repositories."""
    
    def __init__(self, progress_file: str, output_file: str):
        """
        Initialize merge rate collector.
        
        Args:
            progress_file: Path to progress tracking file
            output_file: Path to CSV output file
        """
        self.client = GitHubClient()
        self.progress_file = progress_file
        self.output_file = output_file
        self.start_date = datetime.now() - timedelta(days=30)
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        
        # Initialize output CSV with headers
        if not os.path.exists(self.output_file):
            with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['org', 'repo', 'hyperlink', '30d_merge_rate'])
    
    def get_merge_count(self, owner: str, repo: str) -> int:
        """
        Get merge count for repository in last 30 days.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            Number of merges to main branch in last 30 days
        """
        try:
            # Get commits to main branch since start_date
            url = f"{self.client.base_url}/repos/{owner}/{repo}/commits"
            params = {
                'sha': 'main',  # or 'master' - we'll try both
                'since': self.start_date.isoformat(),
                'per_page': 100
            }
            
            # Try main branch first
            response = self._make_request_with_retry(url, params)
            
            if response.status_code == 409:  # Branch doesn't exist, try master
                params['sha'] = 'master'
                response = self._make_request_with_retry(url, params)
            
            if response.status_code != 200:
                return 0
            
            commits = response.json()
            
            # Count merge commits (have more than 1 parent)
            merge_count = 0
            for commit in commits:
                if len(commit.get('parents', [])) > 1:
                    merge_count += 1
            
            return merge_count
            
        except Exception as e:
            self._log_progress(f"Error getting merge count for {owner}/{repo}: {str(e)}")
            return 0
    
    def _make_request_with_retry(self, url: str, params: Dict[str, Any], max_retries: int = 3):
        """Make request with retry logic for rate limits."""
        for attempt in range(max_retries):
            try:
                response = self.client._make_request(url, params)
                return response
            except RateLimitError as e:
                self._log_progress(f"Rate limit hit, stopping collection. Error: {str(e)}")
                raise
            except GitHubAPIError as e:
                if attempt == max_retries - 1:
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff
        
        return response
    
    def _log_progress(self, message: str):
        """Log progress to file and print to console."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {message}"
        
        print(log_message)
        with open(self.progress_file, 'a', encoding='utf-8') as f:
            f.write(log_message + '\n')
    
    def collect_from_existing_data(self, csv_file: str, company_filter: Optional[str] = None):
        """
        Collect merge rates from existing CSV with repo data.
        
        Args:
            csv_file: Path to CSV file with repo data
            company_filter: Optional company name to filter by
        """
        try:
            # Read the CSV file
            df = pd.read_csv(csv_file, sep=';')
            
            # Filter by company if specified
            if company_filter:
                df = df[df['company'] == company_filter]
            
            # Filter by recent activity (last 30 days)
            df = df[df['days_since_commit'] <= 30]
            
            self._log_progress(f"Starting collection for {len(df)} repositories" + 
                             (f" from company {company_filter}" if company_filter else ""))
            
            # Process each repository
            for idx, row in df.iterrows():
                try:
                    org = row['github_org']
                    repo = row['repo']
                    hyperlink = row['hyperlink']
                    
                    self._log_progress(f"Processing {idx+1}/{len(df)}: {org}/{repo}")
                    
                    merge_count = self.get_merge_count(org, repo)
                    
                    # Write result to CSV
                    with open(self.output_file, 'a', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerow([org, repo, hyperlink, merge_count])
                    
                    self._log_progress(f"✓ {org}/{repo}: {merge_count} merges in 30 days")
                    
                    # Small delay to be respectful to API
                    time.sleep(0.1)
                    
                except RateLimitError:
                    self._log_progress("Rate limit reached. Stopping collection gracefully.")
                    break
                except Exception as e:
                    self._log_progress(f"Error processing {org}/{repo}: {str(e)}")
                    continue
            
            self._log_progress("Collection completed successfully!")
            
        except Exception as e:
            self._log_progress(f"Error in collection: {str(e)}")
            raise
    
    def collect_from_org_list(self, csv_file: str):
        """
        Extract repos from organization list and collect merge rates.
        
        Args:
            csv_file: Path to CSV file with org data (org_repo_counts format)
        """
        try:
            # Read the org CSV file
            df = pd.read_csv(csv_file, sep=';')
            
            self._log_progress(f"Starting repo extraction for {len(df)} organizations")
            
            total_repos_processed = 0
            
            # Process each organization
            for idx, row in df.iterrows():
                try:
                    org_name = row['org']
                    github_org = row['github_org']
                    
                    self._log_progress(f"Processing org {idx+1}/{len(df)}: {org_name} ({github_org})")
                    
                    # Get all repos for this organization
                    repos = self._get_org_repos(github_org)
                    
                    # Process each repo
                    for repo_data in repos:
                        try:
                            repo_name = repo_data['name']
                            hyperlink = repo_data['html_url']
                            
                            # Check if repo was active in last 30 days
                            last_push = repo_data.get('pushed_at')
                            if last_push:
                                last_push_date = datetime.fromisoformat(last_push.replace('Z', '+00:00'))
                                days_since_push = (datetime.now(last_push_date.tzinfo) - last_push_date).days
                                
                                if days_since_push > 30:
                                    continue  # Skip inactive repos
                            
                            merge_count = self.get_merge_count(github_org, repo_name)
                            
                            # Write result to CSV
                            with open(self.output_file, 'a', newline='', encoding='utf-8') as f:
                                writer = csv.writer(f)
                                writer.writerow([github_org, repo_name, hyperlink, merge_count])
                            
                            total_repos_processed += 1
                            self._log_progress(f"  ✓ {github_org}/{repo_name}: {merge_count} merges")
                            
                            time.sleep(0.1)  # Rate limiting courtesy
                            
                        except RateLimitError:
                            self._log_progress("Rate limit reached. Stopping collection gracefully.")
                            return
                        except Exception as e:
                            self._log_progress(f"Error processing repo {repo_name}: {str(e)}")
                            continue
                    
                except RateLimitError:
                    self._log_progress("Rate limit reached. Stopping collection gracefully.")
                    break
                except Exception as e:
                    self._log_progress(f"Error processing org {org_name}: {str(e)}")
                    continue
            
            self._log_progress(f"Collection completed! Processed {total_repos_processed} repositories")
            
        except Exception as e:
            self._log_progress(f"Error in org collection: {str(e)}")
            raise
    
    def _get_org_repos(self, org: str) -> List[Dict[str, Any]]:
        """Get all repositories for an organization."""
        repos = []
        page = 1
        per_page = 100
        
        while True:
            url = f"{self.client.base_url}/orgs/{org}/repos"
            params = {
                'per_page': per_page,
                'page': page,
                'sort': 'pushed',  # Most recently pushed first
                'type': 'public'
            }
            
            response = self._make_request_with_retry(url, params)
            
            if response.status_code != 200:
                break
            
            page_repos = response.json()
            if not page_repos:
                break
            
            repos.extend(page_repos)
            page += 1
            
            # Limit to avoid excessive API calls
            if len(repos) >= 1000:  # Reasonable limit per org
                break
        
        return repos