issue title: [BUG] Wrong statement when using `generated always as`
labels: bug
comment count: 0
hyperlink: https://github.com/stripe/pg-schema-diff/issues/212
status: open
date opened: 2025-06-10
repo 30d_merge_rate: 10

====

description:
### Describe the bug

When I `pg-schema-diff apply` after adding this column:
```
search_vector tsvector generated always as (
  to_tsvector('simple', title || ' ' || coalesce(artist, ''))
) stored
```

I get the following error:
```
Error: generating plan: validating migration plan: running migration plan: executing migration statement: {ALTER TABLE "public"."tabs" ADD COLUMN "search_vector" tsvector DEFAULT to_tsvector('simple'::regconfig, ((title || ' '::text) || COALESCE(artist, ''::text))) 3s 3s []}: ERROR: cannot use column reference in DEFAULT expression (SQLSTATE 0A000) 
diff.Plan{
    Statements: {
        {
            DDL:         "ALTER TABLE \"public\".\"tabs\" ADD COLUMN \"search_vector\" tsvector DEFAULT to_tsvector('simple'::regconfig, ((title || ' '::text) || COALESCE(artist, ''::text)))",
            Timeout:     3000000000,
            LockTimeout: 3000000000,
            Hazards:     nil,
        },
    },
    CurrentSchemaHash: "22b8e78772d29e38",
}
```
It seems that pg-schema-diff is changing the `...generated always as ...` to `...default...`


### Expected behavior

Use `generated always as`.


### Context 

pg-schema-diff version: Version=v0.9.0
Postgres version: 17
pg-schema-diff apply --dsn url --schema-dir db/



===
