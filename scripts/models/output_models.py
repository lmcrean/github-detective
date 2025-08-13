"""Output format models for different export types."""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any
from .base import BaseModel


class OutputFormat(Enum):
    """Supported output formats."""
    CSV = "csv"
    JSON = "json"
    MARKDOWN = "markdown"


@dataclass
class ExportConfig(BaseModel):
    """Configuration for data export."""
    format: OutputFormat
    output_path: str
    include_headers: bool = True
    delimiter: str = ","
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary format."""
        return {
            'format': self.format.value,
            'output_path': self.output_path,
            'include_headers': self.include_headers,
            'delimiter': self.delimiter
        }