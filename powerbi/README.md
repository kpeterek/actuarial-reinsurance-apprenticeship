# Power BI

The goal is analyst-level comfort: open, understand, modify and build a useful dashboard. Not BI engineering. Power BI is used in Module 02 (first dashboard), Module 10 (portfolio dashboard) and, where appropriate, Capstone 4.

## Install (before Module 02)

Microsoft Store → "Power BI Desktop", or:

```powershell
winget install --id 9NTXR16HNW1T --source msstore
```

More detail: [curriculum/software_stack.md](../curriculum/software_stack.md).

## Connecting to Kettlerock data

1. **CSV (recommended).** *Home → Get Data → Text/CSV*. Load the raw tables from `datasets/raw/` or, better, the clean tables the apprentice builds in Modules 02–03 and exports to CSV. Check column types in Power Query before loading: keys as text, dates as dates, amounts as decimal numbers.
2. **SQLite via ODBC (optional).** Install the 64-bit SQLite ODBC driver, create a DSN pointing at `datasets/processed/kettlerock.sqlite`, then *Get Data → ODBC*.

## Model basics

- **Star schema:** fact tables (premium transactions, claim transactions or claim snapshots) related to dimension tables (policies, a date table, line, state, class, territory).
- **Relationships:** one-to-many from dimension to fact, single direction unless there is a reason.
- **A date table** marked as a date table, so accident year, calendar year and policy year can each be expressed.
- **Measures, not calculated columns,** for anything that aggregates. Ratios are measures of sums (`DIVIDE(SUM(...), SUM(...))`), never averages of row-level ratios.

## Module 02 dashboard: minimum contents

| Element | Requirement |
|---|---|
| Data model | Policies, premium, claims and a date table with correct relationships |
| Measures | Written premium, earned premium (from the apprentice's earned-premium table), paid loss, incurred loss, claim count, loss ratio, frequency, severity |
| KPIs | Headline cards for earned premium, incurred loss ratio and claim count |
| Visuals | Loss ratio by line and year; premium and loss by state |
| Slicers | Line, state, year |
| Drill-down | Line → state → class |
| Reconciliation | One table visual whose totals tie to the Module 02 control totals |

Module 10's portfolio dashboard adds catastrophe and reinsurance views; its requirements are set in that lesson.

## Files

Save `.pbix` files here as `NN_<exercise_id>_<topic>.pbix` (for example `02_02-B_book_overview.pbix`), or in the submission folder if the exercise says so. `.pbix` files are binary; keep them small by importing only the columns the report uses.
