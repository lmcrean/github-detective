"""CSV utility functions for reading, writing, and processing CSV files."""

import csv
import os
from typing import List, Dict, Any, Optional


class CSVUtils:
    """Utility class for CSV operations."""
    
    @staticmethod
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
    
    @staticmethod
    def write_csv_file(file_path: str, data: List[Dict[str, Any]], fieldnames: Optional[List[str]] = None) -> None:
        """
        Write list of dictionaries to CSV file.
        
        Args:
            file_path: Output CSV file path
            data: List of dictionaries to write
            fieldnames: Optional list of field names (uses keys from first row if None)
        """
        if not data:
            raise ValueError("No data to write")
        
        # Create output directory if needed
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Use fieldnames from first row if not provided
        if fieldnames is None:
            fieldnames = list(data[0].keys())
        
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    
    @staticmethod
    def combine_csv_files(input_files: List[str], output_file: str, sort_by: str = None) -> None:
        """
        Combine multiple CSV files into one.
        
        Args:
            input_files: List of input CSV file paths
            output_file: Output CSV file path
            sort_by: Optional column to sort by
        """
        all_rows = []
        
        # Read all input files
        for file_path in input_files:
            rows = CSVUtils.read_csv_file(file_path)
            all_rows.extend(rows)
        
        # Sort if requested
        if sort_by and all_rows and sort_by in all_rows[0]:
            try:
                # Try numeric sort
                all_rows.sort(key=lambda x: int(x.get(sort_by, 0)), reverse=True)
            except ValueError:
                # Fall back to string sort
                all_rows.sort(key=lambda x: x.get(sort_by, ''), reverse=True)
        
        # Write combined data
        CSVUtils.write_csv_file(output_file, all_rows)
    
    @staticmethod
    def add_hyperlink_column(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Add GitHub hyperlink column to repository data.
        
        Args:
            rows: List of row dictionaries
        
        Returns:
            List of row dictionaries with hyperlink column added
        """
        for row in rows:
            if 'org_name' in row and 'repo_name' in row:
                org_name = row.get('org_name', '')
                repo_name = row.get('repo_name', '')
                row['hyperlink'] = f"https://github.com/{org_name}/{repo_name}"
            elif 'Name' in row:
                # Handle repo_path format like "owner/repo"
                row['hyperlink'] = f"https://github.com/{row['Name']}"
        
        return rows
    
    @staticmethod
    def filter_rows(rows: List[Dict[str, Any]], filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Filter rows based on criteria.
        
        Args:
            rows: List of row dictionaries
            filters: Dictionary of field -> value filters
        
        Returns:
            Filtered list of rows
        """
        filtered = []
        for row in rows:
            match = True
            for field, value in filters.items():
                if field not in row or row[field] != value:
                    match = False
                    break
            if match:
                filtered.append(row)
        
        return filtered