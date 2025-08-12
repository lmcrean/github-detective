"""Reprocess Shopify repositories with failed merged_prs_30d values."""

import csv
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from scripts.merged_prs_30d.fetch_merged_prs import MergedPRsFetcher
from scripts.merged_prs_30d.identify_failed_repos import get_failed_repos_for_reprocessing


def update_csv_with_new_pr_data(csv_path: str, pr_data: Dict[str, int], output_path: str = None) -> str:
    """Update CSV file with new PR data, replacing -1 values where we got successful results."""
    if not output_path:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = csv_path.replace('.csv', f'_fixed_{timestamp}.csv')
    
    updated_count = 0
    
    with open(csv_path, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        rows = []
        for row in reader:
            key = f"{row['org_name']}/{row['repo_name']}"
            
            # Update if we have new data and the current value is -1
            if key in pr_data and row.get('merged_prs_30d', '').strip() == '-1':
                old_value = row['merged_prs_30d']
                row['merged_prs_30d'] = str(pr_data[key])
                print(f"Updated {key}: {old_value} -> {pr_data[key]}")
                updated_count += 1
            
            rows.append(row)
    
    # Write updated data
    with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Updated {updated_count} repositories in {os.path.basename(output_path)}")
    return output_path


def reprocess_shopify_repos(batch_size: int = 20, batch_delay: int = 45, max_repos: int = 300) -> Dict[str, int]:
    """Re-process failed Shopify repositories with optimal rate limiting.
    
    GitHub Search API allows 30 requests/minute for authenticated users.
    Using 20 repos per batch with 45s delay = ~26.7 requests/minute (safely under limit).
    """
    print(f"\n{'='*60}")
    print(f"RE-PROCESSING FAILED SHOPIFY REPOSITORIES (OPTIMIZED)")
    print(f"{'='*60}")
    
    # Get failed repositories for Shopify
    failed_repos = get_failed_repos_for_reprocessing('shopify')
    
    if not failed_repos:
        print("No failed repositories found for shopify")
        return {}
    
    print(f"Found {len(failed_repos)} failed repositories for shopify")
    
    # Process a larger subset with optimized rate limiting
    if max_repos and len(failed_repos) > max_repos:
        print(f"Processing first {max_repos} repositories (out of {len(failed_repos)})")
        failed_repos = failed_repos[:max_repos]
    
    print(f"Using OPTIMIZED settings: batch_size={batch_size}, batch_delay={batch_delay}s")
    print(f"Rate: ~{(batch_size * 60) / (batch_delay + (batch_size * 2)):.1f} requests/minute (limit: 30/min)")
    
    # Initialize fetcher with improved settings
    fetcher = MergedPRsFetcher()
    
    # Process with very conservative rate limiting
    pr_data = fetcher.get_batch_merged_prs(
        failed_repos, 
        days=30, 
        batch_size=batch_size,
        batch_delay=batch_delay
    )
    
    # Analyze results
    successful = sum(1 for v in pr_data.values() if v != -1)
    still_failed = sum(1 for v in pr_data.values() if v == -1)
    
    print(f"\nRe-processing results for shopify:")
    print(f"  Successful: {successful}")
    print(f"  Still failed: {still_failed}")
    print(f"  Success rate: {(successful/len(failed_repos))*100:.1f}%")
    
    return pr_data


def fix_shopify_csv_files(pr_data: Dict[str, int]) -> List[str]:
    """Fix Shopify CSV files with new PR data."""
    if not pr_data:
        print("No PR data retrieved for shopify")
        return []
    
    # Find CSV files to update
    org_dir = "data/orgs/shopify"
    csv_files = [
        "shopify_repos_filter1_20250812_with_prs_20250812.csv",
        "shopify_repos_filter2_20250812.csv", 
        "shopify_repos_filter3_20250812.csv"
    ]
    
    updated_files = []
    
    for csv_file in csv_files:
        csv_path = os.path.join(org_dir, csv_file)
        if os.path.exists(csv_path):
            print(f"\nUpdating {csv_file}...")
            updated_path = update_csv_with_new_pr_data(csv_path, pr_data)
            updated_files.append(updated_path)
        else:
            print(f"File not found: {csv_path}")
    
    return updated_files


def main():
    """Main function for Shopify reprocessing."""
    print("SHOPIFY REPOSITORIES - MERGED PRS REPROCESSING (OPTIMIZED)")
    print("=" * 60)
    print("Processing failed Shopify repositories with OPTIMAL rate limiting.")
    print("GitHub Search API limit: 30 requests/minute for authenticated users.")
    print("Using 20 repos/batch, 45s delay = ~26.7 requests/min (safely under limit)")
    print()
    
    # Use optimal settings for Shopify (GitHub Search API limit: 30 requests/min)
    batch_size = 20  # Optimal batch size for rate limiting
    batch_delay = 45  # Calculated to stay under 30 requests/min
    max_repos = 300  # Process more repositories efficiently
    
    try:
        # Re-process failed repositories
        pr_data = reprocess_shopify_repos(batch_size, batch_delay, max_repos)
        
        if pr_data:
            # Update CSV files
            updated_files = fix_shopify_csv_files(pr_data)
            
            print(f"\n{'='*60}")
            print("SHOPIFY REPROCESSING COMPLETE")
            print(f"{'='*60}")
            print(f"Updated files:")
            for file_path in updated_files:
                print(f"  - {os.path.basename(file_path)}")
            
            # Show some successful results
            successful_results = {k: v for k, v in pr_data.items() if v != -1}
            if successful_results:
                print(f"\nSample successful results:")
                for i, (repo, count) in enumerate(list(successful_results.items())[:10]):
                    print(f"  {repo}: {count} PRs")
                if len(successful_results) > 10:
                    print(f"  ... and {len(successful_results) - 10} more")
        else:
            print("No PR data was successfully retrieved.")
            
    except Exception as e:
        print(f"Error processing shopify repositories: {str(e)}")
        import traceback
        traceback.print_exc()
    
    print(f"\n{'='*60}")
    print("RECOMMENDATIONS:")
    print(f"{'='*60}")
    print("1. Check the updated CSV files for improved PR counts")
    print("2. This processed first 300 repositories with optimal rate limiting")
    print("3. If many still failed, the remaining repos may have legitimate 0 PRs or be inactive")
    print("4. Verify API token is working properly in .env file")


if __name__ == "__main__":
    main()