# Module 02 — Insurance Data

| | |
|---|---|
| **Phase** | I — Insurance Operating System |
| **Estimated hours** | 10–12 (see `curriculum/roadmap.md`) |
| **Gate** | 90 (foundational) |
| **Prerequisites** | 01 |
| **Software** | Excel Power Query and PivotTables; Power BI Desktop (import, relationships, measures). Install Power BI Desktop and a SQLite GUI before starting. |
| **Capstone linkage** | The data preparation and validation skills here are graded in every capstone and in the Final Readiness Assessment. |

**Status:** Not started — `lesson.md` is generated when you reach this module.

## Competencies touched

Names as in `curriculum/competency_matrix.md`.

- Insurance terminology
- Policy & premium data
- Claims & transaction data
- Data validation
- Power Query / VBA
- Power BI
- Professional judgment
- Written communication

## Planned concept sequence

Taught one concept at a time, with a comprehension question after each (see `CLAUDE.md`). The sequence may be compressed or expanded to fit the gradebook when the lesson is generated.

1. How insurance systems store data: policy, coverage, location, claim, and transaction tables
2. Grain and keys: what one row means and why it matters for every join
3. Transactions vs snapshots; evaluation dates
4. Premium transactions: new, renewal, endorsement, cancellation, audit; earning premium pro rata
5. Claim transactions: reserve changes, payments, recoveries; deriving paid, case, and incurred at a date
6. Claim status logic and the claim lifecycle in data
7. Exposure: written, earned, in-force; reconciling to month-end snapshots
8. A data validation checklist and control totals
9. Power Query and PivotTables for insurance data
10. A first Power BI dashboard: relationships and measures

## Exercise theme

Convert claim transactions into a claim-level snapshot at 2025-12-31, reconcile it to control totals, and document the data-quality problems you find.
