issue title: [QUESTION] Can I compare 2 schemas named differently?
labels: none
comment count: 0
hyperlink: https://github.com/stripe/pg-schema-diff/issues/210
status: open
date opened: 2025-05-20
repo 30d_merge_rate: 10

====

description:
As far as I've seen, you can only compare full databases. What I would want to do is comparing 2 schemas with different names.

For instance, say we have **schemaA** and **schemaB**, and in the **schemaA** we have a table `schemaA.test` that doesn't exist in **schemaB**.
Calling `Generate()` would return something like: `CREATE TABLE schemaB.test (...);`

Is this possible currently? And if not, is this something you have in mind for an eventually coming release?

Thanks! 👋 

===
