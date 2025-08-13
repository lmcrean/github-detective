"""Organizations module for GitHub organization analysis."""

try:
    from .collector import OrganizationCollector
    from .analyzer import OrganizationAnalyzer
    __all__ = ['OrganizationCollector', 'OrganizationAnalyzer']
except ImportError:
    # Handle import errors gracefully
    __all__ = []