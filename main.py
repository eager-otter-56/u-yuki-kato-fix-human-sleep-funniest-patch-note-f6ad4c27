#!/usr/bin/env python3
"""Entry for Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes announcing that human sleep is fixed.
The fix: sleep now checkpoints at 23:00 and restores at 07:00. The bug
was the agent restoring the 03:12 checkpoint 19 nights in a row.
"""
import os

ENTRY = "Fixed: sleep now checkpoints at 23:00 and restores at 07:00; previously it restored the 03:12 checkpoint 19 nights in a row."

def main():
    # Gate: UTF-8 text, 1-160 characters, single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 160, len(ENTRY)
    assert "\n" not in ENTRY and ENTRY.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
