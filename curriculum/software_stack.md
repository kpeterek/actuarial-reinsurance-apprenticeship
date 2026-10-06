# Software Stack

The tools an entry-level actuarial or reinsurance analyst meets in the first year, installed and verified on the apprenticeship machine (Windows 11). Python is the primary programming language; Excel is the primary modeling and exhibit tool; SQL is how data is pulled.

## Status (as built, 2026-10-06)

| Tool | Version | Status | First used |
|---|---|---|---|
| Python | 3.14.7 | Installed; virtualenv `C:\Users\kpeterek\venvs\actuary` (outside OneDrive) | Module 03 (light), Module 04 (main) |
| Jupyter kernel | "Python (actuary)", kernel name `actuary` | Registered | Module 04 |
| pandas | 3.0.6 | Installed | 03 |
| numpy | 2.5.3 | Installed | 04 |
| scipy | 1.18.1 | Installed | 04 |
| statsmodels | 0.15.0 | Installed | 04, 11 |
| scikit-learn | 1.9.1 | Installed | 11 |
| matplotlib / seaborn | 3.11.2 / 0.13.2 | Installed | 04 |
| openpyxl / xlsxwriter | 3.1.5 / 3.2.9 | Installed | 05 (exporting exhibits) |
| SQLAlchemy | 2.1.3 | Installed | 03 (optional) |
| jupyter (JupyterLab / Notebook) | 1.1.1 (4.6.4 / 7.6.3) | Installed | 04 |
| ipykernel | 7.4.0 | Installed | 04 |
| PyYAML, Faker | 6.0.3, 40.41.0 | Installed (used by the data build) | — |
| chainladder | 0.10.1 | Installed, optional | 06 (cross-check only, after triangles are built by hand) |
| SQLite engine | 3.50.4 (Python `sqlite3`) | Installed | 03 |
| SQLite GUI | DB Browser for SQLite or VS Code "SQLite Viewer" | **Not installed — apprentice installs before Module 02** | 02–03 |
| Microsoft Excel | Microsoft 365 desktop | Installed (dynamic arrays, LET, XLOOKUP available) | 01 |
| Power BI Desktop | Current release | **Not installed — apprentice installs before Module 02** | 02, 10 |
| Git | 2.55 | Installed; remote is a public GitHub repo | 01 |
| R + RStudio | Current release | **Not installed — apprentice installs before Module 11** | 11 |

## Python environment

The virtualenv already exists. These commands rebuild it from scratch (PowerShell, from the repo root):

```powershell
py -3.14 -m venv C:\Users\kpeterek\venvs\actuary
C:\Users\kpeterek\venvs\actuary\Scripts\python.exe -m pip install --upgrade pip
C:\Users\kpeterek\venvs\actuary\Scripts\python.exe -m pip install -r requirements.txt
C:\Users\kpeterek\venvs\actuary\Scripts\python.exe -m ipykernel install --user --name actuary --display-name "Python (actuary)"
```

Verify:

```powershell
C:\Users\kpeterek\venvs\actuary\Scripts\python.exe -c "import pandas, numpy, scipy, statsmodels, matplotlib, openpyxl, sqlalchemy, yaml; print('ok', pandas.__version__)"
C:\Users\kpeterek\venvs\actuary\Scripts\jupyter.exe kernelspec list
```

Activate in a PowerShell session (optional; the full path to `python.exe` always works):

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned   # one time, if activation is blocked
C:\Users\kpeterek\venvs\actuary\Scripts\Activate.ps1
```

Launch JupyterLab from the repo root so notebooks can find `python/` helpers:

```powershell
C:\Users\kpeterek\venvs\actuary\Scripts\jupyter.exe lab
```

Never create a virtualenv inside this OneDrive folder, and never commit `.ipynb_checkpoints/` (it is gitignored).

## The database

The SQLite database is built locally from the committed CSVs and is not stored in Git.

```powershell
C:\Users\kpeterek\venvs\actuary\Scripts\python.exe datasets/processed/build_database.py
```

Output: `datasets/processed/kettlerock.sqlite`. In Python, `python/kettlerock.py` provides `connect()` (a `sqlite3` connection) and `load(table)` (a DataFrame). If the database is ever modified by accident, delete it and rebuild.

## SQLite GUI (install before Module 02)

Either option works; DB Browser is the more complete tool.

```powershell
winget install -e --id DBBrowserForSQLite.DBBrowserForSQLite
```

or, if VS Code is installed:

```powershell
code --install-extension qwtel.sqlite-viewer
```

Open the database read-only (DB Browser: *File → Open Database Read Only*) so exploratory work cannot change it. Scripts that create tables write to a separate working database or to the student's own views, as taught in Module 03.

## Power BI Desktop (install before Module 02)

Install from the Microsoft Store (search "Power BI Desktop"), or:

```powershell
winget install --id 9NTXR16HNW1T --source msstore
```

Connecting to data, in order of preference:

1. **CSV files** (*Get Data → Text/CSV*) from `datasets/raw/` or from clean extracts the apprentice exports. Simplest and sufficient for this program.
2. **SQLite via ODBC** (optional): install the SQLite ODBC driver (64-bit) from Christian Werner's site (ch-werner.de/sqliteodbc), create a DSN pointing at `kettlerock.sqlite`, then *Get Data → ODBC*.

Details and the Module 02 dashboard requirements: [powerbi/README.md](../powerbi/README.md).

## R and RStudio (install before Module 11)

```powershell
winget install -e --id RProject.R
winget install -e --id Posit.RStudio
```

Then, in the R console:

```r
install.packages(c("readr", "dplyr", "ggplot2", "DBI", "RSQLite"))
```

Base R's `glm()` is enough for Module 11. Verify with `R.version.string` in the console. The R installer does not add `Rscript.exe` to `PATH`; run it from RStudio or by full path (`C:\Program Files\R\R-<version>\bin\Rscript.exe`).

## pandas 3 notes

pandas 3 changed several defaults. Older tutorials and Stack Overflow answers will mislead in these places.

| Change | What it means here |
|---|---|
| Copy-on-Write is always on | Chained assignment such as `df["paid"][mask] = 0` never changes `df` (pandas raises a `ChainedAssignmentError` warning). Use `df.loc[mask, "paid"] = 0`. `SettingWithCopyWarning` no longer exists. |
| Text loads as the `str` dtype | `read_csv` returns text columns as `str` (a `StringDtype`), not `object`. Tests like `df[col].dtype == object` are now `False`; use `df.select_dtypes(include="str")`. Missing text is `NaN`. |
| Datetime resolution | `pd.to_datetime` on ISO strings returns `datetime64[us]`, not `[ns]`. Harmless for this program; do not hard-code `ns` in comparisons. |
| Dates are not parsed automatically | Parse explicitly (`parse_dates=` or `pd.to_datetime(..., format=..., errors="coerce")`) and count the values that failed to parse before trusting the column. |
| Prefer assignment over `inplace=True` | Write `df = df.dropna(...)`; it is clearer and works the same under Copy-on-Write. |

Keys such as policy and claim numbers are text. Keep them as text; never let a key become a float.

## Excel

Microsoft 365 desktop with dynamic arrays, `LET`, `XLOOKUP`, `FILTER`, `UNIQUE`, `SORT`, Power Query and PivotTables. Model conventions and the two starter templates: [excel/README.md](../excel/README.md).

## Git (taught in Module 01)

The repository is published on GitHub (public). Commands used in this program:

| Command | Purpose |
|---|---|
| `git status` | What changed; what is staged |
| `git add <file>` / `git add -A` | Stage changes (`.gitignore` is respected) |
| `git commit -m "Module 01: build 01-A results review"` | Record a change with a descriptive message |
| `git log --oneline` | Version history |
| `git diff` / `git diff --staged` | What changed, line by line |
| `git switch -c <branch>` | Branch for an experiment (introduced, rarely needed) |
| `git push origin main` | Publish to GitHub |

Rules: commit at the end of every session; close Excel workbooks before committing (lock files are ignored, open workbooks may be half-saved); grading answer keys under `solutions/` are local-only and gitignored — never force-add them.

## OneDrive

The repository sits in a OneDrive-synced folder. Keep the virtualenv outside it, close files before Git operations, and pause OneDrive sync if Git reports a locked file.
