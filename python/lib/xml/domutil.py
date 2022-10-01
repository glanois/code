""" 
domutil - XML DOM utilities.  The functions you wish had been included 
in xml.dom.minidom.
"""

import xml.dom.minidom

def getChildrenByTagName(node, tagName):
    for child in node.childNodes:
        if child.nodeType == child.ELEMENT_NODE:
            if tagName == '*' or child.tagName == tagName:
                yield child


def getNodeText(node):
    text = ''
    for t in node.childNodes:
        if t.nodeType == t.TEXT_NODE:
            text = text + t.nodeValue
        elif t.nodeType == node.CDATA_SECTION_NODE:
            text = text + t.data
    return text

def setNodeText(node, newText):
    if not node.firstChild:
        raise(Exception('node has no child'))
    if node.firstChild.nodeType != node.TEXT_NODE:
        raise(Exception('node child is not a text node'))
    node.firstChild.replaceWholeText(newText)
