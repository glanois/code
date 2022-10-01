""" indent - Implement text indentation.  Useful for pretty printing. """

# Tell pydoc to only document these classes:
__all__ = [ 'Indent' ]

class Indent:
    def __init__(self, spaces = 4):
        self._spaces = ' ' * spaces
        self.reset()

    def indent(self):
        self._i += 1

    def outdent(self):
        if self._i > 0:
            self._i -= 1

    def get(self):
        """ Indentation prefix string. """
        return self._spaces * self._i

    def reset(self):
        self._i = 0

    def iprint(self, s):
        """ Return s prefixed by indentation. """
        return('%s%s' % (self.get(), s))
