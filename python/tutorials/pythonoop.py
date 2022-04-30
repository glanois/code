""" pythonoop - Object oriented Python tutorial.

Demonstrates: inheritance, invoking base class constructor from
derived class, property and setter decorators, unit test.
"""

# Tell pydoc to only document these classes:
__all__ = [ 'A',  'B' ]

class A:
    def __init__(self):
        self._data = [1, 2, 3]

    @property
    def data(self):
        return self._data  

    @data.setter
    def data(self, value):
        self._data = value

class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.data = [4, 5]


import unittest

class TestSubclassConstructor(unittest.TestCase):
    def test_B(self):
        b = B()
        self.assertEqual(b.data, [4, 5])
        
if __name__ == '__main__':
    unittest.main()

