#!/usr/bin/env python3
"""Build the standalone Reinforce ZIP using only Python's standard library.

SPDX-License-Identifier: MIT
Copyright (c) 2026 Richard Wolff
See generic/skills/reinforce/LICENSE for license terms for this script.
"""

import argparse
import hashlib
from pathlib import Path
import re
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "generic/skills/reinforce"
    version = (source / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        parser.error("VERSION must contain a numeric MAJOR.MINOR.PATCH version")
    names = ("CHANGELOG.md", "LICENSE", "README.md", "SKILL.md", "VERSION")
    # Read and validate everything before creating output. Never traverse the repo.
    payloads = {}
    for name in names:
        path = source / name
        if path.is_symlink() or not path.is_file():
            parser.error(f"Expected a regular non-symlink package file: {name}")
        payloads[name] = path.read_bytes()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    archive = args.output_dir / f"reinforce-{version}.zip"
    # Stored entries avoid compression-library variation; this package is small.
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_STORED) as bundle:
        for name in names:
            entry = zipfile.ZipInfo(f"reinforce/{name}", (1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            bundle.writestr(entry, payloads[name])
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (args.output_dir / "SHA256SUMS").write_text(
        f"{digest}  {archive.name}\n", encoding="ascii"
    )
    print(f"{digest}  {archive.name}")


if __name__ == "__main__":
    main()
