issue title: Named shell steps appear in output and notification payload as their command, not name.
labels: deficiency
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/336
status: open
date opened: 2025-07-23
repo 30d_merge_rate: 13

====

description:
A step like `- clear_files: $(rm -rf some/file)` does not appear in the run output, or the ActiveSupport::Notification payload as "clear_files", instead the whole command is its "name":
```
% bundle exec roast execute ci-coverage
🔥🔥🔥 Everyone loves a good roast 🔥🔥🔥

Starting workflow...
...
Executing: $(rm -rf some/file) (Resource type: none)
```

===
