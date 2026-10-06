# `claim_transactions`: Claim transactions

**File:** `datasets/raw/claims/claim_transactions.csv` | **Rows:** 239,608 | **SQLite table:** `claim_transactions`

**Grain:** One row per financial or status movement on a claim.  
**Key:** `transaction_id`

## Notes

- Outstanding case reserve for a category (INDEMNITY or EXPENSE) at a date = cumulative sum of RESERVE_SET and RESERVE_CHANGE amounts in that category up to that date. Payments do not reduce the reserve automatically; adjusters book a RESERVE_CHANGE when they revise it.
- Paid loss = PAYMENT_INDEMNITY. Paid ALAE = PAYMENT_EXPENSE. Recoveries (salvage, subrogation, deductible reimbursement) are money received and reduce net paid.
- Reported incurred = paid indemnity + paid expense - recoveries + outstanding case reserves.
- Only movements dated on or before 2025-12-31 are included, so open claims show case reserves and partial payments.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `transaction_id` | text | Transaction identifier, in date order. | `T0119326` | No | Primary key. |
| `claim_number` | text | Claim. | `C21-002530` | No | Joins to `claims.claim_number`. |
| `transaction_date` | date (YYYY-MM-DD) | Date of the movement. | `2022-02-23` | No | Defines the calendar period and the evaluation it belongs to. |
| `transaction_type` | text | RESERVE_SET, RESERVE_CHANGE, PAYMENT_INDEMNITY, PAYMENT_EXPENSE, RECOVERY_SALVAGE, RECOVERY_SUBRO, RECOVERY_DEDUCTIBLE, CLOSE or REOPEN. | `PAYMENT_EXPENSE` | No |  |
| `amount` | decimal | Amount in dollars and cents. | `2386.17` | No | Reserve rows: change in the outstanding case reserve (positive raises it, negative lowers it). Payments: positive amount paid. Recoveries: positive amount received. CLOSE and REOPEN: 0.00. |
| `reserve_category` | text | INDEMNITY or EXPENSE (allocated loss adjustment expense). | `EXPENSE` | Yes | Blank on CLOSE and REOPEN rows. Recoveries are INDEMNITY. |
| `adjuster_id` | text | Handling adjuster: office prefix plus number. | `DAL03` | No |  |
| `note` | text | Short free-text note from the adjuster. | `Medical bills` | Yes | Mostly blank; at most 40 characters. |

Back to the [data dictionary overview](README.md).
