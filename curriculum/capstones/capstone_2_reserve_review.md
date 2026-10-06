# Capstone 2 — Reserve Review (General Liability and Workers' Compensation)

| | |
|---|---|
| **Assigned** | After Module 06 is passed |
| **Prerequisites** | Module 06 (Reserving) at 80+; Modules 02–03 data work |
| **Gate** | 80+ to pass. 70–79: targeted remediation on the weak components, then a shorter follow-up problem that must score 80+. Below 70: a replacement capstone on a new data cut. A capstone is never resubmitted with corrections (see `curriculum/grading_framework.md` §4). |
| **Time expectation** | 10–14 hours (see `curriculum/roadmap.md`) |
| **Spec reference** | `reference/program_specification.md` §9, §18, §19, §21 |

---

## 1. The request

> **From:** CFO, Kettlerock Mutual Insurance Company
> **Cc:** Chief Actuary
> **To:** Reserving Analyst
> **Re:** Year-end 2025 reserve review — GL and WC
>
> General Liability and Workers' Compensation are our two longest-tailed lines, and they carry a large share of our loss reserves. Before we finalize the year-end 2025 statements, I want an independent estimate of unpaid loss and ALAE for both lines as of 2025-12-31.
>
> Tell me what you think the reserves should be, how confident you are, and how you got there. Where your methods produce different answers, I need to know which one you believe and why. The external auditors and the appointed actuary will read your memo.

## 2. Data provided

All files are synthetic. The raw layer contains realistic data-quality problems; validate before use. Column definitions are in `datasets/data_dictionary/`.

| File | Use |
|---|---|
| `datasets/raw/claims/claims.csv` | Claim header: accident, report, close dates; status; flags |
| `datasets/raw/claims/claim_transactions.csv` | Reserve changes, payments, recoveries (the source for every triangle) |
| `datasets/raw/policies/policies.csv` | Policy terms (for linking and earned exposure) |
| `datasets/raw/policies/policy_coverages.csv` | Coverage detail and exposure |
| `datasets/raw/premiums/premium_transactions.csv` | Earned premium for expected-loss-ratio methods |
| `datasets/reference/rate_change_history.csv` | Rate level history (for on-level premium in ELR and Cape Cod) |
| `datasets/reference/expense_assumptions.csv` | ULAE assumption (context only; ULAE is out of scope) |
| `datasets/processed/kettlerock.sqlite` | The same raw tables loaded as-is |

**Scope:** coverages `GL-OCC` and `WC-STAT`; accident years 2016–2025; gross of reinsurance; loss and ALAE. You decide whether to analyze ALAE with loss or separately, and must justify the choice. ULAE and net-of-reinsurance reserves are out of scope, but the memo must say what you would need to estimate them.

You may reuse your Module 06 Excel template and `python/triangles.py`, corrected for any feedback.

## 3. Required analysis

1. **Data preparation.** Build the claim-level history at each year-end 2016–2025 from transactions. Validate it, document every issue and its treatment, and reconcile your 2025-12-31 paid and case totals to the transaction data.
2. **Triangles.** For each line, build at minimum: cumulative paid, reported (paid + case), reported claim counts, and closed claim counts by accident year and age (12-month intervals). Add any other triangle you need to support your conclusions.
3. **Development factors.** Compute age-to-age factors, consider several averages, select factors, and justify each selection. Select and support a tail factor for each line.
4. **Ultimates by method.** At minimum: paid chain ladder, reported chain ladder, expected loss ratio, and Bornhuetter-Ferguson (state which development basis drives the B-F). Cape Cod is expected at least conceptually; implementing it earns credit.
5. **Diagnostics.** Test whether the historical patterns you are projecting still hold. Explain what each diagnostic shows.
6. **Method comparison.** Show ultimates side by side by accident year. Where methods differ materially, explain why, and say which estimate you believe for each year.
7. **Selection.** Select ultimate loss and ALAE by accident year for each line; derive IBNR (total unpaid less case) and total unpaid.
8. **Uncertainty.** Provide a reasonable range and show which assumptions drive it (sensitivity table at minimum; a stochastic method such as Mack or bootstrap earns credit if you can explain it).
9. **Recommendation.** Recommended reserve point estimate and range by line, with the evidence behind it.

Questions you must answer explicitly in the memo:

- What are your selected unpaid loss and ALAE by line, and what is the reasonable range?
- Where do your methods disagree, why, and which do you believe?
- What does each method assume about the future, and how did you test whether those assumptions hold for each line?
- Which accident years carry the most uncertainty, and what would narrow it?
- What would you ask the claims department before signing off?

## 4. Deliverables

Place everything under `submissions/C2/` (exercise id `C2`).

| Deliverable | Requirements |
|---|---|
| **Excel workbook** | One workbook per line or one combined, following `excel/README.md`: triangles, factor selection, method exhibits, selection exhibit, diagnostics, sensitivity. Selections must be visibly marked as judgment (input cells) with a comment explaining each. |
| **Python analysis** | Notebook that builds the triangles from raw transactions and reproduces your chain-ladder and B-F results; reconciles to the Excel workbook within rounding. |
| **Reserve memo** | Two to three pages plus exhibits, format per `reference/communication_standards.md`, with a 200-word executive summary for the CFO. |
| **Data issues log** | Issue, detection, records affected, treatment, effect on triangles. |

## 5. Software

Excel (triangle layout, INDEX/MATCH or XLOOKUP, dynamic arrays, data validation for selections), Python (pandas pivoting, `python/triangles.py`), SQL optional for data preparation, Git.

## 6. Grading emphasis

Standard rubric (`curriculum/grading_framework.md`). For this capstone:

- **Technical:** triangles built correctly from transactions (dates, statuses, recoveries handled correctly); factor and tail selections defensible; B-F and ELR use an appropriate premium base and a priori; IBNR defined consistently.
- **Reasoning:** whether you can explain the results, including any differences between methods. A mechanically correct review that cannot explain its own numbers will not score well on the reasoning criterion.
- **Data handling:** triangles reconcile to transaction totals; the Python and Excel results agree.
- **Business judgment:** a selected estimate, not a menu; a range with a stated basis; clear statement of what would change your view.

## 7. What separates an 80 from a 90

| An 80 submission | A 90 submission |
|---|---|
| All required methods applied correctly, selections reasonable | Selections explained factor by factor; averages chosen for stated reasons, not by default |
| Method results compared | Any differences between methods are explained with evidence from the data, and the selected ultimate follows from that explanation |
| Diagnostics included | Diagnostics drive decisions: you can point to the exhibit that changed your selection |
| Range provided | Range built from the assumptions that actually drive uncertainty, with a stated basis |
| Assumptions listed | Each key assumption tested against the data for each line, with the test shown and the result stated |
| Memo is clear | The auditor could follow the memo without opening the workbook |
