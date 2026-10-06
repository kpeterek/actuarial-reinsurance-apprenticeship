# `county_region_map`: County to region map

**File:** `datasets/reference/county_region_map.csv` | **Rows:** 67 | **SQLite table:** `county_region_map`

**Grain:** One row per state x county.  
**Key:** `state` + `county`

## Notes

- County names repeat across states (for example Jefferson), so always join on state and county.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `state` | text | State. | `OK` | No |  |
| `county` | text | County or parish. | `Canadian` | No |  |
| `territory` | text | Rating territory the county belongs to. | `OK01` | No |  |
| `cat_region` | text | Catastrophe modeling region. | `OK-CENTRAL` | No | Used in `region_keys` of the catastrophe tables. |
| `coastal_flag` | flag (Y/N) | Y if the county is designated coastal. | `N` | No |  |
| `zip3` | text | Representative ZIP3. | `730` | No |  |

Back to the [data dictionary overview](README.md).
