"""Selective re-processing of failed repositories with improved rate limiting."""

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
    """
    Update CSV file with new PR data, replacing -1 values where we got successful results.
    
    Args:
        csv_path: Path to original CSV file
        pr_data: Dictionary mapping "org/repo" to PR counts
        output_path: Optional output path (defaults to timestamped version)
    
    Returns:
        Path to updated CSV file
    """
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
                row['merged_prs_30d'] = str(pr_data[key])
                updated_count += 1
            
            rows.append(row)
    
    # Write updated data
    with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Updated {updated_count} repositories in {output_path}")
    return output_path


def reprocess_failed_repos(org_name: str, batch_size: int = 3, batch_delay: int = 30) -> Dict[str, int]:
    """
    Re-process failed repositories for a specific organization.
    
    Args:
        org_name: Organization name (stripe, shopify)
        batch_size: Number of repos to process per batch
        batch_delay: Seconds to wait between batches
    
    Returns:
        Dictionary mapping repo keys to PR counts
    """
    print(f"\n{'='*60}")
    print(f"RE-PROCESSING FAILED REPOS FOR {org_name.upper()}")
    print(f"{'='*60}")
    
    # Get failed repositories for this organization
    failed_repos = get_failed_repos_for_reprocessing(org_name)
    
    if not failed_repos:
        print(f"No failed repositories found for {org_name}")
        return {}
    
    print(f"Found {len(failed_repos)} failed repositories for {org_name}")
    print(f"Using conservative settings: batch_size={batch_size}, batch_delay={batch_delay}s")
    
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
    
    print(f"\nRe-processing results for {org_name}:")
    print(f"  Successful: {successful}")
    print(f"  Still failed: {still_failed}")
    print(f"  Success rate: {(successful/len(failed_repos))*100:.1f}%")
    
    return pr_data


def fix_csv_files_for_org(org_name: str, batch_size: int = 3, batch_delay: int = 30) -> List[str]:
    """
    Fix all CSV files for an organization by re-processing failed repositories.
    
    Args:
        org_name: Organization name
        batch_size: Batch size for processing
        batch_delay: Delay between batches
    
    Returns:
        List of updated file paths
    """
    # Re-process failed repositories
    pr_data = reprocess_failed_repos(org_name, batch_size, batch_delay)
    
    if not pr_data:
        print(f"No PR data retrieved for {org_name}")
        return []
    
    # Find CSV files to update
    org_dir = f"data/orgs/{org_name}"
    csv_files = [
        f"{org_name}_repos_filter1_20250812_with_prs_20250812.csv",
        f"{org_name}_repos_filter2_20250812.csv", 
        f"{org_name}_repos_filter3_20250812.csv"
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
    """Main function for selective re-processing."""
    print("SELECTIVE RE-PROCESSING OF FAILED REPOSITORIES")
    print("=" * 80)
    print("This script will re-process failed repositories with improved rate limiting.")
    print("Using very conservative settings to avoid API rate limits.")
    print()
    
    # Process organizations separately with very conservative settings
    orgs_to_process = ['stripe', 'shopify']  # Start with stripe (smaller)
    
    # Ask user for confirmation
    response = input(f"Process {', '.join(orgs_to_process)}? This will take significant time with conservative rate limiting. (y/N): ")
    
    if response.lower() != 'y':
        print("Re-processing cancelled.")
        return
    
    all_results = {}
    
    for org_name in orgs_to_process:
        print(f"\n{'='*80}")
        print(f"PROCESSING {org_name.upper()}")
        print(f"{'='*80}")
        
        # Use very conservative settings
        batch_size = 3 if org_name == 'stripe' else 2  # Even smaller for shopify
        batch_delay = 30 if org_name == 'stripe' else 45  # Longer delays for shopify
        
        try:
            updated_files = fix_csv_files_for_org(org_name, batch_size, batch_delay)
            all_results[org_name] = updated_files
            
            print(f"\nCompleted {org_name}. Updated files:")
            for file_path in updated_files:
                print(f"  - {os.path.basename(file_path)}")
            
            # Long delay between organizations
            if org_name != orgs_to_process[-1]:
                print(f"\nTaking 60 second break before processing next organization...")
                import time
                time.sleep(60)
                
        except Exception as e:
            print(f"Error processing {org_name}: {str(e)}")
            import traceback
            traceback.print_exc()
    
    # Final summary
    print(f"\n{'='*80}")
    print("RE-PROCESSING COMPLETE")
    print(f"{'='*80}")
    
    for org_name, files in all_results.items():
        print(f"\n{org_name.upper()}:")
        if files:
            print(f"  Successfully updated {len(files)} files")
            for file_path in files:
                print(f"    - {os.path.basename(file_path)}")
        else:
            print(f"  No files updated")
    
    print(f"\nRecommendations:")
    print(f"1. Check the updated files for improved PR counts")
    print(f"2. If many repositories still have -1, consider running again with longer delays")
    print(f"3. Verify API token is working: check .env file for API_GITHUB_TOKEN")


if __name__ == "__main__":
    main()