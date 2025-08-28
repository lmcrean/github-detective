"""Collect and filter FTSE-100 organization repositories by recent activity."""

import os
import sys
import csv
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.github_client.client import GitHubClient

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FTSE100ActiveReposCollector:
    """Collect active repositories from FTSE-100 organizations."""
    
    def __init__(self, days_threshold: int = 30):
        """
        Initialize collector.
        
        Args:
            days_threshold: Number of days to consider a repo as active (default 30)
        """
        self.github_client = GitHubClient()
        self.days_threshold = days_threshold
        self.input_file = Path(__file__).parent.parent / 'data' / 'orgs' / 'index' / 'pull' / 'ftse-100-claude.csv'
        self.output_file = Path(__file__).parent.parent / 'data' / 'repos' / 'batch_Aug28' / 'ftse100_active_repos_last30d.csv'
        self.results = []
        
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
    
    def get_org_repositories_filtered(self, org_name: str) -> List[Dict]:
        """Get repositories for an organization filtered by recent activity."""
        logger.info(f"Fetching repositories for {org_name}...")
        
        try:
            repos_data = self.github_client.get_org_repositories(org_name)
            
            if not repos_data:
                logger.warning(f"No repositories found for {org_name}")
                return []
            
            logger.info(f"Found {len(repos_data)} total repositories for {org_name}")
            
            # Filter repositories by recent activity
            filtered_repos = []
            for repo in repos_data:
                # Skip forks and archived repos
                if repo.get('fork', False) or repo.get('archived', False):
                    continue
                
                # Check last commit date (pushed_at)
                pushed_at = repo.get('pushed_at', '')
                days_since_commit = self.calculate_days_since(pushed_at)
                
                # Filter by threshold
                if days_since_commit >= 0 and days_since_commit <= self.days_threshold:
                    repo_info = {
                        'org': org_name,
                        'repo': repo.get('name', ''),
                        'github_repo_url': f"https://github.com/{org_name}/{repo.get('name', '')}",
                        'last_committed': pushed_at[:10] if pushed_at else '',  # Extract date part
                        'days_since_commit': days_since_commit,
                        'stars': repo.get('stargazers_count', 0),
                        'language': repo.get('language', '') or 'None'
                    }
                    filtered_repos.append(repo_info)
            
            logger.info(f"Found {len(filtered_repos)} active repositories (last {self.days_threshold} days) for {org_name}")
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
        """Save results to CSV file."""
        if not self.results:
            logger.warning("No active repositories found to save")
            return
        
        # Ensure output directory exists
        self.output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Sort results by org name and repo name
        self.results.sort(key=lambda x: (x['org'], x['repo']))
        
        # Save to CSV
        logger.info(f"Saving {len(self.results)} repositories to {self.output_file}")
        
        with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['org', 'repo', 'github_repo_url', 'last_committed', 'days_since_commit', 'stars', 'language']
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
        
        print("\n" + "="*60)
        print("SUMMARY STATISTICS")
        print("="*60)
        print(f"Total active repositories: {len(self.results)}")
        print(f"Number of organizations: {len(orgs)}")
        print(f"Average days since last commit: {avg_days:.1f}")
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
        
        print("="*60)
    
    def run(self):
        """Run the complete collection process."""
        logger.info(f"Starting FTSE-100 active repositories collection")
        logger.info(f"Activity threshold: {self.days_threshold} days")
        
        self.collect_all_organizations()
        self.save_results()
        
        logger.info("Collection complete!")


def main():
    """Main entry point."""
    # Create collector with 30-day threshold
    collector = FTSE100ActiveReposCollector(days_threshold=30)
    collector.run()


if __name__ == "__main__":
    main()