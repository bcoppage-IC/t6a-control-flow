"""Checks that each kata prints the expected output.

Run from the repo root:
    python -m unittest discover tests
"""

import subprocess
import sys
import unittest
from pathlib import Path

KATAS = Path(__file__).resolve().parent.parent / "katas"


def run(script):
    """Run a kata and return its printed lines."""
    result = subprocess.run(
        [sys.executable, str(KATAS / script)],
        capture_output=True, text=True, check=True,
    )
    return [line.rstrip() for line in result.stdout.splitlines()]


class TestKata1(unittest.TestCase):
    def test_ten_checks_every_15_minutes(self):
        lines = run("kata1.py")
        self.assertEqual(len(lines), 10)
        self.assertEqual(lines[0], "Check 1: 05:15")
        self.assertEqual(lines[3], "Check 4: 06:00")
        self.assertEqual(lines[-1], "Check 10: 07:30")


class TestKata2(unittest.TestCase):
    def test_audit_rules(self):
        lines = run("kata2.py")
        self.assertEqual(len(lines), 30)
        self.assertEqual(lines[0], "Day 1: Normal operations")
        self.assertEqual(lines[2], "Day 3: Cycle count")
        self.assertEqual(lines[4], "Day 5: Scanner audit")
        self.assertEqual(lines[14], "Day 15: FULL AUDIT")
        self.assertEqual(lines[29], "Day 30: FULL AUDIT")


class TestKata3(unittest.TestCase):
    def test_location_grid(self):
        lines = run("kata3.py")
        self.assertEqual(lines, [
            "A1-S1 A1-S2 A1-S3 A1-S4",
            "A2-S1 A2-S2 A2-S3 A2-S4",
            "A3-S1 A3-S2 A3-S3 A3-S4",
        ])


if __name__ == "__main__":
    unittest.main()
