issue title: Parallelization output concatenated?
labels: Bug
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/109
status: open
date opened: 2025-05-30
repo 30d_merge_rate: 13

====

description:
from @styrmis 

> Ran into a possible bug, when we use the step parallelisation then all of the parallel steps will be under a single concatenated key under workflow.outputs, rather than having individual entries. For now we're switching back to serial execution so that we can interpolate the output of a number of steps into a later unifying analysis prompt

===
