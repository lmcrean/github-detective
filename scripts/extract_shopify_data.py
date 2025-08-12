"""Extract and analyze Shopify repository data with updated merged_prs_30d values."""

import csv
import os
import glob
from datetime import datetime
from typing import Dict, List, Tuple


def find_latest_shopify_files() -> Dict[str, str]:
    """Find the latest Shopify CSV files, preferring fixed versions."""
    shopify_dir = "data/orgs/shopify"
    
    # Define the base file patterns
    base_patterns = [
        "shopify_repos_filter1_*",
        "shopify_repos_filter2_*", 
        "shopify_repos_filter3_*"
    ]
    
    latest_files = {}
    
    for pattern in base_patterns:
        # Look for fixed files first, then original files
        search_pattern = os.path.join(shopify_dir, pattern + ".csv")
        matching_files = glob.glob(search_pattern)
        
        if matching_files:
            # Prefer files with "fixed" in the name, then by modification time
            fixed_files = [f for f in matching_files if "fixed" in f]
            if fixed_files:
                latest_file = max(fixed_files, key=os.path.getctime)
            else:
                latest_file = max(matching_files, key=os.path.getctime)
            
            # Extract filter number
            if "filter1" in pattern:
                latest_files["filter1"] = latest_file
            elif "filter2" in pattern:
                latest_files["filter2"] = latest_file
            elif "filter3" in pattern:
                latest_files["filter3"] = latest_file
    
    return latest_files


def analyze_csv_file(csv_path: str) -> Dict:
    """Analyze a CSV file for merged_prs_30d data quality."""
    if not os.path.exists(csv_path):
        return {"error": f"File not found: {csv_path}"}
    
    total_repos = 0
    successful_prs = 0
    failed_prs = 0
    zero_prs = 0
    total_pr_count = 0
    
    pr_distribution = {}
    sample_repos = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            total_repos += 1
            pr_value = row.get('merged_prs_30d', '').strip()
            
            if pr_value == '-1':
                failed_prs += 1
            elif pr_value == '0':
                zero_prs += 1
                successful_prs += 1
            else:
                try:
                    pr_count = int(pr_value)
                    successful_prs += 1
                    total_pr_count += pr_count
                    
                    # Track distribution
                    if pr_count in pr_distribution:
                        pr_distribution[pr_count] += 1
                    else:
                        pr_distribution[pr_count] = 1
                    
                    # Collect sample repos with high PR counts
                    if pr_count > 5:
                        sample_repos.append((f"{row['org_name']}/{row['repo_name']}", pr_count))
                        
                except ValueError:
                    failed_prs += 1
    
    # Sort sample repos by PR count
    sample_repos.sort(key=lambda x: x[1], reverse=True)
    
    return {
        "total_repos": total_repos,
        "successful_prs": successful_prs,
        "failed_prs": failed_prs,
        "zero_prs": zero_prs,
        "success_rate": (successful_prs / total_repos * 100) if total_repos > 0 else 0,
        "total_pr_count": total_pr_count,
        "avg_prs_per_repo": (total_pr_count / successful_prs) if successful_prs > 0 else 0,
        "pr_distribution": pr_distribution,
        "top_active_repos": sample_repos[:10]
    }


def extract_shopify_summary() -> None:
    """Extract and summarize Shopify repository data."""
    print("SHOPIFY REPOSITORY DATA EXTRACTION")
    print("=" * 60)
    
    # Find latest files
    latest_files = find_latest_shopify_files()
    
    if not latest_files:
        print("No Shopify CSV files found!")
        return
    
    print("Latest files found:")
    for filter_name, file_path in latest_files.items():
        print(f"  {filter_name}: {os.path.basename(file_path)}")
    
    print(f"\n{'='*60}")
    print("ANALYSIS RESULTS")
    print(f"{'='*60}")
    
    all_results = {}
    total_repos = 0
    total_successful = 0
    total_failed = 0
    
    # Analyze each file
    for filter_name, file_path in latest_files.items():
        print(f"\n{filter_name.upper()} - {os.path.basename(file_path)}")
        print("-" * 50)
        
        analysis = analyze_csv_file(file_path)
        all_results[filter_name] = analysis
        
        if "error" in analysis:
            print(f"ERROR: {analysis['error']}")
            continue
        
        print(f"Total repositories: {analysis['total_repos']}")
        print(f"Successful PR data: {analysis['successful_prs']}")
        print(f"Failed (-1 values): {analysis['failed_prs']}")
        print(f"Zero PRs: {analysis['zero_prs']}")
        print(f"Success rate: {analysis['success_rate']:.1f}%")
        print(f"Total PRs (30 days): {analysis['total_pr_count']}")
        
        if analysis['successful_prs'] > 0:
            print(f"Average PRs per active repo: {analysis['avg_prs_per_repo']:.1f}")
        
        # Show top active repositories
        if analysis['top_active_repos']:
            print(f"\nTop active repositories:")
            for repo, pr_count in analysis['top_active_repos'][:5]:
                print(f"  {repo}: {pr_count} PRs")
        
        # Accumulate totals
        total_repos += analysis['total_repos']
        total_successful += analysis['successful_prs']
        total_failed += analysis['failed_prs']
    
    # Overall summary
    print(f"\n{'='*60}")
    print("OVERALL SUMMARY")
    print(f"{'='*60}")
    print(f"Total repositories across all filters: {total_repos}")
    print(f"Successfully processed: {total_successful}")
    print(f"Still failed (-1 values): {total_failed}")
    print(f"Overall success rate: {(total_successful/total_repos*100):.1f}%")
    
    # Find the most comprehensive dataset
    if latest_files:
        # Recommend filter1 as it usually has the most repositories
        recommended_file = latest_files.get('filter1', list(latest_files.values())[0])
        print(f"\nRecommended dataset for analysis:")
        print(f"  File: {os.path.basename(recommended_file)}")
        print(f"  Full path: {recommended_file}")
        
        if 'filter1' in all_results and 'error' not in all_results['filter1']:
            result = all_results['filter1']
            print(f"  Contains: {result['total_repos']} repositories")
            print(f"  PR data quality: {result['success_rate']:.1f}% successful")


def save_analysis_report():
    """Save a detailed analysis report to .notes directory."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = f".notes/shopify_analysis_{timestamp}.md"
    
    if not os.path.exists(".notes"):
        os.makedirs(".notes")
    
    latest_files = find_latest_shopify_files()
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Shopify Repository Analysis Report\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Files Analyzed\n\n")
        for filter_name, file_path in latest_files.items():
            f.write(f"- **{filter_name}**: `{os.path.basename(file_path)}`\n")
        
        f.write("\n## Analysis Results\n\n")
        
        for filter_name, file_path in latest_files.items():
            analysis = analyze_csv_file(file_path)
            
            f.write(f"### {filter_name.upper()}\n\n")
            
            if "error" in analysis:
                f.write(f"ERROR: {analysis['error']}\n\n")
                continue
            
            f.write(f"- Total repositories: {analysis['total_repos']}\n")
            f.write(f"- Successful PR data: {analysis['successful_prs']}\n")
            f.write(f"- Failed (-1 values): {analysis['failed_prs']}\n")
            f.write(f"- Success rate: {analysis['success_rate']:.1f}%\n")
            f.write(f"- Total PRs (30 days): {analysis['total_pr_count']}\n\n")
            
            if analysis['top_active_repos']:
                f.write("**Top Active Repositories:**\n\n")
                for repo, pr_count in analysis['top_active_repos'][:10]:
                    f.write(f"- {repo}: {pr_count} PRs\n")
                f.write("\n")
        
        f.write("## Recommendations\n\n")
        f.write("1. Use the filter1 dataset for most comprehensive analysis\n")
        f.write("2. Consider reprocessing remaining failed repositories\n")
        f.write("3. Focus analysis on repositories with successful PR data\n")
    
    print(f"\nDetailed analysis saved to: {report_path}")
    return report_path


def main():
    """Main extraction and analysis function."""
    extract_shopify_summary()
    report_path = save_analysis_report()
    
    print(f"\n{'='*60}")
    print("EXTRACTION COMPLETE")
    print(f"{'='*60}")
    print("Shopify repository data is ready for analysis!")
    print(f"Detailed report saved to: {os.path.basename(report_path)}")


if __name__ == "__main__":
    main()