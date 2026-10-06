# Grading Framework

Every graded item in the apprenticeship is scored here. The standard is professional, not academic: would a senior actuary be comfortable relying on this work for an underwriting, pricing, reserving, or reinsurance decision?

## 1. The rubric (100 points)

| Criterion | Points | Question |
|---|---|---|
| Technical Accuracy | 35 | Were calculations and methods correct? |
| Analytical Reasoning | 25 | Does the apprentice understand what the results mean? |
| Data Handling / Software | 15 | Was the analysis implemented competently? |
| Business Judgment | 15 | Is the recommendation defensible? |
| Communication | 10 | Could an underwriter, broker, actuary, or manager understand and act on the conclusion? |

### Band descriptors

**Technical Accuracy (35)**

| Band | Descriptor |
|---|---|
| 31–35 | All material calculations correct. Methods suit the data and the question. Results reconcile to source and control totals. At most immaterial slips. |
| 25–30 | One material error, or a method weakness (a defensible but inferior method, a missing adjustment) that does not overturn the conclusion. |
| 18–24 | Multiple material errors, or a wrong method on one major component. The conclusion is partly unreliable. |
| 0–17 | Approach wrong, core calculations missing or incorrect, or results unusable. |

**Analytical Reasoning (25)**

| Band | Descriptor |
|---|---|
| 22–25 | Explains what the results mean and why. Identifies the drivers, tests plausibility, names the assumption that matters most and how sensitive the answer is to it. Separates signal from noise. |
| 18–21 | Interprets the main results correctly. Some drivers or assumptions unexamined; plausibility testing is light. |
| 13–17 | Restates numbers rather than interpreting them, misses a key driver, or misreads one result. |
| 0–12 | Interpretation wrong or absent. |

**Data Handling / Software (15)**

| Band | Descriptor |
|---|---|
| 14–15 | Data validated and reconciled before use; problems found are documented and treated with a stated rationale. Work runs end to end and is reproducible. Tools used appropriately; model conventions followed. |
| 11–13 | Competent implementation with minor hygiene gaps: a hardcode, a missing check, an immaterial unreconciled total. |
| 8–10 | Produces numbers but is fragile or opaque: thin validation, hard to audit or rerun. |
| 0–7 | Data mishandled (wrong grain, faulty joins, double counting, unvalidated inputs) or the work cannot be reproduced. |

**Business Judgment (15)**

| Band | Descriptor |
|---|---|
| 14–15 | Decisive, sized, defensible recommendation that accounts for business constraints (retention, market, regulation, capital) and anticipates how an underwriter, broker, or chief actuary would challenge it. |
| 11–13 | Defensible recommendation; one important consideration missing or not sized. |
| 8–10 | Vague, hedged until it is not actionable, or only loosely tied to the analysis. |
| 0–7 | No recommendation, or one the analysis does not support. |

**Communication (10)**

| Band | Descriptor |
|---|---|
| 9–10 | Bottom line first. Data, interpretation and recommendation clearly separated. Right length for the audience. Exhibits titled, with units and sources. A non-actuarial manager could act on it. |
| 7–8 | Clear, with structure or length problems or minor labeling gaps. |
| 5–6 | The reader has to dig for the conclusion; unexplained jargon; unclear exhibits. |
| 0–4 | Conclusion missing, buried, or misleading. |

Standards for written work are in [reference/communication_standards.md](../reference/communication_standards.md); Excel standards are in [excel/README.md](../excel/README.md).

## 2. Classifying errors

Each error in a grade report is classified two ways.

**Severity**

- **Material:** would change a decision or mislead a reader. Examples: wrong denominator for a loss ratio; double-counted claims; development applied to the wrong basis; a recommendation the numbers contradict.
- **Immaterial:** cosmetic, or changes a result by less than about 2% with no effect on the decision. Examples: rounding, a mislabeled axis that the text clarifies, a slightly different but reasonable averaging choice.

When in doubt, ask whether the error would survive review by a chief actuary without comment. If it would not, it is material.

**Type** (decision D11)

- **Reasoning:** wrong concept, method, or interpretation.
- **Calculation:** right method, wrong arithmetic or formula.
- **Data:** wrong grain, join, filter, or an unvalidated input.
- **Presentation:** correct work communicated poorly.

**Scoring discipline**

- Deduct in the criterion where the error lives. Do not penalize one root error in several criteria, unless it independently causes a wrong recommendation (then Business Judgment also loses points).
- Strong reasoning with a calculation error is scored as exactly that: Reasoning keeps its points, Technical loses them.
- Technically correct but professionally weak work (no recommendation, no plausibility check, unusable exhibit) loses points in Reasoning, Business Judgment, or Communication even when every number is right.

## 3. Performance bands and gates

| Score | Band |
|---|---|
| 90–100 | Mastery |
| 80–89 | Proficient |
| 70–79 | Developing |
| Below 70 | Remediation required |

| Item | Gate to advance |
|---|---|
| Modules 01, 02, 03 (foundational) | 90 |
| Modules 04–11 | 80 |
| Capstones C1–C4 | 80 |
| Interview drills (Module 12) | 80 average across a drill set |
| Final Readiness Assessment | Classification (section 7) |

Each module designates one **gate exercise** in its `lesson.md`. Other exercises in the module are graded and count as competency evidence; any below 80 creates a remediation item that is cleared before the gate exercise is assigned.

## 4. Remediation protocol (spec §4)

When a gate exercise scores below its gate:

1. **Explain the problem.** Name the material errors and the misunderstanding behind them.
2. **Teach a shorter remediation lesson.** One to three concepts, same one-concept-one-question protocol, aimed only at the gap.
3. **Assign a new problem.** New scenario or new data cut, same competencies, id `<exercise_id>-R1` (then `-R2`). The solution is written before assigning. Correcting numbers in the original submission is never accepted.
4. **Regrade** the new problem against the same gate.

If two remediation problems fail on the same competency, step back: revisit the prerequisite concepts named in [dependency_map.md](dependency_map.md), record it under "Remediation required" in `progress/current_status.md`, and only then assign `-R3`.

**Capstones.** 80+ passes. 70–79: targeted remediation on the failing components, followed by a new, shorter problem covering those components; the capstone passes when that problem scores 80+. Below 70: a replacement capstone on a new data cut (decision D12). A capstone is never resubmitted with corrections.

## 5. Hints

- Hints are given only on request and escalate one level at a time: 1 conceptual, 2 method, 3 implementation clue, 4 substantial assistance.
- Hints carry **no score penalty**. Every hint is logged in `progress/hints_log.csv` and counted in the gradebook.
- An exercise that used **three or more hints** can move a competency no higher than Developing, whatever its score.
- The grade report states the hints used and whether they shaped the result.

## 6. Grade report template

Saved as `grading/<exercise_id>_grade.md`.

```markdown
# Grade report — <exercise_id>: <title>

| Field | Value |
|---|---|
| Module | NN <module name> |
| Attempt | 1 (or 2+ for remediation problems) |
| Date graded | YYYY-MM-DD |
| Submission | submissions/<exercise_id>/ |
| Hints used | n (levels: …) |
| Reviewer role | e.g., senior reinsurance pricing actuary |

## Score

| Criterion | Score | Max |
|---|---|---|
| Technical Accuracy | | 35 |
| Analytical Reasoning | | 25 |
| Data Handling / Software | | 15 |
| Business Judgment | | 15 |
| Communication | | 10 |
| **Total** | | **100** |

**Gate:** <90 or 80> — **Result:** PASS / FAIL (band: Mastery / Proficient / Developing / Remediation required)

## Bottom line
Two or three sentences: would I rely on this work, and why or why not.

## What was done correctly
- Specific, evidence-based points. No generic praise.

## Errors

| # | Error | Severity | Type | Criterion | Effect |
|---|---|---|---|---|---|
| 1 | | Material / Immaterial | Reasoning / Calculation / Data / Presentation | | |

## Better approach
What a stronger analyst would have done differently and why.

## Professional-standard answer
The approach, key results and conclusion a competent senior analyst would have delivered, at the level of detail the exercise required.

## Remediation
Specific actions, readings, or practice before the next item (or the remediation plan if the gate failed).

## Competency updates applied

| Competency | Old level | New level | Evidence |
|---|---|---|---|

## Gate result and next step
PASS → next concept / module. FAIL → remediation lesson topic and new problem id.
```

## 7. Interview drill rubric

Interview drills (ids `INT-NN`) use a shorter 100-point rubric. Each question is scored; the drill score is the average.

| Criterion | Points | Full marks | Half marks | Low marks |
|---|---|---|---|---|
| Correctness | 50 | Technically right, complete, uses correct terms | Right idea with gaps or one error | Wrong or confused |
| Clarity | 30 | Structured, concise, pitched to the stated audience, within time | Understandable but rambling or jargon-heavy | Hard to follow |
| Judgment | 20 | Names assumptions, limitations and what to check next; ties to a decision | Some judgment, not tied to a decision | Mechanical answer only |

Drills are answered in writing or as a timed "verbal" answer typed as spoken. Gradebook recording: correctness in `technical_score`, clarity in `communication_score`, judgment in `business_score`. The question bank is [reference/interview_question_bank.md](../reference/interview_question_bank.md).

## 8. Final readiness classification (spec §36)

The Final Readiness Assessment ([final_readiness_assessment.md](capstones/final_readiness_assessment.md)) simulates an analyst's first week. Its written deliverables are scored on the 100-point rubric; the closing defense under questioning is scored on the interview rubric. The classification below uses those two scores plus the cumulative record. **The criteria in this section govern the classification.**

The apprentice receives the **highest class for which every criterion is met**.

**Core competencies** (used below): Insurance terminology; Insurer financials; Claims & transaction data; Data validation; Excel modeling; SQL; Python (pandas); Loss development; Reserving methods; Ratemaking / indications; Reinsurance structures; Layer mathematics; Treaty pricing; Professional judgment; Written communication.

| Criterion | ENTRY-LEVEL READY | STRONG ENTRY-LEVEL | ABOVE-TYPICAL ENTRY-LEVEL |
|---|---|---|---|
| Final assessment score | 80+ | 87+ | 93+ |
| Defense score | 75+ | 85+ | 90+ |
| Material errors in the final assessment | Any left are caught by the apprentice under questioning | None in core calculations | None |
| Capstones | All four passed (replacements allowed) | All passed; average 85+ | All passed on the first capstone; average 90+ |
| Competency matrix | Every core competency Proficient or better | Every core competency Proficient or better; at least one Mastered in each of pricing, reserving and reinsurance | Majority of all competencies Mastered, including most core competencies |
| Data issues in the final assessment | Finds the issues that would distort the main conclusion | Finds most issues unprompted and treats them with stated rationale | Finds issues no lesson announced and quantifies their effect |
| Independence | No Hint 4 on any capstone or on the final assessment | Hint level 3+ used on no more than three items in Phases III–V | Hint level 3+ used on no more than one item in Phases III–V |
| Deliverable quality | Usable after a senior's corrections | Usable with light edits | Usable without edits; anticipates the chief actuary's questions |

**NOT READY** applies when any ENTRY-LEVEL READY criterion is unmet. The report then names the binding gaps and a remediation plan (targeted modules, new problems, and a re-sit of a fresh final assessment).

### Evidence required in the readiness report

The classification report (`grading/FRA_grade.md`) must include:

1. The final assessment score table and defense score, with the material errors listed.
2. The capstone record: ids, scores, attempts, replacements.
3. A snapshot of the competency matrix with evidence ids for every core competency.
4. Hint totals by phase from `progress/hints_log.csv`.
5. For each criterion row above, one or two sentences citing specific evidence (exercise id, file, quoted passage, or defense answer).
6. The single strongest and single weakest piece of work in the program, with ids.
7. What the apprentice should say to an employer about their readiness, and what they should not claim.
