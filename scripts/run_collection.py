#!/usr/bin/env python3
"""
Entry point script for GitHub repository data collection.
"""

import sys
import os

from github_client.collector import main

if __name__ == '__main__':
    main()