#!/usr/bin/env python3
"""
Entry point script for GitHub repository data collection.
"""

import sys
import os

# Add src directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from github_client.collector import main

if __name__ == '__main__':
    main()