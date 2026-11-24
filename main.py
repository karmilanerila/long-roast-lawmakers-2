#!/usr/bin/env python3
"""Backup angle-2 entry for the Long Roast bounty.

One satirical sentence: a senator who writes the rules for crypto and
the internet cannot open an email attachment on his own.
"""

import os

ENTRY = (
    "The senator drafting the nation's crypto rules just asked his aide to "
    "open an email attachment for him, because the PDF was hiding inside "
    "a zip file he has now forwarded to IT three times since Tuesday."
)

def validate(text):
    """Gate: UTF-8 text, 1-320 chars, not only whitespace, one sentence."""
    if not (1 <= len(text) <= 320 and text.strip()):
        raise ValueError("entry out of gate bounds")
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
