issue title: Feature request: DSL compiler for RuboCop's `def_node_matcher`
labels: help-wanted
comment count: 1
hyperlink: https://github.com/shopify/tapioca/issues/2321
status: open
date opened: 2025-06-13
repo 30d_merge_rate: 12

====

description:
This code:

```ruby
class MyCop < ::RuboCop::Cop::Base
  def_node_matcher :my_pattern?, <<~PATTERN
    (send _ :some_method ...)
  PATTERN
end
```

Should produce this RBI:

```rb
class MyCop < ::RuboCop::Cop::Base
  sig do
    params(
      node: RuboCop::AST::Node,
      block: T.proc.params(*captures: T.untyped).void,
    ).returns(T::Boolean)
  end
  def my_pattern?; end
end
```

Typing the block would be pretty challenging... we'd need to statically analyze the NodePattern, to figure out how many matches where will be. I just left it as an untyped varargs.

===

comment #1 by dduugg, 2025-06-30, 19:43:31
I created a somewhat hacky one for Homebrew that you may find helpful as a starting point: https://github.com/Homebrew/brew/blob/main/Library/Homebrew/sorbet/tapioca/compilers/rubocop.rb
