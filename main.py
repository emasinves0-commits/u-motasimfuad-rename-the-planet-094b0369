#!/usr/bin/env python3
"""Rename the Planet — writes the entry line to /output/entry.txt.

Deterministic: the entry is a fixed string; the program only validates it
(1-200 characters, not whitespace-only, UTF-8) and writes it with no
trailing newline.
"""
import os

ENTRY = "Rename Venus 'The Two-Hour Hotel': every probe that checks in dies within two hours \u2014 crushed, melted, and still charged full price."

def main():
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry is whitespace only"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)

if __name__ == "__main__":
    main()
