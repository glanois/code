""" printenv - print out the environment

Synopsis:
    printenv.py [name]

Description:
    The printenv utility prints out the names and values of the variables in
    the environment, with one name/value pair per line.  If name is speci-
    fied, only its value is printed.

    Some shells may provide a builtin printenv command which is similar or
    identical to this utility.  Consult the builtin(1) manual page.

Exit Status:
    The printenv utility exits 0 on success, and >0 if an error occurs.

Notes:
    When multiple command line arguments are provided printenv 
    implementations typically succeed and print the first value when the
    first argument is a valid environment variable name; the validity
    of subsequent environment variable names is never checked.
"""

import argparse
import os
import sys


def main(options):
    # Return 0 on success, 1 if an error occurs.
    result = 0
    if not options.name:
        print('\n'.join([ '%s=%s' % (k, v) for (k, v) in os.environ.items() ]))
    else:
        name = options.name[0]
        if name not in os.environ:
            result = 1
        else:
            print('%s=%s' % (name, os.environ[name]))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'name',
        help='Print the value of the specified environment variable.',
        nargs='*')
    options = parser.parse_args()
    sys.exit(main(options))
