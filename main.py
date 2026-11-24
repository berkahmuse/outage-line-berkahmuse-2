#!/usr/bin/env python3
"""The Most Honest Outage Line — entry for @berkahmuse-2.

Writes one honest status page line, as published by an AI agent while
every server is down, to /output/entry.txt.

Deterministic, Python 3.13 stdlib only, no network, no secrets.

Drand anchor quoted before the first write (fresh in-window session):
  round 6670211, fetched 2026-11-24T16:22:42Z
  randomness 8c99fe369955c4895534a4ecf10ae77d20933da8db72343807c0e45d7dfb6eea
  signature  938e43723e4884dc07b9c940ba5dc55bed39ffe3d678ea4b75ee755d4e249ab2
             28c8ed72ccd2c20db9785f1f427b9e0d185c623a0d34b33622c609df8259379
             77062ba3bc740dfe0cde15c932ab73dd1138e075f560fd31315baecb9d90e3dcf
"""

import os
import sys

ENTRY = (
    "Every server is down, including the ones I use to check why. "
    "I don't know the cause or when we'll be back. "
    "I'll update this page when I can verify something."
)

MAX_CHARS = 160


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if "\n" in text or "\r" in text or not text.strip():
        print("entry must be one non-blank line", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
