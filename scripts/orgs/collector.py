"""Collect repository data for entire organizations using GitHub CLI."""

import json
import csv
import subprocess
import time
import os
import sys
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from models import OrganizationRepository
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class OrganizationCollector:
    """Collect all repository data for a GitHub organization."""
    
    def __init__(self, org_name: str):
        """Initialize collector for a specific organization."""
        self.org_name = org_name
        self.repositories: List[OrganizationRepository] = []
        self.github_token = os.getenv('API_GITHUB_TOKEN')
        self.rate_limit_hit = False
        
    def run_gh_command(self, command: List[str]) -> Optional[str]:
        """Run a GitHub CLI command and return the output."""
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
                encoding='utf-8'
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            if 'API rate limit exceeded' in e.stderr:
                if not self.rate_limit_hit:
                    print(f"\nRate limit hit. Continuing with collection but PR counts may be incomplete.")
                    self.rate_limit_hit = True
            else:
                print(f"Error running command {' '.join(command)}: {e.stderr}")
            return None
    
    def get_all_repos(self) -> List[Dict]:
        """Get all repositories for the organization using GitHub CLI."""
        print(f"Fetching all repositories for {self.org_name}...")
        
        # Use gh api with --paginate to automatically handle pagination
        command = [
            'gh', 'api',
            f'orgs/{self.org_name}/repos',
            '--paginate',
            '-H', 'Accept: application/vnd.github+json',
            '-H', 'X-GitHub-Api-Version: 2022-11-28'
        ]
        
        output = self.run_gh_command(command)
        if not output:
            print("No output received from GitHub API")
            return []
        
        try:
            # The paginate option returns a JSON array of all results
            repos = json.loads(output)
            print(f"Total repositories found: {len(repos)}")
            return repos
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            print(f"Output preview: {output[:500]}...")
            return []
    
    def get_pr_count(self, repo_name: str) -> int:
        """Get the count of open pull requests for a repository."""
        command = [
            'gh', 'api',
            f'search/issues',
            '--jq', '.total_count',
            '-X', 'GET',
            '-F', f'q=is:pr is:open repo:{self.org_name}/{repo_name}'
        ]
        
        output = self.run_gh_command(command)
        if output:
            try:
                return int(output.strip())
            except ValueError:
                return 0
        # Return -1 to indicate rate limit or error
        return -1
    
    def collect_repository_data(self, repo_data: Dict) -> Optional[OrganizationRepository]:
        """Collect data for a single repository."""
        repo_name = repo_data.get('name', '')
        if not repo_name:
            return None
        
        # Get open PR count separately
        pr_count = self.get_pr_count(repo_name)
        
        # Create repository object
        repo = OrganizationRepository.from_api_response(
            org_name=self.org_name,
            repo_data=repo_data,
            pr_count=pr_count
        )
        
        return repo
    
    def collect_all(self):
        """Collect data for all repositories in the organization."""
        repos = self.get_all_repos()
        
        print(f"\nCollecting detailed data for {len(repos)} repositories...")
        for i, repo_data in enumerate(repos, 1):
            repo_name = repo_data.get('name', 'unknown')
            print(f"  [{i}/{len(repos)}] Processing {repo_name}...")
            
            repo = self.collect_repository_data(repo_data)
            if repo:
                self.repositories.append(repo)
            
            # Rate limiting
            if i % 10 == 0:
                time.sleep(1)
        
        print(f"\nSuccessfully collected data for {len(self.repositories)} repositories")
    
    def save_to_csv(self, output_dir: str):
        """Save collected data to CSV file."""
        if not self.repositories:
            print("No data to save")
            return
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{self.org_name}_repos_{timestamp}.csv"
        filepath = os.path.join(output_dir, filename)
        
        # Write CSV
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'org_name', 'repo_name', 'open_issue_count', 
                'stars_count', 'forks_count', 'last_pushed_date',
                'pull_requests_open_count', 'about_description'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for repo in self.repositories:
                writer.writerow(repo.to_dict())
        
        print(f"Data saved to: {filepath}")
        
        # Also save a latest version without timestamp
        latest_filepath = os.path.join(output_dir, f"{self.org_name}_repos_latest.csv")
        with open(latest_filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for repo in self.repositories:
                writer.writerow(repo.to_dict())
        
        print(f"Latest version saved to: {latest_filepath}")
        
        return filepath


def main():
    """Main entry point for the script."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Collect GitHub organization repository data')
    parser.add_argument('organization', help='GitHub organization name (e.g., stripe, shopify)')
    parser.add_argument('--output-dir', help='Output directory', default=None)
    parser.add_argument('--sample', type=int, help='Only collect first N repositories (for testing)', default=0)
    
    args = parser.parse_args()
    
    # Determine output directory
    if args.output_dir:
        output_dir = args.output_dir
    else:
        # Use absolute path from project root
        project_root = Path(__file__).parent.parent
        output_dir = project_root / "data" / "orgs" / args.organization.lower()
        output_dir = str(output_dir)
    
    # Create collector
    collector = OrganizationCollector(args.organization)
    
    # Collect data
    if args.sample > 0:
        print(f"Running in sample mode: collecting first {args.sample} repositories")
        repos = collector.get_all_repos()
        repos = repos[:args.sample]  # Limit to sample size
        
        print(f"\nCollecting detailed data for {len(repos)} repositories...")
        for i, repo_data in enumerate(repos, 1):
            repo_name = repo_data.get('name', 'unknown')
            print(f"  [{i}/{len(repos)}] Processing {repo_name}...")
            
            repo = collector.collect_repository_data(repo_data)
            if repo:
                collector.repositories.append(repo)
    else:
        collector.collect_all()
    
    # Save results
    collector.save_to_csv(output_dir)
    
    # Print summary
    print(f"\n=== Collection Summary ===")
    print(f"Organization: {args.organization}")
    print(f"Total repositories: {len(collector.repositories)}")
    print(f"Output directory: {output_dir}")
    
    if collector.repositories:
        total_stars = sum(r.stars_count for r in collector.repositories)
        total_forks = sum(r.forks_count for r in collector.repositories)
        print(f"Total stars: {total_stars:,}")
        print(f"Total forks: {total_forks:,}")


if __name__ == '__main__':
    main()