r"""
usage: cal.py [-h] [year ...]

    Displays a simple calendar.

    With no argument, displays the calendar for the month of the current year.

    With argument, displays the calendar for the specified year.

positional arguments:
  year        Display a calendar for this year.

options:
  -h, --help  show this help message and exit
"""

import argparse
import sys
import calendar
import datetime


def main(args):
    
    cal = calendar.TextCalendar(calendar.SUNDAY)
    if not args.year:
        now = datetime.datetime.now()
        cal.prmonth(now.year, now.month)
    else:
        cal.pryear(int(args.year[0]))
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""    Displays a simple calendar.

    With no argument, displays the calendar for the month of the current year.

    With argument, displays the calendar for the specified year.""",
    formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        'year',
        help='Display a calendar for this year.',
        nargs='*')
    args = parser.parse_args()
    sys.exit(main(args))

