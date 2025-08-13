issue title: loading in progress, circular require considered harmful
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/116
status: open
date opened: 2025-05-31
repo 30d_merge_rate: 13

====

description:
Running the tests (`rake test`) spits out several screens full of warnings, starting with:

```
❯ bundle exec rake test
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: loading in progress, circular require considered harmful - /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui.rb
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  '<main>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  'select'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:21:in  'block in <main>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/josh.nichols/workspace/roast/test/roast/cli_test.rb:3:in  '<top (required)>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/josh.nichols/workspace/roast/test/test_helper.rb:17:in  '<top (required)>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/josh.nichols/workspace/roast/lib/roast.rb:4:in  '<top (required)>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui.rb:8:in  '<top (required)>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui.rb:9:in  '<module:CLI>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui.rb:29:in  '<module:UI>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:4:in  '<top (required)>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'

/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: loading in progress, circular require considered harmful - /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui.rb
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  '<main>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  'select'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:21:in  'block in <main>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/josh.nichols/workspace/roast/test/roast/cli_test.rb:3:in  '<top (required)>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/josh.nichols/workspace/roast/test/test_helper.rb:17:in  '<top (required)>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/josh.nichols/workspace/roast/lib/roast.rb:4:in  '<top (required)>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui.rb:8:in  '<top (required)>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui.rb:9:in  '<module:CLI>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui.rb:29:in  '<module:UI>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:6:in  '<top (required)>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:7:in  '<module:CLI>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:8:in  '<module:UI>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:23:in  '<module:Spinner>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/cli-ui-2.3.1/lib/cli/ui/color.rb:4:in  '<top (required)>'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
```

It repeats twice. It also happens during CI, ie https://github.com/Shopify/roast/actions/runs/15354873023/job/43211603567

===
