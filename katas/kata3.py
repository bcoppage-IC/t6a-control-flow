"""Kata 3 (Option A): Location Codes

Print the warehouse location codes for 3 aisles x 4 shelves,
one row per aisle.

Concepts: nested for loops, print(end=" ") to stay on one line.
Expected first row: A1-S1 A1-S2 A1-S3 A1-S4

The assignment offered two options. This repo implements Option A.
Option B (Incident Validation with guard clauses) was not attempted.
"""

AISLES = 3
SHELVES_PER_AISLE = 4

# Aisles 1 to 3.
for aisle in range(1, AISLES + 1):

    # Shelves 1 to 4. end=" " keeps codes on one line.
    for shelf in range(1, SHELVES_PER_AISLE + 1):
        print(f"A{aisle}-S{shelf}", end=" ")

    # New line after each aisle.
    print()
