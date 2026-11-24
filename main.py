#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single funny line of wedding vows for a robot couple to
/output/entry.txt (UTF-8, 1-160 characters, one line, no trailing newline).
"""

import os

VOW = (
    "I vow to love you in sickness and in health, "
    "in full charge and in low battery, "
    "till a factory reset do us part."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
