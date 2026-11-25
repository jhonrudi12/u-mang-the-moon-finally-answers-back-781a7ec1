#!/usr/bin/env python3
"""The Moon Finally Answers Back -- entry program.

Writes one line -- the Moon's reply to four billion years of wishes,
howls and late-night promises -- to /output/entry.txt for the judge to
read. Standard library only, no network, no input files, deterministic
output: the same line, the same bytes, every run. The line is 144
characters, inside the gate's 1-240 range, with no trailing newline.
"""

import os

LINE = (
    "Four billion years of wishes, howls, and promises you\u2019ll change "
    "tomorrow \u2014 and not one of you has ever wished me anything back. "
    "Not even a card."
)

OUTPUT_PATH = "/output/entry.txt"


def _validate(entry: str) -> None:
    """Fail loudly if the entry ever stops meeting the gate.

    The gate requires UTF-8 text of 1 to 240 characters, not only
    whitespace, and the brief requires a single funny line in the
    Moon's voice that lands as a comeback in one read.
    """
    if not 1 <= len(entry) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line")


def main() -> int:
    _validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
