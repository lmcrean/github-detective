issue title: [FEATURE] option to write out migration files
labels: enhancement
comment count: 1
hyperlink: https://github.com/stripe/pg-schema-diff/issues/221
status: open
date opened: 2025-07-26
repo 30d_merge_rate: 10

====

description:
### Describe the feature
Add an option to write out migration `.sql` files in raw sql. This way incremental migration files can be stored to go through/review the migration changes/history and maybe use them with other tools like `sqlc`.

I already tested it with via shell script on a project with `atlas` migration files.

Schema files are under `./db/schemas` and migration files under `./db/migrations`. For `apply` I set `--to-dir` to the migration files dir and for `plan` I set `--to-dir` to the schemas dir.

I was able to continue the incremental migrations and apply them to a test database with `pg-schema-diff` successfully. `sqlc` was also able to pickup from there.

Minor things missing from the Atlas workflow, that not necessarily need to be adressed in this context:
- Write out the migration file hashes to prevent recreating the last migration file, if nothing has changed but the latest migrations are not applied yet e.g.. The hashes are also used to verify that no migration file has been changed manually before executing any command.
- An option to allow all hazards at once and only show the confirm prompt.

The proposal would be to provide a flag like `--out-dir` to write out the result in raw sql. A bonus would be to also write out the hash to a `.sum` file which can be used to validate the migration files before executing commands.

<details>

<summary><italic>I created this script so far</italic></summary>

```sh
#!/bin/bash

set -e

if [ ! -f ".env" ]; then
    echo "Error: .env file not found!"
    exit 1
fi

set -a
source .env
set +a

if [ $# -eq 0 ]; then
    echo "Runs pg-schema-diff <command> with arguments based on .env"
    echo ""
    echo "Usage:"
    echo "  $0 <command> [additional_args...]"
    echo ""
    echo "Available commands:"
    echo "  apply    Migrate your database to the match the inputted schema (apply the schema to the database)"
    echo "  plan     Generate the diff between two databases and the SQL to get from one to the other"
    exit 1
fi

COMMAND=$1
shift

POSTGRES_DNS=postgres://${DB_USER}:${DB_PASS}@${DB_HOST}/${DB_NAME}

SCHEMAS_DIR=./db/schemas
MIGRATIONS_DIR=./db/migrations

ALLOWED_HAZARDS=ACQUIRES_ACCESS_EXCLUSIVE_LOCK,\
ACQUIRES_SHARE_LOCK,\
ACQUIRES_SHARE_ROW_EXCLUSIVE_LOCK,\
CORRECTNESS,\
DELETES_DATA,\
HAS_UNTRACKABLE_DEPENDENCIES,\
INDEX_BUILD,\
INDEX_DROPPED,\
IMPACTS_DATABASE_PERFORMANCE,\
IS_USER_GENERATED,\
UPGRADING_EXTENSION_VERSION,\
AUTHZ_UPDATE

case $COMMAND in
    "apply")
        pg-schema-diff apply --allow-hazards $ALLOWED_HAZARDS --from-dsn "$POSTGRES_DNS" --to-dir $MIGRATIONS_DIR "$@"
        ;;
    "plan")
        RESULT_FILE=$(date +%Y%m%d%H%M%S).sql
        if output=$(
            pg-schema-diff plan --output-format json --from-dsn "$POSTGRES_DNS" --to-dir $SCHEMAS_DIR "$@" 2>&1
        ); then
            if [ -z "$output" ]; then
                echo "pg-schema-diff output is empty"
                exit 1
            fi

            if output=$(
                echo "$output" | jq -r '
                if (.statements | not) then
                    "Schema matches expected. No plan generated\n" | halt_error(5)
                else
                    empty
                end,

                .statements.[]
                | if .hazards then
                  (.hazards | select(. != null) | map("-- " + .type + ": " + .message) | join("\n")) + "\n"
                else
                  ""
                end
                + "\(.ddl);\n"
                ' 2>&1
            ); then
                echo "$output" | tee "$MIGRATIONS_DIR/$RESULT_FILE"
            else
                exit_code=$?
                echo "$output"
                if [ $exit_code -ne 5 ]; then
                    exit $exit_code
                else
                    exit 0
                fi
            fi
        else
            echo "$output"
            exit 1
        fi
        echo "Added new migration $RESULT_FILE"
        ;;
    *)
        echo "Error: Unknown command '$COMMAND'"
        echo "Available commands: apply, plan"
        exit 1
        ;;
esac
```

</details>


### Motivation
In general I like the diff concept for incremental migrations I think its nice to have options with this approach.

In my specific case I want to replace Atlas on a smaller project that needs function and trigger migrations, which are behind a paywall in Atlas.

===

comment #1 by perrygeo, 2025-07-28, 18:23:55
Just a +1, it would greatly help implement the workflow I'm trying to achieve:

1. Edit `schemas/app.sql`
2. Run something _like_ `pg-schema-diff plan ...` but instead of writing to stdout, it would write a new sql file to a migrations directory, with the explanatory text as sql comments. 
4. Confirm that running both the `app.sql` and the `migrations/*.sql` produce an identical schema.
5. Nothing else, I'm looking for a workflow to *create* migrations, not apply them.

I've tried building this workflow on top of [tusker](https://github.com/bikeshedder/tusker) but would love a non-python solution. This CLI & library comes pretty close but it lacks migration file output and has superfluous apply functionality that I don't need, but otherwise does a great job.

My current implementation of the above workflow is to run `plan`, manually copy the output to new file and edit it to be valid sql. Works ok, but sql file output would unlock this as a viable workflow without hacks. 

An MVP of this functionality could be as simple as a `--sql-output` flag or similar that alters the stdout of the existing `plan` command to be valid sql. Then a user could do something like

```
pg-schema-diff plan --sql-output ... > migrations/002-add-new-table.sql
```

By giving the user full control over the sql file naming, that saves this library from having to make decisions about naming conventions that often come baked into a migration library (there's equally valid reasons to prefix with serial ints, timestamps, or hashes)
