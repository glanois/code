""" wc - print newline, word, and byte counts for each file
 
Synopsis:
 
    wc.py [-h] [-c] [-m] [-l] [-w] [--files0] [filenames [filenames ...]]
 
Description:
 
    Print newline, word, and byte counts for each file, and a total
    line if more than one file is specified. With no file, read
    standard input.
 
    Positional Arguments:
      filenames    Names of files whose words are to be counted.
 
    Optional Arguments:
      -h, --help   show help message and exit
      -c, --bytes  Count the number of bytes.
      -m, --chars  Count the number of characters.
      -l, --lines  Count the number of lines.
      -w, --words  Count the number of words.
      --files0     Read input from the files specified by NUL-terminated names in
                   the standard input.
"""
 
import os
import os.path
import argparse
import re
import sys
 

def count_requested(count):
    num_requested = 0
    for (k, v) in list(count['requests'].items()):
        if v['requested']:
            num_requested += 1
    return num_requested


def word_count_text(args, text, filepath):
    # For stdin (filepath == ''), just use the length of
    # the incoming text.
    bytes_count = len(text)

    # For actual files, use the size on disk.
    if os.path.isfile(filepath):
        bytes_count = os.stat(filepath).st_size

    # Note that the size on disk will be greater than the
    # the length of the text when there are unicode characters.
    # (eg, em dash instead of plain ASCII minus '-')

    count = {
        'requests' : {
            'bytes' : {
                'count'     : bytes_count,
                'requested' : args.bytes },
            'chars' : {
                'count'     : len(text),
                'requested' : args.chars },
            'lines' : {
                'count'     : text.count('\n'),
                'requested' : args.lines },
            'words' : {
                'count'     : len(re.findall(r'[^\s]+', text)),
                'requested' : args.words} },
        'filepath' : filepath }

    if count_requested(count) == 0:
        # Nothing explicitly requested.  Therefore, request lines,
        # words, and bytes.
        count['requests']['lines']['requested'] = True
        count['requests']['words']['requested'] = True
        count['requests']['bytes']['requested'] = True

    return count
 

def word_count_file(args, filepath):
    with open(filepath, 'r', encoding='utf-8') as fin:
        text = fin.read()
        return word_count_text(args, text, filepath) 

 
def measure_width(count):
    width = 0
    # Find the width of the widest requested count.
    for v in count['requests'].values():
        if v['requested'] and len(str(v['count'])) > width:
            width = len(str(v['count']))
    return width


def word_count_filenames(args):
    total = {
        'bytes' : {
            'count'     : 0,
            'requested' : False },
        'chars' : {
            'count'     : 0,
            'requested' : False },
        'lines' : {
            'count'     : 0,
            'requested' : False },
        'words' : {
            'count'     : 0,
            'requested' : False } }

    # Find the width of the widest requested count.
    widths = []
    counts = []
    for filepath in args.filenames:
        count = word_count_file(args, filepath)
        width = measure_width(count)
        counts.append(count)
        widths.append(width)
        for k in count['requests'].keys():
            if count['requests'][k]['requested']:
                total[k]['count']     = total[k]['count'] + count['requests'][k]['count']
                total[k]['requested'] = count['requests'][k]['requested']

    return counts, widths, total

 
def print_counts_by_file(count, width):

    # Have to do some work to duplicate the way wc spaces the numbers.
    if count_requested(count) == 1:
        # 1. When only one command line switch count requested, there are no leading spaces.
        if count['requests']['lines']['requested']:
            print(f"{count['requests']['lines']['count']} {count['filepath']}")
        elif count['requests']['bytes']['requested']:
            print(f"{count['requests']['bytes']['count']} {count['filepath']}")
        elif count['requests']['chars']['requested']:
            print(f"{count['requests']['chars']['count']} {count['filepath']}")
        elif count['requests']['words']['requested']:
            print(f"{count['requests']['words']['count']} {count['filepath']}")
    else:
        # 2. When there are
        #     a) no requested values (which means print all counts), or
        #     b) more than one requested value,
        #
        #    wc uses the width of the widest requested number
        #    (plus one space between as a separator), and always
        #    prints them in this order: lines, words, characters, bytes.

        # Assemble them in the specific order: lines, words, characters, bytes.
        counts = []
        for c in ('lines', 'words', 'chars', 'bytes'):
            if count['requests'][c]['requested']:
                counts.append(f"{count['requests'][c]['count']:>{width}}")

        # Print it out.
        print(f"{' '.join(counts)} {count['filepath']}")


def main(args):
    if len(args.filenames) == 0:
        # No filenames given on the command line.
        if args.files0:
            # Read NUL-terminated input filenames from stdin.
            filenames = sys.stdin.read()
            # Split on NUL and throw away last one due to last NUL terminator.
            args.filenames = filenames.split('\x00')[:-1]
            counts, widths, total = word_count_filenames(args)
        else:
            # Process data directly from stdin.
            text = sys.stdin.read()
            count = word_count_text(args, text, '')
            width = measure_width(count)
            print_counts_by_file(count, width)
    elif len(args.filenames) == 1:
        # Just one file on the command line.
        count = word_count_file(args, args.filenames[0])
        width = measure_width(count)
        print_counts_by_file(count, width)
    else:
        # Multiple files.
        counts, widths, total = word_count_filenames(args)
        for count in counts:
            print_counts_by_file(count, max(widths))

        totals = []
        for c in ('lines', 'words', 'chars', 'bytes'):
            if total[c]['requested']:
                totals.append(f"{total[c]['count']:>{max(widths)}}")

        print(f"{' '.join(totals)} total")
    return 0


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c',
        '--bytes',
        dest='bytes',
        help='Count the number of bytes.',
        action='store_true',
        default=False)
    parser.add_argument(
        '-m',
        '--chars',
        dest='chars',
       help='Count the number of characters.',
        action='store_true',
        default=False)
    parser.add_argument(
        '-l',
        '--lines',
        dest='lines',
        help='Count the number of lines.',
        action='store_true',
        default=False)
    parser.add_argument(
        '-w',
        '--words',
        dest='words',
        help='Count the number of words.',
        action='store_true',
        default=False)
    parser.add_argument(
        '--files0',
        dest='files0',
        help='Read input from the files specified by NUL-terminated names in the standard input.',
        action='store_true',
        default=False)
    parser.add_argument(
        'filenames',
        help='Names of files whose words are to be counted.',
        nargs='*')
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    sys.exit(main(args))

