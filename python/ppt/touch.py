import argparse
import sys
import os

def main(options):
    with open(options.path[0], 'a'):
        os.utime(options.path[0], None)
    # TODO better error handling needed here.
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path',
        help='Path to file to be touched.',
        nargs=1)
    options = parser.parse_args()
    sys.exit(main(options))
