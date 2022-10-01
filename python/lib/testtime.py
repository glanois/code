""" testtime.py - Unit test time.py. """

import lib.util
import lib.time
import unittest

class TestToMilitaryTime(unittest.TestCase):
    def test_formats(self):
        # Missing am/pm.
        with self.assertRaises(ValueError):
            lib.time.to_military_time('12:00')

        # Illegal am/pm.
        with self.assertRaises(ValueError):
            lib.time.to_military_time('12:00 x')
            lib.time.to_military_time('12:00 xx')

        # Illegal am/pm.
        with self.assertRaises(ValueError):
            lib.time.to_military_time('12:00 x')
            lib.time.to_military_time('12:00 xxx')

        # Already in military time.
        with self.assertRaises(ValueError):
            lib.time.to_military_time('00:00')
            lib.time.to_military_time('13:00')

        # Leading 0 hours.
        self.assertEqual(lib.time.to_military_time('01:00 am'), '01:00')

        # Single digit hours.
        self.assertEqual(lib.time.to_military_time('2:00 am'), '02:00')

        # Leading space(s).
        with self.assertRaises(ValueError):
            self.assertEqual(lib.time.to_military_time(' 3:00 am'), '03:00')

        # More than one space separating HH:MM and am/pm.
        self.assertEqual(lib.time.to_military_time('4:00  pm'), '16:00')
        self.assertEqual(lib.time.to_military_time('5:00   pm'), '17:00')

    def test_am_pm(self):
        # Combinations of capitalization of am/pm.
        self.assertEqual(lib.time.to_military_time('12:00 am'), '00:00')
        self.assertEqual(lib.time.to_military_time('12:00 pm'), '12:00')
        self.assertEqual(lib.time.to_military_time('12:00 Am'), '00:00')
        self.assertEqual(lib.time.to_military_time('12:00 Pm'), '12:00')
        self.assertEqual(lib.time.to_military_time('12:00 aM'), '00:00')
        self.assertEqual(lib.time.to_military_time('12:00 pM'), '12:00')
        self.assertEqual(lib.time.to_military_time('12:00 AM'), '00:00')
        self.assertEqual(lib.time.to_military_time('12:00 PM'), '12:00')

    def test_all(self):
        # Illegal times.
        with self.assertRaises(ValueError):
            lib.time.to_military_time('13:00 am')
        with self.assertRaises(ValueError):
            lib.time.to_military_time('99:00 am')
        with self.assertRaises(ValueError):
            lib.time.to_military_time('12:60 am')
        with self.assertRaises(ValueError):
            lib.time.to_military_time('garbage o\'clock pm')

        # All legal times in a 24 hour period from 12:00 am to 11:59 pm.
        for h in lib.util.range_inclusive(0, 23):
            for m in lib.util.range_inclusive(0, 59):
                # Military time.
                tm = f'{h:02d}:{m:02d}'
                h12 = h
                if h <= 11:
                    apm = 'am'

                    # 12am times are 12:MM, not 0:MM
                    if h == 0:
                        h12 = 12
                elif h == 12:
                    apm = 'pm'
                else:
                    apm = 'pm'
                    h12 = h - 12

                # AM/PM time.
                tapm = f'{h12:d}:{m:02d} {apm}'

                # Converting AM/PM time to military time should be
                # the predicted military time.
                self.assertEqual(lib.time.to_military_time(tapm), tm)

