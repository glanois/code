""" wfreq - word frequency counter. """

import sys
import collections
import re

s = """Four score and seven years ago our fathers brought forth on this
continent a new nation, conceived in Liberty, and dedicated to the
proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation
or any nation so conceived and so dedicated, can long endure. We are
met on a great battle-field of that war. We have come to dedicate a
portion of that field, as a final resting place for those who here
gave their lives that that nation might live. It is altogether fitting
and proper that we should do this.

But, in a larger sense, we can not dedicate--we can not consecrate--we
can not hallow--this ground. The brave men, living and dead, who
struggled here, have consecrated it, far above our poor power to add
or detract. The world will little note, nor long remember what we say
here, but it can never forget what they did here. It is for us the
living, rather, to be dedicated here to the unfinished work which they
who fought here have thus far so nobly advanced. It is rather for us
to be here dedicated to the great task remaining before us—that from
these honored dead we take increased devotion to that cause for which
they gave the last full measure of devotion—that we here highly
resolve that these dead shall not have died in vain—that this nation,
under God, shall have a new birth of freedom—and that government of
the people, by the people, for the people, shall not perish from the
earth."""

def lookup(d, w):
    s = ''
    if not w in d:
        s = '\'{}\' did not occur.'.format(w)
    elif d[w] > 1:
        s = '\'{}\' occured {} times.'.format(w, d[w])
    else:
        s = '\'{}\' occured once.'.format(w)
    return s

def main():
    w = [x.lower() for x in re.findall('\w+', s)]
    c = collections.Counter(w)
    f = c.most_common()
    print(f)
    print('The most common word was \'{}\' and it occurred {} times.'.format(f[0][0], f[0][1]))
    print('The second most common word was \'{}\' and it occurred {} times.'.format(f[1][0], f[1][1]))

    d = dict(f)

    print(lookup(d, 'zzz'))
    print(lookup(d, 'liberty'))
    print(lookup(d, 'shall'))
    return 0

if __name__ == '__main__':
    sys.exit(main())
