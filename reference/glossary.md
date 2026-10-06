# Glossary

Working definitions for the apprenticeship. They follow common US P&C usage (Werner & Modlin, *Basic Ratemaking*; Friedland, *Estimating Unpaid Claims Using Basic Techniques*; Clark, *Basics of Reinsurance Pricing*; CAS syllabus readings). Where a term has more than one meaning in practice, the entry says so. In a deliverable, define any term your reader might take differently.

**How to read the analogies.** Where a commercial real estate (CRE) finance concept maps cleanly, it is given as *CRE analogy*. *Where it breaks* flags the point at which the analogy stops being true. Use the analogy to get your bearings, then think in insurance terms.

**Notation.** X = ground-up loss per claim or occurrence; S(x) = P(X > x); N = claim count; a = attachment; l = layer limit; u = a policy limit or cap; E[X ∧ u] = E[min(X, u)] is the limited expected value.

Sections:
1. [Insurance fundamentals](#1-insurance-fundamentals) (spec §7)
2. [Insurance data](#2-insurance-data) (spec §6)
3. [Primary pricing](#3-primary-pricing) (spec §8)
4. [Reserving](#4-reserving) (spec §9)
5. [Reinsurance fundamentals](#5-reinsurance-fundamentals) (spec §10)
6. [Reinsurance mathematics and pricing](#6-reinsurance-mathematics-and-pricing) (spec §11–§12)
7. [Catastrophe and portfolio analytics](#7-catastrophe-and-portfolio-analytics) (spec §14)
8. [Casualty analytics](#8-casualty-analytics) (spec §15)
9. [Statistics and predictive modeling](#9-statistics-and-predictive-modeling) (spec §16)
10. [Insurer financial analysis](#10-insurer-financial-analysis) (spec §17)

---

## 1. Insurance fundamentals

**Accident** — A sudden, unexpected event that causes injury or damage. Policy wording often uses the broader term *occurrence*. In data, the accident date is when the loss event happened, and it determines the accident year.

**Accident year (AY)** — Groups losses by the year the loss event happened. It doesn't matter when the policy was written, when the claim was reported, or when it was paid. AY is the standard basis for loss development and most pricing because it matches losses to the period of exposure that produced them.

**ALAE (allocated loss adjustment expense)** — Claim expenses that can be assigned to a specific claim, mainly defense counsel, experts, and court costs. US statutory reporting uses the closely related category DCC (defense and cost containment). The two overlap heavily but are not identical. ALAE is often analyzed together with loss ("loss and ALAE") because it develops in a similar way.
*CRE analogy:* legal and workout costs charged to a specific defaulted loan.

**Attachment point** — The loss amount at which a layer (an excess policy or a reinsurance layer) starts to pay. A layer of $5M xs $5M pays the part of each loss between $5M and $10M.
*CRE analogy:* a lender's position in a capital stack, measured in loss terms. In a stack of 60% senior, 15% mezzanine, and 25% equity, the mezzanine "attaches" once losses in value exceed 25% and is "exhausted" at 40%.
*Where it breaks:* a reinsurance layer is unfunded. The reinsurer receives premium up front and pays only when a loss happens; it doesn't invest principal and earn a coupon. Most layers also apply per occurrence and renew each year, whereas a loan's principal loss is a one-time event on one asset.

**Calendar year (CY)** — Groups transactions by when they are booked, whatever the accident date. CY incurred loss = losses paid during the year + the change in loss reserves (case and IBNR) during the year. It therefore mixes current-year losses with revisions to prior years. Financial statements are prepared on a CY basis.
*CRE analogy:* a property's annual GAAP income statement, which includes catch-up items such as a prior-year CAM reconciliation or a tax-appeal refund alongside the current year's operations.

**Case reserve** — The adjuster's estimate of what remains to be paid on a specific reported claim: the estimated total cost minus the amount already paid. It is revised as facts emerge and set to zero when the claim closes.
*CRE analogy:* an accrued liability carried at an estimate, such as a litigation accrual for a known premises-liability suit.
*Where it breaks:* case reserves are revised continually, and how adequate they are depends on the adjuster and on company practice. Actuaries therefore treat them as data to be tested, not as facts.

**Ceded** — The part of premium or losses transferred to a reinsurer. Ceded premium is paid to reinsurers, and ceded losses are recoverable from them.
*CRE analogy:* the share of a loan sold to participants.
*Where it breaks:* the ceding insurer stays fully liable to its policyholders even if a reinsurer fails to pay. Reinsurance recoverables carry credit risk.

**Claim** — A demand for payment under a policy. One occurrence can produce several claims (for example, several injured people in one auto accident), and one claim can touch several coverages. Claim systems usually store one row per claimant per coverage, so a "claim count" depends on the definition used.

**Combined ratio** — (Incurred losses + LAE + underwriting expenses) ÷ premium. Below 100% means an underwriting profit before investment income. On the statutory "trade basis," losses and LAE are divided by earned premium and underwriting expenses by written premium. On a GAAP basis, everything is divided by earned premium.
*CRE analogy:* total operating cost per dollar of revenue before investment income, where the loss ratio plays the role of the main cost of delivering the product.
*Where it breaks:* the largest cost (losses) is still an estimate when the ratio is reported, and it can be revised for years afterward.

**Coverage** — A specific promise within a policy, such as bodily injury liability, building damage, or business income. Each coverage has its own limit, deductible, and exposure base, and a commercial policy usually contains several.

**Deductible** — The part of each loss the insured bears before the insurer pays. With an ordinary deductible d, the insurer pays max(X − d, 0), up to the limit. Deductibles remove many small claims, so they cut claim frequency much more than total cost. Variants include percentage deductibles (for example, wind/hail as a percentage of insured value), aggregate deductibles, and self-insured retentions (SIRs), where the insured pays and handles claims below the SIR.
*CRE analogy:* the equity's first-loss position below a lender.
*Where it breaks:* deductibles apply per claim or occurrence, not once per asset. On some programs the insurer pays from the first dollar and then bills the insured for the deductible, which creates credit risk.

**Development year (development age)** — Time from the start of the accident year (or policy year) to the evaluation date, usually in months. For example, AY 2024 evaluated at 2025-12-31 is at 24 months. Triangles are laid out by origin year and development age.

**Direct vs assumed** — Direct business is written by the company itself. Assumed business is reinsurance the company has accepted from another insurer. Gross = direct + assumed.

**Earned premium** — The part of written premium for which coverage has already been provided. An annual policy written on 2025-07-01 for $1,200 has earned $600 by 2025-12-31 (pro rata). Earned premium is the denominator for loss ratios because it matches losses to the coverage provided.
*CRE analogy:* rent revenue recognized straight-line over the lease term.
*Where it breaks:* earning is usually pro rata over the term even when risk is seasonal. A few products use non-pro-rata earning.

**Expense ratio** — Underwriting expenses ÷ premium. Underwriting expenses are commissions, other acquisition costs, general expenses, and premium taxes, licenses, and fees. Statutory practice divides by written premium because acquisition costs are incurred when policies are written; GAAP divides by earned premium. LAE normally sits with losses (in the loss and LAE ratio), not here.
*CRE analogy:* leasing commissions and overhead as a percentage of revenue.
*Where it breaks:* the denominator convention changes the number. Always state which one you used.

**Exposure** — The unit of risk on which premium is based. Examples: power units (commercial auto), revenue in $000 (general liability), total insured value (property), and payroll in $100 (workers' compensation). A good exposure base is proportional to expected loss, practical to measure, and hard to manipulate. Written, earned, and in-force exposure mirror the premium concepts.
*CRE analogy:* rentable square feet as the base for rent.
*Where it breaks:* an exposure base is chosen because it correlates with loss, not because it measures what is sold.

**Frequency** — Claim count ÷ exposure, for example claims per 100 power units. It measures how often losses happen.
*CRE analogy:* probability of default.
*Where it breaks:* one exposure unit can generate several claims in a year, but a loan defaults once.

**Gross vs net** — Gross means before reinsurance (direct + assumed). Net means after deducting ceded reinsurance. A net loss ratio can be higher or lower than the gross one, depending on the reinsurance terms. Always label the basis.

**IBNR (incurred but not reported)** — The reserve for losses that have happened but are not yet in reported losses (paid + case). In the broad sense used in most actuarial work, IBNR = estimated ultimate − reported. It therefore covers both *pure IBNR* (claims not yet reported) and *IBNER* (future development on claims already reported). Some companies report the two separately.
*CRE analogy:* liabilities incurred but not yet invoiced, such as December contractor work billed in February. The broad definition also covers invoices that have arrived but whose final amount will change.
*Where it breaks:* IBNR is estimated statistically from development patterns. For long-tailed lines it can be larger than case reserves, and it emerges over years rather than weeks.

**Incurred loss** — Usually paid loss + case reserves, also called reported or case-incurred loss. Some people use "incurred" to include IBNR ("ultimate incurred"), so state which you mean.
*CRE analogy:* cash paid plus accrued liabilities.

**LAE (loss adjustment expense)** — The cost of investigating, defending, and settling claims. It splits into ALAE (allocated to specific claims) and ULAE (not allocated). US statutory reporting instead uses DCC and AO (adjusting and other).

**Limit** — The most the insurer will pay. A per-occurrence limit caps payment for one event; an aggregate limit caps total payments over the policy term. With an ordinary deductible d and a maximum payment u, the insurer pays min(max(X − d, 0), u). Contract wording decides whether the limit applies before or after the deductible.

**Loss cost** — Expected loss (often loss and ALAE) per unit of exposure, usually the same thing as pure premium. Advisory organizations publish prospective loss costs, which insurers turn into rates by adding expense and profit provisions.

**Loss ratio** — Losses ÷ earned premium. A loss ratio is meaningless unless you state whether losses include LAE or ALAE, whether they are paid, reported, or ultimate, and whether premium is at current rate level.

**Occurrence** — An event, including continuous or repeated exposure to substantially the same harmful conditions, that causes injury or damage. Per-occurrence limits and per-occurrence reinsurance treat all claims from one occurrence as one loss. Contracts define the term differently (see *hours clause*).

**Paid loss** — Amounts actually paid on claims, cumulative to an evaluation date. It is usually shown net of salvage and subrogation, so state the convention. Paid losses are facts, but they lag the true cost.

**Policy** — The contract that sets out coverages, limits, deductibles, premium, term (commonly 12 months), and conditions. Each renewal is a new policy term, and the policy term is the basic unit of most policy data.

**Policy year (PY)** — Groups premium and losses by the year the policy took effect. A policy year of annual policies spans 24 months of accident dates. It is used where premium and losses must come from the same contracts, for example in lines with premium audits.
*CRE analogy:* loan origination vintage analysis.
*Where it breaks:* one origination year of loans maps to one cohort, but one policy year's losses arrive over two accident years.

**Premium** — The price of insurance: rate × exposure, adjusted by rating factors and individual risk modifications.

**Pure premium** — Losses (often loss and ALAE) ÷ exposure, which equals frequency × severity. It is the expected-loss part of the rate, before expenses and profit.
*CRE analogy:* expected credit loss = PD × LGD × EAD. Both split expected loss into "how often" and "how much."
*Where it breaks:* insurance severity is heavy-tailed, and one exposure can produce several claims.

**Severity** — Average loss per claim: losses ÷ claim count. Severity distributions are heavy-tailed, so a few large claims dominate. Analysts often study severity with large losses capped.
*CRE analogy:* loss given default, in dollars.

**ULAE (unallocated loss adjustment expense)** — Claims-department costs that cannot be assigned to individual claims, such as salaries, rent, and systems. It is usually estimated as a percentage of losses.
*CRE analogy:* asset-management overhead, as opposed to costs tied to one property.

**Underwriting profit** — Earned premium − incurred losses − LAE − underwriting expenses (and policyholder dividends where applicable), which equals (1 − combined ratio) × premium. It excludes investment income.
*CRE analogy:* operating income from the core business before financing and investment returns.

**Unearned premium** — Written premium not yet earned. It is carried as a liability (the unearned premium reserve) because the insurer owes either the remaining coverage or, if the policy is cancelled, a refund.
*CRE analogy:* prepaid rent, or deferred revenue.
*Where it breaks:* the reserve also has to fund future losses on in-force policies. If those expected losses exceed it, a premium deficiency reserve is required, which has no counterpart for prepaid rent.

**Written premium** — Premium on policies written (booked) during a period, including endorsements, audits, and cancellations booked in that period. It measures sales.
*CRE analogy:* signed lease value (bookings), as opposed to rent recognized.

---

## 2. Insurance data

**Audit (premium audit)** — A review after expiration of the insured's actual exposure (payroll, sales), followed by an additional or return premium. It is common in workers' compensation and general liability. Written premium for a policy can therefore change long after the policy has expired.

**Cancellation** — Ending a policy before expiration. A pro rata cancellation returns unearned premium in proportion to time remaining; a short-rate cancellation returns less, as a penalty. A flat cancellation voids the policy from inception. In data, a cancellation is a negative premium transaction.

**Cause of loss** — A coded reason for the claim, such as collision, fire, hail, or slip-and-fall. It is used for segmentation, catastrophe identification, and subrogation potential.

**Claim status** — Open, closed, or reopened, as recorded by the claim system. Status should agree with the transactions (for example, a closed claim should carry no case reserve). When it does not, the transactions are usually more reliable.

**Close date** — The date a claim was closed. A claim can close and later reopen, so "close date" may mean the first or the latest closing.

**Control total** — An independently sourced total (from the general ledger, a prior report, or another table) that a derived dataset must reconcile to. Reconciling to control totals is how you prove a dataset is complete.

**Endorsement** — A mid-term change to a policy (adding a vehicle, raising a limit) that generates an additional or return premium transaction.

**Evaluation date** — The "as of" date of a dataset. All paid, case, incurred, and count figures depend on it, so a triangle is a set of evaluations.

**Grain** — What one row in a table represents (one policy term, one coverage, one claim, one financial transaction). Knowing the grain of every table is the first step in any analysis. Joining tables of different grain without aggregating first duplicates amounts.

**In-force** — Policies (or exposure, or premium) providing coverage on a given date. In-force snapshots taken at month-ends give an independent way to check earned exposure.

**Key (primary / foreign)** — A primary key uniquely identifies a row (for example, `claim_number`). A foreign key links to another table (`policy_number` on a claim). *Referential integrity* means every foreign key has a matching primary key.

**Recovery** — Money that comes back to the insurer after a payment: salvage, subrogation, or a deductible reimbursement. Analyses must state whether losses are gross or net of recoveries.

**Reinstatement (policy)** — Restoring a cancelled policy to force. This is unrelated to a reinsurance reinstatement (see section 5).

**Renewal** — A new policy term that replaces an expiring one for the same insured. Renewal flags and links to the prior term let you measure retention.

**Reopened claim** — A closed claim that is reopened, usually because new information or further payments arise. Reopenings affect closed-count triangles, status logic, and development on accident years that looked finished.

**Report date** — The date the insurer was first notified of a claim. The time from accident to report (the report lag) drives pure IBNR.

**Reserve change** — A transaction that raises or lowers a claim's case reserve. The case reserve at any date is the sum of reserve-setting and reserve-change transactions, less any payments that the system books against the reserve. Each system has its own convention, so read the data dictionary.

**Salvage** — Recovery from selling damaged property the insurer took over after paying a total loss.

**Snapshot vs transaction table** — A transaction table records every financial movement with its date. A snapshot records the state of each item (paid to date, case reserve, status) at one evaluation date. Snapshots at any date can be built from transactions, but not the other way round.

**Subrogation** — The insurer's right, after paying a claim, to recover from the third party who caused the loss.

**Transaction date vs effective date** — The transaction date is when a movement was booked. The effective date is when the change takes effect in coverage terms. An endorsement booked in March can be effective from January, and the difference matters for calendar-year reporting and for earning premium.

---

## 3. Primary pricing

**Actual vs expected (A/E)** — A comparison of emerged losses (or claim counts) in a period with the amounts expected under the assumptions currently in use. Expected emergence = expected ultimate × the share expected to emerge in the period. A/E is used to monitor both pricing and reserving assumptions between full reviews.

**Basic limit** — The reference limit at which base rates are set. Higher limits are priced with increased limits factors.

**Catastrophe load** — A provision for expected catastrophe losses. It usually comes from a catastrophe model's AAL or long-term history, and it replaces the actual (volatile) catastrophe losses in the experience period.

**Complement of credibility** — The estimate given weight (1 − Z) when the experience is not fully credible. Examples: a trended prior indication, industry loss costs, or a larger related group's experience. A good complement is unbiased, independent of the experience, and readily available.

**Credibility** — The weight Z given to observed experience: estimate = Z × observed + (1 − Z) × complement. *Classical (limited fluctuation)* credibility sets a full-credibility standard. For claim frequency with 90% probability of being within ±5%, the standard is n_F = (1.645 / 0.05)² ≈ 1,082 claims, and partial credibility is Z = √(n / n_F). *Bühlmann* credibility uses Z = n / (n + k), with k = expected process variance ÷ variance of hypothetical means.

**Exposure development** — Adjusting reported exposure (and premium) for expected changes at audit, in lines where exposure is audited after expiration.

**Extension of exposures** — Re-rating every historical policy at current rates to put premium at current rate level. It is the most accurate on-level method, and it needs policy-level rating data.

**Fixed vs variable expenses** — Fixed expenses do not vary with premium (policy issuance, overhead) and are often expressed per policy or per exposure. Variable expenses are proportional to premium (commissions, premium taxes). Treating fixed expenses as variable overcharges large risks and undercharges small ones.

**Indicated rate change** — The change in rates needed for expected future premium to cover expected losses, LAE, expenses, and profit. Under the loss ratio method: indicated change = (projected loss & LAE ratio + F) ÷ (1 − V − Q) − 1, where F is the fixed expense ratio, V the variable expense ratio, and Q the profit and contingencies provision.

**Large-loss adjustment** — Capping individual losses at a threshold and replacing the capped amount with a long-run excess loss provision. This keeps random large losses from swinging the indication.

**Loss development (in pricing)** — Bringing experience-period losses to their estimated ultimate value using development factors. Pricing borrows the reserving machinery (section 4).

**Off-balance** — An adjustment to the base rate so that changes to rating relativities do not unintentionally change total premium.

**On-level premium** — Historical earned premium restated at the rates currently in effect, so that loss ratios from different years are comparable.
*CRE analogy:* marking in-place rents to current market rent to compare a property's history on a like-for-like basis.

**Parallelogram method** — An approximate on-level method that assumes policies are written evenly through the year. It calculates the share of each year's earned premium written at each historical rate level.

**Permissible loss ratio** — The loss and LAE ratio that current rates can support while still covering expenses and the target profit. When all expenses are variable, it equals 1 − V − Q.

**Profit and contingencies provision** — The underwriting profit margin built into rates. Its size should reflect expected investment income on the funds the business generates and the risk being taken.

**Pure premium method** — An indication method that produces a rate rather than a rate change: indicated average rate = (projected pure premium including LAE + fixed expense per exposure) ÷ (1 − V − Q).

**Rate adequacy** — Whether current rates are expected to cover losses, LAE, expenses, and the target profit for the period in which they will be used.

**Rate relativity** — The factor by which a segment's rate differs from the base, such as a territory factor or a class factor.

**Segmentation** — Dividing a book by rating characteristics to set relativities and find segments that are mispriced. Credibility limits how finely you can segment.

**Selected rate change** — The rate change actually recommended or filed. It reflects the indication plus judgment about credibility, the competitive market, retention, regulation, and how much change policyholders can absorb at once.

**Trend** — The annual rate of change in frequency, severity, or pure premium, usually fitted as exponential: ln(y) = a + b·t, so trend = e^b − 1. Frequency and severity trends are best measured separately because they have different causes.

**Trend period** — The time from the average accident date of the experience period to the average accident date of the period the rates will cover. For annual policies written evenly over the 12 months starting on date E, the average accident date is E + 12 months. For an accident-year experience period, it is mid-year.

---

## 4. Reserving

**Age-to-age factor (link ratio)** — Cumulative losses at age k+1 ÷ cumulative losses at age k for the same origin year. Several averages (simple, volume-weighted, latest-n, excluding high and low) are compared before a factor is selected.

**Berquist-Sherman adjustments** — Techniques that restate a triangle to a consistent basis when operations have changed. Paid triangles are adjusted for changes in settlement rate using disposal (closure) rates; reported triangles are adjusted for changes in case reserve adequacy by restating average case reserves.

**Bootstrap (ODP)** — A stochastic reserving method that resamples residuals from an over-dispersed Poisson model of incremental losses to simulate a distribution of unpaid losses.

**Bornhuetter-Ferguson (B-F)** — Ultimate = reported (or paid) to date + earned premium × a priori ELR × (1 − 1/CDF). It blends the chain ladder and the expected loss ratio method, with credibility on the emerged losses of Z = 1/CDF. It is stable for immature years because it does not leverage early emergence.

**Calendar-year (diagonal) effects** — Influences that hit every accident year at the same calendar time, such as an inflation shock, a legal change, a claims-practice or system change, or a one-time reserve review. They show up along diagonals and break the chain-ladder assumption that development depends only on age.

**Cape Cod (Stanard-Bühlmann)** — Like B-F, but the expected loss ratio is estimated from the data: ELR = Σ reported losses ÷ Σ (on-level earned premium × 1/CDF). The denominator is sometimes called "used-up premium."

**Carried vs indicated reserves** — Carried reserves are those booked on the balance sheet. Indicated reserves are the actuary's estimate. Management decides what is carried.

**Case reserve adequacy** — How close case reserves are, on average, to the eventual cost of the claims. Changes in adequacy over time distort reported (incurred) development.

**Chain ladder (development method)** — Ultimate = latest cumulative losses × CDF. It assumes future development will look like past development at the same ages. Applied to paid data, it is sensitive to changes in payment speed; applied to reported data, to changes in case reserve adequacy.

**Closure rate** — Closed claim count ÷ reported claim count (or ÷ ultimate count) at each age. It is a diagnostic for changes in settlement speed.

**Cumulative development factor (CDF, age-to-ultimate)** — The product of selected age-to-age factors from age k to ultimate, including the tail. 1/CDF is the expected share of ultimate reported (or paid) at age k.

**Development triangle** — A table of losses or counts with origin years (AY, PY, or report year) in rows and development ages in columns. Only the upper-left triangle is known. Each diagonal is one evaluation date.

**Diagnostics** — Ratios that test whether historical patterns still hold before you project with them: paid-to-reported ratios, closure rates, average case reserve per open claim, average paid per closed claim, and reported count development. Read them down the columns and along the diagonals.

**Expected loss ratio (ELR) method** — Ultimate = earned premium × a priori expected loss ratio. It ignores emerged losses, which makes it useful when the data is immature or unreliable and poor when the a priori is wrong.

**IBNER (incurred but not enough reported)** — Future development on claims already reported. Part of broad IBNR.

**Incurred (reported) triangle** — A triangle of cumulative paid + case losses. It responds faster than paid but depends on case reserving practice.

**Mack method** — A distribution-free way to estimate the standard error of chain-ladder reserves from the variability of the age-to-age factors.

**Paid triangle** — A triangle of cumulative paid losses. It does not depend on case reserves but is sensitive to payment speed and slow to respond in long-tailed lines.

**Paid-to-reported ratio** — Cumulative paid ÷ cumulative reported, by origin year and age. Movement along a diagonal can indicate a change in payment speed or in case reserve adequacy.

**Pure IBNR** — The reserve for claims that have happened but have not yet been reported.

**Reserve range** — A range of reasonable estimates of unpaid losses. It should be based on the assumptions that drive uncertainty, not an arbitrary ±%.

**Selected factor** — The age-to-age factor the actuary chooses after comparing averages and diagnostics. Each selection is a judgment and should be documented.

**Sensitivity analysis** — Re-estimating with one assumption changed (a tail factor, an a priori ELR, the averaging period) to show how much the answer depends on it.

**Settlement pattern** — The timing of claim closings and payments. A change in settlement speed distorts paid development.

**Statement of Actuarial Opinion (SAO)** — The appointed actuary's annual opinion on the reasonableness of an insurer's carried reserves, required in the US statutory filing.

**Tail factor** — Development expected beyond the oldest age in the triangle. It is selected from curve fits (exponential decay, inverse power), industry benchmarks, or the relationship between paid and reported at the oldest ages. Tail factors matter most for long-tailed lines.

**Ultimate loss** — The total cost of all claims for an origin period once every claim is settled. It is an estimate until then.

**Unpaid loss** — Ultimate − paid = case reserves + IBNR.

---

## 5. Reinsurance fundamentals

**Adjustable premium** — Reinsurance premium that is adjusted after the period on the basis of actual subject premium (rate × actual subject premium), or in some contracts on the basis of losses (swing-rated).

**Aggregate excess (aggregate XOL)** — Cover for the total of losses over a period (or from one class) above an aggregate retention, such as $20M xs $30M of annual aggregate losses. It protects against an accumulation of many moderate losses, not only single large ones.

**Attachment** — The retention point at which a reinsurance layer begins to pay. See *attachment point* (section 1) and *retention*.

**Broker (reinsurance intermediary)** — Represents the cedent: designs the program, prepares the submission, markets it to reinsurers, negotiates terms, and handles placement and claims collection.
*CRE analogy:* a capital-markets advisor placing a debt or equity raise.

**Brokerage** — The reinsurance broker's fee, usually a percentage of reinsurance premium. It is typically deducted from the premium the reinsurer receives.
*CRE analogy:* a debt-placement or investment-sales fee paid out of the transaction.

**Catastrophe excess of loss (cat XOL)** — Excess of loss cover for the total of losses from one catastrophe event across many risks, subject to an occurrence definition (hours clause). It protects the cedent's capital against accumulations from a single event.

**Cedent (ceding company)** — The insurer that buys reinsurance and transfers (cedes) part of its risk.
*CRE analogy:* the originating lender that sells participations.

**Ceding commission** — On proportional treaties, the commission the reinsurer pays the cedent, as a percentage of ceded premium, to reimburse acquisition costs and overhead.
*CRE analogy:* a lead lender keeping an origination or servicing fee out of a participant's share.
*Where it breaks:* ceding commissions are often variable (sliding scale) and tied to loss experience.

**Clash cover** — A casualty excess cover that attaches above the largest single policy limit (or above a per-policy excess layer). It responds only when one occurrence involves several policies, insureds, or coverages, or to losses in excess of policy limits.

**Excess of loss (XOL)** — Non-proportional reinsurance that pays the part of a loss above the retention (attachment), up to a limit. It can apply per risk, per occurrence, or in aggregate.
*CRE analogy:* a mezzanine tranche, which absorbs losses only after the junior position is wiped out, up to its own thickness.
*Where it breaks:* see *attachment point* (unfunded, priced annually, applies per event).

**Exhaustion point** — The top of a layer: attachment + limit. A $5M xs $5M layer exhausts at $10M; losses above that go back to the cedent or to higher layers.

**Facultative** — Reinsurance negotiated and underwritten for one risk at a time. It is used for risks outside treaty limits or appetite.
*CRE analogy:* syndicating one deal at a time, as opposed to a programmatic forward-flow agreement (a treaty).

**Gross, ceded, and net loss** — Gross loss is before reinsurance; ceded loss is the reinsurers' share; net loss = gross − ceded. They must reconcile for every claim and occurrence.

**Hours clause** — The part of an occurrence definition that sets the time window within which catastrophe losses count as one event. The window is commonly 72 hours for windstorm and longer for flood or earthquake; terms vary. The cedent usually chooses when the window starts.

**Layer** — A band of loss defined by an attachment and a limit, written "limit xs attachment" (for example, $5M xs $5M).

**Limit (reinsurance)** — The most a layer pays per occurrence (or per risk), and separately, if stated, in aggregate per year.

**Losses occurring during (LOD) vs risks attaching during (RAD)** — An LOD treaty covers losses that happen during the treaty period, whenever the policy incepted. A RAD treaty covers losses on policies that incept during the treaty period, whenever the loss happens, so its exposure can run for up to 24 months on annual policies.

**Minimum and deposit premium (MDP)** — A deposit premium paid in installments during the treaty year and adjusted at year-end to rate × actual subject premium. The final premium cannot fall below the stated minimum.
*CRE analogy:* estimated CAM charges paid monthly and reconciled to actual costs at year-end, with a floor.

**Non-proportional reinsurance** — Reinsurance in which the reinsurer's share depends on the size of the loss (excess of loss, stop loss), not on a fixed percentage.

**Occurrence definition** — Contract wording that decides which losses are combined into one occurrence. For catastrophes, it is the hours clause and peril definitions. For casualty, it is wording on continuous exposure and on aggregating claims from one cause. It can change ceded results materially.

**Per-risk excess of loss** — XOL that applies separately to the loss on each risk (each location or each policy). It protects against large individual losses, not catastrophe accumulations.

**Profit commission** — A share of the reinsurer's profit on the treaty, returned to the cedent. Profit is typically ceded premium − ceded losses − ceding commission − a reinsurer expense allowance, often with any deficit carried forward to later years.
*CRE analogy:* a promote, where the sponsor shares in profits above a threshold.

**Proportional reinsurance** — The reinsurer takes a fixed share of each risk's premium and losses (quota share, surplus share).

**Quota share (QS)** — Proportional reinsurance in which the reinsurer takes a fixed percentage of every policy's premium and losses in the covered book, usually paying a ceding commission. It provides capital relief and capacity, and it reduces net volatility proportionally.
*CRE analogy:* a pari passu participation, in which each participant shares income and losses pro rata.
*Where it breaks:* ceding commissions, sliding scales, and loss-ratio caps or corridors modify the strict pro-rata sharing.

**Rate on line (ROL)** — Reinsurance premium ÷ layer limit. A $600K premium for a $5M limit is a 12% ROL. Payback period = 1/ROL.

**Reinstatement** — Restoring a layer's limit after it has been used by a loss, so it is available for a later occurrence in the same period. "One reinstatement" means total available limit = 2 × the layer limit.
*CRE analogy:* replenishing a drawn letter of credit or a reserve account so the protection is available again.
*Where it breaks:* the cedent pays reinsurance premium again to restore cover, and the number of reinstatements is fixed in advance.

**Reinstatement premium** — The premium paid to reinstate a layer. Typically it is original premium × (loss to layer ÷ layer limit) × the reinstatement rate (for example, 100%), which is "pro rata as to amount." Some contracts also pro-rate for the time remaining in the period.

**Reinsurer** — The company that accepts risk from a cedent in exchange for premium.
*CRE analogy:* a participant or co-investor in a deal.

**Retention** — The part of each loss the cedent keeps before reinsurance responds. In an XOL layer, the retention is the attachment point.
*CRE analogy:* the sponsor's first-loss equity.

**Retrocession** — Reinsurance bought by reinsurers.

**Sliding-scale commission** — A ceding commission that moves inversely with the ceded loss ratio between a minimum and a maximum, for example 30% at a 60% loss ratio, sliding to 22% at 70% and above. The reinsurer shares profit with the cedent when results are good and gives up less when results are bad.
*CRE analogy:* a performance-based promote in a JV waterfall.

**Stop loss** — Aggregate cover expressed in loss-ratio terms, such as 20 loss-ratio points xs a 75% loss ratio. It is often capped in dollars and protects annual results against an accumulation of losses, whatever their cause.

**Subject premium** — The cedent's premium on the business covered by the treaty, to which the reinsurance rate is applied (for example, reinsurance premium = 4% × subject premium). Sometimes called GNPI (gross net premium income).
*CRE analogy:* percentage rent computed on tenant gross sales.

**Surplus share** — Proportional reinsurance in which the cedent keeps a fixed dollar "line" per risk and the reinsurer takes a multiple of it. Each risk is shared in the proportion that the ceded amount bears to its total insured value. With a $1M line and a 4-line surplus, a $3M risk is 2/3 ceded, in premium and in losses.

**Treaty** — A reinsurance agreement covering a defined class of business automatically, without underwriting each risk.
*CRE analogy:* a forward-flow or programmatic agreement.

---

## 6. Reinsurance mathematics and pricing

**Aggregate loss vs occurrence loss** — Occurrence loss is the total from one event (all claims sharing an occurrence). Aggregate loss is the total of all losses over a period, usually a year. Per-occurrence covers respond to each occurrence separately; aggregate covers respond to the annual total. The same year can be benign on one measure and severe on the other.

**As-if losses** — Historical losses restated as if they had happened under current conditions: trended to the prospective period, developed to ultimate, and run through the proposed reinsurance structure. Experience rating is done on an as-if basis, not on historical cessions.

**Attachment probability** — The probability that a loss reaches the layer. Per loss it is P(X > a). Per year, if ground-up losses follow a Poisson process with annual rate λ, P(at least one loss into the layer) = 1 − exp(−λ·S(a)).

**Burning cost** — Σ as-if (trended, developed) layer losses ÷ Σ on-level subject premium over the experience period. Multiply it by projected subject premium to get the experience-rated expected layer loss.

**Ceded loss ratio** — Ceded losses ÷ ceded (reinsurance) premium. It measures the reinsurer's result on the treaty.

**Compound distribution** — Aggregate loss S = X₁ + … + X_N, where N is a random count independent of the iid severities Xᵢ. E[S] = E[N]·E[X] and Var(S) = E[N]·Var(X) + Var(N)·E[X]². For compound Poisson, Var(S) = λ·E[X²].

**Cost of capital** — The return investors require on the capital held to support a risk. In pricing, the capital charge = capital allocated × (cost of capital − investment return earned on that capital). It is one way to set the risk load.

**Exhaustion probability** — The probability that a loss exceeds the top of the layer: P(X > a + l) per loss, or its annual equivalent.

**Expected ceded loss** — The mean of losses ceded to a structure over a year, reflecting limits, aggregate features, and reinstatements.

**Expected layer loss (layer LEV identity)** — For a layer of limit l above attachment a, layer loss per occurrence = min(max(X − a, 0), l). Its expectation is E[X ∧ (a + l)] − E[X ∧ a]. Multiply by expected occurrence count for the annual expectation (before aggregate features).

**Expense load** — The part of a reinsurance price that covers the reinsurer's internal expenses and the brokerage.

**Experience rating** — Estimating expected layer losses from the cedent's own history. Losses are trended, developed, put on an as-if basis, and adjusted for changes in exposure and rate level, then expressed as a burning cost and weighted by credibility.

**Exposure curve** — For property, the share of expected loss below a deductible expressed as a fraction d of the maximum possible loss M (often insured value): G(d) = E[X ∧ dM] ÷ E[X]. The share of expected loss in a layer from aM to bM is G(b) − G(a). The MBBEFD family (Bernegger, 1997) parameterizes these curves with c. The Swiss Re curves correspond to c = 1.5, 2.0, 3.0, 4.0, and c = 5.0 is often associated with the Lloyd's industrial curve; higher c means losses are concentrated in smaller damage ratios.

**Exposure rating** — Estimating expected layer losses from the current exposure profile and a severity curve rather than from loss history. Expected losses for each policy or band (premium × expected loss ratio) are allocated to the layer using ILFs (casualty) or exposure curves (property).

**Increased limits factor (ILF)** — The ratio of expected loss at limit L to expected loss at the basic limit B: ILF(L) = E[X ∧ L] ÷ E[X ∧ B] (published tables may also include ALAE and a risk load). For a policy with limit P, the share of its expected loss falling in a layer from a to a+l is [ILF(min(P, a+l)) − ILF(min(P, a))] ÷ ILF(P).

**Limited expected value (LEV)** — E[X ∧ u] = E[min(X, u)] = ∫₀ᵘ S(x) dx for a non-negative loss X. It is the expected loss to a policy with limit u, and it is the building block for ILFs and layer pricing.

**Loss cost (reinsurance)** — Expected ceded loss, often expressed as a percentage of subject premium or as a rate on line.

**Monte Carlo simulation** — Estimating a distribution by repeated random sampling: simulate claim counts and severities, apply the treaty terms year by year, and summarize. It is needed when aggregate limits, reinstatements, or combinations of covers make closed-form answers impractical.

**Payback period** — Limit ÷ premium = 1/ROL: the number of years of premium needed to pay for one full-limit loss. Reinsurers compare it with the return period of a full-limit loss.

**Policy profile (limits profile)** — The distribution of policies and premium by limit band (casualty) or insured-value band (property). It is the main input to exposure rating.

**Quoted premium** — The price offered in the market. It reflects the technical premium plus market conditions: capacity, competition, relationship, payback expectations, and minimum rates on line.

**Retained loss** — Gross loss − ceded loss, i.e., what the cedent keeps.

**Risk load** — The margin above expected loss that compensates for uncertainty and the capital a reinsurer must hold. Common methods are a percentage of the standard deviation, a percentage of the variance, or a cost-of-capital charge. Higher, thinner, more volatile layers carry larger risk loads relative to expected loss.

**Severity curve** — The size-of-loss distribution used to allocate expected losses across layers. For example, a lognormal or Pareto fitted to large losses, or an industry curve behind an ILF table.

**Target return** — The return on allocated capital that the reinsurer (or cedent) requires. It drives the capital component of the price.

**Technical premium** — The premium that covers expected loss, expenses (internal and brokerage), and a risk or capital margin. One common convention is (expected loss + risk load) ÷ (1 − brokerage − internal expense ratio). Conventions differ, so state the formula.

---

## 7. Catastrophe and portfolio analytics

**AAL (average annual loss)** — Expected annual catastrophe loss. From an ELT with Poisson occurrence, AAL = Σ (annual rateᵢ × mean lossᵢ). From a YLT, it is the average of total annual loss across simulated years. It is the basis of catastrophe loads in pricing.

**Accumulation** — The build-up of exposure that a single event can hit: many locations in one region, or many policies exposed to one cause.

**AEP (aggregate exceedance probability)** — The probability that total catastrophe loss in a year exceeds x. AEP(x) ≥ OEP(x) for every x, because the annual total is at least as large as the largest single event.

**Catastrophe model** — Software that estimates the distribution of catastrophe losses for a portfolio. It has four modules: hazard (event frequency and intensity at each location), vulnerability (damage as a function of intensity), exposure (locations, values, construction, occupancy), and financial (deductibles, limits, reinsurance).

**Concentration** — A large share of exposure in a small area or a single risk factor. Concentration raises tail risk without raising expected loss proportionally.

**Diversification** — The reduction in relative volatility from combining risks that are not perfectly correlated. A diversified portfolio's tail is less than the sum of its parts' tails.
*CRE analogy:* geographic and property-type diversification in a real estate portfolio.
*Where it breaks:* catastrophes and inflation can correlate risks that look independent in normal years.

**ELT (event loss table)** — One row per stochastic event with annual rate, mean loss, standard deviations (independent and correlated components of secondary uncertainty), and exposure value. It is compact, but it loses the sequencing of events within a year.

**Event set (stochastic catalog)** — A large set of simulated events, each with an annual rate, representing the range of catastrophes that could plausibly occur, including ones bigger than any in history.

**Exceedance probability (EP) curve** — A plot of the annual probability that loss exceeds each level. OEP and AEP are the two standard versions.

**Exposure (catastrophe modeling)** — The insured properties and their attributes as entered into the model: location, values, construction, occupancy, year built, deductibles. Errors in exposure data are a leading source of model error.

**Hazard** — The physical phenomenon and its intensity at a site: wind speed, hail size, flood depth, ground motion.

**Model uncertainty** — Uncertainty from a model's structure and assumptions, visible in material differences between vendor models for the same portfolio.

**Modeled loss** — Loss estimated by a catastrophe model, as opposed to historical (actual) loss. Modeled losses depend on the exposure data, the event set, and the vulnerability assumptions.

**OEP (occurrence exceedance probability)** — The probability that the largest single-event loss in a year exceeds x. It is the relevant metric for per-occurrence catastrophe XOL. With Poisson events, OEP(x) = 1 − exp(−Σ λᵢ·P(Lᵢ > x)).

**PML (probable maximum loss)** — Loosely, the loss at a stated return period (for example, the 1-in-250 OEP). The term is used inconsistently, so always state the return period, OEP or AEP, peril, gross or net, and the model used.

**Primary uncertainty** — Uncertainty about which events occur, how many, where, and how intense they are.

**Return period** — 1 ÷ annual exceedance probability. A 1-in-100 loss has a 1% chance of being exceeded in any year. It does not mean the loss happens once a century; over 30 years, the probability of at least one exceedance is about 26%.

**Secondary uncertainty** — Uncertainty in the loss given that an event occurs, mainly variability of the damage ratio for a given intensity. Ignoring it understates tail losses.

**TVaR (tail value at risk)** — The expected loss given that loss exceeds the VaR at level p: TVaR_p = E[X | X > VaR_p] for continuous distributions. Unlike VaR, it reflects how bad the tail is and is subadditive. Also called CTE (conditional tail expectation).

**VaR (value at risk)** — The p-th quantile of the loss distribution, such as the 99th percentile annual loss (equal to the 1-in-100 AEP for annual aggregate loss). It says nothing about losses beyond it and is not additive across portfolios.

**Vulnerability** — The relationship between hazard intensity and damage ratio for a type of building (construction, occupancy, age, height).

**YLT (year loss table)** — A simulation of many years, each listing the events that occur, their timing, and sampled losses (including secondary uncertainty). It keeps the sequence of events within each year, which aggregate covers and reinstatements require.

---

## 8. Casualty analytics

**Attachment erosion (leveraged trend)** — When ground-up severity rises and an attachment stays fixed, losses in an excess layer grow faster than ground-up losses. More claims pierce the attachment, and those that do pierce it by more. How strong the leverage is depends on the shape of the severity curve. Indexation (stability) clauses, which index the retention to inflation, are one market response.

**Claims-made vs occurrence** — An occurrence policy covers injury or damage that happens during the policy period, whenever the claim is made. A claims-made policy covers claims first made (often also reported) during the policy period for incidents after a retroactive date. Claims-made coverage shortens the insurer's tail because it largely eliminates pure IBNR beyond the reporting period, but it does not eliminate development on known claims. An extended reporting period ("tail") can be bought when a claims-made policy ends.

**Commercial auto** — Liability (bodily injury and property damage to others) for vehicles used in business, plus physical damage to the insured's own vehicles. The usual exposure base is vehicles or power units. Liability is medium-tailed, and its severity is driven by medical costs and litigation.

**Employers' liability** — Part Two of a workers' compensation policy. It covers the employer's liability for employee injuries outside the statutory benefit system (for example, third-party-over actions), subject to stated limits.

**Excess casualty** — Umbrella and excess liability policies above primary auto, general liability, and employers' liability limits. They are low-frequency and high-severity, report slowly, and are very sensitive to severity trend.

**General liability (GL)** — Liability for third-party bodily injury and property damage arising from premises, operations, products, and completed operations, plus personal and advertising injury. It is usually written on an occurrence form with a per-occurrence limit and a general aggregate (for example, $1M/$2M). Exposure bases include sales, payroll, and area.

**Limits profile** — See *policy profile* (section 6). In casualty it decides how much of the book can reach a given reinsurance layer.

**Long-tailed vs short-tailed lines** — In short-tailed lines (property, auto physical damage), most losses are reported and paid within a year or two. In long-tailed lines (general liability, workers' compensation, professional liability, excess casualty), reporting and settlement take many years. Long tails mean more IBNR, more float, more reserve uncertainty, and more exposure to inflation.

**Occurrence form** — See *claims-made vs occurrence*.

**Professional liability** — Coverage for negligence in professional services: errors and omissions, medical malpractice, lawyers' professional liability, and, in a broader sense, directors and officers. It is usually claims-made, severity-heavy, and long-tailed.

**Retroactive date** — Under a claims-made policy, the date before which incidents are not covered, even if the claim is made during the policy period.

**Severity trend (casualty)** — The annual rate of change in average claim cost. It is driven by medical and wage inflation and by legal and social factors. It is the single most important pricing assumption for excess casualty layers because of the leverage effect.

**Social inflation** — Growth in liability claim costs above general economic inflation, driven by litigation and social factors. These include more attorney involvement, larger jury verdicts (very large awards are sometimes called "nuclear verdicts"), third-party litigation funding, broader liability theories, and plaintiff-friendly jurisdictions. It is hard to measure directly and tends to show up as a severity trend that past data understates.

**Workers' compensation (WC)** — Covers statutory benefits for work-related injury and illness: medical care, wage replacement (indemnity), rehabilitation, and death benefits. Part One has no policy limit, and Part Two (employers' liability) has stated limits. Benefits are set by each state. Coverage is compulsory in most states, but Texas lets most private employers opt out ("non-subscribers"). The exposure base is payroll per $100, audited after expiration. The tail is long because of lifetime medical and permanent disability benefits.

---

## 9. Statistics and predictive modeling

**AIC (Akaike information criterion)** — 2k − 2 ln L, where k is the number of parameters and L the maximized likelihood. It compares models on the same data and penalizes extra parameters; lower is better.

**Calibration** — Whether predicted values match actual outcomes overall and across prediction bands (actual ÷ expected ≈ 1 in each band). A model can rank risks well and still be miscalibrated.

**Confidence interval** — A range built so that, over repeated samples, a stated share of such ranges (for example, 95%) contains the true parameter. It is not a statement that the parameter has a 95% probability of lying in this particular interval.

**Correlation** — A measure of linear association between two variables (Pearson) or of monotonic association (Spearman, Kendall). Correlation in normal years can differ from dependence in the tail.

**Cross-validation** — Repeatedly fitting on part of the data and testing on the held-out part (k-fold) to estimate out-of-sample performance and tune model complexity.

**Deviance** — Twice the difference in log-likelihood between a saturated model and the fitted model. It is used to compare nested GLMs (a drop-in-deviance test) and to define deviance residuals.

**Exploratory data analysis (EDA)** — Profiling, plotting, and summarizing data before modeling, to find errors, distributions, relationships, and candidate variables. In insurance, EDA is always done on an exposure-weighted basis.

**Exposure offset** — A term ln(exposure) with a fixed coefficient of 1 in a log-link frequency GLM, so the model predicts claims per unit of exposure.

**Gamma distribution (in GLMs)** — Used for claim severity. Variance is proportional to the mean squared (a constant coefficient of variation), usually with a log link.

**Generalized linear model (GLM)** — g(E[Y]) = Xβ, with Y from an exponential-family distribution and g a link function. With a log link, coefficients turn into multiplicative rating relativities, which is why GLMs are standard in pricing.

**Hypothesis test** — A procedure for deciding whether data is consistent with a null hypothesis at a stated significance level. Type I error means rejecting a true null; Type II error means failing to reject a false one.

**Interaction** — When the effect of one variable depends on the level of another (for example, territory effects that differ by class). It is modeled with product terms.

**Lift** — How well a model separates low-risk from high-risk business, usually shown by sorting on predicted value into bands and plotting actual results per band. A *double lift chart* compares two models by sorting on the ratio of their predictions.

**Link function** — The function g connecting the mean of the response to the linear predictor. Common choices are log (multiplicative effects), logit (probabilities), and identity.

**Logistic regression** — A GLM for binary outcomes with a logit link: ln(p ÷ (1 − p)) = Xβ.

**Model validation** — Testing whether a model is fit for its purpose before relying on it. This covers out-of-sample performance, stability over time, calibration, lift, the plausibility and stability of the coefficients, and a review of the data and code. Validation includes asking whether the model answers the business question, not only whether it fits.

**Negative binomial** — A count distribution with variance greater than the mean (overdispersion). It is used for frequency when the Poisson variance assumption fails.

**Overfitting** — A model that fits noise in the training data and performs worse on new data. Prevent it with holdout testing, cross-validation, regularization, and judgment about which effects are plausible.

**p-value** — The probability, if the null hypothesis is true, of seeing a result at least as extreme as the one observed. It is not the probability that the null is true.

**Poisson distribution** — A count distribution with variance equal to the mean. It is the standard starting point for claim frequency, usually with a log link and an exposure offset.

**Regression** — Modeling a response as a function of predictors. Ordinary least squares assumes constant variance and normal errors, which insurance losses rarely satisfy; hence GLMs.

**Regularization** — Penalizing coefficient size (lasso, ridge, elastic net) to reduce overfitting and perform variable selection.

**Residual** — Actual minus fitted, often standardized (Pearson or deviance residuals). Residual plots against fitted values and predictors reveal misspecification.

**Sampling** — Selecting a subset of data for analysis. In insurance, the main concerns are sampling bias (for example, using only closed claims) and changes over time in which policies or claims are in the data.

**Train/test split** — Holding out part of the data, often a later time period in insurance, to test a model fitted on the rest.

**Tweedie distribution** — A compound Poisson-gamma distribution with power parameter 1 < p < 2. Variance is proportional to μ^p, and there is a point mass at zero. It is used to model pure premium directly.

**Variable selection** — Choosing which predictors to include, using statistical evidence (deviance tests, AIC, regularization) together with business sense (whether the variable is plausible, stable, legal to use, and available at quote).

---

## 10. Insurer financial analysis

**AM Best** — A credit rating agency specializing in insurers. It publishes Financial Strength Ratings, the Best's Capital Adequacy Ratio (BCAR), and industry financial data (for example, *Best's Aggregates & Averages*). Commercial buyers and lenders often require an insurer rated A- or better, so the rating constrains how much business an insurer can write.

**Business mix** — The composition of a portfolio by line, class, territory, limit, and similar characteristics. Changes in mix alter average loss costs and average premium even when rates are unchanged, so they must be separated from trend and rate change in any performance analysis.

**Exposure change** — The change in insured units (vehicles, payroll, insured value) from one period to the next, as distinct from changes in price.

**Float** — Funds an insurer holds between collecting premium and paying claims, which it invests. Long-tailed lines generate more float per dollar of premium.
*CRE analogy:* tenant security deposits and prepaid rents held and invested until they must be returned or applied.
*Where it breaks:* the amount eventually owed is uncertain, and the "cost" of float is the underwriting result, which can be positive (an underwriting profit means the float cost less than nothing) or negative.

**Investment income** — Net investment income earned on the assets backing reserves, unearned premium, and surplus. Realized capital gains are reported separately.

**Loss reserves (balance sheet)** — Case reserves + IBNR for losses and LAE. They are usually the largest liability on a P&C insurer's balance sheet, so reserve estimation errors flow directly into surplus.

**NAIC Annual Statement** — The standardized statutory financial filing that US insurers submit to state regulators. It includes the balance sheet, income statement, underwriting and investment exhibits, and Schedule P.

**Operating ratio** — Combined ratio − net investment income ratio (investment income ÷ earned premium). It measures overall operating profitability before capital gains and taxes.

**Policyholder surplus** — Statutory assets − statutory liabilities: the insurer's capital cushion.
*CRE analogy:* the equity in a capital stack.
*Where it breaks:* statutory surplus excludes non-admitted assets and uses conservative valuation, and regulators set minimum levels through risk-based capital.

**Premium growth** — The change in written premium. It splits into rate change, exposure change, retention and new business, and mix. Growth with no rate is a warning sign in a hardening market.

**Premium-to-surplus ratio** — Net written premium ÷ policyholder surplus, a measure of operating leverage. Regulatory screening ratios flag high values (the NAIC IRIS test uses 300% for net written premium to surplus).

**Prior-year development (PYD)** — The change during a calendar year in estimated ultimate losses for earlier accident years. It is adverse when estimates rise, which reduces current earnings, and favorable when they fall. It appears in Schedule P and in GAAP claims-development disclosures and is a primary signal of past reserve adequacy.
*CRE analogy:* prior-period true-ups of estimated expense or tax accruals that hit current-year income.

**Rate change** — The change in price for the same exposure and coverage. Filed or approved rate change differs from achieved (written) rate change, which reflects the actual mix of renewals, schedule credits, and debits.

**Renewal retention** — The share of expiring policies (or premium) that renew. Rate increases usually reduce retention, so rate and retention are monitored together.

**Reserve changes** — The change in loss and LAE reserves during a period. Calendar-year incurred = paid + change in reserves. Reserve changes on prior accident years are prior-year development.

**Risk-based capital (RBC)** — The NAIC formula for minimum capital, based on asset, credit, reserve, and premium risk. The ratio of total adjusted capital to authorized-control-level RBC triggers regulatory action at 200% (company action level), 150%, 100%, and 70%.

**Schedule P** — The part of the NAIC Annual Statement that gives 10 years of loss and LAE history by line, largely net of reinsurance: Part 1 (summary by accident year), Part 2 (incurred loss and DCC triangles), Part 3 (paid loss and DCC triangles), Part 4 (bulk and IBNR reserves), Part 5 (claim counts, for certain lines), and Part 6 (earned premium, for certain lines). It is "the triangle in the annual statement" and a public source for peer and industry benchmarking.

**Statutory vs GAAP accounting** — Statutory accounting (SAP, set by the NAIC for regulators) focuses on solvency. Acquisition costs are expensed immediately, some assets are non-admitted, and bonds are mostly carried at amortized cost; the result is policyholder surplus. GAAP (for investors) matches revenue and expense. Acquisition costs are deferred (DAC) and amortized, and the result is shareholders' equity. US P&C loss reserves are generally undiscounted under both, with limited exceptions.

**Underwriting income** — See *underwriting profit* (section 1).
