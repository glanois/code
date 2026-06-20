r"""
usage: find.py [-h] [-a] [-e EXCLUDE] [-i] [-d] [-p] path [regex]

Find files (or directories) recursively and optionally filter with regular expression.

positional arguments:
  path                  Directory path to search.
  regex                 Optional regular expression to match on.

options:
  -h, --help            show this help message and exit
  -a, --all             Include hidden files and directories.
  -e, --exclude EXCLUDE
                        Exclusion regex to prevent recursing into directories which match.
  -i, --ignore-case     Prepend "(?i)" to your regex for case-insenstive matching.
  -d, --dirs            Match directory paths only (not files).
  -p, --prune           When searching paths (with --path), ignore subdirectories of prior matches.
"""

import argparse
import sys
import os
import re


def find_tree(
    startpath,
    exclude,
    aall,
    dirsonly,
    regex,
    prune):
    """ Recursively traverse the directory tree starting from
        the given path, and apply inclusion/exclusion filtering
        along with any regex.
    """

    # Exclusion regular expression.
    excre = None
    if exclude:
        excre = re.compile(exclude)

    entries = sorted(os.listdir(startpath))

    # Filter out hidden files/directories unless -a is used.
    if not aall:
        entries = [e for e in entries if not e.startswith('.')]

    # Separate dirs and files.
    dirs = [e for e in entries if os.path.isdir(os.path.join(startpath, e))]
    files = [e for e in entries if not os.path.isdir(os.path.join(startpath, e))]

    if excre is not None:
        # Exclude directories which match excre.
        dirs[:] = [d for d in dirs if not excre.search(d)] 

        # Exclude files which match excre.
        files[:] = [f for f in files if not excre.search(f)] 

    # Combine items to find (dirs first, then files).
    all_items = dirs[:]
    if not dirsonly:
        # Find both directories and files.
        all_items += files

    # Use set for fast + reliable directory lookup.
    dir_set = set(dirs)

    for i, name in enumerate(all_items):
        # Full path down the tree to this item.
        fullpath = os.path.join(startpath, name)

        prune_path = False
        if regex is None:
            # No regex specified, just print.

            # Print out the path if:
            #     1. It is a path to a file.
            #         OR
            #     2. We are only searching directory paths and this is a directory path.
            if (not (name in dir_set)) or (dirsonly and (name in dir_set)):
                print(fullpath)
        else:
            # Apply regex to full path.
            if re.search(regex, fullpath):
                print(fullpath)

                # If we matched on a directory, and pruning,
                # don't recurse into this directory.
                if (name in dir_set) and prune:
                    prune_path = True

        # Recurse only into subdirectories.
        if name in dir_set:
            if not prune_path:
                find_tree(fullpath, exclude, aall, dirsonly, regex, prune)


class PathException(Exception):
    pass


class ArgumentException(Exception):
    pass


def main(args):
    if not os.path.isdir(args.path):
        raise(PathException(f'ERROR - {args.path} is not a directory.'))
    if args.path and args.prune and not args.regex:
        raise(ArgumentException(f'ERROR - You don\'t need --prune with --path when you don\'t specify a regex.'))
    if args.ignore_case:
        args.regex = '(?i)' + args.regex
    find_tree(args.path, args.exclude, args.aall, args.dirsonly, args.regex, args.prune)
    return 0


def get_parser():
    parser = argparse.ArgumentParser(
        description='Find files (or directories) recursively and optionally filter with regular expression.')

    parser.add_argument(
        '-a',
        '--all',
        dest='aall', # Avoid name collision with Python's all() function.
        help='Include hidden files and directories.',
        action='store_true',
        default=False)

    parser.add_argument(
        '-e',
        '--exclude',
        dest='exclude',
        help='Exclusion regex to prevent recursing into directories which match.')

    parser.add_argument(
        '-i',
        '--ignore-case',
        dest='ignore_case',
        help='Prepend "(?i)" to your regex for case-insenstive matching.',
        action='store_true',
        default=False)

    parser.add_argument(
        '-d',
        '--dirs',
        dest='dirsonly',
        help='Match directory paths only (not files).',
        action='store_true',
        default=False)

    parser.add_argument(
        '-p',
        '--prune',
        dest='prune',
        help='When searching paths (with --path), ignore subdirectories of prior matches.',
        action='store_true',
        default=False)

    parser.add_argument(
        'path',
        help='Directory path to search.')

    parser.add_argument(
        'regex',
        help='Optional regular expression to match on.',
        nargs='?',
        default=None)
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    sys.exit(main(args))
