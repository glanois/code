""" Demonstrate coordinate reference system transformations (both directions). """
import pyproj
import math

def ll_to_xy(t, lon, lat):
    return t.transform(
        lon,
        lat,
        radians=False,
        direction=pyproj.enums.TransformDirection.FORWARD)

def xy_to_ll(t, x, y):
    return t.transform(
        x,
        y,
        radians=False,
        direction=pyproj.enums.TransformDirection.INVERSE)


geo_crs = pyproj.CRS("EPSG:4326") 

lon_0, lat_0 = -116.5, 32.5
tmerc_crs = pyproj.CRS.from_proj4(
    f'+proj=tmerc +ellps=WGS84 +lon_0={lon_0} +lat_0={lat_0} +units=m +no_defs')
ll_to_tmerc = pyproj.Transformer.from_crs(geo_crs, tmerc_crs, always_xy=True)

xstep, ystep = 1000.0, 1000.0

lon, lat = -117.0, 33.0
print(f'lon = {lon}, lat = {lat}')

x, y = ll_to_xy(ll_to_tmerc, lon, lat)

print(f'x = {x}, y = {y}')

x_prime, y_prime = x + 1000.0, y - 1000.0

print(f'x_prime = {x_prime}, y_prime = {y_prime}')

lon_prime, lat_prime = xy_to_ll(ll_to_tmerc, x_prime, y_prime)

print(f'lon_prime = {lon_prime}, lat_prime = {lat_prime}')

x_prime_2, y_prime_2  = ll_to_xy(ll_to_tmerc, lon_prime, lat_prime)

print(f'x_prime_2 = {x_prime_2}, y_prime_2 = {y_prime_2}')

x_2, y_2 = x_prime_2 - xstep, y_prime_2 + ystep

print(f'x_2 = {x_2}, y_2 = {y_2}')

ex, ey = abs(x-x_2), abs(y-y_2)

print(f'ex = {ex}, ey = {ey}')

lon_2, lat_2 = xy_to_ll(ll_to_tmerc, x_2, y_2)

print(f'lon_2 = {lon_2}, lat_2 = {lat_2}')

elon, elat = abs(lon-lon_2), abs(lat-lat_2)

print(f'elon = {elon}, elat = {elat}')

# Use a geodisc, for comparison purposes.
g = pyproj.Geod(ellps='WGS84')
a21, a12, dx = g.inv(lon, lat, lon_prime, lat, radians=False)
a21, a12, dy = g.inv(lon, lat, lon, lat_prime, radians=False)
print(f'dx = {dx} dy = {dy}')

a21, a12, dx = g.inv(lon, lat, lon_2, lat, radians=False)
a21, a12, dy = g.inv(lon, lat, lon, lat_2, radians=False)
print(f'dx = {dx} dy = {dy}')
