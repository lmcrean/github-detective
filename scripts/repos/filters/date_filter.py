"""Date-based filtering for repository data."""

import csv
import os
from datetime import datetime
from typing import List, Dict, Any
from ...utils.date_utils import DateUtils


class DateFilter:
    """Filter repositories based on date criteria."""
    
    def __init__(self, cutoff_date: str = "2025-03-01"):
        """
        Initialize date filter.
        
        Args:
            cutoff_date: Date string in YYYY-MM-DD format
        """
        self.cutoff_date = cutoff_date
        self.cutoff_datetime = datetime.strptime(cutoff_date, "%Y-%m-%d")
    
    def filter_by_push_date(self, input_csv: str, output_csv: str) -> int:
        """
        Filter out repositories pushed before the cutoff date.
        
        Args:
            input_csv: Path to input CSV file
            output_csv: Path to output CSV file
        
        Returns:
            Number of repositories kept after filtering
        """
        kept_count = 0
        total_count = 0
        
        with open(input_csv, 'r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            
            rows_to_keep = []
            
            for row in reader:
                total_count += 1
                
                # Parse the last_pushed_date
                push_date_str = row.get('last_pushed_date', '')
                
                if push_date_str:
                    try:
                        push_date = datetime.strptime(push_date_str, "%Y-%m-%d")
                        
                        # Keep if pushed on or after cutoff date
                        if push_date >= self.cutoff_datetime:
                            rows_to_keep.append(row)
                            kept_count += 1
                        else:
                            print(f"  Filtering out {row.get('org_name', '')}/{row.get('repo_name', '')} (last pushed: {push_date_str})")
                            
                    except ValueError as e:
                        print(f"  Warning: Invalid date format for {row.get('org_name', '')}/{row.get('repo_name', '')}: {push_date_str}")
                        # Keep rows with invalid dates (conservative approach)
                        rows_to_keep.append(row)
                        kept_count += 1
                else:
                    # Keep rows without push date (conservative approach)
                    rows_to_keep.append(row)
                    kept_count += 1
        
        # Create output directory if needed
        os.makedirs(os.path.dirname(output_csv), exist_ok=True)
        
        # Write filtered data
        with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows_to_keep)
        
        print(f"Date filter complete: Kept {kept_count}/{total_count} repositories (removed {total_count - kept_count})")
        return kept_count
    
    def filter_repositories_data(self, repositories: List[Dict[str, Any]], date_field: str = 'last_pushed_date') -> List[Dict[str, Any]]:
        """
        Filter repository data in memory.
        
        Args:
            repositories: List of repository dictionaries
            date_field: Field name containing the date to filter by
        
        Returns:
            Filtered list of repositories
        """
        filtered = []
        
        for repo in repositories:
            date_str = repo.get(date_field, '')
            
            if date_str:
                if DateUtils.is_after_date(date_str, self.cutoff_date):
                    filtered.append(repo)
            else:
                # Keep repositories without date (conservative approach)
                filtered.append(repo)
        
        return filtered
    
    def apply_to_organization(self, org_name: str, input_csv: str) -> str:
        """
        Apply date filter to an organization's CSV file.
        
        Args:
            org_name: Organization name
            input_csv: Path to input CSV
        
        Returns:
            Path to filtered output file
        """
        # Generate output filename with filter1 and date
        date_str = datetime.now().strftime('%Y%m%d')
        
        # Extract directory path
        dir_path = os.path.dirname(input_csv)
        output_csv = os.path.join(dir_path, f"{org_name}_repos_filter1_{date_str}.csv")
        
        print(f"\nApplying Date Filter to {org_name}...")
        print(f"  Cutoff date: {self.cutoff_date}")
        print(f"  Input: {input_csv}")
        print(f"  Output: {output_csv}")
        
        kept_count = self.filter_by_push_date(input_csv, output_csv)
        
        return output_csv
    
    def batch_filter(self, org_configs: Dict[str, str]) -> Dict[str, str]:
        """
        Apply date filter to multiple organizations.
        
        Args:
            org_configs: Dictionary mapping org names to CSV paths
        
        Returns:
            Dictionary mapping org names to filtered output paths
        """
        results = {}
        
        for org_name, input_csv in org_configs.items():
            if not os.path.exists(input_csv):
                print(f"Warning: Input file not found for {org_name}: {input_csv}")
                continue
            
            try:
                output_path = self.apply_to_organization(org_name, input_csv)
                results[org_name] = output_path
                print(f"[SUCCESS] Successfully filtered {org_name}")
                
            except Exception as e:
                print(f"[ERROR] Error filtering {org_name}: {str(e)}")
                results[org_name] = None
        
        return results


# Backward compatibility functions
def filter_by_push_date(input_csv: str, output_csv: str, cutoff_date: str = "2025-03-01") -> int:
    """Backward compatibility wrapper."""
    filter_instance = DateFilter(cutoff_date)
    return filter_instance.filter_by_push_date(input_csv, output_csv)

def apply_filter1_to_org(org_name: str, input_csv: str, cutoff_date: str = "2025-03-01") -> str:
    """Backward compatibility wrapper."""
    filter_instance = DateFilter(cutoff_date)
    return filter_instance.apply_to_organization(org_name, input_csv)