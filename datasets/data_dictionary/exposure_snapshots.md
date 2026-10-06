# `exposure_snapshots`: Exposure snapshots

**File:** `datasets/raw/exposures/exposure_snapshots.csv` | **Rows:** 28,221 | **SQLite table:** `exposure_snapshots`

**Grain:** One row per month-end x coverage x state x class with at least one coverage in force.  
**Key:** `month_end` + `coverage_code` + `state` + `class_code`

## Notes

- In force at a month-end means effective on or before the month-end and not yet expired or cancelled.
- Exposure and premium are annual (full-term) amounts as currently written; audit adjustments are not reflected.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `month_end` | date (YYYY-MM-DD) | Calendar month-end, 2016-01-31 to 2025-12-31. | `2021-01-31` | No |  |
| `coverage_code` | text | Coverage. | `CP-BLDG` | No |  |
| `state` | text | Policy state. | `OK` | No |  |
| `class_code` | text | Rating class. | `CP-WHS` | No |  |
| `inforce_coverages` | integer | Number of policy coverages in force. | `33` | No |  |
| `inforce_exposure` | integer | Sum of in-force annual exposure in `exposure_base` units. | `147156000` | No |  |
| `inforce_premium` | integer | Sum of in-force annualised written premium, $. | `809391` | No |  |

Back to the [data dictionary overview](README.md).
