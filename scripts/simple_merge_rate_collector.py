"""Standalone merge rate collection utility for GitHub repositories."""

import os
import csv
import time
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class SimpleMergeRateCollector:
    """Collects 30-day merge rates for GitHub repositories using direct API calls."""
    
    def __init__(self, progress_file: str, output_file: str):
        """
        Initialize merge rate collector.
        
        Args:
            progress_file: Path to progress tracking file
            output_file: Path to CSV output file
        """
        # Load GitHub token from environment
        self.token = os.getenv('API_GITHUB_TOKEN')
        self.headers = {
            'Authorization': f'token {self.token}' if self.token else '',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        self.progress_file = progress_file
        self.output_file = output_file
        self.start_date = datetime.now() - timedelta(days=30)
        self.base_url = 'https://api.github.com'
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        
        # Initialize output CSV with headers
        if not os.path.exists(self.output_file):
            with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['org', 'repo', 'hyperlink', 'commits_last_30d', 'PRs_closed_30d'])
    
    def get_repo_metrics(self, owner: str, repo: str) -> tuple[int, int]:
        """
        Get repository health metrics for last 30 days.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            Tuple of (commits_last_30d, PRs_closed_30d)
        """
        commits_count = 0
        prs_closed_count = 0
        
        try:
            # Get commits to main branch since start_date
            commits_url = f"{self.base_url}/repos/{owner}/{repo}/commits"
            commits_params = {
                'sha': 'main',
                'since': self.start_date.isoformat(),
                'per_page': 100
            }
            
            # Try main branch first
            response = requests.get(commits_url, headers=self.headers, params=commits_params)
            
            # Handle rate limiting
            if response.status_code == 403 and 'rate limit' in response.text.lower():
                self._log_progress("Rate limit hit, stopping collection")
                raise Exception("Rate limit exceeded")
            
            if response.status_code == 409:  # Branch doesn't exist, try master
                commits_params['sha'] = 'master'
                response = requests.get(commits_url, headers=self.headers, params=commits_params)
            
            if response.status_code == 200:
                commits = response.json()
                commits_count = len(commits)  # Count all commits, not just merges
            
            # Get closed PRs in last 30 days
            prs_url = f"{self.base_url}/repos/{owner}/{repo}/pulls"
            prs_params = {
                'state': 'closed',
                'since': self.start_date.isoformat(),
                'per_page': 100
            }
            
            response = requests.get(prs_url, headers=self.headers, params=prs_params)
            
            # Handle rate limiting
            if response.status_code == 403 and 'rate limit' in response.text.lower():
                self._log_progress("Rate limit hit, stopping collection")
                raise Exception("Rate limit exceeded")
            
            if response.status_code == 200:
                prs = response.json()
                # Count PRs that were actually merged (not just closed)
                prs_closed_count = len([pr for pr in prs if pr.get('merged_at')])
            
            return commits_count, prs_closed_count
            
        except Exception as e:
            self._log_progress(f"Error getting metrics for {owner}/{repo}: {str(e)}")
            if "rate limit" in str(e).lower():
                raise
            return 0, 0
    
    def _log_progress(self, message: str):
        """Log progress to file and print to console."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Replace checkmark with OK for Windows compatibility
        safe_message = message.replace('✓', 'OK')
        log_message = f"[{timestamp}] {safe_message}"
        
        print(log_message)
        try:
            with open(self.progress_file, 'a', encoding='utf-8') as f:
                f.write(log_message + '\n')
        except UnicodeEncodeError:
            # Fallback to ascii if utf-8 fails
            with open(self.progress_file, 'a', encoding='ascii', errors='replace') as f:
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
                    
                    commits_count, prs_closed_count = self.get_repo_metrics(org, repo)
                    
                    # Write result to CSV
                    with open(self.output_file, 'a', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerow([org, repo, hyperlink, commits_count, prs_closed_count])
                    
                    self._log_progress(f"OK {org}/{repo}: {commits_count} commits, {prs_closed_count} PRs merged in 30 days")
                    
                    # Small delay to be respectful to API
                    time.sleep(0.1)
                    
                except Exception as e:
                    if "rate limit" in str(e).lower():
                        self._log_progress("Rate limit reached. Waiting 1 hour before retrying...")
                        time.sleep(3600)  # Wait 1 hour (3600 seconds)
                        self._log_progress("Resuming collection after 1 hour wait")
                        try:
                            commits_count, prs_closed_count = self.get_repo_metrics(org, repo)
                            with open(self.output_file, 'a', newline='', encoding='utf-8') as f:
                                writer = csv.writer(f)
                                writer.writerow([org, repo, hyperlink, commits_count, prs_closed_count])
                            self._log_progress(f"OK {org}/{repo}: {commits_count} commits, {prs_closed_count} PRs merged in 30 days")
                        except Exception as retry_e:
                            self._log_progress(f"Retry failed for {org}/{repo}: {str(retry_e)}")
                            break
                    else:
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
                            
                            commits_count, prs_closed_count = self.get_repo_metrics(github_org, repo_name)
                            
                            # Write result to CSV
                            with open(self.output_file, 'a', newline='', encoding='utf-8') as f:
                                writer = csv.writer(f)
                                writer.writerow([github_org, repo_name, hyperlink, commits_count, prs_closed_count])
                            
                            total_repos_processed += 1
                            self._log_progress(f"  OK {github_org}/{repo_name}: {commits_count} commits, {prs_closed_count} PRs")
                            
                            time.sleep(0.1)  # Rate limiting courtesy
                            
                        except Exception as e:
                            if "rate limit" in str(e).lower():
                                self._log_progress("Rate limit reached. Waiting 1 hour before retrying...")
                                time.sleep(3600)  # Wait 1 hour
                                self._log_progress("Resuming collection after 1 hour wait")
                                try:
                                    commits_count, prs_closed_count = self.get_repo_metrics(github_org, repo_name)
                                    with open(self.output_file, 'a', newline='', encoding='utf-8') as f:
                                        writer = csv.writer(f)
                                        writer.writerow([github_org, repo_name, hyperlink, commits_count, prs_closed_count])
                                    total_repos_processed += 1
                                    self._log_progress(f"  OK {github_org}/{repo_name}: {commits_count} commits, {prs_closed_count} PRs")
                                except Exception as retry_e:
                                    self._log_progress(f"Retry failed for {github_org}/{repo_name}: {str(retry_e)}")
                                    return
                            else:
                                self._log_progress(f"Error processing repo {repo_name}: {str(e)}")
                                continue
                    
                except Exception as e:
                    if "rate limit" in str(e).lower():
                        self._log_progress("Rate limit reached. Stopping collection gracefully.")
                        break
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
            url = f"{self.base_url}/orgs/{org}/repos"
            params = {
                'per_page': per_page,
                'page': page,
                'sort': 'pushed',  # Most recently pushed first
                'type': 'public'
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            
            # Handle rate limiting
            if response.status_code == 403 and 'rate limit' in response.text.lower():
                raise Exception("Rate limit exceeded")
            
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