#!/usr/bin/env python3
"""Verify current status of all Round 1 nominated issues."""

import requests
import os
import json
from typing import Dict, Any, List, Tuple

def get_issue_status(owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
    """Get current status and recent activity for an issue."""
    
    token = os.getenv('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    issue_url = f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}'
    
    try:
        response = requests.get(issue_url, headers=headers)
        if response.status_code == 404:
            return {'error': 'Not found'}
        elif response.status_code == 403:
            return {'error': 'Access denied'}
        
        response.raise_for_status()
        issue_data = response.json()
        
        return {
            'state': issue_data['state'],
            'created_at': issue_data['created_at'][:10],
            'updated_at': issue_data['updated_at'][:10],
            'comments_count': issue_data['comments'],
            'labels': [label['name'] for label in issue_data.get('labels', [])],
            'assignee': issue_data['assignee']['login'] if issue_data['assignee'] else None,
            'title': issue_data['title'],
            'body_length': len(issue_data['body']) if issue_data['body'] else 0,
            'url': issue_data['html_url']
        }
    
    except requests.RequestException as e:
        return {'error': str(e)}

def check_recent_activity(owner: str, repo: str) -> Dict[str, Any]:
    """Check recent repository activity to gauge project health."""
    
    token = os.getenv('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    repo_url = f'https://api.github.com/repos/{owner}/{repo}'
    
    try:
        response = requests.get(repo_url, headers=headers)
        response.raise_for_status()
        repo_data = response.json()
        
        return {
            'last_push': repo_data['pushed_at'][:10],
            'open_issues': repo_data['open_issues_count'],
            'watchers': repo_data['watchers_count'],
            'stars': repo_data['stargazers_count']
        }
    
    except requests.RequestException:
        return {}

def main():
    """Verify all Round 1 nominated issues."""
    
    # All Round 1 nominated issues
    issues = [
        # mastercard-flow
        ("mastercard", "flow", 976, "Fix jline compatibility"),
        ("mastercard", "flow", 999, "Fix mermaid compatibility"), 
        ("mastercard", "flow", 975, "Fix mysterious CI failures"),
        ("mastercard", "flow", 896, "Package chains as DynamicContainers"),
        ("mastercard", "flow", 881, "Fix inter-line deadzone in hexdump view"),
        ("mastercard", "flow", 887, "Message view line numbers"),
        ("mastercard", "flow", 882, "Show raw data for unparseable actuals"),
        ("mastercard", "flow", 820, "Versions capture"),
        ("mastercard", "flow", 868, "Configuration capture"),
        ("mastercard", "flow", 816, "HttpReq - basic auth utility method"),
        
        # monzo-response (pre-2024, likely closed)
        ("monzo", "response", 262, "docker-compose build error at step 2/8"),
        ("monzo", "response", 125, "Add back Statuspage and PagerDuty integrations"),
        
        # nvidia-cccl
        ("NVIDIA", "cccl", 5488, "Port thrust::transform_if to cub::DeviceTransform::TransformIf"),
        ("NVIDIA", "cccl", 5397, "[BUG]: cub::ScatterToStripedFlagged overload calling wrong function"),
        ("NVIDIA", "cccl", 874, "[RFE] Use cudaLaunchKernel instead of <<<>>>"),
        ("NVIDIA", "cccl", 5327, "[BUG]: Potentially uninitialized/oob reads in DeviceMergeSort, DeviceReduceByKey, and DeviceScanByKey"),
        ("NVIDIA", "cccl", 4531, "Enumerate Thrust features to pull into cuda:: namespace"),
        ("NVIDIA", "cccl", 5124, "Several Thrust unit tests fail for negative numbers"),
        ("NVIDIA", "cccl", 1947, "[EPIC] Optimize thrust::transform for newer architectures"),
        ("NVIDIA", "cccl", 5367, "[BUG]: DeviceReduce gpu_to_gpu determinism fallbacks to run_to_run determinism"),
        ("NVIDIA", "cccl", 5444, "Figure out how to expose opt-in to calculate grid dimensions using 32-bit type"),
        ("NVIDIA", "cccl", 5438, "Add support for virtual shared memory to DispatchReduceByKey"),
        
        # nvidia-container-toolkit
        ("NVIDIA", "nvidia-container-toolkit", 1239, "Wrong CDI spec creates error \"Unresolvable CDI device\""),
        ("NVIDIA", "nvidia-container-toolkit", 1227, "Failed to initialize NVML after systemctl daemon-reload"),
        ("NVIDIA", "nvidia-container-toolkit", 1215, "CDI Spec Generation missing driver libraries"),
        ("NVIDIA", "nvidia-container-toolkit", 1225, "CLI flags should be ignored when unrecognised hook detected"),
        ("NVIDIA", "nvidia-container-toolkit", 1224, "Support IMEX_CHANNELS in jit-cdi mode"),
        ("NVIDIA", "nvidia-container-toolkit", 1222, "Container Toolkit messed up config.toml in GKE cluster with containerd 2.0"),
        ("NVIDIA", "nvidia-container-toolkit", 1218, "Disable chmod hook by default"),
        ("NVIDIA", "nvidia-container-toolkit", 1208, "invalid mitigation of cve-2025-23266"),
        ("NVIDIA", "nvidia-container-toolkit", 1203, "CDI behavior with NVIDIA GPU devices in Kubernetes"),
        ("NVIDIA", "nvidia-container-toolkit", 1199, "NVIDIA Container Toolkit fails with \"libnvidia-ml.so.1 not found\" on RTX 5070"),
        
        # stripe-react-stripe-js
        ("stripe", "react-stripe-js", 603, "[BUG]: The on method of useCheckout() function is omitted"),
        ("stripe", "react-stripe-js", 601, "[BUG]: ExpressCheckoutElement onClick doesn't work with latest stripe-js"),
        ("stripe", "react-stripe-js", 596, "[BUG]: Auto-focus in Country field dropdown after entering CVC on iOS Safari"),
        ("stripe", "react-stripe-js", 569, "[BUG]: React 19 global JSX namespace deprecation"),
        ("stripe", "react-stripe-js", 441, "[BUG]: input.__PrivateStripeElement-input ARIA hidden element must not be focusable"),
        ("stripe", "react-stripe-js", 592, "[BUG]: 3DS confirmation flow broken with ExpressCheckoutElement"),
        ("stripe", "react-stripe-js", 594, "[BUG]: Hydration Error with Stripe PaymentElement in Next.js"),
        ("stripe", "react-stripe-js", 581, "[BUG]: Express Checkout Element errors with token_already_used"),
        ("stripe", "react-stripe-js", 580, "[BUG]: Accessibility issues with Paypal button from Express Checkout element"),
        ("stripe", "react-stripe-js", 574, "[BUG]: Card Element onChange does not work consistently"),
        
        # stripe-go (we know 2092, 2093 are closed)
        ("stripe", "stripe-go", 2104, "Add Opentelemetry support"),
        ("stripe", "stripe-go", 2095, "TerminalReaderCollectInputsInputSelectionParams server-side validation issue"),
        ("stripe", "stripe-go", 2094, "charge.Invoice does not exist in Charges Retrieve API"),
        ("stripe", "stripe-go", 2087, "Seq2 and LastResponse"),
        ("stripe", "stripe-go", 2085, "V2 Accounts"),
        ("stripe", "stripe-go", 2075, "Missing PaymentIntent property in Invoice struct"),
        ("stripe", "stripe-go", 2072, "noncompliant not represented as a DisputeReason"),
        ("stripe", "stripe-go", 1937, "Add omitempty to JSON field tags on optional fields"),
        
        # stripe-node
        ("stripe", "stripe-node", 950, "StripeAuthenticationError when loading stripe secret from environment variables"),
        ("stripe", "stripe-node", 2382, "createPreview doesn't expand lines.data.price.tiers"),
        ("stripe", "stripe-node", 2368, "Auto-pagination error iterating over subscriptions when updating last record"),
        ("stripe", "stripe-node", 2332, "Requests not aborted within timeout"),
        ("stripe", "stripe-node", 2327, "TypeScript types are not accurate when expanding data"),
        ("stripe", "stripe-node", 2361, "Add support for accounts v2"),
        ("stripe", "stripe-node", 2357, "Export current api version string"),
        ("stripe", "stripe-node", 2351, "apiVersion set in new Stripe, but ephemeralKeys.create still asks for it"),
        ("stripe", "stripe-node", 2241, "Add AbortSignal support"),
        ("stripe", "stripe-node", 2211, "Default Node httpClient configuration does not get mocked by MSW")
    ]
    
    open_issues = []
    closed_issues = []
    error_issues = []
    
    print("ROUND 1 ISSUE VERIFICATION")
    print("=" * 80)
    
    repos_checked = set()
    
    for owner, repo, issue_num, title in issues:
        repo_key = f"{owner}/{repo}"
        
        # Check repo health first time we encounter it
        if repo_key not in repos_checked:
            print(f"\n[REPO HEALTH CHECK: {repo_key}]")
            health = check_recent_activity(owner, repo)
            if health:
                print(f"  Last push: {health['last_push']}")
                print(f"  Open issues: {health['open_issues']}")
                print(f"  Stars: {health['stars']}")
            else:
                print("  Could not fetch repo health data")
            repos_checked.add(repo_key)
        
        print(f"\nChecking {owner}/{repo} #{issue_num}: {title[:50]}...")
        
        status = get_issue_status(owner, repo, issue_num)
        
        if 'error' in status:
            error_issues.append((owner, repo, issue_num, title, status['error']))
            print(f"  ERROR: {status['error']}")
        elif status['state'] == 'open':
            open_issues.append((owner, repo, issue_num, title, status))
            print(f"  OPEN - Updated: {status['updated_at']} - Comments: {status['comments_count']}")
        else:
            closed_issues.append((owner, repo, issue_num, title, status))
            print(f"  CLOSED - Updated: {status['updated_at']}")
    
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"Open issues: {len(open_issues)}")
    print(f"Closed issues: {len(closed_issues)}")
    print(f"Error issues: {len(error_issues)}")
    
    print(f"\n[TOP OPEN ISSUES BY RECENT ACTIVITY]")
    # Sort open issues by recent activity
    open_issues.sort(key=lambda x: x[4]['updated_at'], reverse=True)
    
    for i, (owner, repo, issue_num, title, status) in enumerate(open_issues[:15]):
        print(f"{i+1:2}. {owner}/{repo} #{issue_num}")
        print(f"    Title: {title}")
        print(f"    Updated: {status['updated_at']} | Comments: {status['comments_count']} | Labels: {status['labels']}")
        print(f"    URL: {status['url']}")
        print()

if __name__ == "__main__":
    main()