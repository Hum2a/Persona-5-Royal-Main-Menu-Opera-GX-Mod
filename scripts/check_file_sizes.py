#!/usr/bin/env python3
"""
Block files over GitHub's regular-Git limit (~100 MiB per blob).
Use --staged before commit; use --tracked in CI on the full tree.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys

# GitHub: blocks pushes of files larger than 100 MB (non-LFS)
DEFAULT_MAX_MIB = 100.0


def _git_null_separated(args: list[str]) -> list[str]:
    out = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return [p for p in out.split("\0") if p]


def staged_paths() -> list[str]:
    return _git_null_separated(["diff", "--cached", "--name-only", "-z"])


def tracked_paths() -> list[str]:
    return _git_null_separated(["ls-files", "-z"])


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--staged",
        action="store_true",
        help="only files staged for commit",
    )
    p.add_argument(
        "--tracked",
        action="store_true",
        help="all files currently tracked in the index (for CI)",
    )
    p.add_argument(
        "--max-mib",
        type=float,
        default=DEFAULT_MAX_MIB,
        metavar="N",
        help=f"max size per file in MiB (default: {DEFAULT_MAX_MIB:g})",
    )
    args = p.parse_args()
    if args.staged == args.tracked:
        p.error("specify exactly one of --staged or --tracked")

    limit = int(args.max_mib * 1024 * 1024)
    paths = staged_paths() if args.staged else tracked_paths()
    bad: list[tuple[str, int]] = []
    for rel in paths:
        if not rel or not os.path.isfile(rel):
            continue
        try:
            size = os.path.getsize(rel)
        except OSError:
            continue
        if size > limit:
            bad.append((rel, size))

    if not bad:
        print(f"OK: no files exceed {args.max_mib:g} MiB")
        return 0

    for rel, size in sorted(bad):
        mib = size / (1024 * 1024)
        print(
            f"ERROR: {rel!r} is {mib:.2f} MiB (limit {args.max_mib:g} MiB). "
            "Use Git LFS, split/compress the asset, or keep it outside the repo "
            "(see not-for-github/ in .gitignore).",
            file=sys.stderr,
        )
    return 1


if __name__ == "__main__":
    sys.exit(main())
