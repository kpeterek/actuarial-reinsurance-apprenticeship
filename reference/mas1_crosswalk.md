# MAS-I Crosswalk

This file links exam material to the work it supports. Each row is a probability or statistics idea, the module that uses it, a concrete task in the Kettlerock data, and why a business decision depends on it. Teaching sessions cite this file when a concept has a MAS-I connection (spec §35) and append new connections at the bottom.

**Syllabus home.** CAS reorganizes exam content periodically. The column below reflects the 2026 MAS-I content outline as understood at build time: Domain A (Probability Models: stochastic processes, survival models, simulation), Domain B (Statistics: estimation, testing, frequency/severity/aggregate loss models, censoring and truncation), and Domain C (Extended Linear Models). Some rows sit mainly on MAS-II (credibility, time series, Bayesian methods) or in CAS Exam 5/8/9 readings. They are kept because they build directly on MAS-I machinery and the spec asks for them. **Check the current outline at casact.org before relying on this column for exam planning.**

---

## 1. Seed pairs from the spec (§35)

| MAS-I topic | Syllabus home | Module | Concrete Kettlerock application | Why it matters to the business |
|---|---|---|---|---|
| Compound Poisson | MAS-I A/B | 04, 08, 09 | Annual aggregate casualty losses above $1M modeled as a Poisson count of large occurrences × a fitted severity; the annual aggregate CA loss ratio distribution needed to evaluate an aggregate stop loss | Aggregate covers, capital, and earnings volatility depend on the whole annual distribution, not just its mean |
| Limited expected value | MAS-I A | 04, 05, 08 | ILFs from $1M to $5M for CA and GL; expected loss in a casualty layer = E[X ∧ (a + l)] − E[X ∧ a] | Every limit and every reinsurance layer is priced from LEVs; a wrong severity tail misprices all of them |
| Conditional expectation | MAS-I A/B | 04, 08 | Mean excess loss e(d) = E[X − d \| X > d] for large casualty claims; expected severity of claims that pierce a layer | Drives large-loss loads in pricing and the severity assumption in excess-layer pricing |
| Credibility | MAS-II; Exam 5 | 05, 08 | How much weight a state or class's experience gets in the rate indication; weighting experience rating against exposure rating for a reinsurance layer | Decides how far rates move toward a segment's own experience, and how far a treaty price moves toward the cedent's history |
| GLMs | MAS-I C | 11 | Poisson frequency and gamma severity GLMs for commercial auto with class, territory, limit, and state | Rating relativities and segmentation; finding segments the aggregate indication misprices |
| Survival models | MAS-I A (survival); B (censoring) | 02, 06 | Report-lag and time-to-close distributions; open claims are right-censored observations of settlement time | Report lag drives pure IBNR; settlement time drives paid development and the timing of cash flows |
| Monte Carlo simulation | MAS-I A | 08, 09, 10 | Simulating 10,000+ years of casualty large losses to price layers with reinstatements and aggregate limits; applying cat XOL terms to the year loss table | Treaty features and portfolio metrics (tail loss, capital) have no practical closed form |

## 2. Extended crosswalk by MAS-I area

### Probability models and stochastic processes (Domain A)

| MAS-I topic | Syllabus home | Module | Concrete Kettlerock application | Why it matters to the business |
|---|---|---|---|---|
| Homogeneous Poisson process; thinning | MAS-I A | 04, 08 | If ground-up claims arrive at rate λ, claims exceeding attachment a arrive at rate λ·S(a); annual attachment probability 1 − e^(−λ·S(a)) | Attachment and exhaustion probabilities are the first numbers a reinsurer asks for |
| Nonhomogeneous Poisson process | MAS-I A | 04, 10 | Seasonal timing of convective storm events in the year loss table (`day_of_year`); claim arrivals growing with exposure | Seasonality matters for reinstatement timing and for interim financial results |
| Splitting a Poisson process | MAS-I A | 04, 10 | Separating catastrophe and non-catastrophe claims, or perils, into independent Poisson streams | Allows cat and attritional losses to be modeled and priced separately, then recombined |
| Hazard rate | MAS-I A | 04, 06 | Hazard of claim closure by age; heavy-tailed severities have decreasing hazard rates | Explains why old open claims are often the largest, and why tail factors matter |
| Markov chains | MAS-I A | 06 | Annual transitions of claims between open and closed states by development year; expected time a claim remains open | Settlement dynamics feed paid development and claim-count projections |
| Life contingencies (annuities) | MAS-I A | 06 | Workers' compensation permanent-disability indemnity and lifetime medical payments behave like life annuities | Long WC tails and their sensitivity to mortality and medical inflation |
| Simulation by inversion | MAS-I A | 08, 10 | Drawing lognormal or Pareto severities via F⁻¹(U); re-sampling secondary uncertainty for catastrophe events | Underlies every pricing simulation in Modules 08–10 and Capstones 3–4 |

### Loss models and estimation (Domain B)

| MAS-I topic | Syllabus home | Module | Concrete Kettlerock application | Why it matters to the business |
|---|---|---|---|---|
| Frequency models (Poisson, negative binomial, binomial) | MAS-I B | 04, 08, 11 | Claim counts by line and year; overdispersion in large-loss counts | The count distribution drives volatility of aggregate and layer losses |
| Severity distributions (lognormal, gamma, Pareto, Weibull) | MAS-I B | 04, 08 | Fitting casualty severities; comparing tails; selecting a curve for excess layers | The severity tail is the main driver of excess-layer cost and of disagreement between pricing methods |
| Coverage modifications (deductibles, limits; per-loss vs per-payment) | MAS-I A/B | 04, 07 | Effect of property AOP deductibles on frequency and severity; per-payment severity vs per-loss severity | Deductible and limit changes alter frequency, severity, and loss cost in predictable ways that must be priced |
| Aggregate loss models (moments, approximations, simulation) | MAS-I B | 04, 08, 09 | Distribution of annual CA losses for an aggregate stop loss; normal vs lognormal approximations vs simulation | Aggregate covers and capital need the right tail, which normal approximations understate |
| MLE with censoring and truncation | MAS-I B | 04, 08 | Claims capped at policy limits are right-censored; claims below a deductible are left-truncated; fitting a severity curve correctly to Kettlerock large losses | Ignoring censoring understates the tail and underprices high layers |
| Point estimation properties (bias, consistency, efficiency) | MAS-I B | 04, 05 | Retransformation bias: the mean of a lognormal is exp(μ + σ²/2), not exp(μ); small-sample trend estimates from ten accident years | Biased estimators flow straight into indications and layer prices |
| Order statistics | MAS-I B | 08, 10 | OEP is the distribution of the largest event loss in a year; the largest single casualty occurrence in a year | Per-occurrence covers respond to the maximum, not the sum |
| Hypothesis testing (Type I/II error) | MAS-I B | 04, 11 | Testing whether a segment's frequency differs from the book average by more than Poisson noise before acting on it | Prevents rate actions driven by noise, and prevents missing real signals |
| Confidence intervals | MAS-I B | 04, 05 | Interval around a fitted trend rate; interval around a segment loss ratio | Communicates how much the indication could move; supports ranges in memos |
| Extreme value ideas (Pareto tails, mean excess plots) | Related; not core MAS-I | 08, 10 | Mean excess plot of large casualty losses to choose between lognormal and Pareto for the upper layer | High layers and catastrophe tails are priced from the shape of the extreme tail, where data is thinnest |

### Extended linear models (Domain C)

| MAS-I topic | Syllabus home | Module | Concrete Kettlerock application | Why it matters to the business |
|---|---|---|---|---|
| Ordinary least squares | MAS-I C | 04, 05 | Log-linear trend fits of frequency and severity by accident year | Trend is often the most consequential pricing assumption |
| GLM family and link selection | MAS-I C | 11 | Poisson/log for frequency, gamma/log for severity, Tweedie for pure premium | Wrong variance assumptions mis-weight segments and distort relativities |
| Offsets and weights | MAS-I C | 11 | ln(earned exposure) offset in CA frequency models; claim-count weights in severity models | Without an offset, the model confuses size of risk with riskiness |
| Categorical and ordinal predictors; interactions | MAS-I C | 11 | Territory and class as categorical; limit as ordinal; class × territory interaction | Determines whether rating factors stack multiplicatively or need interaction terms |
| Deviance, AIC/BIC, model comparison | MAS-I C | 11 | Comparing nested frequency models; deciding whether a variable earns its place | Parsimonious models are more stable when filed and used for years |
| Diagnostics and residuals | MAS-I C | 11 | Deviance residuals by predicted band; actual vs expected by segment | Finds misspecification before it reaches rates |
| Logistic regression / classification | MAS-I C | 11 | Probability that a newly reported claim will exceed a large-loss threshold | Claims triage, early large-loss identification, reserving input |
| Regularization, cross-validation, tree methods | MAS-I C (verify current outline) | 11 | Lasso for variable selection among many territory and class dummies; k-fold validation of a frequency model | Controls overfitting; common in pricing teams' workflow |

### Topics mainly outside MAS-I that build on it

| Topic | Syllabus home | Module | Concrete Kettlerock application | Why it matters to the business |
|---|---|---|---|---|
| Bühlmann and Bayesian credibility | MAS-II | 05, 06, 08 | B-F and Cape Cod as credibility blends (Z = 1/CDF); experience vs exposure rating blend | Formalizes how much to trust immature or thin data |
| Time series (trend, autocorrelation, ARIMA) | MAS-II | 04, 05 | Residual autocorrelation in annual trend fits; external indices (medical CPI) as trend benchmarks | Trend projections that ignore autocorrelation overstate confidence |
| Dependence and copulas | Beyond syllabus | 10 | Combining catastrophe, casualty, and attritional results in Capstone 4 | Tail metrics and capital depend heavily on dependence assumptions |

---

## Sessions append here

Add one row whenever a teaching session makes a MAS-I connection that is not already above, or uses an existing one in a new way. Keep entries short.

| Date | Module / concept | MAS-I topic | Application used | Notes |
|---|---|---|---|---|
| | | | | |
