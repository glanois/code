# First, you need to know the local time zone of the computer you're on.
#
# On MacOS X,
#   $ sudo systemsetup -gettimezone
#   Time Zone: America/Los_Angeles
#
# Debian/Ubuntu,
#   $ cat /etc/timezone
#
# Redhat,
#   $ grep ZONE /etc/sysconfig/clock

import datetime

# NOTE: Calling now() with no argument results in %z being the empty string.
now = datetime.datetime.now()
print('now() is                      %s' % (now.strftime("%Y-%m-%d %H:%M:%S %z")))

# Calling now() with with your system's local time zone as the 
# argument will populate the zone and it is printable so you
# can see what your UTC offset is.
import dateutil.tz
localtimezone = dateutil.tz.tzlocal()
now_local = datetime.datetime.now(localtimezone)
print('now(localtimezone) is         %s' % (now_local.strftime("%Y-%m-%d %H:%M:%S %z")))

# But there is a better way to get your local UTC offset.
utcoffset = localtimezone.utcoffset(now_local)
utcoffset_hours = utcoffset.total_seconds()/3600.0
print('The local UTC offset is %f hours' % (utcoffset_hours))

# If you want to try to convert between local time and UTC, you can use the UTC offset.
now_local_plus_utcoffset = now_local + datetime.timedelta(hours=-utcoffset_hours)
print('Local time plus UTC offset is %s' % (now_local_plus_utcoffset.strftime("%Y-%m-%d %H:%M:%S")))

# If ultimately what you only want is time in UTC, the safest approach is 
# to get UTC time directly.  It is unadvisable to get local time and try
# to convert that to UTC; that approach is fraught with danger, due to
# DST and other considerations (such the history of UTC offsets being changed
# in various time zones around the world).
now_UTC = datetime.datetime.utcnow()
print('UTC time is                   %s' % (now_UTC.strftime("%Y-%m-%d %H:%M:%S %z")))


