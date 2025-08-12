"""Check results of optimized Shopify reprocessing and provide quick analysis."""

import os
import glob
from datetime import datetime
from scripts.extract_shopify_data import find_latest_shopify_files, analyze_csv_file


def check_for_new_files():
    """Check if new fixed files have been created."""
    shopify_dir = "data/orgs/shopify"
    
    # Look for files with "fixed" in the name
    fixed_files = glob.glob(os.path.join(shopify_dir, "*fixed*.csv"))
    
    if fixed_files:
        print("NEW FIXED FILES FOUND:")
        for file_path in fixed_files:
            file_stat = os.stat(file_path)
            mod_time = datetime.fromtimestamp(file_stat.st_mtime)
            print(f"  - {os.path.basename(file_path)} (modified: {mod_time.strftime('%H:%M:%S')})")
        return fixed_files
    else:
        print("No fixed files found yet - processing may still be running")
        return []


def quick_comparison():
    """Compare before/after results if new files exist."""
    fixed_files = check_for_new_files()
    
    if not fixed_files:
        return
    
    print(f"\n{'='*60}")
    print("QUICK COMPARISON - BEFORE vs AFTER OPTIMIZATION")
    print(f"{'='*60}")
    
    # Analyze one of the fixed files
    sample_file = fixed_files[0]
    analysis = analyze_csv_file(sample_file)
    
    if "error" not in analysis:
        print(f"\nResults from {os.path.basename(sample_file)}:")
        print(f"  Total repositories: {analysis['total_repos']}")
        print(f"  Successful PR data: {analysis['successful_prs']}")
        print(f"  Failed (-1 values): {analysis['failed_prs']}")
        print(f"  Success rate: {analysis['success_rate']:.1f}%")
        print(f"  Total PRs (30 days): {analysis['total_pr_count']}")
        
        if analysis['top_active_repos']:
            print(f"\n  Top repositories by PR activity:")
            for repo, pr_count in analysis['top_active_repos'][:5]:
                print(f"    {repo}: {pr_count} PRs")
        
        # Compare to previous 26.1% success rate
        old_success_rate = 26.1
        improvement = analysis['success_rate'] - old_success_rate
        print(f"\n  IMPROVEMENT: {improvement:+.1f}% (from {old_success_rate}% to {analysis['success_rate']:.1f}%)")


if __name__ == "__main__":
    print("CHECKING OPTIMIZED REPROCESSING RESULTS")
    print("=" * 60)
    quick_comparison()