"""Update shopify_stripe_filter3.csv with today's new issues."""

import os
import csv
import glob
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Set

def read_existing_filter3() -> Set[str]:
    """Read existing filter3.csv and return set of unique issue identifiers."""
    existing_issues = set()
    filter3_path = 'data/repos/shopify_stripe_filter3.csv'
    
    if os.path.exists(filter3_path):
        with open(filter3_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Create unique identifier from org, repo, and issue title
                unique_id = f"{row['org_name']}|{row['repo_name']}|{row['issue_title']}"
                existing_issues.add(unique_id)
    
    return existing_issues

def read_individual_repo_csvs() -> List[Dict]:
    """Read all individual repository CSV files and extract issues."""
    all_issues = []
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Find all individual repo CSV files
    csv_files = glob.glob('data/repos/*.csv')
    
    for csv_file in csv_files:
        # Skip the filter files
        if 'filter' in os.path.basename(csv_file):
            continue
            
        # Extract org and repo name from filename
        filename = os.path.basename(csv_file).replace('.csv', '')
        parts = filename.split('_')
        
        if len(parts) == 2:
            org_name = parts[0]
            repo_name = parts[1]
        else:
            continue
            
        # Read the CSV file
        with open(csv_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            # Skip metadata lines (those starting with #)
            data_lines = [line for line in lines if not line.startswith('#')]
            
            if data_lines:
                # Parse CSV data
                import io
                csv_data = io.StringIO(''.join(data_lines))
                reader = csv.DictReader(csv_data)
                
                for row in reader:
                    # Check if issue was opened today
                    opened_date = row.get('opened_date', '')
                    if opened_date == today:
                        issue = {
                            'org_name': org_name,
                            'repo_name': repo_name,
                            'issue_title': row.get('issue_title', ''),
                            'comments_count': row.get('comments_count', '0'),
                            'labels': row.get('labels', ''),
                            'opened_date': opened_date,
                            'hyperlink': row.get('hyperlink', '')
                        }
                        all_issues.append(issue)
    
    return all_issues

def update_filter3_csv(new_issues: List[Dict]):
    """Append new issues to filter3.csv, sorted by most recent first."""
    filter3_path = 'data/repos/shopify_stripe_filter3.csv'
    
    # Read existing data
    existing_data = []
    if os.path.exists(filter3_path):
        with open(filter3_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_data = list(reader)
    
    # Combine with new issues
    all_data = new_issues + existing_data
    
    # Sort by opened_date (most recent first)
    all_data.sort(key=lambda x: x.get('opened_date', ''), reverse=True)
    
    # Write back to file
    fieldnames = ['org_name', 'repo_name', 'issue_title', 'comments_count', 'labels', 'opened_date', 'hyperlink']
    
    with open(filter3_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)
    
    return len(new_issues), len(all_data)

def main():
    """Main execution function."""
    print("Updating shopify_stripe_filter3.csv with today's issues")
    print("=" * 60)
    
    # Read existing issues to avoid duplicates
    existing_issues = read_existing_filter3()
    print(f"Found {len(existing_issues)} existing issues in filter3.csv")
    
    # Read all individual repo CSVs and find today's issues
    todays_issues = read_individual_repo_csvs()
    print(f"Found {len(todays_issues)} issues opened today")
    
    # Filter out duplicates
    new_issues = []
    for issue in todays_issues:
        unique_id = f"{issue['org_name']}|{issue['repo_name']}|{issue['issue_title']}"
        if unique_id not in existing_issues:
            new_issues.append(issue)
    
    print(f"Found {len(new_issues)} new issues to add")
    
    if new_issues:
        # Update the CSV file
        added_count, total_count = update_filter3_csv(new_issues)
        
        print(f"\nSuccessfully updated filter3.csv:")
        print(f"  - Added {added_count} new issues")
        print(f"  - Total issues now: {total_count}")
        print(f"  - File sorted by most recent date first")
        
        print("\nNew issues added:")
        for issue in new_issues:
            print(f"  - [{issue['org_name']}/{issue['repo_name']}] {issue['issue_title'][:60]}...")
    else:
        print("\nNo new issues to add - filter3.csv is already up to date!")

if __name__ == '__main__':
    main()