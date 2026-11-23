#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry -- a single-line safety warning label for every human
being, 160 characters or fewer -- to /output/entry.txt.
"""

import os

# Entry for u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85:
# one warning label, exactly 120 characters, punchline at the end.
ENTRY = (
    "WARNING: This human contains strong opinions, selective hearing, "
    "and a hair-trigger response to being told to calm down."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
