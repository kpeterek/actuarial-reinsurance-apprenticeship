# `event_loss_table`: Event loss table

**File:** `datasets/raw/catastrophe/event_loss_table.csv` | **Rows:** 2,000 | **SQLite table:** `event_loss_table`

**Grain:** One row per catalog event.  
**Key:** `event_id`

## Notes

- Losses to Kettlerock's CP locations in force at 2025-12-31, after policy deductibles, before reinsurance.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `event_id` | text | Event. | `EV01001` | No | Joins to `event_catalog.event_id`. |
| `mean_gross_loss` | integer | Expected loss given the event occurs, $. | `62724` | No |  |
| `sd_independent` | integer | Standard deviation of the independent (location-level) part of secondary uncertainty, $. | `2855` | No |  |
| `sd_correlated` | integer | Standard deviation of the correlated part of secondary uncertainty, $. | `28226` | No | Total standard deviation is commonly taken as `sd_independent` + `sd_correlated`. |
| `exposure_value` | integer | Total insured value of in-force locations in the event footprint, $. | `1713271000` | No |  |

Back to the [data dictionary overview](README.md).
