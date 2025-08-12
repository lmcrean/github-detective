import pandas as pd
import requests
import re
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()
token = os.getenv('API_GITHUB_TOKEN')
headers = {'Authorization': f'token {token}'} if token else {}

def check_issue_status(url):
    # Extract owner, repo, issue number from URL
    pattern = r'https://github\.com/([^/]+)/([^/]+)/issues/(\d+)'
    match = re.match(pattern, url)
    
    if not match:
        return 'invalid_url'
    
    owner, repo, issue_number = match.groups()
    api_url = f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}'
    
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return response.json().get('state', 'unknown')
        elif response.status_code == 404:
            return 'not_found'
        else:
            return 'error'
    except:
        return 'error'

# Load CSV and check first 20 issues as a sample
df = pd.read_csv("C:\\Projects\\github-library\\data\\repos\\shopify_stripe_filter2.csv")
sample_size = 20

print(f"Checking first {sample_size} issues as a sample...")
open_count = 0
closed_count = 0

for i in range(min(sample_size, len(df))):
    url = df.iloc[i]['hyperlink']
    status = check_issue_status(url)
    
    if status == 'open':
        open_count += 1
        result = "OPEN"
    elif status == 'closed':
        closed_count += 1
        result = "CLOSED" 
    else:
        result = f"ERROR: {status}"
    
    print(f"  {i+1:2}/{sample_size}: {result} - {url}")

print(f"\nSample Results:")
print(f"Open: {open_count}/{sample_size} ({open_count/sample_size*100:.1f}%)")
print(f"Closed: {closed_count}/{sample_size} ({closed_count/sample_size*100:.1f}%)")
print(f"\nEstimated final counts for {len(df)} total issues:")
print(f"Open: ~{int(len(df) * open_count/sample_size)}")
print(f"Closed: ~{int(len(df) * closed_count/sample_size)}")