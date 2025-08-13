issue title: Cleanup child processes on SIGINT
labels: Bug, deficiency
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/340
status: open
date opened: 2025-07-30
repo 30d_merge_rate: 13

====

description:
If you `ctrl+c` roast while its running a long running process (e.g. claude swarm), it doesn't die, it hangs. You can ctrl+c again and it'll kill roast, but leave claude-swarm behind:

One ctrl+c:
```
Executing: do thing (Resource type: none)
^C

Caught CTRL-C! Printing before exiting:
[]
```

After the second:
```
Executing: do thing (Resource type: none)
^C

Caught CTRL-C! Printing before exiting:
[]
^C

Caught CTRL-C! Printing before exiting:
[]
```

This is likely because roast just trying to exit(1) without propagating any signals on SIGINT:
https://github.com/Shopify/roast/pull/339


===
