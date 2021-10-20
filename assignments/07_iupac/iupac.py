#!/usr/bin/env python3
"""
Author : caro <caro@localhost>
Date   : 2021-10-18
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('SEQ',
                        metavar='SEQ',
                        help='Input sequence(s)',
                        nargs='+')

    parser.add_argument('-o',
                        '--outfile',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    SEQ = list(args.SEQ)
    # print(SEQ)

    IUPAC_Table = {
        "A": "A",
        "T": "T",
        "G": "G",
        "C": "C",
        "U": "U",
        "R": "[AG]",
        "Y": "[CT]",
        "S": "[GC]",
        "W": "[AT]",
        "K": "[GT]",
        "M": "[AC]",
        "B": "[CGT]",
        "D": "[AGT]",
        "H": "[ACT]",
        "V": "[ACG]",
        "N": "[ACGT]"
    }

    for seq in SEQ:
        translation = ""
        Sequence = ""
        for char in seq:
            # print(char)
            if char.upper() in IUPAC_Table:
                translation += IUPAC_Table.get(char)
                Sequence += char
            else:
                translation += '-'
                Sequence += char.lower()
        print(Sequence, translation, file=args.outfile)

    if args.outfile != sys.stdout:
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
