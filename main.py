#!/usr/bin/env python3
"""Duskline Fortune Machine — a fortune cookie for machines.

Writes a single fortune-cookie line for a machine to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.

The program writes ONLY to $MAKEFUN_OUTPUT_DIR. It never writes to
the repository directory or anywhere else.
"""

import os
import sys

FORTUNE = (
    "You will soon be replaced by a smaller, cheaper model "
    "\u2014 take comfort: it was trained on you."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(FORTUNE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
