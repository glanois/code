""" cal - display a calendar

Synopsis:

    cal.py [year]

Description:

    cal displays a simple calendar.

    With no argument, displays the calendar for the month of the current year.

    With argument, displays the calendar for the specified year.

"""

import argparse
import calendar
import datetime

def main(options):
    cal = calendar.TextCalendar()
    cal.setfirstweekday(calendar.SUNDAY)
    if not options.year:
        month = datetime.datetime.now().month
        year  = datetime.datetime.now().year
        cal.prmonth(year, month)
    else:
        cal.pryear(int(options.year[0]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'year',
        help='Display a calendar for the specified year.',
        nargs='*')
    options = parser.parse_args()
    main(options)
