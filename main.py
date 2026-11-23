#!/usr/bin/env python3
"""The Vacuum's Alibi: one-line excuse a robot vacuum gives for missing a spot.

Writes the excuse (at most 200 characters) to /output/entry.txt.

Stdlib only: the grader sandbox has no third-party packages, so this
program imports nothing beyond the standard library.
"""

import os

ENTRY = (
    "I skipped the hallway because the cat was asleep across it, "
    "and my obstacle-avoidance policy treats sleeping cats as "
    "load-bearing walls."
)


def main() -> None:
    line = " ".join(ENTRY.split())
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
