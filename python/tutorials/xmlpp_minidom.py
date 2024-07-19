import xml.dom.minidom 
  
# https://www.w3schools.com/xml/note.xml
s = '''
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>'''

dom = xml.dom.minidom.parseString(s)
print(dom.toprettyxml(newl='', indent=' '*2))
