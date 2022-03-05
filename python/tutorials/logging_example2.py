"""
    Demonstrates logging to both screen and a log file,
    with runtime control over the logfile location.

    Utilizes custom date/time stamp in the file name.
        Example: logfile-20220302T222913Z.log

    Utilizes custom date/time stamp in the log messages.
        Example: 2022-03-02 14:29:13.130 INFO: Hello INFO
"""
import sys
import argparse
import datetime
import logging
import os.path

def get_logger(prefix, path):
    # This is a logging object instance.
    logger = logging.getLogger()

    # Put the overall lowest logging level here.
    # The, in the individual handlers, let them specify
    # higher levels if they want.
    logger.setLevel(logging.DEBUG)

    # Define a common formatter for both handlers.
    formatter = logging.Formatter(
        '%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
        '%Y-%m-%d %H:%M:%S')

    # Handler for logging to stdout.
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    # Hanlder for logging to a file.
    file_handler = logging.FileHandler(
        os.path.join(
            path,
            '{}-{}.log'.format(
                prefix,
                datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'))),
            mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)
    return logger

def main(options):
    logger = get_logger('logging_example2', options.path[0])

    # Now log some messages:
    logger.info('logging_example.py')
    logger.critical('Hello CRITICAL')
    logger.error('Hello ERROR')
    logger.warning('Hello WARNING')
    logger.info('Hello INFO')
    logger.debug('Hello DEBUG')
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'path',
        help='Path to the directory where you want thelof file to be written.  Defaults to current working directory.',
        nargs='*', # We will only use the first one.
        default='.')

    options = parser.parse_args()

    sys.exit(main(options))
