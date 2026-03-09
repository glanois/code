''' testwc.py - Unit test wc.py. '''

import ppt.wc
import unittest
import warnings

import os
import unittest.mock
import io
import sys
from contextlib import redirect_stdout, redirect_stderr

# Locate the data folder relative to this test file.
TEST_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(TEST_DIR, 'data')
DATA_FILE = os.path.join(DATA_DIR, 'gettysburg_address.txt')

class TestWc(unittest.TestCase):
    def test_wc_help(self):
        # Capturing the help output is tricky, due to:
        #     1. The way -h/--help options work.  You have to patch them
        #        into sys.argv in order to trigger the SystemExit exception.
        #     2. You don't get any output to stdout unless you trigger
        #        the SystemExit exception.
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            parser = ppt.wc.get_parser()

            for h in ['-h', '--help']:
                with unittest.mock.patch('sys.argv', ['wc.py', h]), \
                     unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout, \
                     self.assertRaises(SystemExit) as cm:
                    parser.parse_args()

                self.assertEqual(cm.exception.code, 0)
                self.assertIn('-h, --help   show this help message and exit', mock_stdout.getvalue())


    def test_wc_help2(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            parser = ppt.wc.get_parser()

            # This works, but can't seem to capture the output via stdout as with the above.
            # (Or any other way that I know at this time.)
            for h in ['-h', '--help']:
                parser.parse_args(h)


    @unittest.skip('Skipping - mock_stdout is empty.')
    def test_wc_help3(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            for h in ['-h', '--help']:
                with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                    parser = ppt.wc.get_parser()
                    parser.parse_args(h)

                self.assertIn('-h, --help   show this help message and exit', mock_stdout.getvalue())


    @unittest.skip('Skipping - io_out and io_err are empty.')
    def test_wc_help4(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            for h in ['-h', '--help']:
                io_out = io.StringIO()
                io_err = io.StringIO()
                with redirect_stdout(io_out), redirect_stderr(io_err):
                    parser = ppt.wc.get_parser()
                    parser.parse_args(h)

                captured_stdout = io_out.getvalue()
                captured_stderr = io_err.getvalue()


    def test_wc_file(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)
            parser = ppt.wc.get_parser()

            # Run all options on the file in turn.
            # Can't test the help options (-h, --help) because argparse exits after printing the help.
            fixture = [
                { 'sw' : '-c',      'val' : 1464 },
                { 'sw' : '--bytes', 'val' : 1464 },
                { 'sw' : '-m',      'val' : 1456 },
                { 'sw' : '--chars', 'val' : 1456 },
                { 'sw' : '-l',      'val' : 25 },
                { 'sw' : '--lines', 'val' : 25 },
                { 'sw' : '-w',      'val' : 302 },
                { 'sw' : '--words', 'val' : 302 }]
                
            for f in fixture:
                # Capture stdout when running.
                io_out = io.StringIO()
                with redirect_stdout(io_out):
                    parser = ppt.wc.get_parser()
                    options = parser.parse_args([f['sw'], DATA_FILE])
                    ppt.wc.main(options)

                # Parse the result and compare to expected value.
                captured_stdout = io_out.getvalue()
                val_int = int(captured_stdout.split()[0])
                self.assertEqual(val_int, f['val']) 
        

    def test_wc_file2(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)

            # Capture stdout when running.
            io_out = io.StringIO()
            with redirect_stdout(io_out):
                parser = ppt.wc.get_parser()
                options = parser.parse_args([DATA_FILE])
                ppt.wc.main(options)
                
            # Compare the results.
            captured_stdout = io_out.getvalue()
            vals_int = [int(v) for v in captured_stdout.split()[0:3]]
            expected_vals = [25, 302, 1464]
            self.assertEqual(vals_int, expected_vals) 


    def test_wc_stdin(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)
            parser = ppt.wc.get_parser()
            options = parser.parse_args([])

            # Feed the file in via stdin.
            # Unfortunately, passing the file handle doesn't work.
            # re.findall() gives this error:
            #    File "/usr/lib/python3.12/re/__init__.py", line 217, in findall
            #    return _compile(pattern, flags).findall(string)
            #    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            #    TypeError: expected string or bytes-like object, got 'MagicMock'
            #
            # Therefore, this reads the whole file in (frown) and passes that.

            with unittest.mock.patch('sys.stdin') as mock_stdin, open(DATA_FILE, 'r', encoding='utf-8') as data_file:
                data_file_contents = data_file.read()

                mock_stdin.read.return_value = data_file_contents

                # Capture stdout when running.
                io_out = io.StringIO()
                with redirect_stdout(io_out):
                    ppt.wc.main(options)
                
                # Compare the results.
                captured_stdout = io_out.getvalue()
                vals_int = [int(v) for v in captured_stdout.split()[0:3]]
                expected_vals = [25, 302, 1456]
                self.assertEqual(vals_int, expected_vals) 

