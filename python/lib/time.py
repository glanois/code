""" time - Convenient time handling functions. """

import datetime


def doy(ds):
    """ Convert ISO-8061 date string to ordinal day (the day of the year). """
    # See https://landweb.modaps.eosdis.nasa.gov/browse/calendar.html

    # Convert date string to a Python datetime.
    dt = datetime.datetime.fromisoformat(ds)

    # Return ordinal day.
    return dt.timetuple().tm_yday


def date_from_year_doy(year, doy):
    """ Convert year and ordinal day to ISO-8061 date string. """

    d = datetime.datetime(year=year, month=1, day=1) + datetime.timedelta(days=doy)
    return d.isoformat()


def to_military_time(x):
    """ Converts hours/minutes am/pm to military time. """
    return datetime.datetime.strptime(x, "%I:%M %p").strftime("%H:%M")

