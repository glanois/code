""" 
util - XML utilities.
"""

# Tell pydoc to only document these functions:
__all__ = [ 'escape' ]

xml_special_chars = {
    "<": "&lt;",
    ">": "&gt;",
    "&": "&amp;",
    "'": "&apos;",
    '"': "&quot;",
}

import re
import string

xml_special_chars_re = re.compile("({})".format("|".join(xml_special_chars)))

""" Substitute XML literal escapes. """
def escape(unescaped):
    return xml_special_chars_re.sub(
        lambda match: xml_special_chars[match.group(0)],
        unescaped)

def cdata(s):
    cdata_template = '''<![CDATA[
$CDATA
]]>'''
    ctemplate = string.Template(cdata_template)
    return ctemplate.substitute(CDATA=s)


import unittest

class TestUtilFunctions(unittest.TestCase):
    def test_escape(self):
        for k,v in xml_special_chars.items():
            self.assertEqual(escape(k), xml_special_chars[k])
    
    def test_cdata(self):
        hello = '''<![CDATA[
hello
]]>'''
        self.assertEqual(cdata('hello'), hello)
        
if __name__ == '__main__':
    unittest.main()

