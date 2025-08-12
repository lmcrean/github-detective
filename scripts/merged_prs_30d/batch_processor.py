"""Batch processor for handling multiple organizations' PR data."""

import os
from datetime import datetime
from typing import List, Dict, Tuple
from add_pr_column import process_org_csv


def process_multiple_orgs(org_configs: Dict[str, str], output_dir: str = None) -> Dict[str, str]:
    """
    Process multiple organizations' CSV files to add PR metrics.
    
    Args:
        org_configs: Dictionary mapping org names to their CSV paths
        output_dir: Optional output directory for processed files
    
    Returns:
        Dictionary mapping org names to output file paths
    """
    results = {}
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    for org_name, input_csv in org_configs.items():
        if not os.path.exists(input_csv):
            print(f"Warning: Input file not found for {org_name}: {input_csv}")
            continue
        
        print(f"\n{'='*50}")
        print(f"Processing {org_name.upper()}")
        print(f"{'='*50}")
        
        # Generate output path
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            filename = os.path.basename(input_csv)
            output_csv = os.path.join(
                output_dir,
                filename.replace('.csv', f'_with_prs_{timestamp}.csv')
            )
        else:
            output_csv = None  # Let process_org_csv handle it
        
        try:
            # Process the organization's data
            output_path = process_org_csv(
                org_name,
                input_csv,
                f'with_prs_{timestamp}' if not output_dir else None
            )
            
            if output_dir and output_csv:
                # Move to specified output directory if needed
                import shutil
                shutil.move(output_path, output_csv)
                output_path = output_csv
            
            results[org_name] = output_path
            print(f"[SUCCESS] Successfully processed {org_name}")
            
        except Exception as e:
            print(f"[ERROR] Error processing {org_name}: {str(e)}")
            results[org_name] = None
    
    print(f"\n{'='*50}")
    print("BATCH PROCESSING COMPLETE")
    print(f"{'='*50}")
    print(f"Processed {len([v for v in results.values() if v])} out of {len(org_configs)} organizations")
    
    return results


def get_org_latest_files(base_dir: str = "data/orgs") -> Dict[str, str]:
    """
    Get latest CSV files for all organizations.
    
    Args:
        base_dir: Base directory containing org subdirectories
    
    Returns:
        Dictionary mapping org names to their latest CSV paths
    """
    org_files = {}
    
    if not os.path.exists(base_dir):
        print(f"Base directory not found: {base_dir}")
        return org_files
    
    for org_name in os.listdir(base_dir):
        org_dir = os.path.join(base_dir, org_name)
        if os.path.isdir(org_dir):
            latest_file = os.path.join(org_dir, f"{org_name}_repos_latest.csv")
            if os.path.exists(latest_file):
                org_files[org_name] = latest_file
            else:
                # Try to find any CSV file
                csv_files = [f for f in os.listdir(org_dir) if f.endswith('.csv')]
                if csv_files:
                    # Use the most recent one
                    csv_files.sort()
                    org_files[org_name] = os.path.join(org_dir, csv_files[-1])
    
    return org_files


if __name__ == "__main__":
    # Process Stripe and Shopify specifically
    org_configs = {
        'stripe': 'data/orgs/stripe/stripe_repos_latest.csv',
        'shopify': 'data/orgs/shopify/shopify_repos_latest.csv'
    }
    
    print("Starting batch processing for Stripe and Shopify...")
    results = process_multiple_orgs(org_configs)
    
    print("\nResults:")
    for org, output_file in results.items():
        if output_file:
            print(f"  {org}: {output_file}")
        else:
            print(f"  {org}: Failed to process")