# Module 01 — How a P&C Insurer Actually Works

**Phase I — Insurance Operating System · Gate: 90 · Estimated 8–10 hours**

These are your running notes. Each concept is added here after we cover it in session, so this file grows as you go. Exercise 01-A is assigned after concept 8.

| # | Concept | Status |
|---|---|---|
| 1 | The insurer's business model | In progress |
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
