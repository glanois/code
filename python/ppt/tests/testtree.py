""" testtree.py - Unit test tree.py. """

import ppt.tree
import unittest
import warnings
import os
import io
from contextlib import redirect_stdout, redirect_stderr

# Locate the data folder relative to this test file.
DATA_DIR = '.'


""" mkfile - Utility to populate a file. """
def mkfile(filename, body=None):
    with open(filename, 'w') as f:
        f.write(body or filename)
    return


""" make_example_dir - Utility to create a directory hierarchy of files.  """
def make_example_dir(top):
    if not os.path.exists(top):
        os.mkdir(top)
    curdir = os.getcwd()
    os.chdir(top)

    os.makedirs('xxx/sub1/yyy', exist_ok=True)
    mkfile('xxx/sub1/yyy/aaa.txt')
    mkfile('xxx/sub1/yyy/aaa_bbb.txt')
    mkfile('xxx/sub1/yyy/__thing__')
    mkfile('xxx/sub1/yyy/AAAAAA.txt')

    os.makedirs('xxx/sub2/xxx', exist_ok=True)
    mkfile('xxx/sub2/xxx/ccc.txt')
    mkfile('xxx/sub2/xxx/ccc_ddd.txt')
    mkfile('xxx/sub2/xxx/.dotfile')
    os.makedirs('xxx/sub2/.dotdir', exist_ok=True)
    mkfile('xxx/sub2/.dotdir/somefile.txt')

    os.chdir(curdir)


class TestTree(unittest.TestCase):
    def test_full_tree(self):
        """ Test full tree with no options. """
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            tree_test_tree = os.path.join(DATA_DIR, 'tree_test_tree')

            make_example_dir(tree_test_tree)

            parser = ppt.tree.get_parser()
            args = parser.parse_args([ tree_test_tree ])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.tree.main(args)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            expected_result = """./tree_test_tree
└── xxx/
    ├── sub1/
    │   └── yyy/
    │       ├── __thing__
    │       ├── aaa.txt
    │       ├── aaa_bbb.txt
    │       └── AAAAAA.txt
    └── sub2/
        └── xxx/
            ├── ccc.txt
            └── ccc_ddd.txt
"""
            self.assertEqual(captured_stdout, expected_result)

    def test_full_tree_all(self):
        """ Test full tree with -a 'all' option. """
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            tree_test_tree = os.path.join(DATA_DIR, 'tree_test_tree')

            make_example_dir(tree_test_tree)

            parser = ppt.tree.get_parser()
            args = parser.parse_args([ '-a', tree_test_tree ])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.tree.main(args)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            expected_result = """./tree_test_tree
└── xxx/
    ├── sub1/
    │   └── yyy/
    │       ├── __thing__
    │       ├── aaa.txt
    │       ├── aaa_bbb.txt
    │       └── AAAAAA.txt
    └── sub2/
        ├── .dotdir/
        │   └── somefile.txt
        └── xxx/
            ├── .dotfile
            ├── ccc.txt
            └── ccc_ddd.txt
"""
            self.assertEqual(captured_stdout, expected_result)

    @unittest.skip('Skipping - unsorted order is indeterminate across operating systems.')
    def test_full_tree_unsorted(self):
        """ Test full tree with -U unsorted option. """
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            tree_test_tree = os.path.join(DATA_DIR, 'tree_test_tree')

            make_example_dir(tree_test_tree)

            parser = ppt.tree.get_parser()
            args = parser.parse_args([ '-U', tree_test_tree ])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.tree.main(args)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            expected_result = """./tree_test_tree
└── xxx/
    ├── sub1/
    │   └── yyy/
    │       ├── aaa.txt
    │       ├── AAAAAA.txt
    │       ├── __thing__
    │       └── aaa_bbb.txt
    └── sub2/
        └── xxx/
            ├── ccc_ddd.txt
            └── ccc.txt
"""
            self.assertEqual(captured_stdout, expected_result)

    def test_dir_only(self):
        """ Test full tree -d directories only option. """
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            tree_test_tree = os.path.join(DATA_DIR, 'tree_test_tree')

            make_example_dir(tree_test_tree)

            parser = ppt.tree.get_parser()
            args = parser.parse_args([ '-d', tree_test_tree ])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.tree.main(args)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            expected_result = """./tree_test_tree
└── xxx/
    ├── sub1/
    │   └── yyy/
    └── sub2/
        └── xxx/
"""
            self.assertEqual(captured_stdout, expected_result)
            
