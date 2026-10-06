# Portfolio

Sanitized, employer-facing versions of the strongest work from the apprenticeship. Each project shows the full analyst workflow on insurance data: business problem, data handling, actuarial method, result, recommendation, and the code and workbooks behind it.

## What the portfolio is meant to demonstrate

Excel · SQL · Python · insurance analytics · actuarial methodology · reinsurance knowledge · business communication

## Which work gets promoted

A graded item becomes a portfolio candidate when it scores **85 or higher** and is substantial enough to stand alone (capstones, underspecified manager assignments, the final assessment). Expected projects:

| Project | Source | Status |
|---|---|---|
| Primary pricing study | Capstone 1 | Not started |
| Reserve review | Capstone 2 | Not started |
| Casualty excess-of-loss treaty pricing | Capstone 3 | Not started |
| Reinsurance program optimization | Capstone 4 | Not started |
| Additional projects | Strong module exercises | — |

## Sanitizing a project

1. Copy [template/](template/) to `portfolio/<project_name>/`.
2. Rewrite the deliverables for an outside reader: explain context a grader already knew, remove references to exercise ids, grades, hints and feedback.
3. Keep the work reproducible from the public data in `datasets/` plus the project's own SQL and notebook.
4. Do not include grading materials or anything from `solutions/` (it is not published).
5. All data is synthetic (the fictional carrier Kettlerock Mutual Insurance Company). Say so in the project README.
6. Re-run the notebook top to bottom and confirm every check passes before committing.

## Project structure

```
portfolio/<project_name>/
├── README.md              business problem, data, method, results, recommendation, technologies
├── executive_summary.md   one page for a non-technical reader
├── methodology.md         actuarial method, assumptions, judgment calls, limitations
├── data_dictionary.md     tables and fields used, grain, keys, transformations
├── analysis.ipynb         reproducible analysis
├── sql/                   extraction and reconciliation queries
├── excel/                 exhibit workbook where appropriate
└── charts/                exported charts used in the summary
```
