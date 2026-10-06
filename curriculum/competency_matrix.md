# Competency Matrix

Levels change only on graded evidence. Completing a lesson never moves a competency beyond Exposure. Claude updates this file during grading (see `CLAUDE.md` §8) and logs every change in `progress/competency_history.csv`.

## Level definitions

| Level | Requirement |
|---|---|
| Not started | Not yet taught. |
| Exposure | Concept taught and comprehension questions answered. No graded evidence yet. |
| Developing | Best relevant graded item scored 70–79, or any item completed with three or more hints. |
| Proficient | A relevant graded item scored 80–89, or 90+ on only one item. |
| Mastered | 90+ on at least two graded items, at least one of which is an underspecified exercise or a capstone. |

Rules:

- **Evidence** is recorded as `exercise_id:score` (for example `04-A:86`). Only items that genuinely exercise the competency count.
- **Hints:** an exercise that used three or more hints can move a competency no higher than Developing.
- **Downgrades:** if a later graded item shows a material error in a competency already rated Proficient or Mastered, Claude lowers the level by one step and records the evidence. Levels track current ability, not best-ever.
- **Interview drills** count as evidence for Verbal / interview and, where the question is technical, for the relevant technical competency.

## Matrix

| Competency | Assessed in | Level | Evidence | Last updated |
|---|---|---|---|---|
| Insurance terminology | 01, 02, 07 | Not started | — | — |
| Insurer financials | 01, 12 | Not started | — | — |
| Policy & premium data | 02, 03 | Not started | — | — |
| Claims & transaction data | 02, 03, 06 | Not started | — | — |
| Data validation | 02, 03, all capstones | Not started | — | — |
| Excel modeling | 01, 05, 06, 07, 08 | Not started | — | — |
| Power Query / VBA | 02, 06, 12 | Not started | — | — |
| SQL | 03, then 04–12 | Not started | — | — |
| Python (pandas) | 04, 05, 06 | Not started | — | — |
| Python (simulation / stats) | 04, 08, 09, 10, 11 | Not started | — | — |
| Jupyter / reproducibility | 04 onward | Not started | — | — |
| Power BI | 02, 10, C4 | Not started | — | — |
| Git | 01 onward | Not started | — | — |
| R | 11 | Not started | — | — |
| Frequency / severity analysis | 04, 05 | Not started | — | — |
| Trend | 04, 05, 08 | Not started | — | — |
| Loss development | 05, 06, 08 | Not started | — | — |
| Reserving methods | 06, C2 | Not started | — | — |
| Ratemaking / indications | 05, C1 | Not started | — | — |
| Credibility | 05, 08 | Not started | — | — |
| Reinsurance structures | 07, 09 | Not started | — | — |
| Layer mathematics | 07, 08, 09 | Not started | — | — |
| Experience rating | 08, C3 | Not started | — | — |
| Exposure rating | 08, C3 | Not started | — | — |
| Treaty pricing | 08, C3 | Not started | — | — |
| Structuring / capital | 09, C4 | Not started | — | — |
| Cat model outputs | 10, C4 | Not started | — | — |
| Portfolio analytics | 10, C4 | Not started | — | — |
| GLMs | 11 | Not started | — | — |
| Model validation | 11, 12 | Not started | — | — |
| Professional judgment | All modules | Not started | — | — |
| Written communication | All modules | Not started | — | — |
| Verbal / interview | 12, FRA | Not started | — | — |

## Mapping to the specification's tracker (spec §26)

| Spec row | Matrix rows |
|---|---|
| Insurance terminology | Insurance terminology; Insurer financials |
| Claims data | Policy & premium data; Claims & transaction data; Data validation |
| Excel | Excel modeling; Power Query / VBA |
| SQL | SQL |
| Python | Python (pandas); Python (simulation / stats); Jupyter / reproducibility |
| Pricing | Frequency / severity analysis; Trend; Ratemaking / indications; Credibility |
| Reserving | Loss development; Reserving methods |
| Reinsurance | Reinsurance structures; Layer mathematics; Structuring / capital |
| Reinsurance pricing | Experience rating; Exposure rating; Treaty pricing |
| Cat modeling | Cat model outputs; Portfolio analytics |
| GLMs | GLMs; Model validation |
| Communication | Written communication; Verbal / interview; Professional judgment |

The employer overlay ([reference/employer_overlay/process.md](../reference/employer_overlay/process.md)) maps job-description skills against this matrix.
