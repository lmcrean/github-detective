"""Quick script to count repositories per organization and save incrementally."""

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


class OrganizationRepoCounter:
    """Count repositories for all organizations."""
    
    def __init__(self):
        """Initialize with GitHub client."""
        self.github_client = GitHubClient()
        self.output_file = Path(__file__).parent.parent / 'data' / 'repos' / 'org_repo_counts.csv'
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
        path = github_url.replace('github.com/', '').strip('/')
        parts = path.split('/')
        if parts and parts[0]:
            return parts[0].lower()
        return None
    
    def count_org_repositories(self, org_name: str) -> int:
        """Count public repositories for an organization."""
        try:
            repos_data = self.github_client.get_org_repositories(org_name)
            if repos_data:
                return len(repos_data)
            else:
                return 0
        except Exception as e:
            logger.error(f"Error counting repositories for {org_name}: {str(e)}")
            return 0
    
    def save_progress(self):
        """Save current results to CSV (incremental save)."""
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        
        with open(self.output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['org', 'github_org', 'repo_count', 'revenue']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            
            writer.writeheader()
            for result in self.results:
                writer.writerow(result)
        
        logger.info(f"Progress saved to {self.output_file}")
    
    def count_all_organizations(self, orgs_filepath: str):
        """Count repositories for all organizations."""
        # Parse organizations
        organizations = self.parse_orgs_ts(orgs_filepath)
        
        total_orgs = len(organizations)
        total_repos = 0
        
        for i, (company_name, org_data) in enumerate(organizations.items(), 1):
            logger.info(f"\n[{i}/{total_orgs}] Processing {company_name}")
            
            company_total = 0
            processed_orgs = set()
            
            for github_url in org_data['github_urls']:
                org_name = self.extract_org_from_github_url(github_url)
                
                if not org_name or org_name in processed_orgs:
                    continue
                
                processed_orgs.add(org_name)
                
                # Count repositories for this organization
                logger.info(f"  Counting repos for github.com/{org_name}...")
                repo_count = self.count_org_repositories(org_name)
                
                if repo_count > 0:
                    logger.info(f"    Found {repo_count} repositories")
                    company_total += repo_count
                    
                    # Add result for this GitHub org
                    self.results.append({
                        'org': company_name,
                        'github_org': org_name,
                        'repo_count': repo_count,
                        'revenue': org_data['revenue']
                    })
                else:
                    logger.info(f"    No public repositories found")
                
                # Small delay between GitHub orgs
                time.sleep(1)
            
            if company_total == 0:
                # Add entry even if no repos found
                self.results.append({
                    'org': company_name,
                    'github_org': 'N/A',
                    'repo_count': 0,
                    'revenue': org_data['revenue']
                })
            
            total_repos += company_total
            logger.info(f"  {company_name} total: {company_total} repositories")
            logger.info(f"  Running total: {total_repos} repositories")
            
            # Save progress after each organization
            self.save_progress()
            
            # Delay between companies
            if i < total_orgs:
                time.sleep(2)
        
        # Print final statistics
        self.print_statistics(total_repos)
    
    def print_statistics(self, total_repos: int):
        """Print summary statistics."""
        logger.info("\n" + "="*60)
        logger.info("FINAL STATISTICS")
        logger.info("="*60)
        
        # Group by company
        company_totals = {}
        for result in self.results:
            company = result['org']
            if company not in company_totals:
                company_totals[company] = 0
            company_totals[company] += result['repo_count']
        
        # Sort by repo count
        sorted_companies = sorted(company_totals.items(), key=lambda x: x[1], reverse=True)
        
        logger.info(f"\nTotal repositories across all organizations: {total_repos:,}")
        logger.info(f"Total companies analyzed: {len(company_totals)}")
        logger.info(f"Average repos per company: {total_repos // len(company_totals) if company_totals else 0}")
        
        # Companies with no repos
        no_repo_companies = [c for c, count in company_totals.items() if count == 0]
        logger.info(f"Companies with no public GitHub repos: {len(no_repo_companies)}")
        
        # Top 10 companies by repo count
        logger.info("\nTop 10 companies by repository count:")
        for company, count in sorted_companies[:10]:
            revenue = next((r['revenue'] for r in self.results if r['org'] == company), 'N/A')
            logger.info(f"  {company}: {count:,} repos (Revenue: {revenue})")
        
        # Bottom 10 companies with repos
        companies_with_repos = [(c, count) for c, count in sorted_companies if count > 0]
        if len(companies_with_repos) > 10:
            logger.info("\nBottom 10 companies with repositories:")
            for company, count in companies_with_repos[-10:]:
                revenue = next((r['revenue'] for r in self.results if r['org'] == company), 'N/A')
                logger.info(f"  {company}: {count} repos (Revenue: {revenue})")
        
        logger.info(f"\nResults saved to: {self.output_file}")


def main():
    """Main function to count repositories."""
    logger.info("Starting organization repository count")
    
    # Paths
    orgs_file = Path(__file__).parent.parent / 'orgs.ts'
    
    # Check if orgs.ts exists
    if not orgs_file.exists():
        logger.error(f"orgs.ts not found at {orgs_file}")
        sys.exit(1)
    
    # Initialize counter
    counter = OrganizationRepoCounter()
    
    try:
        # Count all organizations
        counter.count_all_organizations(str(orgs_file))
        
        logger.info("\n✅ Counting complete!")
        
    except KeyboardInterrupt:
        logger.warning("\n⚠️  Process interrupted by user")
        logger.info("Partial results saved")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Counting failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()