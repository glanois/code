""" mp3tags.py

    DESCRIPTION
        Print mp3 tags.

    SEE ALSO:
        https://eyed3.readthedocs.io/en/latest/eyed3.html
"""
import sys
import os
import argparse
import eyed3

def print_tags(album, debug, path):
    audiofile = eyed3.load(path)
    if album:
        # Only print the artist and album.
        print('{} - {}'.format(
                audiofile.tag.artist, 
                audiofile.tag.album))
    else:
        if debug:
            print('DEBUG - {} - {} - {}'.format(
                    audiofile.tag.artist, 
                    audiofile.tag.album, 
                    audiofile.tag.title))

        tn = 'N/A'
        if audiofile.tag.track_num[0] is not None:
            if audiofile.tag.track_num[1] is None:
                tn = '{}'.format(audiofile.tag.track_num[0])
            else:
                tn = '{} of {}'.format(
                    audiofile.tag.track_num[0],
                    audiofile.tag.track_num[1])
        print('{} - {} - {} - {}'.format(
                audiofile.tag.artist, 
                audiofile.tag.album, 
                tn, 
                audiofile.tag.title))


def main(options):
    result = 0
    if not os.path.isfile(options.path):
        print('ERROR: %s is not a file.' % options.path())
        result = 1
    else:
        print_tags(options.album, options.debug, options.path)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-a',
        '--album',
        dest='album',
        help='Only print artist and album.',
        action='store_true',
        default=False)

    parser.add_argument(
        '-d',
        '--debug',
        dest='debug',
        help='Enable debug print.',
        action='store_true',
        default=False)

    parser.add_argument(
        'path',
        help='Path to MP3 file.')

    options = parser.parse_args()

    sys.exit(main(options))
