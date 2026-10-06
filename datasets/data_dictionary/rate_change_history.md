# `rate_change_history`: Rate change history

**File:** `datasets/reference/rate_change_history.csv` | **Rows:** 36 | **SQLite table:** `rate_change_history`

**Grain:** One row per line x rate change.  
**Key:** `line` + `effective_date`

## Notes

- Approved overall average rate changes, applying to policies effective on or after `effective_date`.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `line` | text | Line of business. | `CP` | No |  |
| `effective_date` | date (YYYY-MM-DD) | Policy effective date from which the change applies. | `2017-01-01` | No |  |
| `approved_rate_change_pct` | decimal | Approved average rate change, % (5.0 = +5%). | `-4.6` | No |  |
| `notes` | text | Filing notes. | `Annual rate review; statewide average across classes and ...` | Yes |  |

Back to the [data dictionary overview](README.md).
