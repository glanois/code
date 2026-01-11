""" colordiff.py - Renders a .diff file as colorized HTML.

usage: colordiff.py [-h] [filename]

positional arguments:
  filename    Name of file.

options:
  -h, --help  show this help message and exit
"""
import argparse
import sys
import html

def main(options):
    result = 0
    try:
        with open(options.filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File '{options.filename}' not found.")
        resulte = 1
    else:
        # Start HTML output
        print('<html>')
        print('<head>')
        print('<style>')
        print('body { font-family: monospace; }')
        print('.green { background-color: lightgreen; color: black; }')
        print('.red { background-color: lightpink; color: black; }')
        print('.bold { font-weight: bold; }')
        print('pre { white-space: pre; }')
        print('span { display: inline; }')
        print('</style>')
        print('</head>')
        print('<body>')
        print('<pre>')

        for line in lines:
            stripped_line = line.rstrip('\n')
            escaped_line = html.escape(stripped_line)
            if stripped_line.startswith('diff'):
                sys.stdout.write(f'<span class="bold">{escaped_line}</span>\n')
            elif stripped_line.startswith('+++') or stripped_line.startswith('---'):
                sys.stdout.write(f'    {escaped_line}\n')
            elif stripped_line and stripped_line[0] == '+':
                sys.stdout.write(f'    <span class="green">{escaped_line}</span>\n')
            elif stripped_line and stripped_line[0] == '-':
                sys.stdout.write(f'    <span class="red">{escaped_line}</span>\n')
            else:
                sys.stdout.write(f'    {escaped_line}\n')

        print('</pre>')
        print('</body>')
        print('</html>')
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'filename',
        help='Name of file.',
        nargs='?')

    options = parser.parse_args()

    sys.exit(main(options))
