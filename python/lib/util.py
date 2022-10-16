""" util - Convenient utility functions. """

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
