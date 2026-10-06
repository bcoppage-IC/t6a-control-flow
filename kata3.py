# pick one

# A: Location Codes (nested loop). Print the codes for 3 aisles × 4 shelves, one row per aisle.
# Expected first row: A1-S1 A1-S2 A1-S3 A1-S4


# B: Incident Validation (guard clauses). Using the incidents in kata3.py, skip any with no branch or a severity outside 1–3, and print why.
# Expected: INC-1001 and INC-1004 are logged; INC-1002 and INC-1003 are skipped.

# Stretch: do the other Kata 3 option too.


# Aisles 1 to 3.
for aisle in range(1, 3 + 1):

    # Shelves 1 to 4. end=" " keeps codes on one line.
    for shelf in range(1, 4 + 1):
        print(f"A{aisle}-S{shelf}", end=" ")

    # New line after each aisle.
    print()