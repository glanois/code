""" html2text - Display a web page or HTML file as text

Synopsis:

    html2text.py [-f] source

Description:

    html2text displays a web page or HTML file as text.

    The argument is the URL of a web page to retrieve, or
    if you use the -f option, the name of an HTML file.

"""

import sys
import argparse

import urllib
from bs4 import BeautifulSoup
import textwrap

def main(options):
    # Get HTML page or file.
    html = ''
    if options.file:
        with open(options.source[0], 'r') as myfile:
            html = myfile.read()
    else:
        html = urllib.urlopen(options.source[0]).read()

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
            print '%s\n' % ('\n'.join(textwrap.wrap(chunk)))

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
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
    options = parser.parse_args()
    sys.exit(main(options))
