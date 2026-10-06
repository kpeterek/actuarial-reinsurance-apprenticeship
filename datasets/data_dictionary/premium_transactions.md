# `premium_transactions`: Premium transactions

**File:** `datasets/raw/premiums/premium_transactions.csv` | **Rows:** 88,113 | **SQLite table:** `premium_transactions`

**Grain:** One row per premium movement on a policy coverage.  
**Key:** `transaction_id`

## Notes

- Earned premium is not provided. Each transaction earns pro rata from its `effective_date` to the policy `expiration_date`.
- Only transactions booked (transaction_date) on or before 2025-12-31 are included; audits book after the term expires, so recent terms may not yet be audited.
- A REINSTATEMENT reverses a CANCELLATION on the same coverage.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `transaction_id` | text | Transaction identifier, in booking order. | `P0043869` | No | Primary key. |
| `policy_number` | text | Policy term. | `KR-CA-2021-000963` | No | Joins to `policies` and, with `coverage_code`, to `policy_coverages`. |
| `coverage_code` | text | Coverage. | `CA-LIAB` | No |  |
| `transaction_type` | text | NEW, RENEWAL, ENDORSEMENT, CANCELLATION, REINSTATEMENT or AUDIT. | `RENEWAL` | No |  |
| `transaction_date` | date (YYYY-MM-DD) | Date the transaction was booked. | `2021-08-17` | No | Drives written premium by calendar period. |
| `effective_date` | date (YYYY-MM-DD) | Date the change takes effect. | `2021-08-21` | No | NEW/RENEWAL/AUDIT: term inception. ENDORSEMENT: change date. CANCELLATION/REINSTATEMENT: cancellation date. |
| `written_premium_change` | integer | Signed change in written premium, whole dollars. | `21493` | No | Covers the period from `effective_date` to expiration. |
| `exposure_change` | integer | Signed change in exposure, in the coverage's `exposure_base` units. | `8` | No | NEW/RENEWAL: full-term exposure. ENDORSEMENT: change from the effective date. CANCELLATION: minus the in-force exposure. AUDIT: audited minus estimated exposure. |
| `commission_rate` | decimal | Agent commission rate as a decimal (0.150 = 15%). | `0.150` | No |  |

Back to the [data dictionary overview](README.md).
