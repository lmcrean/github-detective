"""File utility functions for common file operations."""

import os
import json
import shutil
from typing import Any, Dict, List, Optional
from pathlib import Path


class FileUtils:
    """Utility class for file operations."""
    
    @staticmethod
    def ensure_directory(path: str) -> None:
        """Ensure directory exists, create if it doesn't."""
        os.makedirs(path, exist_ok=True)
    
    @staticmethod
    def read_json(file_path: str) -> Dict[str, Any]:
        """Read JSON file and return dictionary."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    @staticmethod
    def write_json(data: Dict[str, Any], file_path: str, indent: int = 2) -> None:
        """Write dictionary to JSON file."""
        FileUtils.ensure_directory(os.path.dirname(file_path))
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
    
    @staticmethod
    def read_text(file_path: str) -> str:
        """Read text file and return content."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    @staticmethod
    def write_text(content: str, file_path: str) -> None:
        """Write text content to file."""
        FileUtils.ensure_directory(os.path.dirname(file_path))
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    @staticmethod
    def copy_file(src: str, dst: str) -> None:
        """Copy file from source to destination."""
        FileUtils.ensure_directory(os.path.dirname(dst))
        shutil.copy2(src, dst)
    
    @staticmethod
    def move_file(src: str, dst: str) -> None:
        """Move file from source to destination."""
        FileUtils.ensure_directory(os.path.dirname(dst))
        shutil.move(src, dst)
    
    @staticmethod
    def delete_file(file_path: str) -> None:
        """Delete file if it exists."""
        if os.path.exists(file_path):
            os.remove(file_path)
    
    @staticmethod
    def list_files(directory: str, extension: Optional[str] = None) -> List[str]:
        """List files in directory, optionally filtered by extension."""
        if not os.path.exists(directory):
            return []
        
        files = []
        for filename in os.listdir(directory):
            if extension is None or filename.endswith(extension):
                files.append(os.path.join(directory, filename))
        
        return files
    
    @staticmethod
    def get_file_size(file_path: str) -> int:
        """Get file size in bytes."""
        return os.path.getsize(file_path) if os.path.exists(file_path) else 0
    
    @staticmethod
    def get_file_modified_time(file_path: str) -> float:
        """Get file modification time as timestamp."""
        return os.path.getmtime(file_path) if os.path.exists(file_path) else 0
    
    @staticmethod
    def find_files(directory: str, pattern: str) -> List[str]:
        """Find files matching pattern using glob."""
        from glob import glob
        search_path = os.path.join(directory, pattern)
        return glob(search_path)
    
    @staticmethod
    def create_backup(file_path: str) -> str:
        """Create backup of file with .bak extension."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        backup_path = f"{file_path}.bak"
        shutil.copy2(file_path, backup_path)
        return backup_path