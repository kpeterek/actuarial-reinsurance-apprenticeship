# `ceded_loss_transactions`: Ceded loss transactions

**File:** `datasets/raw/reinsurance/ceded_loss_transactions.csv` | **Rows:** 15,737 | **SQLite table:** `ceded_loss_transactions`

**Grain:** One row per claim x treaty x year-end evaluation at which the ceded amount changed.  
**Key:** `cession_id` (natural key: `evaluation_date` + `treaty_id` + `claim_number`)

## Notes

- Evaluations are each 31 December, 2016-2025. A claim-treaty pair has a row only in years its ceded paid or ceded incurred changed; the latest row carries the current cumulative values.
- Gross amounts are loss plus ALAE net of recoveries. Ceded amounts are allocated from the occurrence (or risk, or event) to claims in proportion to gross.
- Net = gross - sum of ceded across all treaties for the claim.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `cession_id` | text | Row identifier. | `R0007869` | No | Primary key. |
| `evaluation_date` | date (YYYY-MM-DD) | Year-end evaluation date. | `2020-12-31` | No |  |
| `treaty_id` | text | Treaty. | `QS-CA` | No | Joins to `treaty_terms` on `treaty_id` + `treaty_year`. |
| `treaty_year` | integer | Treaty year (accident year of the claim). | `2020` | No |  |
| `occurrence_id` | text | Occurrence of the claim. | `OC0013517` | No | Joins to `claims.occurrence_id`. |
| `claim_number` | text | Claim. | `C20-002212` | No | Joins to `claims.claim_number`. |
| `gross_paid_to_date` | decimal | Gross paid loss + ALAE net of recoveries at the evaluation, $. | `0.00` | No |  |
| `gross_incurred_to_date` | decimal | Gross incurred loss + ALAE (paid + case) at the evaluation, $. | `15000.00` | No |  |
| `ceded_paid_to_date` | decimal | Cumulative ceded paid under this treaty, $. | `0.00` | No |  |
| `ceded_incurred_to_date` | decimal | Cumulative ceded incurred under this treaty, $. | `3000.00` | No |  |
| `ceded_paid_change` | decimal | Change in ceded paid since the claim's previous row for this treaty, $. | `0.00` | No |  |
| `ceded_incurred_change` | decimal | Change in ceded incurred since the previous row, $. | `3000.00` | No |  |

Back to the [data dictionary overview](README.md).
