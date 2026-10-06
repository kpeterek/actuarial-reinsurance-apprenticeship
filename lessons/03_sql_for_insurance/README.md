# Module 03 — SQL for Insurance

| | |
|---|---|
| **Phase** | I — Insurance Operating System |
| **Estimated hours** | 8–10 (see `curriculum/roadmap.md`) |
| **Gate** | 90 (foundational) |
| **Prerequisites** | 02 |
| **Software** | SQLite through a GUI (DB Browser for SQLite or the VS Code SQLite Viewer) and Python `sqlite3`; CTEs and window functions |
| **Capstone linkage** | Prerequisite for Capstone 1 (which requires a SQL deliverable). SQL is used in every later capstone. |

**Status:** Not started — `lesson.md` is generated when you reach this module.

## Competencies touched

Names as in `curriculum/competency_matrix.md`.

- Policy & premium data
- Claims & transaction data
- Data validation
- SQL
- Git
- Professional judgment
- Written communication

## Planned concept sequence

Taught one concept at a time, with a comprehension question after each (see `CLAUDE.md`). The sequence may be compressed or expanded to fit the gradebook when the lesson is generated.

1. The Kettlerock database: tables, as-is views, and three ways to run a query
2. SELECT, WHERE, and ORDER BY on policy and claim tables
3. GROUP BY and HAVING: accident-year and calendar-year aggregation
4. Joins across policies, coverages, claims, and transactions, and what joins do to row counts
5. CASE expressions and date handling in SQLite
6. Subqueries and CTEs for layered logic
7. Window functions: running totals, latest record per claim, ranking
8. Earned premium in SQL
9. Data-quality and reconciliation queries: key integrity, duplicate detection, control totals
10. Dialect differences: SQLite vs SQL Server, PostgreSQL, Snowflake, and Databricks

## Exercise theme

Produce an accident-year loss and premium summary by line from the raw tables, with a reconciliation and a data-quality query log.
