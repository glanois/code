""" jsonpp - Pretty-print JSON from file or stdin. """
import argparse
import sys
import json

def pp(f, sort):
    j = json.load(f)
    print(json.dumps(j, sort_keys=sort, indent=4, separators=(',', ': ')))

def main(args):
    if not args.filename:
        # No filename given on the command line.
        # Process data directly from stdin.
        pp(sys.stdin, args.sort)
    else:
        # Read from the file.
        with open(args.filename, 'r') as f:
            pp(f, args.sort)
    return 0
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s',
        '--sort',
        dest='sort',
        help='Sort the keys..',
        action='store_true',
        default=False)
    parser.add_argument(
        'filename',
        help='Name of file to read.',
        nargs='?')
    args = parser.parse_args()
    sys.exit(main(args))
