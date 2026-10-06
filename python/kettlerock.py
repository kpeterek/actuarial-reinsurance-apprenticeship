"""Helpers for the Kettlerock Mutual training database.

    import sys; sys.path.append("python")      # if running from the repository root
    from kettlerock import connect, load, tables

    tables()                 # list the tables
    claims = load("claims")  # one table as a pandas DataFrame
    con = connect()          # sqlite3 connection for your own SQL
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = REPO_ROOT / "datasets" / "processed" / "kettlerock.sqlite"


def connect() -> sqlite3.Connection:
    """Open a connection to datasets/processed/kettlerock.sqlite."""
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found at {DB_PATH}.\n"
            "Build it first, from the repository root:\n"
            "    python datasets/processed/build_database.py"
        )
    return sqlite3.connect(DB_PATH)


def tables() -> list[str]:
    """Names of all tables in the database."""
    con = connect()
    try:
        rows = con.execute("SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name").fetchall()
    finally:
        con.close()
    return [r[0] for r in rows]


def load(table: str) -> pd.DataFrame:
    """Return one table as a DataFrame, exactly as stored (no cleaning)."""
    if table not in tables():
        raise ValueError(f"Unknown table {table!r}. Available: {', '.join(tables())}")
    con = connect()
    try:
        return pd.read_sql_query(f'SELECT * FROM "{table}"', con)
    finally:
        con.close()
