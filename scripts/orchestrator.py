"""Main orchestrator for the complete filtering pipeline."""

import os
import sys
from datetime import datetime
from typing import Dict, Tuple

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.merged_prs_30d.add_pr_column import process_org_csv
from scripts.filters.filter_by_date import apply_filter1_to_org
from scripts.filters.filter_by_pr_activity import apply_filter2_to_org
from scripts.filters.filter_top_percentile import apply_filter3_to_org


class PipelineOrchestrator:
    """Orchestrate the complete filtering pipeline for organizations."""
    
    def __init__(self, base_dir: str = "data/orgs"):
        """
        Initialize the orchestrator.
        
        Args:
            base_dir: Base directory containing organization data
        """
        self.base_dir = base_dir
        self.timestamp = datetime.now().strftime('%Y%m%d')
    
    def process_organization(self, org_name: str, input_csv: str = None) -> Dict[str, str]:
        """
        Process a single organization through all filters.
        
        Args:
            org_name: Organization name
            input_csv: Optional input CSV path (defaults to latest)
        
        Returns:
            Dictionary with paths to all generated files
        """
        results = {
            'original': None,
            'filter1': None,
            'filter2': None,
            'filter3': None
        }
        
        # Determine input file
        if not input_csv:
            org_dir = os.path.join(self.base_dir, org_name)
            input_csv = os.path.join(org_dir, f"{org_name}_repos_latest.csv")
        
        if not os.path.exists(input_csv):
            print(f"Error: Input file not found for {org_name}: {input_csv}")
            return results
        
        results['original'] = input_csv
        
        print(f"\n{'='*60}")
        print(f"PROCESSING {org_name.upper()}")
        print(f"{'='*60}")
        
        try:
            # Step 1: Apply Filter 1 (Date filter - remove repos pushed before March 2025)
            print(f"\n[Step 1/4] Applying Date Filter...")
            filter1_output = apply_filter1_to_org(org_name, input_csv, "2025-03-01")
            results['filter1'] = filter1_output
            
            if not os.path.exists(filter1_output):
                print(f"Error: Filter 1 failed to create output")
                return results
            
            # Step 2: Add merged PRs column
            print(f"\n[Step 2/4] Adding merged_prs_30d column...")
            pr_output = process_org_csv(org_name, filter1_output, f"with_prs_{self.timestamp}")
            
            if not os.path.exists(pr_output):
                print(f"Error: Failed to add PR column")
                return results
            
            # Step 3: Apply Filter 2 (with PR data)
            print(f"\n[Step 3/4] Applying PR Activity Filter...")
            filter2_output = apply_filter2_to_org(org_name, pr_output)
            results['filter2'] = filter2_output
            
            if not os.path.exists(filter2_output):
                print(f"Error: Filter 2 failed to create output")
                return results
            
            # Step 4: Apply Filter 3 (Top 50%)
            print(f"\n[Step 4/4] Applying Top 50% Filter...")
            filter3_output = apply_filter3_to_org(org_name, filter2_output, percentile=0.5)
            results['filter3'] = filter3_output
            
            if not os.path.exists(filter3_output):
                print(f"Error: Filter 3 failed to create output")
                return results
            
            print(f"\n[SUCCESS] Successfully processed {org_name} through all filters")
            
        except Exception as e:
            print(f"\n[ERROR] Error processing {org_name}: {str(e)}")
            import traceback
            traceback.print_exc()
        
        return results
    
    def process_multiple_organizations(self, org_names: list) -> Dict[str, Dict[str, str]]:
        """
        Process multiple organizations through the pipeline.
        
        Args:
            org_names: List of organization names
        
        Returns:
            Dictionary mapping org names to their results
        """
        all_results = {}
        
        print(f"\n{'='*60}")
        print(f"BATCH PROCESSING PIPELINE")
        print(f"Organizations: {', '.join(org_names)}")
        print(f"Timestamp: {self.timestamp}")
        print(f"{'='*60}")
        
        for org_name in org_names:
            results = self.process_organization(org_name)
            all_results[org_name] = results
        
        # Print summary
        self.print_summary(all_results)
        
        return all_results
    
    def print_summary(self, all_results: Dict[str, Dict[str, str]]):
        """Print a summary of the pipeline results."""
        print(f"\n{'='*60}")
        print("PIPELINE SUMMARY")
        print(f"{'='*60}")
        
        for org_name, results in all_results.items():
            print(f"\n{org_name.upper()}:")
            
            if results['filter3'] and os.path.exists(results['filter3']):
                # Count rows in final output
                with open(results['filter3'], 'r') as f:
                    row_count = sum(1 for line in f) - 1  # Subtract header
                print(f"  [SUCCESS] Complete - {row_count} repositories in final output")
                print(f"  Files created:")
                for filter_name, path in results.items():
                    if path and os.path.exists(path):
                        filename = os.path.basename(path)
                        print(f"    - {filename}")
            else:
                print(f"  [FAILED] Failed - Check logs for details")
        
        print(f"\n{'='*60}")
        print("PIPELINE COMPLETE")
        print(f"{'='*60}")


def main():
    """Main entry point for the orchestrator."""
    # Define organizations to process
    orgs_to_process = ['stripe', 'shopify']
    
    # Create orchestrator
    orchestrator = PipelineOrchestrator()
    
    # Process organizations
    results = orchestrator.process_multiple_organizations(orgs_to_process)
    
    # Check if all successful
    all_successful = all(
        results[org]['filter3'] and os.path.exists(results[org]['filter3'])
        for org in orgs_to_process
    )
    
    if all_successful:
        print("\n[SUCCESS] All organizations processed successfully!")
        return 0
    else:
        print("\n[ERROR] Some organizations failed to process completely.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)