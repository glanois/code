""" xmlpp - Pretty-print XML from file or stdin. """
import argparse
import sys
import xml.etree.ElementTree

def pp(f):
    ndm = xml.etree.ElementTree.XML(f.read())
    xml.etree.ElementTree.indent(ndm)
    print(xml.etree.ElementTree.tostring(ndm, encoding='unicode'))

def main(options):
    if not options.filename:
        # No filename given on the command line.
        # Process data directly from stdin.
        pp(sys.stdin)
    else:
        # Read from the file.
        with open(options.filename, 'r') as f:
            pp(f)
    return 0
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename',
        help='Name of file to read.',
        nargs='?')
    options = parser.parse_args()
    sys.exit(main(options))
