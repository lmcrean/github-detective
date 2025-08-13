#!/usr/bin/env python3
"""
Entry point script for GitHub repository data collection.
"""

import sys
import os

# Add parent directory to path for absolute imports from project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.github_client.collector import main

if __name__ == '__main__':
    main()