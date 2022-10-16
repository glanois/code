""" testindent.py - Unit test for indent. """

import unittest
import lib.indent

class TestIndentMethods(unittest.TestCase):
    def test_constructor_default(self):
        # Default (4 spaces)
        i = lib.indent.Indent()
        self.assertEqual(i.get(), '')
        i.indent()
        self.assertEqual(i.get(), ' ' * 4)

    def test_constructor_spaces(self):
        # Specify spaces (3)
        i = lib.indent.Indent(3)
        self.assertEqual(i.get(), '')
        i.indent()
        self.assertEqual(i.get(), ' ' * 3)
        i.indent()
        self.assertEqual(i.get(), ' ' * 6)

    def test_indent_outdent(self):
        i = lib.indent.Indent()

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
        i = lib.indent.Indent()
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
        i = lib.indent.Indent()
        self.assertEqual(i.iprint('hello iprint'), 'hello iprint')
        i.indent()
        self.assertEqual(i.iprint('hello iprint'), '    hello iprint')
        i.indent()
        self.assertEqual(i.iprint('hello iprint'), '        hello iprint')

