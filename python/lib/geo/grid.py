import math
import pyproj
import csv

# Tell pydoc to only document these classes:
__all__ = [ 'generate_grid', 'generate_cells' ]


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
            

import unittest

class TestGridMethods(unittest.TestCase):
    def test_constructor_default(self):
        region = {
            'upper_left': {
                'latitude': 33.5,
                'longitude': -117.5 },
            'lower_right': {
                'latitude': 32.5,
                'longitude': -116.5 } }

        print('UL', region['upper_left']['longitude'], region['upper_left']['latitude'])
        print('LR', region['lower_right']['longitude'], region['lower_right']['latitude'])

        cells = generate_cells(10000.0, 10000.0, region['upper_left'], region['lower_right'])

        # Test the cell dimensions with a geodesic to verify
        # they are really 1km x 1km.
        g = pyproj.Geod(ellps='WGS84')

        for (i, row) in enumerate(cells):
            for (j, col) in enumerate(row):
                # Measure top edge of cell[i][j].
                a12, a21, dx = g.inv(
                    # From upper left corner.
                    cells[i][j]['ul'][0],
                    cells[i][j]['ul'][1],
                    # To upper right corner.
                    cells[i][j]['lr'][0],
                    cells[i][j]['ul'][1],
                    radians=False)
                # Measure left edge of cell[i][j].
                a12, a21, dy = g.inv(
                    # From upper left corner.
                    cells[i][j]['ul'][0],
                    cells[i][j]['ul'][1],
                    # to lower left corner.
                    cells[i][j]['ul'][0],
                    cells[i][j]['lr'][1],
                    radians=False)

                # Measure diagonal.
                a12, a21, dd = g.inv(
                    # From upper left corner.
                    cells[i][j]['ul'][0],
                    cells[i][j]['ul'][1],
                    # to lower right corner.
                    cells[i][j]['lr'][0],
                    cells[i][j]['lr'][1],
                    radians=False)

                h = math.sqrt(dx*dx + dy*dy)
                print('cells[{0}][{1}] '.format(i, j))
                print('  ul = {0} '.format(cells[i][j]['ul']))
                print('  lr = {0} '.format(cells[i][j]['lr']))
                print('  dx = {0} dy = {1} dd = {2} h = {3}'.format(dx, dy, dd, h))

                # if j == 4: break
            # if i == 4: break
        self.assertEqual(True, True)
    
if __name__ == '__main__':
    unittest.main()
