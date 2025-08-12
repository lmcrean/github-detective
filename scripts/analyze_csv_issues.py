"""Analyze which rows in CSV need repair without making API calls."""

import csv


def analyze_csv_issues(csv_path: str):
    """Analyze CSV to identify rows needing repair."""
    
    total_rows = 0
    issues_needing_repair = []
    prs_needing_repair = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row_idx, row in enumerate(reader):
            total_rows += 1
            
            # Check for -1 values
            if row.get('open_issue_count', '0') == '-1':
                issues_needing_repair.append({
                    'row': row_idx + 1,
                    'org': row['org_name'],
                    'repo': row['repo_name']
                })
            
            if row.get('pull_requests_open_count', '0') == '-1':
                prs_needing_repair.append({
                    'row': row_idx + 1,
                    'org': row['org_name'],
                    'repo': row['repo_name']
                })
    
    print(f"CSV Analysis Results")
    print(f"==================")
    print(f"Total rows: {total_rows}")
    print(f"Rows with open_issue_count = -1: {len(issues_needing_repair)}")
    print(f"Rows with pull_requests_open_count = -1: {len(prs_needing_repair)}")
    
    if issues_needing_repair:
        print(f"\nRepositories needing open_issue_count repair:")
        for item in issues_needing_repair[:10]:  # Show first 10
            print(f"  Row {item['row']}: {item['org']}/{item['repo']}")
        if len(issues_needing_repair) > 10:
            print(f"  ... and {len(issues_needing_repair) - 10} more")
    
    if prs_needing_repair:
        print(f"\nRepositories needing pull_requests_open_count repair:")
        for item in prs_needing_repair[:10]:  # Show first 10
            print(f"  Row {item['row']}: {item['org']}/{item['repo']}")
        if len(prs_needing_repair) > 10:
            print(f"  ... and {len(prs_needing_repair) - 10} more")
    
    return len(issues_needing_repair), len(prs_needing_repair)


if __name__ == "__main__":
    csv_path = r'C:\Projects\github-library\data\orgs\shopify_stripe_filter4.csv'
    analyze_csv_issues(csv_path)