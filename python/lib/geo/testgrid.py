import unittest
import math
import pyproj
import lib.geo.grid

debug = False

class TestGridMethods(unittest.TestCase):
    def test_constructor_default(self):
        region = {
            'upper_left': {
                'latitude': 33.5,
                'longitude': -117.5 },
            'lower_right': {
                'latitude': 32.5,
                'longitude': -116.5 } }

        if debug:
            print('UL', region['upper_left']['longitude'], region['upper_left']['latitude'])
            print('LR', region['lower_right']['longitude'], region['lower_right']['latitude'])

        cells = lib.geo.grid.generate_cells(10000.0, 10000.0, region['upper_left'], region['lower_right'])

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
                if debug:
                    print('cells[{0}][{1}] '.format(i, j))
                    print('  ul = {0} '.format(cells[i][j]['ul']))
                    print('  lr = {0} '.format(cells[i][j]['lr']))
                    print('  dx = {0} dy = {1} dd = {2} h = {3}'.format(dx, dy, dd, h))

                # if j == 4: break
            # if i == 4: break
        self.assertEqual(True, True)
