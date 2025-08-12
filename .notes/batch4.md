# process Stripe and Shopify

For each Org

1. delete those with most recently pushed before March 2025
2. return a new list with _filter1_{{date}} appended to the .csv and same/appended column count
3. define scripts/merged_prs_30d/... .py files
4. run files to get output which should...
5. add merged_prs_30d column to new csv....
6. return a new list with _filter2_{{date}} appended to the .csv and same/appended column count
7. filter to top 50%
8. return a new list with _filter3_{{date}} appended to the .csv and same/appended column count

# script architecture

```
scripts/
├── org-research/                     # Organization data collection (moved here)
│   ├── collect_org_repos.py         # Existing collector
│   └── models.py                    # Data models
│
├── merged_prs_30d/                  # PR metrics collection
│   ├── __init__.py
│   ├── fetch_merged_prs.py         # Fetch merged PRs for last 30 days
│   ├── add_pr_column.py            # Add merged_prs_30d column to CSV
│   └── batch_processor.py          # Process multiple orgs in batch
│
├── filters/                         # Data filtering scripts
│   ├── filter_by_date.py          # Filter1: Remove repos pushed before March 2025
│   ├── filter_by_pr_activity.py   # Filter2: After adding merged_prs_30d
│   └── filter_top_percentile.py   # Filter3: Keep top 50%
│
└── orchestrator.py                 # Main script to run full pipeline
```

# expected output

```
data/orgs/shopify/shopify_repos_filter1_{{datehere}}.csv
data/orgs/shopify/shopify_repos_filter2_{{datehere}}.csv
data/orgs/shopify/shopify_repos_filter3_{{datehere}}.csv
data/orgs/stripe/stripe_repos_filter1_{{datehere}}.csv
data/orgs/stripe/stripe_repos_filter2_{{datehere}}.csv
data/orgs/stripe/stripe_repos_filter3_{{datehere}}.csv
```