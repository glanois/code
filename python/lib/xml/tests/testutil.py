""" 
testutil.py - Unit tests for util.py.
"""

import unittest
import lib.xml.util

class TestUtilFunctions(unittest.TestCase):
    def test_escape(self):
        for k,v in lib.xml.util.xml_special_chars.items():
            self.assertEqual(
                lib.xml.util.escape(k), 
                lib.xml.util.xml_special_chars[k])
    
    def test_cdata(self):
        hello = '''<![CDATA[
hello
]]>'''
        self.assertEqual(
            lib.xml.util.cdata('hello'), hello)

