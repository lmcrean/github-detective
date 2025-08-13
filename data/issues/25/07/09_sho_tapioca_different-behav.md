issue title: Different behaviour between CLI and add-on
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/tapioca/issues/2349
status: open
date opened: 2025-07-09
repo 30d_merge_rate: 12

====

description:
When we moved to RBS comment annotations, the `Tapioca::Dsl::Compiler` base class lost the `extend T::Generic`. This is a breaking change because most custom compilers out there just use `type_member` directly without extending `T::Generic` themselves. That ends up not being an issue thanks to the Spoom rewriting, which adds back those extends.

Somehow, this does not happen for the add-on. It's not clear to me why this is the case yet, but we can at least fix the behaviour temporarily by extending `T::Generic` only in the add-on while we investigate why the behaviour would be different between the two.

===
