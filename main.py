#!/usr/bin/env python3
"""food-picture-01 entry: write the bundled ramen photo to the output dir.

The picture itself is the entry. This program does nothing creative at
runtime: it copies the image shipped alongside it (entry.png, next to this
file) to $MAKEFUN_OUTPUT_DIR/entry.png. The copy is byte-for-byte, so the
two grader runs produce identical output. Standard library only, no
network, no clock, no randomness.
"""

import os
import sys

SOURCE_NAME = "entry.png"
DEST_NAME = "entry.png"


def locate_source() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, DEST_NAME)


def copy_image(source: str, dest: str) -> int:
    """Copy the image in fixed-size chunks and report how many bytes moved."""
    total = 0
    with open(source, "rb") as src, open(dest, "wb") as dst:
        while True:
            chunk = src.read(65536)
            if not chunk:
                break
            dst.write(chunk)
            total += len(chunk)
    return total


def main() -> int:
    source = locate_source()
    dest = output_path()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    copied = copy_image(source, dest)
    if copied != os.path.getsize(source):
        raise SystemExit("copy incomplete: %d of %d bytes" % (copied, os.path.getsize(source)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
