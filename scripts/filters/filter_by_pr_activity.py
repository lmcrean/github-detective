"""Filter 2: Process data after adding merged_prs_30d column."""

import csv
import os
from datetime import datetime
from typing import Dict


def apply_filter2(input_csv: str, output_csv: str, min_prs: int = 0) -> int:
    """
    Apply Filter 2 - currently just passes through data with merged_prs_30d column.
    Can be enhanced to filter based on PR activity thresholds.
    
    Args:
        input_csv: Path to input CSV (should have merged_prs_30d column)
        output_csv: Path to output CSV
        min_prs: Minimum number of merged PRs to keep (optional filtering)
    
    Returns:
        Number of repositories in output
    """
    kept_count = 0
    total_count = 0
    
    with open(input_csv, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        # Verify merged_prs_30d column exists
        if 'merged_prs_30d' not in fieldnames:
            print("Warning: merged_prs_30d column not found in input CSV")
        
        rows_to_keep = []
        
        for row in reader:
            total_count += 1
            
            # Optional: Filter by minimum PR activity
            if min_prs > 0 and 'merged_prs_30d' in row:
                try:
                    pr_count = int(row['merged_prs_30d'])
                    if pr_count < min_prs:
                        print(f"  Filtering out {row['org_name']}/{row['repo_name']} (merged PRs: {pr_count})")
                        continue
                except (ValueError, KeyError):
                    pass  # Keep rows with invalid PR counts
            
            rows_to_keep.append(row)
            kept_count += 1
    
    # Write data
    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_to_keep)
    
    print(f"Filter 2 complete: {kept_count}/{total_count} repositories")
    return kept_count


def apply_filter2_to_org(org_name: str, input_csv: str, min_prs: int = 0) -> str:
    """
    Apply Filter 2 to an organization's CSV file.
    
    Args:
        org_name: Organization name
        input_csv: Path to input CSV (should be filter1 output with merged_prs_30d)
        min_prs: Minimum merged PRs threshold
    
    Returns:
        Path to filtered output file
    """
    # Generate output filename with filter2 and date
    date_str = datetime.now().strftime('%Y%m%d')
    
    # Extract directory path
    dir_path = os.path.dirname(input_csv)
    output_csv = os.path.join(dir_path, f"{org_name}_repos_filter2_{date_str}.csv")
    
    print(f"\nApplying Filter 2 to {org_name}...")
    print(f"  Input: {input_csv}")
    print(f"  Output: {output_csv}")
    if min_prs > 0:
        print(f"  Minimum PRs threshold: {min_prs}")
    
    kept_count = apply_filter2(input_csv, output_csv, min_prs)
    
    return output_csv


def batch_filter2(org_configs: Dict[str, str], min_prs: int = 0) -> Dict[str, str]:
    """
    Apply Filter 2 to multiple organizations.
    
    Args:
        org_configs: Dictionary mapping org names to CSV paths (filter1 outputs)
        min_prs: Minimum merged PRs threshold
    
    Returns:
        Dictionary mapping org names to filtered output paths
    """
    results = {}
    
    for org_name, input_csv in org_configs.items():
        if not os.path.exists(input_csv):
            print(f"Warning: Input file not found for {org_name}: {input_csv}")
            continue
        
        try:
            output_path = apply_filter2_to_org(org_name, input_csv, min_prs)
            results[org_name] = output_path
            print(f"[SUCCESS] Successfully applied Filter 2 to {org_name}")
            
        except Exception as e:
            print(f"[ERROR] Error applying Filter 2 to {org_name}: {str(e)}")
            results[org_name] = None
    
    return results


if __name__ == "__main__":
    # Test with filter1 outputs
    date_str = datetime.now().strftime('%Y%m%d')
    test_configs = {
        'stripe': f'data/orgs/stripe/stripe_repos_filter1_{date_str}.csv',
        'shopify': f'data/orgs/shopify/shopify_repos_filter1_{date_str}.csv'
    }
    
    print("Testing Filter 2 (PR Activity Filter)...")
    
    # Check if filter1 outputs exist
    for org, path in test_configs.items():
        if not os.path.exists(path):
            print(f"Note: Filter 1 output not found for {org}. Run filter_by_date.py first.")
    
    results = batch_filter2(test_configs, min_prs=0)  # No minimum threshold for now
    
    print("\nFilter 2 Results:")
    for org, output_file in results.items():
        if output_file:
            print(f"  {org}: {output_file}")
        else:
            print(f"  {org}: Not processed")