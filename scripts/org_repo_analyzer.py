"""Analyze all organizations from orgs.ts and generate CSV with 30-day merge rates."""

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


class OrganizationRepoAnalyzer:
    """Analyze repositories for all organizations and calculate merge rates."""
    
    def __init__(self):
        """Initialize with GitHub client and PR fetcher."""
        self.github_client = GitHubClient()
        self.pr_fetcher = MergedPRsFetcher()
        self.results = []
        
    def parse_orgs_ts(self, filepath: str) -> Dict[str, Dict]:
        """Parse the orgs.ts file to extract organization data."""
        logger.info(f"Parsing organizations from {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract the ORGS object content
        orgs_match = re.search(r'const ORGS = \{(.*?)\};', content, re.DOTALL)
        if not orgs_match:
            raise ValueError("Could not find ORGS object in orgs.ts")
        
        orgs_content = orgs_match.group(1)
        
        # Parse organization entries
        org_pattern = r'"([^"]+)":\s*\{([^}]*(?:\{[^}]*\}[^}]*)*)\}'
        organizations = {}
        
        for match in re.finditer(org_pattern, orgs_content):
            org_name = match.group(1)
            org_data_str = match.group(2)
            
            # Extract github URLs
            github_match = re.search(r'github:\s*\[(.*?)\]', org_data_str, re.DOTALL)
            github_urls = []
            if github_match:
                urls_str = github_match.group(1)
                url_matches = re.findall(r'"([^"]*github\.com/[^"]*)"', urls_str)
                github_urls = url_matches
            
            # Extract revenue
            revenue_match = re.search(r'revenue:\s*"([^"]*)"', org_data_str)
            revenue = revenue_match.group(1) if revenue_match else ""
            
            # Extract tags
            tags_match = re.search(r'tags:\s*\[(.*?)\]', org_data_str)
            tags = []
            if tags_match:
                tags_str = tags_match.group(1)
                tag_matches = re.findall(r'"([^"]*)"', tags_str)
                tags = tag_matches
            
            organizations[org_name] = {
                'github_urls': github_urls,
                'revenue': revenue,
                'tags': tags
            }
        
        logger.info(f"Parsed {len(organizations)} organizations")
        return organizations
    
    def extract_org_from_github_url(self, github_url: str) -> Optional[str]:
        """Extract organization name from GitHub URL."""
        # Remove protocol and domain
        path = github_url.replace('github.com/', '').strip('/')
        
        # Split by '/' and take first part (organization name)
        parts = path.split('/')
        if parts and parts[0]:
            return parts[0].lower()
        return None
    
    def get_org_repositories(self, org_name: str) -> List[Dict]:
        """Get all public repositories for an organization."""
        logger.info(f"Fetching all repositories for {org_name}")
        
        try:
            repos_data = self.github_client.get_org_repositories(org_name)
            if repos_data:
                logger.info(f"Found {len(repos_data)} repositories for {org_name}")
                return repos_data
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
    
    def analyze_organizations(self, orgs_filepath: str) -> List[Dict]:
        """Analyze all organizations and their repositories."""
        # Parse organizations
        organizations = self.parse_orgs_ts(orgs_filepath)
        
        results = []
        total_orgs = len(organizations)
        
        for i, (company_name, org_data) in enumerate(organizations.items(), 1):
            logger.info(f"Processing {company_name} ({i}/{total_orgs})")
            
            # Process each GitHub URL for this organization
            processed_orgs = set()  # To avoid duplicates
            
            for github_url in org_data['github_urls']:
                org_name = self.extract_org_from_github_url(github_url)
                
                if not org_name or org_name in processed_orgs:
                    continue
                
                processed_orgs.add(org_name)
                
                # Get repositories for this organization (limit to 10 per org)
                repositories = self.get_org_repositories(org_name, limit=10)
                
                for repo in repositories:
                    repo_name = repo.get('name', '')
                    if not repo_name:
                        continue
                    
                    # Calculate merge rate
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
                    logger.info(f"  {org_name}/{repo_name}: {merge_rate} merges (30d)")
                    
                    # Rate limiting - longer delay between repos to avoid rate limits
                    time.sleep(10)
                
                # Much longer delay between organizations to be respectful to GitHub API
                time.sleep(30)
        
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
        
        logger.info(f"Results saved to {output_filepath}")


def main():
    """Main function to run the analysis."""
    logger.info("Starting organization repository analysis")
    
    # Paths
    orgs_file = Path(__file__).parent.parent / 'orgs.ts'
    output_file = Path(__file__).parent.parent / 'data' / 'repos' / 'high_revenue_companies.csv'
    
    # Check if orgs.ts exists
    if not orgs_file.exists():
        logger.error(f"orgs.ts not found at {orgs_file}")
        sys.exit(1)
    
    # Initialize analyzer
    analyzer = OrganizationRepoAnalyzer()
    
    try:
        # Run analysis
        results = analyzer.analyze_organizations(str(orgs_file))
        
        # Save results
        analyzer.save_to_csv(results, str(output_file))
        
        logger.info(f"Analysis complete. Processed {len(results)} repository entries.")
        
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()