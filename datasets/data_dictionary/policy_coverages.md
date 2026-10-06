# `policy_coverages`: Policy coverages

**File:** `datasets/raw/policies/policy_coverages.csv` | **Rows:** 64,334 | **SQLite table:** `policy_coverages`

**Grain:** One row per policy term x coverage.  
**Key:** `policy_number` + `coverage_code`

## Notes

- `written_premium` and `exposure_amount` are the final values after all premium transactions booked through 2025-12-31 (endorsements, cancellations, audits). The transaction detail is in `premium_transactions`.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `policy_number` | text | Policy term. | `KR-CP-2023-000398` | No | Joins to `policies.policy_number`. |
| `coverage_code` | text | CA-LIAB (auto liability), CA-PD (auto physical damage), GL-OCC (general liability, occurrence), CP-BLDG / CP-CONT / CP-BI (property building, contents, business income), WC-STAT (workers' compensation and employers liability). | `CP-BLDG` | No |  |
| `occurrence_limit` | integer | Per-occurrence limit in dollars. | `4744000` | Yes | CA-LIAB and GL-OCC: liability limit. CP: total insured value of the coverage across the policy's locations at inception. WC-STAT: employers liability limit (workers' compensation itself is statutory, no limit). Blank for CA-PD (actual cash value). |
| `aggregate_limit` | integer | Annual aggregate limit in dollars. | `(blank)` | Yes | GL-OCC only. |
| `deductible` | integer | Per-occurrence deductible in dollars. | `25000` | No | CP: all-other-perils deductible per location (see `locations` for wind/hail). CA-LIAB and GL-OCC: losses are paid from the first dollar and the deductible is reimbursed by the insured (RECOVERY_DEDUCTIBLE). |
| `exposure_base` | text | Unit of `exposure_amount`: units (power units), revenue_000 (revenue in $000), tiv (total insured value, $), payroll_00 (payroll in $100s). | `tiv` | No |  |
| `exposure_amount` | integer | Exposure for the term in `exposure_base` units. | `4744000` | No | Full-term (annual) amount, not earned. |
| `written_premium` | integer | Written premium for the term in whole dollars. | `41430` | No | Equals the sum of `premium_transactions.written_premium_change` for the coverage. |

Back to the [data dictionary overview](README.md).
