""" 
testdomutil.py - Unit test for domutil.py XML DOM utilities.
"""

import xml.dom.minidom
import lib.xml.domutil

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
        self.assertEqual(lib.xml.domutil.getNodeText(xxx), 'some text')

        # Change the text to some other text.
        lib.xml.domutil.setNodeText(xxx, 'some other text')

        # Get the text back and make sure it was what we set it to.
        self.assertEqual(lib.xml.domutil.getNodeText(xxx), 'some other text')

        # Try setting node text for an empty element.
        yyy = doc.createElement('yyy')
        with self.assertRaises(Exception) as cmy:
            lib.xml.domutil.setNodeText(yyy, 'this text')
        self.assertTrue('node has no child' in str(cmy.exception))
        
        # Try setting node text for an element which is not a text node.
        zzz = doc.createElement('zzz')
        uuu = doc.createElement('uuu')
        zzz.appendChild(uuu)
        with self.assertRaises(Exception) as cmz:
            lib.xml.domutil.setNodeText(zzz, 'this other text')
        self.assertTrue('node child is not a text node' in str(cmz.exception))
        
        # Test CDATA.
        ttt = doc.createElement('ttt')
        s = 'cdtcdtcdtcdt'
        ttt.appendChild(doc.createCDATASection(s))
        self.assertEqual(lib.xml.domutil.getNodeText(ttt), s)

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
        for aaa in lib.xml.domutil.getChildrenByTagName(root, 'aaa'):
            for bbb in lib.xml.domutil.getChildrenByTagName(aaa, 'bbb'):
                texts.append(lib.xml.domutil.getNodeText(bbb))

        # Verify the text we set was retrieved.  Order is insignificant.
        for i in range(3):
            self.assertTrue(('text%d' % (i)) in texts)
