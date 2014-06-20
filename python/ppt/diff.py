import sys, optparse
import itertools

from difflib import Differ, SequenceMatcher

class POSIXDiffer(Differ):
    """
    This class produces differences in the POSIX default format 
    (see http://www.unix.com/man-page/POSIX/1posix/diff/),
    which is the same as the Gnu diff "normal format"
    (see http://www.gnu.org/software/diffutils/manual/diffutils.html#Normal).
    """

    def compare(self, a, b):
        cruncher = SequenceMatcher(self.linejunk, a, b)
        for tag, alo, ahi, blo, bhi in cruncher.get_opcodes():
            if alo == ahi:
                f1 = '%d' % alo
            elif alo+1 == ahi:
                f1 = '%d' % (alo+1)
            else:
                f1 = '%d,%d' % (alo+1, ahi)

            if blo == bhi:
                f2 = '%d' % blo
            elif blo+1 == bhi:
                f2 = '%d' % (blo+1)
            else:
                f2 = '%d,%d' % (blo+1, bhi)

            if tag == 'replace':
                g = itertools.chain([ '%sc%s\n' % (f1, f2) ], self._my_plain_replace(a, alo, ahi, b, blo, bhi))
            elif tag == 'delete':
                g = itertools.chain([ '%sd%s\n' % (f1, f2) ], self._dump('<', a, alo, ahi))
            elif tag == 'insert':
                g = itertools.chain([ '%sa%s\n' % (f1, f2) ], self._dump('>', b, blo, bhi))
            elif tag == 'equal':
                g = []
            else:
                raise ValueError, 'unknown tag %r' % (tag,)

            for line in g:
                yield line

    def _my_plain_replace(self, a, alo, ahi, b, blo, bhi):
        assert alo < ahi and blo < bhi
        first  = self._dump('<', a, alo, ahi)
        second = self._dump('>', b, blo, bhi)

        for g in first, '---\n', second:
            for line in g:
                yield line


def pdiff(a, b):
    """
    Compare `a` and `b` (lists of strings); return a POSIX/Gnu "normal format" diff.
    """
    return POSIXDiffer().compare(a, b)


def main():
    """
    This program is based on Python's difflib sample program, Tools\Scripts\diff.py.

    It produces differences in the POSIX format.

    See http://www.unix.com/man-page/POSIX/1posix/diff/
    """

    usage = "usage: %prog file1 file2"
    parser = optparse.OptionParser(usage)
    (options, args) = parser.parse_args()

    if len(args) == 0:
        parser.print_help()
        sys.exit(1)
    if len(args) != 2:
        parser.print_help()

    file1, file2 = args

    file1lines = open(file1, 'U').readlines()
    file2lines = open(file2, 'U').readlines()

    diff = pdiff(file1lines, file2lines)

    sys.stdout.writelines(diff)

if __name__ == '__main__':
    main()
