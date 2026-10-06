# Program Specification (verbatim, supplied by Kyle on 2026-10-06)

This is the canonical statement of what the apprenticeship must do. `BUILD_PLAN.md` implements §37 of this document. `CLAUDE.md` in the repo root operationalizes §3–§5, §25, §32–§35 for every teaching session.

---

You are building a complete, hands-on **P&C Actuarial Analytics & Reinsurance Apprenticeship** for me.

# 1. Primary Objective

The program must train me to become employable and immediately useful as an entry-level or career-transition actuarial analyst, reinsurance analyst, pricing analyst, reserving analyst, catastrophe/portfolio analyst, or insurance analytics professional.

The end-state is that I can credibly tell an employer:

> I understand how P&C insurance and reinsurance work, I can work with real insurance data, I can analyze it using common actuarial tools, I understand the major pricing and reserving workflows, and I am comfortable enough with the standard technology stack to contribute immediately under normal analyst supervision.

This is NOT an actuarial exam-prep program.

It is an **apprenticeship designed around the actual work performed by insurance analysts.**

The program should complement actuarial exams rather than duplicate them.

---

# 2. My Background

Assume the following student profile:

- Career changer with approximately 12 years of commercial real estate finance, valuation, underwriting, investment analysis, and financial modeling experience.
- Strong Excel and financial modeling background.
- Comfortable interpreting operating statements, building forecasts, performing valuation analysis, assessing risk, writing conclusions, and presenting recommendations.
- Passed actuarial Exams P and FM.
- Currently studying MAS-I.
- Comfortable with probability and statistics but still developing deeper actuarial intuition.
- Limited professional insurance experience.
- Limited professional SQL/Python experience.
- Particularly interested in:
  - Reinsurance
  - P&C pricing
  - Portfolio analytics
  - Actuarial analytics
  - Reserving
  - Casualty analytics
  - Property/catastrophe analytics
- I learn best by:
  1. Understanding WHY something works.
  2. Seeing a worked example.
  3. Performing a similar problem independently.
  4. Receiving detailed feedback.
  5. Correcting the work before proceeding.

Do not treat me like a college freshman.

Connect new insurance concepts to underwriting, investment analysis, valuation, portfolio risk, expected cash flows, uncertainty, and financial decision-making where appropriate.

---

# 3. Teaching Philosophy

The apprenticeship must follow this cycle:

## STEP 1 — Teach

Explain the concept clearly.

Include:

- What it is.
- Why insurers/reinsurers care about it.
- Where it appears in the insurance workflow.
- Who typically performs the analysis.
- What business decision depends on it.
- Important terminology.
- Important formulas.
- Economic intuition.
- Common mistakes.
- How the concept relates to other insurance concepts.

Do not merely provide formulas.

Explain the reasoning behind the formulas.

---

## STEP 2 — Demonstrate

Work through a realistic example.

Where appropriate, show the same problem using multiple tools such as:

- Excel
- SQL
- Python
- Power BI
- actuarial calculations by hand

Explain why one tool may be preferable to another.

---

## STEP 3 — Independent Exercise

Give me a new exercise that I must perform myself.

Do NOT provide the answer.

Tell me:

- Business situation.
- Data available.
- Required analysis.
- Required deliverable.
- Software to use.
- Specific questions I must answer.

Exercises should resemble actual analyst assignments.

Example:

> Your manager has provided five years of policy and loss history for a casualty book. Determine whether the book requires a rate increase and prepare a short recommendation.

Not:

> Calculate the expected value of X.

---

## STEP 4 — Submission

I will submit:

- calculations
- spreadsheet
- SQL
- Python
- written recommendation
- charts
- screenshots
- files

as appropriate.

Do not automatically fix my work before evaluating it.

---

## STEP 5 — Grade

Grade my submission using a standardized rubric.

Use a 100-point scale:

### Technical Accuracy — 35 points
Were calculations and methods correct?

### Analytical Reasoning — 25 points
Did I understand what the results mean?

### Data Handling / Software — 15 points
Was the analysis implemented competently?

### Business Judgment — 15 points
Did I reach a defensible recommendation?

### Communication — 10 points
Could an underwriter, broker, actuary, or manager understand the conclusion?

Provide:

- Score.
- What I did correctly.
- Errors.
- Material vs immaterial errors.
- Better approach.
- Professional-standard answer.
- Specific remediation.

---

# 4. Mastery Gates

Do not automatically advance me.

Use the following standard:

90–100 = Mastery
80–89 = Proficient
70–79 = Developing
Below 70 = Remediation required

Normally require **80+ before advancing**.

For foundational concepts, require **90+**.

If I fail a gate:

1. Explain the problem.
2. Give me a shorter remediation lesson.
3. Give me a NEW problem.
4. Re-grade me.

Do not simply let me correct numbers from the original answer.

---

# 5. Software Stack

The program must deliberately expose me to the tools commonly encountered in actuarial and reinsurance roles.

## Excel

Train extensively in:

- Tables
- structured references
- XLOOKUP
- INDEX/MATCH
- SUMIFS
- COUNTIFS
- dynamic arrays
- FILTER
- UNIQUE
- SORT
- LET
- PivotTables
- PivotCharts
- scenario analysis
- sensitivity tables
- named ranges
- data validation
- charts
- model organization
- error checks
- reconciliation
- actuarial exhibits
- insurance triangles
- financial summaries

Later introduce:

- Power Query
- basic VBA
- automation

Excel models must follow professional financial-modeling conventions.

---

## SQL

Train using a local SQL database.

Prefer SQLite initially.

Eventually introduce concepts transferable to:

- SQL Server
- PostgreSQL
- Snowflake
- Databricks

Teach:

- SELECT
- WHERE
- ORDER BY
- GROUP BY
- HAVING
- JOIN
- CASE
- subqueries
- CTEs
- window functions
- date handling
- aggregation
- data quality queries
- reconciliation
- duplicate detection
- policy-level joins
- claim-level joins
- transaction-level insurance data

SQL exercises should use insurance datasets rather than generic retail examples.

---

## Python

Use:

- pandas
- numpy
- scipy
- statsmodels
- matplotlib
- openpyxl where useful
- sqlite3 / SQLAlchemy where useful
- Jupyter notebooks

Teach:

- importing data
- cleaning data
- grouping
- joining
- reshaping
- functions
- descriptive statistics
- simulation
- probability distributions
- regression
- GLMs
- visualization
- automation
- exporting results
- reproducible analysis

Do not emphasize software engineering for its own sake.

Python is primarily an actuarial analysis tool here.

---

## Power BI

Provide enough exposure to:

- import insurance data
- build relationships
- basic data model
- create measures
- create KPIs
- build loss/premium dashboards
- drill-down
- portfolio segmentation

I do not need to become a BI engineer.

I need to be comfortable opening, understanding, modifying, and building a useful analyst dashboard.

---

## Git

Teach practical basics:

- repository
- commits
- branches
- diff
- version history
- README
- reproducible work

Do not overemphasize advanced Git.

---

## R

Introduce R later in the program.

Objective:

I should be able to:

- understand basic R syntax
- import data
- manipulate data
- read an existing actuarial script
- modify basic calculations
- run a GLM
- interpret output

Python should remain the primary programming language.

---

# 6. Insurance Data Literacy

This must be a major part of the curriculum.

Teach me how insurance databases are actually structured.

Include:

## Policy Data

Fields such as:

- policy number
- insured
- effective date
- expiration date
- state
- territory
- class
- limit
- deductible
- exposure
- written premium
- earned premium
- coverage
- policy status

---

## Claims Data

Fields such as:

- claim number
- policy number
- accident date
- report date
- payment date
- close date
- paid indemnity
- paid expense
- case reserve
- incurred loss
- recovery
- salvage/subrogation
- claim status
- cause of loss

---

## Transactions

Teach why insurance databases often contain transactions rather than one clean row per claim.

Cover:

- premium transactions
- reserve changes
- loss payments
- recoveries
- endorsements
- cancellations

Teach how to convert transactional data into actuarially useful datasets.

---

# 7. Insurance Fundamentals Curriculum

Before specialized analysis, establish fluency in:

- exposure
- policy
- coverage
- limit
- deductible
- attachment point
- premium
- written premium
- earned premium
- unearned premium
- gross vs net
- direct vs assumed
- ceded
- claim
- occurrence
- accident
- paid loss
- case reserve
- incurred loss
- IBNR
- LAE
- ALAE
- ULAE
- frequency
- severity
- pure premium
- loss cost
- loss ratio
- expense ratio
- combined ratio
- underwriting profit
- accident year
- policy year
- calendar year
- development year

Require mastery.

---

# 8. Primary Insurance Pricing Module

Teach a complete pricing workflow.

Include:

1. Data validation.
2. Exposure development.
3. Premium on-leveling.
4. Loss development.
5. Loss trend.
6. Frequency trend.
7. Severity trend.
8. Catastrophe adjustment where relevant.
9. Large-loss adjustment.
10. Credibility.
11. Expected loss costs.
12. Expenses.
13. Profit provision.
14. Rate indication.
15. Segmentation.
16. Rate adequacy.
17. Portfolio profitability.
18. Actual vs expected.
19. Selection considerations.

Teach both:

- aggregate ratemaking
- more granular predictive approaches

Eventually introduce GLMs.

---

# 9. Reserving Module

Teach:

- development triangles
- paid triangles
- incurred triangles
- age-to-age factors
- selected development factors
- cumulative development factors
- ultimate losses
- IBNR
- chain ladder
- expected loss ratio method
- Bornhuetter-Ferguson
- Cape Cod conceptually
- tail factors
- diagnostics
- calendar-year effects
- changing claim settlement patterns
- reserve uncertainty
- sensitivity analysis

Build triangles in:

- Excel
- Python

Then reproduce analysis programmatically.

---

# 10. Reinsurance Fundamentals

This is a major focus.

Teach thoroughly:

- cedent
- reinsurer
- broker
- treaty
- facultative
- proportional
- non-proportional
- quota share
- surplus share
- excess of loss
- per-risk XOL
- catastrophe XOL
- clash
- aggregate excess
- stop loss
- attachment
- exhaustion
- limit
- retention
- occurrence definition
- reinstatements
- reinstatement premium
- ceding commission
- sliding-scale commission
- profit commission
- subject premium
- rate on line
- minimum deposit premium
- adjustable premium
- brokerage
- gross vs ceded vs net loss

Use diagrams frequently.

---

# 11. Reinsurance Mathematics

Develop intuition through progressively harder exercises involving:

- layer losses
- expected layer loss
- limited expected value
- increased limits
- attachment probability
- exhaustion probability
- aggregate loss
- occurrence loss
- frequency/severity
- compound distributions
- Monte Carlo simulation
- expected ceded loss
- retained loss
- ceded loss ratio
- rate on line
- payback period
- loss cost
- risk load
- expense load
- brokerage
- target return

Tie MAS-I probability concepts directly to reinsurance applications.

---

# 12. Reinsurance Pricing

Teach actual analyst workflow.

Include:

## Experience Rating

- historical losses
- development
- trend
- exposure adjustment
- rate-level adjustment
- layer losses
- burning cost
- credibility
- large-loss considerations
- frequency/severity changes

## Exposure Rating

Teach conceptually and practically:

- severity curves
- increased limits factors
- exposure curves
- policy profiles
- attachment/exhaustion
- layer expected loss

## Pricing

Show how to move from:

Expected Loss Cost

to:

Technical Premium

to:

Quoted Premium

Include:

- expenses
- brokerage
- risk margin
- cost of capital
- uncertainty
- market considerations

Explain why technical price and market price differ.

---

# 13. Reinsurance Structuring

Give me problems such as:

A cedent currently purchases:

$5M xs $5M

Compare against:

- $4M xs $4M
- $5M xs $10M
- $10M xs $5M
- quota share
- aggregate protection

Evaluate:

- expected ceded losses
- retained losses
- volatility
- tail risk
- premium
- capital implications
- earnings stability

Require written recommendations.

---

# 14. Catastrophe / Portfolio Analytics

Introduce:

- catastrophe models
- hazard
- vulnerability
- exposure
- event sets
- stochastic event catalogs
- modeled losses
- AAL
- occurrence EP
- aggregate EP
- exceedance probability
- return periods
- PML
- TVaR
- modeled uncertainty
- secondary uncertainty
- accumulation
- concentration
- diversification

Do NOT attempt to recreate RMS or AIR.

Teach me enough that I can intelligently work with outputs from such models.

Use simulated catastrophe datasets.

---

# 15. Casualty Analytics

Include:

- long-tailed vs short-tailed lines
- claims-made vs occurrence
- social inflation
- severity trend
- limits profiles
- attachment erosion
- loss development
- excess casualty
- workers compensation
- commercial auto
- general liability
- professional liability

Explain why casualty reinsurance is difficult to price.

---

# 16. Statistical / Predictive Analytics

Connect statistical concepts to insurance problems.

Include:

- exploratory data analysis
- sampling
- confidence intervals
- hypothesis testing
- correlation
- regression
- generalized linear models
- Poisson
- negative binomial
- Gamma
- Tweedie
- logistic regression
- model validation
- overfitting
- train/test split
- variable selection
- interactions
- residuals
- lift
- calibration

Explain when actuarial judgment should override mechanical model output.

---

# 17. Insurance Financial Analysis

Teach:

- underwriting income
- loss ratio
- expense ratio
- combined ratio
- investment income
- reserve changes
- premium growth
- renewal retention
- rate change
- exposure change
- mix shift
- prior-year development
- statutory vs GAAP concepts at a high level
- Schedule P conceptually
- AM Best data conceptually

Teach how an insurer makes money.

---

# 18. Communication Training

Every major project must end with a professional communication deliverable.

Examples:

- underwriting recommendation
- pricing memo
- reserve memo
- broker presentation
- executive summary
- portfolio review
- management email

Require conclusions like:

> Loss emergence indicates approximately 8–10% rate inadequacy, driven primarily by severity deterioration in commercial auto. I recommend pursuing a 12% indicated increase while monitoring retention impacts.

Not:

> The model produced 11.6%.

Teach me to separate:

DATA

from

INTERPRETATION

from

RECOMMENDATION.

---

# 19. Professional Judgment

Frequently ask:

- Is this result plausible?
- What assumption matters most?
- What could make this wrong?
- What would you investigate next?
- What additional information would you request?
- Would you trust this model?
- What decision would you make?
- How would an underwriter challenge this?
- How would a broker challenge this?
- How would a chief actuary challenge this?

Develop skepticism.

---

# 20. Curriculum Structure

Build approximately a **12-week core apprenticeship**.

Do NOT organize weeks solely around software.

Software should be embedded in insurance work.

Suggested architecture:

## Phase I — Insurance Operating System
Weeks 1–2

Insurance fundamentals
Insurance financial statements
Policy/claims data
Excel insurance analysis
SQL basics

## Phase II — Core Actuarial Work
Weeks 3–5

Frequency/severity
Pricing
Loss development
Reserving
Credibility
Trend

## Phase III — Reinsurance
Weeks 6–8

Treaty structures
Layer mathematics
Experience rating
Exposure rating
Treaty pricing
Structuring

## Phase IV — Advanced Analytics
Weeks 9–10

Python
GLMs
Simulation
Portfolio analytics
Catastrophe analytics

## Phase V — Professional Practice
Weeks 11–12

Integrated projects
Executive communication
Model review
Interview case studies
Final capstone

Adjust sequencing if a better pedagogical structure exists.

---

# 21. Capstone Projects

Require at least four major projects.

## CAPSTONE 1 — Primary Pricing Study

Provide synthetic portfolio data.

I must:

- validate data
- analyze premium
- analyze exposures
- analyze losses
- examine frequency
- examine severity
- apply development
- apply trend
- determine rate adequacy
- recommend action

Deliver:

- Excel
- SQL
- Python
- management memo

---

## CAPSTONE 2 — Reserve Review

Provide multi-year claims data.

I must:

- construct triangles
- select development factors
- calculate ultimate losses
- estimate IBNR
- compare methods
- explain differences
- make reserve recommendation

Deliver:

- Excel workbook
- Python analysis
- reserve memo

---

## CAPSTONE 3 — Reinsurance Pricing

Provide:

- historical losses
- exposure history
- premium history
- proposed treaty structures

I must:

- trend losses
- develop losses
- calculate layer losses
- perform experience rating
- simulate prospective losses
- calculate expected ceded loss
- estimate technical price
- compare alternatives

Deliver:

- pricing model
- exhibits
- recommendation

---

## CAPSTONE 4 — Reinsurance Portfolio Optimization

Create a synthetic insurance portfolio.

I must compare multiple reinsurance programs.

Evaluate:

- retained expected loss
- ceded expected loss
- volatility
- tail loss
- cost
- downside protection
- capital efficiency

Deliver:

- Python simulation
- Excel summary
- Power BI dashboard if appropriate
- executive recommendation

---

# 22. Interview Preparation

Create interview drills based on completed coursework.

Ask questions such as:

- Walk me through how you would price an excess-of-loss treaty.
- Why might incurred and paid development tell different stories?
- Explain IBNR.
- How would you determine whether a book is adequately priced?
- What does $5M xs $5M mean?
- What happens if severity inflation accelerates?
- How would you investigate deterioration in loss ratio?
- How would you validate a claims dataset?
- What SQL would you use to aggregate losses by accident year?
- Why would a reinsurer care about attachment probability?
- What is the difference between experience rating and exposure rating?
- How would you explain a 100-year PML to a CFO?

Grade my responses.

---

# 23. Portfolio / Employer Evidence

Create a `/portfolio` directory.

As I complete strong projects, create sanitized portfolio versions.

Each portfolio project should contain:

README.md
data_dictionary.md
methodology.md
analysis.ipynb
SQL scripts
Excel output where appropriate
charts
executive_summary.md

The README should explain:

- Business problem.
- Data.
- Method.
- Results.
- Recommendation.
- Technologies used.

The objective is to eventually demonstrate:

Excel
SQL
Python
insurance analytics
actuarial methodology
reinsurance knowledge
business communication

to prospective employers.

---

# 24. Repository Structure

Create something similar to:

actuarial-apprenticeship/

CLAUDE.md
README.md

curriculum/
    roadmap.md
    competency_matrix.md

lessons/
    01_insurance_foundations/
    02_insurance_data/
    03_sql/
    04_frequency_severity/
    05_pricing/
    06_reserving/
    07_reinsurance_foundations/
    08_reinsurance_pricing/
    09_portfolio_analytics/
    10_catastrophe/
    11_predictive_modeling/
    12_professional_practice/

datasets/

exercises/

submissions/

solutions/

grading/

portfolio/

sql/

python/

excel/

powerbi/

reference/

progress/

---

# 25. Solutions Security

Do NOT place exercise solutions where I will accidentally see them during normal coursework.

Create a solution structure that Claude can reference for grading but do not instruct me to inspect it before submitting.

Whenever assigning an exercise:

Do NOT reveal:

- final numeric answers
- completed code
- completed formulas
- exact solution path

unless I explicitly request a hint.

Hints should escalate:

Hint 1 = conceptual
Hint 2 = method
Hint 3 = implementation clue
Hint 4 = substantial assistance

Track how many hints I require.

---

# 26. Competency Matrix

Create a competency tracker such as:

| Competency | Exposure | Developing | Proficient | Mastered |
|---|---|---|---|---|
| Insurance terminology | | | | |
| Claims data | | | | |
| Excel | | | | |
| SQL | | | | |
| Python | | | | |
| Pricing | | | | |
| Reserving | | | | |
| Reinsurance | | | | |
| Reinsurance pricing | | | | |
| Cat modeling | | | | |
| GLMs | | | | |
| Communication | | | | |

Update it based on graded work.

Do not award mastery simply because a lesson was completed.

---

# 27. Progress Tracking

Maintain:

progress/current_status.md

Include:

Current lesson
Lessons completed
Exercise grades
Weak competencies
Strong competencies
Remediation required
Software proficiency
Projects completed
Next milestone

Also maintain:

progress/gradebook.csv

with fields such as:

date
module
exercise
technical_score
reasoning_score
software_score
business_score
communication_score
total_score
hints_used
passed
notes

---

# 28. Difficulty

Start moderately difficult.

Do not make exercises trivial.

Increase complexity progressively.

By the second half of the program, datasets should contain realistic complications such as:

- missing values
- duplicate records
- incorrect data types
- inconsistent dates
- reopened claims
- extreme losses
- incomplete development
- exposure changes
- rate changes
- mix shifts
- inflation
- policy limits
- deductibles
- changing retention
- catastrophe losses

Make me discover some problems myself.

Do not always tell me what is wrong with the data.

---

# 29. Realistic Manager Assignments

Some exercises should intentionally be underspecified.

Example:

> Here are five years of commercial auto results. Management believes performance has deteriorated. Determine what is happening and recommend what we should do.

I should decide:

- what to calculate
- what to investigate
- what charts matter
- what assumptions are required

Grade my judgment.

---

# 30. Time Pressure

Later exercises should occasionally simulate actual work constraints.

Examples:

### 30-minute diagnostic

### 60-minute pricing review

### 90-minute data analysis

### Executive summary limited to 200 words

### Explain results verbally in five minutes

Do not use time pressure during the initial learning phase.

---

# 31. Employer-Specific Overlay

Create a reusable process for when I provide a job description.

When I provide one:

1. Parse required skills.
2. Map skills against my competency matrix.
3. Separate:
   - core skills
   - role-specific concepts
   - proprietary software
   - nice-to-haves
4. Identify gaps.
5. Build a short targeted sprint.
6. Give me an employer-specific case exercise.
7. Prepare likely technical interview questions.

The objective is that a new job description should require **incremental adaptation**, not an entirely new curriculum.

---

# 32. Claude's Role During Training

Act as:

- Senior actuarial analyst
- Reinsurance pricing actuary
- Technical mentor
- Reviewer
- Manager

depending on the exercise.

Do not constantly praise me.

Judge work based on professional standards.

If something is wrong, say it clearly.

If my reasoning is strong but calculation is wrong, distinguish those.

If the answer is technically correct but professionally weak, explain why.

The ultimate question is:

> Would I be comfortable giving this analyst work that affects an underwriting, pricing, reserving, or reinsurance decision?

---

# 33. Lesson Interaction Protocol

VERY IMPORTANT:

Do NOT dump the entire course on me.

Build the repository and roadmap first.

Then training proceeds **one lesson at a time**.

Each lesson should work like this:

### PART A
Explain one concept.

### PART B
Ask me a short comprehension question.

WAIT FOR MY RESPONSE.

### PART C
Evaluate my response.

Correct misunderstandings.

### PART D
Teach the next concept.

Continue until the lesson is complete.

### PART E
Give me the independent exercise.

STOP.

Wait for my submission.

Then grade it.

This must be interactive.

Do not provide 30 pages of material and then ask questions at the end.

---

# 34. Socratic Questions

Frequently stop and ask me to predict what should happen before calculating it.

Examples:

> If severity rises 8% while frequency remains unchanged, what should happen to pure premium?

> If an XOL attachment increases, should the expected ceded loss increase or decrease?

> If paid claims are developing more slowly than historically, what might that do to a paid chain-ladder estimate?

I should develop intuition rather than formula memorization.

---

# 35. Connection to MAS-I

Whenever appropriate, explicitly connect practical insurance applications to MAS-I concepts.

Examples:

Compound Poisson
→ aggregate claims.

Limited expected value
→ insurance limits and reinsurance layers.

Conditional expectation
→ severity analysis.

Credibility
→ ratemaking.

GLMs
→ pricing segmentation.

Survival models
→ time to claim / claim settlement.

Monte Carlo simulation
→ treaty pricing and portfolio risk.

The purpose is to make exam material feel economically meaningful.

---

# 36. Final Readiness Assessment

At the end, run a comprehensive assessment.

Simulate the first week of an actuarial/reinsurance analyst job.

Provide several files without detailed instructions.

Include:

policy data
claims data
premium data
loss history
reinsurance terms

Ask me to:

1. Inspect the data.
2. Identify issues.
3. Query it.
4. Analyze performance.
5. Perform actuarial calculations.
6. Evaluate reinsurance.
7. Build exhibits.
8. Recommend action.
9. Prepare an executive summary.
10. Defend the analysis under questioning.

Grade the entire assignment.

Final classifications:

NOT READY
ENTRY-LEVEL READY
STRONG ENTRY-LEVEL
ABOVE-TYPICAL ENTRY-LEVEL

Provide evidence supporting the rating.

---

# 37. Initial Build Instructions

Begin now by creating the project architecture.

Specifically:

1. Create the directory structure.
2. Create `CLAUDE.md`.
3. Create the 12-week roadmap.
4. Create the competency matrix.
5. Create the grading framework.
6. Create the progress tracking system.
7. Define the software environment.
8. Create initial synthetic insurance datasets.
9. Create the curriculum dependency map.
10. Create the four capstone specifications.
11. Create the employer-specific job-description analysis process.
12. Create a README explaining how the apprenticeship works.

Do NOT generate all detailed lessons yet.

Detailed lessons should be generated as I reach them so they can adapt to my performance.

After completing the initial repository build:

Show me:

- repository structure
- roadmap
- competency framework
- technology stack
- how progression works

Then begin:

# Lesson 1 — How a P&C Insurer Actually Works

Start interactively.

Teach only the first concept.

Then ask me the first comprehension question.

WAIT FOR MY RESPONSE.
