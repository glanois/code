""" testpythonoop.py - Unit test pythonoop. """

import unittest
import tutorials.pythonoop

class TestSubclassConstructor(unittest.TestCase):
    def test_B(self):
        b = tutorials.pythonoop.B()
        self.assertEqual(b.data, [4, 5])

