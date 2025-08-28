"""Collect and filter FTSE-250 organization repositories by recent activity with health metrics."""

import os
import sys
import csv
import logging
import time
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dotenv import load_dotenv
import requests

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.github_client.client import GitHubClient

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FTSE250ActiveReposCollector:
    """Collect active repositories from FTSE-250 organizations with health metrics."""
    
    def __init__(self, days_threshold: int = 30):
        """
        Initialize collector.
        
        Args:
            days_threshold: Number of days to consider a repo as active (default 30)
        """
        self.github_client = GitHubClient()
        self.days_threshold = days_threshold
        self.input_file = Path(__file__).parent.parent / 'data' / 'orgs' / 'index' / 'pull' / 'ftse-250-github-chec.csv'
        self.output_file = Path(__file__).parent.parent / 'data' / 'repos' / 'batch_Aug28' / 'ftse250_active_repos_sorted_by_health.csv'
        self.results = []
        self.github_token = os.getenv('API_GITHUB_TOKEN') or os.getenv('GITHUB_TOKEN')
        
        if not self.github_token:
            logger.warning("No GitHub token found. API rate limits will be restricted.")
            
    def parse_org_from_url(self, github_url: str) -> Optional[str]:
        """Extract organization name from GitHub URL."""
        if not github_url or github_url == 'no github presence':
            return None
        
        # Remove trailing spaces and slashes
        github_url = github_url.strip().rstrip('/')
        
        # Extract org name from URL
        if 'github.com/' in github_url:
            parts = github_url.split('github.com/')
            if len(parts) > 1:
                org_name = parts[1].strip('/')
                # Handle potential trailing paths
                if '/' in org_name:
                    org_name = org_name.split('/')[0]
                return org_name
        
        return None
    
    def calculate_days_since(self, date_str: str) -> int:
        """Calculate days since a given date."""
        if not date_str:
            return -1
        
        try:
            # Parse ISO format date
            date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            now = datetime.now(date.tzinfo)
            delta = now - date
            return delta.days
        except Exception as e:
            logger.warning(f"Error parsing date {date_str}: {str(e)}")
            return -1
    
    def get_commit_and_merge_stats(self, org: str, repo: str, days: int = 30) -> tuple:
        """Get commit and merge count for the last N days using GitHub API."""
        try:
            # Prepare headers
            headers = {'Accept': 'application/vnd.github.v3+json'}
            if self.github_token:
                headers['Authorization'] = f'token {self.github_token}'
            
            # Calculate since date
            since_date = (datetime.now() - timedelta(days=days)).isoformat()
            
            # Get commits from last 30 days
            commits_url = f"https://api.github.com/repos/{org}/{repo}/commits"
            params = {
                'since': since_date,
                'per_page': 100
            }
            
            all_commits = []
            page = 1
            
            while True:
                params['page'] = page
                response = requests.get(commits_url, headers=headers, params=params)
                
                if response.status_code == 404:
                    logger.debug(f"Repository {org}/{repo} not found (404)")
                    return 0, 0
                elif response.status_code == 403:
                    logger.debug(f"Access denied to {org}/{repo} (403)")
                    return 0, 0
                elif response.status_code != 200:
                    logger.debug(f"API error for {org}/{repo}: {response.status_code}")
                    return 0, 0
                
                commits = response.json()
                
                if not commits:
                    break
                    
                all_commits.extend(commits)
                
                # Check if there are more pages
                if len(commits) < 100:
                    break
                
                page += 1
                
                # Rate limiting protection
                time.sleep(0.1)
            
            total_commits = len(all_commits)
            
            # Count merge commits (commits with more than one parent)
            merges = sum(1 for commit in all_commits 
                        if 'parents' in commit and len(commit.get('parents', [])) > 1)
            
            return total_commits, merges
            
        except requests.exceptions.RequestException as e:
            logger.debug(f"Network error for {org}/{repo}: {e}")
            return 0, 0
        except Exception as e:
            logger.debug(f"Error fetching data for {org}/{repo}: {e}")
            return 0, 0
    
    def get_org_repositories_filtered(self, org_name: str) -> List[Dict]:
        """Get repositories for an organization filtered by recent activity with health metrics."""
        logger.info(f"Fetching repositories for {org_name}...")
        
        try:
            repos_data = self.github_client.get_org_repositories(org_name)
            
            if not repos_data:
                logger.warning(f"No repositories found for {org_name}")
                return []
            
            logger.info(f"Found {len(repos_data)} total repositories for {org_name}")
            
            # Filter repositories by recent activity
            filtered_repos = []
            active_count = 0
            
            for repo in repos_data:
                # Skip forks and archived repos
                if repo.get('fork', False) or repo.get('archived', False):
                    continue
                
                # Check last commit date (pushed_at)
                pushed_at = repo.get('pushed_at', '')
                days_since_commit = self.calculate_days_since(pushed_at)
                
                # Filter by threshold
                if days_since_commit >= 0 and days_since_commit <= self.days_threshold:
                    repo_name = repo.get('name', '')
                    
                    # Get commit and merge stats
                    logger.debug(f"  Getting activity metrics for {org_name}/{repo_name}")
                    commits, merges = self.get_commit_and_merge_stats(org_name, repo_name, self.days_threshold)
                    
                    # Calculate health score
                    health_score = (commits + merges) / 2
                    
                    repo_info = {
                        'org': org_name,
                        'repo': repo_name,
                        'github_repo_url': f"https://github.com/{org_name}/{repo_name}",
                        'last_committed': pushed_at[:10] if pushed_at else '',  # Extract date part
                        'days_since_commit': days_since_commit,
                        'stars': repo.get('stargazers_count', 0),
                        'language': repo.get('language', '') or 'None',
                        'commits_last_30d': commits,
                        'merges_last_30d': merges,
                        'repo_health_score': health_score
                    }
                    filtered_repos.append(repo_info)
                    active_count += 1
                    
                    # Rate limiting
                    time.sleep(0.5)
            
            logger.info(f"Found {active_count} active repositories (last {self.days_threshold} days) for {org_name}")
            return filtered_repos
            
        except Exception as e:
            logger.error(f"Error fetching repositories for {org_name}: {str(e)}")
            return []
    
    def collect_all_organizations(self):
        """Process all organizations from the FTSE-250 CSV."""
        logger.info(f"Reading organizations from {self.input_file}")
        
        if not self.input_file.exists():
            logger.error(f"Input file not found: {self.input_file}")
            return
        
        # Read FTSE-250 organizations
        orgs_to_process = []
        with open(self.input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                github_url = row.get('GitHub URL', '')
                if github_url and github_url != 'no github presence':
                    org_name = self.parse_org_from_url(github_url)
                    if org_name:
                        org_info = {
                            'company': row.get('Organization Name', ''),
                            'org_name': org_name,
                            'url': github_url
                        }
                        orgs_to_process.append(org_info)
        
        logger.info(f"Found {len(orgs_to_process)} organizations with GitHub presence")
        
        # Collect repositories for each organization
        for i, org_info in enumerate(orgs_to_process, 1):
            logger.info(f"\n[{i}/{len(orgs_to_process)}] Processing {org_info['company']} ({org_info['org_name']})")
            
            repos = self.get_org_repositories_filtered(org_info['org_name'])
            self.results.extend(repos)
            
            logger.info(f"Total active repositories collected so far: {len(self.results)}")
    
    def save_results(self):
        """Save results to CSV file sorted by health score."""
        if not self.results:
            logger.warning("No active repositories found to save")
            return
        
        # Ensure output directory exists
        self.output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Sort results by health score (descending), then by org and repo name
        self.results.sort(key=lambda x: (-x['repo_health_score'], x['org'], x['repo']))
        
        # Save to CSV
        logger.info(f"Saving {len(self.results)} repositories to {self.output_file}")
        
        with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['org', 'repo', 'github_repo_url', 'last_committed', 'days_since_commit', 
                         'stars', 'language', 'commits_last_30d', 'merges_last_30d', 'repo_health_score']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.results)
        
        logger.info(f"Successfully saved results to {self.output_file}")
        
        # Print summary statistics
        self.print_summary()
    
    def print_summary(self):
        """Print summary statistics."""
        if not self.results:
            return
        
        # Calculate statistics
        orgs = set(r['org'] for r in self.results)
        languages = {}
        for r in self.results:
            lang = r['language']
            languages[lang] = languages.get(lang, 0) + 1
        
        total_stars = sum(r['stars'] for r in self.results)
        avg_days = sum(r['days_since_commit'] for r in self.results) / len(self.results)
        avg_health = sum(r['repo_health_score'] for r in self.results) / len(self.results)
        
        print("\n" + "="*60)
        print("FTSE-250 ACTIVE REPOSITORIES SUMMARY")
        print("="*60)
        print(f"Total active repositories: {len(self.results)}")
        print(f"Number of organizations: {len(orgs)}")
        print(f"Average days since last commit: {avg_days:.1f}")
        print(f"Average health score: {avg_health:.2f}")
        print(f"Total stars: {total_stars:,}")
        print(f"\nTop 5 languages:")
        for lang, count in sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {lang}: {count} repositories")
        
        # Show most active organizations
        org_counts = {}
        for r in self.results:
            org = r['org']
            org_counts[org] = org_counts.get(org, 0) + 1
        
        print(f"\nTop 5 most active organizations (by repo count):")
        for org, count in sorted(org_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {org}: {count} active repositories")
        
        # Show top repositories by health score
        print(f"\nTop 5 healthiest repositories:")
        for repo in self.results[:5]:
            print(f"  {repo['org']}/{repo['repo']}: score={repo['repo_health_score']:.1f} "
                  f"(commits={repo['commits_last_30d']}, merges={repo['merges_last_30d']})")
        
        print("="*60)
    
    def run(self):
        """Run the complete collection process."""
        logger.info(f"Starting FTSE-250 active repositories collection with health metrics")
        logger.info(f"Activity threshold: {self.days_threshold} days")
        
        self.collect_all_organizations()
        self.save_results()
        
        logger.info("Collection complete!")


def main():
    """Main entry point."""
    # Create collector with 30-day threshold
    collector = FTSE250ActiveReposCollector(days_threshold=30)
    collector.run()


if __name__ == "__main__":
    main()