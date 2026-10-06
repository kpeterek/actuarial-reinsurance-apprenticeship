# Final Readiness Assessment — Your First Week as an Analyst

| | |
|---|---|
| **Assigned** | In Module 12, after Capstones 1–4 are passed |
| **Prerequisites** | All modules and all four capstones passed |
| **Outcome** | One of four classifications (below), with written evidence. Not a pass/fail gate. |
| **Time expectation** | About 12–16 hours of work (see `curriculum/roadmap.md`) across five "days" (sessions), plus a 60–90 minute oral defense |
| **Spec reference** | `reference/program_specification.md` §36 (also §18, §19, §22, §32) |

---

## 1. The situation

It is Monday of your first week as an analyst. Your manager stops by, hands you a folder, and says:

> "This is the data for the account we discuss on Friday. Policies, claims, premium, loss history, and the reinsurance terms. I haven't had time to look at it. Tell me what's going on with this business and what we should do about its reinsurance. I'll want something I can forward to the CFO, and I'll want to walk through it with you before the meeting. Ask me if you're stuck, but I'm in meetings most of the week."

That is the full brief. There is no step-by-step list. Part of what is being assessed is whether you can turn an open request into a sensible plan of work.

## 2. What you receive

A folder at `lessons/12_professional_practice/exercises/data/FRA/` is assembled when the assessment begins (exercise id `FRA`). It contains several files covering:

- policy data
- claims data
- premium data
- loss history
- reinsurance terms

The files may come from Kettlerock or from a cedent you have not seen before. Their layout may not match the Kettlerock tables you know, and documentation may be partial. Nothing in the folder has been validated.

## 3. What you are expected to do

These are the ten things the assessment grades (spec §36). They are not a sequence of instructions; you decide the order, the depth, and the tools.

1. **Inspect the data.** Understand what each file is, its grain, its keys, and how the files relate.
2. **Identify issues.** Find problems with the data and decide what each one means for the analysis.
3. **Query it.** Use SQL to build the datasets you need, reproducibly.
4. **Analyze performance.** Determine how the business has performed and what is driving it.
5. **Perform actuarial calculations.** Apply the methods the situation calls for. Choosing them is part of the task.
6. **Evaluate reinsurance.** Assess what the current reinsurance does for this business and whether it should change.
7. **Build exhibits.** Produce the exhibits a reviewer would need to check your conclusions.
8. **Recommend action.** Make a recommendation that someone could act on.
9. **Prepare an executive summary.** No more than 200 words, written for the CFO.
10. **Defend the analysis under questioning.** A live session (see §5).

## 4. Rules of the week

- **Questions.** You may ask questions the way you would ask a manager. Questions about business context ("Is this account renewing on the same terms?", "What does this field mean?") are answered. Questions about method or what to look for are logged as hints and weighed in the classification.
- **Hints.** None are offered unprompted. Each hint you request is recorded.
- **Time.** Work is organized into five sessions ("Monday" through "Friday"). Friday's session is the oral defense. If you finish early, use the time to test your own conclusions.
- **Reuse.** You may reuse any code, templates, or helper modules you built during the program. Reuse is expected; it is how real analysts work.
- **Deliverables location.** `submissions/FRA/`.

## 5. The defense

On "Friday" you walk through your work in a 60–90 minute session. Claude plays several roles in turn:

- your **manager**, who checks whether the work is right and complete;
- the **Chief Actuary**, who challenges methods, assumptions, and selections;
- an **underwriter**, who challenges whether the conclusions match how the business is written;
- a **reinsurance broker** or **reinsurer's underwriter**, who challenges your view of the reinsurance;
- the **CFO**, who wants the answer and the decision in plain language.

Expect follow-up questions on anything in your submission, requests to explain a number without looking it up, and at least one question that asks what would make your recommendation wrong. You may revise a conclusion during the defense if you are given a good reason; changing your mind for a good reason is a strength, changing it under pressure without one is not.

## 6. Deliverables

| Deliverable | Notes |
|---|---|
| Data issues log | Issue, how found, records affected, treatment, effect |
| SQL scripts | Every dataset you built, runnable from the raw files |
| Analysis workbook and/or notebook | Your calculations, organized so a reviewer can follow them |
| Exhibits | The set you would hand a reviewer |
| Executive summary | 200 words maximum, for the CFO |
| Memo | To your manager, supporting the summary (length is your judgment) |
| Defense | Live; notes optional |

## 7. How it is graded

Each of the ten tasks is assessed. The written deliverables are scored on the standard rubric in `curriculum/grading_framework.md` (Technical 35 / Reasoning 25 / Data & Software 15 / Business Judgment 15 / Communication 10). The defense is scored on the interview rubric (correctness 50 / clarity 30 / judgment 20). The grade report (`grading/FRA_grade.md`) gives evidence for every conclusion.

The outcome is one of four classifications. It uses both scores plus your cumulative record (capstones, competency matrix, hints). The criteria and evidence requirements are in `curriculum/grading_framework.md` §8, which governs. In plain terms:

| Classification | In plain terms |
|---|---|
| **NOT READY** | Material gaps that would make it unsafe to rely on your work for a pricing, reserving, or reinsurance decision, even under supervision. |
| **ENTRY-LEVEL READY** | Can do the core work correctly under normal supervision; needs direction on what to investigate. |
| **STRONG ENTRY-LEVEL** | Does the core work correctly with little direction, finds most issues independently, and communicates conclusions a manager can use. |
| **ABOVE-TYPICAL ENTRY-LEVEL** | Work and judgment comparable to an analyst with experience: sets the plan, catches what others miss, defends conclusions convincingly, and knows the limits of the analysis. |

The question behind every classification is the one in spec §32: *would a manager be comfortable giving this analyst work that affects an underwriting, pricing, reserving, or reinsurance decision?*

## 8. What separates the classifications

The difference between the top classifications is rarely technical. It shows up in:

- whether you planned the week or reacted to it;
- whether your issues log is ranked by what matters to the decision;
- whether every number in the executive summary can be traced to an exhibit;
- whether your recommendation says what you would do, why, and what would change it;
- whether, under questioning, you can separate what the data shows from what you infer from what you recommend.
