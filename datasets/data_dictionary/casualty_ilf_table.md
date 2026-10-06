# `casualty_ilf_table`: Casualty increased limits factors

**File:** `datasets/raw/reinsurance/casualty_ilf_table.csv` | **Rows:** 24 | **SQLite table:** `casualty_ilf_table`

**Grain:** One row per line x limit.  
**Key:** `line` + `limit`

## Notes

- Industry increased limits factors for 2026 policy-year exposure, relative to the basic limit. Not derived from Kettlerock's own data.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `line` | text | CA (auto liability) or GL. | `GL` | No |  |
| `limit` | integer | Policy limit, $. | `100000` | No |  |
| `basic_limit` | integer | Basic limit the factors are relative to, $. | `100000` | No |  |
| `increased_limits_factor` | decimal | Ratio of expected limited loss at `limit` to expected limited loss at the basic limit. | `1.0000` | No | Indemnity only. |

Back to the [data dictionary overview](README.md).
