# `reinsurer_quotes_2026`: 2026 reinsurer quotes

**File:** `datasets/raw/reinsurance/reinsurer_quotes_2026.csv` | **Rows:** 90 | **SQLite table:** `reinsurer_quotes_2026`

**Grain:** One row per proposal x component x reinsurer.  
**Key:** `quote_id`

## Notes

- Indicative quotes from three fictional reinsurers. Premium quotes are in dollars; quota share quotes are a ceding commission.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `quote_id` | text | Quote identifier. | `Q0046` | No | Primary key. |
| `proposal_id` | text | Proposal. | `P3` | No | Joins to `treaty_proposals_2026` with `component_id`. |
| `component_id` | text | Component quoted. | `CAT-1` | No |  |
| `reinsurer` | text | Reinsurer name (fictional). | `Ashgrove Re Ltd` | No |  |
| `quote_type` | text | PREMIUM or CEDING_COMMISSION. | `PREMIUM` | No |  |
| `quoted_premium` | integer | Annual reinsurance premium quoted, $. | `5593000` | Yes |  |
| `quoted_rate_on_line_pct` | decimal | Quoted premium as % of the occurrence limit. | `7.46` | Yes | Excess layers priced on a rate-on-line basis. |
| `quoted_rate_pct_of_subject_premium` | decimal | Quoted premium as % of subject premium. | `3.371` | Yes | Working layers and stop loss. |
| `quoted_ceding_commission_pct` | decimal | Ceding commission offered, %. | `31.1` | Yes | Quota share only. |
| `terms_notes` | text | Quote conditions. | `Indicative; subject to final underwriting information` | No |  |

Back to the [data dictionary overview](README.md).
