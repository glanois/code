""" testreutil.py - Unit test reutil. """

import unittest
import lib.reutil

class TestMultipleReplace(unittest.TestCase):
    def test_example(self):
        d = { 'bbb' : 'xxx', 'ddd' : 'yyy' }
        self.assertEqual(lib.reutil.multiple_replace('aaa bbb ccc ddd', d), 'aaa xxx ccc yyy')

        
