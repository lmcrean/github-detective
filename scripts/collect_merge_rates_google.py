#!/usr/bin/env python3
"""Merge rate collection for Google repositories."""

import os
import sys

# Add scripts directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from simple_merge_rate_collector import SimpleMergeRateCollector

def main():
    """Collect merge rates for Google repositories."""
    
    # File paths
    input_file = "data/repos/batch_Aug_18/big_three_recent_commits.csv"
    progress_file = ".notes/progress_google.txt"
    output_file = "data/output/merge_rates_google.csv"
    
    # Initialize collector
    collector = SimpleMergeRateCollector(progress_file, output_file)
    
    # Start collection
    collector._log_progress("=== Starting Google Merge Rate Collection ===")
    collector._log_progress("Input file: " + input_file)
    collector._log_progress("Output file: " + output_file)
    
    try:
        collector.collect_from_existing_data(input_file, company_filter="Google")
    except KeyboardInterrupt:
        collector._log_progress("Collection interrupted by user")
    except Exception as e:
        collector._log_progress(f"Collection failed with error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()