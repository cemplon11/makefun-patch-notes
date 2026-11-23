#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one funny one-line patch note for a bug in real life / human
biology to /output/entry.txt. Pure Python stdlib only.
"""

from pathlib import Path

LINE = (
    "v2.0.7: fixed a bug where the brain replayed an embarrassing "
    "moment from 2014 at 3 a.m. instead of sleeping."
)


def main() -> None:
    # The gate requires 1-160 characters of non-whitespace UTF-8 text.
    assert 1 <= len(LINE) <= 160, f"patch note is {len(LINE)} chars"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
