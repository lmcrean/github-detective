issue title: [BUG] Constraint triggers generate invalid plans
labels: bug
comment count: 1
hyperlink: https://github.com/stripe/pg-schema-diff/issues/213
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 10

====

description:
### Describe the bug
Apologies if this is expected and should instead be a feature request instead. I can move this if that makes more sense.

I am using the library to automatically generate migrations programmatically. The schema makes use of constraint triggers which, when changed, result in an invalid plan that tries to use `CREATE OR REPLACE CONSTRAINT TRIGGER` which is not supported in Postgres. 

I am currently working around this by ignoring the tool's validation and post-processing the plan to drop & re-create the trigger instead.

### Expected behavior
A valid plan can be generated when constraint triggers are modified whether this is via a pair of `DROP TRIGGER IF EXISTS...` & `CREATE CONSTRAINT TRIGGER...` or other means.

### To Reproduce
1. Start a postgres instance (`docker run --name test-pg -e POSTGRES_PASSWORD=postgres -v "$(pwd)/data:/var/lib/postgresql/data" -p 5432:5432 -d postgres`)
2. `mkdir initial_schema after_schema`
3. `touch initial_schema/schema.sql after_schema/schemal.sql`
4. Add the following to `initial_schema/schema.sql`. 

    ```sql
    CREATE FUNCTION test_fn() RETURNS trigger
        LANGUAGE plpgsql
        AS $_$
    DECLARE
        msg TEXT := TG_ARGV[0];
    BEGIN
        RAISE NOTICE '%', msg;
        RETURN NEW;
    END;
    $_$;

    CREATE TABLE foobar (id int);

    CREATE CONSTRAINT TRIGGER test_trigger
      AFTER INSERT OR UPDATE ON foobar DEFERRABLE INITIALLY DEFERRED
      FOR EACH ROW EXECUTE FUNCTION test_fn('hello');
    ```
5. Add the following to `after_schema/schemal.sql` (note, just the parameter changed)
  
    ```sql
    CREATE FUNCTION test_fn() RETURNS trigger
        LANGUAGE plpgsql
        AS $_$
    DECLARE
        msg TEXT := TG_ARGV[0];
    BEGIN
        RAISE NOTICE '%', msg;
        RETURN NEW;
    END;
    $_$;

    CREATE TABLE foobar (id int);

    CREATE CONSTRAINT TRIGGER trigger_1
      AFTER INSERT OR UPDATE ON foobar DEFERRABLE INITIALLY DEFERRED
      FOR EACH ROW EXECUTE FUNCTION test_fn('HI');
    ```
6. Apply the initial schema with `pg-schema-diff apply --dsn "postgres://postgres:test@localhost:5432/postgres" --schema-dir before_schema --allow-hazards HAS_UNTRACKABLE_DEPENDENCIES` (click "Yes" when promoted)
7. Generate a plan to migrate to the "after" schema with `pg-schema-diff plan --dsn "postgres://postgres:test@localhost:5432/postgres" --schema-dir after_schema`

This generates the following output:

```
Error: generating plan: validating migration plan: running migration plan: executing migration statement: {CREATE OR REPLACE CONSTRAINT TRIGGER trigger_1 AFTER INSERT OR UPDATE ON public.foobar DEFERRABLE INITIALLY DEFERRED FOR EACH ROW EXECUTE FUNCTION test_fn('HI') 3s 3s []}: ERROR: CREATE OR REPLACE CONSTRAINT TRIGGER is not supported (SQLSTATE 0A000)
diff.Plan{
    Statements: {
        {
            DDL:         "CREATE OR REPLACE CONSTRAINT TRIGGER trigger_1 AFTER INSERT OR UPDATE ON public.foobar DEFERRABLE INITIALLY DEFERRED FOR EACH ROW EXECUTE FUNCTION test_fn('HI')",
            Timeout:     3000000000,
            LockTimeout: 3000000000,
            Hazards:     nil,
        },
    },
    CurrentSchemaHash: "b9bb8afe1d961d34",
}
```


### Context 
pg-schema-diff version: v0.9.0
pg-schema-diff usage: CLI & LIBRARY 
Postgres version: 17



===

comment #1 by bplunkett-stripe, 2025-07-20, 22:36:24
This should be fixed by #217. I cut a new release [0.9.1](https://github.com/stripe/pg-schema-diff/releases/tag/v0.9.1) that contains the fix. Let me know if that works for you!
