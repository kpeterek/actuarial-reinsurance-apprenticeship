# Capstone 3 — Casualty Reinsurance Pricing

| | |
|---|---|
| **Assigned** | After Module 08 is passed |
| **Prerequisites** | Module 08 (Reinsurance Pricing) at 80+; Modules 05–07 |
| **Gate** | 80+ to pass. 70–79: targeted remediation on the weak components, then a shorter follow-up problem that must score 80+. Below 70: a replacement capstone on a new data cut. A capstone is never resubmitted with corrections (see `curriculum/grading_framework.md` §4). |
| **Time expectation** | 15–20 hours (see `curriculum/roadmap.md`) |
| **Spec reference** | `reference/program_specification.md` §10–§13, §15, §18, §21 |

---

## 1. The request

> **From:** Chief Actuary, Kettlerock Mutual Insurance Company
> **To:** Reinsurance Analyst
> **Re:** 2026 casualty treaty renewal — independent technical pricing
>
> Our reinsurance broker has sent the renewal submission and indicative quotes from three reinsurers for the casualty excess-of-loss program, along with several alternative structures we asked them to explore. Before we firm order, I want our own technical view.
>
> For each casualty structure on the table: what do we expect to cede, what should it cost, and how do the reinsurers' quotes compare with that? Then tell me which casualty structure you would buy and at what price we should be willing to firm order.
>
> I will be asked by the CFO why our technical number differs from the market, so be ready to explain the difference. Capstone-level rigor: the board will see a summary of this.

## 2. Data provided

All files are synthetic. The raw layer contains realistic data-quality problems; validate before use. Column definitions are in `datasets/data_dictionary/`.

| File | Use |
|---|---|
| `datasets/raw/claims/claims.csv` | Casualty claims, including `occurrence_id` |
| `datasets/raw/claims/claim_transactions.csv` | Loss and ALAE history for development of individual claims |
| `datasets/raw/policies/policies.csv`, `policy_coverages.csv` | Limits profile and subject exposure |
| `datasets/raw/premiums/premium_transactions.csv` | Subject premium history |
| `datasets/raw/exposures/exposure_snapshots.csv` | Exposure history |
| `datasets/reference/rate_change_history.csv` | On-leveling subject premium |
| `datasets/reference/expense_assumptions.csv`, `class_codes.csv`, `territory_codes.csv` | Context and lookups |
| `datasets/raw/reinsurance/treaty_terms.csv` | Kettlerock's historical reinsurance program, 2016–2025 |
| `datasets/raw/reinsurance/ceded_loss_transactions.csv` | Historical ceded losses under the program in force each year |
| `datasets/raw/reinsurance/treaty_proposals_2026.csv` | The 2026 structures under consideration |
| `datasets/raw/reinsurance/reinsurer_quotes_2026.csv` | Indicative quotes from three reinsurers |
| `datasets/raw/reinsurance/casualty_ilf_table.csv` | Increased limits factors by line and limit, for exposure rating |
| `datasets/processed/kettlerock.sqlite` | The same raw tables loaded as-is |

**Scope:** every casualty structure in `treaty_proposals_2026.csv` (per-occurrence excess layers, and any aggregate or proportional casualty alternatives in the file). Property and catastrophe structures are out of scope here; they come back in Capstone 4. Apply treaty terms exactly as written. Where the terms are silent on a point that matters (for example, the treatment of ALAE), state your assumption and test its sensitivity.

You may reuse your Capstone 1 trend work and Capstone 2 development work, corrected for feedback.

## 3. Required analysis

1. **Data preparation.** Build an individual large-loss listing (claim and occurrence level) with ground-up loss and ALAE at each evaluation. Validate it and document issues and treatments.
2. **Trend.** Trend individual losses to the 2026 treaty period. Justify the trend rate; show how trend affects excess layers differently from ground-up losses.
3. **Development.** Develop losses to ultimate in a way that is appropriate for excess layers. Explain why ground-up development factors may not be appropriate for a layer and what you did instead.
4. **Layer losses.** Compute as-if layer losses for each proposed structure, for each historical treaty year, applying the 2026 terms (attachment, limit, occurrence basis, aggregate features, reinstatements) to trended, developed losses.
5. **Experience rating.** Bring subject premium to the 2026 rate and exposure level; compute burning cost by structure; assess the credibility of the experience.
6. **Exposure rating.** Use the limits profile and `casualty_ilf_table.csv` to produce an exposure-rated expected layer loss for each per-occurrence layer.
7. **Reconciliation.** Compare experience and exposure results; explain the difference; select an expected loss cost with a credibility rationale.
8. **Simulation.** Build a frequency-severity Monte Carlo model of prospective losses (at least 10,000 simulated years) parameterized from your work. Produce, for each structure: expected ceded loss, retained loss, standard deviation of ceded loss, attachment and exhaustion probabilities, and reinstatement premium where applicable. Validate the simulation against your analytical results.
9. **Technical price.** Move from expected loss cost to technical premium: expenses, brokerage, risk margin or cost of capital, with every load stated and justified. Express results as premium, rate on line (where meaningful), and percentage of subject premium.
10. **Market comparison.** Compare technical prices with the three quotes; explain why technical and market prices differ.
11. **Alternatives and recommendation.** Compare the casualty structures on expected cost of reinsurance (premium less expected recoveries, net of any commission) and on what each does to retained results. Recommend a structure and a firm-order price or negotiation position.

Questions you must answer explicitly:

- What is your expected ceded loss and technical price for each casualty structure, and what range do you place around each?
- Why do your experience and exposure ratings differ, and which do you trust more for each layer?
- Which assumption is the price most sensitive to?
- Are the quotes fair? Where would you push back, and with what argument?
- Which structure do you recommend, and what would make you change your mind?

## 4. Deliverables

Place everything under `submissions/C3/` (exercise id `C3`).

| Deliverable | Requirements |
|---|---|
| **Pricing model** | Excel pricing workbook (inputs, as-if layer losses, burning cost, exposure rating, loads, price) and a Python notebook (large-loss preparation, trend, development, simulation). The two must reconcile on expected layer loss within your stated tolerance. |
| **Simulation output** | Save simulated annual results (one row per simulated year per structure: ground-up casualty loss above your modeling threshold, ceded, retained, reinstatement premium) to a CSV in your submission folder. **Capstone 4 uses this file.** Document the seed and parameters. |
| **Exhibits** | Pricing summary by structure; experience vs exposure reconciliation; technical vs quoted comparison; sensitivity table. |
| **Recommendation** | Memo to the Chief Actuary, two pages plus exhibits, with a 200-word executive summary. Format per `reference/communication_standards.md`. |

## 5. Software

Python (pandas, numpy, scipy.stats for severity fitting, `python/layers.py` from Module 08), Excel (pricing workbook, sensitivity tables), SQL for data extraction, Git.

## 6. Grading emphasis

Standard rubric (`curriculum/grading_framework.md`). For this capstone:

- **Technical:** correct layer arithmetic, correct application of occurrence and aggregate terms, appropriate excess development, correct trend application to individual losses, a simulation that reproduces analytical expectations, a coherent load structure.
- **Reasoning:** the experience-vs-exposure reconciliation and the technical-vs-market explanation. These two discussions carry most of the reasoning score.
- **Data handling:** a reproducible large-loss listing built from transactions; seeded, documented simulation.
- **Business judgment:** a firm-order position you could defend to a reinsurer's underwriter, not only a number.

## 7. What separates an 80 from a 90

| An 80 submission | A 90 submission |
|---|---|
| Both rating methods applied correctly | Both applied correctly, and the gap between them is explained by identifying the specific assumption that drives it |
| Layer losses computed on trended, developed losses | Layer losses computed on an as-if basis that is consistent across years, with the effect of each adjustment shown |
| Simulation runs and gives plausible results | Simulation is validated against closed-form or analytical checks, and its sensitivity to severity parameters is shown |
| Technical price built from stated loads | Loads justified from first principles (capital, volatility, expenses), with the risk margin linked to the volatility of the layer |
| Quotes compared to technical price | Market differences explained (different severity views, capacity, relationship, payback expectations) and turned into a negotiation stance |
| Recommendation made | Recommendation explicitly weighs cost against what the structure does for retained volatility and sets up the portfolio question for Capstone 4 |
