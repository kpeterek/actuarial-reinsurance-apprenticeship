# Communication Standards

Every major deliverable in this program ends with something a non-specialist must act on: a memo, an executive summary, an email, an exhibit. This file sets the standard those are graded against (Communication is 10 points of every rubric, and weak communication also costs Business Judgment points). The standard comes from spec §18 and from how actuarial work is actually reviewed.

All worked examples below are **illustrative**. They use invented numbers and do not describe Kettlerock's data.

---

## 1. The core rule: separate data, interpretation, and recommendation

| Layer | What it is | Test |
|---|---|---|
| **Data** | What the numbers are. Observed or calculated facts, with their basis (paid/reported/ultimate, gross/net, as-of date). | Could another analyst reproduce it from the same files? |
| **Interpretation** | What you believe the numbers mean, and why. Causes, drivers, reliability. | Does it say how confident you are and what evidence supports it? |
| **Recommendation** | What the reader should do. An action, a size, a timing, and what to watch. | Could the reader act on it tomorrow? |

Mixing the layers is the most common weakness in analyst writing. Readers need to know which statements are facts they can rely on, which are your judgment they can challenge, and which are decisions they own.

### Worked contrast 1 — Pricing (an illustrative small commercial package book)

**Weak:** "Loss ratios have gone up a lot because severity is bad, so we need about 7%."

**Strong:**

- **Data.** On-level loss and ALAE ratios for accident years 2021–2025 are 58%, 61%, 66%, 64%, and 69%. AY2025 is at 12 months and has been developed to ultimate. Claim frequency per $1,000 of payroll has been flat (±2%); average severity has risen about 7% a year.
- **Interpretation.** The deterioration is a severity problem, not a frequency problem. The severity increase is broad across classes rather than concentrated in one. AY2025 is the least certain point; a reasonable range for it is 63–75%.
- **Recommendation.** Take a +7% base rate change effective 7/1, uniform across classes. Review again after Q2 emergence. If AY2025 develops above 72%, a second change will be needed in the next cycle.

### Worked contrast 2 — Reserving (an illustrative homeowners book)

**Weak:** "Chain ladder gives IBNR of $14.2M. BF gives $11.8M. I took the average."

**Strong:**

- **Data.** At 12/31/2025, the paid chain ladder indicates total IBNR of $14.2M, and the Bornhuetter-Ferguson method (65% a priori loss ratio) indicates $11.8M. The difference is almost entirely AY2025, which is 55% reported.
- **Interpretation.** The chain ladder leverages a large early-reported hail event in AY2025 through a development factor built mostly on non-event years. Event claims report faster than average, so this overstates AY2025 development. B-F is more reliable for that year. For AY2024 and older, the methods agree within 3%.
- **Recommendation.** Carry IBNR of $12.0M (range $11.0M–$13.5M). Use B-F for AY2025 and chain ladder for older years. Revisit AY2025 at 3/31 once event claims mature.

### Worked contrast 3 — Reinsurance (an illustrative property per-risk layer)

**Weak:** "The layer price is $1.9M, a 9.5% ROL. Reinsurer A is too expensive."

**Strong:**

- **Data.** Our technical price for the $20M xs $5M per-risk layer is $1.6M (8.0% ROL): expected loss $0.95M, expenses and brokerage $0.25M, risk margin $0.40M. Quotes range from $1.7M to $2.1M.
- **Interpretation.** All three quotes sit above technical, which is normal for a low-frequency layer: reinsurers price in capacity cost and payback expectations that a loss-cost model does not capture. Reinsurer A applies a minimum rate on line to layers in this range regardless of the cedent's experience. That is a market constraint, not a disagreement about our risk.
- **Recommendation.** Firm order at up to $1.8M, led by Reinsurer B. If A will not follow at that price, replace its share rather than paying its rate. The layer is worth buying at that price because it removes about 40% of our 1-in-50 per-risk net loss.

---

## 2. The "model produced 11.6%" anti-pattern

Spec §18 sets the standard.

> **Not this:** "The model produced 11.6%."

> **This:** "Loss emergence indicates approximately 8–10% rate inadequacy, driven primarily by severity deterioration in commercial auto. I recommend pursuing a 12% indicated increase while monitoring retention impacts."

Why the first fails:

| Problem | Why it matters |
|---|---|
| **False precision.** 11.6% implies accuracy to a tenth of a point. | Indications are uncertain by several points; precision you don't have destroys credibility when the next review moves it. |
| **No driver.** It says nothing about *why*. | The reader cannot judge whether the number is plausible or what would change it. |
| **No range.** | The reader cannot tell a confident 11.6% from a guess. |
| **No recommendation.** | The reader still has to decide what to do, with less information than you have. |
| **No ownership.** "The model produced." | Models don't make recommendations; analysts do. You are accountable for the number whether or not a model calculated it. |

Why the second works: it gives a range (8–10%) with a basis ("loss emergence"), a driver (severity, commercial auto), a recommendation with a size (12%), and something to monitor (retention).

It also leaves one gap that a reviewer will spot at once. The recommendation (12%) sits above the inadequacy range (8–10%). There can be good reasons for that: the indication projects to a later policy period than the emerged experience, the company wants to recover past inadequacy, or the change is being phased. But the reader shouldn't have to guess. In your own writing, close that gap in the next sentence.

**Rewriting drill.** Before submitting, find every sentence of the form "the model / the analysis / the result shows X" and rewrite it so that it states what X means and what to do about it.

---

## 3. Memo template

Use this for pricing memos, reserve memos, reinsurance recommendations, and capstone memos. Two pages plus exhibits unless the assignment says otherwise.

```
TO:      [name, title]
FROM:    [your name]
DATE:    [date]
RE:      [specific subject — e.g., "Commercial Auto 7/1/2026 rate indication"]
BASIS:   [data as-of date; gross/net; loss definition (e.g., loss & ALAE)]

1. PURPOSE
   One or two sentences: what question this memo answers and for what decision.

2. BOTTOM LINE
   The answer and the recommendation in three sentences or fewer.
   If the reader stops here, they have what they need.

3. KEY FINDINGS
   Three to five findings, each one sentence of interpretation supported by
   one sentence of data, with an exhibit reference.

4. METHOD
   What you did, in plain terms, at the level a reviewing actuary needs to
   judge appropriateness. Key assumptions and why you chose them.
   Details go in an appendix, not here.

5. CAVEATS AND UNCERTAINTY
   What could make this wrong, the range, and the one or two assumptions that
   matter most (with the result under a reasonable alternative).
   Data limitations and how you handled them.

6. RECOMMENDATION
   The action, its size, its timing, and what to monitor afterward.
   If your recommendation differs from the mechanical result, say why.

7. NEXT STEPS
   Who does what, by when. Information you are requesting.

EXHIBITS
   Numbered, each with a title that states its message, units, basis, and source.

APPENDIX (optional)
   Reconciliations, detailed method notes, data issues log.
```

Rules for the memo:

- The bottom line comes before the method. Readers are busy and senior.
- Each finding has an exhibit reference. Each exhibit supports at least one finding.
- Every number in the memo can be traced to an exhibit or the workbook.
- Use the same terms throughout. If you call it "reported loss" on page one, don't call it "incurred" on page two.

---

## 4. The 200-word executive summary

Used at the top of capstone memos, for board and CFO audiences, and in timed exercises (spec §30). Hard limit: 200 words, counted. Tables and exhibit references don't count; everything else does.

**Structure:**

1. **Answer and action** (1–2 sentences). What you recommend and the headline number.
2. **Why** (2–3 sentences). The two or three drivers, each with one number.
3. **Confidence** (1 sentence). The range and what drives it.
4. **Decision requested** (1 sentence). What you need from the reader, by when.
5. **Next steps** (1 sentence). What happens after the decision.

**Illustrative example (a homeowners rate filing at a fictional carrier; about 135 words):**

> **Recommendation.** File a +8% statewide homeowners rate change effective September 1, with larger increases for roofs older than 15 years.
>
> **Why.** Non-catastrophe loss costs have risen about 9% a year for three years, driven by roof and water claims. Our current rates assume 5%. Older roofs produce twice the claim frequency of newer ones but pay only 20% more premium. The indicated statewide change is +7% to +10%.
>
> **Confidence.** The range reflects the choice of trend period. Every reasonable choice indicates at least +7%, so the direction is not in doubt.
>
> **Decision requested.** Approval to file by June 15, which is the latest date that preserves the September 1 effective date.
>
> **Next steps.** Underwriting will model retention effects by segment, and we will report filed versus approved changes at the Q3 review.

Rules: no method detail; no jargon the reader would need defined (or define it in five words); one number per claim; no hedging stacks ("it may possibly suggest").

---

## 5. Management email format

For quick answers to managers, underwriters, and executives. Under 150 words in the body.

```
Subject: [the answer, not the topic]
         e.g., "HO 9/1 indication: +7% to +10%, recommend +8%"
         not   "CA rate analysis"

[Line 1: the answer and recommendation.]

[2–4 bullets: the supporting facts, one number each.]

[One line: the main caveat or range.]

[One line: what you need from them, by when — or "no action needed".]

[Attachment list, if any, with one-line descriptions.]
```

Rules: lead with the answer, not with what you did. No more than one caveat in the body; put the rest in the attachment. If the email asks for a decision, say so in the subject line.

---

## 6. Chart and exhibit standards

| Standard | Detail |
|---|---|
| **One message per chart** | The title states the message ("Homeowners severity has grown 6% a year while frequency is flat"), not the contents ("Homeowners frequency and severity by AY"). |
| **Units and basis on every chart** | $000 or $M; %; loss & ALAE or loss only; gross or net; paid, reported, or ultimate. |
| **Source line** | Data source, as-of date, and your name or initials, e.g., "Source: Kettlerock claim transactions, evaluated 12/31/2025; analyst calculations." |
| **Show immaturity** | Mark immature accident years (hatching, lighter shade, or a note) so readers don't over-read the latest point. |
| **Start bar axes at zero** | Line charts may use a non-zero axis if it is labeled clearly. |
| **Consistent colors across exhibits** | The same line or segment keeps the same color in every chart in a deliverable. |
| **Annotate what matters** | Label the point the reader should look at (a rate change date, an event, a threshold). |
| **No 3-D, no pie charts for more than three categories, no dual axes unless unavoidable** | Each of these makes comparisons harder. |
| **EP curves** | Return period on the x-axis (log scale) with labeled points at 10, 25, 50, 100, 250; state OEP or AEP and gross or net. |
| **Triangles** | Show as tables, with conditional formatting to reveal diagonals; label origin and age clearly; highlight selected factors. |

Recommended forms for common exhibits:

| Exhibit | Form |
|---|---|
| Loss ratio by accident year | Bars (ratio) with a line for the target or permissible loss ratio |
| Frequency and severity trend | Two panels, log scale, with fitted trend lines and stated rates |
| Rate indication build-up | Waterfall from current loss ratio to indicated change |
| Reserve method comparison | Table by AY with methods in columns and the selection highlighted |
| Sensitivity | Tornado chart or a two-way table |
| Reinsurance layers | Stacked layer diagram (retention, layers, exhaustion) with loss examples marked |
| Program comparison | Scatter of cost vs tail protection, one point per program, dominated programs marked |

---

## 7. Stating uncertainty and ranges

| Do | Don't |
|---|---|
| Give a range with its basis: "8–10%, reflecting the choice of trend window" | Give an unexplained ±%: "±10%" |
| Name the assumption that drives the range and show the result under an alternative | List every possible caveat at equal weight |
| Round to the precision the analysis supports: rate changes to the nearest point, reserves to the nearest $0.1M at line level | Report 11.6% or $14,237,612 |
| Distinguish process uncertainty (randomness), parameter uncertainty (estimates), and model uncertainty (wrong method) where it matters | Imply that a stochastic model's percentiles capture all uncertainty |
| Describe a return period as an annual probability: "a 1% chance in any year" | Say "a once-in-a-century loss," which readers hear as "won't happen soon" |
| Say what would change your view and how you would know | Hedge every sentence ("may," "might," "possibly") |
| State immaturity explicitly: "AY2025 is 40% reported; its estimate could move by ±15 points" | Present the latest year with the same confidence as mature years |

**Wording ladder** for confidence, used consistently:

- "The data shows" — a fact you can point to.
- "We estimate" — a calculated result with a stated method.
- "The evidence indicates" — interpretation supported by more than one source.
- "We believe" — judgment, with reasons stated.
- "We cannot determine from this data" — say it when it is true, and say what information would resolve it.

---

## 8. Numbers and terms checklist

- Percent change vs percentage points: a loss ratio moving from 60% to 66% is +6 points, or +10%. Say which.
- Gross vs net, paid vs reported vs ultimate, AY vs PY vs CY: label every figure.
- Loss vs loss & ALAE vs loss & LAE: state the definition once in the memo header and keep it.
- Units: state $000 or $M in every table header.
- Dates: state the evaluation date and the period covered.
- Signs: increases and decreases, favorable and adverse. Make the direction unambiguous.
- Abbreviations: define on first use unless the reader is an actuary and the term is standard.
