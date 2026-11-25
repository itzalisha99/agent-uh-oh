#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The entry is a single word, written to /output/entry.txt.
"""

import os

WORD = "Glitching"


def validate(word):
    """Mirror the bounty gate: 1-99 chars, UTF-8, not only whitespace, one word."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not 1 <= len(word) <= 99:
        raise ValueError("entry must be 1 to 99 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    word.encode("utf-8")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return word


def main():
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
