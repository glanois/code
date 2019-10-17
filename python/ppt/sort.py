import argparse
import sys

def main(options):
    try:
        f = open(options.path[0], 'r')
    except IndexError:
        f = sys.stdin

    with f:
        data = f.readlines()

    data.sort()

    [print(d.strip()) for d in data]

    # If file option fails, we default to reading stdin,
    # therefore this fuction can't ever fail.
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path',
        help='Path to file to be sorted.',
        nargs='*')
    options = parser.parse_args()
    sys.exit(main(options))
