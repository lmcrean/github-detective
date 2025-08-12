"""Final fix for the remaining 4 Stripe repositories with -1 values."""

import csv
import os
import sys
from datetime import datetime
from typing import Dict, List

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from scripts.merged_prs_30d.fetch_merged_prs import MergedPRsFetcher


def get_remaining_stripe_repos() -> List[Dict[str, str]]:
    """Get the 4 remaining Stripe repositories that need fixing."""
    remaining_repos = [
        {"org_name": "stripe", "repo_name": "stripe-react-native"},
        {"org_name": "stripe", "repo_name": "stripe-apps"}, 
        {"org_name": "stripe", "repo_name": "pg-schema-diff"},
        {"org_name": "stripe", "repo_name": "stripe-terminal-react-native"}
    ]
    
    print(f"Targeting {len(remaining_repos)} remaining Stripe repositories:")
    for repo in remaining_repos:
        print(f"  - {repo['org_name']}/{repo['repo_name']}")
    
    return remaining_repos


def fetch_remaining_pr_data() -> Dict[str, int]:
    """Fetch PR data for the remaining 4 repositories."""
    print(f"\n{'='*60}")
    print("FETCHING PR DATA FOR REMAINING STRIPE REPOS")
    print(f"{'='*60}")
    
    repos = get_remaining_stripe_repos()
    
    # Initialize fetcher
    fetcher = MergedPRsFetcher()
    
    # Fetch with minimal delay since it's only 4 repos
    pr_data = fetcher.get_batch_merged_prs(
        repos, 
        days=30, 
        batch_size=4,  # All 4 in one batch
        batch_delay=5  # Very short delay since we're well under limits
    )
    
    # Analyze results
    successful = sum(1 for v in pr_data.values() if v != -1)
    still_failed = sum(1 for v in pr_data.values() if v == -1)
    
    print(f"\nFetch results:")
    print(f"  Successful: {successful}")
    print(f"  Still failed: {still_failed}")
    print(f"  Success rate: {(successful/len(repos))*100:.1f}%")
    
    # Show results
    if successful > 0:
        print(f"\nPR data retrieved:")
        for repo_key, pr_count in pr_data.items():
            if pr_count != -1:
                print(f"  {repo_key}: {pr_count} PRs")
    
    return pr_data


def update_stripe_csv_with_pr_data(csv_path: str, pr_data: Dict[str, int], output_path: str = None) -> str:
    """Update Stripe CSV file with new PR data."""
    if not output_path:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = csv_path.replace('.csv', f'_final_fixed_{timestamp}.csv')
    
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


def fix_all_stripe_csv_files(pr_data: Dict[str, int]) -> List[str]:
    """Fix all Stripe CSV files with the new PR data."""
    if not pr_data:
        print("No PR data retrieved")
        return []
    
    print(f"\n{'='*60}")
    print("UPDATING STRIPE CSV FILES")
    print(f"{'='*60}")
    
    stripe_dir = "data/orgs/stripe"
    
    # Find the most recent CSV files (prefer quickfix versions)
    import glob
    
    csv_patterns = [
        "stripe_repos_filter1_*quickfix*.csv",
        "stripe_repos_filter2_*quickfix*.csv", 
        "stripe_repos_filter3_*quickfix*.csv"
    ]
    
    updated_files = []
    
    for pattern in csv_patterns:
        matching_files = glob.glob(os.path.join(stripe_dir, pattern))
        if matching_files:
            # Use the most recent file
            latest_file = max(matching_files, key=os.path.getctime)
            print(f"\nUpdating {os.path.basename(latest_file)}...")
            updated_path = update_stripe_csv_with_pr_data(latest_file, pr_data)
            updated_files.append(updated_path)
        else:
            print(f"No files found matching pattern: {pattern}")
    
    return updated_files


def verify_final_results(updated_files: List[str]):
    """Verify that all -1 values have been eliminated."""
    print(f"\n{'='*60}")
    print("VERIFICATION - CHECKING FOR REMAINING -1 VALUES")
    print(f"{'='*60}")
    
    total_remaining_failures = 0
    
    for file_path in updated_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            failures = [row for row in reader if row.get('merged_prs_30d', '').strip() == '-1']
            
        print(f"\n{os.path.basename(file_path)}:")
        print(f"  Remaining -1 values: {len(failures)}")
        
        if failures:
            print(f"  Failed repositories:")
            for row in failures:
                print(f"    - {row['org_name']}/{row['repo_name']}")
        else:
            print(f"  ✅ SUCCESS: No -1 values remaining!")
        
        total_remaining_failures += len(failures)
    
    print(f"\n{'='*60}")
    print("FINAL VERIFICATION RESULTS")
    print(f"{'='*60}")
    
    if total_remaining_failures == 0:
        print("🎉 SUCCESS! All Stripe repositories now have valid merged_prs_30d data!")
        print("Stripe dataset is 100% complete with no -1 values.")
    else:
        print(f"⚠️  {total_remaining_failures} repositories still have -1 values")


def main():
    """Main function to fix the remaining Stripe repositories."""
    print("STRIPE FINAL FIX - REMAINING 4 REPOSITORIES")
    print("=" * 60)
    print("Fixing the last 4 Stripe repositories with -1 values")
    print("This should complete in under 2 minutes with optimal rate limiting")
    print()
    
    try:
        # Fetch PR data for the 4 remaining repos
        pr_data = fetch_remaining_pr_data()
        
        if pr_data:
            # Update all CSV files
            updated_files = fix_all_stripe_csv_files(pr_data)
            
            if updated_files:
                # Verify results
                verify_final_results(updated_files)
                
                print(f"\n{'='*60}")
                print("STRIPE FINAL FIX COMPLETE")
                print(f"{'='*60}")
                print("Updated files:")
                for file_path in updated_files:
                    print(f"  - {os.path.basename(file_path)}")
            else:
                print("No CSV files were updated")
        else:
            print("No PR data was successfully retrieved")
            
    except Exception as e:
        print(f"Error during final fix: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()