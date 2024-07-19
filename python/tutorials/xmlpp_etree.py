import xml.etree.ElementTree

# https://www.w3schools.com/xml/note.xml
s = '''
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>'''

element = xml.etree.ElementTree.XML(s)
xml.etree.ElementTree.indent(element)
print(xml.etree.ElementTree.tostring(element, encoding='unicode'))
