# `historical_cat_events`: Historical catastrophe events

**File:** `datasets/raw/catastrophe/historical_cat_events.csv` | **Rows:** 10 | **SQLite table:** `historical_cat_events`

**Grain:** One row per catastrophe event coded by Kettlerock's claims department.  
**Key:** `cat_event_id`

## Notes

- Event names are fictional. Claims from an event carry its `cat_event_id`.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `cat_event_id` | text | Event code `CAT-<year>-<nn>`. | `CAT-2016-11` | No | Primary key. |
| `name` | text | Event name. | `April North Texas Hail` | No |  |
| `peril` | text | Hurricane, Severe Convective Storm or Winter Storm. | `Severe Convective Storm` | No |  |
| `start_date` | date (YYYY-MM-DD) | First day of the event. | `2016-04-11` | No |  |
| `end_date` | date (YYYY-MM-DD) | Last day of the event. | `2016-04-12` | No |  |
| `states` | text | States affected, semicolon separated. | `TX` | No |  |
| `region_keys` | text | Catastrophe regions affected, semicolon separated. | `TX-NORTH` | No | Same codes as `county_region_map.cat_region`. |

Back to the [data dictionary overview](README.md).
