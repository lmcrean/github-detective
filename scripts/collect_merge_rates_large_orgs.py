#!/usr/bin/env python3
"""Merge rate collection for large organizations."""

import os
import sys

# Add scripts directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from simple_merge_rate_collector import SimpleMergeRateCollector

def main():
    """Collect merge rates for large organization repositories."""
    
    # File paths
    input_file = "data/repos/batch_Aug_18/org_repo_counts_large.csv"
    progress_file = ".notes/progress_large_orgs.txt"
    output_file = "data/output/merge_rates_large_orgs.csv"
    
    # Initialize collector
    collector = SimpleMergeRateCollector(progress_file, output_file)
    
    # Start collection
    collector._log_progress("=== Starting Large Orgs Merge Rate Collection ===")
    collector._log_progress("Input file: " + input_file)
    collector._log_progress("Output file: " + output_file)
    
    try:
        collector.collect_from_org_list(input_file)
    except KeyboardInterrupt:
        collector._log_progress("Collection interrupted by user")
    except Exception as e:
        collector._log_progress(f"Collection failed with error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()