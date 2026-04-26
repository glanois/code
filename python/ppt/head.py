r"""
usage: head.py [-h] [-n LINES] [filename]

Print the first line(s) of a file or standard input.

positional arguments:
  filename              Name of file.

options:
  -h, --help            show this help message and exit
  -n LINES, --lines LINES
                        Print the first LINES lines of the file.
"""

import argparse
import sys
import re


def printlines(f, n):
    for i in range(n):
        print(f.readline().strip())


def main(numlines, args):
    result = 0
    if (numlines is not None) and (args.lines is not None):
        # Specified both.
        print('ERROR: cannot specify both -<n> and -n/--lines')
        result = 1
    else:
        if (numlines is None) and (args.lines is None):
            # Specified neither.
            # Default is 10 according to the man page.
            numlines = 10

        # They must have specified one or the other.
        # (The neither case is handled above).
        if numlines is not None:
            pass
        elif args.lines is not None:
            numlines = args.lines

        if not args.filename:
            # No filename given on the command line.
            # Process data directly from stdin.
            printlines(sys.stdin, numlines)
        else:
            # Process data from the file.
            with open(args.filename, 'r') as f:
                printlines(f, numlines)

    return result


if __name__ == '__main__':
    numlines = None

    if len(sys.argv) > 1:
        # Look for '-<n>' (minus number) syntax.
        mn = re.compile(r'\-(?P<digits>\d+)')
        m = mn.match(sys.argv[1])
        if m:
            numlines = int(m.group('digits'))
            del(sys.argv[1])

    parser = argparse.ArgumentParser(description='Print the first line(s) of a file or standard input.')

    parser.add_argument(
        '-n',
        '--lines',
        help='Print the first LINES lines of the file.',
        type=int,
        action='store',
        default=None)

    parser.add_argument(
        'filename',
        help='Name of file.',
        nargs='?')

    args = parser.parse_args()

    sys.exit(main(numlines, args))
