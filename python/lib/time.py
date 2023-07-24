""" time - Convenient time handling functions. """

import datetime


def doy(ds):
    """ Convert ISO-8061 date string to ordinal day (the day of the year). """
    # See https://landweb.modaps.eosdis.nasa.gov/browse/calendar.html

    # Convert date string to a Python datetime.
    dt = datetime.datetime.fromisoformat(ds)

    # Return ordinal day.
    return dt.timetuple().tm_yday


def to_military_time(x):
    """ Converts hours/minutes am/pm to military time. """
    return datetime.datetime.strptime(x, "%I:%M %p").strftime("%H:%M")

