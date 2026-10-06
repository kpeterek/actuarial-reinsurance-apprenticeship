# Datasets: Kettlerock Mutual Insurance Company

Every exercise and capstone in this program uses one data universe: **Kettlerock Mutual Insurance Company** ("Kettlerock"), a fictional regional commercial-lines mutual insurer. Kettlerock is not a real company, and none of the policyholders, agents, claims or reinsurers in these files are real.

| | |
|---|---|
| Lines of business | Commercial Auto Liability and physical damage (CA), General Liability (GL), Commercial Property (CP), Workers' Compensation (WC) |
| States | Texas, Louisiana, Oklahoma, Arkansas, New Mexico, Colorado |
| Policy terms | Annual policies effective 2016-01-01 through 2025-12-31 |
| Evaluation date | **2025-12-31**. Every transaction file is cut off at this date. |
| Reinsurance | Historical treaty program 2016-2025, ceded loss detail, and proposals and indicative quotes for 2026 |
| Catastrophe | Historical cat events, a stochastic event catalog, event loss table, and a 10,000-year year loss table |

> **This data is synthetic and contains realistic data-quality problems. Validate before use.**

## Folder map

```
datasets/
├── raw/                    transaction-level source extracts, as delivered by Kettlerock's systems
│   ├── policies/           policies.csv, policy_coverages.csv, locations.csv
│   ├── premiums/           premium_transactions.csv
│   ├── claims/             claims.csv, claim_transactions.csv
│   ├── exposures/          exposure_snapshots.csv
│   ├── reinsurance/        treaty_terms.csv, ceded_loss_transactions.csv, treaty_proposals_2026.csv,
│   │                       reinsurer_quotes_2026.csv, casualty_ilf_table.csv, property_exposure_curves.csv
│   └── catastrophe/        historical_cat_events.csv, event_catalog.csv, event_loss_table.csv, year_loss_table.csv
├── reference/              lookup tables: rate_change_history, expense_assumptions, class_codes,
│                           territory_codes, cause_of_loss_codes, county_region_map
├── processed/              build_database.py -> kettlerock.sqlite (built locally, not committed)
├── data_dictionary/        README.md (diagram, grain, keys, join paths) and one page per table
└── synthetic_generators/   note on how the data is produced
```

The raw layer is left exactly as extracted. Building clean, analysis-ready tables from it is part of the coursework (Modules 02 and 03).

## Building the database

From the repository root, with the course virtual environment active:

```
python datasets/processed/build_database.py
```

This loads every CSV in `raw/` and `reference/` into `datasets/processed/kettlerock.sqlite`, one table per file, without cleaning anything. It takes well under a minute. Rebuild it whenever the CSVs change.

Then, from Python:

```python
import sys; sys.path.append("python")
from kettlerock import load, tables
claims = load("claims")
```

or open `kettlerock.sqlite` in DB Browser for SQLite or the VS Code "SQLite Viewer" extension.

## Where to start

Read [`data_dictionary/README.md`](data_dictionary/README.md) first: it shows how the tables join and what one row of each table means.
