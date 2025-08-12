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



# expected output

```
data/orgs/shopify/shopify_repos_filter1_{{datehere}}.csv
data/orgs/shopify/shopify_repos_filter2_{{datehere}}.csv
data/orgs/shopify/shopify_repos_filter3_{{datehere}}.csv
data/orgs/stripe/stripe_repos_filter1_{{datehere}}.csv
data/orgs/stripe/stripe_repos_filter2_{{datehere}}.csv
data/orgs/stripe/stripe_repos_filter3_{{datehere}}.csv
```