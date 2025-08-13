issue title: Noisy output when running tests :(
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/297
status: open
date opened: 2025-06-24
repo 30d_merge_rate: 13

====

description:
When running tests, there's a lot of noisy output.  This is caused by the usage of `$stderr.puts` inside classes.

There are plenty of ways to fix that:

- Surround function calls that uses `$stderr.puts` with a `capture_io`. The last comes with `minitest`
- Create a dependency injections that we could manage `$stderr.puts`
- Stubbing `$stderr` for tests
- ...

I like the dependency injection. Any other suggestions ?

===
