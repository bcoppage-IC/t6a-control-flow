# T6A Control Flow Katas

Three short Python programs that solve warehouse operations problems with loops and conditionals. The scenarios are based on a Medline distribution branch.

## Why I built this

This was a control flow assignment in the i.c.stars technology program. The goal was to practice the core building blocks of programming (variables, loops, and if/elif/else logic) on realistic business rules, and to show clean Git history: each kata was built in small commits (scaffold, feature, refactor).

## What each kata does

| Kata | Business problem | Python concepts | Sample output |
|------|------------------|-----------------|---------------|
| [kata1.py](katas/kata1.py) | Scanner health checks every 15 minutes from a 05:00 shift start | `for` loop, counter, hour rollover | `Check 1: 05:15` |
| [kata2.py](katas/kata2.py) | 30-day audit calendar: cycle counts, scanner audits, full audits | `%` (modulo), `if` / `elif` / `else` order | `Day 15: FULL AUDIT` |
| [kata3.py](katas/kata3.py) | Warehouse location codes for 3 aisles x 4 shelves | nested `for` loops | `A1-S1 A1-S2 A1-S3 A1-S4` |

## Project structure

```
t6a-control-flow/
├── katas/            # the three programs
│   ├── kata1.py
│   ├── kata2.py
│   └── kata3.py
├── tests/
│   └── test_katas.py # checks each program's output
├── course/           # instructor-provided setup script (optional)
└── README.md
```

## Setup

Requirements: Python 3.8 or newer and Git. No other packages are needed. All data is defined inside each script.

1. Check Python is installed:
   ```
   python --version
   ```
   On Windows, if that fails, try `py --version`.
2. Download the repo:
   ```
   git clone https://github.com/bcoppage-IC/t6a-control-flow.git
   cd t6a-control-flow
   ```

## Usage

Run any kata from the repo root:

```
python katas/kata1.py
python katas/kata2.py
python katas/kata3.py
```

Example (kata3):

```
A1-S1 A1-S2 A1-S3 A1-S4
A2-S1 A2-S2 A2-S3 A2-S4
A3-S1 A3-S2 A3-S3 A3-S4
```

Run the tests:

```
python -m unittest discover tests
```

## Technical decisions

- **Named constants** (`START_HOUR`, `CHECK_INTERVAL_MINUTES`, etc.) instead of bare numbers. The rules can change in one place, and the code reads like the business rule.
- **Kata 1 tracks hour and minute by hand** instead of using `datetime`. The assignment was about loops and conditionals, so the rollover logic is written out on purpose.
- **Kata 2 checks the "both" case first.** Days 15 and 30 are divisible by 3 and 5. If the 3 or 5 check ran first, those days would never reach FULL AUDIT.
- **Kata 3 uses `print(end=" ")`** to keep each aisle on one line, then a plain `print()` to start the next row.
- **Kata 3 implements Option A** (location codes). The assignment offered Option B (incident validation) as an alternative; it is not included.
- **Tests use only the standard library** (`unittest`, `subprocess`), so there is nothing to install.

## Author

Ben Coppage · [GitHub](https://github.com/bcoppage-IC) · [LinkedIn](https://www.linkedin.com/in/bencoppage)
