"""Base model classes for all data models."""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseModel(ABC):
    """Base class for all data models."""
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary representation."""
        pass
    
    def __repr__(self) -> str:
        """String representation of the model."""
        class_name = self.__class__.__name__
        attrs = ', '.join(f'{k}={v}' for k, v in self.to_dict().items())
        return f'{class_name}({attrs})'