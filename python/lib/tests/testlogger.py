""" testlogger.py - Unit test logger.py. """

import lib.logger
import unittest
import logging


class TestLogger(unittest.TestCase):
    def _log_messages(self, l):
        # 1 - default behavior - only prints INFO and above.
        # This DEBUG message will be suppressed, all the rest are printed.
        l.debug('This is a debug log message. (1)')
        l.info('This is an info log message. (1)')
        l.warning('This is a warning log message. (1)')
        l.error('This is an error log message. (1)')
        l.critical('This is a critical log message. (1)')

        # 2 - Set all handlers of this logger to output DEBUG and higher level messages.
        lib.logger.set_level(l, logging.DEBUG)

        l.debug('This is a debug log message. (2)')
        l.info('This is an info log message. (2)')
        l.warning('This is a warning log message. (2)')
        l.error('This is an error log message. (2)')
        l.critical('This is a critical log message. (2)')


    def test_logger(self):
        self._log_messages(lib.logger.get_logger('testlogger-test_logger', './'))


    def test_stdout_logger(self):
        self._log_messages(lib.logger.get_stdout_logger())


    def test_file_logger(self):
        self._log_messages(lib.logger.get_file_logger('testlogger-test_file_logger', './'))
