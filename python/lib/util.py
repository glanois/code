""" Convenient utility functions. """

# Tell pydoc to only document these functions:
__all__ = [ 'range_inclusive', 'Stack' ]


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def top(self):
        return self._stack[-1]

    def empty(self):
        return len(self._stack) == 0


def range_inclusive(*args):
    """ Yields a range that includes the last item. """
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

class TestStack(unittest.TestCase):
    def test_misc(self):
        s = Stack()

        for i in range(14):
            s.push(i)

        for i in reversed(range(14)):
            self.assertEqual(s.top(), i)
            t = s.pop()
            self.assertEqual(t, i)

        self.assertTrue(s.empty())

    def test_empty_pop(self):
        # pop() of an empty stack throws IndexError.
        s = Stack()
        self.assertRaises(IndexError, s.pop)

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
