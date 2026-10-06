# `expense_assumptions`: Expense assumptions

**File:** `datasets/reference/expense_assumptions.csv` | **Rows:** 44 | **SQLite table:** `expense_assumptions`

**Grain:** One row per line x year (2016-2026).  
**Key:** `line` + `year`

## Notes

- Ratios to premium except `ulae_pct_of_loss`, which is unallocated loss adjustment expense as a share of loss + ALAE.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `line` | text | Line of business. | `GL` | No |  |
| `year` | integer | Calendar / policy year. | `2016` | No |  |
| `commission` | decimal | Agent commission ratio. | `0.1500` | No |  |
| `other_acquisition` | decimal | Other acquisition expense ratio. | `0.0400` | No |  |
| `general` | decimal | General expense ratio. | `0.0600` | No |  |
| `taxes_licenses` | decimal | Taxes, licenses and fees ratio. | `0.0250` | No |  |
| `ulae_pct_of_loss` | decimal | ULAE as a share of loss + ALAE. | `0.0700` | No |  |

Back to the [data dictionary overview](README.md).
