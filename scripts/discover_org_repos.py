"""Step 1: Discover all repositories for all organizations and save to CSV."""

import re
import csv
import os
import sys
import time
import logging
from pathlib import Path
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


class OrganizationRepoDiscoverer:
    """Discover all repositories for all organizations."""
    
    def __init__(self):
        """Initialize with GitHub client."""
        self.github_client = GitHubClient()
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
            
            organizations[org_name] = {
                'github_urls': github_urls,
                'revenue': revenue
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
    
    def discover_all_repositories(self, orgs_filepath: str) -> List[Dict]:
        """Discover all repositories for all organizations."""
        # Parse organizations
        organizations = self.parse_orgs_ts(orgs_filepath)
        
        results = []
        total_orgs = len(organizations)
        org_stats = {}
        
        for i, (company_name, org_data) in enumerate(organizations.items(), 1):
            logger.info(f"Processing {company_name} ({i}/{total_orgs})")
            
            # Process each GitHub URL for this organization
            processed_orgs = set()  # To avoid duplicates
            company_repo_count = 0
            
            for github_url in org_data['github_urls']:
                org_name = self.extract_org_from_github_url(github_url)
                
                if not org_name or org_name in processed_orgs:
                    continue
                
                processed_orgs.add(org_name)
                
                # Get all repositories for this organization
                repositories = self.get_org_repositories(org_name)
                
                for repo in repositories:
                    repo_name = repo.get('name', '')
                    if not repo_name:
                        continue
                    
                    # Store repository info (we'll calculate merge rates later)
                    hyperlink = f"https://github.com/{org_name}/{repo_name}"
                    
                    result = {
                        'org': company_name,
                        'github_org': org_name,
                        'repo': repo_name,
                        'hyperlink': hyperlink,
                        'stars': repo.get('stargazers_count', 0),
                        'updated_at': repo.get('updated_at', ''),
                        'language': repo.get('language', ''),
                        '30d_merge_rate': 'TBD'  # To be calculated in step 2
                    }
                    
                    results.append(result)
                    company_repo_count += 1
                
                # Small delay between GitHub orgs
                time.sleep(2)
            
            org_stats[company_name] = company_repo_count
            logger.info(f"  Total repos for {company_name}: {company_repo_count}")
            
            # Delay between companies
            time.sleep(5)
        
        # Print summary statistics
        logger.info("\n=== Discovery Summary ===")
        logger.info(f"Total organizations processed: {len(org_stats)}")
        logger.info(f"Total repositories discovered: {len(results)}")
        
        # Show top 10 organizations by repo count
        sorted_orgs = sorted(org_stats.items(), key=lambda x: x[1], reverse=True)[:10]
        logger.info("\nTop 10 organizations by repository count:")
        for org, count in sorted_orgs:
            logger.info(f"  {org}: {count} repositories")
        
        return results
    
    def save_to_csv(self, results: List[Dict], output_filepath: str):
        """Save results to CSV file."""
        logger.info(f"Saving {len(results)} repository entries to {output_filepath}")
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        
        with open(output_filepath, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['org', 'github_org', 'repo', 'hyperlink', 'stars', 'updated_at', 'language', '30d_merge_rate']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            
            writer.writeheader()
            for result in results:
                writer.writerow(result)
        
        logger.info(f"Repository list saved to {output_filepath}")


def main():
    """Main function to discover all repositories."""
    logger.info("Starting repository discovery for all organizations")
    
    # Paths
    orgs_file = Path(__file__).parent.parent / 'orgs.ts'
    output_file = Path(__file__).parent.parent / 'data' / 'repos' / 'all_org_repos_checkpoint.csv'
    
    # Check if orgs.ts exists
    if not orgs_file.exists():
        logger.error(f"orgs.ts not found at {orgs_file}")
        sys.exit(1)
    
    # Initialize discoverer
    discoverer = OrganizationRepoDiscoverer()
    
    try:
        # Discover all repositories
        results = discoverer.discover_all_repositories(str(orgs_file))
        
        # Save checkpoint
        discoverer.save_to_csv(results, str(output_file))
        
        logger.info(f"\n✅ Discovery complete! Found {len(results)} total repositories")
        logger.info(f"Checkpoint saved to: {output_file}")
        logger.info("\nNext step: Run calculate_merge_rates.py to compute 30-day merge rates")
        
    except Exception as e:
        logger.error(f"Discovery failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()