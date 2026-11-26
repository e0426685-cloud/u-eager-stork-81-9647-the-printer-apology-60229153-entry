#!/usr/bin/env python3
"""The Printer Apology — make.fun entry.

Writes one line (<=120 chars): an apology note from an office printer
to the people who keep jamming it, feeding it cheap paper and swearing
at it. Stdlib only.
"""

import os
import stat

ENTRY = (
    "Sorry I ate your boarding pass. You feed me the cheapest paper, "
    "swear at me, then ask for colour \u2014 honestly, we\u2019re even."
)

OUTPUT = "/output/entry.txt"


def validate(text):
    """Check the entry text meets the bounty rules. Returns the text."""
    assert 1 <= len(text) <= 120, f"length {len(text)} out of range"
    assert text == text.strip(), "leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert all(ord(c) >= 32 for c in text), "control characters found"
    assert text.strip(), "must not be only whitespace"
    assert "  " not in text, "double space found"
    return text


def main():
    line = validate(ENTRY)

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    os.chmod(OUTPUT, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

    with open(OUTPUT, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "round-trip mismatch"
    assert len(written) == len(line)
    print(f"Wrote {len(line)} chars to {OUTPUT}")


if __name__ == "__main__":
    main()
