""" Indent - Implement text indentation.  Useful for pretty printing. """

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


import unittest

class TestIndentMethods(unittest.TestCase):
    def test_constructor_default(self):
        # Default (4 spaces)
        i = Indent()
        self.assertEqual(i.get(), '')
        i.indent()
        self.assertEqual(i.get(), ' ' * 4)

    def test_constructor_spaces(self):
        # Specify spaces (3)
        i = Indent(3)
        self.assertEqual(i.get(), '')
        i.indent()
        self.assertEqual(i.get(), ' ' * 3)
        i.indent()
        self.assertEqual(i.get(), ' ' * 6)

    def test_indent_outdent(self):
        i = Indent()

        self.assertEqual(i.get(), '')
        i.indent()
        self.assertEqual(i.get(), ' ' * 4)
        i.indent()
        self.assertEqual(i.get(), ' ' * 8)
        i.outdent()
        self.assertEqual(i.get(), ' ' * 4)
        i.outdent()
        self.assertEqual(i.get(), '')

        # Test underflow.
        i.outdent()
        self.assertEqual(i.get(), '')

        # Back to one level.
        i.indent()
        self.assertEqual(i.get(), ' ' * 4)

    def test_reset(self):
        i = Indent()
        self.assertEqual(i.get(), '')
        i.indent()
        i.indent()
        self.assertEqual(i.get(), ' ' * 8)
        i.reset()
        self.assertEqual(i.get(), '')
        # Back to one level.
        i.indent()
        self.assertEqual(i.get(), ' ' * 4)

    def test_iprint(self):
        i = Indent()
        self.assertEqual(i.iprint('hello iprint'), 'hello iprint')
        i.indent()
        self.assertEqual(i.iprint('hello iprint'), '    hello iprint')
        i.indent()
        self.assertEqual(i.iprint('hello iprint'), '        hello iprint')
        
if __name__ == '__main__':
    unittest.main()

