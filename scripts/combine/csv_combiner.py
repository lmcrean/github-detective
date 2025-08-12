"""CSV Combiner for merging organization repository data."""

import argparse
import csv
import os
import sys
from typing import List, Dict


def read_csv_file(file_path: str) -> List[Dict[str, str]]:
    """
    Read CSV file and return list of dictionaries.
    
    Args:
        file_path: Path to the CSV file
    
    Returns:
        List of dictionaries representing rows
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")
    
    rows = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    
    return rows


def add_hyperlink_column(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Add hyperlink column to each row.
    
    Args:
        rows: List of row dictionaries
    
    Returns:
        List of row dictionaries with hyperlink column added
    """
    for row in rows:
        org_name = row.get('org_name', '')
        repo_name = row.get('repo_name', '')
        row['hyperlink'] = f"https://github.com/{org_name}/{repo_name}"
    
    return rows


def combine_and_sort_csvs(input_files: List[str], output_file: str, sort_by: str = 'merged_prs_30d'):
    """
    Combine multiple CSV files, add hyperlinks, and sort by specified column.
    
    Args:
        input_files: List of input CSV file paths
        output_file: Output CSV file path
        sort_by: Column to sort by (default: 'merged_prs_30d')
    """
    all_rows = []
    
    # Read all input files
    for file_path in input_files:
        print(f"Reading: {file_path}")
        rows = read_csv_file(file_path)
        print(f"  Found {len(rows)} rows")
        all_rows.extend(rows)
    
    print(f"Total rows combined: {len(all_rows)}")
    
    # Add hyperlink column
    all_rows = add_hyperlink_column(all_rows)
    
    # Sort by specified column (descending for merged_prs_30d)
    if sort_by in all_rows[0]:
        try:
            # Try to sort as numeric values
            all_rows.sort(key=lambda x: int(x.get(sort_by, 0)), reverse=True)
            print(f"Sorted by {sort_by} (numeric, descending)")
        except ValueError:
            # Fall back to string sorting
            all_rows.sort(key=lambda x: x.get(sort_by, ''), reverse=True)
            print(f"Sorted by {sort_by} (string, descending)")
    else:
        print(f"Warning: Sort column '{sort_by}' not found in data")
    
    # Determine output columns (preserve order, add hyperlink at end)
    if all_rows:
        columns = list(all_rows[0].keys())
        # Move hyperlink to the end if it's not already there
        if 'hyperlink' in columns:
            columns.remove('hyperlink')
            columns.append('hyperlink')
    else:
        raise ValueError("No data to write")
    
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Write combined CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        writer.writerows(all_rows)
    
    print(f"Combined CSV written to: {output_file}")
    print(f"Total rows written: {len(all_rows)}")


def main():
    """Main entry point for the CSV combiner."""
    parser = argparse.ArgumentParser(
        description='Combine CSV files with hyperlink generation and sorting'
    )
    parser.add_argument('--input1', required=True, help='First input CSV file')
    parser.add_argument('--input2', required=True, help='Second input CSV file')
    parser.add_argument('--output', required=True, help='Output CSV file path')
    parser.add_argument('--sort-by', default='merged_prs_30d', 
                       help='Column to sort by (default: merged_prs_30d)')
    
    args = parser.parse_args()
    
    try:
        input_files = [args.input1, args.input2]
        combine_and_sort_csvs(input_files, args.output, args.sort_by)
        print("SUCCESS: CSV combination completed!")
        return 0
    
    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())