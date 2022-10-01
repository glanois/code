""" 
util - XML utilities.
"""

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

