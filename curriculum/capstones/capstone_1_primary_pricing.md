# Capstone 1 — Primary Pricing Study (Commercial Auto Liability and General Liability)

| | |
|---|---|
| **Assigned** | After Module 05 is passed |
| **Prerequisites** | Modules 03 (SQL), 04 (Frequency & Severity), 05 (Primary Pricing) at 80+ |
| **Gate** | 80+ to pass. 70–79: targeted remediation on the weak components, then a shorter follow-up problem that must score 80+. Below 70: a replacement capstone on a new data cut. A capstone is never resubmitted with corrections (see `curriculum/grading_framework.md` §4). |
| **Time expectation** | 10–14 hours (see `curriculum/roadmap.md`), spread over as many sessions as you need |
| **Spec reference** | `reference/program_specification.md` §8, §18, §19, §21 |

---

## 1. The request

> **From:** Chief Actuary, Kettlerock Mutual Insurance Company
> **To:** Pricing Analyst
> **Re:** 2026 rate review — Commercial Auto and General Liability
>
> The underwriting committee meets in March to set rate actions for policies effective on and after **2026-07-01**. I need an independent view of whether our Commercial Auto liability and General Liability rates are adequate for that period, and what we should do about it.
>
> I want an indication by line, a recommendation, and enough support that I can defend it to the committee and to the state filing reviewers. Underwriting will also ask whether any change should be applied uniformly or differentiated across the book, so be ready for that question.
>
> Use the full policy and claim history through the 2025-12-31 evaluation. Assume nothing in the raw data has been cleaned.

Read the request twice. Some of what you need to decide is not spelled out. Deciding it, and explaining why, is part of the assignment.

## 2. Data provided

All files are synthetic. The raw layer contains realistic data-quality problems; validate before use. Column definitions are in `datasets/data_dictionary/`.

| File | Use |
|---|---|
| `datasets/raw/policies/policies.csv` | Policy terms, state, territory, class, status |
| `datasets/raw/policies/policy_coverages.csv` | Coverage limits, deductibles, exposure base and amount |
| `datasets/raw/premiums/premium_transactions.csv` | Transactional written premium and exposure changes |
| `datasets/raw/claims/claims.csv` | Claim header: dates, status, cause, state, flags |
| `datasets/raw/claims/claim_transactions.csv` | Reserve changes, payments, recoveries |
| `datasets/raw/exposures/exposure_snapshots.csv` | Month-end in-force exposure and premium (independent reconciliation source) |
| `datasets/reference/rate_change_history.csv` | Approved rate changes by line and effective date |
| `datasets/reference/expense_assumptions.csv` | Commission, acquisition, general, taxes/licenses, ULAE by line and year |
| `datasets/reference/class_codes.csv`, `territory_codes.csv`, `cause_of_loss_codes.csv` | Lookup tables |
| `datasets/processed/kettlerock.sqlite` | The same raw tables loaded as-is (build with `datasets/processed/build_database.py`) |

**Scope:** coverages `CA-LIAB` and `GL-OCC`. Auto physical damage (`CA-PD`) is out of scope. Kettlerock prices on a loss-and-ALAE basis; ULAE is provided in `expense_assumptions.csv` as a percentage of loss. Management's target underwriting profit and contingencies provision is 5% of premium, before investment income.

You may reuse your own SQL, Python, and Excel work from Modules 02–05, corrected for any feedback you received.

## 3. Required analysis

You decide the order and the depth, but the submission must cover each item below and show how you did it.

1. **Data validation.** Profile the tables you use. Document every issue you find, how you detected it, how you treated it, and its effect on the numbers (material or not). Reconcile premium, exposure, and loss totals across sources.
2. **Premium.** Written and earned premium by line and year, computed from transactions. Bring historical earned premium to current rate level and explain your method.
3. **Exposure.** Earned exposure by line and year. Reconcile to an independent source. Explain how exposure growth and composition have changed.
4. **Losses.** Reported loss and ALAE by line and accident year from the transaction data. State your treatment of recoveries, ALAE, and large losses.
5. **Frequency and severity.** Measure each by line and year, separately and per unit of exposure. Explain what is moving and why you believe it.
6. **Development.** Bring accident years to ultimate. Choose and justify the data (paid or reported) and the factors. Module 06 has not been taught in full; a well-supported chain-ladder approach is acceptable if you explain its limits.
7. **Trend.** Select frequency and severity (or pure premium) trends, choose the fitting window, compute trend periods to the proposed policy period, and justify every selection.
8. **Large losses and credibility.** Decide how to treat large losses and how much credibility the experience deserves; name your complement.
9. **Rate adequacy.** Produce an indicated rate change by line, with expense and profit provisions reconciled to the reference data.
10. **Segmentation.** Determine whether the indication should differ by segment (for example state, territory, class, or limit) and whether any segment-level difference is credible.
11. **Recommendation.** Recommend an action by line. If your recommendation differs from the indication, say why.

Questions you must answer explicitly in the memo:

- Is each line adequately priced for the 2026-07-01 policy period? By how much does it differ, and how confident are you?
- What is driving the result? Separate what the data shows from what you infer.
- Which single assumption moves the indication most, and what is the indication under a reasonable alternative?
- Should the change be uniform or differentiated? On what evidence?
- What would you investigate next, and what additional information would you request from underwriting or claims?

## 4. Deliverables

Place everything under `submissions/C1/` (exercise id `C1`).

| Deliverable | Requirements |
|---|---|
| **SQL** | Scripts that build every base dataset you used (earned premium, exposure, loss and ALAE by accident year, claim counts) from the raw tables. They must run against `datasets/processed/kettlerock.sqlite` without edits. |
| **Excel** | A ratemaking workbook following `excel/README.md`: inputs sheet, calculation sheets, and exhibit sheets (on-level premium, development, trend, indication, segmentation). Check cells that reconcile to the SQL output. |
| **Python** | A Jupyter notebook that independently reproduces the indication for at least one line from the raw data, and produces the charts used in the memo. Runs top to bottom in the `actuary` kernel. |
| **Management memo** | Two pages maximum plus exhibits, in the format in `reference/communication_standards.md`, with a 200-word executive summary at the top. |
| **Data issues log** | One table: issue, detection method, records affected, treatment, effect on results. |

## 5. Software

SQL (SQLite via Python or a GUI), Excel (structured references, SUMIFS/XLOOKUP, dynamic arrays, sensitivity tables), Python (pandas, numpy, scipy or statsmodels for trend fitting, matplotlib), Git (commit your work with meaningful messages as you go).

## 6. Grading emphasis

Scored on the standard rubric in `curriculum/grading_framework.md` (Technical 35 / Reasoning 25 / Data & Software 15 / Business Judgment 15 / Communication 10). For this capstone the grader pays particular attention to:

- **Technical:** correct earned premium and on-leveling, defensible development and trend selections, correct trend periods, an indication formula that is internally consistent with the expense and profit provisions.
- **Reasoning:** whether you can explain *why* the indication is what it is, not just what it is.
- **Data handling:** reconciliation across sources, documented treatment of every data issue, reproducibility of SQL and Python.
- **Business judgment:** a recommendation that a committee could act on, including how you would handle the gap (if any) between indication and selection.

## 7. What separates an 80 from a 90

| An 80 submission | A 90 submission |
|---|---|
| Correct mechanics throughout; indication by line reconciles across Excel, SQL, and Python | Same, and the reconciliation is built into the workbook as check cells |
| Trend selected from a reasonable fit with a stated window | Window chosen from evidence; sensitivity shown; frequency and severity examined separately before being combined |
| Data issues found and fixed | Data issues found, fixed, quantified, and ranked by materiality; validation goes beyond a standard checklist to tests designed around how the numbers will be used |
| Recommendation follows the indication | Recommendation weighs indication, credibility, and the drivers behind it; says what the committee should watch after the change |
| Segment results shown | Segment results interpreted: says which differences are credible, which are noise, and what that means for rate action |
| Memo is clear | Memo is decision-ready: the first 200 words would let the committee act |
