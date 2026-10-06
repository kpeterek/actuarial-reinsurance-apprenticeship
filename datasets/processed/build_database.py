"""Build datasets/processed/kettlerock.sqlite from the CSV files in datasets/raw/ and datasets/reference/.

Usage (from the repository root):

    python datasets/processed/build_database.py

Every CSV is loaded as-is into a table named after the file (for example raw/claims/claims.csv -> table
"claims"). Values are not cleaned, trimmed, or converted beyond SQLite's normal column type affinity, so the
database shows exactly what the source files contain. Blank fields are stored as NULL.

Column types are assigned from the contents: identifier, code, flag and date columns are TEXT; other columns
are INTEGER or REAL when every non-blank value is numeric, otherwise TEXT. Dates are stored as TEXT.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import re
import sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
RAW = REPO / "datasets" / "raw"
REF = REPO / "datasets" / "reference"
DB = HERE / "kettlerock.sqlite"

DATASET_SEED = 20261006
DATASET_VERSION = "1.0.0"

TEXT_PATTERNS = re.compile(r"(_id|_number|_code|_date|_flag|_of|^state$|^territory$|^zip3$|^line$|^county$|month_end|"
                           r"_keys$|^lines_covered$|^reinstatements$|^basis$)")
INDEX_COLUMNS = {"policy_number", "claim_number", "occurrence_id", "location_id", "insured_id", "treaty_id",
                 "event_id", "cat_event_id", "proposal_id"}
INDEX_DATES = {"accident_date", "report_date", "transaction_date", "effective_date", "evaluation_date", "month_end"}
INT_RE = re.compile(r"^-?\d+$")
FLOAT_RE = re.compile(r"^-?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?$")


def column_type(name: str, values: list[str]) -> str:
    if TEXT_PATTERNS.search(name):
        return "TEXT"
    nonblank = [v for v in values if v != ""]
    if not nonblank:
        return "TEXT"
    if all(INT_RE.match(v) for v in nonblank):
        return "INTEGER"
    if all(FLOAT_RE.match(v) for v in nonblank):
        return "REAL"
    return "TEXT"


def load_csv(con: sqlite3.Connection, path: Path) -> tuple[str, int]:
    table = path.stem
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        header = next(reader)
        rows = [r for r in reader]
    cols = list(zip(*rows)) if rows else [[] for _ in header]
    types = [column_type(h, list(c)) for h, c in zip(header, cols)]
    con.execute(f'DROP TABLE IF EXISTS "{table}"')
    coldefs = ", ".join(f'"{h}" {t}' for h, t in zip(header, types))
    con.execute(f'CREATE TABLE "{table}" ({coldefs})')
    marks = ", ".join("?" for _ in header)
    con.executemany(f'INSERT INTO "{table}" VALUES ({marks})',
                    ([None if v == "" else v for v in r] for r in rows))
    for h in header:
        if h in INDEX_COLUMNS or h in INDEX_DATES:
            con.execute(f'CREATE INDEX "ix_{table}_{h}" ON "{table}" ("{h}")')
    return table, len(rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--seed", type=int, default=DATASET_SEED)
    ap.add_argument("--version", default=DATASET_VERSION)
    args = ap.parse_args(argv)
    files = sorted(RAW.rglob("*.csv")) + sorted(REF.glob("*.csv"))
    if not files:
        print("No CSV files found under datasets/raw or datasets/reference.")
        return 1
    tmp = DB.with_name(DB.name + ".building")
    if tmp.exists():
        tmp.unlink()
    con = sqlite3.connect(tmp)
    con.execute("PRAGMA journal_mode=OFF")
    con.execute("PRAGMA synchronous=OFF")
    counts = {}
    for f in files:
        name, n = load_csv(con, f)
        counts[name] = n
        print(f"  {name:<28} {n:>9,} rows")
    con.execute("CREATE TABLE _metadata (generated_at TEXT, seed INTEGER, generator_version TEXT, table_count INTEGER)")
    con.execute("INSERT INTO _metadata VALUES (?, ?, ?, ?)",
                (dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), args.seed, args.version, len(counts)))
    con.commit()
    con.close()
    os.replace(tmp, DB)
    print(f"Built {DB.relative_to(REPO)} with {len(counts)} tables.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
