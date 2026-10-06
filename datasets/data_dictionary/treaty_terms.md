# `treaty_terms`: Treaty terms

**File:** `datasets/raw/reinsurance/treaty_terms.csv` | **Rows:** 52 | **SQLite table:** `treaty_terms`

**Grain:** One row per treaty x treaty year, 2016-2025.  
**Key:** `treaty_id` + `treaty_year`

## Notes

- All treaties are written on a losses-occurring basis: the treaty year is the accident year.
- Inuring order (stated in `placement_notes`): facultative, then property per-risk, then property catastrophe; casualty excess of loss, then the CA quota share.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `treaty_id` | text | Treaty: QS-CA, CXL-1, CXL-2, PRX-1, CAT-1 or FAC. | `FAC` | No |  |
| `treaty_year` | integer | Treaty (accident) year. | `2016` | No |  |
| `treaty_type` | text | QS (quota share), XOL-CASUALTY, XOL-RISK (property per risk), XOL-CAT (property catastrophe) or FAC (facultative). | `FAC` | No |  |
| `lines_covered` | text | Lines covered, semicolon separated. | `CP` | No |  |
| `basis` | text | Attachment basis. | `Losses occurring` | No |  |
| `attachment` | integer | Retention per occurrence / risk, $. | `10000000` | Yes | FAC: insured-value threshold above which each location is ceded. |
| `occurrence_limit` | integer | Limit per occurrence / risk, $. | `9000000` | Yes |  |
| `aggregate_limit` | integer | Annual aggregate limit, $ (limit x (1 + reinstatements)). | `27000000` | Yes | Blank when unlimited or not applicable. |
| `reinstatements` | text | Number of reinstatements, or Unlimited. | `2` | Yes |  |
| `reinstatement_premium_pct` | decimal | Reinstatement premium as % of the annual premium, pro rata as to amount. | `0.0` | Yes | For PRX-1 the first reinstatement is free and the second costs 100%; see `placement_notes`. |
| `ceded_pct` | decimal | Quota share cession percentage; 100 for FAC. | `100.0` | Yes |  |
| `ceding_commission_pct` | decimal | Provisional ceding commission, %. | `28.0` | Yes |  |
| `sliding_scale_min` | decimal | Minimum sliding-scale commission, %. | `24.0` | Yes | QS-CA; slide terms in `placement_notes`. |
| `sliding_scale_max` | decimal | Maximum sliding-scale commission, %. | `32.0` | Yes |  |
| `sliding_scale_provisional` | decimal | Provisional sliding-scale commission, %. | `28.0` | Yes |  |
| `profit_commission_pct` | decimal | Profit commission, %. | `(blank)` | Yes |  |
| `rate_on_line` | decimal | Premium as % of the occurrence limit (flat-rated layers). | `11.00` | Yes |  |
| `rate_pct_of_subject_premium` | decimal | Premium rate as % of subject premium (swing or flat-rate layers). | `3.20` | Yes |  |
| `minimum_deposit_premium` | integer | Minimum and deposit premium, $. | `529000` | Yes |  |
| `subject_premium_basis` | text | Premium base the rate applies to. | `Individual risk certificates` | Yes |  |
| `brokerage_pct` | decimal | Reinsurance brokerage, % of reinsurance premium. | `10.0` | Yes |  |
| `placement_notes` | text | Wording points: occurrence definition, ALAE treatment, inuring, commission slide. | `Facultative excess certificates on locations with total i...` | Yes |  |

Back to the [data dictionary overview](README.md).
