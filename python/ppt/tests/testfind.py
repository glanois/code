""" testfind.py - Unit test diff.py. """

import ppt.find
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


""" make_example_dir - Utility to create a directory hierarchy of files.  """
def make_example_dir(top):
    if not os.path.exists(top):
        os.mkdir(top)
    curdir = os.getcwd()
    os.chdir(top)

    os.makedirs('xxx/sub1/yyy', exist_ok=True)
    mkfile('xxx/sub1/yyy/aaa.txt')
    mkfile('xxx/sub1/yyy/aaa_bbb.txt')

    os.makedirs('xxx/sub2/xxx', exist_ok=True)
    mkfile('xxx/sub2/xxx/ccc.txt')
    mkfile('xxx/sub2/xxx/ccc_ddd.txt')

    os.chdir(curdir)


class TestFind(unittest.TestCase):
    def test_find_files(self):
        """ Find all the files under the specified directory. """
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            find_test_tree = os.path.join(DATA_DIR, 'find_test_tree')

            make_example_dir(find_test_tree)

            parser = ppt.find.get_parser()
            args = parser.parse_args([ find_test_tree ])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.find.main(args)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            expected_result = """./find_test_tree/xxx/sub1/yyy/aaa.txt
./find_test_tree/xxx/sub1/yyy/aaa_bbb.txt
./find_test_tree/xxx/sub2/xxx/ccc.txt
./find_test_tree/xxx/sub2/xxx/ccc_ddd.txt
"""
            self.assertEqual(captured_stdout, expected_result)

    def test_find_files_regex(self):
        """ Find all the files whose name matches the regex. """
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            find_test_tree = os.path.join(DATA_DIR, 'find_test_tree')

            make_example_dir(find_test_tree)

            parser = ppt.find.get_parser()
            args = parser.parse_args([ find_test_tree, 'aaa' ])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.find.main(args)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            expected_result = """./find_test_tree/xxx/sub1/yyy/aaa.txt
./find_test_tree/xxx/sub1/yyy/aaa_bbb.txt
"""
            self.assertEqual(captured_stdout, expected_result)

    def test_find_path(self):
        """ Find all directories. """
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            find_test_tree = os.path.join(DATA_DIR, 'find_test_tree')

            make_example_dir(find_test_tree)

            parser = ppt.find.get_parser()
            args = parser.parse_args([ '--dirs', find_test_tree ])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.find.main(args)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            expected_result = """./find_test_tree/xxx
./find_test_tree/xxx/sub1
./find_test_tree/xxx/sub1/yyy
./find_test_tree/xxx/sub2
./find_test_tree/xxx/sub2/xxx
"""
            self.assertEqual(captured_stdout, expected_result)

    def test_find_path_regex(self):
        """ Find all directories that match the regex. """
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            find_test_tree = os.path.join(DATA_DIR, 'find_test_tree')

            make_example_dir(find_test_tree)

            parser = ppt.find.get_parser()
            args = parser.parse_args([ '--dirs', find_test_tree, 'sub2' ])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.find.main(args)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            expected_result = """./find_test_tree/xxx/sub2
./find_test_tree/xxx/sub2/xxx
"""
            self.assertEqual(captured_stdout, expected_result)

    def test_find_path_prune(self):
        """ Find all directories that match regex but prune subdirectories. """
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            find_test_tree = os.path.join(DATA_DIR, 'find_test_tree')

            make_example_dir(find_test_tree)

            parser = ppt.find.get_parser()
            args = parser.parse_args([ '--dirs', '--prune', find_test_tree, 'xxx'])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.find.main(args)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            expected_result = """./find_test_tree/xxx
"""
            self.assertEqual(captured_stdout, expected_result)
