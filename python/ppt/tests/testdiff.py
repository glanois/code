""" testdiff.py - Unit test diff.py. """

import ppt.diff
import unittest
import warnings
import os
import io
from contextlib import redirect_stdout, redirect_stderr

# Locate the data folder relative to this test file.
TEST_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(TEST_DIR, 'data')


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

    os.mkdir('dir1')
    os.mkdir('dir2')

    mkfile('dir1/file_only_in_dir1')
    mkfile('dir2/file_only_in_dir2')

    os.mkdir('dir1/dir_only_in_dir1')
    os.mkdir('dir2/dir_only_in_dir2')

    os.mkdir('dir1/common_dir')
    os.mkdir('dir2/common_dir')

    mkfile('dir1/common_file', 'this file is the same')
    mkfile('dir2/common_file', 'this file is the same')

    mkfile('dir1/not_the_same', 'aaaa bbbb cccc\n')
    mkfile('dir2/not_the_same', 'dddd eeee ffff\n')

    mkfile('dir1/file_in_dir1', 'This is a file in dir1')
    os.mkdir('dir2/file_in_dir1')
    
    os.chdir(curdir)


class TestDiff(unittest.TestCase):
    def test_diff_two_files(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)
            parser = ppt.diff.get_parser()
            options = parser.parse_args([ os.path.join(DATA_DIR, 'foo.txt'), os.path.join(DATA_DIR, 'bar.txt') ])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.diff.main(options)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            expected_result = """2,3c2,4
< fgjij
< klmno
---
> zzzzz
> klmnoy
> tuvwxy
"""
            self.assertEqual(captured_stdout, expected_result)

    def test_diff_another_two_files(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)
            parser = ppt.diff.get_parser()
            options = parser.parse_args([ os.path.join(DATA_DIR, 'file1.txt'), os.path.join(DATA_DIR, 'file2.txt') ])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.diff.main(options)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            expected_result = """6a7,8
> 
> We also sometimes add a line to a file.
21c23
< perish from the earth.
---
> perish from the earth because we changed a line in the file.
"""
            self.assertEqual(captured_stdout, expected_result)

    def test_diff_recursively_compare_two_directory_trees(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            # Make the directory hierarchies (dir1 + dir2)
            make_example_dir(os.path.join(DATA_DIR, 'example'))
            make_example_dir(os.path.join(DATA_DIR, 'example/dir1/common_dir'))
            make_example_dir(os.path.join(DATA_DIR, 'example/dir2/common_dir'))

            parser = ppt.diff.get_parser()
            options = parser.parse_args([ '-r', os.path.join(DATA_DIR, 'example/dir1'), os.path.join(DATA_DIR, 'example/dir2') ])

            # Capture stdout when running.
            out = io.StringIO()
            with redirect_stdout(out):
                ppt.diff.main(options)
                
            # Compare the results.
            captured_stdout = out.getvalue()
            s = captured_stdout.split('\n')

            self.assertRegex(s[0], r'Only in .+/data/example/dir1:$')
            self.assertRegex(s[1], r'dir_only_in_dir1')
            self.assertRegex(s[2], r'file_only_in_dir1')
            self.assertRegex(s[3], r'Only in .+/data/example/dir2:$')
            self.assertRegex(s[4], r'dir_only_in_dir2')
            self.assertRegex(s[5], r'file_only_in_dir2')
            self.assertRegex(s[6], r'diff .+/data/example/dir1/not_the_same .+/data/example/dir2/not_the_same$')

            diffs = '\n'.join(s[7:11])
            expected_diffs = """1c1
< aaaa bbbb cccc
---
> dddd eeee ffff"""
            self.assertEqual(diffs, expected_diffs)
