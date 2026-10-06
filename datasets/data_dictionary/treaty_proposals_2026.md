# `treaty_proposals_2026`: 2026 treaty proposals

**File:** `datasets/raw/reinsurance/treaty_proposals_2026.csv` | **Rows:** 30 | **SQLite table:** `treaty_proposals_2026`

**Grain:** One row per proposal x component.  
**Key:** `proposal_id` + `component_id`

## Notes

- Each proposal is a complete 2026 program; components repeated from the expiring program carry the same `component_id`.
- Subject premium estimates are 2026 projections.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `proposal_id` | text | Proposal P0-P6. | `P3` | No |  |
| `proposal_name` | text | Short description of the proposal. | `Expiring program plus CA aggregate stop loss` | No |  |
| `component_id` | text | Treaty component within the proposal. | `CAT-1` | No |  |
| `treaty_type` | text | QS, XOL-CASUALTY, XOL-RISK, XOL-CAT, AGG-STOP-LOSS or AGG-CAT. | `XOL-CAT` | No |  |
| `lines_covered` | text | Lines covered. | `CP` | No |  |
| `attachment` | integer | Retention per occurrence / risk, $. | `15000000` | Yes |  |
| `occurrence_limit` | integer | Limit per occurrence / risk, $ (AGG-CAT: aggregate limit). | `75000000` | Yes |  |
| `aggregate_limit` | integer | Annual aggregate limit, $. | `150000000` | Yes |  |
| `aggregate_attachment` | integer | Annual aggregate retention, $ (aggregate covers). | `20000000` | Yes |  |
| `reinstatements` | text | Number of reinstatements, or Unlimited. | `1` | Yes |  |
| `reinstatement_premium_pct` | decimal | Reinstatement premium, % of annual premium. | `100.0` | Yes |  |
| `ceded_pct` | decimal | Quota share cession %. | `25.0` | Yes |  |
| `ceding_commission_pct` | decimal | Quota share ceding commission %. | `30.0` | Yes |  |
| `stop_loss_attachment_lr_pct` | decimal | Stop-loss attachment as a loss ratio, %. | `78.0` | Yes |  |
| `stop_loss_limit_lr_pts` | decimal | Stop-loss limit in loss-ratio points. | `15.0` | Yes |  |
| `subject_premium_estimate_2026` | integer | Estimated 2026 subject premium for the component, $. | `95725000` | Yes |  |
| `notes` | text | Structure notes. | `25% of CA premium and losses net of casualty excess recov...` | Yes |  |

Back to the [data dictionary overview](README.md).
