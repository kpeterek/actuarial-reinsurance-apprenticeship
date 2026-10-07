# Module 01 — How a P&C Insurer Actually Works

**Phase I — Insurance Operating System · Gate: 90 · Estimated 8–10 hours**

These are your running notes. Each concept is added here after we cover it in session, so this file grows as you go. Exercise 01-A is assigned after concept 8.

| # | Concept | Status |
|---|---|---|
| 1 | The insurer's business model | In progress — open until you say it is settled |
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

### One policy, start to finish

A Dallas trucking company buys a year of auto liability insurance on January 1, 2025, for $100,000.

| Date | Event | Accounting effect at the insurer |
|---|---|---|
| Jan 2025 | Premium received | Cash (asset) +$100,000 |
| Jan 2025 | Commission and the insurer's own costs paid | Cash (asset) −$18,000; expense $18,000 |
| Mar 2025 | A truck rear-ends a car and the driver sues. The adjuster estimates the case will settle for $80,000. | Loss reserve (liability) +$80,000; loss expense $80,000. **No cash moves.** |
| 2025–2028 | The lawsuit runs. The insurer's assets stay invested in bonds. | Investment income (revenue) earned on the assets |
| Mar 2028 | The case settles and is paid | Cash (asset) − settlement; loss reserve (liability) −$80,000 |

In practice the insurer's cash and bonds are pooled across all policies. Nothing is set aside for this particular claim. Following one policy's cash on its own is only for illustration.

### What a loss reserve is
- A **loss reserve** is an **accounting liability**: the insurer's **actuarial estimate** of what it still owes on claims that have already happened.
- It is **not** a segregated pile of cash. The insurer's **assets** (cash and bonds) support its liabilities.
- Investment income is earned on **assets**, never on the liability.

### When the settlement differs from the estimate
**Surplus** is assets minus liabilities, measured at a date. It is the insurer's equity.

| Settlement | Assets | Loss reserve (liability) | Surplus |
|---|---|---|---|
| $80,000, equal to the estimate | −$80,000 | −$80,000 | No change |
| $88,000, above the estimate | −$88,000 | −$80,000 | **−$8,000** |
| $60,000, below the estimate | −$60,000 | −$80,000 | **+$20,000** |

The estimate does not change how much cash is eventually paid. It changes how much profit the insurer reports, and how large its liabilities and surplus are, while the claim is open.

### Stocks and flows

| Item | Type |
|---|---|
| Premium for a year | FLOW (over a period) |
| Claims paid during a year | FLOW |
| Investment income during a year | FLOW |
| Loss reserves at 12/31 | STOCK (balance at a date) |
| Surplus at 12/31 | STOCK |

A slow-paying insurer has claims from many past years still open at once. Its loss reserves (a stock) can therefore be several times its annual premium (a flow). A reserve-to-annual-premium ratio of 2.5× does **not** mean every new premium dollar requires $2.50 of reserves. It means the estimated unpaid claims from every year with claims still open, added together at one date, equal 2.5 years of premium.

### Two sources of profit
1. **Underwriting result** (a flow) = premium − losses − the cost of handling claims (adjusters, defense lawyers) − underwriting expenses (commissions, salaries, premium taxes). The **combined ratio** expresses the same thing per dollar of premium: below 100% means an underwriting profit. Concepts 3 and 5 make the premium figure and the ratio precise.
2. **Investment income** (a flow) on the assets the insurer holds, which are larger for an insurer that pays claims slowly.

A 100% combined ratio can still be a profitable business if investment income is large enough.

### Harbor vs Longview
Longview pays claims slowly, so it holds far more assets relative to its premium and earns far more investment income than Harbor. That advantage is only real if Longview's estimates of what it owes are accurate. Its loss reserves are large, so an estimating error of a few percent can cost more than a year of investment income and comes straight out of surplus. Harbor's results are smaller but much closer to certain.

### One analogy
Holding premium before claims are paid works like low-cost financing: the insurer invests money it will owe later. Unlike a loan, the amount owed is an estimate, and the true amount is only known when claims settle.

### Common mistakes
- Treating a loss reserve as cash rather than as a liability supported by assets.
- Comparing a stock (reserves at a date) with a flow (premium for a year) without saying so.
- Treating a reported combined ratio as a fact rather than as something built on estimates.