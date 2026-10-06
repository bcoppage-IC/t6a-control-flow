# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start


hour = 5

minute = 0

for check in range(1, 11):
    minute = minute + 15
    if minute == 60:
        minute = 0
        hour = hour + 1

    print(f"Check {check}: {hour:02d}:{minute:02d}")

