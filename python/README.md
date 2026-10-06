# Python helpers

Python is the primary analysis language in this program, used as an actuarial tool rather than for software engineering. This folder holds the small shared modules that accumulate as the apprenticeship progresses.

## What is here

| Module | Provided by | Purpose |
|---|---|---|
| `kettlerock.py` | The data build (the only helper provided for free) | `connect()` returns a `sqlite3` connection to `datasets/processed/kettlerock.sqlite`; `load(table)` returns a table as a pandas DataFrame |
| `triangles.py` | Written in class, Module 06 | Build triangles from transactions; age-to-age factors; projections |
| `layers.py` | Written in class, Module 08 | Layer loss, limited expected value, reinstatement mechanics |
| `simulate.py` | Written in class, Modules 08–10 | Frequency/severity and aggregate loss simulation |

Everything except `kettlerock.py` is written by the apprentice when the corresponding module teaches it. Helpers are created only after the method has been done by hand at least once (in Excel or a notebook), so the code encodes understanding rather than replacing it.

## Using the helpers from a notebook

Notebooks live in submission folders, so locate the repo root first:

```python
from pathlib import Path
import sys

ROOT = next(p for p in [Path.cwd(), *Path.cwd().parents] if (p / "CLAUDE.md").exists())
sys.path.insert(0, str(ROOT / "python"))

import kettlerock
claims = kettlerock.load("claims")
```

Use the "Python (actuary)" kernel. Environment details and pandas 3 notes: [curriculum/software_stack.md](../curriculum/software_stack.md).

## Conventions

- Functions with docstrings that state inputs, outputs and units. No classes unless they clearly help.
- No hidden state: a function's result depends only on its arguments.
- Every helper gets a short check against a hand calculation (a tiny example in the docstring or a `__main__` block).
- Notebooks run top to bottom on a fresh kernel. Restart and run all before submitting.
- Results exported to Excel go through `openpyxl` or `xlsxwriter`, never copy-paste from the notebook display.
