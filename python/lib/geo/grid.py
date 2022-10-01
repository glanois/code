import math
import pyproj
import csv

debug = False

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


def generate_grid(xstep, ystep, upper_left, lower_right):
    """ Generate a grid of points at a specified horizontal spacing. """

    # Transverse mercator coordinate reference system,
    # whose origin is in the middle of the region.
    lon_0 = upper_left['longitude'] + (lower_right['longitude'] - upper_left['longitude'])/2
    lat_0 = lower_right['latitude'] + (upper_left['latitude']   - lower_right['latitude'])/2
    geo_crs = pyproj.CRS("EPSG:4326") 
    tmerc_crs = pyproj.CRS.from_proj4(f'+proj=tmerc +ellps=WGS84 +lon_0={lon_0} +lat_0={lat_0} +units=m +no_defs')

    # Lon/lat to tmerc.
    ll_to_tmerc = pyproj.Transformer.from_crs(geo_crs, tmerc_crs, always_xy=True)

    ul = ll_to_xy(ll_to_tmerc, upper_left['longitude'],  upper_left['latitude'])
    ur = ll_to_xy(ll_to_tmerc, lower_right['longitude'], upper_left['latitude'])
    lr = ll_to_xy(ll_to_tmerc, lower_right['longitude'], lower_right['latitude'])
    ll = ll_to_xy(ll_to_tmerc, upper_left['longitude'],  lower_right['latitude'])

    # Generate a grid, beginning with the upper left point.
    grid = []
    gx = ul[0]
    gy = ul[1]
    row = 0
    lon, lat = xy_to_ll(ll_to_tmerc, gx, gy)
    with open('grid_points.csv', 'w') as gpf:
        gpw = csv.writer(gpf)
        gpw.writerow(['longitude', 'latitude'])
        while lat > lower_right['latitude']:
            grid.append([])
            while lon <= lower_right['longitude']:
                lon, lat = xy_to_ll(ll_to_tmerc, gx, gy)
                grid[row].append((lon, lat))
                if debug:
                    print(f'gx = {gx} gy = {gy} lon = {lon} lat = {lat}')
                gpw.writerow([lon, lat])
                gx += xstep

            # Start the next row.
            gx = ul[0]
            row += 1
            gy -= ystep
            lon, lat = xy_to_ll(ll_to_tmerc, gx, gy)
    return grid


def generate_cells(xstep, ystep, upper_left, lower_right):
    """ Generate cells of the specified size. """

    # Make cells from the grid points.
    grid = generate_grid(xstep, ystep, upper_left, lower_right)
    cells = []
    for i in range(len(grid) - 1):
        cells.append([])
        for j in range(len(grid[0]) - 1):
            cells[i].append({ 'ul' : grid[i][j], 'lr' : grid[i+1][j+1]})
    return cells
