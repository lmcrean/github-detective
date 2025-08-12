"""Filter 1: Remove repositories that were last pushed before March 2025."""

import csv
import os
from datetime import datetime
from typing import List, Dict


def filter_by_push_date(input_csv: str, output_csv: str, cutoff_date: str = "2025-03-01") -> int:
    """
    Filter out repositories pushed before the cutoff date.
    
    Args:
        input_csv: Path to input CSV file
        output_csv: Path to output CSV file
        cutoff_date: Date string in YYYY-MM-DD format
    
    Returns:
        Number of repositories kept after filtering
    """
    cutoff = datetime.strptime(cutoff_date, "%Y-%m-%d")
    kept_count = 0
    total_count = 0
    
    with open(input_csv, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        rows_to_keep = []
        
        for row in reader:
            total_count += 1
            
            # Parse the last_pushed_date
            push_date_str = row.get('last_pushed_date', '')
            
            if push_date_str:
                try:
                    push_date = datetime.strptime(push_date_str, "%Y-%m-%d")
                    
                    # Keep if pushed on or after cutoff date
                    if push_date >= cutoff:
                        rows_to_keep.append(row)
                        kept_count += 1
                    else:
                        print(f"  Filtering out {row['org_name']}/{row['repo_name']} (last pushed: {push_date_str})")
                        
                except ValueError as e:
                    print(f"  Warning: Invalid date format for {row['org_name']}/{row['repo_name']}: {push_date_str}")
                    # Keep rows with invalid dates (conservative approach)
                    rows_to_keep.append(row)
                    kept_count += 1
            else:
                # Keep rows without push date (conservative approach)
                rows_to_keep.append(row)
                kept_count += 1
    
    # Write filtered data
    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_to_keep)
    
    print(f"Filter 1 complete: Kept {kept_count}/{total_count} repositories (removed {total_count - kept_count})")
    return kept_count


def apply_filter1_to_org(org_name: str, input_csv: str, cutoff_date: str = "2025-03-01") -> str:
    """
    Apply Filter 1 to an organization's CSV file.
    
    Args:
        org_name: Organization name
        input_csv: Path to input CSV
        cutoff_date: Date cutoff in YYYY-MM-DD format
    
    Returns:
        Path to filtered output file
    """
    # Generate output filename with filter1 and date
    date_str = datetime.now().strftime('%Y%m%d')
    
    # Extract directory path
    dir_path = os.path.dirname(input_csv)
    output_csv = os.path.join(dir_path, f"{org_name}_repos_filter1_{date_str}.csv")
    
    print(f"\nApplying Filter 1 to {org_name}...")
    print(f"  Cutoff date: {cutoff_date}")
    print(f"  Input: {input_csv}")
    print(f"  Output: {output_csv}")
    
    kept_count = filter_by_push_date(input_csv, output_csv, cutoff_date)
    
    return output_csv


def batch_filter1(org_configs: Dict[str, str], cutoff_date: str = "2025-03-01") -> Dict[str, str]:
    """
    Apply Filter 1 to multiple organizations.
    
    Args:
        org_configs: Dictionary mapping org names to CSV paths
        cutoff_date: Date cutoff in YYYY-MM-DD format
    
    Returns:
        Dictionary mapping org names to filtered output paths
    """
    results = {}
    
    for org_name, input_csv in org_configs.items():
        if not os.path.exists(input_csv):
            print(f"Warning: Input file not found for {org_name}: {input_csv}")
            continue
        
        try:
            output_path = apply_filter1_to_org(org_name, input_csv, cutoff_date)
            results[org_name] = output_path
            print(f"[SUCCESS] Successfully filtered {org_name}")
            
        except Exception as e:
            print(f"[ERROR] Error filtering {org_name}: {str(e)}")
            results[org_name] = None
    
    return results


if __name__ == "__main__":
    # Test with sample data
    test_configs = {
        'stripe': 'data/orgs/stripe/stripe_repos_latest.csv',
        'shopify': 'data/orgs/shopify/shopify_repos_latest.csv'
    }
    
    print("Testing Filter 1 (Date Filter)...")
    results = batch_filter1(test_configs, "2025-03-01")
    
    print("\nFilter 1 Results:")
    for org, output_file in results.items():
        if output_file:
            print(f"  {org}: {output_file}")
        else:
            print(f"  {org}: Failed to filter")