# `class_codes`: Class codes

**File:** `datasets/reference/class_codes.csv` | **Rows:** 23 | **SQLite table:** `class_codes`

**Grain:** One row per rating class.  
**Key:** `class_code`

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `class_code` | text | Rating class code. | `CP-OFF` | No | Primary key. |
| `line` | text | Line of business. | `CP` | No |  |
| `class_description` | text | Class description. | `Office buildings` | No |  |
| `exposure_base` | text | Exposure base used to rate the class. | `tiv` | No |  |

Back to the [data dictionary overview](README.md).
