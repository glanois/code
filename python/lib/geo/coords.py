import math

# Ref:
#   https://stackoverflow.com/questions/13368525/modulus-to-limit-latitude-and-longitude-values/31119445
#   https://web.archive.org/web/20150109080324/http://research.microsoft.com/en-us/projects/wraplatitudelongitude/
# NOTE: both articles have a typo in the formula for longitude_new where
# they say "latitude" but meant to say "longitude".

def wrap_lat(lat):
    """ Wrap latitude (in degrees) to be in the range -90 to 90. """
    return 180.0/math.pi * math.atan(math.sin(lat*math.pi/180.0) / math.fabs(math.cos(lat*math.pi/180.0)))

def wrap_lon(lon):
    """ Wrap longitude (in degrees) to be in the range -180 to 180. """
    return 180.0/math.pi * math.atan2(math.sin(lon*math.pi/180.0), math.cos(lon*math.pi/180.0))
