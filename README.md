# P&C Actuarial Analytics & Reinsurance Apprenticeship

A hands-on apprenticeship that trains me for entry-level work as an actuarial, reinsurance, pricing, reserving, or catastrophe/portfolio analyst. I am a career changer from commercial real estate finance and valuation, with actuarial Exams P and FM passed and MAS-I in progress. Claude acts as my senior actuary, mentor, reviewer and manager.

This is not exam prep. It is organized around the work analysts actually do: pulling and validating insurance data, building triangles and rate indications, pricing and structuring reinsurance, reading catastrophe model output, and writing recommendations someone can act on. The goal is that I can credibly tell an employer:

> I understand how P&C insurance and reinsurance work, I can work with real insurance data, I can analyze it using common actuarial tools, I understand the major pricing and reserving workflows, and I am comfortable enough with the standard technology stack to contribute immediately under normal analyst supervision.

The full program specification is in [reference/program_specification.md](reference/program_specification.md).

## How a module works

```
Teach → Demonstrate → Exercise → Submit → Grade → Gate
```

1. **Teach.** One concept at a time: what it is, why insurers and reinsurers care, who does it, what decision depends on it, the formulas and the reasoning behind them. Each concept ends with one comprehension question, and Claude waits for my answer before moving on.
2. **Demonstrate.** A worked example on the program's data, often in more than one tool (Excel, SQL, Python, Power BI, by hand).
3. **Exercise.** An analyst-style assignment: business situation, data, required analysis, deliverable, software, specific questions. No answers given. Later exercises are deliberately underspecified or time-boxed, the way real requests are.
4. **Submit.** I save my workbook, SQL, notebook and memo under `submissions/<exercise_id>/`.
5. **Grade.** Claude grades against a fixed 100-point rubric and writes a report to `grading/`.
6. **Gate.** I advance only when I clear the gate. Otherwise: a short remediation lesson and a new problem, not a chance to fix the old numbers.

## The modules

| # | Module | Phase | Hours | Gate | Capstone |
|---|---|---|---|---|---|
| 01 | [Insurance Foundations](lessons/01_insurance_foundations/) | I Insurance Operating System | 8–10 | 90 | |
| 02 | [Insurance Data](lessons/02_insurance_data/) | I | 10–12 | 90 | |
| 03 | [SQL for Insurance](lessons/03_sql_for_insurance/) | I | 8–10 | 90 | |
| 04 | [Frequency & Severity](lessons/04_frequency_severity/) | II Core Actuarial Work | 10–12 | 80 | |
| 05 | [Primary Pricing](lessons/05_primary_pricing/) | II | 10–12 | 80 | [C1 Primary Pricing Study](curriculum/capstones/capstone_1_primary_pricing.md) |
| 06 | [Reserving](lessons/06_reserving/) | II | 10–12 | 80 | [C2 Reserve Review](curriculum/capstones/capstone_2_reserve_review.md) |
| 07 | [Reinsurance Foundations](lessons/07_reinsurance_foundations/) | III Reinsurance | 8–10 | 80 | |
| 08 | [Reinsurance Pricing](lessons/08_reinsurance_pricing/) | III | 10–14 | 80 | [C3 Reinsurance Pricing](curriculum/capstones/capstone_3_reinsurance_pricing.md) |
| 09 | [Reinsurance Structuring](lessons/09_reinsurance_structuring/) | III | 8–10 | 80 | |
| 10 | [Portfolio & Cat Analytics](lessons/10_portfolio_cat_analytics/) | IV Advanced Analytics | 10–12 | 80 | [C4 Portfolio Optimization](curriculum/capstones/capstone_4_portfolio_optimization.md) |
| 11 | [Predictive Modeling](lessons/11_predictive_modeling/) | IV | 10–12 | 80 | |
| 12 | [Professional Practice](lessons/12_professional_practice/) | V Professional Practice | 8–10 | Classification | [Final Readiness Assessment](curriculum/capstones/final_readiness_assessment.md) |

Hours are estimates of focused work per module; capstones add roughly 50–70 hours. A "week" in the roadmap is a unit of work, not a calendar week. Detailed lessons are written when I reach each module so they can adapt to my results. Full sequencing, capstone timing and what "complete" means: [curriculum/roadmap.md](curriculum/roadmap.md).

## The data universe

Every dataset belongs to one fictional carrier, Kettlerock Mutual Insurance Company, a regional commercial-lines mutual writing in Texas, Louisiana, Oklahoma, Arkansas, New Mexico and Colorado. It writes four lines: Commercial Auto Liability (CA), General Liability (GL), Commercial Property (CP) and Workers' Compensation (WC), on annual policies effective 2016 through 2025. The data is evaluated as of 2025-12-31, so accident year 2025 is immature and "today" in exercises is early 2026. The raw layer is transactional, as in a real claims and policy system: policies, coverages, locations, premium and claim transactions, exposure snapshots, reinsurance treaties and renewal proposals, and a stochastic catastrophe event set; I build the clean analytical layer myself. The data is synthetic and contains realistic data-quality problems, so everything is validated before use.

Data documentation: [datasets/](datasets/) and [datasets/data_dictionary/](datasets/data_dictionary/).

## Software stack

| Tool | Role |
|---|---|
| Excel (Microsoft 365) | Models, triangles, rate exhibits, reinsurance calculators; [conventions](excel/README.md) |
| SQLite + SQL | Querying transactional insurance data; [notes](sql/README.md) |
| Python 3.14 (pandas 3, numpy, scipy, statsmodels, matplotlib, Jupyter) | Primary analysis language: cleaning, distributions, simulation, GLMs; [helpers](python/README.md) |
| Power BI Desktop | Loss and premium dashboards, portfolio views; [notes](powerbi/README.md) |
| Git + GitHub | Version history for every deliverable |
| R | Introduced in Module 11 to read, modify and run an actuarial GLM script |

Versions and install commands: [curriculum/software_stack.md](curriculum/software_stack.md).

## Starting a session

Open Claude Code in this directory and say:

> Resume my apprenticeship

Claude reads [progress/current_status.md](progress/current_status.md) and the latest entry in [progress/session_log.md](progress/session_log.md), then picks up exactly where the last session stopped: mid-concept, awaiting a submission, grading, or remediation. Other things I can say:

| I say | What happens |
|---|---|
| "Submitted 04-A" | Claude grades the files in `submissions/04-A/` |
| "Hint please" | The next hint level for the current exercise (logged) |
| "Let's stop here" | Claude updates progress, writes the session log, commits and pushes |
| Paste a job description | Claude runs the [employer overlay](reference/employer_overlay/process.md): gap analysis, a short targeted sprint, a case exercise and likely interview questions |

How Claude runs sessions is defined in [CLAUDE.md](CLAUDE.md).

## Grading and gates

Every submission is scored out of 100:

| Criterion | Points |
|---|---|
| Technical Accuracy | 35 |
| Analytical Reasoning | 25 |
| Data Handling / Software | 15 |
| Business Judgment | 15 |
| Communication | 10 |

Bands: 90–100 Mastery, 80–89 Proficient, 70–79 Developing, below 70 Remediation required. Modules 01–03 are foundational and require **90** to advance; all later modules and the capstones require **80**. A failed gate leads to a short remediation lesson and a new problem. A capstone below 70 is replaced with a new capstone on a different data cut. Hints escalate from conceptual to method to implementation clue to substantial assistance; they do not cost points but are logged, and heavy hint use limits how far a competency can advance.

Each grade report lists what was done correctly, errors classified as material or immaterial, a better approach, the professional-standard answer and specific remediation. Competency levels in [curriculum/competency_matrix.md](curriculum/competency_matrix.md) change only on graded evidence. The program ends with a Final Readiness Assessment that simulates an analyst's first week and classifies me as Not Ready, Entry-Level Ready, Strong Entry-Level, or Above-Typical Entry-Level, with evidence. Details: [curriculum/grading_framework.md](curriculum/grading_framework.md).

Grading answer keys and the data's ground truth are kept locally and not published in this repository. My submissions, grade reports and progress records are public.

## Where things live

| Path | Contents |
|---|---|
| [CLAUDE.md](CLAUDE.md) | Operating instructions Claude follows in every session |
| [curriculum/](curriculum/) | [Roadmap](curriculum/roadmap.md), [competency matrix](curriculum/competency_matrix.md), [dependency map](curriculum/dependency_map.md), [grading framework](curriculum/grading_framework.md), [software stack](curriculum/software_stack.md), [capstone specs](curriculum/capstones/) |
| [lessons/](lessons/) | One folder per module: README stub, then `lesson.md`, examples and exercises when reached |
| [datasets/](datasets/) | Raw transactional CSVs, reference tables, data dictionary, database build script |
| [exercises/](exercises/index.md) | Register of every exercise assigned |
| [submissions/](submissions/) | My work, one folder per exercise |
| [grading/](grading/) | One grade report per graded submission |
| [progress/](progress/) | Current status, gradebook, hints log, competency history, session log |
| [reference/](reference/) | [Glossary](reference/glossary.md), [MAS-I crosswalk](reference/mas1_crosswalk.md), [communication standards](reference/communication_standards.md), [professional judgment checklist](reference/professional_judgment_checklist.md), [interview question bank](reference/interview_question_bank.md), [employer overlay](reference/employer_overlay/process.md) |
| [excel/](excel/README.md), [sql/](sql/README.md), [python/](python/README.md), [powerbi/](powerbi/README.md) | Tool conventions, templates and shared helpers |
| [portfolio/](portfolio/README.md) | Employer-facing versions of the strongest projects |
| [solutions/](solutions/README.md) | Grading reference; kept local, not published |

## Building the database

The CSVs in `datasets/raw/` and `datasets/reference/` are the canonical data. The SQLite database is built locally from them and is not stored in Git. From the repository root:

```powershell
C:\Users\kpeterek\venvs\actuary\Scripts\python.exe datasets/processed/build_database.py
```

This creates `datasets/processed/kettlerock.sqlite`. In Python, `python/kettlerock.py` provides `connect()` and `load(table)`. The generator that produced the data is kept with the grading materials so that its parameters do not reveal what is in the data.
