""" find - Find files recursively and optionally filter with regular expression.

"""

import argparse
import sys
import os
import re

def find(path, aall, regex):
    for root, dirs, files in os.walk(path):
        # Skip dot files and directories.
        if not aall:
            # https://stackoverflow.com/questions/13454164/os-walk-without-hidden-folders
            # NOTE: os.walk() with topdown = True means dirs and files are modified in-place.
            files = [f for f in files if not f[0] == '.']
            dirs[:] = [d for d in dirs if not d[0] == '.']

        for f in files:
            if len(regex) == 0:
                # No regex specified.  Print every file path.
                print(os.path.join(root, f))
            else:
                # Apply regex.
                if re.search(regex[0], os.path.join(root, f)):
                    print(os.path.join(root, f))

def main(options):
    if not os.path.isdir(options.path):
        print('ERROR: %s is not a directory' % options.path())
    else:
        find(options.path, options.aall, options.regex)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-a',
        '--all',
        dest='aall', # Avoid name collision with Python's all() function.
        help='Include hidden files and directories.',
        action='store_true',
        default=False)

    parser.add_argument(
        'path',
        help='Directory path to search.')

    parser.add_argument(
        'regex',
        help='Optional regular expression to match on.',
        nargs='*')

    options = parser.parse_args()

    sys.exit(main(options))
