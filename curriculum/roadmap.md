# Roadmap

Twelve modules, five phases, four capstones and a final readiness assessment. Every module is built on one fictional carrier, Kettlerock Mutual Insurance Company, so the work accumulates the way it would in a first analyst job.

## How to read this roadmap

- **A "week" is a unit of work, not a calendar week.** The apprentice works full time. Each module is sized in hours (roughly 8–14), and the calendar belongs to the apprentice. Week numbers below indicate sequence only.
- **Progression is gated, not scheduled.** A module is finished when its gate exercise is passed, not when the hours are spent. Modules 01–03 are foundational and require **90+**; all later modules require **80+**. See [grading_framework.md](grading_framework.md).
- **Lessons are generated when reached.** Each module folder holds a stub at build time. The full `lesson.md`, examples and exercises are written when the apprentice arrives, adapted to the gradebook.
- **Software is embedded in insurance work.** No module is "the Python module". Tools are introduced where an insurance problem needs them.

## Module sequence

| Wk | Module | Phase | Hours | Core content | Software introduced / deepened | Exercise theme | Gate |
|---|---|---|---|---|---|---|---|
| 1 | [01 Insurance Foundations](../lessons/01_insurance_foundations/) | I | 8–10 | How an insurer makes money; policy, premium and loss vocabulary (spec §7); AY/PY/CY; gross/net; insurer financial statements; Schedule P concept | Excel (Tables, structured references, SUMIFS, XLOOKUP, model layout); Git (init, commit, push) | Line-of-business results review for the CFO from a results package; 150-word management note | 90 |
| 2 | [02 Insurance Data](../lessons/02_insurance_data/) | I | 10–12 | Policy, coverage, location, claim and transaction tables; grain and keys; earning premium from transactions; snapshot vs transaction; claim status logic; data validation checklist; first dashboard | Excel Power Query, PivotTables; Power BI (import, relationships, measures) | Convert claim transactions into a claim-level snapshot at 2025-12-31, reconcile to control totals, and document the data-quality problems found | 90 |
| 3 | [03 SQL for Insurance](../lessons/03_sql_for_insurance/) | I | 8–10 | SELECT through window functions on Kettlerock data; AY and CY aggregation; policy-to-claim joins; duplicate detection; earned premium in SQL; reconciliation queries | SQLite via a GUI and Python `sqlite3`; CTEs, window functions | Accident-year loss and premium summary by line from the raw tables, with a reconciliation and a data-quality query log | 90 |
| 4 | [04 Frequency & Severity](../lessons/04_frequency_severity/) | II | 10–12 | Exposure bases; frequency, severity, pure premium; fitting severity distributions; limited expected value; large-loss capping; measuring frequency and severity trend separately; compound Poisson | Python (pandas, scipy.stats, matplotlib), Jupyter; first notebook | "Management believes a line has deteriorated." Diagnose what is driving it and write a memo | 80 |
| 5 | [05 Primary Pricing](../lessons/05_primary_pricing/) | II | 10–12 | Full spec §8 workflow: data validation, exposure, on-leveling, development (preview), trend, catastrophe and large-loss adjustment, credibility, expenses, profit provision, indication, segmentation, actual vs expected | Excel ratemaking exhibit; Python reproduction | Rate indication for a casualty line with a recommendation; **Capstone 1 assigned at module end** | 80 |
| 6 | [06 Reserving](../lessons/06_reserving/) | II | 10–12 | Paid, incurred and count triangles; age-to-age factors, selections, tail, CDFs, ultimates, IBNR; chain ladder, expected loss ratio, Bornhuetter-Ferguson, Cape Cod concept; diagnostics; calendar-year effects; settlement-pattern change; reserve uncertainty | Excel triangle template; basic VBA (record and edit a macro); Python `python/triangles.py` written in class | Reserve review of a long-tailed line: build triangles, select factors, compare methods, reconcile differences; **Capstone 2 assigned at module end** | 80 |
| 7 | [07 Reinsurance Foundations](../lessons/07_reinsurance_foundations/) | III | 8–10 | Spec §10 vocabulary; treaty vs facultative; quota share, surplus share, per-risk XOL, cat XOL, clash, aggregate, stop loss; reinstatements; commissions; rate on line; Kettlerock's own program; gross, ceded, net | Excel layer calculator; diagrams | Apply Kettlerock's 2025 program to a set of occurrences; compute ceded and net; explain reinstatement premium; one-page program summary for a new CFO | 80 |
| 8 | [08 Reinsurance Pricing](../lessons/08_reinsurance_pricing/) | III | 10–14 | Spec §11–12: layer mathematics, LEV, attachment and exhaustion probability; experience rating (trend, develop, on-level, burning cost, credibility); exposure rating (ILFs, exposure curves); Monte Carlo; expected loss cost to technical premium to quoted premium | Python simulation (`python/layers.py` written in class); Excel pricing model | Price a Kettlerock casualty excess layer by experience and exposure rating, reconcile the two, and propose a quote; **Capstone 3 assigned at module end** | 80 |
| 9 | [09 Reinsurance Structuring](../lessons/09_reinsurance_structuring/) | III | 8–10 | Spec §13 structuring comparisons; retained vs ceded distributions; volatility, tail risk, capital, earnings stability; casualty topics (spec §15): long vs short tail, claims-made vs occurrence, social inflation, limits profiles, attachment erosion, why casualty reinsurance is hard to price | Python simulation; Excel decision exhibit | Compare the 2026 renewal proposals and write a recommendation to the CFO (first time-boxed exercise) | 80 |
| 10 | [10 Portfolio & Cat Analytics](../lessons/10_portfolio_cat_analytics/) | IV | 10–12 | Spec §14: hazard, vulnerability, exposure; event catalogs, ELT and YLT; AAL; OEP and AEP; return periods; PML; TVaR; secondary uncertainty; accumulation, concentration, diversification; cat XOL evaluation | Python; Power BI portfolio dashboard | Evaluate cat program adequacy from the year loss table; explain a 100-year PML to a CFO; **Capstone 4 assigned at module end** | 80 |
| 11 | [11 Predictive Modeling](../lessons/11_predictive_modeling/) | IV | 10–12 | Spec §16: EDA, sampling, confidence intervals, hypothesis tests, regression, GLMs (Poisson, negative binomial, Gamma, Tweedie, logistic), validation, train/test, variable selection, interactions, residuals, lift, calibration; when judgment overrides the model | Python statsmodels; **R introduced** (read, modify and run an actuarial GLM script) | Frequency and severity GLMs for a casualty line, compared with the Module 05 aggregate indication | 80 |
| 12 | [12 Professional Practice](../lessons/12_professional_practice/) | V | 8–10 | Spec §17–19 and §22: insurer financial analysis (how an insurer makes money, prior-year development, statutory vs GAAP at a high level, AM Best and Schedule P conceptually); model review; executive communication; interview drills; Final Readiness Assessment (spec §36) | All tools; Power Query and Excel automation revisited | Graded interview drills, then the Final Readiness Assessment | Classification |

Estimated core time: 110–136 hours, plus capstones (below) and any remediation.

## Phases

| Phase | Name (spec §20) | Modules | Purpose |
|---|---|---|---|
| I | Insurance Operating System | 01–03 | Vocabulary, financial statements, how insurance data is actually stored, Excel and SQL fluency on real-shaped data |
| II | Core Actuarial Work | 04–06 | Frequency/severity, trend, pricing, credibility, loss development, reserving |
| III | Reinsurance | 07–09 | Treaty structures, layer mathematics, experience and exposure rating, treaty pricing, structuring |
| IV | Advanced Analytics | 10–11 | Simulation, portfolio and catastrophe analytics, GLMs, R |
| V | Professional Practice | 12 | Integrated work, executive communication, model review, interviews, final assessment |

### Sequencing decisions

- **Phase I has three modules, not two.** Data literacy and SQL (spec §6) are prerequisites for every later module, so SQL gets its own module inside Phase I rather than being squeezed into week 2.
- **Python starts in Module 04, not Phase IV.** Fitting severity distributions and measuring trend need it; deferring Python to week 9 would leave Capstones 1–3 without their Python deliverable. Phase IV deepens Python rather than introducing it.
- **Portfolio and catastrophe analytics (10) come before predictive modeling (11).** Capstone 4 depends on the simulation taught in Modules 08–10, not on GLMs, so cat/portfolio work follows reinsurance directly while the simulation tools are fresh. GLMs then close Phase IV and feed the professional-practice module.
- **Spec §17 (insurer financial analysis)** is introduced in Module 01 and completed in Module 12, where it supports model review and executive communication.

## Capstone timing

| Capstone | Assigned after | Depends on modules | Hours | Gate | Spec |
|---|---|---|---|---|---|
| C1 Primary Pricing Study | Module 05 | 03, 04, 05 | 10–14 | 80 | [capstone_1_primary_pricing.md](capstones/capstone_1_primary_pricing.md) |
| C2 Reserve Review | Module 06 | 06 | 10–14 | 80 | [capstone_2_reserve_review.md](capstones/capstone_2_reserve_review.md) |
| C3 Reinsurance Pricing | Module 08 | 08 | 15–20 | 80 | [capstone_3_reinsurance_pricing.md](capstones/capstone_3_reinsurance_pricing.md) |
| C4 Reinsurance Portfolio Optimization | Module 10 | 09, 10 | 15–20 | 80 | [capstone_4_portfolio_optimization.md](capstones/capstone_4_portfolio_optimization.md) |
| Final Readiness Assessment | Module 12 | All | 12–16 | Classification | [final_readiness_assessment.md](capstones/final_readiness_assessment.md) |

A capstone may run in parallel with the next module's early concepts, but the next module's gate exercise is not assigned until the capstone is graded. A capstone scoring below 70 is replaced by a new capstone on a new data cut, not resubmitted.

## What "complete" means

A module is complete only when all four conditions hold:

1. Every concept in `lesson.md` has been taught and its comprehension question answered and evaluated.
2. The module's gate exercise has been graded at or above the gate (after remediation if needed).
3. The grade file, gradebook, competency matrix, competency history and current status are updated.
4. The work is committed and pushed.

Module-specific evidence of completion:

| Module | Complete when the apprentice has |
|---|---|
| 01 | A conventions-compliant Excel results review with correct denominators, a CFO note that separates data from interpretation from recommendation, and a first Git commit |
| 02 | A reconciled claim-level snapshot built from transactions, a written data-validation log, and a first Power BI dashboard |
| 03 | A set of SQL scripts that reproduce AY premium and loss summaries from raw tables and reconcile to control totals |
| 04 | A reproducible notebook separating frequency, severity and other drivers, with fitted distributions and a memo |
| 05 | An Excel rate indication exhibit reproduced in Python, with a sized recommendation |
| 06 | Paid and incurred triangles in Excel and Python, method comparison, IBNR estimate and a reserve memo |
| 07 | A working layer calculator, correct ceded/net and reinstatement calculations, and a one-page program summary |
| 08 | Experience- and exposure-rated layer costs, a reconciliation between them, and a technical-to-quoted price build |
| 09 | A simulation-backed comparison of structures and a written CFO recommendation delivered within the time box |
| 10 | EP curves, AAL, PML and TVaR from the YLT, a cat program evaluation and a Power BI portfolio view |
| 11 | Validated frequency and severity GLMs, a comparison with the aggregate indication, and an R script run and modified |
| 12 | Passed interview drills and a completed Final Readiness Assessment with a classification |

## Escalating realism

- **Modules 01–04:** no time pressure; exercises are fully specified; data problems are discussed openly in Module 02.
- **Modules 05–12:** at least one deliberately underspecified exercise per module (spec §29). Data problems are no longer announced; the apprentice is expected to find them (spec §28).
- **Modules 08–12:** occasional time-boxed work: 30-minute diagnostics, 60-minute pricing reviews, 90-minute data analyses, 200-word executive summaries, five-minute verbal explanations (spec §30).

## Installs the apprentice performs

| Tool | Install before | Notes |
|---|---|---|
| A SQLite GUI (DB Browser for SQLite or the VS Code SQLite Viewer extension) | Module 02 | Used heavily in Module 03 |
| Power BI Desktop | **Module 02** | First dashboard is part of Module 02 |
| R and RStudio | **Module 11** | R is read, modified and run in Module 11 |

Commands and versions: [software_stack.md](software_stack.md).

## Related documents

- [competency_matrix.md](competency_matrix.md) — what each module is evidence for
- [dependency_map.md](dependency_map.md) — prerequisites, concept reuse, MAS-I topic map
- [grading_framework.md](grading_framework.md) — rubric, gates, remediation, readiness classification
