issue title: [FEATURE] Support for policies on partitions
labels: enhancement
comment count: 0
hyperlink: https://github.com/stripe/pg-schema-diff/issues/209
status: open
date opened: 2025-05-19
repo 30d_merge_rate: 10

====

description:
### Describe the feature
Current implementation has support for RLS but it is not yet supported for partitions (https://github.com/stripe/pg-schema-diff/issues/111)


### Motivation
With the integration to the Supabase CLI, we see an uptick in usage and a few requests from customers to support this. With Migra's lack of support for partitions generally, and Supabase treating RLS a a first-class citizen, this has come up a few times and would unblock some users


===
