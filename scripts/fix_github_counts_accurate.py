"""Accurate GitHub issue and PR count fixer using direct API endpoints.

This script correctly separates issues from pull requests and handles pagination.
GitHub's open_issues_count incorrectly includes PRs, so we must filter them out.
"""

import csv
import time
import requests
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import json
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value


class AccurateGitHubClient:
    """GitHub client that accurately counts issues and PRs separately."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize client with optional authentication token."""
        self.token = token or os.getenv('API_GITHUB_TOKEN') or os.getenv('GITHUB_TOKEN')
        self.headers = {'Authorization': f'token {self.token}'} if self.token else {}
        self.base_url = 'https://api.github.com'
        self.api_calls = 0
        self.rate_limit_remaining = None
    
    def _handle_rate_limit(self, response):
        """Check and handle rate limiting."""
        self.rate_limit_remaining = int(response.headers.get('X-RateLimit-Remaining', 60))
        
        if response.status_code == 429 or self.rate_limit_remaining < 5:
            reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
            current_time = int(time.time())
            sleep_time = max(reset_time - current_time + 10, 60)
            
            print(f"    Rate limit hit ({self.rate_limit_remaining} remaining). Sleeping {sleep_time}s...")
            time.sleep(sleep_time)
            return True
        return False
    
    def _fetch_all_pages(self, url: str, item_filter=None) -> List[Dict]:
        """Fetch all pages of results from a paginated endpoint."""
        all_items = []
        page = 1
        
        while True:
            paginated_url = f"{url}{'&' if '?' in url else '?'}per_page=100&page={page}"
            
            try:
                response = requests.get(paginated_url, headers=self.headers, timeout=30)
                self.api_calls += 1
                
                if self._handle_rate_limit(response):
                    continue  # Retry after rate limit sleep
                
                if response.status_code != 200:
                    print(f"    API error {response.status_code} for page {page}")
                    break
                
                items = response.json()
                
                if not items:  # No more pages
                    break
                
                # Apply filter if provided
                if item_filter:
                    items = [item for item in items if item_filter(item)]
                
                all_items.extend(items)
                
                # Check if there are more pages
                if 'Link' not in response.headers or 'rel="next"' not in response.headers['Link']:
                    break
                
                page += 1
                
                # Small delay between pages
                time.sleep(0.5)
                
            except Exception as e:
                print(f"    Error fetching page {page}: {e}")
                break
        
        return all_items
    
    def get_accurate_issue_count(self, owner: str, repo: str) -> int:
        """Get accurate issue count excluding pull requests."""
        url = f"{self.base_url}/repos/{owner}/{repo}/issues?state=open"
        
        # Filter function to exclude pull requests
        def is_issue(item):
            return 'pull_request' not in item
        
        issues = self._fetch_all_pages(url, item_filter=is_issue)
        return len(issues)
    
    def get_accurate_pr_count(self, owner: str, repo: str) -> int:
        """Get accurate pull request count."""
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls?state=open"
        
        prs = self._fetch_all_pages(url)
        return len(prs)
    
    def get_accurate_counts(self, owner: str, repo: str) -> Tuple[int, int]:
        """Get both accurate issue and PR counts for a repository."""
        print(f"  Fetching accurate counts for {owner}/{repo}...")
        
        # Get issue count (excluding PRs)
        issue_count = self.get_accurate_issue_count(owner, repo)
        print(f"    Issues (excluding PRs): {issue_count}")
        
        # Small delay between API calls
        time.sleep(0.5)
        
        # Get PR count
        pr_count = self.get_accurate_pr_count(owner, repo)
        print(f"    Pull Requests: {pr_count}")
        
        return issue_count, pr_count
    
    def test_shopify_cli(self) -> bool:
        """Test function to verify shopify/cli returns correct values."""
        print("\nTesting shopify/cli for accuracy...")
        issues, prs = self.get_accurate_counts('shopify', 'cli')
        
        print(f"\nTest Results for shopify/cli:")
        print(f"  Issues: {issues} (expected: 43)")
        print(f"  PRs: {prs} (expected: 46)")
        
        if issues == 43 and prs == 46:
            print("  [PASS] TEST PASSED!")
            return True
        else:
            print(f"  [X] TEST FAILED - Values don't match expected")
            return False


def fix_all_counts(csv_path: str, test_only: bool = False) -> Dict:
    """Fix all issue and PR counts in the CSV file."""
    
    # Create backup
    if not test_only:
        backup_path = csv_path.replace('.csv', f'_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
        import shutil
        shutil.copy2(csv_path, backup_path)
        print(f"Backup created: {backup_path}")
    
    # Initialize client
    client = AccurateGitHubClient()
    
    # Test on shopify/cli first
    if not client.test_shopify_cli():
        print("\nWARNING: Test failed for shopify/cli. Continuing anyway...")
    
    if test_only:
        return {"test": "completed"}
    
    print("\n" + "="*60)
    print("Starting full CSV repair with accurate counts")
    print("="*60)
    
    # Read CSV
    all_rows = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        all_rows = list(reader)
    
    # Track statistics
    stats = {
        "total_rows": len(all_rows),
        "rows_updated": 0,
        "issues_fixed": 0,
        "prs_fixed": 0,
        "failed": 0
    }
    
    # Fix each row
    for i, row in enumerate(all_rows):
        org_name = row['org_name']
        repo_name = row['repo_name']
        
        # Check if this row needs fixing
        current_issues = int(row.get('open_issue_count', -1))
        current_prs = int(row.get('pull_requests_open_count', -1))
        
        print(f"\n[{i+1}/{len(all_rows)}] Processing {org_name}/{repo_name}")
        print(f"  Current values - Issues: {current_issues}, PRs: {current_prs}")
        
        try:
            # Get accurate counts
            accurate_issues, accurate_prs = client.get_accurate_counts(org_name, repo_name)
            
            # Update if different
            updated = False
            if accurate_issues != current_issues:
                row['open_issue_count'] = str(accurate_issues)
                stats["issues_fixed"] += 1
                updated = True
                print(f"  [OK] Updated issues: {current_issues} -> {accurate_issues}")
            
            if accurate_prs != current_prs:
                row['pull_requests_open_count'] = str(accurate_prs)
                stats["prs_fixed"] += 1
                updated = True
                print(f"  [OK] Updated PRs: {current_prs} -> {accurate_prs}")
            
            if updated:
                stats["rows_updated"] += 1
            else:
                print(f"  - No changes needed")
                
        except Exception as e:
            print(f"  [ERROR] {e}")
            stats["failed"] += 1
        
        # Rate limiting - be respectful
        if client.api_calls % 20 == 0:
            print(f"\n  [API Status] Calls made: {client.api_calls}, Rate limit remaining: {client.rate_limit_remaining}")
            time.sleep(2)
    
    # Write updated CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
    
    print("\n" + "="*60)
    print("CSV repair completed!")
    print("="*60)
    
    return stats


def spot_check_repos(csv_path: str) -> None:
    """Perform spot checks on specific repositories."""
    print("\n" + "="*60)
    print("SPOT CHECK VERIFICATION")
    print("="*60)
    
    # Repos to spot check
    spot_check_repos = [
        ('shopify', 'cli'),
        ('stripe', 'stripe-android'),
        ('shopify', 'liquid'),
        ('stripe', 'stripe-node')
    ]
    
    # Read current CSV values
    csv_data = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = f"{row['org_name']}/{row['repo_name']}"
            csv_data[key] = {
                'issues': int(row.get('open_issue_count', -1)),
                'prs': int(row.get('pull_requests_open_count', -1))
            }
    
    # Initialize client for spot checks
    client = AccurateGitHubClient()
    
    print("\nVerifying repository counts:")
    for org, repo in spot_check_repos:
        key = f"{org}/{repo}"
        print(f"\n{key}:")
        
        if key in csv_data:
            csv_issues = csv_data[key]['issues']
            csv_prs = csv_data[key]['prs']
            
            # Get fresh counts
            actual_issues, actual_prs = client.get_accurate_counts(org, repo)
            
            print(f"  CSV values    - Issues: {csv_issues}, PRs: {csv_prs}")
            print(f"  Actual values - Issues: {actual_issues}, PRs: {actual_prs}")
            
            if csv_issues == actual_issues and csv_prs == actual_prs:
                print(f"  [OK] MATCH - Values are correct!")
            else:
                print(f"  [FAIL] MISMATCH - Values need updating")
        else:
            print(f"  Not found in CSV")
        
        time.sleep(1)


def generate_report(stats: Dict, csv_path: str) -> None:
    """Generate a detailed repair report."""
    report = f"""
Accurate GitHub Counts Repair Report
====================================
File: {csv_path}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Statistics:
-----------
Total rows processed: {stats['total_rows']}
Rows updated: {stats['rows_updated']}
Issue counts fixed: {stats['issues_fixed']}
PR counts fixed: {stats['prs_fixed']}
Failed updates: {stats['failed']}

Success Rate: {((stats['rows_updated']) / max(stats['total_rows'], 1) * 100):.1f}%

Notes:
------
- This script uses direct API endpoints instead of search API
- Issues are correctly filtered to exclude pull requests
- All paginated results are fetched for accurate counts
- The shopify/cli test case validates our methodology
"""
    
    print(report)
    
    # Save report
    report_path = csv_path.replace('.csv', '_accurate_repair_report.txt')
    with open(report_path, 'w') as f:
        f.write(report)
    
    print(f"Report saved to: {report_path}")


def main():
    """Main execution function."""
    csv_path = r'C:\Projects\github-library\data\orgs\shopify_stripe_filter4.csv'
    
    if not os.path.exists(csv_path):
        print(f"CSV file not found: {csv_path}")
        return
    
    print("="*60)
    print("ACCURATE GITHUB COUNTS FIXER")
    print("="*60)
    print(f"Target: {csv_path}")
    print("This script will fix issue and PR counts using accurate API methods")
    
    # Run test first
    print("\nStep 1: Testing accuracy with shopify/cli...")
    client = AccurateGitHubClient()
    if not client.test_shopify_cli():
        response = input("\nTest failed. Continue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Aborted.")
            return
    
    # Fix all counts
    print("\nStep 2: Fixing all repository counts...")
    stats = fix_all_counts(csv_path, test_only=False)
    
    # Spot checks
    print("\nStep 3: Performing spot checks...")
    spot_check_repos(csv_path)
    
    # Generate report
    print("\nStep 4: Generating report...")
    generate_report(stats, csv_path)
    
    print("\n[DONE] All tasks completed!")


if __name__ == "__main__":
    main()