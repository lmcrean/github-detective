issue title: Tapioca v0.17.5 doesn't handle typing of output of custom GraphQL Scalars correctly
labels: bug, help-wanted
comment count: 1
hyperlink: https://github.com/shopify/tapioca/issues/2337
status: open
date opened: 2025-06-26
repo 30d_merge_rate: 12

====

description:
Just noticed what I believe to be a bug when updating to the latest version of the Gem in a project that also uses the [`graphql-ruby`](https://github.com/rmosolgo/graphql-ruby) gem and where we have some custom scalar types. While the latest version does a great job of locating the correct type, I'm finding that for input arguments that reference the scalar types, the generated methods in the rbi are always nullable.

I've traced the reason down to [this line](https://github.com/Shopify/tapioca/blob/bfd05549107ddfc2c8efb232e89653221f7f032b/lib/tapioca/dsl/helpers/graphql_type_helper.rb#L66), and the underlying issue is that the `coerce_result` of any scalar type has to handle the `nil` case, but in cases where we have a required input argument the value of the argument will never be null. So the type should only have a `T.nilable(...)` if the input argument is not required. 

===

comment #1 by joeytepp, 2025-06-26, 14:49:31
Tagging @nicoco007 and @paracycle for visibility since it looks like you added this originally in https://github.com/Shopify/tapioca/pull/1659
