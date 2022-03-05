"""
    Demonstrates logging to both screen and a log file
    using the logging module as a global singleton instance.

    Utilizes custom date/time stamp in the file name.
        Example: logfile-20220302T222913Z.log

    Utilizes custom date/time stamp in the log messages.
        Example: 2022-03-02 14:29:13.130 INFO: Hello INFO
"""
import sys
import datetime
import logging

# This sends logging messages to stdout.
stdout_handler = logging.StreamHandler()

# This sends logging messages to a log file.
file_handler = logging .FileHandler(
    'logging_example-{}.log'.format(datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')),
    mode='w')

# This configures the logging module.
logging.basicConfig(
    level=logging.DEBUG, # This controls the logging level for the log file.
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[ stdout_handler, file_handler ])


def main():
    # Now log some messages:
    logging.info('logging_example.py')
    logging.critical('Hello CRITICAL')
    logging.error('Hello ERROR')
    logging.warning('Hello WARNING')
    logging.info('Hello INFO')
    logging.debug('Hello DEBUG')
    return 0

if __name__ == '__main__':
    sys.exit(main())
