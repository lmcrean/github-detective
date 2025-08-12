"""Identify repositories with -1 values in merged_prs_30d that need re-processing."""

import csv
import os
import glob
from typing import List, Dict, Tuple
from datetime import datetime


def find_csv_files(base_dir: str = "data/orgs") -> List[str]:
    """Find all CSV files in the organization directories."""
    csv_files = []
    pattern = os.path.join(base_dir, "**", "*.csv")
    csv_files = glob.glob(pattern, recursive=True)
    return csv_files


def analyze_csv_file(csv_path: str) -> Dict:
    """
    Analyze a CSV file for -1 values in merged_prs_30d column.
    
    Args:
        csv_path: Path to CSV file
    
    Returns:
        Dictionary with analysis results
    """
    result = {
        'file': csv_path,
        'total_repos': 0,
        'failed_repos': 0,
        'success_repos': 0,
        'failed_list': [],
        'has_merged_prs_column': False
    }
    
    if not os.path.exists(csv_path):
        return result
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # Check if merged_prs_30d column exists
            if 'merged_prs_30d' not in reader.fieldnames:
                return result
            
            result['has_merged_prs_column'] = True
            
            for row in reader:
                result['total_repos'] += 1
                
                merged_prs_value = row.get('merged_prs_30d', '').strip()
                
                if merged_prs_value == '-1':
                    result['failed_repos'] += 1
                    result['failed_list'].append({
                        'org_name': row.get('org_name', ''),
                        'repo_name': row.get('repo_name', ''),
                        'stars_count': row.get('stars_count', ''),
                        'last_pushed_date': row.get('last_pushed_date', '')
                    })
                elif merged_prs_value.isdigit():
                    result['success_repos'] += 1
    
    except Exception as e:
        print(f"Error analyzing {csv_path}: {str(e)}")
    
    return result


def generate_failed_repos_summary(base_dir: str = "data/orgs") -> None:
    """Generate a comprehensive summary of failed repositories."""
    
    print("=" * 80)
    print("FAILED REPOSITORIES ANALYSIS")
    print("=" * 80)
    
    csv_files = find_csv_files(base_dir)
    
    if not csv_files:
        print(f"No CSV files found in {base_dir}")
        return
    
    all_failed_repos = []
    total_files = 0
    files_with_issues = 0
    
    # Analyze each CSV file
    for csv_file in sorted(csv_files):
        result = analyze_csv_file(csv_file)
        
        if not result['has_merged_prs_column']:
            continue
            
        total_files += 1
        
        filename = os.path.basename(csv_file)
        print(f"\n{filename}")
        print("-" * len(filename))
        print(f"Total repositories: {result['total_repos']}")
        print(f"Failed repositories: {result['failed_repos']}")
        print(f"Success repositories: {result['success_repos']}")
        
        if result['failed_repos'] > 0:
            files_with_issues += 1
            failure_rate = (result['failed_repos'] / result['total_repos']) * 100
            print(f"Failure rate: {failure_rate:.1f}%")
            
            # Add to global list
            for repo in result['failed_list']:
                repo['source_file'] = csv_file
                all_failed_repos.append(repo)
    
    # Global summary
    print("\n" + "=" * 80)
    print("GLOBAL SUMMARY")
    print("=" * 80)
    print(f"Total CSV files analyzed: {total_files}")
    print(f"Files with failures: {files_with_issues}")
    print(f"Total failed repositories: {len(all_failed_repos)}")
    
    # Group by organization
    org_stats = {}
    for repo in all_failed_repos:
        org = repo['org_name']
        if org not in org_stats:
            org_stats[org] = {'count': 0, 'repos': []}
        org_stats[org]['count'] += 1
        org_stats[org]['repos'].append(repo['repo_name'])
    
    print(f"\nFailures by organization:")
    for org, stats in sorted(org_stats.items()):
        print(f"  {org}: {stats['count']} repositories")
    
    # Save failed repos to file for re-processing
    if all_failed_repos:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f".notes/failed_repos_analysis_{timestamp}.csv"
        
        os.makedirs('.notes', exist_ok=True)
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            if all_failed_repos:
                writer = csv.DictWriter(f, fieldnames=['org_name', 'repo_name', 'stars_count', 'last_pushed_date', 'source_file'])
                writer.writeheader()
                writer.writerows(all_failed_repos)
        
        print(f"\nFailed repositories saved to: {output_file}")
        print(f"Use this file for selective re-processing.")


def get_failed_repos_for_reprocessing(org_name: str = None) -> List[Dict[str, str]]:
    """
    Get list of failed repositories for re-processing.
    
    Args:
        org_name: Optional organization name to filter by
    
    Returns:
        List of repository dictionaries suitable for batch processing
    """
    failed_repos = []
    
    # Look for the most recent analysis file
    analysis_files = glob.glob('.notes/failed_repos_analysis_*.csv')
    
    if not analysis_files:
        print("No failed repos analysis found. Run generate_failed_repos_summary() first.")
        return failed_repos
    
    # Use the most recent analysis
    latest_analysis = max(analysis_files, key=os.path.getctime)
    print(f"Using analysis file: {latest_analysis}")
    
    with open(latest_analysis, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if org_name is None or row['org_name'] == org_name:
                failed_repos.append({
                    'org_name': row['org_name'],
                    'repo_name': row['repo_name']
                })
    
    return failed_repos


if __name__ == "__main__":
    # Generate comprehensive analysis
    generate_failed_repos_summary()
    
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    print("1. Check GitHub token configuration (GITHUB_TOKEN or API_GITHUB_TOKEN)")
    print("2. Use get_failed_repos_for_reprocessing() to get repos for re-processing")
    print("3. Process failed repos in small batches with longer delays")
    print("4. Consider processing different organizations separately")
    print("5. Monitor rate limits and adjust batch sizes accordingly")