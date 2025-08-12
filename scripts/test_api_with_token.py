"""Test GitHub API with token for shopify/cli."""

import os
import requests
from pathlib import Path

# Load .env file
env_path = Path(__file__).parent.parent / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

token = os.getenv('API_GITHUB_TOKEN')
print(f"Token loaded: {'Yes' if token else 'No'}")
print(f"Token starts with: {token[:10]+'...' if token else 'None'}")

headers = {'Authorization': f'token {token}'} if token else {}

print("\nTesting shopify/cli issues endpoint WITH token:")
resp = requests.get('https://api.github.com/repos/shopify/cli/issues?state=open&per_page=100', headers=headers)
print(f"Status: {resp.status_code}")

if resp.status_code == 200:
    items = resp.json()
    issues = [i for i in items if 'pull_request' not in i]
    prs_in_issues = [i for i in items if 'pull_request' in i]
    
    print(f"Total items: {len(items)}")
    print(f"Issues (no PR key): {len(issues)}")
    print(f"PRs in issues endpoint: {len(prs_in_issues)}")
    
    if items:
        print("\nFirst 3 items:")
        for item in items[:3]:
            is_pr = 'pull_request' in item
            print(f"  #{item['number']}: {'[PR]' if is_pr else '[ISSUE]'} {item['title'][:40]}")
else:
    print(f"Error: {resp.text[:200]}")

print("\nTesting shopify/cli pulls endpoint:")
resp = requests.get('https://api.github.com/repos/shopify/cli/pulls?state=open&per_page=100', headers=headers)
print(f"Status: {resp.status_code}")
if resp.status_code == 200:
    print(f"Open PRs: {len(resp.json())}")

print("\nCalculated results:")
print(f"- If issues endpoint works: {len(issues) if resp.status_code == 200 else '?'} issues")
print(f"- From pulls endpoint: 46 PRs expected")
print(f"- From repo endpoint: 89 total (43 issues + 46 PRs)")