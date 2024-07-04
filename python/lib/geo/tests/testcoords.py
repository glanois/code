import unittest
import lib.geo.coords

class TestCoords(unittest.TestCase):
    def setUp(self):
        self.tol = 1E-13

    def test_wrap_lat(self):
        lats = {
            0 : 0,
            45 : 45,
            89.999 : 89.999,
            90 : 90,
            90.001 : 89.999,
            91 : 89,
            -91 : -89,
            180 : 0,
            181 : -1,
            270 : -90 }

        [ self.assertAlmostEqual(lib.geo.coords.wrap_lat(lat), expected, delta=self.tol) for lat, expected in lats.items() ]

    def test_wrap_lon(self):
        lons = {
            0 : 0,
            90 : 90,
            179.999 : 179.999,
            180 : 180,
            180.001 : -179.999,
            181 : -179,
            -181 : 179,
            360 : 0,
            361 : 1 }

        [ self.assertAlmostEqual(lib.geo.coords.wrap_lon(lon), expected, delta=self.tol) for lon, expected in lons.items() ]
