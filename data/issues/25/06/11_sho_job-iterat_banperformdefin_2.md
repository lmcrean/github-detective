issue title: ban_perform_definition should be removed
labels: none
comment count: 0
hyperlink: https://github.com/shopify/job-iteration/issues/587
status: open
date opened: 2025-06-11
repo 30d_merge_rate: 9

====

description:
While I know the position of Sorbet regarding the use of `prepend` the `ban_perform_definition` protection is still excessive. It should be possible for a codebase to extend all jobs (also the ones using job-iteration) by `prepending` their implementation of `perform` or by redefining `perform`. When overloading a method it is simply the responsibility of the defining party to call `super`.

Maybe the issue can be solved by better documentation? ("how to overload perform() safely")

===
