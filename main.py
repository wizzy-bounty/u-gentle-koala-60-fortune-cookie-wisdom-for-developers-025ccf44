#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt.

The line is written from one specific truth of a developer's day:
comments rot and lie, while the code itself is the only honest
witness. The fortune turns that truth around: believe the code's
confession, and make the next comment you write a true one.

Gate (from the competition rules): /output/entry.txt must be UTF-8
text of 1 to 120 characters, not only white space, on a single line.
This program validates the line before writing it and fails loudly
if the line ever stops satisfying the gate.
"""

import os
import sys

# The fortune, written fresh for this entry. One line, one breath.
FORTUNE = (
    "The comment lies; the code confesses. "
    "Trust the confession, and write the next comment true."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def validate(line: str) -> None:
    """Check the fortune against the competition gate.

    Raises ValueError with a clear message on the first failure.
    """
    if not line:
        raise ValueError("fortune is empty: entry must be 1-120 characters")
    if line.strip() == "":
        raise ValueError("fortune is only whitespace: entry must say something")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune spans more than one line: entry must be one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"fortune is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    try:
        validate(FORTUNE)
    except ValueError as exc:
        print(f"invalid fortune: {exc}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)

    print(f"wrote {len(FORTUNE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
