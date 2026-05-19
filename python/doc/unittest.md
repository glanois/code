# Python Unit Test

Example unit test, testmymodule.m, put it in a subdirectory:

```
""" testmymodule.py - Unit test mymodule.py. """

import mymodule
import unittest

class TestMymodule(unittest.TestCase):
    def test_thing(self):
        """ Test doing the thing. """
        result = mymodule.do_the_thing()
        expected_result = True
        self.assertEqual(result, expected_result)
```

Test entire module:

```
> python -m unittest mymodule
```

Test entire module verbosely (with docstrings):

```
> python -m unittest -v mymodule
```

Test one specific test case:

```
> python -m unittest mymodule.TestMymodule.test_thing
```

Discover all unit tests from the current directory on down recursively:

```
> PYTHONPATH="$PYTHONPATH:." python -m unittest discover -v -s .
```

To skip a unit test, add the `@unittest.skip` decorator:

```
    @unittest.skip('Skipping - cannot run this unit test for reasons.')
    def testsomething(self):
        .
        .
        .
```