r"""
usage: touch.py [-h] path [path ...]

Update file access/modification time.

positional arguments:
  path        Path(s) of file(s) to be touched.

options:
  -h, --help  show this help message and exit

SEE ALSO:
        https://man7.org/linux/man-pages/man1/touch.1.html
"""
import argparse
import sys
import os

def _fullpath(p):
    return os.path.abspath(os.path.expanduser(p))

def _mkdir(p):
    if p.find("/") > -1 and not os.path.exists(os.path.dirname(p)):
        os.makedirs(os.path.dirname(p))

def _utime(p):
    try:
        os.utime(p, None)
    except Exception:
        open(p, 'a').close()

def touch(paths):
    for p in paths:
        if p:
            p = _fullpath(p)
            _mkdir(p)
            _utime(p)

def main(args):
    touch(args.path)
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Update file access/modification time.',
        epilog="""SEE ALSO:
        https://man7.org/linux/man-pages/man1/touch.1.html""",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path',
        help='Path(s) of file(s) to be touched.',
        nargs='+')
    args = parser.parse_args()
    sys.exit(main(args))
