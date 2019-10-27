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
    return ''.join(t.nodeValue for t in node.childNodes if t.nodeType == t.TEXT_NODE)


def setNodeText(node, newText):
    if not node.firstChild:
        raise(Exception('node has no child'))
    if node.firstChild.nodeType != node.TEXT_NODE:
        raise(Exception('node child is not a text node'))
    node.firstChild.replaceWholeText(newText)


import unittest

class TestDomutilFunctions(unittest.TestCase):
    def test_set_get_node_text(self):
        # Create a document with a root node to work with.
        impl = xml.dom.minidom.getDOMImplementation()
        doc = impl.createDocument(None, 'doc', None)
        root = doc.documentElement

        # Add an element and put some text in it.
        xxx = doc.createElement('xxx')
        root.appendChild(xxx)
        st = doc.createTextNode('some text')
        xxx.appendChild(st)
        
        # Get the text back from that element.
        self.assertEqual(getNodeText(xxx), 'some text')

        # Change the text to some other text.
        setNodeText(xxx, 'some other text')

        # Get the text back and make sure it was what we set it to.
        self.assertEqual(getNodeText(xxx), 'some other text')

        # Try setting node text for an empty element.
        yyy = doc.createElement('yyy')
        with self.assertRaises(Exception) as cmy:
            setNodeText(yyy, 'this text')
        self.assertTrue('node has no child' in str(cmy.exception))
        
        # Try setting node text for an element which is not a text node.
        zzz = doc.createElement('zzz')
        uuu = doc.createElement('uuu')
        zzz.appendChild(uuu)
        with self.assertRaises(Exception) as cmz:
            setNodeText(zzz, 'this other text')
        self.assertTrue('node child is not a text node' in str(cmz.exception))
        
    def test_get_children_by_tag_name(self):
        # Create a document with a root node to work with.
        impl = xml.dom.minidom.getDOMImplementation()
        doc = impl.createDocument(None, 'doc', None)
        root = doc.documentElement

        # Add an element.
        aaa = doc.createElement('aaa')
        root.appendChild(aaa)

        # Add 3 sub elements to that element.
        for i in range(3):
            bbb = doc.createElement('bbb')

            # Add text to this element.
            text = doc.createTextNode('text%d' % i)
            bbb.appendChild(text)
            aaa.appendChild(bbb)

        # Retrieve the text of those sub elements.
        texts = []
        for aaa in getChildrenByTagName(root, 'aaa'):
            for bbb in getChildrenByTagName(aaa, 'bbb'):
                texts.append(getNodeText(bbb))

        # Verify the text we set was retrieved.  Order is insignificant.
        for i in range(3):
            self.assertTrue(('text%d' % (i)) in texts)
    
if __name__ == '__main__':
    unittest.main()
