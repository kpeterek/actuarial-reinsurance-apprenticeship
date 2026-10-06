# `year_loss_table`: Year loss table

**File:** `datasets/raw/catastrophe/year_loss_table.csv` | **Rows:** 38,732 | **SQLite table:** `year_loss_table`

**Grain:** One row per simulated event occurrence.  
**Key:** `sim_year` + `event_id` + `day_of_year`

## Notes

- 10,000 simulated years numbered 1-10,000. Years with no events have no rows.
- Losses include secondary uncertainty sampled around the event loss table mean; same basis as `event_loss_table`.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `sim_year` | integer | Simulated year, 1-10,000. | `5017` | No |  |
| `event_id` | text | Event. | `EV01575` | No | Joins to `event_catalog` and `event_loss_table`. |
| `day_of_year` | integer | Day of the year the event occurs (1-365). | `196` | No |  |
| `gross_loss` | integer | Simulated loss for this occurrence, $. | `34678` | No |  |

Back to the [data dictionary overview](README.md).
