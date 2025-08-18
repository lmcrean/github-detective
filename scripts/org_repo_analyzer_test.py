"""Test version of org analyzer with just a few organizations."""

import re
import csv
import os
import sys
import time
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.repos.metrics.pr_metrics import MergedPRsFetcher
from scripts.github_client.client import GitHubClient

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class OrganizationRepoAnalyzerTest:
    """Test analyzer with small subset of organizations."""
    
    def __init__(self):
        """Initialize with GitHub client and PR fetcher."""
        self.github_client = GitHubClient()
        self.pr_fetcher = MergedPRsFetcher()
        self.results = []
        
    def get_test_organizations(self) -> Dict[str, Dict]:
        """Get just a few test organizations."""
        return {
            "Stripe": {
                "github_urls": ["github.com/stripe"],
                "revenue": "$5.1B",
                "tags": ["payments", "fintech", "api", "infrastructure"]
            },
            "Shopify": {
                "github_urls": ["github.com/shopify"],
                "revenue": "$8.88B",
                "tags": ["ecommerce", "platform", "payments", "retail"]
            },
            "Netflix": {
                "github_urls": ["github.com/netflix"],
                "revenue": "$39B",
                "tags": ["streaming", "entertainment", "content", "media"]
            }
        }
        
    def extract_org_from_github_url(self, github_url: str) -> Optional[str]:
        """Extract organization name from GitHub URL."""
        # Remove protocol and domain
        path = github_url.replace('github.com/', '').strip('/')
        
        # Split by '/' and take first part (organization name)
        parts = path.split('/')
        if parts and parts[0]:
            return parts[0].lower()
        return None
    
    def get_org_repositories(self, org_name: str, limit: int = 5) -> List[Dict]:
        """Get limited number of public repositories for an organization."""
        logger.info(f"Fetching max {limit} repositories for {org_name}")
        
        try:
            repos_data = self.github_client.get_org_repositories(org_name)
            if repos_data:
                # Limit to first N repositories to avoid rate limits
                limited_repos = repos_data[:limit]
                logger.info(f"Found {len(repos_data)} total, using first {len(limited_repos)} repositories for {org_name}")
                return limited_repos
            else:
                logger.warning(f"No repositories found or error fetching repos for {org_name}")
                return []
        except Exception as e:
            logger.error(f"Error fetching repositories for {org_name}: {str(e)}")
            return []
    
    def calculate_merge_rate(self, org_name: str, repo_name: str) -> int:
        """Calculate 30-day merge rate for a repository."""
        try:
            merge_count = self.pr_fetcher.get_merged_prs_count(org_name, repo_name, 30)
            return merge_count if merge_count >= 0 else 0
        except Exception as e:
            logger.warning(f"Error calculating merge rate for {org_name}/{repo_name}: {str(e)}")
            return 0
    
    def analyze_test_organizations(self) -> List[Dict]:
        """Analyze test organizations and their repositories."""
        organizations = self.get_test_organizations()
        results = []
        
        for i, (company_name, org_data) in enumerate(organizations.items(), 1):
            logger.info(f"Processing {company_name} ({i}/{len(organizations)})")
            
            # Process each GitHub URL for this organization
            for github_url in org_data['github_urls']:
                org_name = self.extract_org_from_github_url(github_url)
                
                if not org_name:
                    continue
                
                # Get limited repositories for this organization
                repositories = self.get_org_repositories(org_name, limit=3)  # Only 3 repos per org
                
                for repo in repositories:
                    repo_name = repo.get('name', '')
                    if not repo_name:
                        continue
                    
                    # Calculate merge rate
                    logger.info(f"  Calculating merge rate for {org_name}/{repo_name}")
                    merge_rate = self.calculate_merge_rate(org_name, repo_name)
                    
                    # Create hyperlink
                    hyperlink = f"https://github.com/{org_name}/{repo_name}"
                    
                    result = {
                        'org': company_name,
                        'repo': repo_name,
                        'hyperlink': hyperlink,
                        '30d_merge_rate': merge_rate
                    }
                    
                    results.append(result)
                    logger.info(f"    {org_name}/{repo_name}: {merge_rate} merges (30d)")
                    
                    # Longer delay between repos to avoid rate limits
                    time.sleep(5)
                
                # Even longer delay between organizations
                time.sleep(10)
        
        return results
    
    def save_to_csv(self, results: List[Dict], output_filepath: str):
        """Save results to CSV file."""
        logger.info(f"Saving {len(results)} results to {output_filepath}")
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        
        with open(output_filepath, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['org', 'repo', 'hyperlink', '30d_merge_rate']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            
            writer.writeheader()
            for result in results:
                writer.writerow(result)
        
        logger.info(f"Test results saved to {output_filepath}")


def main():
    """Main function to run the test analysis."""
    logger.info("Starting test organization repository analysis")
    
    output_file = Path(__file__).parent.parent / 'data' / 'repos' / 'test_high_revenue_companies.csv'
    
    # Initialize analyzer
    analyzer = OrganizationRepoAnalyzerTest()
    
    try:
        # Run analysis on test organizations
        results = analyzer.analyze_test_organizations()
        
        # Save results
        analyzer.save_to_csv(results, str(output_file))
        
        logger.info(f"Test analysis complete. Processed {len(results)} repository entries.")
        
        # Display results
        print("\nResults:")
        for result in results:
            print(f"{result['org']};{result['repo']};{result['hyperlink']};{result['30d_merge_rate']}")
        
    except Exception as e:
        logger.error(f"Test analysis failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()