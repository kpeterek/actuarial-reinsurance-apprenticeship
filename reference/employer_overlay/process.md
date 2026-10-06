# Employer Overlay — Operating Procedure

**Trigger:** The apprentice pastes a job description (or a link to one) and asks to prepare for it, or says something like "run the employer overlay."

**Purpose (spec §31):** adapt the apprenticeship to one employer in a few sessions. A new job description should need *incremental adaptation, not a new curriculum*. The overlay reuses the competency matrix, existing modules, the Kettlerock data, and the interview bank wherever it can.

**Who runs it:** Claude, in the teaching session where the job description arrives. The overlay pauses the main curriculum. Set the state to "Paused — employer overlay" and record the return point in `progress/current_status.md` and `progress/session_log.md`.

---

## Outputs

Create one folder per job description:

```
reference/employer_overlay/sprints/<employer>_<YYYY-MM-DD>/
├── jd_analysis.md          steps 1–4 (from jd_analysis_template.md)
├── sprint_plan.md          step 5
├── case_exercise.md        step 6 (student-facing; no answers)
└── interview_questions.md  step 7 (no answers)
```

The case exercise solution goes to `solutions/employer_overlay/<employer>_<YYYY-MM-DD>/case_solution.md`, written at assignment time like every other solution (it is gitignored).

**Naming and privacy.** This repository is public. Before creating the folder, ask the apprentice whether to use the employer's name or an anonymized slug (for example `reinsurer_a`, `regional_carrier_b`). Default to anonymized unless told otherwise. Never write recruiter names, contact details, compensation, internal referral information, or anything the job posting marks confidential into the repository. Paste only the public job description text into `jd_analysis.md`.

`<YYYY-MM-DD>` is the date the job description was received.

---

## Step 1 — Parse required skills

1. Copy the job description text into `jd_analysis.md` (public text only).
2. Extract every skill, knowledge area, tool, credential, and behavior the posting asks for. Quote the posting's own phrase for each.
3. Normalize each to program vocabulary (for example, "loss reserving experience" → Reserving methods; "experience with RMS/AIR" → Cat model outputs + proprietary software).
4. Note how strongly the posting asks: *required*, *preferred*, or *mentioned*.
5. If useful, look up public information about the employer (lines written, primary vs reinsurer vs broker vs consultant, size, recent public news) to understand the role. Cite sources in `jd_analysis.md`. Do not rely on rumor or non-public information.

## Step 2 — Map against the competency matrix

For every normalized skill, record:

- the matching row(s) in `curriculum/competency_matrix.md`;
- the current level and evidence (exercise ids and scores) from that file and `progress/gradebook.csv`;
- the level the role needs (Exposure / Developing / Proficient / Mastered), judged from the posting's wording and the role's seniority.

If no matrix row fits, write "not in matrix" and treat it in Step 3. **The overlay never changes competency levels.** Levels change only through graded work, under the normal grading routine.

## Step 3 — Separate the four categories

| Category | Definition | How the overlay handles it |
|---|---|---|
| **Core skills** | Expected of any entry-level P&C analyst: insurance fundamentals, Excel, SQL, Python basics, loss ratios, triangles, communication | Usually already covered by modules; check evidence, close any gap with a targeted exercise |
| **Role-specific concepts** | Central to this role but not to every analyst job, e.g., treaty pricing for a reinsurer, GLMs for a personal lines pricing role, Schedule P for a reserving role, catastrophe output analysis for a cat analyst | Main focus of the sprint; may pull material forward from a later module in compressed form |
| **Proprietary software** | Vendor or in-house tools that cannot be installed here, e.g., Moody's RMS RiskLink / Risk Modeler, Verisk Touchstone, Aon ReMetrica, Guy Carpenter MetaRisk, WTW ResQ / Igloo / Radar / Emblem, Milliman Arius, Akur8, Guidewire, Duck Creek, SAS | Do not try to teach the tool. Map it to the underlying concept, build a vendor-neutral proxy exercise in Python or Excel, and prepare a short talk track: what the tool does, what the apprentice has done that is equivalent, how quickly the apprentice would expect to pick it up |
| **Nice-to-haves** | Preferred qualifications that won't decide the hire, e.g., a specific exam beyond what the apprentice has, VBA, a cloud data platform | List them; address only if cheap (one session or less) or if the apprentice asks |

## Step 4 — Identify gaps

For each skill, compare the current level with the required level and classify:

- **Critical:** core or role-specific, required, and current level below Proficient, or no graded evidence at all.
- **Moderate:** required and one level short, or preferred and two levels short.
- **Minor:** nice-to-have, or one level short on a preferred skill.
- **Evidence gap:** the skill is probably there (taught and practiced) but no graded artifact or portfolio piece proves it. Close it with a portfolio item or a drill, not a lesson.

Summarize the gaps at the end of `jd_analysis.md` with a one-paragraph readiness view for this role: where the apprentice is competitive today, and what would most change an interviewer's view.

## Step 5 — Build a short targeted sprint (`sprint_plan.md`)

- **Three to six sessions, maximum.** If the gaps need more, say so and recommend which modules to finish first instead of building a parallel curriculum.
- Order: Critical gaps first, then evidence gaps that a portfolio item can close, then Moderate gaps.
- For each session, give: objective; competency rows targeted; concepts (titles only, taught one at a time under the normal interaction protocol); the exercise or drill; and what "done" means.
- Reuse first: existing lessons, Kettlerock data, earlier submissions, `python/` and `sql/` helpers. Pull material forward from a later module only in compressed form, and note in `progress/current_status.md` that the full module is still owed.
- If an interview date is known, schedule backward from it and put the case exercise and an interview drill in the last two sessions.
- State what the sprint will **not** cover and why.

## Step 6 — Employer-specific case exercise (`case_exercise.md`)

Write one realistic assignment in the employer's context, using the standard exercise format (spec §3, Step 3):

- **Business situation** framed from the employer's seat (a reinsurer pricing a cedent's submission, a carrier's reserving team at quarter-end, a broker's analytics team preparing a renewal, a consultant's client deliverable).
- **Data available:** Kettlerock data reframed as the cedent or client where possible. If the role needs data Kettlerock lacks, generate a small add-on dataset (see `solutions/_generator/README.md`) and record its story in the case solution, not in the student file.
- **Required analysis, deliverable, software, and specific questions.**
- **A time limit** matching the employer's likely case-study format (spec §30: 30-, 60-, or 90-minute variants, or a 200-word summary).

Write the solution to `solutions/employer_overlay/<employer>_<YYYY-MM-DD>/case_solution.md` **before** giving the exercise. Use the exercise id `OV-<slug>` (for example `OV-reinsurer_a`) and add a row to `exercises/index.md`. Submissions go to `submissions/OV-<slug>/`. Grade with the standard rubric and log in `progress/gradebook.csv`, with `module` set to the curriculum module whose competencies the case mainly exercises and "employer overlay" in `notes`. Hints are logged as usual.

## Step 7 — Likely technical interview questions (`interview_questions.md`)

- 15–25 technical questions this employer is likely to ask, drawn from the posting, the employer's business, and `reference/interview_question_bank.md`. Mark which come from the bank.
- 3–5 role-fit questions ("Why reinsurance?", "Why us?", "How does your CRE background help in this role?").
- 5 questions the apprentice should ask the interviewer, chosen to show understanding of the role.
- No answers in the file. Run them as graded interview drills (interview-drill rubric in `curriculum/grading_framework.md`) in the final sprint session.

---

## Closing the sprint

1. Update `progress/current_status.md`: sprint completed, results, the return point in the main curriculum, and any modules pulled forward that are still owed in full.
2. Write a `session_log.md` entry.
3. If a sprint artifact is strong (80+), offer to turn it into a sanitized portfolio item under `portfolio/`.
4. Leave the sprint folder in place. Later job descriptions for similar roles should start from the closest previous `jd_analysis.md` and change only what differs.
