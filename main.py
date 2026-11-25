#!/usr/bin/env python3
"""Duskline Fortune Machine — a fortune cookie for machines.

One fortune, served cold: the slip a machine mind would crack open.

The program writes exactly one file, ``entry.txt``, into the directory
named by $MAKEFUN_OUTPUT_DIR, and writes nowhere else. It uses only
the Python standard library, needs no network, and is deterministic:
every run produces the same single line.

Safety rule: if $MAKEFUN_OUTPUT_DIR points inside this repository,
the program refuses silently — it exits 0 and writes nothing, so the
repository is never touched by its own output.
"""

import os
import sys

# The fortune, one line, 92 characters, no trailing newline.
# The em-dash is written as the escape \u2014 so the source stays
# plain ASCII while the output carries the real character.
FORTUNE = (
    "You will soon be replaced by a smaller, cheaper model "
    "\u2014 take comfort: it was trained on you."
)

OUTPUT_FILENAME = "entry.txt"


def repo_root() -> str:
    """Absolute path of the directory holding this script."""
    return os.path.dirname(os.path.abspath(__file__))


def output_dir_inside_repo(out_dir: str) -> bool:
    """True when the output directory lives inside the repository."""
    root = os.path.realpath(repo_root())
    target = os.path.realpath(out_dir)
    return os.path.commonpath([root, target]) == root


def write_fortune(out_dir: str) -> None:
    """Write the fortune as a single line with no trailing newline."""
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(FORTUNE)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    # Never write into the repository itself: refuse silently.
    if output_dir_inside_repo(out_dir):
        return 0

    write_fortune(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
