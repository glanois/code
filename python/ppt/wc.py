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
 
def wordcounttext(options, text, filepath):
    count = {
        'chars' : 0,
        'lines' : 0,
        'words' : 0 }
    count['chars'] = len(text)
    count['lines'] = text.count('\n')
    count['words'] = len(re.findall(r"[\w']+|[.,!?;]", text))
 
    if options.bytes or options.chars:
        print '%7d %s' % (count['chars'], filepath)
    elif options.lines:
        print '%7d %s' % (count['lines'], filepath)
    elif options.words:
        print '%7d %s' % (count['words'], filepath)
    else:
        print '%7d %7d %7d %s' % (count['lines'], count['words'], count['chars'], filepath)
    return count
 
 
def wordcountfile(options, filepath):
    count = {
        'chars' : 0,
        'lines' : 0,
        'words' : 0 }
    try:
        fin = open(filepath, 'r')
        text = fin.read()
        fin.close()
    except IOError:
        print 'Error reading file %s.' % (filepath)
        raise
    else:
        count = wordcounttext(options, text, filepath)
    return count
 
 
def wordcountfilenames(options):
    total = {
        'chars' : 0,
        'lines' : 0,
        'words' : 0 }
 
    for path in options.filenames:
        count = wordcountfile(options, path)
        total = {k: total[k] + v for (k, v) in count.items()}
 
    if len(options.filenames) > 1:
        if options.bytes or options.chars:
            print '%7d %s' % (total['chars'], 'total')
        elif options.lines:
            print '%7d %s' % (total['lines'], 'total')
        elif options.words:
            print '%7d %s' % (total['words'], 'total')
        else:
            print '%7d %7d %7d %s' % (total['lines'], total['words'], total['chars'], 'total')
 
 
def main(options):
    if len(options.filenames) == 0:
        # No filenames given on the command line.
        if options.files0:
            # Read NUL-terminated input filenames from stdin.
            filenames = sys.stdin.read()
            # Split on NUL and throw away last one due to last NUL terminator.
            options.filenames = filenames.split('\x00')[:-1]
            wordcountfilenames(options)
        else:
            # Process data directly from stdin.
            text = sys.stdin.read()
            wordcounttext(options, text, '')
    else:
        wordcountfilenames(options)
 
 
if __name__ == '__main__':
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
    options = parser.parse_args()
    main(options)
