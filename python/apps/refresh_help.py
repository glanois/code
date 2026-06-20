#!/usr/bin/env python3
r"""
usage: refresh_help.py [-h] [-p] source_file

Refresh module docstring from -h output

positional arguments:
  source_file    Python script to update

options:
  -h, --help     show this help message and exit
  -p, --preview  Preview changes without writing to file (pipe to
                 head/tail/etc as needed)
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


def get_help_output(script_path: Path) -> str:
    """Run the script with -h and return clean output."""
    try:
        result = subprocess.run(
            [sys.executable, str(script_path), "-h"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path} with -h:\n{e.stderr or e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Script not found: {script_path}")
        sys.exit(1)


def create_backup(file_path: Path):
    """Create a .bak copy."""
    bak_path = file_path.with_suffix(file_path.suffix + ".bak")
    shutil.copy2(file_path, bak_path)
    print(f"💾 Backup created: {bak_path}")


def update_docstring(file_path: Path, help_text: str, preview: bool = False):
    """Replace the module docstring."""
    content = file_path.read_text(encoding="utf-8")

    # Match leading comments + first triple-quoted string
    docstring_pattern = re.compile(
        r'^((#.*\n)*?)(r?"""[\s\S]*?"""|r?\'\'\'[\s\S]*?\'\'\')',
        re.MULTILINE
    )
    match = docstring_pattern.search(content)

    new_docstring = f'r"""\n{help_text}\n"""'

    if match:
        prefix = match.group(1)   # shebang + comments
        updated = prefix + new_docstring + content[match.end():]
    else:
        # No docstring — insert after leading comments
        lines = content.splitlines(keepends=True)
        insert_pos = 0
        for i, line in enumerate(lines):
            if not line.strip().startswith("#") and line.strip():
                insert_pos = i
                break
        lines.insert(insert_pos, new_docstring + "\n\n")
        updated = "".join(lines)

    if preview:
        print(updated)
    else:
        create_backup(file_path)
        file_path.write_text(updated, encoding="utf-8")
        print(f"✅ Successfully updated docstring in {file_path}")


def main():
    parser = argparse.ArgumentParser(description="Refresh module docstring from -h output")
    parser.add_argument("-p", "--preview", action="store_true",
                        help="Preview changes without writing to file (pipe to head/tail/etc as needed)")
    parser.add_argument("source_file", type=Path, help="Python script to update")
    args = parser.parse_args()

    if not args.source_file.exists():
        print(f"File not found: {args.source_file}")
        sys.exit(1)

    help_output = get_help_output(args.source_file)
    update_docstring(args.source_file, help_output, preview=args.preview)


if __name__ == "__main__":
    main()
