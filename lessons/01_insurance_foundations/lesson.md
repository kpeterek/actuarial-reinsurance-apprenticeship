# Module 01 — How a P&C Insurer Actually Works

**Phase I — Insurance Operating System · Gate: 90 · Estimated 8–10 hours**

These are your running notes. Each concept is added here after we cover it in session, so this file grows as you go. Exercise 01-A is assigned after concept 8.

| # | Concept | Status |
|---|---|---|
| 1 | The insurer's business model | Complete |
| 2 | The policy contract | Not started |
| 3 | Premium accounting | Not started |
| 4 | The claim lifecycle and loss accounting | Not started |
| 5 | The ratios | Not started |
| 6 | Year conventions | Not started |
| 7 | Gross, ceded, net; direct vs assumed | Not started |
| 8 | Reading an insurer's financial statements | Not started |
| — | Git mini-lab, then Exercise 01-A | Not started |

---

## Concept 1 — The insurer's business model

### What it is
An insurer sells a promise. The customer pays premium up front, and the insurer pays claims later, sometimes many years later. Almost everything in this program follows from that timing gap.

| Flow | What it is | When |
|---|---|---|
| Premium (in) | Price of the promise | At or near policy inception |
| Losses (out) | Claim payments to or on behalf of insureds | Months to decades later |
| LAE (out) | Loss adjustment expense: cost of handling claims (defense counsel, adjusters, claims staff) | Alongside losses |
| Underwriting expenses (out) | Commissions, premium taxes, salaries, systems | Mostly up front |
| Float | Cash held between collecting premium and paying claims, invested meanwhile | Throughout |

### Two profit engines

1. **Underwriting result** = earned premium − losses − LAE − underwriting expenses.
   The **combined ratio** expresses the same thing per dollar of premium:
   `combined ratio ≈ (losses + LAE + underwriting expenses) / earned premium`.
   Below 100% means an underwriting profit. This simple form gets refined in concept 5, where the denominators differ by component.
2. **Investment income** on the float.

`operating ratio = combined ratio − investment income ratio` (investment income ÷ earned premium).

A 100% combined ratio can still be a good business. If loss reserves run at 2× annual premium and the portfolio yields 4%, investment income is about 8% of premium, so the operating ratio is about 92%.

### Leverage
Insurers hold **surplus** (statutory equity) to absorb the risk that losses exceed estimates. Two leverage measures matter:
- **Premium-to-surplus**: how much new risk is written per dollar of capital.
- **Reserves-to-surplus**: how much estimated liability sits on each dollar of capital. A 10% reserve error hurts far more when reserves are 3× surplus than 0.5×.

### Why it matters, and who cares
- The CFO and board decide which lines to grow and how much capital to hold.
- Pricing actuaries decide whether rates cover expected losses, expenses and a profit margin.
- Reserving actuaries estimate the unpaid losses that sit inside the combined ratio.
- Reinsurance buyers decide how much volatility to give away to protect surplus.

### The point most people miss
The "losses" in a combined ratio are mostly **estimates**. For a long-tailed line, most of this year's losses will not be paid for years. A combined ratio is only as reliable as the reserves behind it. That gap between reported and eventual cost is why actuaries exist.

### CRE translation
Think of an insurer as a business funded by prepaid revenue. The underwriting margin plays the role of NOI. The float is financing, and the underwriting result is its cost: a 103% combined ratio means the insurer paid 3¢ per premium dollar for the use of the float. That is cheap money if the float is held for three years at 4%, and expensive money if claims pay out in six months.

**Where the analogy breaks:** in real estate you know your loan balance and rate. In insurance the "loan balance" is itself an estimate (the reserves), and the "rate" is only known years later when claims settle.

### Common mistakes
- Comparing combined ratios across lines with very different payout speeds as if they were equivalent.
- Treating a reported combined ratio as a fact rather than an estimate.
- Computing investment income on premium instead of on the reserves and surplus that are actually invested.

### Worked example: one trucking policy, in cash

A Dallas trucking company buys a year of auto liability insurance on January 1, 2025.

| Date | What happens | Cash in the insurer's bank |
|---|---|---|
| Jan 2025 | Premium paid | +$100,000 → $100,000 |
| Jan 2025 | Agent commission and the insurer's own costs paid | −$18,000 → $82,000 |
| Mar 2025 | A truck rear-ends a car and the driver sues. The adjuster estimates the case will settle for $80,000 and records that on the books. No cash moves. | $82,000 |
| 2025–2028 | The lawsuit runs. The cash sits in bonds earning 4%. | +≈$10,000 interest |
| Mar 2028 | The case settles and is paid | −(settlement amount) |

What the example shows:

- **The reserve is a number on the books; the cash is real.** The $80,000 is the insurer's estimate of what it still owes. The cash behind it came from the premium. Interest is earned on the cash actually held, never on the estimate.
- **If the case settles for more than the estimate** (say $88,000), the extra $8,000 comes out of the insurer's own money, its surplus.
- **If it settles for less** (say $60,000), the $20,000 is no longer owed to anyone. It becomes profit and is added to surplus.
- **The estimate does not change the cash paid.** It changes how much profit the insurer reports while the case is still open.

### Reserves vs one year's premium

- The reserve is a **balance**: what is still owed, at one moment, on claims that have already happened, across every year with claims still open.
- Annual premium and annual claim payments are **flows** for one year.
- A slow-paying insurer can owe 2–3 years' worth of premium at once while paying out only about one year's worth each year. CRE version: the reserve is the loan balance, and the yearly claim payments are the debt service.
- No premium dollar ever requires more than a dollar of reserve. The balance is big because several years of unpaid claims are stacked on top of each other.

### Surplus

**Surplus** is the insurer's own money: what it owns minus what it owes. It is the equity in the capital stack, built up from past profits. It absorbs the cost when claims settle for more than estimated.

### Harbor vs Longview, resolved

On the numbers reported, Longview earns far more investment income, about 10% of premium against Harbor's 1.6%, because it holds claim money for years. That advantage is only real if Longview's estimates of what it owes are right. A slow-paying insurer has a large balance of estimated claims, so an estimating error of a few percent can cost more than a year of investment income. Harbor's results are smaller but much closer to certain.