# `cause_of_loss_codes`: Cause of loss codes

**File:** `datasets/reference/cause_of_loss_codes.csv` | **Rows:** 30 | **SQLite table:** `cause_of_loss_codes`

**Grain:** One row per cause of loss code.  
**Key:** `cause_code`

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `cause_code` | text | Cause of loss code. | `PR-FIR` | No | Primary key. |
| `line` | text | Line the code is used for. | `CP` | No |  |
| `description` | text | Description. | `Fire or smoke` | No |  |
| `peril_group` | text | Broader peril grouping. | `Fire` | No |  |

Back to the [data dictionary overview](README.md).
