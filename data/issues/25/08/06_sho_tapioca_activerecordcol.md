issue title: ActiveRecordColumnTypes - Create a 'Mixed' option
labels: enhancement
comment count: 1
hyperlink: https://github.com/shopify/tapioca/issues/2369
status: open
date opened: 2025-08-06
repo 30d_merge_rate: 12

====

description:
Referencing [this page](https://github.com/Shopify/tapioca/blob/main/manual/compiler_activerecordcolumns.md).

I'm wondering if we could create a new mixed option that is between nilable and untyped. If the only reason we mark columns as 'untyped' is non-nil fields might be nilable before save, there's no actual reason that truly nilable columns should be untyped. 

I'm proposing a `ActiveRecordColumnTypes` called `mixed`:
- Non-nil fields continue to be untyped
- Nilable fields get typed consistently with `persisted` mode.


Another possible name might be `untyped-only`

===

comment #1 by Morriar, 2025-08-07, 18:30:19
I think it's a good step between `untyped` and `nilable` 👍

Do you want to take a stab at it?
