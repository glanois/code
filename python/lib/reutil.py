""" reutil - Regular expression utilities. """

import re

def multiple_replace(text, adict):
    """ Apply multiple regular expressions.
    Python Cookbook by David Ascher, Alex Martelli
    Replacing Multiple Patterns in a Single Pass

    https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s15.html

    EXAMPLE:
        d = { 'bbb' : 'xxx', 'ddd' : 'yyy' }
        print(multiple_replace('aaa bbb ccc ddd', d))
    """

    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)
