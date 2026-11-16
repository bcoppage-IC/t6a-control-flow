"""Kata 1: Scanner Health Checks

A Medline branch checks its handheld scanners every 15 minutes.
Print the first 10 check times, starting from a 05:00 shift start.

Concepts: for loop, counter, named constants, hour rollover.
Expected output: Check 1: 05:15 ... Check 10: 07:30
"""

START_HOUR = 5               # shift starts at 0500
CHECK_INTERVAL_MINUTES = 15  # scanners are checked every 15 minutes
TOTAL_CHECKS = 10

hour = START_HOUR
minute = 0

for check in range(1, TOTAL_CHECKS + 1):
    minute = minute + CHECK_INTERVAL_MINUTES
    if minute >= 60:         # roll over to the next hour
        minute = minute - 60
        hour = hour + 1

    print(f"Check {check}: {hour:02d}:{minute:02d}")
