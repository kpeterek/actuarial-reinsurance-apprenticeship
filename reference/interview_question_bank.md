# Interview Question Bank

Questions for interview drills (spec §22). There are no answers here by design: drills are graded live, using the interview-drill rubric in `curriculum/grading_framework.md` (correctness 50 / clarity 30 / judgment 20). Drills begin in Module 12, but any session may pull a question from a module you have finished.

How to practice:

- Answer out loud or in writing, in two minutes or less, unless the question asks for a walk-through.
- Lead with the answer, then the reasoning, then a caveat if one matters.
- Use a concrete example from your coursework where you can. "In my reserve review I found…" beats a textbook definition.
- For technical prompts, talk through your approach before writing code; interviewers grade the approach more than the syntax.

Employer-specific questions are written per job description under `reference/employer_overlay/sprints/`.

---

## 1. Core questions (spec §22)

1. Walk me through how you would price an excess-of-loss treaty.
2. Why might incurred and paid development tell different stories?
3. Explain IBNR.
4. How would you determine whether a book is adequately priced?
5. What does $5M xs $5M mean?
6. What happens if severity inflation accelerates?
7. How would you investigate deterioration in loss ratio?
8. How would you validate a claims dataset?
9. What SQL would you use to aggregate losses by accident year?
10. Why would a reinsurer care about attachment probability?
11. What is the difference between experience rating and exposure rating?
12. How would you explain a 100-year PML to a CFO?

---

## 2. By module

### Module 01 — Insurance foundations

13. Walk me through how a P&C insurer makes money. Can a company with a 102% combined ratio be a good business?
14. What is the difference between written and earned premium, and why do loss ratios use earned?
15. Take one claim and describe how it appears in accident-year, policy-year, and calendar-year results.
16. A company reports $50M of favorable prior-year development. What does that tell you, and what doesn't it tell you?

### Module 02 — Insurance data

17. Why do insurance systems store transactions instead of one row per claim? How would you build a claim snapshot as of a given date?
18. How would you compute calendar-year earned premium from a premium transaction table that includes endorsements, audits, and cancellations?
19. What is "grain," and how have you seen a grain mismatch produce a wrong answer?

### Module 03 — SQL

20. Explain the difference between an inner join and a left join between policies and claims, and describe a situation where choosing the wrong one changes a loss ratio.
21. What is a window function? Give two insurance uses.
22. How would you reconcile a loss summary you built in SQL to the finance department's numbers?

### Module 04 — Frequency and severity

23. If severity rises 8% while frequency is unchanged, what happens to pure premium? What if frequency also falls 3%?
24. Why measure frequency and severity trend separately instead of trending pure premium directly?
25. How would you choose a severity distribution for large liability claims, and how would you judge whether it fits the tail?
26. What is a limited expected value, and where would you use one?

### Module 05 — Primary pricing

27. Walk me through a rate indication from raw data to a recommended change.
28. Why do we put premium on-level? What does the parallelogram method assume, and when is that assumption wrong?
29. How do you calculate the trend period for annual policies to be written over the twelve months starting next July 1?
30. What is credibility, and what makes a good complement?
31. The indication is +18%, and underwriting says the market will not accept more than +8%. What do you recommend, and how do you present it?

### Module 06 — Reserving

32. Explain the chain-ladder method and its key assumption. Give two situations in which it fails.
33. When would you use Bornhuetter-Ferguson instead of chain ladder? What is the weakness of B-F?
34. How would you select a tail factor for a long-tailed line?
35. What would you look at before selecting age-to-age factors?
36. How would you build a reasonable range for a reserve estimate?

### Module 07 — Reinsurance foundations

37. Give four reasons an insurer buys reinsurance.
38. Compare a quota share and an excess-of-loss treaty: what does each do to a cedent's capital, volatility, and margin?
39. Explain reinstatement premium with a numerical example.
40. What is a sliding-scale commission, and why would a reinsurer offer one?

### Module 08 — Reinsurance pricing

41. What is burning cost, and what adjustments does it need before you can use it?
42. How do increased limits factors allocate a policy's expected loss to a reinsurance layer?
43. How do you move from expected loss cost to a technical premium? Why might the quoted market price be different?
44. Why does a fixed attachment point tend to become more expensive for the reinsurer over time?
45. Why is excess casualty harder to price than property per-risk excess?

### Module 09 — Reinsurance structuring

46. A cedent buys $5M xs $5M. How would you evaluate moving to $10M xs $5M instead?
47. How do you measure the value of a reinsurance program beyond its expected cost?
48. What does it mean to say reinsurance is a form of capital? How would you compare its cost with the cost of equity?
49. How does claims-made versus occurrence coverage affect a casualty reinsurer?

### Module 10 — Portfolio and catastrophe analytics

50. What is the difference between OEP and AEP? Which matters for a per-occurrence catastrophe treaty and which for an aggregate cover?
51. What is secondary uncertainty, and why does ignoring it understate the tail?
52. You are handed a catastrophe model output for a portfolio. How would you check it before using it?
53. What are the limits of using a 1-in-250 PML to set capital?

### Module 11 — Predictive modeling

54. Why use a GLM rather than linear regression for claim frequency? What does the exposure offset do?
55. How would you choose between a Poisson and a negative binomial frequency model?
56. How do you know a pricing model is good? Explain the difference between lift and calibration.
57. When should actuarial judgment override a GLM relativity?

### Module 12 — Professional practice

58. How would you review a model someone else built?
59. An executive wants one number, and your analysis supports a range. What do you say?
60. What is the difference between statutory and GAAP accounting that matters most for a P&C insurer?

---

## 3. Technical prompts

Talk through the approach first, then write the code or formula.

### SQL

61. From a claim transaction table, write a query that returns the case reserve on each claim as of 2025-12-31, using a window function or a correlated subquery.
62. Write a query that builds a cumulative paid triangle (accident year × development age at 12-month intervals) from transactions.
63. Write a query that returns the five largest occurrences per accident year, where an occurrence can include several claims.
64. Write a query that computes calendar-year earned premium from policy terms, including policies that span two years.
65. How do SQLite and SQL Server (or Snowflake) differ in date handling, and how would you write date logic that ports between them?

### Python

66. Write a vectorized function that returns layer losses for an array of ground-up losses, given an attachment and a limit.
67. How would you fit a lognormal to claim severities with scipy when some losses are capped at policy limits?
68. Simulate 10,000 years of a compound Poisson-lognormal process and compute the 1-in-100 annual aggregate loss. What would you check to know the simulation is right?
69. In pandas, how would you turn a transaction table into a reported loss triangle? Describe each step.
70. What do you do to make a notebook reproducible for a reviewer?

### Excel

71. How would you structure a ratemaking workbook so a reviewer can audit it in 15 minutes?
72. When would you use XLOOKUP, INDEX/MATCH, or SUMIFS? Give an insurance example of each.
73. How would you build a development triangle from a claim-level table with dynamic array formulas?
74. How do you check a workbook for errors before you send it?

### R

75. You are handed an R script that fits a GLM and writes relativities to a file. How would you work out what it does before trusting its output?

---

## 4. Behavioral questions for a career changer

76. Why are you moving from commercial real estate to insurance?
77. What from CRE underwriting and valuation transfers directly to actuarial and reinsurance work, and what doesn't?
78. You have passed P and FM. How will you balance exams with a full-time analyst role?
79. Tell me about a time you defended a valuation or underwriting conclusion to a skeptical audience.
80. Tell me about a time you found an error in your own model after it had been shared. What did you do?
81. Describe a recommendation you made with incomplete data. How did you decide it was good enough?
82. How do you respond when a manager wants a different answer than your analysis supports?
83. Three people need analysis from you by Friday. How do you decide what to do first?
84. Walk me through a project in your portfolio. What would you do differently now?
85. How do you explain a technical result to someone without a technical background? Give an example from your CRE work.
