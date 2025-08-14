# Top 5 Most Viable SWE Issues Report

**Analysis Date:** 2025-08-14  
**Total Issues Reviewed:** 85+ issues in `.notes/issues/`  
**Evaluation Criteria:** Impact, Complexity, Clarity, Maintainer Engagement, Community Interest, Implementation Feasibility

## Executive Summary

This report ranks the top 5 most viable software engineering issues to tackle in the pg-schema-diff project. These issues were selected based on their potential impact, technical feasibility, and community value. The ranking prioritizes critical bugs and high-demand features with clear implementation paths.

---

## 🏆 Top 5 Ranked Issues

### 1. Issue #212: [BUG] Wrong statement when using `generated always as` ⭐⭐⭐⭐⭐

**Priority:** CRITICAL  
**Status:** Open Bug  
**Created:** 2025-06-10  
**Labels:** bug  
**Link:** https://github.com/stripe/pg-schema-diff/issues/212

#### Problem Description
PostgreSQL `GENERATED ALWAYS AS` columns are incorrectly treated as `DEFAULT` columns, causing migration failures with column reference errors.

**Error Example:**
```sql
-- Desired: GENERATED ALWAYS AS (expression) STORED
-- Generated: DEFAULT expression  -- ❌ This fails
ERROR: cannot use column reference in DEFAULT expression
```

#### Impact Assessment
- **HIGH** - Blocks users from using PostgreSQL generated columns
- Core functionality broken for an important PostgreSQL feature
- Causes migration failures that can leave databases in inconsistent states

#### Technical Complexity
- **MEDIUM** - Root cause clearly identified in CLAUDE.md
- Well-documented fix strategy available
- Specific files to modify: `internal/queries/queries.sql`, `internal/schema/schema.go`, `pkg/diff/sql_generator.go`

#### Implementation Guidance
1. Modify `GetColumnsForTable` query to check `pg_attribute.attgenerated` column
2. Add `IsGenerated` and `GenerationExpression` fields to `Column` struct  
3. Update `buildColumnDefinition` to emit `GENERATED ALWAYS AS ... STORED` syntax

#### Effort Estimate: 2-3 days

---

### 2. Issue #221: [FEATURE] Option to write out migration files ⭐⭐⭐⭐⭐

**Priority:** HIGH  
**Status:** Open Enhancement  
**Created:** 2025-07-26  
**Labels:** enhancement  
**Comments:** 1 with detailed user feedback  
**Link:** https://github.com/stripe/pg-schema-diff/issues/221

#### Problem Description
Users want to output migration plans as raw SQL files for version control, review processes, and integration with other tools like sqlc.

**User Request:**
```bash
# Desired functionality
pg-schema-diff plan --sql-output ... > migrations/002-add-new-table.sql
```

#### Impact Assessment
- **HIGH** - Enables CI/CD workflows and migration file management
- Multiple users requesting this feature
- Integrates with existing toolchains (Atlas, sqlc)
- Supports code review processes for schema changes

#### Technical Complexity
- **MEDIUM** - Clear requirements with user-provided implementation examples
- Add `--sql-output` or `--out-dir` flag to CLI
- Modify output formatting to generate valid SQL with comments
- Consider hash file generation for migration tracking

#### Implementation Guidance
1. Add new CLI flags for SQL output mode
2. Create SQL formatter for plan output
3. Add migration file naming and organization options
4. Optional: Add hash/checksum file generation

#### Community Value
Strong engagement with detailed shell script examples and workflow descriptions from users.

#### Effort Estimate: 3-4 days

---

### 3. Issue #179: [FEATURE] Support switching between non-coercible types via drop/add ⭐⭐⭐⭐

**Priority:** MEDIUM-HIGH  
**Status:** Open Enhancement  
**Created:** 2024-11-08  
**Labels:** enhancement, good first issue  
**Comments:** 2 with maintainer engagement  
**Link:** https://github.com/stripe/pg-schema-diff/issues/179

#### Problem Description
When column types cannot be cast (e.g., `integer` to `timestamptz`), the tool should generate `DROP COLUMN` followed by `ADD COLUMN` instead of failing with cast errors.

**Current Behavior:**
```sql
-- Fails with: ERROR: cannot cast type integer to timestamp with time zone
ALTER TABLE "table" ALTER COLUMN "col" SET DATA TYPE timestamptz using "col"::timestamptz
```

**Expected Behavior:**
```sql
ALTER TABLE "table" DROP COLUMN "col";
ALTER TABLE "table" ADD COLUMN "col" timestamptz;
```

#### Impact Assessment
- **MEDIUM-HIGH** - Enables complex type migration scenarios
- Common use case in schema evolution
- Currently blocks users from certain migrations

#### Technical Complexity
- **MEDIUM** - Labeled "good first issue" by maintainer
- Requires type coercion detection logic
- Integration with existing dependency system

#### Implementation Guidance
1. Implement type coercibility detection system
2. Add logic to determine binary coercibility
3. Generate DROP/ADD statements for incompatible types
4. Handle dependencies and constraints properly

#### Effort Estimate: 4-5 days

---

### 4. Issue #178: [FEATURE] Support User defined Types ⭐⭐⭐⭐

**Priority:** MEDIUM-HIGH  
**Status:** Open Enhancement  
**Created:** 2024-11-01  
**Labels:** enhancement  
**Comments:** 1 with maintainer assessment  
**Link:** https://github.com/stripe/pg-schema-diff/issues/178

#### Problem Description
Add support for PostgreSQL user-defined types (UDTs) to enable schema diffing for composite types.

**Example:**
```sql
CREATE TYPE udt_KeyValue AS (
    Key INT,
    Value VARCHAR(1000)
);
```

#### Impact Assessment
- **MEDIUM-HIGH** - Enables important PostgreSQL feature
- Unblocks users who rely on composite types
- Expands tool compatibility with advanced PostgreSQL schemas

#### Technical Complexity
- **MEDIUM** - Maintainer indicated "should be pretty straightforward to implement"
- Requires extending schema introspection for `pg_type` catalog
- Add UDT support to DDL generation

#### Implementation Guidance
1. Add UDT queries to schema introspection
2. Extend schema model to represent user-defined types
3. Implement UDT diffing logic
4. Add DDL generation for CREATE/DROP/ALTER TYPE

#### Effort Estimate: 3-4 days

---

### 5. Issue #184: Check constraints that depend on UDFs ⭐⭐⭐⭐

**Priority:** MEDIUM  
**Status:** Open Feature Request  
**Created:** 2024-12-05  
**Comments:** 2 with community interest  
**Link:** https://github.com/stripe/pg-schema-diff/issues/184

#### Problem Description
Tool currently blocks check constraints that depend on user-defined functions (UDFs). Users want an option to allow these constraints.

**Current Limitation:**
```go
// pkg/diff/sql_generator.go:1847-1851 
// Currently blocked: check constraints with UDF dependencies
```

#### Impact Assessment
- **MEDIUM** - Removes artificial limitation
- Growing community need (Supabase integration mentioned)
- Enables advanced constraint scenarios

#### Technical Complexity
- **LOW-MEDIUM** - Specific code location identified
- Maintainer confirmed willingness to add support
- Mostly involves removing restriction and adding configuration option

#### Implementation Guidance
1. Add configuration flag to allow UDF-dependent constraints
2. Modify constraint validation logic
3. Add appropriate warnings about UDF dependency risks
4. Update documentation with usage guidelines

#### Community Interest
Recent engagement including Supabase CLI integration interest, showing broader ecosystem value.

#### Effort Estimate: 1-2 days

---

## Alternative Candidates (Honorable Mentions)

### Issue #205: Support for domains
- **Impact:** MEDIUM-HIGH - Blocks users with domain types
- **Complexity:** MEDIUM - Similar to UDT implementation
- **Note:** Referenced by multiple other issues

### Issue #129: Better dependency tracking for non-sql functions
- **Impact:** MEDIUM - Improves plpgsql function handling  
- **Complexity:** HIGH - Complex dependency analysis required
- **Note:** 12 comments showing strong community interest

### Issue #173: Add support for Materialized Views
- **Impact:** HIGH - Major feature addition
- **Complexity:** HIGH - Complex dependency management
- **Note:** Recent progress noted by maintainer

---

## Implementation Recommendations

### Suggested Order of Execution

1. **Start with Issue #212** (Generated columns bug) - Critical fix, clear implementation path
2. **Follow with Issue #184** (UDF constraints) - Quick win, low complexity
3. **Implement Issue #221** (Migration file output) - High community value
4. **Add Issue #178** (User-defined types) - Moderate complexity, good impact
5. **Complete Issue #179** (Non-coercible types) - Complex but valuable

### Development Strategy

- **Quick Wins First:** Address #212 and #184 to deliver immediate value
- **User-Focused Features:** #221 addresses major workflow needs
- **Foundation Building:** #178 and #179 expand core capabilities
- **Incremental Progress:** Each issue builds understanding for more complex features

### Risk Considerations

- **Issue #212** - Critical path, affects core functionality
- **Issue #179** - May require significant architectural changes
- **Issue #221** - UI/UX decisions around file output formats

---

---

## Reference Links

- [Full Issue List](./.notes/issue_list.md)
- [Issue #212 - Generated Columns Bug](./.notes/issues/issue-212.md)  
- [Issue #221 - Migration File Output](./.notes/issues/issue-221.md)
- [Issue #179 - Non-coercible Types](./.notes/issues/issue-179.md)
- [Issue #178 - User Defined Types](./.notes/issues/issue-178.md)
- [Issue #184 - UDF Check Constraints](./.notes/issues/issue-184.md)

---

**Report Compiled by:** Claude Code Assistant  
**Next Review:** Recommended after 2-3 issues are completed to reassess priorities