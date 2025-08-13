issue title: Inconsistent `.roast` usage
labels: Bug
comment count: 2
hyperlink: https://github.com/shopify/roast/issues/135
status: open
date opened: 2025-06-03
repo 30d_merge_rate: 13

====

description:
Currenty, we search up the tree for `.roast` when looking for `.roast/initializers`, but for everything else we use `$PWD/.roast`. This causes a problem where, if you have a parent `.roast/initializers` and you hit one of the other bits of code that uses `$PWD/.roast` (e.g. creating `$PWD/.roast/cache`), we ignore the parent `.roast/initializers`.

Example:

- I'm in `my-project/my-workflow`.
- There's already a `my-project/.roast/initializers/important-thing.rb`.
- I run `roast execute workflow.yml`, and it creates `my-project/my-workflow/.roast` so it can put a `cache` in there.
- Subsequent runs of `roast` no longer find `my-project/.roast/initializers`, as we stop at the first existing `.roast`, which was recently created for a `cache`. 

Potential Solutions:

- Standardize on the `.roast` search behaviour we have for initializers.
  - We'd stop doing `$PWD/.roast`, and just search up the tree like we do for `.roast/initializers` for any use of `.roast`.
- Standardize on `$PWD/.roast`.
  - This limits flexibility a little, and potentially litters the fs with `.roast`, I prefer the former option.

===

comment #1 by obie, 2025-06-06, 01:14:55
The first solution please:

Standardize on the .roast search behaviour we have for initializers.
We'd stop doing $PWD/.roast, and just search up the tree like we do for .roast/initializers for any use of .roast.

comment #2 by nfgrep, 2025-06-09, 16:39:16
Working on this over here: https://github.com/Shopify/roast/pull/134

Related to https://github.com/Shopify/roast/issues/20
