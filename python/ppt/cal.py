""" cal - display a calendar

Synopsis:

    cal.py [year]

Description:

    cal displays a simple calendar.

    With no argument, displays the calendar for the month of the current year.

    With argument, displays the calendar for the specified year.

"""

import argparse
import sys
import calendar
import datetime


def main(options):
    
    cal = calendar.TextCalendar(calendar.SUNDAY)
    if not options.year:
        now = datetime.datetime.now()
        cal.prmonth(now.year, now.month)
    else:
        cal.pryear(int(options.year[0]))
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'year',
        help='Display a calendar for the specified year.',
        nargs='*')
    options = parser.parse_args()
    sys.exit(main(options))

