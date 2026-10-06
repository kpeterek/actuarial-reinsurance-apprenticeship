# Excel Model Conventions

Every Excel deliverable in the apprenticeship follows these conventions. They are graded under Data Handling / Software, and a model that breaks them is harder to review, which costs points elsewhere too. The standard is the one a reviewing actuary or a lender's model auditor would apply.

## Workbook structure

Sheets flow left to right, from inputs to outputs:

| Order | Sheet | Contents |
|---|---|---|
| 1 | **Cover** | Title, purpose, version block, sheet map, master check status, color legend |
| 2 | **Inputs** | Every assumption, once, with its source and date. Named ranges for key inputs |
| 3 | **Data** | Source data pasted or linked unchanged, as Excel Tables. No edits to raw values |
| 4 | **Calc** sheets | Working calculations, one purpose per sheet (for example Triangle, ATA, Ultimates) |
| 5 | **Exhibit** sheets | Print-ready outputs for the reader. Link to Calc; no new calculations here |
| 6 | **Checks** | Every reconciliation and integrity test, rolled up to one master check |

## Cell formatting

| Cell type | Format |
|---|---|
| Hard-coded input | **Blue** font on light yellow fill |
| Formula | **Black** font |
| Link to another sheet | **Green** font |
| Check cell | Status shows `OK` (green fill) or `CHECK` (red fill) |
| Header | Bold, shaded, bottom border; units in every header (`$000`, `%`, `count`, `months`) |
| Note | Grey italic |

Number formats: amounts `#,##0;(#,##0);"–"`; factors `0.000`; ratios `0.0%`; dates `yyyy-mm-dd`.

## Rules

1. **No hard-coded numbers inside formulas.** `=B5*1.05` is wrong; put the 5% on Inputs and reference it.
2. **One formula per row or column.** A formula should copy across its whole range unchanged. Exceptions are marked with a note.
3. **Tables and structured references** for data (`=SUMIFS(tblClaims[paid], tblClaims[line], $B5)`). Named ranges for key assumptions (`EvalDate`, `Tolerance`).
4. **Check cells.** Each check computes a difference that should be zero (a total by line minus the grand total; a data total minus the control total). Status: `=IF(ABS(diff)<=Tolerance,"OK","CHECK")`. All checks roll up to a master check on Cover. A workbook is not submitted with a `CHECK` showing unless the memo explains it.
5. **Sign conventions are stated on Inputs.** Default: premiums and losses positive; recoveries reduce losses.
6. **Version block** on Cover: version, date, author, description of change, reviewer.
7. **Avoid** volatile functions (`OFFSET`, `INDIRECT`) where a non-volatile alternative exists, circular references, hidden sheets containing logic, merged cells in calculation areas (use *Center Across Selection*), and links to other workbooks.
8. **Pasted values** from SQL or Python are inputs: format them blue and record the query or notebook that produced them.

## Exhibit standards

- Title block: company, exhibit title, line of business, evaluation date, units.
- Numbered columns with the derivation in the header, as in actuarial exhibits: `(3) = (1) × (2)`.
- Totals row with a top border. No gridlines. Print area set, landscape, fit to one page wide.
- Footnotes for every source and every judgmental selection.
- One message per exhibit. Charts follow [reference/communication_standards.md](../reference/communication_standards.md).

## File naming

Submissions: `submissions/<exercise_id>/<exercise_id>_<short_topic>_v<NN>.xlsx` (for example `01-A_results_review_v01.xlsx`). Increment the version when a material change is made after review.

## Functions this program trains

`XLOOKUP`, `INDEX`/`MATCH`, `SUMIFS`, `COUNTIFS`, dynamic arrays (`FILTER`, `UNIQUE`, `SORT`), `LET`, PivotTables and PivotCharts, data tables for sensitivity, scenario analysis, named ranges, data validation, Power Query (Module 02), and basic VBA (Module 06).

## Templates

Both templates contain structure, styles, named ranges and check-cell wiring only. They contain no data and no formulas that perform any exercise's analysis.

| File | Use | Sheets |
|---|---|---|
| [templates/triangle_template.xlsx](templates/triangle_template.xlsx) | Loss development work (Module 06 onward) | Cover, Inputs, Data, Triangle, ATA, Ultimates, Checks |
| [templates/exhibit_template.xlsx](templates/exhibit_template.xlsx) | Any analysis that ends in a printed exhibit | Cover, Inputs, Data, Calc, Exhibit, Checks |

Copy a template into your submission folder and rename it; never edit the template in place.
