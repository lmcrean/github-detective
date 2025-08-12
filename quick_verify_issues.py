import pandas as pd
import requests
import re
import os
import time
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('API_GITHUB_TOKEN')
headers = {'Authorization': f'token {token}'} if token else {}

def extract_issue_info(hyperlink):
    pattern = r'https://github\.com/([^/]+)/([^/]+)/issues/(\d+)'
    match = re.match(pattern, hyperlink)
    if match:
        return match.group(1), match.group(2), match.group(3)
    return None, None, None

def check_issue_status(owner, repo, issue_number):
    url = f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('state', 'unknown')
        else:
            return 'error'
    except:
        return 'error'

# Load data
input_file = "C:\\Projects\\github-library\\data\\repos\\shopify_stripe_filter2.csv"
output_file = "C:\\Projects\\github-library\\data\\repos\\shopify_stripe_filter3.csv"

df = pd.read_csv(input_file)
print(f"Processing {len(df)} issues...")

open_issues = []
batch_size = 50
processed = 0

for i, row in df.iterrows():
    processed += 1
    hyperlink = row['hyperlink']
    
    owner, repo, issue_number = extract_issue_info(hyperlink)
    if not owner:
        continue
    
    status = check_issue_status(owner, repo, issue_number)
    
    if status == 'open':
        open_issues.append(row)
        result = "OPEN"
    else:
        result = "CLOSED/ERROR"
    
    if processed % 10 == 0:
        print(f"Progress: {processed}/{len(df)} - Open issues found: {len(open_issues)} - Current: {result}")
        
        # Save intermediate results every 50 issues
        if processed % batch_size == 0:
            temp_df = pd.DataFrame(open_issues)
            temp_df.to_csv(output_file, index=False)
            print(f"  Saved intermediate results: {len(open_issues)} open issues")
    
    # Short pause to avoid overwhelming API
    if processed % 5 == 0:
        time.sleep(0.5)

# Final save
if open_issues:
    final_df = pd.DataFrame(open_issues)
    final_df.to_csv(output_file, index=False)
    print(f"\nCOMPLETE: Saved {len(open_issues)} open issues to {output_file}")
    print(f"Open rate: {len(open_issues)/len(df)*100:.1f}%")
else:
    print("No open issues found!")
    empty_df = pd.DataFrame(columns=df.columns)
    empty_df.to_csv(output_file, index=False)