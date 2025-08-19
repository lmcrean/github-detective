#!/usr/bin/env python3
"""Merge rate collection for Meta repositories."""

import os
import sys

# Add scripts directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from simple_merge_rate_collector import SimpleMergeRateCollector

def main():
    """Collect merge rates for Meta repositories."""
    
    # File paths
    input_file = "data/repos/batch_Aug_18/big_three_recent_commits.csv"
    progress_file = ".notes/progress_meta.txt"
    output_file = "data/output/repo_health_meta.csv"
    
    # Initialize collector
    collector = SimpleMergeRateCollector(progress_file, output_file)
    
    # Start collection
    collector._log_progress("=== Starting Meta Repo Health Collection ===")
    collector._log_progress("Collecting: commits_last_30d + PRs_closed_30d")
    collector._log_progress("Input file: " + input_file)
    collector._log_progress("Output file: " + output_file)
    
    try:
        collector.collect_from_existing_data(input_file, company_filter="Meta")
    except KeyboardInterrupt:
        collector._log_progress("Collection interrupted by user")
    except Exception as e:
        collector._log_progress(f"Collection failed with error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()