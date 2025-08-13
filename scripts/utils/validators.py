"""Data validation utilities."""

import re
from typing import Any, Dict, List, Optional, Union


class Validators:
    """Utility class for data validation."""
    
    @staticmethod
    def is_valid_repo_path(repo_path: str) -> bool:
        """Validate GitHub repository path format (owner/repo)."""
        pattern = r'^[a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+$'
        return bool(re.match(pattern, repo_path))
    
    @staticmethod
    def is_valid_github_url(url: str) -> bool:
        """Validate GitHub URL format."""
        pattern = r'^https://github\.com/[a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+.*$'
        return bool(re.match(pattern, url))
    
    @staticmethod
    def is_positive_integer(value: Any) -> bool:
        """Check if value is a positive integer."""
        try:
            num = int(value)
            return num >= 0
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_valid_date(date_string: str) -> bool:
        """Validate ISO date format."""
        try:
            from datetime import datetime
            datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_repository_data(data: Dict[str, Any]) -> List[str]:
        """
        Validate repository data dictionary.
        
        Args:
            data: Repository data dictionary
        
        Returns:
            List of validation error messages (empty if valid)
        """
        errors = []
        
        # Required fields
        required_fields = ['Name', 'Stars', 'Forks', 'Open Issues']
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
            elif data[field] is None:
                errors.append(f"Field cannot be None: {field}")
        
        # Validate repository path
        if 'Name' in data and not Validators.is_valid_repo_path(data['Name']):
            errors.append(f"Invalid repository path format: {data['Name']}")
        
        # Validate numeric fields
        numeric_fields = ['Stars', 'Forks', 'Contributors', 'Open Issues', 'Open Pull Requests']
        for field in numeric_fields:
            if field in data and not Validators.is_positive_integer(data[field]) and data[field] != -1:
                errors.append(f"Invalid numeric value for {field}: {data[field]}")
        
        # Validate dates
        date_fields = ['Date Created', 'Last Active']
        for field in date_fields:
            if field in data and data[field] and not Validators.is_valid_date(str(data[field])):
                errors.append(f"Invalid date format for {field}: {data[field]}")
        
        return errors
    
    @staticmethod
    def validate_issue_data(data: Dict[str, Any]) -> List[str]:
        """
        Validate issue data dictionary.
        
        Args:
            data: Issue data dictionary
        
        Returns:
            List of validation error messages (empty if valid)
        """
        errors = []
        
        # Required fields
        required_fields = ['number', 'title', 'state']
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
            elif data[field] is None:
                errors.append(f"Field cannot be None: {field}")
        
        # Validate issue number
        if 'number' in data and not Validators.is_positive_integer(data['number']):
            errors.append(f"Invalid issue number: {data['number']}")
        
        # Validate state
        if 'state' in data and data['state'] not in ['open', 'closed']:
            errors.append(f"Invalid issue state: {data['state']}")
        
        # Validate comments count
        if 'comments' in data and not Validators.is_positive_integer(data['comments']):
            errors.append(f"Invalid comments count: {data['comments']}")
        
        return errors
    
    @staticmethod
    def clean_repository_data(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Clean and normalize repository data.
        
        Args:
            data: Repository data dictionary
        
        Returns:
            Cleaned repository data dictionary
        """
        cleaned = data.copy()
        
        # Convert numeric strings to integers
        numeric_fields = ['Stars', 'Forks', 'Contributors', 'Open Issues', 'Open Pull Requests']
        for field in numeric_fields:
            if field in cleaned:
                try:
                    cleaned[field] = int(cleaned[field])
                except (ValueError, TypeError):
                    cleaned[field] = -1  # Use -1 for unknown values
        
        # Clean repository path
        if 'Name' in cleaned:
            cleaned['Name'] = str(cleaned['Name']).strip()
        
        # Clean languages field
        if 'Top Languages' in cleaned and cleaned['Top Languages']:
            cleaned['Top Languages'] = str(cleaned['Top Languages']).strip()
        
        return cleaned
    
    @staticmethod
    def is_valid_csv_file(file_path: str) -> bool:
        """Check if file is a valid CSV file."""
        try:
            import csv
            import os
            
            if not os.path.exists(file_path):
                return False
            
            with open(file_path, 'r', encoding='utf-8') as f:
                # Try to read first few rows
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if i >= 2:  # Just check first couple rows
                        break
            
            return True
        except Exception:
            return False