""" testutil - Unit test util. """

import unittest
import lib.util

class TestStack(unittest.TestCase):
    def test_misc(self):
        s = lib.util.Stack()

        for i in range(14):
            s.push(i)

        for i in reversed(range(14)):
            self.assertEqual(s.top(), i)
            t = s.pop()
            self.assertEqual(t, i)

        self.assertTrue(s.empty())

    def test_empty_pop(self):
        # pop() of an empty stack throws IndexError.
        s = lib.util.Stack()
        self.assertRaises(IndexError, s.pop)

class TestRangeInclusive(unittest.TestCase):
    def test_arguments(self):
        with self.assertRaises(TypeError):
            list(lib.util.range_inclusive())

        for i in range(100):
            self.assertEqual(list(lib.util.range_inclusive(i)), list(range(i+1)))
            self.assertEqual(list(lib.util.range_inclusive(0, i)), list(range(0, i+1)))
            self.assertEqual(list(lib.util.range_inclusive(0, i, 1)), list(range(0, i+1, 1)))
