# `claims`: Claims

**File:** `datasets/raw/claims/claims.csv` | **Rows:** 37,128 | **SQLite table:** `claims`

**Grain:** One row per claim: one claimant (or first-party loss) on one coverage.  
**Key:** `claim_number`

## Notes

- Contains claims reported on or before 2025-12-31.
- Status and dates describe the claim as of 2025-12-31.
- Financial values are in `claim_transactions`; this table has no amounts.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `claim_number` | text | Claim identifier: `C<report year yy>-<sequence>`. | `C21-002904` | No | Primary key. |
| `policy_number` | text | Policy term the claim is made under. | `KR-WC-2020-000597` | No | Joins to `policies.policy_number`. |
| `coverage_code` | text | Coverage the claim is made under. | `WC-STAT` | No | Joins to `policy_coverages` with `policy_number`. |
| `occurrence_id` | text | Occurrence (event) identifier. | `OC0017304` | No | Shared by all claims arising from one occurrence: multi-vehicle auto accidents and every claim from a catastrophe event. Single-claim occurrences have their own id. |
| `accident_date` | date (YYYY-MM-DD) | Date of loss. | `2021-07-16` | No | Defines accident year. |
| `report_date` | date (YYYY-MM-DD) | Date the claim was first reported to Kettlerock. | `2021-09-04` | No |  |
| `close_date` | date (YYYY-MM-DD) | Most recent date the claim was closed. | `2023-06-15` | Yes | Blank if never closed. For a claim reopened and still open, the date it was closed before reopening. |
| `reopen_date` | date (YYYY-MM-DD) | Most recent date the claim was reopened. | `2022-10-30` | Yes |  |
| `claim_status` | text | Open, Closed, Reopened (reopened and currently open) or Closed-Reopened (reopened and closed again). | `Closed` | No |  |
| `cause_of_loss` | text | Cause of loss code. | `WC-STR` | No | Joins to `cause_of_loss_codes.cause_code`. |
| `state` | text | State where the loss occurred. | `CO` | No |  |
| `cat_event_id` | text | Catastrophe event code. | `CAT-2022-13` | Yes | Joins to `historical_cat_events.cat_event_id`; blank for non-catastrophe claims. |
| `claimant_type` | text | Third party BI, Third party PD, First party, Medical (medical-only workers' compensation) or Indemnity (lost-time workers' compensation). | `Indemnity` | No |  |
| `litigated_flag` | flag (Y/N) | Y if a lawsuit has been filed. | `N` | No |  |
| `large_loss_flag` | flag (Y/N) | Large-loss flag maintained by the claims system. | `N` | No | Threshold: $250,000 incurred (indemnity + expense, paid + case). |

Back to the [data dictionary overview](README.md).
