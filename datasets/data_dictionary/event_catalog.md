# `event_catalog`: Stochastic event catalog

**File:** `datasets/raw/catastrophe/event_catalog.csv` | **Rows:** 2,000 | **SQLite table:** `event_catalog`

**Grain:** One row per simulated event.  
**Key:** `event_id`

## Notes

- Vendor-style catalog of possible events with annual occurrence rates (Poisson).

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `event_id` | text | Event identifier. | `EV01001` | No | Primary key. |
| `peril` | text | Hurricane, Severe Convective Storm or Winter Storm. | `Severe Convective Storm` | No |  |
| `annual_rate` | decimal | Expected occurrences per year. | `0.002373` | No |  |
| `region_keys` | text | Footprint: catastrophe regions affected, semicolon separated. | `CO-FRONT` | No |  |
| `intensity_index` | decimal | Relative event intensity, 1 (weak) to 5 (severe). | `1.138` | No |  |

Back to the [data dictionary overview](README.md).
