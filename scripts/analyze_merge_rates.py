#!/usr/bin/env python3
"""Analyze and sort merge rate results from all collection processes."""

import os
import pandas as pd
from datetime import datetime

def analyze_merge_rates():
    """Combine and sort all merge rate CSV files by highest merge rate first."""
    
    # Define all possible CSV files and their sources
    csv_files = {
        'data/output/merge_rates_google.csv': 'GOOGLE',
        'data/output/merge_rates_meta.csv': 'META', 
        'data/output/merge_rates_microsoft.csv': 'MICROSOFT',
        'data/output/merge_rates_ibm.csv': 'IBM',
        'data/output/merge_rates_large_orgs.csv': 'LARGE_ORGS',
        'data/output/merge_rates_small_orgs.csv': 'SMALL_ORGS'
    }
    
    # Collect all available data
    all_dataframes = []
    files_found = []
    files_missing = []
    
    print("=== Merge Rate Analysis ===")
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
                    print(f"✓ Loaded {csv_file}: {len(df)} repositories")
                else:
                    print(f"⚠ {csv_file} exists but is empty")
            except Exception as e:
                print(f"✗ Error reading {csv_file}: {str(e)}")
                files_missing.append(f"{source}: Error")
        else:
            files_missing.append(f"{source}: File not found")
            print(f"✗ Missing: {csv_file}")
    
    if not all_dataframes:
        print("\n❌ No valid CSV files found!")
        return
    
    print(f"\n📊 Summary:")
    print(f"Files loaded: {len(files_found)}")
    for file_info in files_found:
        print(f"  - {file_info}")
    
    if files_missing:
        print(f"Files missing: {len(files_missing)}")
        for missing_info in files_missing:
            print(f"  - {missing_info}")
    
    # Combine all dataframes
    print(f"\n🔄 Combining data...")
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    
    # Ensure merge rate column is numeric
    combined_df['30d_merge_rate'] = pd.to_numeric(combined_df['30d_merge_rate'], errors='coerce')
    
    # Sort by merge rate (highest first)
    print(f"📈 Sorting by merge rate (highest first)...")
    sorted_df = combined_df.sort_values('30d_merge_rate', ascending=False)
    
    # Generate output files
    output_dir = 'data/output'
    os.makedirs(output_dir, exist_ok=True)
    
    # Main sorted file
    main_output = f"{output_dir}/merge_rates_sorted_by_highest.csv"
    sorted_df.to_csv(main_output, index=False)
    print(f"💾 Saved main results: {main_output}")
    
    # Top 50 most active repositories
    top_50 = sorted_df.head(50)
    top_50_output = f"{output_dir}/top_50_most_active_repos.csv"
    top_50.to_csv(top_50_output, index=False)
    print(f"💾 Saved top 50: {top_50_output}")
    
    # Analysis summary
    print(f"\n📋 Analysis Results:")
    print(f"Total repositories: {len(sorted_df):,}")
    print(f"Active repositories (>0 merges): {len(sorted_df[sorted_df['30d_merge_rate'] > 0]):,}")
    print(f"Inactive repositories (0 merges): {len(sorted_df[sorted_df['30d_merge_rate'] == 0]):,}")
    print(f"Highest merge rate: {sorted_df['30d_merge_rate'].max()}")
    print(f"Average merge rate: {sorted_df['30d_merge_rate'].mean():.2f}")
    
    # Top performers
    print(f"\n🏆 Top 10 Most Active Repositories:")
    top_10 = sorted_df.head(10)
    for idx, row in top_10.iterrows():
        print(f"  {row['30d_merge_rate']:3d} merges - {row['org']}/{row['repo']} ({row['source']})")
    
    # Summary by source
    print(f"\n📊 Summary by Source:")
    source_summary = sorted_df.groupby('source').agg({
        '30d_merge_rate': ['count', 'mean', 'max', 'sum']
    }).round(2)
    
    for source in source_summary.index:
        count = source_summary.loc[source, ('30d_merge_rate', 'count')]
        mean_rate = source_summary.loc[source, ('30d_merge_rate', 'mean')]
        max_rate = source_summary.loc[source, ('30d_merge_rate', 'max')]
        total_merges = source_summary.loc[source, ('30d_merge_rate', 'sum')]
        print(f"  {source}: {count:,} repos, avg {mean_rate:.1f}, max {max_rate:.0f}, total {total_merges:.0f} merges")
    
    # Save summary to file
    summary_output = f"{output_dir}/merge_rate_summary.txt"
    with open(summary_output, 'w') as f:
        f.write(f"Merge Rate Analysis Summary\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Total repositories: {len(sorted_df):,}\n")
        f.write(f"Active repositories (>0 merges): {len(sorted_df[sorted_df['30d_merge_rate'] > 0]):,}\n")
        f.write(f"Inactive repositories (0 merges): {len(sorted_df[sorted_df['30d_merge_rate'] == 0]):,}\n")
        f.write(f"Highest merge rate: {sorted_df['30d_merge_rate'].max()}\n")
        f.write(f"Average merge rate: {sorted_df['30d_merge_rate'].mean():.2f}\n\n")
        
        f.write("Top 10 Most Active Repositories:\n")
        for idx, row in top_10.iterrows():
            f.write(f"  {row['30d_merge_rate']:3d} merges - {row['org']}/{row['repo']} ({row['source']})\n")
    
    print(f"💾 Saved summary: {summary_output}")
    print(f"\n✅ Analysis complete!")

if __name__ == "__main__":
    analyze_merge_rates()