"""Add merged_prs_30d column to existing CSV files."""

import csv
import os
from datetime import datetime
from typing import Dict, List
from .fetch_merged_prs import MergedPRsFetcher


def add_merged_prs_column(input_csv: str, output_csv: str, pr_data: Dict[str, int]) -> None:
    """
    Add merged_prs_30d column to CSV file.
    
    Args:
        input_csv: Path to input CSV file
        output_csv: Path to output CSV file with added column
        pr_data: Dictionary mapping "org/repo" to merged PR count
    """
    with open(input_csv, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['merged_prs_30d']
        
        with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in reader:
                # Create key from org and repo names
                key = f"{row['org_name']}/{row['repo_name']}"
                
                # Add merged PRs count
                row['merged_prs_30d'] = pr_data.get(key, 0)
                
                writer.writerow(row)
    
    print(f"Added merged_prs_30d column to {output_csv}")


def process_org_csv(org_name: str, input_csv: str, output_suffix: str = None) -> str:
    """
    Process a single organization's CSV file to add PR metrics.
    
    Args:
        org_name: Organization name
        input_csv: Path to input CSV
        output_suffix: Optional suffix for output file
    
    Returns:
        Path to output CSV file
    """
    # Read repositories from CSV
    repos = []
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            repos.append({
                'org_name': row['org_name'],
                'repo_name': row['repo_name']
            })
    
    print(f"Found {len(repos)} repositories for {org_name}")
    
    # Fetch merged PRs data
    fetcher = MergedPRsFetcher()
    pr_data = fetcher.get_batch_merged_prs(repos, days=30)
    
    # Generate output filename
    if output_suffix:
        output_csv = input_csv.replace('.csv', f'_{output_suffix}.csv')
    else:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_csv = input_csv.replace('.csv', f'_with_prs_{timestamp}.csv')
    
    # Add column to CSV
    add_merged_prs_column(input_csv, output_csv, pr_data)
    
    return output_csv


if __name__ == "__main__":
    # Test with existing data
    test_orgs = {
        'stripe': 'data/orgs/stripe/stripe_repos_latest.csv',
        'shopify': 'data/orgs/shopify/shopify_repos_latest.csv'
    }
    
    for org, csv_path in test_orgs.items():
        if os.path.exists(csv_path):
            print(f"\nProcessing {org}...")
            output = process_org_csv(org, csv_path, 'test_prs')
            print(f"Output saved to: {output}")
        else:
            print(f"File not found: {csv_path}")