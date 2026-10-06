# `locations`: Property locations

**File:** `datasets/raw/policies/locations.csv` | **Rows:** 36,140 | **SQLite table:** `locations`

**Grain:** One row per CP policy term x location.  
**Key:** `policy_number` + `location_id`

## Notes

- `location_id` identifies a physical location and repeats on each renewal term of the same policyholder.
- Insured values are for the term shown and are revalued at each renewal.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `location_id` | text | Physical location identifier. | `L004872` | No | Repeats across renewal terms. |
| `policy_number` | text | CP policy term. | `KR-CP-2021-000748` | No | Joins to `policies.policy_number`. |
| `state` | text | Location state. | `TX` | No |  |
| `county` | text | County or parish. | `Midland` | No | Joins to `county_region_map` on `state` + `county`. |
| `zip3` | text | First three digits of the ZIP code. | `797` | No | Stored as text. |
| `construction_class` | text | ISO-style construction: Frame, Joisted Masonry, Non-combustible, Masonry Non-combustible, Fire-resistive. | `Masonry Non-combustible` | No |  |
| `occupancy` | text | Office, Retail, Warehouse, Light Mfg, Restaurant or Apartment. | `Office` | No |  |
| `year_built` | integer | Year of construction. | `1982` | No |  |
| `stories` | integer | Number of stories. | `1` | No |  |
| `tiv_building` | integer | Building insured value, $. | `3507000` | No |  |
| `tiv_contents` | integer | Contents insured value, $. | `0` | No | 0 when the policy has no CP-CONT coverage. |
| `tiv_bi` | integer | Business income insured value (annual), $. | `0` | No | 0 when the policy has no CP-BI coverage. |
| `aop_deductible` | integer | All-other-perils deductible per occurrence, $. | `2500` | No |  |
| `wind_hail_deductible_pct` | integer | Windstorm/hail deductible as a percent of the location's total insured value: 0, 1, 2 or 5. | `2` | No | 0 means the AOP deductible applies to wind and hail. |
| `coastal_flag` | flag (Y/N) | Y if the county is designated coastal. | `N` | No | Same as `county_region_map.coastal_flag`. |
| `fac_flag` | flag (Y/N) | Y if facultative reinsurance was purchased for the location. | `N` | No | Facultative cover is bought for locations whose total insured value exceeds $10M; it takes 100% of each loss above $10M per location. |

Back to the [data dictionary overview](README.md).
