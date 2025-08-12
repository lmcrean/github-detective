"""Filter 3: Keep only top 50% of repositories based on activity metrics."""

import csv
import os
from datetime import datetime
from typing import Dict, List, Tuple


def calculate_activity_score(row: Dict[str, str]) -> float:
    """
    Calculate an activity score for a repository.
    
    Considers:
    - Merged PRs in last 30 days (weight: 40%)
    - Stars count (weight: 20%)
    - Open issues (weight: 20%)
    - Open PRs (weight: 20%)
    
    Args:
        row: CSV row dictionary
    
    Returns:
        Activity score (higher is better)
    """
    score = 0.0
    
    try:
        # Merged PRs (most important for recent activity)
        merged_prs = int(row.get('merged_prs_30d', 0))
        score += merged_prs * 40
        
        # Stars (popularity indicator)
        stars = int(row.get('stars_count', 0))
        score += min(stars / 10, 100) * 20  # Cap contribution at 1000 stars
        
        # Open issues (community engagement)
        open_issues = int(row.get('open_issue_count', 0))
        score += min(open_issues, 100) * 20  # Cap at 100 issues
        
        # Open PRs (active development)
        open_prs = int(row.get('pull_requests_open_count', 0))
        score += min(open_prs * 2, 100) * 20  # Weight PRs higher, cap at 50 PRs
        
    except (ValueError, KeyError) as e:
        # Return low score for repos with invalid data
        return 0.0
    
    return score


def filter_top_percentile(input_csv: str, output_csv: str, percentile: float = 0.5) -> int:
    """
    Keep only top percentile of repositories based on activity score.
    
    Args:
        input_csv: Path to input CSV
        output_csv: Path to output CSV
        percentile: Fraction to keep (0.5 = top 50%)
    
    Returns:
        Number of repositories kept
    """
    # Read all rows and calculate scores
    rows_with_scores = []
    
    with open(input_csv, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        for row in reader:
            score = calculate_activity_score(row)
            rows_with_scores.append((score, row))
    
    total_count = len(rows_with_scores)
    
    if total_count == 0:
        print("No repositories to filter")
        return 0
    
    # Sort by score (descending)
    rows_with_scores.sort(key=lambda x: x[0], reverse=True)
    
    # Calculate how many to keep
    keep_count = max(1, int(total_count * percentile))
    
    # Keep top repositories
    rows_to_keep = [row for score, row in rows_with_scores[:keep_count]]
    
    # Write filtered data
    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_to_keep)
    
    # Print statistics
    print(f"Filter 3 complete: Kept top {keep_count}/{total_count} repositories ({percentile*100:.0f}%)")
    
    # Show score distribution
    if rows_with_scores:
        top_score = rows_with_scores[0][0]
        cutoff_score = rows_with_scores[keep_count-1][0] if keep_count > 0 else 0
        print(f"  Top score: {top_score:.2f}")
        print(f"  Cutoff score: {cutoff_score:.2f}")
        
        # Show top 3 repositories
        print("  Top 3 repositories:")
        for i, (score, row) in enumerate(rows_with_scores[:3], 1):
            print(f"    {i}. {row['org_name']}/{row['repo_name']} (score: {score:.2f})")
    
    return keep_count


def apply_filter3_to_org(org_name: str, input_csv: str, percentile: float = 0.5) -> str:
    """
    Apply Filter 3 to an organization's CSV file.
    
    Args:
        org_name: Organization name
        input_csv: Path to input CSV (should be filter2 output)
        percentile: Fraction to keep (0.5 = top 50%)
    
    Returns:
        Path to filtered output file
    """
    # Generate output filename with filter3 and date
    date_str = datetime.now().strftime('%Y%m%d')
    
    # Extract directory path
    dir_path = os.path.dirname(input_csv)
    output_csv = os.path.join(dir_path, f"{org_name}_repos_filter3_{date_str}.csv")
    
    print(f"\nApplying Filter 3 to {org_name}...")
    print(f"  Keeping top {percentile*100:.0f}% of repositories")
    print(f"  Input: {input_csv}")
    print(f"  Output: {output_csv}")
    
    kept_count = filter_top_percentile(input_csv, output_csv, percentile)
    
    return output_csv


def batch_filter3(org_configs: Dict[str, str], percentile: float = 0.5) -> Dict[str, str]:
    """
    Apply Filter 3 to multiple organizations.
    
    Args:
        org_configs: Dictionary mapping org names to CSV paths (filter2 outputs)
        percentile: Fraction to keep (0.5 = top 50%)
    
    Returns:
        Dictionary mapping org names to filtered output paths
    """
    results = {}
    
    for org_name, input_csv in org_configs.items():
        if not os.path.exists(input_csv):
            print(f"Warning: Input file not found for {org_name}: {input_csv}")
            continue
        
        try:
            output_path = apply_filter3_to_org(org_name, input_csv, percentile)
            results[org_name] = output_path
            print(f"[SUCCESS] Successfully applied Filter 3 to {org_name}")
            
        except Exception as e:
            print(f"[ERROR] Error applying Filter 3 to {org_name}: {str(e)}")
            results[org_name] = None
    
    return results


if __name__ == "__main__":
    # Test with filter2 outputs
    date_str = datetime.now().strftime('%Y%m%d')
    test_configs = {
        'stripe': f'data/orgs/stripe/stripe_repos_filter2_{date_str}.csv',
        'shopify': f'data/orgs/shopify/shopify_repos_filter2_{date_str}.csv'
    }
    
    print("Testing Filter 3 (Top Percentile Filter)...")
    
    # Check if filter2 outputs exist
    for org, path in test_configs.items():
        if not os.path.exists(path):
            print(f"Note: Filter 2 output not found for {org}. Run previous filters first.")
    
    results = batch_filter3(test_configs, percentile=0.5)  # Keep top 50%
    
    print("\nFilter 3 Results:")
    for org, output_file in results.items():
        if output_file:
            print(f"  {org}: {output_file}")
        else:
            print(f"  {org}: Not processed")