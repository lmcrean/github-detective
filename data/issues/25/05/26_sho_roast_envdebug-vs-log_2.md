issue title: ENV['DEBUG'] vs Logger's log_level
labels: none
comment count: 1
hyperlink: https://github.com/shopify/roast/issues/81
status: open
date opened: 2025-05-26
repo 30d_merge_rate: 13

====

description:
I've seen some `if ENV['DEBUG']` for not calling `Roast::Helpers::Logger.debug` and since its not meaningful to test it, our code coverage is lower than it should be. I think we could benefit from calling the `block` of [debug](https://rubyapi.org/o/logger#method-i-debug) and all other log levels like `error`, `info` etc ... instead of passing a regular string.

The main advantage is that the block is not evaluated unless the log_level permits the entry. For instance, if the `log_level` is set to `INFO` which is the default, `Roast::Helpers::Logger.debug ` call will never execute the block since `DEBUG` a lower than `info`. Here are the levels from lowest to highest 

```
DEBUG < INFO < WARN < ERROR < FATAL < UNKNOWN.
```

That way, we could remove all the `if ENV['DEBUG']` in front of the calls and code coverage would increase naturally. 

Here are few thing also related to logging and improvements:
- we might want to set `ROAST_LOG_LEVEL` to `DEBUG` if `ENV['DEBUG']` is set to make sure we don't loose the actual way of debugging.
- we should set `log_level` to `fatal` in test for not polluting CI or even local output.














===

comment #1 by technicalpickles, 2025-05-31, 19:27:39
I was looking for issues around `ENV['DEBUG']` on the repo, and landed here. I have been trying to set DEBUG=1 but don't see it having an effect.

Agree that it would be better to use log levels, perhaps with an ENV-specific value to set it?
