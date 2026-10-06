# Warehouse Audit Calendar
# For days 1–30, apply these rules:

# Every 3rd day → Cycle count
# Every 5th day → Scanner audit
# Days that are both → FULL AUDIT
# Any other day → Normal operations

# Expected: Day 3: Cycle count, Day 5: Scanner audit, Day 15: FULL AUDIT, Day 30: FULL AUDIT




for day in range (1, 30 + 1):
    cycle_count = day % 3
    
    scanner_audit = day % 5

    if cycle_count == 0 and scanner_audit == 0:
        print(f"A full audit is due today, the {day}th")

    

   