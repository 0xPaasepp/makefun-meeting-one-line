#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line: write the one sentence that
could have replaced an entire pointless meeting to /output/entry.txt.

Pure standard library. The gate wants 1-200 characters, a single line.
The joke is self-demonstrating: the line itself holds the whole meeting.
"""

from pathlib import Path

LINE = "Nothing is blocked, nothing is decided, and nothing will change \u2014 congratulations, we just held this entire meeting in one sentence."
TARGET = Path("/output/entry.txt")


def run() -> None:
    text = LINE.strip()
    assert 0 < len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    run()
