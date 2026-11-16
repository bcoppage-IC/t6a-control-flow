"""Kata 2: Warehouse Audit Calendar

For days 1 to 30, apply these rules:
    Every 3rd day        -> Cycle count
    Every 5th day        -> Scanner audit
    Days that are both   -> FULL AUDIT
    Any other day        -> Normal operations

Concepts: for loop, modulo (%), if / elif / else order.
Expected output: Day 3: Cycle count, Day 5: Scanner audit,
                 Day 15: FULL AUDIT, Day 30: FULL AUDIT
"""

CYCLE_COUNT_EVERY = 3
SCANNER_AUDIT_EVERY = 5
DAYS_IN_MONTH = 30

# Days 1 to 30. range() excludes the end number.
for day in range(1, DAYS_IN_MONTH + 1):

    # True when the day divides evenly (remainder 0).
    cycle_count = day % CYCLE_COUNT_EVERY == 0
    scanner_audit = day % SCANNER_AUDIT_EVERY == 0

    # Both. Checked first so 15 and 30 aren't caught below.
    if cycle_count and scanner_audit:
        print(f"Day {day}: FULL AUDIT")

    # Every 3rd day only.
    elif cycle_count:
        print(f"Day {day}: Cycle count")

    # Every 5th day only.
    elif scanner_audit:
        print(f"Day {day}: Scanner audit")

    # Neither.
    else:
        print(f"Day {day}: Normal operations")
