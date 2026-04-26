r"""
usage: html2text.py [-h] [-f] source

Display a web page or HTML file as text.

positional arguments:
  source      Source URL or filename (use -f for file).

options:
  -h, --help  show this help message and exit
  -f, --file  Read input from this file.


NOTES:
    The argument is the URL of a web page to retrieve, or
    if you use the -f option, the name of an HTML file.

"""

import sys
import argparse

import urllib
from bs4 import BeautifulSoup
import textwrap

def main(args):
    # Get HTML page or file.
    html = ''
    if args.file:
        with open(args.source[0], 'r') as myfile:
            html = myfile.read()
    else:
        html = urllib.urlopen(args.source[0]).read()

    # Filter out non-utf-8 characters in web pages which advertise utf-8
    # but then provide characters outside of utf-8.  
    html = html.decode('utf-8', 'ignore')

    soup = BeautifulSoup(html, features='html.parser')

    # Rip out all script and style elements.
    for script in soup(['script', 'style']):
        script.extract()

    # Get the text.
    text = soup.get_text()

    # Modern terminals display unicode just fine, but 'more' 
    # does not like it.  So force it into ASCII.
    text = text.encode('ascii', 'ignore').decode('ascii')

    # Break into lines and remove leading and trailing space on each.
    lines = (line.strip() for line in text.splitlines())

    # Break multi-headlines into a line each.
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    # Pretty print it.
    for chunk in chunks:
        if chunk:
            [print(x) for x in '\n'.join(textwrap.wrap(chunk))]

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display a web page or HTML file as text.')
    parser.add_argument(
        '-f',
        '--file',
        dest='file',
        help='Read input from this file.',
        action='store_true',
        default=False)
    parser.add_argument(
        'source',
        help='Source URL or filename (use -f for file).',
        nargs=1)
    args = parser.parse_args()
    sys.exit(main(args))
