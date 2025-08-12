"""Fix only pull_requests_open_count in CSV files where value is -1."""

import csv
import time
import requests
import os
from datetime import datetime
from typing import Optional


class GitHubPRFixer:
    """GitHub client specifically for fixing PR counts."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize client with optional authentication token."""
        self.token = token or os.getenv('GITHUB_TOKEN')
        self.headers = {'Authorization': f'token {self.token}'} if self.token else {}
        self.base_url = 'https://api.github.com'
        self.api_calls_made = 0
    
    def get_open_prs_count(self, owner: str, repo: str) -> int:
        """Get accurate open pull requests count."""
        search_url = f'{self.base_url}/search/issues?q=is:pr+is:open+repo:{owner}/{repo}'
        
        try:
            response = requests.get(search_url, headers=self.headers, timeout=30)
            self.api_calls_made += 1
            
            if response.status_code == 200:
                data = response.json()
                count = data.get('total_count', 0)
                print(f"  {owner}/{repo}: {count} open PRs")
                return count
            elif response.status_code == 429:
                print(f"  Rate limit hit, sleeping...")
                time.sleep(60)
                return self.get_open_prs_count(owner, repo)  # Retry once
            else:
                print(f"  API error {response.status_code} for {owner}/{repo}")
                return -1
                
        except Exception as e:
            print(f"  Request error for {owner}/{repo}: {e}")
            return -1


def fix_pr_counts_only(csv_path: str) -> None:
    """Fix only PR counts in CSV file."""
    
    # Create backup
    backup_path = csv_path.replace('.csv', f'_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
    import shutil
    shutil.copy2(csv_path, backup_path)
    print(f"Backup created: {backup_path}")
    
    # Read all rows
    all_rows = []
    rows_to_fix = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        
        for row_idx, row in enumerate(reader):
            all_rows.append(row)
            
            if row.get('pull_requests_open_count', '0') == '-1':
                rows_to_fix.append((row_idx, row))
    
    if not rows_to_fix:
        print("No PR counts need fixing!")
        return
    
    print(f"Found {len(rows_to_fix)} repositories needing PR count fixes")
    
    # Initialize GitHub client
    client = GitHubPRFixer()
    
    fixed_count = 0
    failed_count = 0
    
    # Process each row needing repair
    for i, (row_idx, row) in enumerate(rows_to_fix):
        org_name = row['org_name']
        repo_name = row['repo_name']
        
        print(f"Fixing {i+1}/{len(rows_to_fix)}: {org_name}/{repo_name}")
        
        # Get accurate PR count
        pr_count = client.get_open_prs_count(org_name, repo_name)
        
        if pr_count != -1:
            all_rows[row_idx]['pull_requests_open_count'] = str(pr_count)
            fixed_count += 1
        else:
            failed_count += 1
        
        # Rate limiting - be respectful
        if client.api_calls_made % 10 == 0:
            print(f"  Made {client.api_calls_made} API calls, taking a short break...")
            time.sleep(5)
        else:
            time.sleep(1)
    
    # Write updated CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
    
    # Generate report
    report = f"""
PR Count Repair Report
=====================
File: {csv_path}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Statistics:
- Total repositories processed: {len(rows_to_fix)}
- Successfully fixed: {fixed_count}
- Failed to fix: {failed_count}
- API calls made: {client.api_calls_made}

Success rate: {(fixed_count / len(rows_to_fix) * 100):.1f}%
"""
    
    print(report)
    
    # Save report
    report_path = csv_path.replace('.csv', '_pr_repair_report.txt')
    with open(report_path, 'w') as f:
        f.write(report)
    
    print(f"Report saved to: {report_path}")


if __name__ == "__main__":
    csv_path = r'C:\Projects\github-library\data\orgs\shopify_stripe_filter4.csv'
    
    if not os.path.exists(csv_path):
        print(f"CSV file not found: {csv_path}")
        exit(1)
    
    print(f"Starting PR count repair for: {csv_path}")
    print("This will fix -1 values in pull_requests_open_count column only")
    
    fix_pr_counts_only(csv_path)