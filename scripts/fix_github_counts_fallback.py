"""Fix GitHub counts using a fallback calculation method.

For repositories where the issues endpoint returns empty (like shopify/cli),
we calculate: issues = open_issues_count - pull_requests_count
"""

import csv
import time
import requests
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value


class FallbackGitHubClient:
    """GitHub client with fallback calculation for restricted repos."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize client with optional authentication token."""
        self.token = token or os.getenv('API_GITHUB_TOKEN') or os.getenv('GITHUB_TOKEN')
        self.headers = {'Authorization': f'token {self.token}'} if self.token else {}
        self.base_url = 'https://api.github.com'
        self.api_calls = 0
    
    def get_counts_with_fallback(self, owner: str, repo: str) -> Tuple[int, int]:
        """Get issue and PR counts with fallback calculation."""
        
        # First, get repository data
        repo_url = f"{self.base_url}/repos/{owner}/{repo}"
        repo_resp = requests.get(repo_url, headers=self.headers)
        self.api_calls += 1
        
        if repo_resp.status_code != 200:
            print(f"    Error fetching repo data: {repo_resp.status_code}")
            return -1, -1
        
        repo_data = repo_resp.json()
        total_open_issues = repo_data.get('open_issues_count', 0)
        
        # Get PR count from pulls endpoint (this usually works)
        pulls_url = f"{self.base_url}/repos/{owner}/{repo}/pulls?state=open&per_page=100"
        pulls_resp = requests.get(pulls_url, headers=self.headers)
        self.api_calls += 1
        
        if pulls_resp.status_code == 200:
            pr_count = len(pulls_resp.json())
            
            # Check if there are more pages
            if 'Link' in pulls_resp.headers and 'rel="next"' in pulls_resp.headers['Link']:
                # Need to count all pages
                pr_count = self._count_all_prs(owner, repo)
        else:
            print(f"    Error fetching PRs: {pulls_resp.status_code}")
            pr_count = -1
        
        # Try to get issues directly first
        issues_url = f"{self.base_url}/repos/{owner}/{repo}/issues?state=open&per_page=100"
        issues_resp = requests.get(issues_url, headers=self.headers)
        self.api_calls += 1
        
        if issues_resp.status_code == 200:
            items = issues_resp.json()
            
            if len(items) > 0:
                # Issues endpoint works - count properly
                issue_count = len([i for i in items if 'pull_request' not in i])
                
                # Check for pagination
                if 'Link' in issues_resp.headers and 'rel="next"' in issues_resp.headers['Link']:
                    issue_count = self._count_all_issues(owner, repo)
            else:
                # Issues endpoint returns empty - use fallback calculation
                if pr_count >= 0:
                    issue_count = total_open_issues - pr_count
                    print(f"    Using fallback calculation: {total_open_issues} total - {pr_count} PRs = {issue_count} issues")
                else:
                    issue_count = -1
        else:
            # Issues endpoint failed - use fallback
            if pr_count >= 0:
                issue_count = total_open_issues - pr_count
                print(f"    Using fallback calculation: {total_open_issues} total - {pr_count} PRs = {issue_count} issues")
            else:
                issue_count = -1
        
        return issue_count, pr_count
    
    def _count_all_prs(self, owner: str, repo: str) -> int:
        """Count all PRs across paginated results."""
        total = 0
        page = 1
        
        while True:
            url = f"{self.base_url}/repos/{owner}/{repo}/pulls?state=open&per_page=100&page={page}"
            resp = requests.get(url, headers=self.headers)
            self.api_calls += 1
            
            if resp.status_code != 200:
                break
            
            items = resp.json()
            if not items:
                break
            
            total += len(items)
            
            if len(items) < 100:
                break
            
            page += 1
            time.sleep(0.5)
        
        return total
    
    def _count_all_issues(self, owner: str, repo: str) -> int:
        """Count all issues (excluding PRs) across paginated results."""
        total = 0
        page = 1
        
        while True:
            url = f"{self.base_url}/repos/{owner}/{repo}/issues?state=open&per_page=100&page={page}"
            resp = requests.get(url, headers=self.headers)
            self.api_calls += 1
            
            if resp.status_code != 200:
                break
            
            items = resp.json()
            if not items:
                break
            
            # Count only items without pull_request key
            issues = [i for i in items if 'pull_request' not in i]
            total += len(issues)
            
            if len(items) < 100:
                break
            
            page += 1
            time.sleep(0.5)
        
        return total


def test_shopify_cli():
    """Test shopify/cli to verify our approach works."""
    print("Testing shopify/cli with fallback method...")
    
    client = FallbackGitHubClient()
    issues, prs = client.get_counts_with_fallback('shopify', 'cli')
    
    print(f"\nResults:")
    print(f"  Issues: {issues} (expected: 43)")
    print(f"  PRs: {prs} (expected: 46)")
    
    if issues == 43 and prs == 46:
        print("  [SUCCESS] Test passed!")
        return True
    else:
        print("  [WARNING] Values don't match expected")
        return False


def fix_csv_with_fallback(csv_path: str) -> Dict:
    """Fix CSV using fallback calculation method."""
    
    # Create backup
    backup_path = csv_path.replace('.csv', f'_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
    import shutil
    shutil.copy2(csv_path, backup_path)
    print(f"Backup created: {backup_path}")
    
    # Initialize client
    client = FallbackGitHubClient()
    
    # Read CSV
    all_rows = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        all_rows = list(reader)
    
    stats = {
        "total_rows": len(all_rows),
        "rows_updated": 0,
        "issues_fixed": 0,
        "prs_fixed": 0,
        "failed": 0
    }
    
    # Process each row
    for i, row in enumerate(all_rows):
        org_name = row['org_name']
        repo_name = row['repo_name']
        
        current_issues = int(row.get('open_issue_count', -1))
        current_prs = int(row.get('pull_requests_open_count', -1))
        
        # Skip if both values are already valid (not -1)
        if current_issues >= 0 and current_prs >= 0 and current_prs != -1:
            continue
        
        print(f"\n[{i+1}/{len(all_rows)}] {org_name}/{repo_name}")
        print(f"  Current: Issues={current_issues}, PRs={current_prs}")
        
        try:
            new_issues, new_prs = client.get_counts_with_fallback(org_name, repo_name)
            
            updated = False
            
            # Update issues if we got a valid value and it's different
            if new_issues >= 0 and new_issues != current_issues:
                row['open_issue_count'] = str(new_issues)
                stats["issues_fixed"] += 1
                updated = True
                print(f"  Updated issues: {current_issues} -> {new_issues}")
            
            # Update PRs if we got a valid value and it's different
            if new_prs >= 0 and (new_prs != current_prs or current_prs == -1):
                row['pull_requests_open_count'] = str(new_prs)
                stats["prs_fixed"] += 1
                updated = True
                print(f"  Updated PRs: {current_prs} -> {new_prs}")
            
            if updated:
                stats["rows_updated"] += 1
            
        except Exception as e:
            print(f"  Error: {e}")
            stats["failed"] += 1
        
        # Rate limiting
        if client.api_calls % 30 == 0:
            print(f"  [Rate limit check - {client.api_calls} API calls made]")
            time.sleep(2)
    
    # Write updated CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
    
    print("\n" + "="*60)
    print("CSV repair completed!")
    print(f"Rows updated: {stats['rows_updated']}")
    print(f"Issues fixed: {stats['issues_fixed']}")
    print(f"PRs fixed: {stats['prs_fixed']}")
    print("="*60)
    
    return stats


def spot_check(csv_path: str):
    """Perform spot check on shopify/cli after fix."""
    print("\n" + "="*60)
    print("SPOT CHECK: shopify/cli")
    print("="*60)
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['org_name'] == 'shopify' and row['repo_name'] == 'cli':
                print(f"CSV values for shopify/cli:")
                print(f"  open_issue_count: {row['open_issue_count']}")
                print(f"  pull_requests_open_count: {row['pull_requests_open_count']}")
                
                if row['open_issue_count'] == '43' and row['pull_requests_open_count'] == '46':
                    print("  [SUCCESS] Values match expected (43 issues, 46 PRs)!")
                else:
                    print("  [WARNING] Values don't match expected")
                break


def main():
    """Main execution."""
    csv_path = r'C:\Projects\github-library\data\orgs\shopify_stripe_filter4.csv'
    
    print("GitHub Counts Fixer with Fallback Calculation")
    print("="*60)
    
    # Test first
    if not test_shopify_cli():
        print("\nWarning: Test case shows unexpected values, but continuing...")
    
    # Fix CSV
    print("\nFixing CSV file...")
    stats = fix_csv_with_fallback(csv_path)
    
    # Spot check
    spot_check(csv_path)
    
    print("\n[DONE] Process completed!")


if __name__ == "__main__":
    main()