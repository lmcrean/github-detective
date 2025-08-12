"""Fix open issue and pull request counts in CSV files.

This script repairs -1 values in CSV files by re-fetching accurate data from GitHub API.
It specifically addresses issues with open_issue_count and pull_requests_open_count columns.
"""

import csv
import time
import requests
from typing import Dict, List, Optional, Tuple
import os
from datetime import datetime


class EnhancedGitHubClient:
    """Enhanced GitHub client with improved error handling and rate limiting."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize client with optional authentication token."""
        self.token = token or os.getenv('GITHUB_TOKEN')
        self.headers = {'Authorization': f'token {self.token}'} if self.token else {}
        self.base_url = 'https://api.github.com'
        self.rate_limit_remaining = None
        self.rate_limit_reset = None
    
    def _check_rate_limit(self, response):
        """Check and handle rate limiting."""
        self.rate_limit_remaining = int(response.headers.get('X-RateLimit-Remaining', 0))
        self.rate_limit_reset = int(response.headers.get('X-RateLimit-Reset', 0))
        
        if response.status_code == 429 or self.rate_limit_remaining < 10:
            reset_time = self.rate_limit_reset
            current_time = int(time.time())
            sleep_time = max(reset_time - current_time + 60, 60)  # Add 60s buffer
            
            print(f"Rate limit reached. Sleeping for {sleep_time} seconds...")
            time.sleep(sleep_time)
            return True
        return False
    
    def _make_request_with_retry(self, url: str, max_retries: int = 3) -> Optional[requests.Response]:
        """Make request with exponential backoff retry."""
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=self.headers, timeout=30)
                
                # Handle rate limiting
                if self._check_rate_limit(response):
                    continue  # Retry after sleep
                
                if response.status_code == 200:
                    return response
                elif response.status_code == 404:
                    print(f"Repository not found: {url}")
                    return None
                elif response.status_code == 403:
                    print(f"Access denied (private repo?): {url}")
                    return None
                else:
                    print(f"API error {response.status_code} for {url}")
                    
            except requests.exceptions.RequestException as e:
                print(f"Request error (attempt {attempt + 1}): {e}")
                
            # Exponential backoff
            if attempt < max_retries - 1:
                sleep_time = 2 ** attempt
                print(f"Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
        
        print(f"Failed to fetch data after {max_retries} attempts: {url}")
        return None
    
    def get_accurate_open_issues_count(self, owner: str, repo: str) -> int:
        """Get accurate open issues count excluding pull requests."""
        search_url = f'{self.base_url}/search/issues?q=is:issue+is:open+repo:{owner}/{repo}'
        
        response = self._make_request_with_retry(search_url)
        if response:
            data = response.json()
            return data.get('total_count', 0)
        
        print(f"Failed to get issues count for {owner}/{repo}")
        return -1
    
    def get_accurate_open_prs_count(self, owner: str, repo: str) -> int:
        """Get accurate open pull requests count."""
        search_url = f'{self.base_url}/search/issues?q=is:pr+is:open+repo:{owner}/{repo}'
        
        response = self._make_request_with_retry(search_url)
        if response:
            data = response.json()
            return data.get('total_count', 0)
        
        print(f"Failed to get PRs count for {owner}/{repo}")
        return -1
    
    def get_repo_counts(self, owner: str, repo: str) -> Tuple[int, int]:
        """Get both open issues and PRs counts efficiently."""
        print(f"Fetching counts for {owner}/{repo}")
        
        issues_count = self.get_accurate_open_issues_count(owner, repo)
        time.sleep(0.5)  # Small delay between API calls
        prs_count = self.get_accurate_open_prs_count(owner, repo)
        
        return issues_count, prs_count


def identify_rows_needing_repair(csv_path: str) -> List[Dict]:
    """Identify CSV rows that need repair (where counts = -1)."""
    rows_to_fix = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row_idx, row in enumerate(reader):
            needs_repair = False
            
            # Check if open_issue_count needs repair
            if row.get('open_issue_count', '0') == '-1':
                needs_repair = True
                
            # Check if pull_requests_open_count needs repair
            if row.get('pull_requests_open_count', '0') == '-1':
                needs_repair = True
            
            if needs_repair:
                row['_row_index'] = row_idx
                rows_to_fix.append(row)
    
    return rows_to_fix


def fix_csv_counts(csv_path: str, backup: bool = True) -> Dict:
    """Fix open issue and PR counts in CSV file."""
    
    # Create backup if requested
    if backup:
        backup_path = csv_path.replace('.csv', f'_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
        import shutil
        shutil.copy2(csv_path, backup_path)
        print(f"Backup created: {backup_path}")
    
    # Identify rows needing repair
    rows_to_fix = identify_rows_needing_repair(csv_path)
    
    if not rows_to_fix:
        print("No rows need repair - all counts look good!")
        return {"total_rows": 0, "fixed_issues": 0, "fixed_prs": 0, "failed": 0}
    
    print(f"Found {len(rows_to_fix)} rows needing repair")
    
    # Initialize GitHub client
    client = EnhancedGitHubClient()
    
    # Track statistics
    stats = {
        "total_rows": len(rows_to_fix),
        "fixed_issues": 0,
        "fixed_prs": 0,
        "failed": 0
    }
    
    # Read all rows from CSV
    all_rows = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        all_rows = list(reader)
    
    # Fix each row that needs repair
    for i, row_to_fix in enumerate(rows_to_fix):
        org_name = row_to_fix['org_name']
        repo_name = row_to_fix['repo_name']
        row_idx = row_to_fix['_row_index']
        
        print(f"Fixing {i+1}/{len(rows_to_fix)}: {org_name}/{repo_name}")
        
        # Get accurate counts
        issues_count, prs_count = client.get_repo_counts(org_name, repo_name)
        
        # Update the row in all_rows
        if issues_count != -1:
            all_rows[row_idx]['open_issue_count'] = str(issues_count)
            stats["fixed_issues"] += 1
        
        if prs_count != -1:
            all_rows[row_idx]['pull_requests_open_count'] = str(prs_count)
            stats["fixed_prs"] += 1
        
        if issues_count == -1 and prs_count == -1:
            stats["failed"] += 1
        
        # Small delay to be respectful to API
        time.sleep(1)
    
    # Write updated CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
    
    return stats


def generate_repair_report(stats: Dict, csv_path: str) -> str:
    """Generate a repair report."""
    report = f"""
CSV Repair Report
================
File: {csv_path}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Statistics:
- Total rows processed: {stats['total_rows']}
- Issues count fixed: {stats['fixed_issues']}
- PRs count fixed: {stats['fixed_prs']}
- Failed repairs: {stats['failed']}

Success rate: {((stats['fixed_issues'] + stats['fixed_prs']) / (stats['total_rows'] * 2) * 100):.1f}%
"""
    
    return report


def main():
    """Main execution function."""
    csv_path = r'C:\Projects\github-library\data\orgs\shopify_stripe_filter4.csv'
    
    if not os.path.exists(csv_path):
        print(f"CSV file not found: {csv_path}")
        return
    
    print(f"Starting CSV repair process for: {csv_path}")
    print("This will fix -1 values in open_issue_count and pull_requests_open_count columns")
    
    # Fix the CSV
    stats = fix_csv_counts(csv_path, backup=True)
    
    # Generate and display report
    report = generate_repair_report(stats, csv_path)
    print(report)
    
    # Save report to file
    report_path = csv_path.replace('.csv', '_repair_report.txt')
    with open(report_path, 'w') as f:
        f.write(report)
    
    print(f"Repair complete! Report saved to: {report_path}")


if __name__ == "__main__":
    main()