# Warehouse Audit Calendar
# For days 1–30, apply these rules:

# Every 3rd day → Cycle count
# Every 5th day → Scanner audit
# Days that are both → FULL AUDIT
# Any other day → Normal operations

# Expected: Day 3: Cycle count, Day 5: Scanner audit, Day 15: FULL AUDIT, Day 30: FULL AUDIT

# Days 1 to 30. range() excludes the end number.
for day in range(1, 30 + 1):

    # 0 means divisible by 3.
    cycle_count = day % 3

    # 0 means divisible by 5.
    scanner_audit = day % 5

    # Both. Checked first so 15 and 30 aren't caught below.
    if cycle_count == 0 and scanner_audit == 0:
        print(f"FULL AUDIT DUE, {day}")

    # 3 only.
    elif cycle_count == 0:
        print(f"CYCLE COUNT DUE, {day}")

    # 5 only.
    elif scanner_audit == 0:
        print(f"SCANNER AUDIT DUE, {day}")

    # Neither.
    else:
        print(f"MISSED COUNTS AND AUDITS, {day}")

    

   