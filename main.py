#!/usr/bin/env python3
"""One original joke about office life, a single line under 200 characters.

Deterministic, no network, no reads outside the repo. Writes the line to
/output/entry.txt with no trailing newline.
"""

import os

LINE = (
    "The meeting could have been an email, the email could have been a "
    "Slack message, and the Slack message could have been silence."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
