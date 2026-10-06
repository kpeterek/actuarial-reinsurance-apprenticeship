# Professional Judgment Checklist

Run this on every deliverable before you submit it. It turns the questions in spec §19 into concrete checks. Graders use the same questions, so anything you skip here will probably come back as a deduction under Analytical Reasoning or Business Judgment.

You don't need to write out answers to every item. You do need to be able to answer every item if asked. For capstones, include a short "Judgment checks" note in your submission that answers Part A.

---

## Part A — The ten questions (spec §19)

| # | Question | What "done" looks like |
|---|---|---|
| 1 | **Is this result plausible?** | You have compared it with at least one independent reference: prior years, another method, an industry benchmark, a back-of-envelope estimate. If it is surprising, you can explain why, or you have looked for an error and not found one. |
| 2 | **What assumption matters most?** | You can name the one or two assumptions that move the answer most and show the result under a reasonable alternative. |
| 3 | **What could make this wrong?** | You have listed the realistic failure modes (data, method, assumption, changed conditions) and checked the most likely ones. |
| 4 | **What would you investigate next?** | You have a concrete next step, not "more analysis." |
| 5 | **What additional information would you request?** | You can name specific data or context, and from whom (claims, underwriting, finance, the broker). |
| 6 | **Would you trust this model?** | You have tested it out of sample, against history, or against an independent method, and you know where it is weakest. |
| 7 | **What decision would you make?** | Your deliverable contains a recommendation an owner could act on, not a menu. |
| 8 | **How would an underwriter challenge this?** | You have checked the conclusion against how the business is actually written: classes, limits, distribution, competitive position, what the underwriter sees on individual risks. |
| 9 | **How would a broker challenge this?** | You have considered the market view: what reinsurers or competitors would assume, whether the price is achievable, what the cedent's alternatives are. |
| 10 | **How would a chief actuary challenge this?** | You have defended every selection (factors, trends, credibility, loads) with evidence, and you know which ones are judgment calls. |

---

## Part B — Mechanics (before anyone reads it)

- [ ] Every total reconciles to a control total or an independent source, and the reconciliation is shown.
- [ ] Every figure is labeled: gross or net; paid, reported, or ultimate; AY, PY, or CY; loss, loss & ALAE, or loss & LAE; units ($000 / $M).
- [ ] The evaluation date and the data period are stated.
- [ ] Ratios use the right denominator: earned premium for loss ratios, on-level premium for comparisons across years, exposure for frequency, claim count for severity.
- [ ] No hardcoded numbers inside formulas; inputs sit in one place and are marked as inputs.
- [ ] Check cells evaluate to zero (or within stated tolerance).
- [ ] SQL and Python run start to finish on a clean session and reproduce the numbers in the workbook.
- [ ] Your Excel and Python versions of the same calculation agree within rounding.
- [ ] Rounding in the memo matches the precision of the analysis.
- [ ] Work is committed to Git with a meaningful message.

---

## Part C — Data sanity checks

**Structure**

- [ ] You know the grain of every table you used, and you aggregated before joining tables of different grain.
- [ ] Primary keys are unique where they should be. Duplicates were investigated, not just dropped.
- [ ] Every foreign key has a match, or the unmatched records are counted and their treatment stated.
- [ ] Row counts before and after each join or filter are recorded, and every change is explained.

**Dates and status**

- [ ] Dates parse consistently across the whole table.
- [ ] Date logic holds: accident ≤ report ≤ close; accident within the policy term; transaction dates not after the evaluation date.
- [ ] Claim status agrees with the transactions (closed claims carry no case reserve; open claims have one).

**Amounts**

- [ ] Paid to date = the sum of payment transactions, net or gross of recoveries as you stated.
- [ ] Reported (incurred) = paid + case, and therefore paid reconciles to reported minus case.
- [ ] Case reserves are never negative.
- [ ] Payments, recoveries, and reserve changes are classified and signed the way the data dictionary says they should be.
- [ ] Premium and exposure move together over time and by segment.
- [ ] Earned premium for a year ≤ written premium for the year + unearned premium at the start of the year (allowing for cancellations).

**Counts and amounts together**

- [ ] Claim counts and loss amounts move in the same direction over time, or you can explain why they don't.
- [ ] Average severity by year is smooth enough to be believable; spikes are traced to specific claims.
- [ ] Frequency per unit of exposure is stable, or its changes have an explanation.

**Composition**

- [ ] You have looked at results by segment (state, territory, class, limit, coverage) before trusting the total.
- [ ] You have checked whether the composition of the book changed over the period, and how that affects the aggregate trend.
- [ ] Loss ratio movement has been decomposed into frequency, severity, and premium (rate and exposure) before you name a cause.

---

## Part D — Line-specific sanity checks

These are orientation checks, not benchmarks. Compare against Kettlerock's own history and against industry sources (Schedule P aggregates, AM Best, NCCI for workers' compensation) before drawing conclusions.

### Commercial auto liability

- Medium-tailed: paid losses at 12 months are a minority of ultimate; reported at 12 months is materially below ultimate.
- Multi-claimant accidents are common, so per-occurrence and per-claim views differ. Check which one a limit or treaty uses.
- Liability and physical damage behave completely differently (physical damage is short-tailed and small). Do not mix them in one triangle or one trend.
- ALAE is material and is much higher on litigated claims.
- Commercial auto has had industry combined ratios above 100% for much of the past decade. A loss ratio far below industry deserves a second look, not a celebration.

### General liability

- Long-tailed: paid at 12 months is small; most of recent accident years' ultimate is IBNR.
- Products and completed operations claims can be reported years after the accident.
- Per-occurrence and general aggregate limits both matter; check which one constrains large losses.
- ALAE can be a large fraction of indemnity and may develop differently from loss.
- Year-to-year loss ratio volatility is high; one or two large claims can move an accident year by several points.

### Commercial property

- Short-tailed: most of ultimate is known within 12–24 months.
- Separate catastrophe from non-catastrophe losses before any trend, development, or loss ratio analysis. A catastrophe year can exceed 100% loss ratio on its own.
- Claims are capped by insured value and reduced by deductibles; percentage wind/hail deductibles change the picture by region.
- Salvage and subrogation recoveries are meaningful; state whether losses are net.
- Construction type, occupancy, and location drive both attritional and catastrophe loss; a portfolio total can hide very different segments.

### Workers' compensation

- Statutory benefits: Part One has no policy limit. Large claims are bounded by benefit law, not by a limit.
- Very long medical tail; the tail factor can be a material share of unpaid losses.
- Premium is subject to payroll audit, so written premium for a year keeps moving after expiration.
- Medical-only claims are numerous and small; lost-time claims drive cost. Look at them separately.
- Texas permits most private employers to opt out of the system ("non-subscribers"), which affects market composition there.

---

## Part E — Method-specific checks

**Pricing**

- [ ] Premium is on-level; losses are developed and trended; the trend period runs from the average accident date of the experience to the average accident date of the future policy period.
- [ ] Large losses are capped and an excess provision added back (or the decision not to cap is justified).
- [ ] Credibility and the complement are stated.
- [ ] The expense and profit provisions reconcile to the reference data, and fixed and variable expenses are treated correctly.
- [ ] The recommendation addresses selection, not just indication.

**Reserving**

- [ ] Triangles reconcile to transaction totals at the latest diagonal.
- [ ] Diagnostics were reviewed down columns and along diagonals before factors were selected.
- [ ] You asked whether claims handling, case reserving practice, staffing, or systems changed during the experience period, and how you would know from the data.
- [ ] Immature years use a method suited to immature data.
- [ ] The tail factor is supported.
- [ ] Where methods disagree, you can explain why.

**Reinsurance pricing and structuring**

- [ ] Treaty terms are applied exactly as written (occurrence basis, aggregate limits, reinstatements, ALAE treatment); assumptions are stated where terms are silent.
- [ ] Layer losses are computed on an as-if basis from ground-up losses, not from historical cessions.
- [ ] Trend is applied to individual ground-up losses before layering.
- [ ] Experience and exposure rating are both done and the difference is explained.
- [ ] The simulation reproduces analytical results where they exist.
- [ ] Price components (expected loss, expenses, brokerage, risk or capital load) are explicit.

**Catastrophe and portfolio**

- [ ] OEP and AEP are not confused; per-occurrence covers are applied event by event.
- [ ] The YLT reconciles to the ELT.
- [ ] Percentiles are not added across portfolios.
- [ ] Dependence assumptions are stated and tested.
- [ ] Return periods are described as annual probabilities.

**Predictive models**

- [ ] Performance is measured on data the model has not seen.
- [ ] The exposure offset and the distribution are appropriate.
- [ ] Relativities are plausible and stable; implausible ones are explained or constrained.
- [ ] Lift and calibration are both checked.
- [ ] You can say where judgment should override the model and why.

---

## Part F — Communication check

- [ ] The first paragraph contains the answer and the recommendation.
- [ ] Data, interpretation, and recommendation are separated (`reference/communication_standards.md`).
- [ ] Every number in the summary can be traced to an exhibit.
- [ ] A range is given for every key estimate, with its basis.
- [ ] Each chart has a message title, units, basis, and source line.
- [ ] Someone outside actuarial (an underwriter, a CFO) could act on the summary without help.
