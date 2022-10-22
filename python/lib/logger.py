import sys
import datetime
import logging
import os.path
import uuid

# Tell pydoc to only document these functions:
__all__ = [ 'get_logger', 'get_stdout_logger', 'get_file_logger', 'set_level' ]


def get_formatter():
    ''' Define a common formatter for all handlers. '''
    return logging.Formatter(
        '%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
        '%Y-%m-%d %H:%M:%S')


def get_stdout_handler(name):
    ''' Return a stream handler directed to stdout. '''
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.name = name
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.setFormatter(get_formatter())
    return stdout_handler


def get_file_handler(name, prefix, path):
    ''' Return a stream handler directed to a file. '''
    file_handler = logging.FileHandler(
        os.path.join(
            path,
            '{}-{}.log'.format(
                prefix,
                datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
                mode='w')))
    file_handler.name = name
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(get_formatter())
    return file_handler


def get_logger(prefix, path):
    ''' Return a logging object instance which outputs to both
    stdout and a file. '''

    # https://docs.python.org/3/library/logging.html
    # "Multiple calls to getLogger() with the same name will always
    # return a reference to the same Logger object."
    name = str(uuid.uuid4()) # Generate a unique name.
    l = logging.getLogger(name)

    # The default logging level is WARNING.
    # Ref: https://docs.python.org/3/howto/logging.html
    # "The level set in the logger determins which severity
    # of messages it will pass to its handlers. The level set
    # in each handler determs which message that handler
    # will send on."

    # In order to pass DEBUG messate to the handlers, we
    # set the logger's level here.
    # Then, in the individual handlers, let them specify higher
    # levels if they want.
    l.setLevel(logging.DEBUG)

    l.addHandler(get_stdout_handler(name))
    l.addHandler(get_file_handler(name, prefix, path))
    return l


def get_stdout_logger():
    ''' Return a logging object instance which outputs to stdout. '''
    name = str(uuid.uuid4())
    l = logging.getLogger(name)
    l.setLevel(logging.DEBUG)
    l.addHandler(get_stdout_handler(name))
    return l


def get_file_logger(prefix, path):
    ''' Return a logging object instance which outputs to a file. '''
    name = str(uuid.uuid4())
    l = logging.getLogger(name)
    l.setLevel(logging.DEBUG)
    l.addHandler(get_file_handler(name, prefix, path))
    return l


def set_level(l, level):
    ''' Set all logger handlers to the specified level. '''
    [ h.setLevel(level) for h in l.handlers ]

