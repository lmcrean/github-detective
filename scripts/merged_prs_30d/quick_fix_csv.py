"""Quick fix to update CSV files with known PR data that we've successfully collected."""

import csv
import os
import sys
from datetime import datetime

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Known PR data from successful API calls during testing and partial processing
KNOWN_PR_DATA = {
    # From test runs and partial processing
    "stripe/stripe-python": 4,
    "stripe/smokescreen": 4,
    "stripe/krl": 0,
    "stripe/openapi": 0,
    "stripe/stripe-mock": 64,
    "stripe/homebrew-stripe-mock": 0,
    "stripe/stripe-terminal-ios": 3,
    "stripe/skycfg": 0,
    "stripe/stripe-terminal-android": 2,
    "stripe/example-terminal-backend": 1,
    "stripe/stripe-cli": 4,
    "stripe/scoop-stripe-cli": 0,
    "stripe/homebrew-stripe-cli": 0,
    "stripe/react-stripe-js": 4,
    "stripe/stripe-js": 11,
    "stripe/checkout-sales-demo": 0,
    "stripe/vscode-stripe": 0,
    "stripe/terminal-connector-releases": 0,
    "stripe/agent-toolkit": 1,
    "stripe/stripe-commercetools-checkout-app": 1,
    "stripe/scripts": 0,
    "stripe/munkisrv": 1,
    "stripe/memlink": 1,
    "stripe/ft3": 0,
    "stripe/LibreChat": 2,
    
    # Values already correct in the CSV (not -1)
    "stripe/stripe-android": 126,
    "stripe/stripe-ios": 119,
    "stripe/stripe-node": 8,
    "stripe/stripe-dotnet": 8,
    "stripe/stripe-ruby": 6,
    "stripe/stripe-go": 7,
    "stripe/stripe-java": 4,
    "stripe/stripe-php": 4,
    "stripe/subprocess": 2
}


def update_csv_with_known_data(csv_path: str, output_path: str = None) -> int:
    """
    Update CSV file with known PR data.
    
    Args:
        csv_path: Path to original CSV file
        output_path: Optional output path (defaults to timestamped version)
    
    Returns:
        Number of repositories updated
    """
    if not output_path:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        base_name = os.path.splitext(csv_path)[0]
        output_path = f"{base_name}_quickfix_{timestamp}.csv"
    
    updated_count = 0
    
    if not os.path.exists(csv_path):
        print(f"Input file not found: {csv_path}")
        return 0
    
    with open(csv_path, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        rows = []
        for row in reader:
            key = f"{row['org_name']}/{row['repo_name']}"
            
            # Update if we have known data and the current value is -1
            if key in KNOWN_PR_DATA and row.get('merged_prs_30d', '').strip() == '-1':
                old_value = row['merged_prs_30d']
                row['merged_prs_30d'] = str(KNOWN_PR_DATA[key])
                print(f"Updated {key}: {old_value} -> {KNOWN_PR_DATA[key]}")
                updated_count += 1
            
            rows.append(row)
    
    # Write updated data
    with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\nUpdated {updated_count} repositories in {os.path.basename(output_path)}")
    return updated_count


def fix_all_stripe_csvs():
    """Fix all Stripe CSV files with known PR data."""
    print("QUICK FIX: Updating Stripe CSV files with known PR data")
    print("=" * 60)
    
    stripe_dir = "data/orgs/stripe"
    csv_files = [
        "stripe_repos_filter1_20250812_with_prs_20250812.csv",
        "stripe_repos_filter2_20250812.csv",
        "stripe_repos_filter3_20250812.csv"
    ]
    
    total_updated = 0
    
    for csv_file in csv_files:
        csv_path = os.path.join(stripe_dir, csv_file)
        print(f"\nProcessing {csv_file}...")
        
        if os.path.exists(csv_path):
            updated = update_csv_with_known_data(csv_path)
            total_updated += updated
        else:
            print(f"File not found: {csv_path}")
    
    print(f"\n" + "=" * 60)
    print(f"SUMMARY: Updated {total_updated} total repository entries")
    print(f"From {len(KNOWN_PR_DATA)} known PR data points")
    
    # Show some statistics
    successful_prs = [v for v in KNOWN_PR_DATA.values() if v > 0]
    zero_prs = [v for v in KNOWN_PR_DATA.values() if v == 0]
    
    print(f"\nKnown data breakdown:")
    print(f"  Repositories with PRs: {len(successful_prs)}")
    print(f"  Repositories with 0 PRs: {len(zero_prs)}")
    print(f"  Total PR count: {sum(KNOWN_PR_DATA.values())}")


def analyze_remaining_failures():
    """Analyze what repositories still need to be processed."""
    print("\n" + "=" * 60)
    print("ANALYZING REMAINING FAILURES")
    print("=" * 60)
    
    # Read the latest quickfix file to see what's left
    stripe_dir = "data/orgs/stripe"
    
    # Find the most recent quickfix file
    import glob
    quickfix_files = glob.glob(os.path.join(stripe_dir, "*quickfix*.csv"))
    
    if not quickfix_files:
        print("No quickfix files found yet.")
        return
    
    latest_file = max(quickfix_files, key=os.path.getctime)
    print(f"Analyzing: {os.path.basename(latest_file)}")
    
    still_failed = []
    fixed = []
    
    with open(latest_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = f"{row['org_name']}/{row['repo_name']}"
            pr_value = row.get('merged_prs_30d', '').strip()
            
            if pr_value == '-1':
                still_failed.append(key)
            else:
                fixed.append(key)
    
    print(f"\nResults from quick fix:")
    print(f"  Fixed repositories: {len(fixed)}")
    print(f"  Still failed: {len(still_failed)}")
    
    if still_failed:
        print(f"\nRepositories still needing processing:")
        for repo in still_failed[:10]:  # Show first 10
            print(f"  - {repo}")
        if len(still_failed) > 10:
            print(f"  ... and {len(still_failed) - 10} more")


if __name__ == "__main__":
    fix_all_stripe_csvs()
    analyze_remaining_failures()
    
    print(f"\n" + "=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    print("1. Review the quickfix files to verify the updates look correct")
    print("2. For remaining -1 values, you can:")
    print("   a. Run the full reprocessing script for the remaining repos")
    print("   b. Manually look up PR counts for critical repositories")
    print("   c. Accept that some less active repos may have legitimate 0 PRs")
    print("\n3. The quickfix files are:")
    for csv_file in ["stripe_repos_filter1_20250812_with_prs_20250812",
                     "stripe_repos_filter2_20250812", 
                     "stripe_repos_filter3_20250812"]:
        print(f"   - data/orgs/stripe/{csv_file}_quickfix_*.csv")