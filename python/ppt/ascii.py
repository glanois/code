"""
usage: ascii.py [-h] [-l]

Prints an ASCII table similar to "man ascii"

options:
  -h, --help  show this help message and exit
  -l, --long  Long version of the ASCII table.
"""

import sys
import argparse

long_text = r"""
       Dec   Hex   Char                        Dec   Hex   Char
       ────────────────────────────────────────────────────────────
       0     00    NUL '\0' (null character)   64    40    @
       1     01    SOH (start of heading)      65    41    A
       2     02    STX (start of text)         66    42    B
       3     03    ETX (end of text)           67    43    C
       4     04    EOT (end of transmission)   68    44    D
       5     05    ENQ (enquiry)               69    45    E
       6     06    ACK (acknowledge)           70    46    F
       7     07    BEL '\a' (bell)             71    47    G
       8     08    BS  '\b' (backspace)        72    48    H
       9     09    HT  '\t' (horizontal tab)   73    49    I
       10    0A    LF  '\n' (new line)         74    4A    J
       11    0B    VT  '\v' (vertical tab)     75    4B    K
       12    0C    FF  '\f' (form feed)        76    4C    L
       13    0D    CR  '\r' (carriage ret)     77    4D    M
       14    0E    SO  (shift out)             78    4E    N
       15    0F    SI  (shift in)              79    4F    O
       16    10    DLE (data link escape)      80    50    P
       17    11    DC1 (device control 1)      81    51    Q
       18    12    DC2 (device control 2)      82    52    R
       19    13    DC3 (device control 3)      83    53    S
       20    14    DC4 (device control 4)      84    54    T
       21    15    NAK (negative ack.)         85    55    U
       22    16    SYN (synchronous idle)      86    56    V
       23    17    ETB (end of trans. blk)     87    57    W
       24    18    CAN (cancel)                88    58    X
       25    19    EM  (end of medium)         89    59    Y
       26    1A    SUB (substitute)            90    5A    Z
       27    1B    ESC (escape)                91    5B    [
       28    1C    FS  (file separator)        92    5C    \  '\\'
       29    1D    GS  (group separator)       93    5D    ]
       30    1E    RS  (record separator)      94    5E    ^
       31    1F    US  (unit separator)        95    5F    _
       32    20    SPACE                       96    60    `
       33    21    !                           97    61    a
       34    22    "                           98    62    b
       35    23    #                           99    63    c
       36    24    $                           100   64    d
       37    25    %                           101   65    e
       38    26    &                           102   66    f
       39    27    '                           103   67    g
       40    28    (                           104   68    h
       41    29    )                           105   69    i
       42    2A    *                           106   6A    j
       43    2B    +                           107   6B    k
       44    2C    ,                           108   6C    l
       45    2D    -                           109   6D    m
       46    2E    .                           110   6E    n
       47    2F    /                           111   6F    o
       48    30    0                           112   70    p
       49    31    1                           113   71    q
       50    32    2                           114   72    r
       51    33    3                           115   73    s
       52    34    4                           116   74    t
       53    35    5                           117   75    u
       54    36    6                           118   76    v
       55    37    7                           119   77    w
       56    38    8                           120   78    x
       57    39    9                           121   79    y
       58    3A    :                           122   7A    z
       59    3B    ;                           123   7B    {
       60    3C    <                           124   7C    |
       61    3D    =                           125   7D    }
       62    3E    >                           126   7E    ~
       63    3F    ?                           127   7F    DEL"""
                                                    
short_text = r"""
          2 3 4 5 6 7
        -------------
       0:   0 @ P ` p
       1: ! 1 A Q a q
       2: " 2 B R b r
       3: # 3 C S c s
       4: $ 4 D T d t
       5: % 5 E U e u
       6: & 6 F V f v
       7: ' 7 G W g w
       8: ( 8 H X h x
       9: ) 9 I Y i y
       A: * : J Z j z
       B: + ; K [ k {
       C: , < L \ l |
       D: - = M ] m }
       E: . > N ^ n ~
       F: / ? O _ o DEL"""


def main(options):
    if options.long:
        print(long_text)
    else:
        print(short_text)
    return 0


def get_parser():
    parser = argparse.ArgumentParser(
        description="Prints an ASCII table similar to \"man ascii\".")
    parser.add_argument(
        '-l',
        '--long',
        dest='long',
        help='Long version of the ASCII table.',
        action='store_true',
        default=False)
    return parser


if __name__ == '__main__':
    parser = get_parser()
    options = parser.parse_args()
    sys.exit(main(options))
