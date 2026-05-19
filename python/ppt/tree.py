r"""
usage: tree.py [-h] [-d] [-U] [-a] [path]

Python clone of the 'tree' command.

positional arguments:
  path        Directory to start from (default: current directory).

options:
  -h, --help  show this help message and exit
  -d          List directories only.
  -U          Do not sort. Use raw filesystem order (like tree -U).
  -a          Include hidden dot files/directories.
"""
import os
import argparse
import sys


def sort_key(name: str) -> str:
    """Push hidden items (starting with . or _) to the front when sorting."""
    if name.startswith(('.', '_')):
        return ' ' + name.lower()
    return name.lower()


def print_tree(startpath: str, prefix: str = "", show_files: bool = True,
               sort_enabled: bool = True, show_all: bool = False):
    """Recursive tree printer - mimics the tree command."""
    try:
        entries = os.listdir(startpath)

        # Filter out hidden files/directories unless -a is used.
        if not show_all:
            entries = [e for e in entries if not e.startswith('.')]

        # Separate dirs and files.
        dirs = [e for e in entries if os.path.isdir(os.path.join(startpath, e))]
        files = [e for e in entries if not os.path.isdir(os.path.join(startpath, e))]

        # Apply sorting if requested.
        if sort_enabled:
            dirs = sorted(dirs, key=sort_key)
            files = sorted(files, key=sort_key)

        # Combine items to print (dirs first, then files).
        all_items = dirs[:]
        if show_files:
            all_items += files

        # Use set for fast + reliable directory lookup.
        dir_set = set(dirs)

        for i, name in enumerate(all_items):
            is_last = (i == len(all_items) - 1)
            connector = "└── " if is_last else "├── "

            # Only directories get trailing '/'.
            display_name = name + "/" if name in dir_set else name

            print(prefix + connector + display_name)

            # Recurse only into directories.
            if name in dir_set:
                new_prefix = prefix + ("    " if is_last else "│   ")
                print_tree(
                    os.path.join(startpath, name),
                    new_prefix,
                    show_files=show_files,
                    sort_enabled=sort_enabled,
                    show_all=show_all
                )

    except OSError as e:
        # Option 2: Show a helpful message on error but continue traversing
        error_msg = str(e).strip()
        print(prefix + "└── [error: " + error_msg + "]", file=sys.stderr)


class PathException(Exception):
    pass


def main(args):
    result = 0
    try:
        if not os.path.isdir(args.path):
            raise PathException(f'tree.py ERROR: {args.path} is not a directory.')

        print(args.path)
        print_tree(
            startpath=args.path,
            show_files=not args.d,
            sort_enabled=not args.U,
            show_all=args.a
        )
    except PathException as e:
        print(e, file=sys.stderr)
        result = 1
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        result = 130
    except Exception as e:          # fallback for unexpected errors
        print(f'Unexpected error: {e}', file=sys.stderr)
        result = 1

    return result


def get_parser():
    parser = argparse.ArgumentParser(description="Python clone of the 'tree' command.")
    parser.add_argument('path', nargs='?', default='.',
                        help="Directory to start from (default: current directory).")
    parser.add_argument('-d', action='store_true',
                        help="List directories only.")
    parser.add_argument('-U', action='store_true',
                        help="Do not sort. Use raw filesystem order (like tree -U).")
    parser.add_argument('-a', action='store_true',
                        help="Include hidden dot files/directories.")
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    sys.exit(main(args))
