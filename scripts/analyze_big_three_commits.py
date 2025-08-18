"""Analyze last commit dates for Microsoft, Google, and Meta repositories."""

import os
import sys
import time
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


class BigThreeCommitAnalyzer:
    """Analyze last commits for Microsoft, Google, and Meta repositories."""
    
    def __init__(self):
        """Initialize with GitHub client."""
        self.github_client = GitHubClient()
        self.output_file = Path(__file__).parent.parent / 'data' / 'repos' / 'big_three_last_commits.csv'
        self.results = []
        
    def get_org_repositories_with_dates(self, org_name: str) -> List[Dict]:
        """Get all repositories with last update dates."""
        logger.info(f"Fetching repositories for {org_name}...")
        
        try:
            repos_data = self.github_client.get_org_repositories(org_name)
            if repos_data:
                logger.info(f"Found {len(repos_data)} repositories for {org_name}")
                
                # Extract relevant data including dates
                repo_list = []
                for repo in repos_data:
                    repo_info = {
                        'name': repo.get('name', ''),
                        'full_name': repo.get('full_name', ''),
                        'pushed_at': repo.get('pushed_at', ''),  # Last commit date
                        'updated_at': repo.get('updated_at', ''),  # Last update (includes non-code changes)
                        'created_at': repo.get('created_at', ''),
                        'stars': repo.get('stargazers_count', 0),
                        'language': repo.get('language', ''),
                        'fork': repo.get('fork', False),
                        'archived': repo.get('archived', False)
                    }
                    repo_list.append(repo_info)
                
                return repo_list
            else:
                logger.warning(f"No repositories found for {org_name}")
                return []
        except Exception as e:
            logger.error(f"Error fetching repositories for {org_name}: {str(e)}")
            return []
    
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
    
    def categorize_activity(self, days: int) -> str:
        """Categorize repository by activity level."""
        if days < 0:
            return "Unknown"
        elif days <= 7:
            return "Very Active"
        elif days <= 30:
            return "Active"
        elif days <= 90:
            return "Maintained"
        elif days <= 365:
            return "Stale"
        else:
            return "Abandoned"
    
    def analyze_organizations(self):
        """Analyze Microsoft, Google, Meta, and IBM repositories."""
        organizations = {
            'Microsoft': ['microsoft'],
            'Google': ['google'],
            'Meta': ['facebook', 'facebookresearch'],
            'IBM': ['ibm']
        }
        
        all_results = []
        org_stats = {}
        
        for company, github_orgs in organizations.items():
            logger.info(f"\n{'='*60}")
            logger.info(f"Processing {company}")
            logger.info('='*60)
            
            company_repos = []
            
            for org_name in github_orgs:
                repos = self.get_org_repositories_with_dates(org_name)
                
                for repo in repos:
                    days_since_push = self.calculate_days_since(repo['pushed_at'])
                    activity_status = self.categorize_activity(days_since_push)
                    
                    result = {
                        'company': company,
                        'github_org': org_name,
                        'repo': repo['name'],
                        'hyperlink': f"https://github.com/{repo['full_name']}",
                        'last_commit': repo['pushed_at'][:10] if repo['pushed_at'] else 'N/A',
                        'days_since_commit': days_since_push,
                        'activity_status': activity_status,
                        'stars': repo['stars'],
                        'language': repo['language'] or 'N/A',
                        'is_fork': repo['fork'],
                        'is_archived': repo['archived']
                    }
                    
                    all_results.append(result)
                    company_repos.append(result)
                
                # Small delay between orgs
                time.sleep(2)
            
            # Calculate company statistics
            org_stats[company] = self.calculate_statistics(company_repos)
            self.print_company_stats(company, org_stats[company])
            
            # Save progress after each company
            self.save_results(all_results)
            logger.info(f"Progress saved for {company}")
            
            # Delay between companies
            time.sleep(5)
        
        # Print overall comparison
        self.print_comparison(org_stats)
        
        return all_results
    
    def calculate_statistics(self, repos: List[Dict]) -> Dict:
        """Calculate statistics for a set of repositories."""
        if not repos:
            return {}
        
        # Filter out forks and archived repos for main stats
        active_repos = [r for r in repos if not r['is_fork'] and not r['is_archived']]
        
        days_list = [r['days_since_commit'] for r in active_repos if r['days_since_commit'] >= 0]
        
        if not days_list:
            return {}
        
        # Count by activity status
        status_counts = {}
        for repo in active_repos:
            status = repo['activity_status']
            status_counts[status] = status_counts.get(status, 0) + 1
        
        # Find most active repos
        sorted_repos = sorted(active_repos, key=lambda x: x['days_since_commit'] if x['days_since_commit'] >= 0 else 999999)
        
        return {
            'total_repos': len(repos),
            'active_repos': len(active_repos),
            'fork_count': len([r for r in repos if r['is_fork']]),
            'archived_count': len([r for r in repos if r['is_archived']]),
            'status_counts': status_counts,
            'avg_days_since_commit': sum(days_list) / len(days_list) if days_list else 0,
            'median_days': sorted(days_list)[len(days_list)//2] if days_list else 0,
            'most_active': sorted_repos[:5] if sorted_repos else [],
            'least_active': sorted_repos[-5:] if len(sorted_repos) > 5 else []
        }
    
    def print_company_stats(self, company: str, stats: Dict):
        """Print statistics for a company."""
        if not stats:
            logger.info(f"No statistics available for {company}")
            return
        
        logger.info(f"\n{company} Statistics:")
        logger.info(f"  Total repositories: {stats['total_repos']}")
        logger.info(f"  Active (non-fork, non-archived): {stats['active_repos']}")
        logger.info(f"  Forks: {stats['fork_count']}")
        logger.info(f"  Archived: {stats['archived_count']}")
        
        logger.info(f"\n  Activity Distribution:")
        for status in ['Very Active', 'Active', 'Maintained', 'Stale', 'Abandoned', 'Unknown']:
            count = stats['status_counts'].get(status, 0)
            if count > 0:
                percentage = (count / stats['active_repos']) * 100 if stats['active_repos'] > 0 else 0
                logger.info(f"    {status}: {count} ({percentage:.1f}%)")
        
        logger.info(f"\n  Average days since last commit: {stats['avg_days_since_commit']:.1f}")
        logger.info(f"  Median days since last commit: {stats['median_days']}")
        
        logger.info(f"\n  Most recently updated repos:")
        for repo in stats['most_active'][:3]:
            logger.info(f"    - {repo['repo']}: {repo['days_since_commit']} days ago")
    
    def print_comparison(self, org_stats: Dict):
        """Print comparison between organizations."""
        logger.info("\n" + "="*60)
        logger.info("COMPARISON SUMMARY")
        logger.info("="*60)
        
        # Create comparison table
        companies = list(org_stats.keys())
        
        logger.info("\nRepository Counts:")
        for company in companies:
            stats = org_stats[company]
            logger.info(f"  {company}: {stats['total_repos']} total, {stats['active_repos']} active")
        
        logger.info("\nAverage Days Since Last Commit:")
        for company in companies:
            stats = org_stats[company]
            logger.info(f"  {company}: {stats['avg_days_since_commit']:.1f} days")
        
        logger.info("\nVery Active Repos (< 7 days):")
        for company in companies:
            stats = org_stats[company]
            very_active = stats['status_counts'].get('Very Active', 0)
            percentage = (very_active / stats['active_repos']) * 100 if stats['active_repos'] > 0 else 0
            logger.info(f"  {company}: {very_active} ({percentage:.1f}%)")
        
        logger.info("\nAbandoned Repos (> 365 days):")
        for company in companies:
            stats = org_stats[company]
            abandoned = stats['status_counts'].get('Abandoned', 0)
            percentage = (abandoned / stats['active_repos']) * 100 if stats['active_repos'] > 0 else 0
            logger.info(f"  {company}: {abandoned} ({percentage:.1f}%)")
    
    def save_results(self, results: List[Dict]):
        """Save results to CSV."""
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        
        with open(self.output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['company', 'github_org', 'repo', 'hyperlink', 'last_commit', 
                         'days_since_commit', 'activity_status', 'stars', 'language', 
                         'is_fork', 'is_archived']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            
            writer.writeheader()
            for result in results:
                writer.writerow(result)
        
        logger.info(f"Results saved to {self.output_file}")


def main():
    """Main function."""
    logger.info("Starting Big Four (Microsoft, Google, Meta, IBM) last commit analysis")
    
    analyzer = BigThreeCommitAnalyzer()
    
    try:
        results = analyzer.analyze_organizations()
        
        logger.info(f"\n✅ Analysis complete! Processed {len(results)} repositories")
        logger.info(f"Results saved to: {analyzer.output_file}")
        
    except KeyboardInterrupt:
        logger.warning("\n⚠️  Process interrupted by user")
        logger.info("Partial results may have been saved")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()