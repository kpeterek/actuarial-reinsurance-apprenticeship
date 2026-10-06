# Capstone 4 — Reinsurance Portfolio Optimization

| | |
|---|---|
| **Assigned** | After Module 10 is passed |
| **Prerequisites** | Modules 09 (Structuring) and 10 (Portfolio & Cat Analytics) at 80+; Capstone 3 passed (its simulation output is an input here) |
| **Gate** | 80+ to pass. 70–79: targeted remediation on the weak components, then a shorter follow-up problem that must score 80+. Below 70: a replacement capstone on a new data cut. A capstone is never resubmitted with corrections (see `curriculum/grading_framework.md` §4). |
| **Time expectation** | 15–20 hours (see `curriculum/roadmap.md`) |
| **Spec reference** | `reference/program_specification.md` §13, §14, §18, §21 |

---

## 1. The request

> **From:** CFO, Kettlerock Mutual Insurance Company
> **To:** Reinsurance Analyst
> **Cc:** Chief Actuary, Chief Risk Officer
> **Re:** 2026 reinsurance program — what should we buy?
>
> We have priced the casualty options. Now I need one recommendation for the whole 2026 program, casualty and property catastrophe together. The board's risk committee will ask three things: what does the program cost us in an average year, how much does it protect us in a bad year, and is it consistent with our risk appetite?
>
> Show me the options side by side. I do not need every combination, but I need to see enough of them to trust that the one you recommend is the right one. Tell me what we give up with your recommendation, not only what we get.

## 2. Data provided

All files are synthetic. Validate before use. Column definitions are in `datasets/data_dictionary/`.

| File | Use |
|---|---|
| `datasets/raw/catastrophe/year_loss_table.csv` | 10,000 simulated years of modeled property catastrophe event losses (gross) |
| `datasets/raw/catastrophe/event_loss_table.csv` | Event-level mean loss, independent and correlated standard deviations, exposure value |
| `datasets/raw/catastrophe/event_catalog.csv` | Event rates, perils, regions, intensity |
| `datasets/raw/catastrophe/historical_cat_events.csv` | Kettlerock's actual catastrophe events, for comparison with modeled results |
| `datasets/raw/policies/locations.csv`, `datasets/reference/county_region_map.csv` | Property exposure by location and region |
| `datasets/raw/reinsurance/treaty_terms.csv` | Current and historical program terms |
| `datasets/raw/reinsurance/treaty_proposals_2026.csv` | All 2026 structures under consideration, casualty and property |
| `datasets/raw/reinsurance/reinsurer_quotes_2026.csv` | Indicative quotes |
| `datasets/raw/reinsurance/property_exposure_curves.csv` | Exposure curves, if you choose to model property per-risk losses |
| Premium, claims, and expense data from earlier capstones | For attritional (non-catastrophe, below-retention) losses, premium, and expenses |
| **Your Capstone 3 simulation output** | Simulated annual casualty results by structure |

**Information you will need that is not in the files.** Kettlerock's policyholder surplus and the board's risk tolerance are provided when the capstone is issued. If they are not, ask for them, as you would in practice. Do not invent them silently.

## 3. Required analysis

1. **Validate the catastrophe model output.** Before you use it: check the YLT against the ELT, check its internal consistency, and compare modeled results with Kettlerock's historical catastrophe experience. Say what the comparison does and does not tell you.
2. **Gross catastrophe metrics.** AAL; OEP and AEP curves; losses at standard return periods (at least 10, 25, 50, 100, 250 years); TVaR at stated levels. Explain the difference between OEP and AEP for this portfolio.
3. **Apply each property catastrophe structure** to the YLT event by event and year by year, including reinstatements and any aggregate features. Produce ceded and net catastrophe losses by simulated year.
4. **Combine with casualty and attritional results.** Build a whole-account annual distribution of net underwriting result for each candidate program (a combination of a casualty structure and a property catastrophe structure). How you represent attritional losses, and how you treat dependence between catastrophe, casualty, and attritional results, is your decision. State the assumption and test its importance.
5. **Evaluate each candidate program** on, at minimum:
   - expected ceded loss and expected retained loss;
   - reinsurance cost (premium paid, less expected recoveries, adjusted for commissions and reinstatement premium);
   - volatility of the net result (standard deviation or another measure you justify);
   - tail loss (net loss at the 1-in-100 and 1-in-250 levels; TVaR);
   - downside protection (how much each program improves the bad years, and which bad years it does not help);
   - capital efficiency (capital relief per dollar of reinsurance cost, using a capital measure you define and justify).
6. **Frontier and recommendation.** Show the cost-versus-protection trade-off across programs; identify programs that are dominated; recommend one program and state what Kettlerock gives up by choosing it.
7. **Sensitivity.** Show how the recommendation changes under at least two alternative assumptions that matter (for example, a different view of catastrophe model risk, a different dependence assumption, or a different quote).

Questions you must answer explicitly:

- Which program do you recommend, what does it cost in an average year, and what does it save in a 1-in-100 year?
- Is the recommended program consistent with the board's risk tolerance? With what margin?
- How much does your answer depend on trusting the catastrophe model, and how did you test that?
- Which programs are dominated, and why should the board not consider them?
- How would you explain the 1-in-100 net loss to a board member who is not an actuary?

## 4. Deliverables

Place everything under `submissions/C4/` (exercise id `C4`).

| Deliverable | Requirements |
|---|---|
| **Python simulation** | Notebook (or notebook plus module) that loads the YLT and Capstone 3 output, applies every structure, combines results, and writes a tidy results file (program × metric). Seeded and reproducible. |
| **Excel summary** | Decision exhibit: programs in columns, metrics in rows, with the frontier chart and the sensitivity table. Built from the Python results file, not retyped. |
| **Power BI dashboard** | Expected if time allows: EP curves gross and net, program comparison, drill-down by peril or region. Optional if you explain what you would have built and why it would help the audience. |
| **Executive recommendation** | 200-word executive summary for the board risk committee, plus a two-to-three-page memo to the CFO with exhibits. Format per `reference/communication_standards.md`. |

## 5. Software

Python (numpy, pandas, matplotlib), Excel, Power BI (optional), Git.

## 6. Grading emphasis

Standard rubric (`curriculum/grading_framework.md`). For this capstone:

- **Technical:** correct OEP/AEP construction, correct event-by-event application of terms including reinstatements, a whole-account combination that preserves simulated-year alignment where it should, correctly computed tail metrics.
- **Reasoning:** what the metrics mean for the decision; how model risk and dependence assumptions affect the answer.
- **Data handling:** validation of the catastrophe output before use; reproducible simulation.
- **Business judgment:** a single recommendation, stated trade-offs, and consistency with the stated risk tolerance.
- **Communication:** a board member should understand the recommendation and what a 1-in-100 result means from the executive summary alone.

## 7. What separates an 80 from a 90

| An 80 submission | A 90 submission |
|---|---|
| Metrics computed correctly for each program | Same, plus a frontier that makes dominated programs obvious |
| Catastrophe output used as given after basic checks | Catastrophe output validated, compared with history, and a model-risk sensitivity built into the recommendation |
| Dependence assumption stated | Dependence assumption stated and its effect on the tail quantified |
| Capital efficiency calculated | Capital measure justified, and the conclusion tested against an alternative measure |
| Recommendation made | Recommendation states what is given up and under what conditions a different program would be better |
| Executive summary within 200 words | Executive summary a board member could repeat accurately to a colleague |
