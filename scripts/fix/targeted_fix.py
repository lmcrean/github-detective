"""Targeted fix for specific problematic rows in CSV."""

import csv
import time
from datetime import datetime
from fix_github_counts_fallback import FallbackGitHubClient

def targeted_fix():
    """Fix only the rows that need it."""
    
    csv_path = r'C:\Projects\github-library\data\orgs\shopify_stripe_filter4.csv'
    
    # Create backup
    backup_path = csv_path.replace('.csv', f'_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
    import shutil
    shutil.copy2(csv_path, backup_path)
    print(f"Backup created: {backup_path}")
    
    # Initialize client
    client = FallbackGitHubClient()
    
    # Read CSV
    all_rows = []
    rows_to_fix = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        
        for idx, row in enumerate(reader):
            all_rows.append(row)
            
            # Check if this row needs fixing
            issues = int(row.get('open_issue_count', -1))
            prs = int(row.get('pull_requests_open_count', -1))
            
            # Fix if:
            # 1. PRs are -1 (definitely wrong)
            # 2. shopify/cli specifically (we know it's wrong)
            # 3. open_issue_count seems to include PRs (suspicious high counts)
            
            needs_fix = False
            
            if prs == -1:
                needs_fix = True
            elif row['org_name'] == 'shopify' and row['repo_name'] == 'cli':
                needs_fix = True  # We know this one is wrong
            elif issues > 50 and prs == 0:  # Suspicious - high issues but 0 PRs
                needs_fix = True
            
            if needs_fix:
                rows_to_fix.append((idx, row))
    
    print(f"Found {len(rows_to_fix)} rows to fix out of {len(all_rows)} total")
    
    # Fix targeted rows
    fixed = 0
    failed = 0
    
    for idx, row in rows_to_fix:
        org_name = row['org_name']
        repo_name = row['repo_name']
        
        print(f"\nFixing {org_name}/{repo_name} (row {idx+1})")
        print(f"  Current: issues={row['open_issue_count']}, PRs={row['pull_requests_open_count']}")
        
        try:
            new_issues, new_prs = client.get_counts_with_fallback(org_name, repo_name)
            
            if new_issues >= 0:
                all_rows[idx]['open_issue_count'] = str(new_issues)
            if new_prs >= 0:
                all_rows[idx]['pull_requests_open_count'] = str(new_prs)
            
            print(f"  Fixed: issues={new_issues}, PRs={new_prs}")
            fixed += 1
            
        except Exception as e:
            print(f"  Error: {e}")
            failed += 1
        
        # Rate limiting
        time.sleep(1)
        
        # Early exit after fixing key repos for testing
        if fixed >= 10:
            print("\nFixed first 10 repos for testing...")
            break
    
    # Write updated CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
    
    print(f"\nFixed {fixed} rows, {failed} failures")
    
    # Spot check shopify/cli
    print("\n" + "="*60)
    print("SPOT CHECK: shopify/cli")
    
    for row in all_rows:
        if row['org_name'] == 'shopify' and row['repo_name'] == 'cli':
            print(f"  Issues: {row['open_issue_count']} (expected: 43)")
            print(f"  PRs: {row['pull_requests_open_count']} (expected: 46)")
            
            if row['open_issue_count'] == '43' and row['pull_requests_open_count'] == '46':
                print("  [SUCCESS] shopify/cli correctly fixed!")
            break
    
    print("="*60)

if __name__ == "__main__":
    targeted_fix()