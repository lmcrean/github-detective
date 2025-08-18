"""Step 2: Calculate 30-day merge rates for discovered repositories."""

import csv
import os
import sys
import time
import logging
from pathlib import Path
from typing import Dict, List
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.repos.metrics.pr_metrics import MergedPRsFetcher

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class MergeRateCalculator:
    """Calculate merge rates for repositories from checkpoint."""
    
    def __init__(self):
        """Initialize with PR fetcher."""
        self.pr_fetcher = MergedPRsFetcher()
        self.processed_count = 0
        self.error_count = 0
        
    def load_checkpoint(self, filepath: str) -> List[Dict]:
        """Load repository list from checkpoint CSV."""
        logger.info(f"Loading checkpoint from {filepath}")
        
        repos = []
        with open(filepath, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                repos.append(row)
        
        logger.info(f"Loaded {len(repos)} repositories from checkpoint")
        return repos
    
    def calculate_merge_rates(self, repos: List[Dict], batch_size: int = 10, batch_delay: int = 30) -> List[Dict]:
        """Calculate merge rates for all repositories with batching."""
        total = len(repos)
        logger.info(f"Starting merge rate calculation for {total} repositories")
        logger.info(f"Batch size: {batch_size}, Delay between batches: {batch_delay}s")
        
        for i, repo in enumerate(repos, 1):
            github_org = repo['github_org']
            repo_name = repo['repo']
            
            logger.info(f"[{i}/{total}] Processing {github_org}/{repo_name}")
            
            try:
                # Calculate 30-day merge rate
                merge_count = self.pr_fetcher.get_merged_prs_count(github_org, repo_name, 30)
                
                if merge_count >= 0:
                    repo['30d_merge_rate'] = str(merge_count)
                    self.processed_count += 1
                    logger.info(f"  ✓ {merge_count} merges in last 30 days")
                else:
                    repo['30d_merge_rate'] = '0'
                    self.error_count += 1
                    logger.warning(f"  ⚠ Failed to get merge rate, defaulting to 0")
                    
            except Exception as e:
                repo['30d_merge_rate'] = '0'
                self.error_count += 1
                logger.error(f"  ✗ Error: {str(e)}")
            
            # Rate limiting
            if i < total:  # Don't sleep after last item
                time.sleep(5)  # 5 seconds between each API call
                
                # Longer break after each batch
                if i % batch_size == 0:
                    logger.info(f"Completed batch {i//batch_size}. Taking {batch_delay}s break...")
                    logger.info(f"Progress: {self.processed_count} successful, {self.error_count} errors")
                    time.sleep(batch_delay)
        
        return repos
    
    def save_final_results(self, repos: List[Dict], output_filepath: str):
        """Save final results with merge rates to CSV."""
        logger.info(f"Saving final results to {output_filepath}")
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        
        # Save with only the required columns
        with open(output_filepath, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['org', 'repo', 'hyperlink', '30d_merge_rate']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            
            writer.writeheader()
            for repo in repos:
                # Write only the required fields
                writer.writerow({
                    'org': repo['org'],
                    'repo': repo['repo'],
                    'hyperlink': repo['hyperlink'],
                    '30d_merge_rate': repo['30d_merge_rate']
                })
        
        logger.info(f"✅ Final results saved to {output_filepath}")
    
    def print_statistics(self, repos: List[Dict]):
        """Print statistics about the merge rates."""
        # Calculate statistics
        merge_rates = [int(r['30d_merge_rate']) for r in repos if r['30d_merge_rate'].isdigit()]
        
        if merge_rates:
            total_merges = sum(merge_rates)
            avg_merges = total_merges / len(merge_rates)
            max_merges = max(merge_rates)
            active_repos = len([m for m in merge_rates if m > 0])
            
            logger.info("\n=== Merge Rate Statistics ===")
            logger.info(f"Total repositories: {len(repos)}")
            logger.info(f"Successfully processed: {self.processed_count}")
            logger.info(f"Errors: {self.error_count}")
            logger.info(f"Active repos (>0 merges): {active_repos}")
            logger.info(f"Total merges (30 days): {total_merges}")
            logger.info(f"Average merges per repo: {avg_merges:.1f}")
            logger.info(f"Most active repo: {max_merges} merges")
            
            # Find top 5 most active repos
            sorted_repos = sorted(repos, key=lambda r: int(r['30d_merge_rate']) if r['30d_merge_rate'].isdigit() else 0, reverse=True)[:5]
            logger.info("\nTop 5 most active repositories:")
            for repo in sorted_repos:
                logger.info(f"  {repo['org']}/{repo['repo']}: {repo['30d_merge_rate']} merges")


def main():
    """Main function to calculate merge rates."""
    logger.info("Starting merge rate calculation")
    
    # Paths
    checkpoint_file = Path(__file__).parent.parent / 'data' / 'repos' / 'all_org_repos_checkpoint.csv'
    output_file = Path(__file__).parent.parent / 'data' / 'repos' / 'high_revenue_companies.csv'
    
    # Check if checkpoint exists
    if not checkpoint_file.exists():
        logger.error(f"Checkpoint file not found at {checkpoint_file}")
        logger.error("Please run discover_org_repos.py first to create the checkpoint")
        sys.exit(1)
    
    # Initialize calculator
    calculator = MergeRateCalculator()
    
    try:
        # Load checkpoint
        repos = calculator.load_checkpoint(str(checkpoint_file))
        
        # Ask for confirmation before proceeding
        logger.info(f"\n⚠️  This will make approximately {len(repos)} API calls to GitHub")
        logger.info(f"Estimated time: {(len(repos) * 5 + (len(repos) // 10) * 30) / 60:.1f} minutes")
        
        # Calculate merge rates
        repos_with_rates = calculator.calculate_merge_rates(repos)
        
        # Save final results
        calculator.save_final_results(repos_with_rates, str(output_file))
        
        # Print statistics
        calculator.print_statistics(repos_with_rates)
        
        logger.info(f"\n✅ Complete! Results saved to: {output_file}")
        
    except KeyboardInterrupt:
        logger.warning("\n⚠️  Process interrupted by user")
        logger.info("Partial results may have been saved")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Calculation failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()