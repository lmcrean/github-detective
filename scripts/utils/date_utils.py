"""Date utility functions for parsing and formatting dates."""

from datetime import datetime, timedelta
from typing import Optional, Union
import re


class DateUtils:
    """Utility class for date operations."""
    
    @staticmethod
    def parse_iso_date(date_string: str) -> Optional[datetime]:
        """Parse ISO format date string to datetime object."""
        try:
            # Handle various ISO formats
            if 'T' in date_string:
                return datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            else:
                return datetime.fromisoformat(date_string)
        except ValueError:
            return None
    
    @staticmethod
    def format_date(dt: datetime, format_str: str = '%Y-%m-%d') -> str:
        """Format datetime object to string."""
        return dt.strftime(format_str)
    
    @staticmethod
    def get_date_range(start_date: str, end_date: str) -> tuple:
        """Get date range as tuple of datetime objects."""
        start_dt = DateUtils.parse_iso_date(start_date)
        end_dt = DateUtils.parse_iso_date(end_date)
        return (start_dt, end_dt)
    
    @staticmethod
    def days_ago(date_string: str) -> int:
        """Calculate number of days ago from date string."""
        date_obj = DateUtils.parse_iso_date(date_string)
        if date_obj is None:
            return -1
        
        now = datetime.now()
        if date_obj.tzinfo is not None:
            # Make now timezone-aware
            import pytz
            now = now.replace(tzinfo=pytz.UTC)
        
        return (now - date_obj).days
    
    @staticmethod
    def is_within_days(date_string: str, days: int) -> bool:
        """Check if date is within specified number of days from now."""
        days_past = DateUtils.days_ago(date_string)
        return days_past >= 0 and days_past <= days
    
    @staticmethod
    def is_after_date(date_string: str, threshold_date: str) -> bool:
        """Check if date is after threshold date."""
        date_obj = DateUtils.parse_iso_date(date_string)
        threshold_obj = DateUtils.parse_iso_date(threshold_date)
        
        if date_obj is None or threshold_obj is None:
            return False
        
        return date_obj > threshold_obj
    
    @staticmethod
    def get_current_timestamp() -> str:
        """Get current timestamp in ISO format."""
        return datetime.now().isoformat()
    
    @staticmethod
    def extract_date_from_string(text: str) -> Optional[str]:
        """Extract date in YYYY-MM-DD format from string."""
        pattern = r'\d{4}-\d{2}-\d{2}'
        match = re.search(pattern, text)
        return match.group(0) if match else None
    
    @staticmethod
    def add_days(date_string: str, days: int) -> str:
        """Add specified number of days to date string."""
        date_obj = DateUtils.parse_iso_date(date_string)
        if date_obj is None:
            raise ValueError(f"Invalid date format: {date_string}")
        
        new_date = date_obj + timedelta(days=days)
        return DateUtils.format_date(new_date)