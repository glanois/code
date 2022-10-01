""" pythonoop - Object oriented Python tutorial.

Demonstrates: inheritance, invoking base class constructor from
derived class, property and setter decorators, unit test.
"""

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
