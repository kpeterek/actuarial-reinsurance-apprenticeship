# SQL

SQL scripts written during the apprenticeship, and shared snippets taught in class. All queries run against the local SQLite database `datasets/processed/kettlerock.sqlite` (build it first; see [curriculum/software_stack.md](../curriculum/software_stack.md)).

## Layout

| Location | Contents |
|---|---|
| `sql/snippets/` | Reusable patterns taught in Module 03 and later (created as they are taught) |
| `submissions/<exercise_id>/*.sql` | Graded exercise queries |
| `portfolio/<project>/sql/` | Cleaned-up queries for portfolio projects |

## Three ways to run a query

1. **DB Browser for SQLite** (or the VS Code SQLite Viewer): open the database read-only, use the *Execute SQL* tab. Best for exploring.
2. **Python** with the provided helper (run from the repo root with `python/` on the path; see [python/README.md](../python/README.md)):

   ```python
   import pandas as pd
   import kettlerock                     # python/kettlerock.py
   con = kettlerock.connect()
   df = pd.read_sql_query(open("sql/snippets/example.sql").read(), con)
   ```

3. **Python `sqlite3` directly**, for scripts that must run without pandas:

   ```python
   import sqlite3
   con = sqlite3.connect("datasets/processed/kettlerock.sqlite")
   rows = con.execute("SELECT COUNT(*) FROM claims").fetchall()
   ```

The `.sql` file is the deliverable; the notebook or GUI is just how it was run.

## Script conventions

```sql
-- Purpose:   Accident-year paid loss by line (what question this answers)
-- Author:    <name>          Date: YYYY-MM-DD
-- Inputs:    claims, claim_transactions
-- Output:    one row per line x accident_year
-- Reconciles to: total paid in claim_transactions (state the control total)
WITH ... AS (
    SELECT ...
)
SELECT ...;
```

- Keywords in upper case; one clause per line; meaningful aliases.
- CTEs instead of deeply nested subqueries.
- State the grain of every result set in a comment.
- Every aggregation query has a companion reconciliation query (totals before and after).
- Never modify the raw tables. Build cleaned tables or views in a separate working database (taught in Module 03).

## Dialect notes: SQLite vs the warehouse at your next job

The logic transfers; the syntax for dates, types and a few functions does not.

| Topic | SQLite (here) | SQL Server | PostgreSQL | Snowflake / Databricks |
|---|---|---|---|---|
| Row limit | `LIMIT 10` | `TOP 10` | `LIMIT 10` | `LIMIT 10` |
| Dates | Stored as ISO text; `date()`, `strftime('%Y', d)`, `julianday(d2) - julianday(d1)` | `DATE` type; `YEAR(d)`, `DATEDIFF(day, d1, d2)` | `DATE` type; `EXTRACT(YEAR FROM d)`, `d2 - d1` | `YEAR(d)`, `DATEDIFF('day', d1, d2)` |
| String concat | `a \|\| b` | `a + b` or `CONCAT` | `a \|\| b` | `a \|\| b` or `CONCAT` |
| Integer division | `7 / 2` = 3 (cast to `REAL` for decimals) | `7 / 2` = 3 | `7 / 2` = 3 | `7 / 2` = 3.5 |
| Types | Dynamic typing; a column can hold mixed types | Strict | Strict | Strict |
| Booleans | 0 / 1 integers | `BIT` | `BOOLEAN` | `BOOLEAN` |
| Window functions | Supported | Supported | Supported | Supported |
| `FULL OUTER JOIN` | Supported (3.39+) | Supported | Supported | Supported |
| Create table from query | `CREATE TABLE t AS SELECT ...` | `SELECT ... INTO t` | `CREATE TABLE t AS SELECT ...` | `CREATE TABLE t AS SELECT ...` |

SQLite's dynamic typing is a trap worth knowing: a numeric-looking column can contain text, and comparisons will not fail loudly. Check types (`typeof(col)`) when results look wrong.
