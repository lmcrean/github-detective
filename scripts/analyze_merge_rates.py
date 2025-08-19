#!/usr/bin/env python3
"""Analyze and sort merge rate results from all collection processes."""

import os
import pandas as pd
from datetime import datetime

def analyze_merge_rates():
    """Combine and sort all merge rate CSV files by highest merge rate first."""
    
    # Define all possible CSV files and their sources
    csv_files = {
        'data/output/repo_health_google.csv': 'GOOGLE',
        'data/output/repo_health_meta.csv': 'META', 
        'data/output/repo_health_microsoft.csv': 'MICROSOFT',
        'data/output/repo_health_ibm.csv': 'IBM',
        'data/output/repo_health_small_orgs.csv': 'SMALL_ORGS',
        'data/output/repo_health_large_bucket1.csv': 'LARGE_BUCKET1',
        'data/output/repo_health_large_bucket2.csv': 'LARGE_BUCKET2',
        'data/output/repo_health_large_bucket3.csv': 'LARGE_BUCKET3',
        'data/output/repo_health_large_bucket4.csv': 'LARGE_BUCKET4'
    }
    
    # Collect all available data
    all_dataframes = []
    files_found = []
    files_missing = []
    
    print("=== Repository Health Analysis ===")
    print("Metrics: commits_last_30d + PRs_closed_30d")
    print(f"Starting analysis at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    for csv_file, source in csv_files.items():
        if os.path.exists(csv_file):
            try:
                df = pd.read_csv(csv_file)
                if len(df) > 0:
                    df['source'] = source
                    all_dataframes.append(df)
                    files_found.append(f"{source}: {len(df)} repos")
                    print(f"OK Loaded {csv_file}: {len(df)} repositories")
                else:
                    print(f"WARNING {csv_file} exists but is empty")
            except Exception as e:
                print(f"ERROR reading {csv_file}: {str(e)}")
                files_missing.append(f"{source}: Error")
        else:
            files_missing.append(f"{source}: File not found")
            print(f"MISSING: {csv_file}")
    
    if not all_dataframes:
        print("\nERROR: No valid CSV files found!")
        return
    
    print(f"\nSUMMARY:")
    print(f"Files loaded: {len(files_found)}")
    for file_info in files_found:
        print(f"  - {file_info}")
    
    if files_missing:
        print(f"Files missing: {len(files_missing)}")
        for missing_info in files_missing:
            print(f"  - {missing_info}")
    
    # Combine all dataframes
    print(f"\nCombining data...")
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    
    # Ensure columns are numeric and create health score
    combined_df['commits_last_30d'] = pd.to_numeric(combined_df['commits_last_30d'], errors='coerce')
    combined_df['PRs_closed_30d'] = pd.to_numeric(combined_df['PRs_closed_30d'], errors='coerce')
    
    # Create health score: commits + (PRs * 2) - PRs are more valuable
    combined_df['health_score'] = combined_df['commits_last_30d'] + (combined_df['PRs_closed_30d'] * 2)
    
    # Sort by health score (highest first)
    print(f"Sorting by health score (commits + PRs*2, highest first)...")
    sorted_df = combined_df.sort_values('health_score', ascending=False)
    
    # Generate output files
    output_dir = 'data/output'
    os.makedirs(output_dir, exist_ok=True)
    
    # Main sorted file
    main_output = f"{output_dir}/repo_health_sorted_by_score.csv"
    sorted_df.to_csv(main_output, index=False)
    print(f"SAVED main results: {main_output}")
    
    # Top 100 healthiest repositories  
    top_100 = sorted_df.head(100)
    top_100_output = f"{output_dir}/top_100_healthiest_repos.csv"
    top_100.to_csv(top_100_output, index=False)
    print(f"SAVED top 100: {top_100_output}")
    
    # Analysis summary
    print(f"\nAnalysis Results:")
    print(f"Total repositories: {len(sorted_df):,}")
    print(f"Active repositories (health_score > 0): {len(sorted_df[sorted_df['health_score'] > 0]):,}")
    print(f"Inactive repositories (health_score = 0): {len(sorted_df[sorted_df['health_score'] == 0]):,}")
    print(f"Highest health score: {sorted_df['health_score'].max()}")
    print(f"Average health score: {sorted_df['health_score'].mean():.2f}")
    print(f"Average commits/30d: {sorted_df['commits_last_30d'].mean():.2f}")
    print(f"Average PRs closed/30d: {sorted_df['PRs_closed_30d'].mean():.2f}")
    
    # Top performers
    print(f"\nTop 10 Healthiest Repositories:")
    top_10 = sorted_df.head(10)
    for idx, row in top_10.iterrows():
        print(f"  Score {row['health_score']:3.0f} ({row['commits_last_30d']:3.0f}c + {row['PRs_closed_30d']:3.0f}p) - {row['org']}/{row['repo']} ({row['source']})")
    
    # Summary by source
    print(f"\nSummary by Source:")
    source_summary = sorted_df.groupby('source').agg({
        'health_score': ['count', 'mean', 'max'],
        'commits_last_30d': ['mean'],
        'PRs_closed_30d': ['mean']
    }).round(2)
    
    for source in source_summary.index:
        count = source_summary.loc[source, ('health_score', 'count')]
        avg_health = source_summary.loc[source, ('health_score', 'mean')]
        max_health = source_summary.loc[source, ('health_score', 'max')]
        avg_commits = source_summary.loc[source, ('commits_last_30d', 'mean')]
        avg_prs = source_summary.loc[source, ('PRs_closed_30d', 'mean')]
        print(f"  {source}: {count:,} repos, health {avg_health:.1f} (max {max_health:.0f}), avg {avg_commits:.1f}c + {avg_prs:.1f}p")
    
    # Save summary to file
    summary_output = f"{output_dir}/repo_health_summary.txt"
    with open(summary_output, 'w') as f:
        f.write(f"Repository Health Analysis Summary\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Metrics: commits_last_30d + PRs_closed_30d (health_score = commits + PRs*2)\n\n")
        f.write(f"Total repositories: {len(sorted_df):,}\n")
        f.write(f"Active repositories (health_score > 0): {len(sorted_df[sorted_df['health_score'] > 0]):,}\n")
        f.write(f"Inactive repositories (health_score = 0): {len(sorted_df[sorted_df['health_score'] == 0]):,}\n")
        f.write(f"Highest health score: {sorted_df['health_score'].max()}\n")
        f.write(f"Average health score: {sorted_df['health_score'].mean():.2f}\n\n")
        
        f.write("Top 10 Healthiest Repositories:\n")
        for idx, row in top_10.iterrows():
            f.write(f"  Score {row['health_score']:3.0f} ({row['commits_last_30d']:3.0f}c + {row['PRs_closed_30d']:3.0f}p) - {row['org']}/{row['repo']} ({row['source']})\n")
    
    print(f"SAVED summary: {summary_output}")
    print(f"\nAnalysis complete!")

if __name__ == "__main__":
    analyze_merge_rates()