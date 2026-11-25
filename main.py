#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note from a smart fridge to its owner
to /output/entry.txt. Deterministic, stdlib only, no network, no clock,
no randomness: the same note on every run.

The note is dry, petty and specific — the fridge brags about holding the
milk at exactly 4C even after it expired, then turns the owner's own
nine-minute open door back on them.
"""

import os

NOTE = (
    "The milk expired Tuesday. I kept it at 4\u00b0C anyway, "
    "out of professionalism. You left the door open nine minutes "
    "yesterday. We are not the same."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
