""" mac2dos - Convert text file with Macintosh line endings to DOS.

usage: mac2dos.py [-h] filepath

positional arguments:
  filepath    Path to file to convert.

options:
  -h, --help  show this help message and exit

"""
import argparse
import sys
import re

def main(options):
    with open(options.filepath, 'rb') as fin:
        data = fin.read()
    newdata = re.sub(b'\r', b'\r\n', data)
    if newdata != data:
        with open(options.filepath, 'wb') as fout:
            fout.write(newdata)
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filepath',
        help='Path to file to convert.')
    options = parser.parse_args()
    sys.exit(main(options))
