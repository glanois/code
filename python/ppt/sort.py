r"""usage: sort.py [-h] [path]

Sorts the specified file or standard input.

positional arguments:
  path        Path to file to be sorted.

options:
  -h, --help  show this help message and exit
"""

import argparse
import sys

def sort(f):
    with f:
        data = f.readlines()

    data.sort()

    [print(d.strip()) for d in data]


def main(args):
    if not args.path:
        # No filename given on the command line.
        # Process data directly from stdin.
        sort(sys.stdin)
    else:
        # Read from the file.
        with open(args.path, 'r') as f:
            sort(f)

    # If file open fails, we default to reading stdin,
    # therefore this fuction can't ever fail.
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sorts the specified file or standard input.')
    parser.add_argument(
        'path',
        help='Path to file to be sorted.',
        nargs='?')
    args = parser.parse_args()
    sys.exit(main(args))
