"""Collect FTSE-100 organization repositories filtered by activity and ordered by open issues."""

import os
import sys
import csv
import logging
import time
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
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


class FTSE100ReposByIssuesCollector:
    """Collect active repositories from FTSE-100 organizations ordered by open issues."""
    
    def __init__(self, days_threshold: int = 365):
        """
        Initialize collector.
        
        Args:
            days_threshold: Maximum days since last commit to consider repo active (default 365)
        """
        self.github_client = GitHubClient()
        self.days_threshold = days_threshold
        self.input_file = Path(__file__).parent.parent / 'data' / 'orgs' / 'index' / 'pull' / 'ftse-100-github-check.csv'
        self.output_file = Path(__file__).parent.parent / 'data' / 'repos' / 'batch_Aug28' / 'ftse100_active_repos_by_open_issues.csv'
        self.results = []
        self.github_token = os.getenv('API_GITHUB_TOKEN') or os.getenv('GITHUB_TOKEN')
        
        if not self.github_token:
            logger.warning("No GitHub token found. API rate limits will be restricted.")
        
    def parse_org_from_name(self, org_name: str) -> Optional[str]:
        """Convert organization name to GitHub username."""
        # Simple mapping for known organizations
        # This could be enhanced with a more comprehensive mapping
        org_mapping = {
            '3i Group Plc': '3i',
            'Admiral Group': 'admiralgroup',
            'AstraZeneca plc': 'AstraZeneca',
            'Auto Trader Group plc': 'autotraderuk',
            'Aviva Plc': 'aviva-group',
            'BAE Systems plc': 'baesystems',
            'Barclays plc': 'Barclays',
            'BP Plc': 'bp',
            'British American Tobacco plc': 'bat',
            'BT Group plc': 'bt',
            'Burberry Group plc': 'Burberry',
            'Centrica plc': 'centrica',
            'Diageo plc': 'Diageo',
            'GSK plc': 'GSK-Biostatistics',
            'HSBC Holdings plc': 'hsbc',
            'Lloyds Banking Group plc': 'LBG-Open-Source',
            'London Stock Exchange Group plc': 'lseg',
            'National Grid plc': 'nationalgrid',
            'Pearson plc': 'Pearson-Higher-Ed',
            'Prudential plc': 'Prudential',
            'Rolls-Royce Holdings plc': 'rolls-royce',
            'Sage Group plc': 'Sage',
            'Shell plc': 'Shell',
            'Standard Chartered plc': 'standard-chartered',
            'Tesco plc': 'Tesco',
            'Unilever plc': 'Unilever',
            'Vodafone Group plc': 'Vodafone',
            'Whitbread plc': 'whitbread',
            'WPP plc': 'wpp'
        }
        
        # Try direct mapping first
        if org_name in org_mapping:
            return org_mapping[org_name]
        
        # Try to extract a simple name
        simple_name = org_name.replace(' plc', '').replace(' Plc', '').replace(' Group', '').replace(' Holdings', '')
        simple_name = simple_name.replace(' ', '').lower()
        
        return simple_name if simple_name else None
    
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
    
    def get_commit_and_merge_stats(self, org: str, repo: str, days: int = 30) -> Tuple[int, int]:
        """Get commit and merge count for the last N days."""
        try:
            headers = {'Accept': 'application/vnd.github.v3+json'}
            if self.github_token:
                headers['Authorization'] = f'token {self.github_token}'
            
            # Calculate since date
            since_date = (datetime.now() - timedelta(days=days)).isoformat()
            
            # Get commits from last N days
            commits_url = f"https://api.github.com/repos/{org}/{repo}/commits"
            params = {
                'since': since_date,
                'per_page': 100
            }
            
            all_commits = []
            page = 1
            
            while page <= 3:  # Limit to 3 pages to avoid rate limits
                params['page'] = page
                response = requests.get(commits_url, headers=headers, params=params)
                
                if response.status_code != 200:
                    return 0, 0
                
                commits = response.json()
                
                if not commits:
                    break
                    
                all_commits.extend(commits)
                
                if len(commits) < 100:
                    break
                
                page += 1
                time.sleep(0.1)  # Rate limiting
            
            total_commits = len(all_commits)
            
            # Count merge commits
            merges = sum(1 for commit in all_commits 
                        if 'parents' in commit and len(commit.get('parents', [])) > 1)
            
            return total_commits, merges
            
        except Exception as e:
            logger.error(f"Error fetching commit stats for {org}/{repo}: {str(e)}")
            return 0, 0
    
    def get_contributors_count(self, org: str, repo: str) -> int:
        """Get total contributors count for a repository."""
        try:
            headers = {'Accept': 'application/vnd.github.v3+json'}
            if self.github_token:
                headers['Authorization'] = f'token {self.github_token}'
            
            contributors_url = f"https://api.github.com/repos/{org}/{repo}/contributors"
            params = {'per_page': 100, 'anon': 'true'}
            
            response = requests.get(contributors_url, headers=headers, params=params)
            
            if response.status_code == 200:
                contributors = response.json()
                total_count = len(contributors)
                
                # Check for pagination
                if 'Link' in response.headers:
                    import re
                    link_header = response.headers['Link']
                    last_page_match = re.search(r'page=(\d+)>; rel="last"', link_header)
                    if last_page_match:
                        last_page = int(last_page_match.group(1))
                        # Estimate total based on pages
                        total_count = (last_page - 1) * 100 + len(contributors)
                
                return total_count
            else:
                return 0
                
        except Exception as e:
            logger.error(f"Error counting contributors for {org}/{repo}: {str(e)}")
            return 0
    
    def get_org_repositories_filtered(self, org_name: str) -> List[Dict]:
        """Get repositories for an organization filtered by recent activity."""
        logger.info(f"Fetching repositories for {org_name}...")
        
        try:
            repos_data = self.github_client.get_org_repositories(org_name)
            
            if not repos_data:
                logger.warning(f"No repositories found for {org_name}")
                return []
            
            logger.info(f"Found {len(repos_data)} total repositories for {org_name}")
            
            # Filter and enrich repositories
            filtered_repos = []
            for repo in repos_data:
                # Skip forks and archived repos
                if repo.get('fork', False) or repo.get('archived', False):
                    continue
                
                # Check last commit date
                pushed_at = repo.get('pushed_at', '')
                days_since_commit = self.calculate_days_since(pushed_at)
                
                # Filter by threshold (within 1 year)
                if days_since_commit >= 0 and days_since_commit <= self.days_threshold:
                    repo_name = repo.get('name', '')
                    
                    logger.info(f"  Processing {org_name}/{repo_name}...")
                    
                    # Get commit and merge stats
                    commits_30d, merges_30d = self.get_commit_and_merge_stats(org_name, repo_name)
                    
                    # Calculate health score
                    health_score = (commits_30d + merges_30d) / 2
                    
                    # Get contributors count
                    contributors_total = self.get_contributors_count(org_name, repo_name)
                    
                    repo_info = {
                        'org': org_name,
                        'repo': repo_name,
                        'github_repo_url': f"https://github.com/{org_name}/{repo_name}",
                        'last_committed': pushed_at[:10] if pushed_at else '',
                        'days_since_commit': days_since_commit,
                        'stars': repo.get('stargazers_count', 0),
                        'language': repo.get('language', '') or 'None',
                        'commits_last_30d': commits_30d,
                        'merges_last_30d': merges_30d,
                        'repo_health_score': health_score,
                        'open_issues_current': repo.get('open_issues_count', 0),
                        'contributors_total': contributors_total
                    }
                    filtered_repos.append(repo_info)
                    
                    # Rate limiting
                    time.sleep(0.5)
            
            logger.info(f"Found {len(filtered_repos)} active repositories (within {self.days_threshold} days) for {org_name}")
            return filtered_repos
            
        except Exception as e:
            logger.error(f"Error fetching repositories for {org_name}: {str(e)}")
            return []
    
    def collect_all_organizations(self):
        """Process all organizations from the FTSE-100 CSV."""
        logger.info(f"Reading organizations from {self.input_file}")
        
        if not self.input_file.exists():
            logger.error(f"Input file not found: {self.input_file}")
            return
        
        # Read FTSE-100 organizations
        orgs_to_process = []
        with open(self.input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                org_name = row.get('Organization Name', '')
                if org_name:
                    # Try to get GitHub org name
                    github_org = self.parse_org_from_name(org_name)
                    if github_org:
                        org_info = {
                            'company': org_name,
                            'org_name': github_org
                        }
                        orgs_to_process.append(org_info)
        
        logger.info(f"Found {len(orgs_to_process)} organizations to check")
        
        # Try known active organizations first
        known_active_orgs = ['Sage', 'GSK-Biostatistics', 'LBG-Open-Source', 'Vodafone', 
                             'baesystems', 'hsbc', 'bp', 'Shell', 'Unilever', 'Barclays',
                             'AstraZeneca', 'Diageo', 'Pearson-Higher-Ed', 'bt', 'Tesco']
        
        processed_orgs = set()
        
        # Process known active orgs first
        for org in known_active_orgs:
            logger.info(f"\nProcessing known org: {org}")
            repos = self.get_org_repositories_filtered(org)
            if repos:
                self.results.extend(repos)
                processed_orgs.add(org)
            logger.info(f"Total repositories collected so far: {len(self.results)}")
        
        # Process remaining organizations
        for org_info in orgs_to_process:
            if org_info['org_name'] not in processed_orgs:
                logger.info(f"\nProcessing {org_info['company']} ({org_info['org_name']})")
                repos = self.get_org_repositories_filtered(org_info['org_name'])
                if repos:
                    self.results.extend(repos)
                logger.info(f"Total repositories collected so far: {len(self.results)}")
    
    def save_results(self):
        """Save results to CSV file sorted by open issues."""
        if not self.results:
            logger.warning("No active repositories found to save")
            return
        
        # Ensure output directory exists
        self.output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Sort results by open_issues_current in descending order
        self.results.sort(key=lambda x: x['open_issues_current'], reverse=True)
        
        # Save to CSV
        logger.info(f"Saving {len(self.results)} repositories to {self.output_file}")
        
        with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['org', 'repo', 'github_repo_url', 'last_committed', 'days_since_commit', 
                         'stars', 'language', 'commits_last_30d', 'merges_last_30d', 
                         'repo_health_score', 'open_issues_current', 'contributors_total']
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
        total_issues = sum(r['open_issues_current'] for r in self.results)
        avg_issues = total_issues / len(self.results) if self.results else 0
        avg_contributors = sum(r['contributors_total'] for r in self.results) / len(self.results) if self.results else 0
        
        print("\n" + "="*60)
        print("SUMMARY STATISTICS")
        print("="*60)
        print(f"Total active repositories: {len(self.results)}")
        print(f"Number of organizations: {len(orgs)}")
        print(f"Total open issues: {total_issues:,}")
        print(f"Average open issues per repo: {avg_issues:.1f}")
        print(f"Average contributors per repo: {avg_contributors:.1f}")
        print(f"Total stars: {total_stars:,}")
        
        print(f"\nTop 5 languages:")
        for lang, count in sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {lang}: {count} repositories")
        
        # Show repos with most open issues
        print(f"\nTop 10 repositories by open issues:")
        for r in self.results[:10]:
            print(f"  {r['org']}/{r['repo']}: {r['open_issues_current']} open issues ({r['contributors_total']} contributors)")
        
        # Show most active organizations by issue count
        org_issues = {}
        for r in self.results:
            org = r['org']
            org_issues[org] = org_issues.get(org, 0) + r['open_issues_current']
        
        print(f"\nTop 5 organizations by total open issues:")
        for org, issues in sorted(org_issues.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {org}: {issues} total open issues")
        
        print("="*60)
    
    def run(self):
        """Run the complete collection process."""
        logger.info(f"Starting FTSE-100 active repositories collection")
        logger.info(f"Activity threshold: repositories active within {self.days_threshold} days")
        logger.info(f"Sorting by: open issues (descending)")
        
        self.collect_all_organizations()
        self.save_results()
        
        logger.info("Collection complete!")


def main():
    """Main entry point."""
    # Create collector with 365-day threshold (1 year)
    collector = FTSE100ReposByIssuesCollector(days_threshold=365)
    collector.run()


if __name__ == "__main__":
    main()