issue title: Circular dependencie in test
labels: Bug
comment count: 2
hyperlink: https://github.com/shopify/roast/issues/128
status: open
date opened: 2025-06-02
repo 30d_merge_rate: 13

====

description:
There's a circular dependency when running test

```
/opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: loading in progress, circular require considered harmful - /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  '<main>'
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  'select'
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:21:in  'block in <main>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/test/roast/cli_test.rb:3:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/test/test_helper.rb:17:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/lib/roast.rb:12:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb:8:in  '<top (required)>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb:9:in  '<module:CLI>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb:29:in  '<module:UI>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:4:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'

/opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: loading in progress, circular require considered harmful - /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  '<main>'
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  'select'
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:21:in  'block in <main>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/test/roast/cli_test.rb:3:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/test/test_helper.rb:17:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/lib/roast.rb:12:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb:8:in  '<top (required)>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb:9:in  '<module:CLI>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb:29:in  '<module:UI>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:6:in  '<top (required)>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:7:in  '<module:CLI>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:8:in  '<module:UI>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:23:in  '<module:Spinner>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/color.rb:4:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'

/opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: loading in progress, circular require considered harmful - /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  '<main>'
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  'select'
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:21:in  'block in <main>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/test/roast/cli_test.rb:3:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/test/test_helper.rb:17:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/lib/roast.rb:12:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb:8:in  '<top (required)>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb:9:in  '<module:CLI>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb:29:in  '<module:UI>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:6:in  '<top (required)>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:7:in  '<module:CLI>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:8:in  '<module:UI>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/spinner.rb:23:in  '<module:Spinner>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/color.rb:6:in  '<top (required)>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/color.rb:7:in  '<module:CLI>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/color.rb:8:in  '<module:UI>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/color.rb:33:in  '<class:Color>'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/color.rb:33:in  'new'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/color.rb:29:in  'initialize'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/ansi.rb:4:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'

/opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82: warning: loading in progress, circular require considered harmful - /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  '<main>'
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:6:in  'select'
        from /opt/rubies/3.4.2/lib/ruby/gems/3.4.0/gems/rake-13.2.1/lib/rake/rake_test_loader.rb:21:in  'block in <main>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/test/roast/cli_test.rb:3:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/test/test_helper.rb:17:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /roast/lib/roast.rb:12:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui.rb:414:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
        from /Users/ericproulx/.gem/ruby/3.4.2/gems/cli-ui-2.3.1/lib/cli/ui/stdout_router.rb:4:in  '<top (required)>'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'block (2 levels) in replace_require'
        from /opt/rubies/3.4.2/lib/ruby/3.4.0/bundled_gems.rb:82:in  'require'
```

===

comment #1 by ericproulx, 2025-06-02, 14:24:58
Related to https://github.com/Shopify/cli-ui/issues/321

comment #2 by obie, 2025-06-06, 01:12:32
Related to #116 
