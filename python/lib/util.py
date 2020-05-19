""" Yields a range that includes the last item. """
def range_inclusive(*args):
    numargs = len(args)
    if numargs == 0:
        raise TypeError('No argument(s) given.')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("Expected at most 3 arguments, got {}".format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step


import unittest

class TestRangeInclusive(unittest.TestCase):
    def test_arguments(self):
        with self.assertRaises(TypeError):
            list(range_inclusive())

        for i in range(100):
            self.assertEqual(list(range_inclusive(i)), list(range(i+1)))
            self.assertEqual(list(range_inclusive(0, i)), list(range(0, i+1)))
            self.assertEqual(list(range_inclusive(0, i, 1)), list(range(0, i+1, 1)))


if __name__ == '__main__':
    unittest.main()
