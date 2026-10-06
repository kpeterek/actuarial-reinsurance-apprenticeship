# `policies`: Policy terms

**File:** `datasets/raw/policies/policies.csv` | **Rows:** 56,571 | **SQLite table:** `policies`

**Grain:** One row per policy term (annual).  
**Key:** `policy_number`

## Notes

- A renewal is a new row with a new `policy_number`; `renewal_of` points to the prior term.
- Status fields are as of the evaluation date, 2025-12-31.
- A cancellation that was later reinstated leaves `policy_status` and `cancel_date` as if the policy was never cancelled; both movements appear in `premium_transactions`.

## Columns

| Column | Type | Description | Example | Nullable | Notes |
|---|---|---|---|---|---|
| `policy_number` | text | Policy term identifier: `KR-<line>-<effective year>-<sequence>`. | `KR-CP-2024-000549` | No | Primary key. |
| `insured_id` | text | Policyholder identifier, stable across renewals. | `IN013971` | No |  |
| `insured_name` | text | Policyholder name (fictional). | `Rivas Apartments Co` | No |  |
| `line` | text | Line of business: CA, GL, CP or WC. | `CP` | No |  |
| `effective_date` | date (YYYY-MM-DD) | Term inception date. | `2024-04-09` | No |  |
| `expiration_date` | date (YYYY-MM-DD) | Term expiration date (one year after inception). | `2025-04-09` | No | Coverage runs to, not through, this date. |
| `state` | text | Two-letter state of the insured's principal operations. | `TX` | No | TX, LA, OK, AR, NM, CO. |
| `territory` | text | Rating territory. | `TX04` | No | Joins to `territory_codes.territory`. |
| `class_code` | text | Rating class. | `CP-OFF` | No | Joins to `class_codes.class_code`. |
| `agent_id` | text | Producing agent. | `AG041` | No |  |
| `policy_status` | text | Active, Expired or Cancelled at the evaluation date. | `Expired` | No |  |
| `cancel_date` | date (YYYY-MM-DD) | Effective date of a mid-term cancellation. | `2024-10-30` | Yes | Populated only when `policy_status` = Cancelled. |
| `renewal_of` | text | `policy_number` of the prior term this term renews. | `KR-CP-2023-000518` | Yes | Blank for new business. |
| `new_renewal_flag` | text | N = new business, R = renewal. | `R` | No |  |

Back to the [data dictionary overview](README.md).
