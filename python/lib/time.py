""" time - Convenient time handling functions. """

import datetime

def to_military_time(x):
    """ Converts hours/minutes am/pm to millitary time. """
    return datetime.datetime.strptime(x, "%I:%M %p").strftime("%H:%M")

