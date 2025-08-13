issue title: Many  method redefined warnings during tests from raix
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/120
status: open
date opened: 2025-05-31
repo 30d_merge_rate: 13

====

description:
I'm seeing a ton of warnings when running `rake test`:

```
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: method redefined; discarding old search_for_file
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: previous definition of search_for_file was here
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: method redefined; discarding old read_file
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: previous definition of read_file was here
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: method redefined; discarding old grep
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: previous definition of grep was here
./Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: method redefined; discarding old search_for_file
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: previous definition of search_for_file was here
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: method redefined; discarding old read_file
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: previous definition of read_file was here
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: method redefined; discarding old grep
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: previous definition of grep was here
```

The smallest command I've foudn to run this is: `bundle exec rake test TEST=test/roast/helpers/prompt_loader_test.rb`:

```
# Running:

../Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: method redefined; discarding old search_for_file
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: previous definition of search_for_file was here
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: method redefined; discarding old read_file
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: previous definition of read_file was here
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: method redefined; discarding old grep
/Users/josh.nichols/.local/share/mise/installs/ruby/3.4.2/lib/ruby/gems/3.4.0/gems/raix-0.8.6/lib/raix/function_dispatch.rb:67: warning: previous definition of grep was here
..

Finished in 0.002224s, 1798.5612 runs/s, 2248.2015 assertions/s.

4 runs, 5 assertions, 0 failures, 0 errors, 0 skips
```

Commenting either tests in the file go away. I'm not sure if this is a raix issue or something in roast, so starting here.



===
