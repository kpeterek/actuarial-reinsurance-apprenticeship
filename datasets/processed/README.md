# Processed: the Kettlerock SQLite database

This folder holds `build_database.py`, which builds `kettlerock.sqlite` from the CSV files in `datasets/raw/` and `datasets/reference/`. The database file itself is not committed to Git (it is listed in `.gitignore`); build it locally.

## Build

From the repository root:

```
python datasets/processed/build_database.py
```

The script prints each table and its row count and finishes with `Built datasets/processed/kettlerock.sqlite with N tables.`

## What the database contains

- **One table per CSV file**, named after the file without `.csv` (for example `claims`, `claim_transactions`, `treaty_terms`, `class_codes`). Raw and reference tables sit side by side in the same database.
- **Values exactly as they appear in the CSV.** Nothing is cleaned, trimmed, de-duplicated, re-formatted or filled in. Blank fields are stored as `NULL`.
- **Column types** assigned from the contents: identifier, code, flag and date columns are `TEXT`; other columns are `INTEGER` or `REAL` when every non-blank value is numeric, otherwise `TEXT`. SQLite has no date type, so dates are `TEXT`.
- **Indexes** on the join keys (`policy_number`, `claim_number`, `occurrence_id`, `location_id`, `insured_id`, `treaty_id`, `event_id`, `cat_event_id`, `proposal_id`) and the main date columns (`accident_date`, `report_date`, `transaction_date`, `effective_date`, `evaluation_date`, `month_end`). Indexes are not unique. Add your own with `CREATE INDEX` if a query needs one.
- **`_metadata`**: one row with the build timestamp (UTC), dataset seed, dataset version and table count.

No primary keys or foreign keys are enforced. Checking keys, grain and referential integrity is your job.

## Using it

- Python: `python/kettlerock.py` provides `connect()`, `load(table)` and `tables()`.
- SQL in a GUI: open the file in DB Browser for SQLite or the VS Code "SQLite Viewer" extension.
- Power BI: connect to the CSVs directly, or to the SQLite file through an ODBC driver (see `powerbi/README.md`).

Table definitions, grain and join paths are in [`../data_dictionary/README.md`](../data_dictionary/README.md).
